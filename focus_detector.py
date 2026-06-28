import cv2
import mediapipe as mp
import time
import winsound

from productivity_score import calculate_productivity

# Initialize Face Mesh
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open Webcam
cap = cv2.VideoCapture(0)

# Variables
distraction_start = None
last_beep_time = 0
alert_count = 0

# Session Start Time
session_start = time.time()

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    # Calculate Focus Time
    focus_time = int((time.time() - session_start) / 60)

    # Productivity Score
    productivity = calculate_productivity(
        focus_time,
        alert_count,
        0
    )

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            # Nose Landmark
            nose = face_landmarks.landmark[1]

            nose_x = int(nose.x * w)
            nose_y = int(nose.y * h)

            cv2.circle(frame, (nose_x, nose_y), 6, (0, 0, 255), -1)

            # Focus Detection
            if 220 < nose_x < 420:

                status = "Focused"
                color = (0, 255, 0)

                distraction_start = None
                last_beep_time = 0

            else:

                status = "Distracted"
                color = (0, 0, 255)

                if distraction_start is None:
                    distraction_start = time.time()

                elapsed = time.time() - distraction_start

                # Alert after 1 second
                if elapsed >= 1:

                    current = time.time()

                    if current - last_beep_time >= 1:

                        winsound.Beep(1200, 300)

                        alert_count += 1

                        last_beep_time = current

                    cv2.putText(
                        frame,
                        "ALERT! PLEASE FOCUS!",
                        (20, 250),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

            # Status
            cv2.putText(
                frame,
                f"Status : {status}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # Alert Count
            cv2.putText(
                frame,
                f"Alerts : {alert_count}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            # Study Time
            cv2.putText(
                frame,
                f"Study Time : {focus_time} min",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Productivity
            cv2.putText(
                frame,
                f"Productivity : {productivity}%",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

    else:

        cv2.putText(
            frame,
            "NO FACE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("Smart Focus Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()