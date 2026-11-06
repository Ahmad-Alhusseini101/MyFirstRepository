import cv2
import mediapipe as mp
import pyautogui
import math

# Disable PyAutoGUI failsafe for testing
pyautogui.FAILSAFE = False

# Initialize MediaPipe Face Mesh with refined landmarks
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Sensitivity multipliers
SENSITIVITY_X = 10
SENSITIVITY_Y = 10

# Balanced Smoothing (EMA) factor
SMOOTHING_FACTOR = 0.7
prev_screen_x, prev_screen_y = screen_w / 2, screen_h / 2

# Click & Drag variables
BLINK_THRESHOLD = 0.015  # Adjust this based on your terminal prints
blink_counter = 0
is_dragging = False

def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print("Starting Custom Eye Mouse... Press 'ESC' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    ih, iw, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            
            # ==================== 1. CURSOR MOVEMENT ====================
            iris_landmark = face_landmarks.landmark[473]
            
            target_x = screen_w / 2 + (iris_landmark.x - 0.5) * screen_w * SENSITIVITY_X
            target_y = screen_h / 2 + (iris_landmark.y - 0.5) * screen_h * SENSITIVITY_Y

            target_x = max(0, min(screen_w - 1, target_x))
            target_y = max(0, min(screen_h - 1, target_y))

            # Apply Smoothing
            screen_x = prev_screen_x + SMOOTHING_FACTOR * (target_x - prev_screen_x)
            screen_y = prev_screen_y + SMOOTHING_FACTOR * (target_y - prev_screen_y)
            prev_screen_x, prev_screen_y = screen_x, screen_y

            try:
                pyautogui.moveTo(screen_x, screen_y)
            except Exception:
                pass


            # ==================== 2. BLINK & CLICK LOGIC ====================
            upper_eyelid = face_landmarks.landmark[159]
            lower_eyelid = face_landmarks.landmark[145]
            
            # Variable correctly defined here!
            eye_vertical_distance = calculate_distance(upper_eyelid, lower_eyelid)
            
            # Print this to your terminal to find your exact open/closed numbers
            print(f"Eye Distance: {eye_vertical_distance:.4f}")

            if eye_vertical_distance < BLINK_THRESHOLD:
                blink_counter += 1
                if blink_counter > 20 and not is_dragging:
                    pyautogui.mouseDown()
                    is_dragging = True
                    print("Dragging Started (Mouse Down)")
            else:
                if is_dragging:
                    pyautogui.mouseUp()
                    is_dragging = False
                    print("Dragging Ended (Mouse Up)")
                elif 3 < blink_counter <= 15:
                    pyautogui.click()
                    print("Standard Click Triggered!")
                
                blink_counter = 0


            # ==================== DEBUG VISUAL ====================
            iris_x = int(iris_landmark.x * iw)
            iris_y = int(iris_landmark.y * ih)
            cv2.circle(frame, (iris_x, iris_y), 5, (0, 255, 0), -1)

    cv2.imshow('Custom Eye Mouse', frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()