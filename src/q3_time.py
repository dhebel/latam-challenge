from typing import List, Tuple
from collections import defaultdict
import json
import heapq


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Diccionario para almacenar el conteo de usuarios mencionados
    user_counter = defaultdict(int)
    
    # Leer el archivo línea por línea
    with open(file_path, "r") as file:
        for line in file:
            try:
                # Cargar la línea como un objeto JSON
                data = json.loads(line.strip())
                # Verificar si hay usuarios mencionados
                if "mentionedUsers" in data:
                    mentioned_users = data["mentionedUsers"]
                    # Actualizar el conteo de menciones por usuario
                    for user in mentioned_users:
                        # Verificar si el usuario tiene un nombre de usuario
                        if "username" in user:
                            # Actualizar el conteo de menciones
                            username = user["username"]
                            user_counter[username] += 1
            except Exception as e:
                continue
    
    # Obtener los 10 usuarios más influyentes directamente usando un heap
    top_users = heapq.nlargest(10, user_counter.items(), key=lambda x: x[1])
    
    return top_users