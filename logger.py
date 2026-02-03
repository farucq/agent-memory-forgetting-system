import json
from datetime import datetime, timezone
from config import LOG_DIR

LOG_FILE = f"{LOG_DIR}/memory_events.jsonl"

def log_event(event_type, data):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "data": data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
