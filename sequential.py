import os
from image_processing import create_subfolder, process_image_bw, process_image_blur, process_image_noise

def process_images_sequential_bw(folder_path):
    subfolder = 'BlackWhite'
    create_subfolder(folder_path, subfolder)
    for image_name in os.listdir(folder_path):
        if image_name.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_name)
            process_image_bw(image_path, folder_path, subfolder)

def process_images_sequential_blur(folder_path):
    subfolder = 'Blurred'
    create_subfolder(folder_path, subfolder)
    for image_name in os.listdir(folder_path):
        if image_name.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_name)
            process_image_blur(image_path, folder_path, subfolder)

def process_images_sequential_noise(folder_path):
    subfolder = 'Noise'
    create_subfolder(folder_path, subfolder)
    for image_name in os.listdir(os.path.join(folder_path, 'BlackWhite')):
        if image_name.lower().endswith('.jpg'):
            bw_image_path = os.path.join(folder_path, 'BlackWhite', image_name)
            original_image_path = os.path.join(folder_path, image_name)
            process_image_noise(original_image_path, folder_path, subfolder, bw_image_path)
