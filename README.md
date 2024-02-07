#PI N°1 ML_OPS

Este proyecto simula el rol de un MLOps Engineer, es decir, la combinación de un Data Engineer y Data Scientist, para la plataforma multinacional de videojuegos Steam. Para su desarrollo, se entregan unos datos y se solicita un Producto Mínimo Viable que muestre una API deployada en un servicio en la nube y la aplicación de un modelo de Machine Learning para hacer recomendaciones de juegos.
Introducción

Para este proyecto se nos proporciona un conjunto de tres archivos en formato JSON: de steam (Steam es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation) para poder trabajar en ellos y crear un Producto Minimo Viable (MVP), que contiene una la implementaciónde una API y con un modelo de Machine Learning. los datos provienen de los archivos siguientes:

    *steam_games información relacionada a los juegos dentro de la plataforma Steam. Por ejemplo: Nombre del juego, género, fecha de lanzamiento, entre otras.

    *user_reviews información que detalla las reseñas realizadas por los usuarios de la plataforma Steam.

    *user_items información acerca de la actividad de los usuarios dentro de la plataforma Steam.

#ETL

Se realizó la extracción, transformación y carga (ETL) de los tres conjuntos de datos entregados. En esta fase del proyecto se realiza la extracción de datos, a fin de familiarizarse con ellos y comenzar con la etapa de limpieza de datos que nos permita el correcto entedimiento. Terminada la limpieza se generará el conjunto de datos para la siguiente fase, estos se guardaron en formato parquet.

Los detalles del ETL para cada Dataset se puede ver en ETL
Feature engineering

En esta etapa se realizo el analisis de sentimientos a los reviews de los usuarios. Para ello se creó una nueva columna llamada 'sentiment_analysis' que reemplaza a la columna que contiene los reviews donde clasifica los sentimientos de los comentarios con la siguiente escala:

    0 si es malo,
    1 si es neutral o esta sin review
    2 si es positivo.

Todos los detalles del desarrollo se pueden ver en la Jupyter Notebook Analisis de sentimientos
#EDA

Se lleva a cabo el analisis exploratorio de los datos, identificando patrones y tendencias de los juegos y generos mas recomendados por los uduarios, a parte de identificar outliers, el codigo utilizado se puede visualizar en EDA

#API

Para su desarrollo se utilizó FastAPI, dicho Framework permite que la API pueda ser consumida desde la WEB, la misma consta de 6 endpoints: def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado

los detalles de codigo se encuentran en API

#Modelo de aprendizaje automático

El modelo se basa en la similitud del coseno, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.

#Deployment

Para el deploy de la API se seleccionó la plataforma Render, a continuacion el link donde se puede ver el funcionamiento de la API desplegado Deploy
