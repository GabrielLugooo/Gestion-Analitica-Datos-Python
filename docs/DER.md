# Modelo entidad-relación

```mermaid
erDiagram
    DIM_LOCATION ||--o{ DIM_STORE : ubica
    DIM_STORE ||--o{ FACT_WEEKLY_SALES : vende
    DIM_DEPARTMENT ||--o{ FACT_WEEKLY_SALES : clasifica
    DIM_DATE ||--o{ FACT_WEEKLY_SALES : ocurre_en
    DIM_STORE ||--o{ FACT_STORE_FEATURES : contextualiza
    DIM_DATE ||--o{ FACT_STORE_FEATURES : contextualiza

    DIM_LOCATION {
        string Location PK
    }
    DIM_STORE {
        int Store PK
        string Type
        decimal Size_raw
        string Location FK
    }
    DIM_DEPARTMENT {
        int Dept PK
    }
    DIM_DATE {
        date Date PK
        int Year
        int Month
        int Quarter
        int ISO_Week
        boolean IsHoliday
    }
    FACT_WEEKLY_SALES {
        int Store PK,FK
        int Dept PK,FK
        date Date PK,FK
        decimal Weekly_Sales
    }
    FACT_STORE_FEATURES {
        int Store PK,FK
        date Date PK,FK
        decimal Temperature
        decimal Fuel_Price
        decimal CPI
        decimal Unemployment
        decimal MarkDown1
        decimal MarkDown2
        decimal MarkDown3
        decimal MarkDown4
        decimal MarkDown5
    }
```

## Granularidad y relaciones

`FACT_WEEKLY_SALES` tiene una fila por tienda, departamento y semana (`Store + Dept + Date`). `FACT_STORE_FEATURES` tiene una fila por tienda y semana (`Store + Date`): son variables contextuales comunes a todos los departamentos de esa tienda y fecha. Mantenerlas en una tabla aparte evita duplicar sus valores al unirlas a ventas de muchos departamentos.

`DIM_STORE` contiene la ubicación observada en `sales.csv`, el tipo y el tamaño original. El tamaño se mantiene como `Size_raw` por la discrepancia de escala detectada frente a las unidades esperadas; confirmar la unidad antes de darle una interpretación. `DIM_LOCATION` puede derivarse como catálogo de ubicaciones distintas. La ubicación no aparece en `stores.csv`, por lo que fue recuperada de `sales.csv` y no es una dimensión independiente de fuente.

Las claves compuestas de ambas tablas de hechos se validan como únicas. `IsHoliday` se conserva en ambas fuentes para detectar desacuerdos; en una versión productiva debe provenir de un calendario de fechas validado.
