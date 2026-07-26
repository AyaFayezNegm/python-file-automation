import os
import shutil

# Source folder 
source_folder = "images"

# Destination folder 
destination_folder = "moved_images"

# Loop through all files in the source folder
for file_name in os.listdir(source_folder):

    # Check if the file is a JPG image
    if file_name.endswith(".jpg"):

        # Create the full path of the source file
        source_path = os.path.join(source_folder, file_name)

        # Create the full path of the destination file
        destination_path = os.path.join(destination_folder, file_name)

        # Move the image
        shutil.move(source_path, destination_path)

        # Print confirmation
        print(f"{file_name} moved successfully!")