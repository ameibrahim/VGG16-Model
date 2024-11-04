import os
import shutil

subfolders = ["Cat", "Dog"]

def consolidate_images_from_folders(data_directory):
    # Paths for training, validation, and testing directories
    train_dir = os.path.join(data_directory, 'train')
    validation_dir = os.path.join(data_directory, 'dev')
    test_dir = os.path.join(data_directory, 'test')

    # List of all split directories
    split_dirs = [train_dir, validation_dir, test_dir]

    for split_dir in split_dirs:
        for subfolder in subfolders:
            subfolder_path = os.path.join(split_dir, subfolder)
            if os.path.exists(subfolder_path):
                # List all image files in the subfolder
                images = [f for f in os.listdir(subfolder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
                
                # Move each image back to the original folder in `data/`
                for image in images:
                    source_path = os.path.join(subfolder_path, image)
                    destination_path = os.path.join(data_directory, subfolder, image)
                    
                    # Ensure the destination subfolder exists
                    os.makedirs(os.path.join(data_directory, subfolder), exist_ok=True)

                    # Move the image
                    shutil.move(source_path, destination_path)
    
    # Optional: Remove empty directories after consolidation
    for split_dir in split_dirs:
        shutil.rmtree(split_dir)

# Specify the path to the main directory containing the training, validation, and test folders
data_directory = 'data/'

# Call the function to consolidate images
consolidate_images_from_folders(data_directory)