"""
Como el codigo consta de un csv, es suficiente solo con ejectuar los comandos respectivos para cargarlo 
a nuestro NoteBook:
"""
#Usamos la opción interactiva para cargar nuestros datos desde nuestro equipo local.
from google.colab import files
uploaded = files.upload()
#Una vez seleccionamos el archivo, usamos pandas e io para leer el archivo csv
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['comentarios_plataforma.csv']), sep = ",")
# Almacenamos los datos en un dataframe y vemos algunos temas descriptivos
df.head()
