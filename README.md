<img align="center" src="https://i.imgur.com/gJzyKft.png" alt="gabriellugo" />

# ANALYTICAL DATA MANAGEMENT WITH PYTHON

<a href="https://github.com/GabrielLugooo/Gestion-Analitica-Datos-Python/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Data%20Analytics%20with%20Python%20English-000000" alt="Data Analytics with Python English" /></a>
<a href="https://github.com/GabrielLugooo/Gestion-Analitica-Datos-Python/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Data%20Analytics%20with%20Python%20Spanish-green" alt="Data Analytics with Python Spanish" /></a>

## Objectives

This is a retail-focused integrative project covering data loading, data quality, dimensional modeling, data exploration, and the development of KPIs based on weekly sales data from various stores and departments.

# Skills Acquired

- Data import and analysis using `Python`.
- Reading and manipulating `.csv` and `.xlsx` files.
- Data cleaning and preparation for analysis.
- Using Pandas to filter, group, and summarize information.
- Exploring data related to sales, stores, and weekly characteristics.
- Calculating key performance indicators (KPIs) and descriptive statistics.
- Analyzing sales by period, store, department, and holidays.
- Comparing sales against variables such as temperature, fuel prices, the Consumer Price Index (CPI), and unemployment rates.
- Creating visualizations to communicate findings.
- Documenting results, analysis criteria, and project limitations. 

## Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Pandas-000000?logo=pandas&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Jupyter-000000?logo=jupyter&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Matplotlib-000000?logo=matplotlib&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Seaborn-000000?logo=seaborn&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Microsoft%20Excel-000000?logo=microsoftexcel&logoSize=auto)
![Static Badge](https://img.shields.io/badge/CSV-000000?logo=files&logoSize=auto)
![Static Badge](https://img.shields.io/badge/GitHub-000000?logo=github&logoSize=auto)

- `Python` (language used for analysis)
- `Pandas` (data manipulation and analysis)
- `Jupyter Notebook` (analysis development and documentation)
- `Matplotlib` and `Seaborn` (data visualization)
- `.csv` and `.xlsx` files (data sources)
- `Git` and `GitHub` (version control and project publishing)

## Project

### Preview

<img align="center" src="https://i.imgur.com/cgx9LDP.jpeg" alt="Python_Analytics_01" />
<img align="center" src="https://i.imgur.com/bLLQYZW.jpeg" alt="Python_Analytics_02" />
<img align="center" src="https://i.imgur.com/MlZYKis.jpeg" alt="Python_Analytics_03" />
<img align="center" src="https://i.imgur.com/wL4fEnE.jpeg" alt="Python_Analytics_04" />
<img align="center" src="https://i.imgur.com/rnothmD.jpeg" alt="Python_Analytics_05" />
<img align="center" src="https://i.imgur.com/x7p0Wr7.jpeg" alt="Python_Analytics_06" />

### Contents

- `Informe_Final.html`: Final report in HTML format.
- `src/run_analysis.py`: Reproducible process.
- `src/build_warehouse_xlsx.py`: Reproducible process.
- `sql/schema.sql`: Reproducible script included in the repository.
- `docs/DER.md`: Entity-Relationship Model (ERM).
- `docs/Paso_a_Paso.md`: Project steps and instructions for reproduction.
- `docs/Informe_Final.md`: Final report in Markdown format.
- `data/raw/`: Original, unaltered data sources.
- `data/processed/`: Cleaned CSV files.
- `data/Datawarehouse.xlsx`: Analytical tables and KPIs in separate sheets.

### Reproduction on Windows / VS Code

1. Open this folder in VS Code.
2. Open Terminal → New Terminal.
3. Run `python src/run_analysis.py` from the project folder.
4. Run `python src/build_warehouse_xlsx.py` to rebuild the Excel file.
5. Check the `data/processed/` directory and open `Informe_final.html`. The script uses only the Python standard library. It normalizes dates in `D/M/YYYY` format—after verifying that all observed weeks end on a Friday—preserves negative sales figures and zeros, converts missing values ​​(encoded as `NA`) into nulls accompanied by flags, and retains the original values ​​alongside the suggested normalized versions.

## Data Quality Finding

Many values ​​for `Fuel_Price` and `Unemployment` appear to be missing their decimal separator. The analysis preserves the original data, creates cleaned columns by dividing values ​​by 1,000 whenever they exceed documented thresholds, and adds an audit flag. The scale of the `Size` variable is preserved as-is, without reinterpretation. The completed workbook included in the materials also contains columns with altered scales; please refer to `docs/Informe_Final.md`.

## Limitations

This project documents the analysis of this specific dataset; it does not perform a causal assessment or demand forecasting.

---

<h3 align="left">Connect With Me</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/gabriellugooo_" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="gabriellugooo_" height="40" width="40" /></a>
<a href="https://x.com/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugooo" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20Views&color=green&base=1" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Licence-MIT-green" alt="MIT License" /></a>