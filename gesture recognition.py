import cv2
import numpy as np
import joblib
import pyautogui  # Automation library

# Load trained model and label encoder
model = joblib.load("gesture_svm_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Gesture-to-Action Mapping
gesture_actions = {
    "Fist": lambda: pyautogui.press("space"),  # Play/Pause
    "Palm": lambda: pyautogui.press("volumeup"),  # Volume Up
    "ThumbsUp": lambda: pyautogui.press("volumedown"),  # Volume Down
}

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture image from webcam")
        break

    # Preprocess frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (64, 64)).flatten()

    # Predict Gesture
    prediction = model.predict([resized])
    gesture = label_encoder.inverse_transform(prediction)[0]

    # Execute Mapped Action
    if gesture in gesture_actions:
        gesture_actions[gesture]()  # Call corresponding function

    # Display Gesture
    cv2.putText(frame, f"Gesture: {gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Gesture Control", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
