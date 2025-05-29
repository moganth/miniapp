import sqlite3
import os

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

def save_file_info(name: str, filename: str, path: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO files (name, filename, path) VALUES (?, ?, ?)", (name, filename, path))
    conn.commit()
    conn.close()

def get_all_files():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM files")
    files = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "filename": row[2], "path": row[3]} for row in files]


def get_file_path_by_name(name: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM files WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None