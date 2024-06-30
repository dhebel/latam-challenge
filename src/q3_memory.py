from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Contador para almacenar el conteo de usuarios mencionados
    user_counter = Counter()
    
    with open(file_path, "r") as file:
        # Leer el archivo línea por línea
        for line in file:
            try:
                # Cargar la línea como un objeto JSON
                data = json.loads(line.strip())\
                # Verificar si hay usuarios mencionados
                if "mentionedUsers" in data:
                    # Actualizar el conteo de menciones por usuario
                    mentioned_users = data["mentionedUsers"]
                    usernames = [user["username"] for user in mentioned_users]
                    user_counter.update(usernames)
            except Exception as e:
                # Ignorar errores de contenido vacío
                continue
    
    return user_counter.most_common(10)
