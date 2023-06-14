# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En nuestro caso, contamos con 11165 registros en nuestro dataset, cada uno de estos registros hace referencia a una valoración de algún usuario en un momento dado del tiempo, a su vez contamos con 4 columnas, también podemos observar que estas valoraciones estan en una escala de 1 a 5

## Resumen de calidad de los datos
En cuanto a la composición de nuestro dataframe, podemos ver que todas las variables son de tipo string excepto la variable de CALIFICACION que es de tipo entero y ID_CLIENTE, a su vez podemos ver también que no tenemos ningún dato faltante:

## Variable objetivo

Nuestro dataframe si tiene una variable que se puede llegar a estimar, es el caso de la CALIFICACION, cuando implementemos el modelo NCF (Neural Collaborative Filtering), su idea principal es llegar a generar predicciones de valoraciones de aquellos usuarios que no han valorado el item, de esta forma llegar a tener una matriz completa de valoraciones con la que pueda trabajar y sacar las similitudes de manera completa de todos los usuarios (Mayor info en el NB de EDA).

## Variables individuales

Un pequeño resumen de nuestras variables es este:

*Número de Ratings: 11,165

*Columnas: ['ID_CLIENTE' 'FECHA_INTERACCION' 'NOMBRE_CORTO_DE_EXPERIENCIA' 'CALIFICACION']

*Número de Usuarios: 2,382

*Número de Experiencias: 254

De igual forma en el NB de EDA podemos ver un poco mas al detalle de estas variables.

## Ranking de variables

Para nuestro casa de motor de recomendación, nuestro ranking de variables es bastante claro y buscamos predecir la calificación de todos los usuarios de la matriz sobre todos los productos.

