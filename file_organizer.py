import os
import shutil

categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".csv": "Documents",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".mkv": "Videos"
}

folder = input("Enter folder path: ").strip()

if not os.path.isdir(folder):
    print("Error: Folder does not exist.")
    exit()

files = os.listdir(folder)

moved_count = 0
unknown_count = 0
skipped_count = 0

for file in files:

    old_path = os.path.join(folder, file)

    if not os.path.isfile(old_path):
        continue

    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if file == os.path.basename(__file__):
        continue

    if extension not in categories:
        print(file, "→ No category")
        unknown_count += 1
        continue

    category = categories[extension]

    category_path = os.path.join(folder, category)

    os.makedirs(category_path, exist_ok=True)

    new_path = os.path.join(category_path, file)

    if os.path.exists(new_path):
        print(file, "→ Skipped (file already exists)")
        skipped_count += 1
        continue

    shutil.move(old_path, new_path)

    print(file, "→", category)
    moved_count += 1

print()
print("Organization complete!")
print("Files moved:", moved_count)
print("Unknown files:", unknown_count)
print("Skipped files:", skipped_count)
