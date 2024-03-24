import os
import multiprocessing
from image_processing import create_subfolder, process_image_bw, process_image_blur, process_image_noise

def process_images_multiproc_starmap_async_bw(folder_path):
    subfolder = 'BlackWhite'
    create_subfolder(folder_path, subfolder)
    tasks = [(os.path.join(folder_path, image_name), folder_path, subfolder) 
             for image_name in os.listdir(folder_path) 
             if image_name.lower().endswith('.jpg')]
    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.starmap_async(process_image_bw, tasks).wait()

def process_images_multiproc_starmap_async_blur(folder_path):
    subfolder = 'Blurred'
    create_subfolder(folder_path, subfolder)
    tasks = [(os.path.join(folder_path, image_name), folder_path, subfolder) 
             for image_name in os.listdir(folder_path) 
             if image_name.lower().endswith('.jpg')]
    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.starmap_async(process_image_blur, tasks).wait()

def process_images_multiproc_starmap_async_noise(folder_path):
    subfolder = 'Noise'
    create_subfolder(folder_path, subfolder)
    tasks = []
    for image_name in os.listdir(os.path.join(folder_path, 'BlackWhite')):
        if image_name.lower().endswith('.jpg'):
            original_image_path = os.path.join(folder_path, image_name) 
            bw_image_path = os.path.join(folder_path, 'BlackWhite', image_name) 
            tasks.append((original_image_path, folder_path, subfolder, bw_image_path))

    with multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2)) as pool:
        pool.starmap_async(process_image_noise, tasks).wait()