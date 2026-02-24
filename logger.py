import datetime

def log_event(level, message):
    timestamp = datetime.datetime.now().isoformat()
    # writing to stdout for now, maybe add file logging later
    print(f"[{timestamp}] [{level.upper()}] {message}")

def log_error(message):
    log_event("error", message)
