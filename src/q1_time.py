from typing import List, Tuple
from datetime import datetime
from collections import Counter, defaultdict
from heapq import nlargest
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para almacenar el conteo de tweets por fecha
    date_counts = Counter()
    # Diccionario para almacenar el conteo de tweets por usuario por fecha
    user_counts_by_date = defaultdict(Counter)
    
    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            # Obtener la fecha y el nombre de usuario
            date = tweet['date'].split('T')[0]
            username = tweet["user"]["username"]
            
            # Actualizar los conteos
            date_counts[date] += 1
            user_counts_by_date[date][username] += 1
    
    # Encontrar las 10 fechas con más tweets
    top_dates = nlargest(10, date_counts.items(), key=lambda x: x[1])
    # Lista para almacenar las fechas y usuarios con más tweets
    top_dates_users = []
    
    # Obtener el usuario con más posts por fecha
    for date, _ in top_dates:
        top_user = user_counts_by_date[date].most_common(1)[0][0]
        top_dates_users.append((datetime.strptime(date, "%Y-%m-%d").date(), top_user))
    
    # Ordenar por fecha en orden descendente
    top_dates_users.sort(key=lambda x: x[0], reverse=True)
    
    return top_dates_users