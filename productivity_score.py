def calculate_productivity(focus_time, face_distractions, screen_distractions):

    score = focus_time - (face_distractions * 5) - (screen_distractions * 5)

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score


if __name__ == "__main__":
    score = calculate_productivity(60, 2, 1)
    print("Productivity Score:", score)