from typing import List, Tuple
from collections import Counter
from utils import count_emojis
import pandas as pd


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Calcula los 10 emojis más comunes en un archivo JSON.

    Args:
        file_path (str): La ruta al archivo JSON.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los emojis más comunes y su frecuencia.
    """
    df = pd.read_json(file_path, lines=True)
    
    # Se unen todo el contenido de los tweets en un solo string
    conteo_de_emojis = count_emojis("".join(df.content.values))
    
    return conteo_de_emojis.most_common(10)