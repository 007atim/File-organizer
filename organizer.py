import os
import shutil

# Downloads folder
DOWNLOADS = os.path.expanduser("~/Downloads")

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
print("Downloads folder not found!")
return

moved = 0

for filename in os.listdir(DOWNLOADS):
file_path = os.path.join(DOWNLOADS, filename)

if not os.path.isfile(file_path):
continue

extension = os.path.splitext(filename)[1].lower()

for category, extensions in CATEGORIES.items():
if extension in extensions:
folder = os.path.join(DOWNLOADS, category)
os.makedirs(folder, exist_ok=True)

destination = os.path.join(folder, filename)

if os.path.exists(destination):
print("Skipped duplicate:", filename)
break

shutil.move(file_path, destination)
print("Moved:", filename, "->", category)
moved += 1
break

print("\nOrganization complete!")
print("Total files moved:", moved)


print("================================")
print(" PYTHON ORGANIZER")
print("================================")

organize_files()
