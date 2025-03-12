import os
import shutil

# Define source folder 
source_folder = "E:\python programming internship 2025\CodeAlpha_File_Organizer" 

# Define Destination Folder Names & File Types
destination_folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Others": []
}

# Create necessary folders inside "Organized_Files"
organized_folder = os.path.join(source_folder, "Organized_Files")
if not os.path.exists(organized_folder):
    os.makedirs(organized_folder)

for folder in destination_folders.keys():
    folder_path = os.path.join(organized_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files based on extensions
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    
    if os.path.isfile(file_path):  # Ensure it's a file
        moved = False
        for folder, extensions in destination_folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(organized_folder, folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break
        
        if not moved:  # If file type not found, move to "Others"
            shutil.move(file_path, os.path.join(organized_folder, "Others", file))
            print(f"Moved: {file} → Others")

print("✅ File Organization Completed Successfully!")
