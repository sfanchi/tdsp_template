# Reporte del Modelo Final

## Resumen Ejecutivo

En nuestro modelo final, al igual que en el modelo baseline que hemos desarrollado previamente, hemos calculado el RMSE como métrica de desempeño, en el caso de nuestro modelo dió un valor de 0.522, lo cual es bastante bien para una corrida no tan extensa, además, se puede ver como va disminuyendo e cada época y se puede notar la mejoría de nuestro modelo en el entrenamiento.

## Descripción del Problema

Buscamos básicamente es poder darle recomendaciones a todos los usuarios de nuestra matriz de valoraciones, en un estado inicial, esa matriz no tienen todas las valoraciones de todos los usuarios sobre todos los productos, entonces nuestro objetivo es rellenar esa matriz con predicciones, para asi tener una matriz completa de valoraciones de usuario aún asi el usuario no haya valorado ni comprado esos productos, de esta manera, podemos seleccionar aquellos productos que mayor valoracion tiene despues de la predicción y que no haya adquirido y ese será el producto a recomendar ya que es el mas propenso a que al usuario le pueda gustar y por ende consumir.

## Descripción del Modelo

Para nuestro caso usamos una red neuronal con un método de ejecuciión secuencial, la arquitectura consta de una primera capa densa con 256 neuronas y activación Relu, una segunda capa densa con 64 neuronas y activación Relu y por ultimo otra capa densa que es la de salida (con la que queremos sacar nuestras predicciones) con 1 sola neurona ya que nos interesa solo predecir las valoraciones de los usuarios.

## Evaluación del Modelo

Para el caso de nuestro modelo, utilizamos como mpetrica el RMSE el cual dió un valor de 0.522, es un buen resultado y nos dice que las valoraciones predichas no estan muy alejadas de las valoraciones que son reales, lo cual nos da un bune nivel de confianza sobre los resultados de nuestro modelo.

## Conclusiones y Recomendaciones

La aplicación es bastante robusta en temas de este modelo ya que a nivel de negocio puede ser muy interesante llevar la personalizacion hacia sus clientes a un siguiente nivel, el siguiente paso puede ser en pensar en como desplegarlo en un ambiente productivo (mediante API por ejemplo), a su vez se puede profundizar en una arquitectura de red neuronal ams robusta e incluso ver la opcion de exploración de hiperparametros para nuestro modelo. Sin embargo puede verse como un buen primer despliegue en un ambiente de pruebas y monitorear sus resultados.

## Referencias

https://www.tensorflow.org/recommenders/examples/basic_ranking?hl=es-419
