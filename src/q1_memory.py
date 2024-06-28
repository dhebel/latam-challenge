from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json
import memory_profiler

#@memory_profiler.profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
        # Dictionary to store the dates and users
    dates = Counter()
    user_counts = {}
    
    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            # Get the date and username
            date = tweet['date'].split('T')[0]
            username = tweet["user"]["username"]
            
            # Update the count of tweets per date
            dates[date] += 1
            
            # Update the count of tweets per user per date
            if date not in user_counts:
                user_counts[date] = Counter()
            user_counts[date][username] += 1
    
    # Top 10 dates with most tweets
    top_dates = dates.most_common(10)
    top_dates_users = []
    
    # Get the user with the most posts per date
    for date, _ in top_dates:
        top_user = user_counts[date].most_common(1)[0][0]
        top_dates_users.append((datetime.strptime(date, "%Y-%m-%d").date(), top_user))
    
    # Sort by date
    top_dates_users.sort(key=lambda x: x[0], reverse=True)
    
    return top_dates_users