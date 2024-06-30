from typing import List, Tuple
from collections import Counter
import json
from emoji import emoji_list
import heapq

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Se inicializa un contador para los emojis
    emojis = Counter()
    
    with open(file_path, "r") as file:
        for line in file:
            # Se extrae el texto del tweet
            tweet = json.loads(line)["content"]
            # Se verifica si el tweet no está vacío
            if tweet:
                # Se utiliza la función `emoji_list` para extraer los emojis del texto
                emojis.update(e["emoji"] for e in emoji_list(tweet))
    
    # Se retorna los 10 emojis más comunes
    return heapq.nlargest(10, emojis.items(), key=lambda x: x[1])