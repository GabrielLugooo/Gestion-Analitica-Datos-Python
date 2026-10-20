"""Build a multi-sheet XLSX without third-party packages."""
import csv, json, re, zipfile
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'processed'
DEST=ROOT/'Henry_Datawarehouse.xlsx'
SHEETS=[('Ventas','fact_weekly_sales.csv'),('Contexto_Tienda_Semana','fact_store_features.csv'),('Tiendas','dim_store.csv'),('Departamentos','dim_department.csv'),('Calendario','dim_date.csv'),('KPIs','kpis.json')]
def col_letter(n):
    out=''
    while n:
        n,rem=divmod(n-1,26);out=chr(65+rem)+out
    return out
def esc(v):return escape(str(v),{'"':'&quot;'})
def worksheet_xml(rows):
    yield '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>'
    for ri,row in enumerate(rows,1):
        yield f'<row r="{ri}">'
        for ci,value in enumerate(row,1):
            if value is None or value=='':continue
            ref=f'{col_letter(ci)}{ri}'
            if isinstance(value,(int,float)) and not isinstance(value,bool):
                yield f'<c r="{ref}"><v>{value}</v></c>'
            else:
                yield f'<c r="{ref}" t="inlineStr"><is><t xml:space="preserve">{esc(value)}</t></is></c>'
        yield '</row>'
    yield '</sheetData></worksheet>'
def read_rows(filename):
    with (OUT/filename).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.reader(f))
def kpi_rows():
    d=json.loads((OUT/'kpis.json').read_text(encoding='utf-8'))
    rows=[['Indicador','Valor']]
    def walk(prefix,value):
        if isinstance(value,dict):
            for k,v in value.items():walk(f'{prefix}.{k}' if prefix else k,v)
        else:rows.append([prefix,value])
    for k,v in d.items():walk(k,v)
    return rows
with zipfile.ZipFile(DEST,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    z.writestr('[Content_Types].xml','''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'''+''.join(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(1,len(SHEETS)+1))+'</Types>')
    z.writestr('_rels/.rels','''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>''')
    sheets=''.join(f'<sheet name="{name}" sheetId="{i}" r:id="rId{i}"/>' for i,(name,_) in enumerate(SHEETS,1))
    z.writestr('xl/workbook.xml',f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>{sheets}</sheets></workbook>')
    rels=''.join(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>' for i in range(1,len(SHEETS)+1))
    z.writestr('xl/_rels/workbook.xml.rels',f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>')
    for i,(name,file) in enumerate(SHEETS,1):
        rows=kpi_rows() if file=='kpis.json' else read_rows(file)
        z.writestr(f'xl/worksheets/sheet{i}.xml',''.join(worksheet_xml(rows)))
print(DEST)
