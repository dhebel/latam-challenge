from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para almacenar las fechas y usuarios
    dates = Counter()
    user_counts = {}
    
    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            # Obtener la fecha y el nombre de usuario
            date = tweet['date'].split('T')[0]
            username = tweet["user"]["username"]
            
            # Actualizar el conteo de tweets por fecha
            dates[date] += 1
            
            # Actualizar el conteo de tweets por usuario por fecha
            if date not in user_counts:
                user_counts[date] = Counter()
            user_counts[date][username] += 1
    
    # Encontrar las 10 fechas con más tweets
    top_dates = dates.most_common(10)
    top_dates_users = []
    
    # Obtener el usuario con más posts por fecha
    for date, _ in top_dates:
        top_user = user_counts[date].most_common(1)[0][0]
        top_dates_users.append((datetime.strptime(date, "%Y-%m-%d").date(), top_user))
    
    # Ordenar por cantidad de tweets en orden descendente
    top_dates_users.sort(key=lambda x: dates[x[0].strftime("%Y-%m-%d")], reverse=True)
    
    return top_dates_users