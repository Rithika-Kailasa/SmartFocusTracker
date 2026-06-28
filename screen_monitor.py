import pygetwindow as gw
import time

study_keywords = [
    "visual studio code",
    "thonny",
    "leetcode",
    "geeksforgeeks",
    "python",
    "tutorial"
]

distraction_keywords = [
    "instagram",
    "facebook",
    "netflix",
    "reels",
    "shorts"
]

while True:
    window = gw.getActiveWindow()

    if window:
        title = window.title.lower()

        if any(word in title for word in study_keywords):
            print("✅ Focused:", window.title)

        elif any(word in title for word in distraction_keywords):
            print("❌ Distracted:", window.title)

        else:
            print("⚠️ Unknown:", window.title)

    time.sleep(3)