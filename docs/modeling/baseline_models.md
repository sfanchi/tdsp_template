# Reporte del Modelo Baseline

En el modelo baseline podemos ver como el modelo basado en redes neuronales puede predecir los ratings de las valoraciones de peliculas que ciertos usuarios no han visto, esto con el fin de poder recomendar peliculas que les puede lelgar a gustar basado en lo que ya hayan visto previamente esos mismos usuarios.

## Descripción del modelo

Este primer modelo se toma como base para ilustrar el funcionamiento de un esuqema recomendador, donde tenemos 2 pilares básicos, que son las valoraciones y los usuarios. A partir de estos dos, se crea la arquitectura de la red neuronal para asi poder predecir toda la matriz de valoraciones de los usuarios.

## Variables de entrada

Las variables de entrada son las valoraciones de los productos que los usuarios ya han comprado/consumido y también los nombres de los productos o sus respectos identificadores que los usuarios han valorado.

## Variable objetivo

La variable objetivo para nuestro caso sigue siendo la misma valoración, pero buscamos predecir aquellas que no tenemos.

## Evaluación del modelo

### Métricas de evaluación

La variable que usamos para medir el rendimiento de nuestro modelo es el RMSE.

### Resultados de evaluación

El RMSE para el caso de el modelo baseline es de 0.251
## Análisis de los resultados

El modelo baseline es una buena primera aproximación a las predicciones de las valoraciones, sin embargo, la arquitectura de lar ed neuronal puede ser mas profunda.

## Conclusiones

Como lo mencioné anteriormente, se puede mejorar en la arquitectura de la red neuronal, esto trae su costo de nivel de procesamineto y tiempo pero puede valer la pena para unos mejores resultados.

## Referencias

https://www.tensorflow.org/recommenders/examples/quickstart?hl=es-419


