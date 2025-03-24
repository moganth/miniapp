import sqlite3

DB_NAME = "files.db"

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