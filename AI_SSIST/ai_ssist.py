import cv2
import mediapipe as mp
import pyttsx3
import webbrowser
import time
import os

# === Initialize TTS ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("🔊", text)
    engine.say(text)
    engine.runAndWait()

# === Mediapipe Setup ===
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# === Camera Setup ===
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

prev_count = None
gesture_hold_time = 1.0
gesture_start_time = None

def get_finger_count(hand_landmarks):
    fingers = []

    # Thumb (x comparison)
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (y comparison)
    tips = [8, 12, 16, 20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    finger_count = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_count = get_finger_count(hand_landmarks)

    if finger_count is not None:
        # Show finger count
        cv2.putText(img, f"Fingers: {finger_count}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (139, 0, 139), 3)

        # Show operation text
        action_text = {
            0: "Exiting...",
            1: "Reading data.txt",
            2: "Opening YouTube",
            3: "Opening Gmail",
            4: "Opening News",
            5: "Playing Music"
        }
        if finger_count in action_text:
            cv2.putText(img, action_text[finger_count], (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255), 2)

        if finger_count != prev_count:
            gesture_start_time = time.time()
            prev_count = finger_count
        elif time.time() - gesture_start_time > gesture_hold_time:
            if finger_count == 0:
                speak("Goodbye! Closing assistant.")
                break

            elif finger_count == 1:
                if os.path.exists("data.txt"):
                    with open("data.txt", "r") as f:
                        text = f.read()
                        speak(text)
                else:
                    speak("Data file not found.")

            elif finger_count == 2:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            elif finger_count == 3:
                speak("Opening Gmail")
                webbrowser.open("https://mail.google.com")

            elif finger_count == 4:
                speak("Opening news website")
                webbrowser.open("https://news.google.com")

            elif finger_count == 5:
                if os.path.exists("music.mp3"):
                    speak("Playing music now.")
                    os.startfile("music.mp3")
                else:
                    speak("Music file not found.")

            gesture_start_time = time.time() + 1  # Reset timer

    cv2.imshow("AI SSIST – Gesture Assistant", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







