<img align="center" src="https://i.imgur.com/gJzyKft.png" alt="gabriellugo" />

# GESTION ANALITICA DE DATOS CON PYTHON

<a href="https://github.com/GabrielLugooo/Gestion-Analitica-Datos-Python/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Analitica%20Datos%20Pyton%20Español-000000" alt="Analitica Datos Python Español" /></a>
<a href="https://github.com/GabrielLugooo/Gestion-Analitica-Datos-Python/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Analitica%20Datos%20Python%20Inglés-green" alt="Analitica Datos Python Inglés" /></a>

## Objetivos

Este es un proyecto integrador de retail: carga, calidad de datos, modelado dimensional, exploración y KPIs a partir de ventas semanales de tiendas y departamentos.

# Habilidades Aprendidas

- Importación y análisis de datos con `Python`.
- Lectura y manipulación de archivos `.csv` y `.xlsx`.
- Limpieza y preparación de datos para el análisis.
- Uso de Pandas para filtrar, agrupar y resumir información.
- Exploración de datos de ventas, tiendas y características semanales.
- Cálculo de indicadores y estadísticas descriptivas.
- Análisis de ventas por período, tienda, departamento y días festivos.
- Comparación de ventas con variables como temperatura, combustible, IPC y desempleo.
- Creación de visualizaciones para comunicar hallazgos.
- Documentación de resultados, criterios de análisis y limitaciones.

## Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Pandas-000000?logo=pandas&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Jupyter-000000?logo=jupyter&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Matplotlib-000000?logo=matplotlib&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Seaborn-000000?logo=seaborn&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Microsoft%20Excel-000000?logo=microsoftexcel&logoSize=auto)
![Static Badge](https://img.shields.io/badge/CSV-000000?logo=files&logoSize=auto)
![Static Badge](https://img.shields.io/badge/GitHub-000000?logo=github&logoSize=auto)

- `Python` (lenguaje utilizado para el análisis)
- `Pandas` (manipulación y análisis de datos)
- `Jupyter Notebook` (desarrollo y documentación del análisis)
- `Matplotlib` y `Seaborn` (visualización de datos)
- Archivos `.csv` y `.xlsx` (fuentes de datos)
- `Git` y `GitHub` (control de versiones y publicación del proyecto)

## Proyecto

### Vista Previa

<img align="center" src="https://i.imgur.com/cgx9LDP.jpeg" alt="Python_Analytics_01" />
<img align="center" src="https://i.imgur.com/bLLQYZW.jpeg" alt="Python_Analytics_02" />
<img align="center" src="https://i.imgur.com/MlZYKis.jpeg" alt="Python_Analytics_03" />
<img align="center" src="https://i.imgur.com/wL4fEnE.jpeg" alt="Python_Analytics_04" />
<img align="center" src="https://i.imgur.com/rnothmD.jpeg" alt="Python_Analytics_05" />
<img align="center" src="https://i.imgur.com/x7p0Wr7.jpeg" alt="Python_Analytics_06" />

### Contenidos

- `Informe_Final.html`: Informe final en HTML.
- `src/run_analysis.py`: Proceso reproducible.
- `src/build_warehouse_xlsx.py`: Proceso reproducible.
- `sql/schema.sql`: El script reproducible en el repositorio.
- `docs/DER.md`: Modelo de Entidad-Relacion.
- `docs/Paso_a_Paso.md`: Pasos del proyecto y como repetirlo.
- `docs/Informe_Final.md`: Informe final en Markdown.
- `data/raw/`: Fuentes intactas.
- `data/processed/`: CSV limpios derivados.
- `data/Datawarehouse.xlsx`: Tablas analíticas y KPIs en hojas separadas.

### Reproducir en Windows / VS Code

1. Abrir esta carpeta con VS Code.
2. Abrir Terminal → New Terminal.
3. Ejecutar `python src/run_analysis.py` desde la carpeta del proyecto.
4. Ejecutar `python src/build_warehouse_xlsx.py` para reconstruir el Excel.
5. Revisar `data/processed/` y abrir `Informe_final.html`.

El script usa solo la biblioteca estándar de Python. Normaliza las fechas `D/M/YYYY` luego de comprobar que todas las semanas observadas terminan en viernes; preserva las ventas negativas y los ceros, transforma faltantes codificados como `NA` en nulos con banderas, y conserva valores originales junto a las normalizaciones sugeridas.

### Hallazgo de calidad de fuente

Muchos valores de `Fuel_Price` y `Unemployment` aparecen con el separador decimal perdido. El análisis guarda el dato de origen, crea columnas limpias dividiendo por 1.000 cuando el valor excede los umbrales documentados y añade una marca de auditoría. La escala de `Size` se conserva sin reinterpretar. El workbook resuelto del material también presenta columnas con escalas alteradas; ver `docs/Informe_Final.md`.

## Limitaciones

El proyecto documenta el análisis de esta copia, no realiza una evaluación causal ni un pronóstico de demanda.

---

<h3 align="left">Conecta Conmigo</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=1" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Licencia-MIT-green" alt="Licencia MIT " /></a>