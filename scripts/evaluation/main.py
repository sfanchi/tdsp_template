import typer
import time
from rich.progress import track
import keras.models as km
import numpy as np
import pandas as pd

PATH = "model" 
model = km.load_model(PATH)

df = pd.read_csv('valoraciones_usuarios.csv', sep = ",")
df = df.astype({'ID_CLIENTE':'string','FECHA_INTERACCION':'string','NOMBRE_CORTO_DE_EXPERIENCIA':'string'})

test_ratings = {}
test_experiencias_titles = df['NOMBRE_CORTO_DE_EXPERIENCIA'].drop_duplicates().values.tolist()

def main():
    person_name = typer.prompt("Hola, cual es tu nombre?")
    print("")
    print(f"Hola {person_name}, soy SIRBI tu asistente para recomendaciones.")
    iniciar = typer.confirm("Deseas dar inicio al proceso de generar recomendaciones?")
    if not iniciar:
        print("Nos veremos pronto!")
        raise typer.Abort()
    print("***************************\nComencemos!\n***************************")
    if iniciar:
        print(f"Para empezar, quiero comentarte que ya tengo cargado el modelo entrenado y está listo para usarse.\n")
        print("He detectado los siguientes usuarios sin recomendar:[17,34,42,77,81]\n")
        id_reco = typer.prompt("A cual de ellos te gustaría generarle sus recomendaciones?")
        print(f"Entendido! Procesaré recomendaciones para el usuario {id_reco}\n")
    for value in track(range(100), description=f"Procesando usuario {id_reco}\n"):
        # Fake processing time
        time.sleep(0.03)
    print(f"Hecho! Hemos generado recomendaciones para el usuario {id_reco}.\n")
    ver_recos = typer.confirm(f"Te gustaría ver las recomendaciones que se le hicieron al usuario {id_reco}?")
    print("")
    if ver_recos:
        print(f"El usuario {id_reco} actualmente tiene los siguientes productos valorados:\n")
        print(df.query(f"ID_CLIENTE == '{id_reco}'"))
        print("")
        cant_recos = typer.prompt(f"Cuantas recomendaciones te gustaría ver?")
        for experiencia_title in test_experiencias_titles:
            test_ratings[experiencia_title] = model({
            "ID_CLIENTE": np.array([id_reco]),
            "NOMBRE_CORTO_DE_EXPERIENCIA": np.array([experiencia_title])
        })
        print(f"Las {cant_recos} recomendaciones con mayor valoración que tenemos del usuario {id_reco} son las siguientes:\n")   
        for title, score in sorted(test_ratings.items(), key=lambda x: x[1], reverse=True)[:int(cant_recos)]:
            print(f"{title}: {score}")
        print("")
        print(f"A su vez, las {cant_recos} recomendaciones con menor valoración que tenemos del usuario {id_reco} son las siguientes:\n")
        for title, score in sorted(test_ratings.items(), key=lambda x: x[1])[:int(cant_recos)]:
            print(f"{title}: {score}")
    print("")
    print(f"Gracias por tu tiempo! He escrito los resultados en la respectiva base de datos, hasta pronto!")
    
    print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)

if __name__ == "__main__":
    typer.run(main)