# ETL Project: Indicadores Económicos Globales

Este proyecto implementa un flujo ETL completo utilizando Airflow para orquestar la extracción, transformación y carga de datos económicos desde múltiples fuentes. Los datos se almacenan en PostgreSQL y se visualizan a través de Power BI.

---

## Objetivos del Proyecto

- Extraer datos económicos de diferentes fuentes: archivos CSV locales y la API del World Bank.
- Transformar y limpiar los datos.
- Fusionar información para enriquecer el dataset principal.
- Cargar los datos en un modelo dimensional en PostgreSQL.
- Visualizar los indicadores económicos clave: inflación y desempleo.

---

## Herramientas Utilizadas

- **Apache Airflow** – Orquestador del flujo ETL  
- **Python** – Scripts de extracción, transformación y carga  
- **PostgreSQL** – Base de datos destino  
- **Pandas + SQLAlchemy** – Procesamiento de datos  
- **Power BI** – Visualización y análisis  
- **Google Drive API** – Almacenamiento en la nube de archivos finales  

---

## Visualizaciones en Power BI

Los datos cargados en el modelo dimensional (`dim_country`, `dim_time`, `fact_economy`) son usados para generar dashboards con:

- **Gráfico de líneas**: Inflación por país y año  
- **Gráfico de barras**: Países con mayor desempleo en el último año  
- **Gráfico de dona**: Distribución de la inflación por región o país  
- **Tabla resumen**: Indicadores filtrables por país y año

---

## Análisis Exploratorio (EDA)

Incluido un notebook `API_EDA.ipynb` con:

- Histogramas y distribución de inflación y desempleo  
- Boxplots por año y país  
- Correlación entre inflación y desempleo

---

## Flujo ETL

1. **Extracción**  
   - Desde archivo CSV: Datos económicos crudos  
   - Desde API del World Bank: Inflación y desempleo por país y año  

2. **Transformación**  
   - Limpieza y normalización  
   - Conversión de tipos y codificación de países  

3. **Fusión**  
   - Merge entre datos transformados y datos enriquecidos por API  

4. **Carga**  
   - Modelo dimensional en PostgreSQL:  
     - `dim_country`  
     - `dim_time`  
     - `fact_economy`  

5. **Almacenamiento externo**  
   - Exportación de archivos transformados a Google Drive  

---

## 📎 Consideraciones

- Se filtran datos con valores nulos antes de graficar o hacer análisis.  
- Se utiliza `merge` por nombre de país debido a diferencias en los identificadores.  
- La extracción de la API no está automatizada en Airflow para evitar sobrecarga de peticiones innecesarias.
