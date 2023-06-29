import pandas as pd
import tensorflow_recommenders as tfrs
import tensorflow as tf
import numpy as np
from typing import Dict, Text

df = pd.read_csv('valoraciones_usuarios.csv', sep = ",")
df.head()
df = df.astype({'ID_CLIENTE':'string','FECHA_INTERACCION':'string','NOMBRE_CORTO_DE_EXPERIENCIA':'string'})

ds = tf.data.Dataset.from_tensor_slices(
      (dict(df[['ID_CLIENTE','NOMBRE_CORTO_DE_EXPERIENCIA']]), df['CALIFICACION']))

    # convertimos y mapeamos las variables que vamos a usar en nuestro modelo
ds = ds.map(lambda x, y: {
    'ID_CLIENTE' : x['ID_CLIENTE'],
    'NOMBRE_CORTO_DE_EXPERIENCIA' : x['NOMBRE_CORTO_DE_EXPERIENCIA'],
    'CALIFICACION' : y
    })

tf.random.set_seed(42)
shuffled = ds.shuffle(11165, seed=42, reshuffle_each_iteration=False)
#Definimos datos de entrenamiento y prueba
train = shuffled.take(8932)
test = shuffled.skip(8932).take(2233)

nombres_experiencias = ds.batch(1_000_000).map(lambda x: x["NOMBRE_CORTO_DE_EXPERIENCIA"])
user_ids = ds.batch(1_000_000).map(lambda x: x["ID_CLIENTE"])
#Sacamos los valores unicos tanto de las experiencias como de los usuarios, estos son los que se usaran como embedings posteriormente
unique_nombres_experiencias = np.unique(np.concatenate(list(nombres_experiencias)))
unique_user_ids = np.unique(np.concatenate(list(user_ids)))

class RankingModel(tf.keras.Model):

  def __init__(self):
    super().__init__()
    embedding_dimension = 32

    # Computamos embeddings para usuarios.
    self.user_embeddings = tf.keras.Sequential([
      tf.keras.layers.StringLookup(
        vocabulary=unique_user_ids, mask_token=None),
      tf.keras.layers.Embedding(len(unique_user_ids) + 1, embedding_dimension)
    ])

    # Computamos embeddings para experiencias.
    self.experiencias_embeddings = tf.keras.Sequential([
      tf.keras.layers.StringLookup(
        vocabulary=unique_nombres_experiencias, mask_token=None),
      tf.keras.layers.Embedding(len(unique_nombres_experiencias) + 1, embedding_dimension)
    ])

    # Computamos predicciones.
    self.ratings = tf.keras.Sequential([
      # Aprendizaje de multiples capas densas.
      tf.keras.layers.Dense(256, activation="relu"), #capa densa con 256 neuronas y activación Relu
      tf.keras.layers.Dense(64, activation="relu"), #capa densa con 64 neuronas y activación Relu
      # Hacemos las predicciones de los rating en la ultima capa (1 neurona).
      tf.keras.layers.Dense(1)
  ])

  def call(self, inputs):

    ID_CLIENTE, NOMBRE_CORTO_DE_EXPERIENCIA = inputs

    user_embedding = self.user_embeddings(ID_CLIENTE)
    experiencia_embedding = self.experiencias_embeddings(NOMBRE_CORTO_DE_EXPERIENCIA)

    return self.ratings(tf.concat([user_embedding, experiencia_embedding], axis=1))

task = tfrs.tasks.Ranking(
  loss = tf.keras.losses.MeanSquaredError(),
  metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

class ExperienciasModel(tfrs.models.Model):

  def __init__(self):
    super().__init__()
    self.ranking_model: tf.keras.Model = RankingModel()
    self.task: tf.keras.layers.Layer = tfrs.tasks.Ranking(
      loss = tf.keras.losses.MeanSquaredError(),
      metrics=[tf.keras.metrics.RootMeanSquaredError()]
    )

  def call(self, features: Dict[str, tf.Tensor]) -> tf.Tensor:
    return self.ranking_model(
        (features["ID_CLIENTE"], features["NOMBRE_CORTO_DE_EXPERIENCIA"]))

  def compute_loss(self, features: Dict[Text, tf.Tensor], training=False) -> tf.Tensor:
    labels = features.pop("CALIFICACION")

    rating_predictions = self(features)

    # El task procesa la perdida y las metricas.
    return self.task(labels=labels, predictions=rating_predictions)

model = ExperienciasModel()
model.compile(optimizer=tf.keras.optimizers.Adagrad(learning_rate=0.1))

cached_train = train.shuffle(11195).batch(8192).cache()
cached_test = test.batch(4096).cache()

model.fit(cached_train, epochs=1000)
model.evaluate(cached_test, return_dict=True)

PATH = "model" 
model.save(PATH)
