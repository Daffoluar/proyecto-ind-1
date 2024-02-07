## Proyecto: PI_1_ML_OPS

Este proyecto representa el rol de un Ingeniero MLOps, fusionando las habilidades de un Ingeniero de Datos y un Científico de Datos, en el contexto de la plataforma de videojuegos multinacional Steam. El objetivo es desarrollar un Producto Mínimo Viable (MVP) que incluya una API desplegada en la nube y la implementación de un modelo de Machine Learning para generar recomendaciones de juegos.

### Introducción

El proyecto se basa en un conjunto de datos en formato JSON relacionados con la plataforma de videojuegos Steam, proporcionando la base para el desarrollo de un Producto Mínimo Viable (MVP). Los archivos de datos incluyen:

    steam_games: Contiene información sobre los juegos en la plataforma Steam, como nombre, género y fecha de lanzamiento, entre otros detalles.

    user_reviews: Proporciona detalles sobre las reseñas realizadas por los usuarios de Steam.

    user_items: Ofrece información sobre la actividad de los usuarios en la plataforma Steam.

### ETL (Extracción, Transformación y Carga)

Se realizó el proceso de ETL para los tres conjuntos de datos entregados. Este proceso incluye la extracción de datos, la limpieza de los mismos para facilitar su comprensión y el almacenamiento de los datos limpios en formato Parquet.

Detalles específicos del proceso de ETL para cada conjunto de datos se encuentran en la sección correspondiente.

### Ingeniería de características

Se llevó a cabo un análisis de sentimientos sobre las reseñas de los usuarios. Se creó una nueva columna llamada 'sentiment_analysis' para clasificar los sentimientos de los comentarios en una escala de:

    0 para sentimientos negativos,
    1 para neutros o sin reseña, y
    2 para sentimientos positivos.

Los detalles completos del desarrollo se pueden encontrar en la Jupyter Notebook "Análisis de Sentimientos".

### Análisis Exploratorio de Datos (EDA)

Se realizó un análisis exploratorio de los datos para identificar patrones y tendencias, así como outliers. El código utilizado está disponible en la sección EDA.

### API

Se desarrolló una API utilizando FastAPI, permitiendo su consumo desde la web. La API consta de 6 endpoints:

    developer: Proporciona la cantidad de ítems y el porcentaje de contenido gratuito por año según la empresa desarrolladora.
    userdata: Devuelve el dinero gastado por un usuario, el porcentaje de recomendación basado en reseñas y la cantidad de ítems.
    UserForGenre: Retorna el usuario con más horas jugadas para un género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
    best_developer_year: Devuelve el top 3 de desarrolladores con más juegos recomendados por usuarios para un año dado.
    developer_reviews_analysis: Proporciona un análisis de reseñas de usuarios categorizadas como positivas o negativas para un desarrollador específico.
    recomendacion_juego: Recibe el ID de un juego y devuelve una lista con 5 juegos recomendados similares.

Detalles de implementación se encuentran en la sección API.
### Modelo de Machine Learning

El modelo se basa en la similitud del coseno, estableciendo una relación ítem-ítem para recomendar juegos similares. También se aplica un filtro usuario-juego para recomendar ítems basados en usuarios similares.

### Despliegue

Para el despliegue de la API se utilizó la plataforma Render. Se puede acceder al funcionamiento de la API desplegada a través del siguiente enlace: Deploy. Link: https://proyecto-ind-1.onrender.com/docs#/
