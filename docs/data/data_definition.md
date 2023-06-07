# Definición de los datos

## Origen de los datos

Estos datos vienen descargados de la plataforma empresarial en formato csv, esta plataforma se encarga de la generación de reportes del motor de recomendación, estos datos son alimentados y generados diariamente, sin embargo para el ejercicio usaremos las valoraciones que estan en el rango de todo el año 2021 y todo el año 2022.

Como he mencionado, la herramienta de descarga es a traves de la plataforma emrpesarial, pensé en hacerlo a través de un proceso automático que visitara esa plataforma y descargara automáticamente en un repositorio, pero no fue posible debido a temas de permisos y seguridad de la empresa.

## Especificación de los scripts para la carga de datos

- El script para cargar los datos será: carga_datos.ipynb

## Referencias a rutas o bases de datos origen y destino

- Al tratarse de un archivo .csv, se tendra disponible en una ruta del equipo local que ejecute los scripts.

### Rutas de origen de datos

- La ubicación del archivo será en el equipo local en el que se esté desarrollando.
- La estructura consta básicamente de 4 columnas, se podrá ver mayor detalle en el apartado de diccionario de datos.
- No se requiere hacer prácticamente ningún trabajo sobre limpieza de datos, incluso para el modelo usaremos únicamente 2 de las 4 columnas y a su vez los datos se encuentran completos.

### Base de datos de destino

- De ser necesario para el proyecto, se esribirán archivos .csv en el equipo local en el que se esté desarrollando.
