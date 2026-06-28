import sqlite3

conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show columns in sessions table
cursor.execute("PRAGMA table_info(sessions)")
print("Columns:", cursor.fetchall())

conn.close()