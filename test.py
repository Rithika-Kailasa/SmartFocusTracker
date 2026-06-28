from productivity_score import calculate_productivity

focus_time = 60
face_distractions = 2
screen_distractions = 1

score = calculate_productivity(
    focus_time,
    face_distractions,
    screen_distractions
)

print("Productivity Score:", score)