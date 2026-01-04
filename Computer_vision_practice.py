import cv2
import mediapipe as mp
import pyautogui
import time
import math

# --- Configuration ---
V_SCROLL_SPEED = 25      
H_SCROLL_SPEED = 15      
PAGE_COOLDOWN = 1.5      
ZOOM_COOLDOWN = 0.8      

# Sensitivity Thresholds
DEAD_ZONE = 0.08         
PAGE_TURN_LIMIT = 0.35   
ZOOM_SENSITIVITY = 0.02  

# --- Setup MediaPipe ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# --- Variables for State ---
last_page_turn = time.time()
last_zoom_time = time.time()
base_face_size = None  # This will calibrate to your sitting position

cam = cv2.VideoCapture(0)

print("System Ready.")
print("- Lean FORWARD to Zoom In, BACK to Zoom Out")
print("- Move Head slightly to Scroll (All Directions)")
print("- Move Head FAR Left/Right to Change Page")
print("- Press 'c' to Calibrate (set your neutral sitting position)")

while True:
    ret, frame = cam.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        
        # 1. Get Coordinates
        nose = landmarks[1]
        left_eye = landmarks[33]
        right_eye = landmarks[263]
        
        # Calculate current face size (Distance between eyes)
        face_size = math.sqrt((right_eye.x - left_eye.x)**2 + (right_eye.y - left_eye.y)**2)
        
        # Calibration logic: Set the neutral distance the first time
        if base_face_size is None:
            base_face_size = face_size
            
        current_time = time.time()
        status = "Reading"
        color = (255, 255, 255)

        # --- ZOOM LOGIC (Leaning) ---
        if current_time - last_zoom_time > ZOOM_COOLDOWN:
            if face_size > base_face_size + ZOOM_SENSITIVITY:
                pyautogui.hotkey('ctrl', '+')
                last_zoom_time = current_time
                status = "ZOOM IN"
                color = (0, 255, 255)
            elif face_size < base_face_size - ZOOM_SENSITIVITY:
                pyautogui.hotkey('ctrl', '-')
                last_zoom_time = current_time
                status = "ZOOM OUT"
                color = (0, 165, 255)

        # --- SCROLL & PAGE LOGIC (Head Position) ---
        val_x = nose.x - 0.5
        val_y = nose.y - 0.5

        # Vertical Scroll
        if abs(val_y) > DEAD_ZONE:
            pyautogui.scroll(V_SCROLL_SPEED if val_y < 0 else -V_SCROLL_SPEED)
            status = "Scrolling Vertical"
            color = (0, 255, 0)

        # Horizontal Movement & Page Turning
        if abs(val_x) > DEAD_ZONE:
            if abs(val_x) > PAGE_TURN_LIMIT:
                if current_time - last_page_turn > PAGE_COOLDOWN:
                    pyautogui.press('left' if val_x < 0 else 'right')
                    last_page_turn = current_time
                status = "PAGE TURN"
                color = (255, 0, 255)
            else:
                with pyautogui.hold('shift'):
                    pyautogui.scroll(H_SCROLL_SPEED if val_x > 0 else -H_SCROLL_SPEED)
                status = "Panning Side-to-Side"
                color = (255, 255, 0)

        # --- Visual UI ---
        nx, ny = int(nose.x * w), int(nose.y * h)
        cv2.circle(frame, (nx, ny), 6, color, -1)
        
        # Draw the neutral zone box
        cv2.rectangle(frame, 
                      (int((0.5-DEAD_ZONE)*w), int((0.5-DEAD_ZONE)*h)), 
                      (int((0.5+DEAD_ZONE)*w), int((0.5+DEAD_ZONE)*h)), 
                      (100, 100, 100), 1)

        cv2.putText(frame, f"Action: {status}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        cv2.putText(frame, "Lean for Zoom | Move for Scroll", (20, h-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow('PDF Face Controller Pro', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        base_face_size = face_size
        print("Recalibrated!")

cam.release()
cv2.destroyAllWindows()