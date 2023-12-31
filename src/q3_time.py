from typing import List, Tuple
import pandas as pd

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Lee un archivo JSON desde la ruta especificada y cuenta cuántas veces se menciona cada usuario.
    
    Args:
        file_path (str): La ruta al archivo JSON.
        
    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene el nombre de usuario y la cantidad de menciones,
                               ordenada en orden descendente según la cantidad.
    """
     # Leer el archivo JSON en un DataFrame
    df = pd.read_json(file_path, lines=True)

     # Seleccionar la columna 'mentionedUsers' y eliminar filas con valores nulos
    df_mentioned_users = df['mentionedUsers'].dropna()

     # Aplicar una función para extraer los nombres de usuario y explotar las listas en filas separadas
    df_mentioned_users = df_mentioned_users.apply(lambda x: [x['username'] for x in x]).explode()

     # Contar la frecuencia de cada nombre de usuario
    conteo = df_mentioned_users.value_counts()

     # Convertir el resultado a un DataFrame, tomar las primeras 10 filas y convertir a lista de tuplas
    conteo_list = conteo.to_frame().head(10).to_records().tolist()
    
     # Devolver la lista de tuplas ordenada en orden descendente según la cantidad de menciones
    return conteo_list