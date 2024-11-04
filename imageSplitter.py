import os
import shutil
import random

subfolders = ["Cat", "Dog"]

def split_images_into_folders(data_directory, train_ratio, validation_ratio, test_ratio):
    # Create folders for training, validation, and testing
    train_dir = os.path.join(data_directory, 'train')
    validation_dir = os.path.join(data_directory, 'dev')
    test_dir = os.path.join(data_directory, 'test')

    # Create directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for directory in [train_dir, validation_dir, test_dir]:
        for subfolder in subfolders:
            subfolder_dir = os.path.join(directory, subfolder)
            os.makedirs(subfolder_dir, exist_ok=True)

    # List all subdirectories in the main directory
    subdirectories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]

    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(data_directory, subdirectory)

        # List all image files in the subdirectory
        all_images = [f for f in os.listdir(subdirectory_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

        # Shuffle the list of images randomly
        random.shuffle(all_images)

        # Calculate the number of images for each split
        total_images = len(all_images)
        train_split = int(train_ratio * total_images)
        validation_split = int(validation_ratio * total_images)

        # Split the images into training, validation, and testing sets
        train_images = all_images[:train_split]
        validation_images = all_images[train_split:train_split + validation_split]
        test_images = all_images[train_split + validation_split:]

        # Move images to the respective folders
        for image in train_images:
            shutil.move(os.path.join(subdirectory_path, image), os.path.join(train_dir, subdirectory, image))

        for image in validation_images:
            shutil.move(os.path.join(subdirectory_path, image), os.path.join(validation_dir, subdirectory, image))

        for image in test_images:
            shutil.move(os.path.join(subdirectory_path, image), os.path.join(test_dir, subdirectory, image))

    # Delete the original subfolders after moving the images
    for subfolder in subfolders:
        subfolder_path = os.path.join(data_directory, subfolder)
        if os.path.exists(subfolder_path):
            shutil.rmtree(subfolder_path)

# Specify the path to the main directory containing subdirectories for each class
data_directory = 'data/'

# Specify the split ratios
train_ratio = 0.7
validation_ratio = 0.2
test_ratio = 0.1

# Call the function to split images into training, validation, and testing sets
split_images_into_folders(data_directory, train_ratio, validation_ratio, test_ratio)