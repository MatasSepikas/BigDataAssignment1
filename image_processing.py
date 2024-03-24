import cv2
import numpy as np
import os

def find_equal_threshold(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = np.bincount(gray_image.ravel(), minlength=256)
    cdf = np.cumsum(hist)
    threshold = np.where(cdf >= cdf[-1] // 2)[0][0]
    return threshold

def convert_to_equal_black_white(image, threshold):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bw_image = np.where(gray_image > threshold, 255, 0).astype(np.uint8)
    return bw_image

def apply_averaging_blur(image, kernel_size=(5, 5)):
    blurred_image = cv2.blur(image, kernel_size)
    return blurred_image

def add_salt_pepper_noise_based_on_bw(image, bw_image):
    total_pixels = image.shape[0] * image.shape[1]
    black_indices = np.where(bw_image == 0)
    num_black_pixels = black_indices[0].size
    num_noise_pixels = num_black_pixels // 10 
    noise_indices = np.random.choice(total_pixels, num_noise_pixels, replace=False)
    rows, cols = np.unravel_index(noise_indices, (image.shape[0], image.shape[1]))
    salt_indices = rows[:num_noise_pixels // 2], cols[:num_noise_pixels // 2]
    image[salt_indices] = [255, 255, 255]
    pepper_indices = rows[num_noise_pixels // 2:], cols[num_noise_pixels // 2:]
    image[pepper_indices] = [0, 0, 0]
    return image

def create_subfolder(folder_path, subfolder):
    os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

def process_image_bw(image_path, folder_path, subfolder):
    image = cv2.imread(image_path)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(image_path)), convert_to_equal_black_white(image, find_equal_threshold(image)))

def process_image_blur(image_path, folder_path, subfolder):
    image = cv2.imread(image_path)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(image_path)), apply_averaging_blur(image))
    
def process_image_noise(original_image_path, folder_path, subfolder, bw_image_path):
    bw_image = cv2.imread(bw_image_path, cv2.IMREAD_GRAYSCALE) 
    image = cv2.imread(original_image_path)
    noise_image = add_salt_pepper_noise_based_on_bw(image, bw_image)
    cv2.imwrite(os.path.join(folder_path, subfolder, os.path.basename(original_image_path)), noise_image)
