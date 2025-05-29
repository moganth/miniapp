import sqlite3
import os

# Use a writable directory instead of relative "data" path
DB_DIR = "/tmp/data"
DB_NAME = f"{DB_DIR}/files.db"

# Add error handling for directory creation
try:
    os.makedirs(DB_DIR, exist_ok=True)
except OSError as e:
    if e.errno == 30:  # Read-only file system
        # Fallback to user's home directory
        DB_DIR = os.path.expanduser("~/plugin_data")
        DB_NAME = f"{DB_DIR}/files.db"
        os.makedirs(DB_DIR, exist_ok=True)
        print(f"Warning: Using fallback database directory: {DB_DIR}")
    else:
        raise

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            filename TEXT NOT NULL,
            path TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_table()
