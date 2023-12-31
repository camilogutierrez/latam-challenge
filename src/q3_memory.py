from typing import List, Tuple
from collections import Counter
import json

from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Cuenta el número de veces que cada usuario mencionado aparece en un archivo que contiene tweets.

    Args:
        file_path (str): La ruta al archivo que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas, donde cada tupla contiene el nombre de usuario de un usuario mencionado
        y el número de veces que fue mencionado, ordenado en orden descendente según el conteo de menciones.
    """
   # Inicializar un contador para contar menciones de usuarios
    mentioned_users_counter = Counter()

    # Abrir el archivo JSON de tweets y procesar cada línea
    with open(file_path, 'r', encoding='utf-8') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Cargar el tweet desde la línea como un objeto JSON
            tweet = json.loads(line)
            
            # Obtener la lista de usuarios mencionados en el tweet
            mentioned_user = tweet['mentionedUsers']
            
            # Verificar si hay usuarios mencionados en el tweet
            if not mentioned_user:
                continue
            
            # Actualizar el contador para cada usuario mencionado en el tweet
            for user in mentioned_user:
                mentioned_users_counter[user['username']] += 1
    
    # Obtener las 10 menciones más comunes y convertirlas a una lista de tuplas
    conteo_lista = mentioned_users_counter.most_common(10)
    
    # Devolver la lista de tuplas ordenada en orden descendente según el conteo de menciones
    return conteo_lista