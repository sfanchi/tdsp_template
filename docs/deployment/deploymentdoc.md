# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Modelo de recomendaciones basado en Redes Neuronales
- **Plataforma de despliegue:** El despliegue se hara directamente sobre CLI, es decir sobre la terminal de un equipo.
- **Requisitos técnicos:** Se debe contar con un hardware no muy sofisticado, al tratarse de un CLI que se ejecuta directamente sobre el script es bastante rápido y liviano. En este ejercicio estamos usando la version de Python 3.11 junto con unas pocas librerias las cuales son:
  *pandas
  *tensorflow_recommenders
  *tensorflow
  *numpy
  *typing
  *typer
  *time
  *rich.progress
  *keras
- **Requisitos de seguridad:** Ninguna
- **Diagrama de arquitectura:** Al tratarse de un despliegue con CLI, es una metodología que se ejecuta directamente sobre el mismo computador.

## Código de despliegue

- **Archivo principal:** main.py
- **Rutas de acceso a los archivos:** valoraciones_usuarios.csv
- **Variables de entorno:** NA

## Documentación del despliegue

- **Instrucciones de instalación:** Se debe contar con el csv (valoraciones_usuarios.csv) descargado para poder usarlo en los script, a su vez el orden de los script es el siguiente:
    1) Ejecutar el script de **modelo.py**, el se encarga de guardar el modelo de recomendación ya entrenado y con los últimos resultados para su posterior uso.
    2) Una vez se tiene el scipt de modelo.py ejecutado (el crea una carpeta en el mismo directorio llamada 'model' que es la que tiene guardado el modelo), se procede a ejecutar el **main.py** directamente desde la terminal con el comando 'python main.py', el tomará el resultado del modelo que salió de modelo.py y lo carga (la carpeta que creamos en el paso 1), a su vez que también se carga el archivo csv, se recomienda tener estos 3 archivos en el mismo directorio para no tener problemas.
- **Instrucciones de configuración:** Tener en la misma carpeta los 3 archivos y seguir las instrucciones de instalación.
- **Instrucciones de uso:** Cuando se ejecute el main.py, la misma terminal irá mostrando los pasos a seguir de una manera interactiva hasta que se llegue al final del proceso.
- **Instrucciones de mantenimiento:** Para mantenimineto, revisar periodicamente el modelo si necesita mejorarse o ajustarse, a su vez ir desarrollando según la necesidad mas pasos o ramas en el desarrollo del CLI.
