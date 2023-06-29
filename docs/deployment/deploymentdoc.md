# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Modelo de recomendaciones basado en Redes Neuronales
- **Plataforma de despliegue:** El despliegue se hara directamente sobre CLI, es decir sobre la terminal de un equipo.
- **Requisitos técnicos:** Se debe contar con un hardware no muy sofisticado, al tratarse de un CLI que se ejecuta directamente sobre el script es bastante rápido y liviano. En este ejercicio estamos usando la version de **Python 3.11** junto con algunas librerias las cuales son:
  - pandas
  - tensorflow_recommenders
  - tensorflow
  - numpy
  - typing
  - typer
  - time
  - rich.progress
  - keras
  
 A su vez, para el entrenamiento y despliegue del CLI, el equipo usado tiene las siguientes caracteristicas:
  - Procesador: AMD Ryzen 7 PRO 3700U w/ Radeon Vega Mobile Gfx   2.30 GHz
  - RAM: 16,0 GB
  - Tipo de sistema: Sistema operativo de 64 bits, procesador basado en x64
  - Núcleos: 4
  
- **Requisitos de seguridad:** Ninguna
- **Diagrama de arquitectura:** Al tratarse de un despliegue con CLI, es una metodología que se ejecuta directamente sobre el mismo computador, sin embargo la idea general del funcionamiento de nuestro de motor de recomendaciones es el siguiente:
  ![image](https://github.com/sfanchi/tdsp_template/assets/42486701/c82c2200-dcf8-4b94-82bc-e7654edecfc5)
Básicamente la idea es generar las recomendaciones ideales (docenas) a partir de información de contexto del usuario (intereses, acciones, clicks, etc...) que vana  nutrir los dos pilares fundamentales de nuestro motor, los cuales son las capas de generación de candidatos y la de ranking (en ese orden respectivamente), la capa de candidatos aplica como tal el algforitmo que estemos usando (para nuestro caso una red neuronal, pero pueden ser otros) despues de ese resultado, se ordenan esos resultados bajo algun criterio (popularidad, interés del negocio, Hinge Loss, Bayesian Personalized Ranking Loss, etc.) lo cual le dara al usuario resultados mucho mas aproximados a sus gustos y preferencias.
  
## Código de despliegue

- **Archivo principal:** En la ruta de scripts/deployment se consigue el archivo principal: **main.py**
- **Rutas de acceso a los archivos:** La ruta donde se consigue lo necesario para ejecutar el CLI es: /scripts/deployment
- **Variables de entorno:** NA

## Documentación del despliegue

- **Instrucciones de instalación:** Se debe contar con el csv (**valoraciones_usuarios.csv**) descargado para poder usarlo en los script, a su vez el orden de los script es el siguiente:
    1) Ejecutar el script de **modelo.py**, el se encarga de guardar el modelo de recomendación ya entrenado y con los últimos resultados para su posterior uso.
    2) Una vez se tiene el scipt de modelo.py ejecutado (el crea una carpeta en el mismo directorio llamada 'model' que es la que tiene guardado el modelo), se procede a ejecutar el **main.py** directamente desde la terminal con el comando 'python main.py', el tomará el resultado del modelo que salió de modelo.py y lo carga (la carpeta que creamos en el paso 1), a su vez que también se carga el archivo csv, se recomienda tener estos 3 archivos en el mismo directorio para no tener problemas.
- **Instrucciones de configuración:** Tener en la misma carpeta los 3 archivos y seguir las instrucciones de instalación.
- **Instrucciones de uso:** Cuando se ejecute el main.py, la misma terminal irá mostrando los pasos a seguir de una manera interactiva hasta que se llegue al final del proceso.
- **Instrucciones de mantenimiento:** Para mantenimiento, revisar periodicamente el modelo si necesita mejorarse o ajustarse, a su vez ir desarrollando según la necesidad mas pasos o ramas en el desarrollo del CLI.
