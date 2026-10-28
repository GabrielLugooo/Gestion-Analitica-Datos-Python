# Proyecto Integrador de Gestión Analítica de Datos con Python

Proyecto integrador de retail: carga, calidad de datos, modelado dimensional, exploración y KPIs a partir de ventas semanales de tiendas y departamentos.

## Entregables principales

- `Informe_final.html`: Informe final en HTML.
- `src/run_analysis.py`: Proceso reproducible.
- `src/build_warehouse_xlsx.py`: Proceso reproducible.
- `sql/schema.sql`: El script reproducible en el repositorio.
- `docs/DER.md`: Modelo de Entidad-Relacion.
- `docs/Paso_a_Paso.md`: Pasos del proyecto y como repetirlo.
- `docs/Informe_Final.md`: Este informe.
- `data/raw/`: Fuentes intactas.
- `data/processed/`: CSV limpios derivados.
- `data/Datawarehouse.xlsx`: Tablas analíticas y KPIs en hojas separadas.

## Reproducir en Windows / VS Code

1. Abrir esta carpeta con VS Code.
2. Abrir Terminal → New Terminal.
3. Ejecutar `python src/run_analysis.py` desde la carpeta del proyecto.
4. Ejecutar `python src/build_warehouse_xlsx.py` para reconstruir el Excel.
5. Revisar `data/processed/` y abrir `Informe_final.html`.

El script usa solo la biblioteca estándar de Python. Normaliza las fechas `D/M/YYYY` luego de comprobar que todas las semanas observadas terminan en viernes; preserva las ventas negativas y los ceros, transforma faltantes codificados como `NA` en nulos con banderas, y conserva valores originales junto a las normalizaciones sugeridas.

## Hallazgo de calidad de fuente

Muchos valores de `Fuel_Price` y `Unemployment` aparecen con el separador decimal perdido. El análisis guarda el dato de origen, crea columnas limpias dividiendo por 1.000 cuando el valor excede los umbrales documentados y añade una marca de auditoría. La escala de `Size` se conserva sin reinterpretar. El workbook resuelto del material también presenta columnas con escalas alteradas; ver `docs/Informe_Final.md`.

## Fuente y uso

El proyecto documenta el análisis de esta copia, no realiza una evaluación causal ni un pronóstico de demanda.
