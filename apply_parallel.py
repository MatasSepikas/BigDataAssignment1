import os
import multiprocessing
from image_processing import create_subfolder, process_image_bw, process_image_blur, process_image_noise

def process_images_multiproc_apply_async_bw(folder_path):
    subfolder = 'BlackWhite'
    create_subfolder(folder_path, subfolder)
    pool = multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2))
    for image_name in os.listdir(folder_path):
        if image_name.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_name)
            args = (image_path, folder_path, subfolder)
            pool.apply_async(process_image_bw, args=args)
    pool.close()
    pool.join()
    
def process_images_multiproc_apply_async_blur(folder_path):
    subfolder = 'Blurred'
    create_subfolder(folder_path, subfolder)
    pool = multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2))
    for image_name in os.listdir(folder_path):
        if image_name.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_name)
            args = (image_path, folder_path, subfolder)
            pool.apply_async(process_image_blur, args=args)
    pool.close()
    pool.join()

def process_images_multiproc_apply_async_noise(folder_path):
    subfolder = 'Noise'
    create_subfolder(folder_path, subfolder)
    pool = multiprocessing.Pool(max(1, multiprocessing.cpu_count() - 2))
    results = []
    for image_name in os.listdir(os.path.join(folder_path, 'BlackWhite')):
        if image_name.lower().endswith('.jpg'):
            bw_image_path = os.path.join(folder_path, 'BlackWhite', image_name)
            original_image_path = os.path.join(folder_path, image_name)
            args = (original_image_path, folder_path, subfolder, bw_image_path)
            result = pool.apply_async(process_image_noise, args=args)
            results.append(result)
    pool.close()
    pool.join()
        
        
        
        
        
        