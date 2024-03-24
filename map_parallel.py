import cv2
import os
import multiprocessing
from image_processing import convert_to_equal_black_white, find_equal_threshold, apply_averaging_blur, add_salt_pepper_noise_based_on_bw, create_subfolder

def process_image_map_bw(args):
    image_path, folder_path, subfolder = args
    image = cv2.imread(image_path)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(image_path)), convert_to_equal_black_white(image, find_equal_threshold(image)))

def process_image_map_blur(args):
    image_path, folder_path, subfolder = args
    image = cv2.imread(image_path)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(image_path)), apply_averaging_blur(image))
    
def process_image_map_noise(args):
    image_path, folder_path, subfolder = args
    original_image = cv2.imread(image_path)
    bw_image_path = os.path.join(folder_path, 'BlackWhite', os.path.basename(image_path))
    bw_image = cv2.imread(bw_image_path, cv2.IMREAD_GRAYSCALE)
    noise_image = add_salt_pepper_noise_based_on_bw(original_image, bw_image)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(image_path)), noise_image)
    
def process_images_multiproc_map_bw(folder_path):
    subfolder = 'BlackWhite'
    create_subfolder(folder_path, subfolder)
    tasks = [(os.path.join(folder_path, image_name), folder_path, subfolder) 
             for image_name in os.listdir(folder_path) 
             if image_name.lower().endswith('.jpg')]
    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.map(process_image_map_bw, tasks)

def process_images_multiproc_map_blur(folder_path):
    subfolder = 'Blurred'
    create_subfolder(folder_path, subfolder)
    tasks = [(os.path.join(folder_path, image_name), folder_path, subfolder) 
             for image_name in os.listdir(folder_path) 
             if image_name.lower().endswith('.jpg')]
    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.map(process_image_map_blur, tasks)

def process_images_multiproc_map_noise(folder_path):
    subfolder = 'Noise'
    create_subfolder(folder_path, subfolder)
    tasks = [(os.path.join(folder_path, image_name), folder_path, subfolder)
             for image_name in os.listdir(folder_path)
             if image_name.lower().endswith('.jpg')]
    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.map(process_image_map_noise, tasks)