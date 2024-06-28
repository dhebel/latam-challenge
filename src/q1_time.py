from typing import List, Tuple
from datetime import datetime
from collections import Counter, defaultdict
from heapq import nlargest
import memory_profiler
import json

#@memory_profiler.profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Dictionary to store the count of tweets per date
    date_counts = Counter()
    # Dictionary to store the count of tweets per user per date
    user_counts_by_date = defaultdict(Counter)
    
    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            # Get the date and username
            date = tweet['date'].split('T')[0]
            username = tweet["user"]["username"]
            
            # Update counts
            date_counts[date] += 1
            user_counts_by_date[date][username] += 1
    
    # Find the top 10 dates with most tweets
    top_dates = nlargest(10, date_counts.items(), key=lambda x: x[1])
    
    top_dates_users = []
    
    # Get the user with the most posts per date
    for date, _ in top_dates:
        top_user = user_counts_by_date[date].most_common(1)[0][0]
        top_dates_users.append((datetime.strptime(date, "%Y-%m-%d").date(), top_user))
    
    # Sort by date
    top_dates_users.sort(key=lambda x: x[0], reverse=True)
    
    return top_dates_users