# PI de Gestión Analítica de Datos

Proyecto integrador de retail: carga, calidad de datos, modelado dimensional, exploración y KPIs a partir de ventas semanales de tiendas y departamentos.

## Entregables principales

- `Informe_final.html`: informe listo para leer y compartir.
- `docs/INFORME_FINAL.md`: versión editable del informe con todos los pasos, resultados y limitaciones.
- `Henry_Datawarehouse.xlsx`: libro de seis hojas: ventas, contexto semanal, tiendas, departamentos, calendario y KPIs.
- `docs/PASO_A_PASO.md`: explicación del flujo y las fórmulas.
- `docs/DER.md`: modelo entidad-relación, granularidades y relaciones.
- `sql/schema.sql`: propuesta de tablas relacionales.
- `src/run_analysis.py`: proceso de limpieza conservadora, creación de tablas analíticas y cálculo de KPIs.
- `src/build_warehouse_xlsx.py`: genera el libro Excel con el resultado del análisis.
- `data/raw/`: CSV originales recibidos; `data/processed/`: tablas derivadas y métricas.

## Reproducir en Windows / VS Code

1. Abrir esta carpeta con VS Code.
2. Abrir Terminal → New Terminal.
3. Ejecutar `python src/run_analysis.py` desde la carpeta del proyecto.
4. Ejecutar `python src/build_warehouse_xlsx.py` para reconstruir el Excel.
5. Revisar `data/processed/` y abrir `Informe_final.html`.

El script usa solo la biblioteca estándar de Python. Normaliza las fechas `D/M/YYYY` luego de comprobar que todas las semanas observadas terminan en viernes; preserva las ventas negativas y los ceros, transforma faltantes codificados como `NA` en nulos con banderas, y conserva valores originales junto a las normalizaciones sugeridas.

## Hallazgo de calidad de fuente

Muchos valores de `Fuel_Price` y `Unemployment` aparecen con el separador decimal perdido. El análisis guarda el dato de origen, crea columnas limpias dividiendo por 1.000 cuando el valor excede los umbrales documentados y añade una marca de auditoría. La escala de `Size` se conserva sin reinterpretar. El workbook resuelto del material también presenta columnas con escalas alteradas; ver `docs/INFORME_FINAL.md`.

## Fuente y uso

Archivos educativos proporcionados en el material del curso de Henry. El proyecto documenta el análisis de esta copia, no realiza una evaluación causal ni un pronóstico de demanda.
