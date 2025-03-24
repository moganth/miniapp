import sqlite3

DB_NAME = "files.db"

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
