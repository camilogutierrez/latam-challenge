from typing import List, Tuple
import json
from collections import Counter
from utils import count_emojis

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Lee un archivo JSON y cuenta la frecuencia de los emojis en los tweets.

    Args:
        file_path (str): La ruta del archivo JSON.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 emojis más comunes y su frecuencia.
    """
    # Leer el archivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        total_emoji_counter = Counter()
        for line in file:
            tweet = json.loads(line) 
            # Extraer los emojis de cada tweet
            emoji_counter = count_emojis(tweet['content'])
            if emoji_counter:
                # Sumar los emojis de cada tweet al contador total 
                total_emoji_counter += emoji_counter

    # Obtener los 10 emojis más comunes
    top_emojis = total_emoji_counter.most_common(10)

    return top_emojis