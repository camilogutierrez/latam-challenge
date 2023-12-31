from collections import defaultdict, Counter
from typing import List, Tuple
from datetime import datetime
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Esta función lee un archivo JSON que contiene tweets y devuelve una lista de las 10 fechas con mayor cantidad de tweets,
    junto con el usuario más activo para cada una de esas fechas.

    Args:
        file_path (str): La ruta del archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Una lista de tuplas que contiene la fecha y el usuario más activo para cada una de las 10 fechas con mayor cantidad de tweets.
    """
    # Se inicializa los diccionarios para contabilizar la actividad de tweets
    tweet_counts = defaultdict(int)  # Contador de tweets por fecha
    tweets_activity = defaultdict(lambda: defaultdict(int))  # Contador de tweets por fecha y usuario

    # Abrir el archivo JSON y procesar cada línea
    with open(file_path, 'r') as file:
        for line in file:
            # Leer los tweets desde la línea del archivo JSON
            tweet = json.loads(line)
            
            # Extraer la fecha y el nombre de usuario del tweet
            date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']

            # Contar la cantidad de tweets por fecha y usuario
            tweet_counts[date] += 1
            tweets_activity[date][username] += 1

    # Obtener las 10 fechas con mayor cantidad de tweets
    top_10_dates = Counter(tweet_counts).most_common(10)

    # Encontrar el usuario más activo para cada una de las 10 fechas con mayor trafico
    top_users = [(date, Counter(tweets_activity[date]).most_common(1)[0][0]) for date, _ in top_10_dates]

    return top_users