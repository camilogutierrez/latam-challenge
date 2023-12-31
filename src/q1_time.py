from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Obtiene las 10 fechas más activas y su usuario más activo correspondiente de un archivo JSON.

    Args:
        file_path (str): La ruta al archivo JSON.

    Returns:
        List[Tuple[datetime.date, str]]: lista de tuplas que contiene la fecha y el usuario más activo para cada fecha.
    """
    df = pd.read_json(file_path, lines=True)

    # Convertir 'date' a datetime y extraer la fecha
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Extraer el nombre de usuario del diccionario anidado 'user'
    df['username'] = df['user'].apply(lambda row: row['username'])

    # Agrupar por 'date' y contar los tweets, obtener el usuario más activo por fecha
    top_dates_df = df.groupby('date')['username'].agg(
        total_tweets='size',
        most_active_user=lambda x: x.value_counts().idxmax()
    ).nlargest(10, columns='total_tweets')

    # Convierte el resultado a una lista de tuplas
    top_dates_list = top_dates_df[['most_active_user']].to_records().tolist()

    return top_dates_list