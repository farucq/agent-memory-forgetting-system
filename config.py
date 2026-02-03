import os

BASE_DIR = "agent_memory_system"
LOG_DIR = f"{BASE_DIR}/logs"
CHROMA_DIR = f"{BASE_DIR}/chroma_db"

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)
