from fastapi import FastAPI
import pandas as pd


app = FastAPI()



@app.get('/')
def proyecto():
    return {'Principal':'Proyecto 1'}


@app.get("/developer/{desarrollador}")
def desarrollador(desarrollador:str):
    df_games = pd.read_parquet('Datasets Finales/steam_games.parquet', engine='pyarrow')
    try:
        df_desarrollador = df_games[df_games['developer'] == desarrollador]
        df_resultado = pd.DataFrame()
        df_resultado['Años'] = df_desarrollador['release_date'].unique()
        df_resultado['Cantidad de items'] = df_desarrollador.groupby('release_date').size().values
        df_resultado['Porcentaje free'] = (len(df_desarrollador[df_desarrollador['price'] == 0]) / df_resultado['Cantidad de items']) * 100
        resultado_dict = df_resultado.to_dict(orient='records')
        return resultado_dict
    except:
        return f'No se encontró el desarrollador {desarrollador}.'
    

@app.get("/userdata/{user_id}")
def userdata(user_id:str):
    df = pd.read_parquet('Datasets Finales/endpoint_2_n.parquet', engine='pyarrow')
    df = df[df['user_id'] == user_id]
    gastado = df['price'].sum()
    recomendacion = (df['recommend'].sum() / len(df)) * 100
    items = df.iloc[0]['items_count'].astype(float)
    return {"Usuario": user_id, "Dinero gastado": gastado, "recomendación": recomendacion, "Cantidad de items": items}





@app.get("/UserForGenre/{genero}")
def UserForGenre(genero):
    df = pd.read_parquet('Datasets Finales/endpoint_3_n.parquet', engine='pyarrow')
    genero_capitalize = genero.capitalize()
    if genero_capitalize in df['genres'].str.capitalize().unique():
        df_genero = df[df['genres'].str.capitalize() == genero_capitalize]
        jugador_mas_horas = df_genero.groupby('user_id')['playtime_forever'].sum().idxmax()
        año = df.groupby('release_date')['playtime_forever'].sum()
        horas_dict = año.to_dict()
        return f"Usuario con más horas jugadas para el género {genero}: {jugador_mas_horas}\nHoras jugadas por año:\n{horas_dict}"       
    else:
        return f"No hay datos para el género '{genero_capitalize}' en el DataFrame."
    


@app.get("/best_developer_year/{año}")
def best_developer_year(año: int): 
    df = pd.read_parquet('Datasets Finales/endpoint_4_5_n.parquet', engine='pyarrow')
    data = df[df['release_date']== año]
    data = data[(data['recommend'] == True) & (data['sentiment_analysis'] == 2)].sort_values(by= 'developer',ascending= False)
    df_developers = data.groupby('developer')['sentiment_analysis'].sum().head(3)
    return {'Primero': df_developers.index[0], 'Segundo': df_developers.index[1], 'Tercero': df_developers.index[2]}


@app.get("/developer_reviews_analysis/{desarrolladora}")
def developer_reviews_analysis(desarrolladora: str ):
    df = pd.read_parquet('Datasets Finales/endpoint_4_5_n.parquet', engine='pyarrow')
    df_desarrolladora = df[df['developer'] == desarrolladora]
    positivos = (df_desarrolladora['sentiment_analysis'] == 2).count()
    negativos = (df_desarrolladora['sentiment_analysis'] == 0).count()
    return {desarrolladora:f'[Negative = {negativos}, Positive = {positivos}]'}

