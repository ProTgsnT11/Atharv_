import os
import shutil
import sys

# Mapping extensions to category folder names
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code_and_Scripts": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json", ".sql"],
    "Executables": [".exe", ".msi", ".dmg", ".sh", ".bat"]
}

def organize_folder(target_dir):
    if not os.path.exists(target_dir):
        print(f"❌ Error: Directory '{target_dir}' does not exist.")
        return

    print(f"🔍 Scanning folder: {target_dir}\n")

    moved_count = 0

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        # Skip directories and hidden files
        if os.path.isdir(item_path) or item.startswith('.'):
            continue

        # Get file extension
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Find matching category
        target_category = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                target_category = category
                break

        # Create target directory if it doesn't exist
        category_dir = os.path.join(target_dir, target_category)
        os.makedirs(category_dir, exist_ok=True)

        # Move file
        destination_path = os.path.join(category_dir, item)
        shutil.move(item_path, destination_path)
        print(f"🚚 Moved: {item} ➔ {target_category}/")
        moved_count += 1

    print(f"\n✅ Done! Organized {moved_count} file(s).")

if __name__ == "__main__":
    # If path provided via terminal, use it; otherwise default to current folder
    target_folder = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    organize_folder(target_folder)
