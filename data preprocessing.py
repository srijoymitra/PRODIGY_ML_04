import os
import cv2
from PIL import Image

# Set dataset folder path
dataset_folder = r"C:\Users\profa\Downloads\archive\leapGestRecog\leapGestRecog"

# Initialize counters
total_images = 0
unreadable_images = []

# Iterate through all subfolders (gestures)
for gesture_folder in os.listdir(dataset_folder):
    gesture_path = os.path.join(dataset_folder, gesture_folder)
    
    if not os.path.isdir(gesture_path):
        continue  # Skip non-folder files
    
    print(f"Checking folder: {gesture_folder}")

    # Iterate through images in each folder
    for img_name in os.listdir(gesture_path):
        img_path = os.path.join(gesture_path, img_name)
        
        # Check if file exists
        if not os.path.exists(img_path):
            print(f"❌ File missing: {img_path}")
            unreadable_images.append(img_path)
            continue

        # Try reading with OpenCV
        img_cv = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if img_cv is None:
            print(f"⚠️ OpenCV Failed: {img_path}")

            # Try reading with PIL (Pillow)
            try:
                img_pil = Image.open(img_path)
                img_pil.verify()  # Check if corrupted
            except Exception as e:
                print(f"❌ PIL Failed: {img_path} - {e}")
                unreadable_images.append(img_path)
                continue
        
        total_images += 1

print("\n✅ Dataset check completed!")
print(f"Total Readable Images: {total_images}")
print(f"Unreadable Images: {len(unreadable_images)}")

if unreadable_images:
    print("\n🔹 Unreadable Images List:")
    for img in unreadable_images:
        print(img)
