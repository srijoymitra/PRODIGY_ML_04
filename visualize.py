import os
import cv2
import matplotlib.pyplot as plt
import random

dataset_path = r"C:\Users\profa\Downloads\archive\leapGestRecog"

def is_image_file(filename):
    """Check if a file is an image"""
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))

def show_sample_images(dataset_path, num_samples=5):
    folders = [f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f))]
    plt.figure(figsize=(10, 5))

    for i, folder in enumerate(random.sample(folders, min(num_samples, len(folders)))):
        sub_folder_path = os.path.join(dataset_path, folder)
        subfolders = [f for f in os.listdir(sub_folder_path) if os.path.isdir(os.path.join(sub_folder_path, f))]

        if not subfolders:
            print(f"⚠️ No subfolders found in {folder}. Skipping.")
            continue

        # Choose a random subfolder
        subfolder = random.choice(subfolders)
        image_folder = os.path.join(sub_folder_path, subfolder)

        image_files = [f for f in os.listdir(image_folder) if is_image_file(f)]
        if not image_files:
            print(f"⚠️ No images found in {image_folder}. Skipping.")
            continue
        
        image_file = random.choice(image_files)
        image_path = os.path.join(image_folder, image_file)

        img = cv2.imread(image_path)
        if img is None:
            print(f"⚠️ Unable to read {image_path}. Skipping.")
            continue
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, num_samples, i+1)
        plt.imshow(img)
        plt.title(folder)
        plt.axis("off")

    plt.show()

show_sample_images(dataset_path)
