import emoji
from collections import Counter

def count_emojis(text) -> Counter:
    """
    Cuenta la cantidad de emojis en un texto.

    Args:
        text (str): El texto en el que se contarán los emojis.

    Returns:
        Counter: Un objeto Counter que contiene la cantidad de cada emoji encontrado en el texto.
    """
    # Analiza el texto en busca de emojis y devuelve una lista de objetos EmojiData.
    data = emoji.analyze(text)

    # Extrae los caracteres de cada objeto EmojiMatch y los almacena en una lista.
    emoji_list = [em.chars for em in data]

    # Crea un objeto Counter a partir de la lista de emojis y devuelve el resultado.
    return Counter(emoji_list) if emoji_list else None
