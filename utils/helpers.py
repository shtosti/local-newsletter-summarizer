from datetime import datetime

def today_str():
    return datetime.now().strftime("%Y-%m-%d")

def week_str():
    return datetime.now().strftime("week-%U-%Y")