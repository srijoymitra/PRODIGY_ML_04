import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm
import joblib

# ✅ Correct Dataset Path
DATASET_PATH = r"C:\Users\profa\Downloads\archive\leapGestRecog"

# Function to load images and labels
def load_dataset(dataset_path):
    images = []
    labels = []

    if not os.path.exists(dataset_path):
        print(f"❌ Dataset path does not exist: {dataset_path}")
        return np.array([]), np.array([])

    for person_folder in tqdm(sorted(os.listdir(dataset_path)), desc="Processing Participants"):
        person_path = os.path.join(dataset_path, person_folder)

        if os.path.isdir(person_path):  # Ensure it's a directory
            for gesture_folder in sorted(os.listdir(person_path)):  # Loop through gestures
                gesture_path = os.path.join(person_path, gesture_folder)

                if os.path.isdir(gesture_path):  # Ensure it's a valid directory
                    for img_name in os.listdir(gesture_path):
                        img_path = os.path.join(gesture_path, img_name)

                        if os.path.isfile(img_path):  # Check if it's a file
                            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
                            if img is not None:
                                img = cv2.resize(img, (64, 64))  # Resize all images to same size
                                images.append(img.flatten())  # Flatten to 1D array
                                labels.append(gesture_folder)  # Use gesture folder name as label
                            else:
                                print(f"⚠️ Warning: Could not read image {img_path}")
                        else:
                            print(f"🔍 Skipping non-image file: {img_path}")

    if len(images) == 0:
        print("❌ No images found in dataset! Please check the dataset structure.")
        return np.array([]), np.array([])

    return np.array(images), np.array(labels)

# ✅ Load dataset
X, y = load_dataset(DATASET_PATH)

# ✅ Exit if dataset is empty
if X.size == 0 or y.size == 0:
    print("❌ Dataset loading failed. Exiting program.")
    exit()

# ✅ Convert labels to numerical values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# ✅ Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Check shape consistency
print(f"✅ Shape of X_train: {X_train.shape}")
print(f"✅ Shape of y_train: {y_train.shape}")

# ✅ Train SVM model
print("🚀 Training SVM Model...")
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# ✅ Test model
accuracy = model.score(X_test, y_test)
print(f"🏆 Model Accuracy: {accuracy * 100:.2f}%")

# ✅ Save model and label encoder
joblib.dump(model, "gesture_svm_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("✅ Model Training Completed & Saved!")
