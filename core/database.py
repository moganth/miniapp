import sqlite3
import os
DB_DIR = "/app_data"
DB_NAME = f"{DB_DIR}/files.db"
os.makedirs(DB_DIR, exist_ok=True)
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
