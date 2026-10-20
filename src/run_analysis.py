"""Limpieza conservadora, modelado y KPIs para el PI de Gestión Analítica de Datos."""
from __future__ import annotations
import csv, json, statistics
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def read_csv(name):
    with (RAW / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def parse_date(s):
    # En los archivos las fechas vienen como D/M/YYYY; todas las fechas
    # distintas resultan viernes al interpretarlas así.
    return datetime.strptime(s.strip(), "%d/%m/%Y").date()

def clean_text(v):
    if v is None: return ""
    v = v.strip()
    return "" if v.upper() in {"", "NA", "N/A", "NULL", "NONE"} else v

def write_csv(path, rows, headers):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w=csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

sales_raw=read_csv("sales.csv")
features_raw=read_csv("features.csv")
stores_raw=read_csv("stores.csv")

sales=[]
for r in sales_raw:
    sales.append({"Store":str(int(float(r["Store"]))), "Dept":str(int(float(r["Dept"]))),
                  "Date":parse_date(r["Date"]).isoformat(), "Weekly_Sales":Decimal(r["Weekly_Sales"].strip()),
                  "IsHoliday":clean_text(r["IsHoliday"]).upper()=="TRUE", "Location":clean_text(r["Location"])})
features=[]
for r in features_raw:
    row={"Store":str(int(float(r["Store"]))), "Date":parse_date(r["Date"]).isoformat(),
         "IsHoliday":clean_text(r["IsHoliday"]).upper()=="TRUE"}
    for c in ["Temperature","Fuel_Price","MarkDown1","MarkDown2","MarkDown3","MarkDown4","MarkDown5","CPI","Unemployment"]:
        row[c]=clean_text(r[c])
        row[c+"_is_missing"]=row[c]==""
    row["Fuel_Price_scale_suspect"]=bool(row["Fuel_Price"] and Decimal(row["Fuel_Price"])>10)
    row["Unemployment_scale_suspect"]=bool(row["Unemployment"] and Decimal(row["Unemployment"])>20)
    row["Fuel_Price_clean"]=str(Decimal(row["Fuel_Price"])/1000 if row["Fuel_Price_scale_suspect"] else Decimal(row["Fuel_Price"])) if row["Fuel_Price"] else ""
    row["Unemployment_clean"]=str(Decimal(row["Unemployment"])/1000 if row["Unemployment_scale_suspect"] else Decimal(row["Unemployment"])) if row["Unemployment"] else ""
    features.append(row)
stores=[{"Store":str(int(float(r["Store"]))),"Type":clean_text(r["Type"]),"Size_raw":clean_text(r["Size"])} for r in stores_raw]

# Quality assertions on keys and referential coverage
sales_key=[(r["Store"],r["Dept"],r["Date"]) for r in sales]
feature_key=[(r["Store"],r["Date"]) for r in features]
assert len(sales_key)==len(set(sales_key)), "La granularidad Store-Dept-Date no es única"
assert len(feature_key)==len(set(feature_key)), "La granularidad Store-Date no es única"
store_set={r["Store"] for r in stores}
assert {r["Store"] for r in sales} <= store_set
assert {(r["Store"],r["Date"]) for r in sales} <= set(feature_key)

# Export fact tables and dimensions as CSV: portable warehouse deliverables.
sales_export=[{**r,"Weekly_Sales":str(r["Weekly_Sales"]),"IsHoliday":str(r["IsHoliday"]).upper()} for r in sales]
write_csv(OUT/"fact_weekly_sales.csv",sales_export,["Store","Dept","Date","Weekly_Sales","IsHoliday","Location"])
feature_headers=["Store","Date","Temperature","Fuel_Price","MarkDown1","MarkDown2","MarkDown3","MarkDown4","MarkDown5","CPI","Unemployment","IsHoliday"] + [c+"_is_missing" for c in ["MarkDown1","MarkDown2","MarkDown3","MarkDown4","MarkDown5"]] + ["Fuel_Price_clean","Unemployment_clean","Fuel_Price_scale_suspect","Unemployment_scale_suspect"]
feature_export=[{**r,"IsHoliday":str(r["IsHoliday"]).upper()} for r in features]
write_csv(OUT/"fact_store_features.csv",feature_export,feature_headers)
loc_by_store=defaultdict(Counter)
for r in sales: loc_by_store[r["Store"]][r["Location"]]+=1
store_export=[]
for r in stores:
    store_export.append({**r,"Location":loc_by_store[r["Store"]].most_common(1)[0][0]})
write_csv(OUT/"dim_store.csv",store_export,["Store","Type","Size_raw","Location"])
write_csv(OUT/"dim_department.csv",[{"Dept":d} for d in sorted({r["Dept"] for r in sales},key=int)],["Dept"])
dates=sorted({r["Date"] for r in sales}|{r["Date"] for r in features})
holiday_date_set={r["Date"] for r in sales if r["IsHoliday"]}
holiday_by_date={d:d in holiday_date_set for d in dates}
write_csv(OUT/"dim_date.csv",[{"Date":d,"Year":d[:4],"Month":str(int(d[5:7])),"Quarter":"Q"+str((int(d[5:7])-1)//3+1),"ISO_Week":str(datetime.strptime(d,"%Y-%m-%d").isocalendar().week),"Weekday":"Friday","IsHoliday":str(holiday_by_date[d]).upper()} for d in dates],["Date","Year","Month","Quarter","ISO_Week","Weekday","IsHoliday"])

# KPIs: dollar sign omitted because the supplied files do not declare currency.
markdown_cols=["MarkDown1","MarkDown2","MarkDown3","MarkDown4","MarkDown5"]
missing={c:sum(r[c+"_is_missing"] for r in features) for c in markdown_cols}
total=sum(r["Weekly_Sales"] for r in sales)
by_week=defaultdict(Decimal); by_dept=defaultdict(Decimal); by_store=defaultdict(Decimal)
for r in sales:
    by_week[(r["Date"],r["IsHoliday"])]+=r["Weekly_Sales"]
    by_dept[r["Dept"]]+=r["Weekly_Sales"]
    by_store[r["Store"]]+=r["Weekly_Sales"]
holiday=[v for (d,h),v in by_week.items() if h]
regular=[v for (d,h),v in by_week.items() if not h]
ordered_dept=sorted(by_dept.items(),key=lambda x:x[1],reverse=True)
ordered_store=sorted(by_store.items(),key=lambda x:x[1],reverse=True)
mean_h=float(statistics.mean(holiday)); mean_r=float(statistics.mean(regular))
metric={
 "sales_rows":len(sales),"stores":len(store_set),"departments":len({r["Dept"] for r in sales}),"locations":len({r["Location"] for r in sales}),
 "date_start":min(r["Date"] for r in sales),"date_end":max(r["Date"] for r in sales),"sales_weeks":len({r["Date"] for r in sales}),
 "total_weekly_sales_sum":round(float(total),2),"mean_store_department_week_sales":round(float(statistics.mean([r["Weekly_Sales"] for r in sales])),2),
 "median_store_department_week_sales":round(float(statistics.median([r["Weekly_Sales"] for r in sales])),2),
 "negative_sales_rows":sum(r["Weekly_Sales"]<0 for r in sales),"zero_sales_rows":sum(r["Weekly_Sales"]==0 for r in sales),
 "holiday_weeks":len(holiday),"regular_weeks":len(regular),"holiday_mean_total_sales_per_week":round(mean_h,2),"regular_mean_total_sales_per_week":round(mean_r,2),
 "holiday_vs_regular_mean_change_pct":round((mean_h/mean_r-1)*100,2),
 "top_department_by_sales":{"Dept":ordered_dept[0][0],"sales":round(float(ordered_dept[0][1]),2)},
 "top_store_by_sales":{"Store":ordered_store[0][0],"sales":round(float(ordered_store[0][1]),2)},
 "markdown_missing_rows_by_column":missing,"fuel_price_scale_suspect_rows":sum(r["Fuel_Price_scale_suspect"] for r in features),
 "unemployment_scale_suspect_rows":sum(r["Unemployment_scale_suspect"] for r in features),
 "duplicate_sales_grain":len(sales_key)-len(set(sales_key)),"duplicate_features_grain":len(feature_key)-len(set(feature_key)),
 "sales_keys_without_store_features":len({(r["Store"],r["Date"]) for r in sales}-set(feature_key))
}
(OUT/"kpis.json").write_text(json.dumps(metric,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps(metric,indent=2,ensure_ascii=False))






