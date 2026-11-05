import os
import shutil

# Downloads folder (Update this to your actual path if needed)
DOWNLOADS = r"C:\Users\Sidi AbdJelil\Downloads"

# File categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".odt"],
    "Music": [".mp3", ".wav", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".cpp"]
}

def organize_files():
    if not os.path.isdir(DOWNLOADS):
        print(f"Error: The folder '{DOWNLOADS}' was not found!")
        return

    moved = 0

    for filename in os.listdir(DOWNLOADS):
        file_path = os.path.join(DOWNLOADS, filename)

        # Skip if it's a directory
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        categorized = False

        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                folder = os.path.join(DOWNLOADS, category)
                os.makedirs(folder, exist_ok=True)
                
                destination = os.path.join(folder, filename)
                
                # Handle duplicates by renaming instead of just skipping
                if os.path.exists(destination):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(destination):
                        new_name = f"{base}_{counter}{ext}"
                        destination = os.path.join(folder, new_name)
                        counter += 1

                try:
                    shutil.move(file_path, destination)
                    print(f"Moved: {filename} -> {category}")
                    moved += 1
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
                
                categorized = True
                break # Stop checking other categories once matched
        
        # Optional: Move uncategorized files to an "Others" folder
        if not categorized and extension != "":
            folder = os.path.join(DOWNLOADS, "Others")
            os.makedirs(folder, exist_ok=True)
            destination = os.path.join(folder, filename)
            
            if os.path.exists(destination):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(folder, f"{base}_{counter}{ext}")
                    counter += 1
            
            try:
                shutil.move(file_path, destination)
                print(f"Moved: {filename} -> Others")
                moved += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    print("\nOrganization complete!")
    print(f"Total files moved: {moved}")

print("================================")
print(" PYTHON ORGANIZER")
print("================================")

organize_files()
