# Informe final del Proyecto Integrador

## Descubriendo el éxito comercial con datos de ventas minoristas

**Curso:** Gestión Analítica de Datos — Henry  
**Alcance:** 45 tiendas, 81 departamentos y 95 semanas con ventas entre el 7 de enero de 2011 y el 26 de octubre de 2012.

## Resumen ejecutivo

Se consolidaron los tres archivos de origen (`sales.csv`, `features.csv` y `stores.csv`) en un modelo analítico con dos tablas de hechos y dimensiones de tienda, departamento, fecha y ubicación. El nivel de detalle de ventas suma **4.448.332.866,70 unidades monetarias** (la fuente no especifica moneda); el promedio por tienda, departamento y semana es 15.836,51. El departamento 92 acumula el mayor total (328,1 millones) y la tienda 4 el mayor total por sucursal (203,9 millones).

Las seis semanas etiquetadas como feriado en el período de ventas promedian 50,85 millones por semana, frente a 46,55 millones en las otras 89 semanas: una diferencia descriptiva de **+9,22 %**. La muestra de feriados es pequeña y no permite afirmar que el feriado cause el aumento. Además, hay valores económicos con separadores alterados y casi la mitad de los cinco campos MarkDown falta. Estas limitaciones se mantienen visibles en las tablas de salida.

## 1. Fuente, alcance y granularidad

La presentación de Henry propone consolidar los datasets, limpiar y preparar variables, diseñar el diagrama entidad-relación, crear la base, buscar insights y definir métricas/KPIs. Se revisaron los tres CSV originales y el `Datawarehouse.xlsx` que acompaña el material como ejemplo resuelto.

| Archivo | Filas | Granularidad | Uso |
|---|---:|---|---|
| `sales.csv` | 280.891 | tienda + departamento + semana | Ventas semanales y etiqueta de feriado |
| `features.csv` | 4.680 | tienda + semana | Clima, precios, promociones e indicadores económicos |
| `stores.csv` | 45 | tienda | Tipo y tamaño reportado |

Las ventas cubren 95 semanas consecutivas observadas desde 2011-01-07 hasta 2012-10-26. Las variables de contexto cubren 104 semanas hasta 2012-12-28. El calendario de ventas contiene 12 ubicaciones, 45 tiendas y 81 departamentos. El análisis no extrapola ventas a las nueve semanas posteriores al último registro de ventas.

## 2. Limpieza, normalización y controles

Se preservaron los CSV originales en `data/raw/` y se aplicó un proceso reproducible en `src/run_analysis.py`.

1. **Encabezados y tipos:** se conservaron los nombres de campos; `Store` y `Dept` se normalizaron a enteros en forma de texto para claves consistentes; ventas y campos numéricos se interpretan como números; `IsHoliday` como booleano.
2. **Fechas:** los CSV usan `D/M/YYYY`. Se interpretaron con ese formato y se convirtieron a ISO (`YYYY-MM-DD`). La interpretación queda respaldada por las 104 fechas semanales de `features.csv`, que caen en viernes; las claves de fecha de ventas encuentran correspondencia en features.
3. **Faltantes:** los valores `NA` de MarkDown se convierten en nulos y se agregan columnas `*_is_missing`. No se imputan como cero: “sin dato” no equivale necesariamente a “sin promoción”. La ausencia alcanza entre 42 % y 60 % según el campo.
4. **Escalas numéricas:** 4.233 de 4.680 valores de `Fuel_Price` exceden 10 y 4.289 valores de `Unemployment` exceden 20, mientras que el resto cae en escalas plausibles. Para hacer el análisis comparable, cuando el valor supera esos umbrales se divide por 1.000 y se guarda en `Fuel_Price_clean` o `Unemployment_clean`. Se conserva el valor recibido y se activa `*_scale_suspect`; las columnas originales nunca se sobrescriben. Este patrón indica pérdida del separador decimal. La regla es auditable, pero se recomienda contrastarla con Henry/la fuente original antes de usarla en una decisión operativa.
5. **Tamaño de tiendas:** se conserva como `Size_raw`. La escala/ unidad no puede confirmarse con los archivos disponibles, así que no se usa para conclusiones ni se corrige automáticamente.
6. **Ventas negativas y cero:** se mantienen 895 valores negativos y 48 ceros. Pueden representar devoluciones, ajustes o casos especiales; eliminarlos sin una regla de negocio sesgaría los resultados. Conviene investigarlos con quien conozca la fuente.
7. **Duplicados y relaciones:** no hay duplicados en las granularidades declaradas (`Store + Dept + Date` para ventas y `Store + Date` para features); no faltan claves de tienda ni cruces tienda-fecha. No se detectó una fila de ventas sin tienda-semana de contexto.

### Observación sobre el Excel resuelto de Henry

El libro de ejemplo no debe tomarse como fuente de verdad para todas las columnas: allí `CPI` aparece transformado, por ejemplo 211,4047419 pasa a 2,114047419E9; `Fuel_Price` 2,976 aparece como 2.976 y `Unemployment` 7,742 como 7.742. La versión de entrega se generó desde los CSV iniciales y mantiene por separado valor original, valor corregido e indicador de corrección. Se recomienda entregar esta versión y aclarar el hallazgo si Henry solicita comparar con el ejemplo.

## 3. Modelo entidad-relación y data warehouse

La propuesta separa ventas del contexto semanal porque una observación de `features` aplica a todos los departamentos de la misma tienda y semana. Unirla directamente a cada línea de ventas y luego sumar sus variables duplicaría su peso por cantidad de departamentos.

- `FACT_WEEKLY_SALES`: una fila por tienda, departamento y semana; medida `Weekly_Sales`.
- `FACT_STORE_FEATURES`: una fila por tienda y semana; clima, promociones y variables económicas, con indicadores de faltantes y escalas sospechosas.
- `DIM_STORE`: tipo, tamaño original y ubicación observada en ventas.
- `DIM_DEPARTMENT`: catálogo de departamentos.
- `DIM_DATE`: fecha, año, mes, trimestre, semana ISO, día e indicador de feriado.
- `DIM_LOCATION`: catálogo derivado de códigos de ubicación.

Las claves y relaciones están detalladas en `DER.md`; `schema.sql` contiene una propuesta SQL. El Excel `Henry_Datawarehouse.xlsx` entrega las hojas Ventas, Contexto_Tienda_Semana, Tiendas, Departamentos, Calendario y KPIs; las mismas tablas también están disponibles como CSV en `data/processed/`.

## 4. Insights

- **Concentración por departamento:** el departamento 92 suma 328,1 millones, aproximadamente 7,38 % del total analizado. Le siguen 95 (299,5 millones) y 38 (264,3 millones). Los totales sirven para priorizar revisión, pero no explican margen, inventario ni desempeño por metro cuadrado.
- **Desempeño por tienda:** la tienda 4 suma 203,9 millones (4,58 % del total); la tienda 20 le sigue con 199,7 millones y la tienda 13 con 191,2 millones. Estos totales dependen de la mezcla de departamentos y período observado.
- **Semanas con feriado:** 50,85 millones de venta agregada semanal promedio en 6 semanas marcadas como feriado versus 46,55 millones en 89 semanas ordinarias (+9,22 %). Es una asociación descriptiva; no controla promociones, estacionalidad, composición de tiendas ni cantidad de feriados.
- **Calidad limita el análisis de contexto:** los faltantes de MarkDown y los errores de escala de combustible/desempleo reducen la confiabilidad de correlaciones. No se publican relaciones causales ni una regresión de ventas contra estas variables.

## 5. Métricas y KPIs

| KPI / métrica | Definición | Resultado |
|---|---|---:|
| Venta total observada | Suma de `Weekly_Sales` en todas las filas | 4.448.332.866,70 |
| Venta media por combinación | Promedio de venta por tienda-departamento-semana | 15.836,51 |
| Venta mediana por combinación | Mediana de venta por tienda-departamento-semana | 7.450,22 |
| Venta semanal agregada media en feriados | Promedio de la suma semanal entre tiendas y departamentos | 50.845.825,64 (6 semanas) |
| Venta semanal agregada media sin feriado | Promedio de suma semanal | 46.553.459,69 (89 semanas) |
| Variación descriptiva feriado vs. resto | (media feriado / media no feriado − 1) × 100 | +9,22 % |
| Departamento con mayor venta total | Suma por departamento | 92: 328.105.765,98 |
| Tienda con mayor venta total | Suma por tienda | 4: 203.863.482,57 |
| Filas con venta negativa / cero | Conteos conservados para investigar | 895 / 48 |

La fuente no identifica explícitamente moneda, por eso los valores se presentan sin símbolo. El indicador de feriado compara totales semanales y no ventas medias por tienda o departamento; usa solo las semanas disponibles.

## 6. Conclusiones y próximos pasos

El proyecto permite recorrer el ciclo de análisis: integrar archivos, normalizar fechas y tipos, hacer visibles los faltantes/anomalías, construir un modelo con granularidad explícita y comunicar resultados con KPIs. La mayor prioridad antes de profundizar es validar con Henry los separadores y la unidad de `Size`, además de confirmar qué significan `NA` en MarkDown y las ventas negativas. Una vez confirmadas esas definiciones, el siguiente análisis útil sería comparar cada tienda/departamento consigo mismo a lo largo del tiempo, controlar estacionalidad y promociones, y evaluar un pronóstico separado de este informe descriptivo.

## Archivos de entrega

- `Henry_Datawarehouse.xlsx`: tablas analíticas y KPIs en hojas separadas.
- `Informe_final.html` y este informe Markdown.
- `DER.md`, `schema.sql` y el script reproducible en el repositorio.
- CSV limpios derivados en `data/processed/`; fuentes intactas en `data/raw/`.
