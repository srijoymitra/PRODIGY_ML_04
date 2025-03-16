import os

dataset_path = r"C:\Users\profa\Downloads\archive"  # Your dataset path

# Count files in each class
class_counts = {}
for class_name in os.listdir(dataset_path):
    class_folder = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_folder):
        class_counts[class_name] = len(os.listdir(class_folder))

# Print dataset summary
for class_name, count in class_counts.items():
    print(f"Class '{class_name}': {count} images")

print(f"\nTotal Classes: {len(class_counts)}")
print(f"Total Images: {sum(class_counts.values())}")
