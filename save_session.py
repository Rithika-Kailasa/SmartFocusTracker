import sqlite3
from datetime import datetime

def save_session(focus_time, distraction_count, screen_distraction_count):

    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sessions
        (date_time, focus_time, distraction_count, screen_distraction_count)
        VALUES (?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        focus_time,
        distraction_count,
        screen_distraction_count
    ))

    conn.commit()
    conn.close()

    print("Session Saved Successfully!")