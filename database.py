import sqlite3

def create_database_and_table():
    conn = sqlite3.connect("blog_data.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def save_to_database(conn, data):
    c = conn.cursor()
    for item in data:
        c.execute("""
            INSERT INTO blog_posts (title, link)
            VALUES (?, ?)
        """, (item["title"], item["link"]))
    conn.commit()
