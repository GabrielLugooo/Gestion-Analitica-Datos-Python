# Pasos del proyecto y cómo repetirlo

## Consigna interpretada

Henry pide mostrar el flujo completo: integrar las fuentes, limpiar y preparar datos, diseñar un DER, crear el warehouse, encontrar insights, definir KPIs y comunicar conclusiones. La entrega preparada conserva evidencia y explicaciones de cada fase.

## De la fuente al resultado

1. **Carga:** `data/raw/` contiene los tres CSV recibidos. No se altera la fuente.
2. **Perfil y granularidad:** `sales` tiene grano tienda-departamento-semana; `features`, tienda-semana; `stores`, tienda. Primero se identifican formatos, cobertura y claves.
3. **Limpieza:** convertir fechas a ISO, uniformar claves y booleanos, traducir `NA` a nulo, agregar marcas de faltantes. Investigar valores de escala heterogénea y conservar columnas originales.
4. **Modelo:** mantener una tabla de hechos de ventas y otra de contexto tienda-semana; sumar dimensiones de tienda, departamento, fecha y ubicación.
5. **Warehouse:** ejecutar `python src/run_analysis.py` para generar CSV limpios y KPIs; luego `python src/build_warehouse_xlsx.py` para crear el libro de seis hojas.
6. **Análisis:** definir el período, sumar ventas por semana/departamento/tienda, comparar semanas con/sin feriado y explicar las limitaciones.
7. **Comunicación:** entregar el Excel y el informe HTML/Markdown. El repositorio contiene el detalle técnico y la reproducción.

## Fórmulas principales

- Venta total = `SUM(Weekly_Sales)`.
- Venta media por observación = `AVG(Weekly_Sales)` a grano tienda-departamento-semana.
- Venta agregada semanal = suma de `Weekly_Sales` por fecha.
- Cambio descriptivo feriado = `(promedio de venta agregada en semanas feriado / promedio en semanas sin feriado - 1) * 100`.
- Participación de departamento/tienda = venta del grupo / venta total * 100.

La comparación con feriados es descriptiva. No controla estacionalidad, promociones ni la mezcla de departamentos y no debe leerse como efecto causal.
