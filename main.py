# just accesing webcam

# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Camera not detected")
#         break

#     cv2.imshow("Driver Monitoring System", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# Start
#   ↓
# Open Camera
#   ↓
# Get Frame
#   ↓
# Frame കിട്ടിയോ?
#   ↓
#  YES ───────────────→ NO
#   ↓                    ↓
# Display Frame       Stop
#   ↓
# 'q' pressed?
#   ↓
#  NO → Get next frame
#   ↓
#  YES
#   ↓
# Release Camera
#   ↓
# Close Window
#   ↓
# End

# Webcam
#    ↓
# OpenCV → Frame
#    ↓
# MediaPipe Face Landmarks
#    ↓
# Face-ന്റെ landmark points


# ith facinte mark full

# import cv2
# import mediapipe as mp

# # MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# mp_drawing = mp.solutions.drawing_utils

# face_mesh = mp_face_mesh.FaceMesh(
#     max_num_faces=1,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5
# )

# # Open camera
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while True:

#     ret, frame = cap.read()

#     if not ret:
#         print("Camera not detected")
#         break

#     # Convert BGR to RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect face landmarks
#     results = face_mesh.process(rgb_frame)

#     if results.multi_face_landmarks:

#         for face_landmarks in results.multi_face_landmarks:

#             mp_drawing.draw_landmarks(
#                 frame,
#                 face_landmarks,
#                 mp_face_mesh.FACEMESH_TESSELATION
#             )

#     # Show output
#     cv2.imshow("Driver Monitoring System", frame)

#     # Press Q to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# Eyes open
#    ↓
# EAR decreases
#    ↓
# Eyes closed
#    ↓
# Closed continuously for X seconds
#    ↓
# DROWSINESS DETECTED
#    ↓
# ALERT 🚨


# face +alignment



# import cv2
# import mediapipe as mp
# import numpy as np

# # ==========================================
# # MEDIAPIPE FACE MESH
# # ==========================================

# mp_face_mesh = mp.solutions.face_mesh
# mp_drawing = mp.solutions.drawing_utils

# face_mesh = mp_face_mesh.FaceMesh(
#     max_num_faces=1,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5
# )

# # ==========================================
# # EYE LANDMARK INDICES
# # ==========================================

# # Left eye
# LEFT_EYE = [33, 160, 158, 133, 153, 144]

# # Right eye
# RIGHT_EYE = [362, 385, 387, 263, 373, 380]


# # ==========================================
# # EAR FUNCTION
# # ==========================================

# def calculate_ear(landmarks, eye_indices):

#     p1 = np.array([
#         landmarks[eye_indices[0]].x,
#         landmarks[eye_indices[0]].y
#     ])

#     p2 = np.array([
#         landmarks[eye_indices[1]].x,
#         landmarks[eye_indices[1]].y
#     ])

#     p3 = np.array([
#         landmarks[eye_indices[2]].x,
#         landmarks[eye_indices[2]].y
#     ])

#     p4 = np.array([
#         landmarks[eye_indices[3]].x,
#         landmarks[eye_indices[3]].y
#     ])

#     p5 = np.array([
#         landmarks[eye_indices[4]].x,
#         landmarks[eye_indices[4]].y
#     ])

#     p6 = np.array([
#         landmarks[eye_indices[5]].x,
#         landmarks[eye_indices[5]].y
#     ])

#     # Vertical distances
#     vertical_1 = np.linalg.norm(p2 - p6)
#     vertical_2 = np.linalg.norm(p3 - p5)

#     # Horizontal distance
#     horizontal = np.linalg.norm(p1 - p4)

#     ear = (vertical_1 + vertical_2) / (2.0 * horizontal)

#     return ear


# # ==========================================
# # CAMERA
# # ==========================================



# # ==========================================
# # CAMERA
# # ==========================================

# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# while True:

#     ret, frame = cap.read()

#     if not ret:
#         print("Camera not detected")
#         break

#     # Convert BGR → RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process face
#     results = face_mesh.process(rgb_frame)

#     # ==========================================
#     # FACE DETECTED
#     # ==========================================

#     if results.multi_face_landmarks:

#         for face_landmarks in results.multi_face_landmarks:

#             # Draw face mesh
#             mp_drawing.draw_landmarks(
#                 frame,
#                 face_landmarks,
#                 mp_face_mesh.FACEMESH_TESSELATION
#             )

#             landmarks = face_landmarks.landmark

#             # ==========================================
#             # CALCULATE EAR
#             # ==========================================

#             left_ear = calculate_ear(
#                 landmarks,
#                 LEFT_EYE
#             )

#             right_ear = calculate_ear(
#                 landmarks,
#                 RIGHT_EYE
#             )

#             # Average EAR
#             ear = (left_ear + right_ear) / 2.0

#             # ==========================================
#             # EYE OPEN / CLOSED
#             # ==========================================

#             EAR_THRESHOLD = 0.22

#             if ear < EAR_THRESHOLD:

#                 eye_status = "CLOSED"

#             else:

#                 eye_status = "OPEN"

#             # ==========================================
#             # DISPLAY EAR
#             # ==========================================

#             cv2.putText(
#                 frame,
#                 f"EAR: {ear:.2f}",
#                 (30, 40),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.8,
#                 (0, 255, 255),
#                 2
#             )

#             # ==========================================
#             # DISPLAY EYE STATUS
#             # ==========================================

#             cv2.putText(
#                 frame,
#                 f"Eyes: {eye_status}",
#                 (30, 80),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.9,
#                 (0, 255, 0),
#                 2
#             )


#     # ==========================================
#     # SHOW CAMERA
#     # ==========================================

#     cv2.imshow(
#         "Driver Monitoring System",
#         frame
#     )

#     # Press Q to exit
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# # ==========================================
# # RELEASE
# # ==========================================

# cap.release()
# cv2.destroyAllWindows()




import cv2
import mediapipe as mp
import numpy as np
import winsound
import threading
import time


# ==========================================
# MEDIAPIPE FACE MESH
# ==========================================

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# ==========================================
# EYE LANDMARK INDICES
# ==========================================

# Left eye
LEFT_EYE = [33, 160, 158, 133, 153, 144]

# Right eye
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


# ==========================================
# EAR FUNCTION
# ==========================================

def calculate_ear(landmarks, eye_indices):

    p1 = np.array([
        landmarks[eye_indices[0]].x,
        landmarks[eye_indices[0]].y
    ])

    p2 = np.array([
        landmarks[eye_indices[1]].x,
        landmarks[eye_indices[1]].y
    ])

    p3 = np.array([
        landmarks[eye_indices[2]].x,
        landmarks[eye_indices[2]].y
    ])

    p4 = np.array([
        landmarks[eye_indices[3]].x,
        landmarks[eye_indices[3]].y
    ])

    p5 = np.array([
        landmarks[eye_indices[4]].x,
        landmarks[eye_indices[4]].y
    ])

    p6 = np.array([
        landmarks[eye_indices[5]].x,
        landmarks[eye_indices[5]].y
    ])

    # Vertical distances
    vertical_1 = np.linalg.norm(p2 - p6)
    vertical_2 = np.linalg.norm(p3 - p5)

    # Horizontal distance
    horizontal = np.linalg.norm(p1 - p4)

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)

    return ear


# ==========================================
# ALARM FUNCTION
# ==========================================

alarm_running = False


def play_alarm():

    global alarm_running

    if alarm_running:
        return

    alarm_running = True

    # Three beep alarm
    for i in range(3):

        winsound.Beep(1000, 500)   #(freq,duration)  0.5 sec 500 millisecnd
        time.sleep(0.2)       # gap btw beeps 

    alarm_running = False



# ==========================================
# CAMERA
# ==========================================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()

# ==========================================
# DROWSINESS VARIABLES
# ==========================================

EAR_THRESHOLD = 0.22

# Eyes must remain closed for 2 seconds
CLOSED_TIME_THRESHOLD = 2.0

closed_start_time = None


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    ret, frame = cap.read()
                                   # read all the frames in camera
    if not ret:                 # ret = gives boolean value

        print("Camera not detected")
        break


    # ==========================================
    # CONVERT BGR → RGB
    # ==========================================

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # ==========================================
    # PROCESS FACE
    # ==========================================

    results = face_mesh.process(rgb_frame)


    # ==========================================
    # FACE DETECTED
    # ==========================================

# “First, I check whether MediaPipe has detected any face landmarks. If a face is
# detected, the for loop allows me to process the landmarks of each detected face individually.
    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:


            # ==========================================
            # DRAW FACE MESH
            # ==========================================
# Face
#  ↓
# Landmark points
#  ↓
# Connections
#  ↓
# Face Mesh
            mp_drawing.draw_landmarks(                                    
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION      # to connect all the landmark points
            )


            landmarks = face_landmarks.landmark


            # ==========================================
            # CALCULATE EAR
            # ==========================================

            left_ear = calculate_ear(
                landmarks,
                LEFT_EYE
            )

            right_ear = calculate_ear(
                landmarks,
                RIGHT_EYE
            )


            # Average EAR
            ear = (left_ear + right_ear) / 2.0


            # ==========================================
            # EYE OPEN / CLOSED
            # ==========================================

            if ear < EAR_THRESHOLD:

                eye_status = "CLOSED"


                # Start timer when eyes first close
                if closed_start_time is None:

                    closed_start_time = time.time()


                # Calculate how long eyes are closed
                closed_duration = time.time() - closed_start_time
                
# eg=Eye closed at 10:00:00
# Current time 10:00:01.5

# Closed duration = 1.5 seconds

                # ==========================================
                # DROWSINESS DETECTION
                # ==========================================

                if closed_duration >= CLOSED_TIME_THRESHOLD:

                    cv2.putText(
                        frame,
                        "DROWSINESS ALERT!",
                        (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),  # red 
                        3
                    )


                    cv2.putText(
                        frame,
                        "WAKE UP!",
                        (30, 170),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        3
                    )


                    # Start alarm in separate thread
# “When the driver is detected as drowsy, I check whether the alarm is 
# already running. If it is not running, I create a separate thread for the alarm 
# and start it. This allows the warning sound to run without blocking the camera and face detection process.


                    if not alarm_running:

                        alarm_thread = threading.Thread(
                            target=play_alarm
                        )

                        alarm_thread.daemon = True
                        alarm_thread.start()


            else:

                eye_status = "OPEN"

                # Reset timer when eyes open
                closed_start_time = None


            # ==========================================
            # DISPLAY EAR
            # ==========================================

            cv2.putText(
                frame,
                f"EAR: {ear:.2f}",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )


            # ==========================================
            # DISPLAY EYE STATUS
            # ==========================================
#(x, y) = (left/right, up/down)
            if eye_status == "OPEN":

                cv2.putText(
                    frame,
                    "Eyes: OPEN",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "Eyes: CLOSED",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )


            # ==========================================
            # DISPLAY CLOSED TIME
            # ==========================================

            if closed_start_time is not None:

                closed_duration = time.time() - closed_start_time

                cv2.putText(
                    frame,
                    f"Closed: {closed_duration:.1f}s",
                    (30, 210),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )


    else:

        # No face detected
        cv2.putText(
            frame,
            "Face Not Detected",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        # Reset timer
        closed_start_time = None

#Face detected
#     ↓
# Eyes closed
#     ↓
# Closed = 1.5 sec
#     ↓
# Face disappears
#     ↓
# Timer reset → None

#None
#  ↓
# Eyes not closed / Timer not started

# time.time()
#  ↓
# Eyes closed / Timer started


    # ==========================================
    # SHOW CAMERA
    # ==========================================

    cv2.imshow(
        "Driver Monitoring System",
        frame
    )


    # ==========================================
    # PRESS Q TO EXIT
    # ==========================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ==========================================
# RELEASE
# ==========================================

cap.release()

cv2.destroyAllWindows()