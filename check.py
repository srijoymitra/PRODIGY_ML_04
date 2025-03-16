import os

dataset_path = r"C:\Users\profa\Downloads\archive\leapGestRecog"

# Check folder structure
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    print(f"📂 {folder} -> {'Folder' if os.path.isdir(folder_path) else 'File'}")

    if os.path.isdir(folder_path):  # If it's a folder, check its contents
        sub_files = os.listdir(folder_path)
        print(f"   📄 Contains {len(sub_files)} items (First 5: {sub_files[:5]})")
