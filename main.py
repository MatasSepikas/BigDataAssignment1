from starmap_parallel import process_images_multiproc_starmap_async_bw, process_images_multiproc_starmap_async_blur, process_images_multiproc_starmap_async_noise
from map_parallel import process_images_multiproc_map_bw, process_images_multiproc_map_blur, process_images_multiproc_map_noise
from apply_parallel import process_images_multiproc_apply_async_bw, process_images_multiproc_apply_async_blur, process_images_multiproc_apply_async_noise
from sequential import process_images_sequential_bw, process_images_sequential_blur, process_images_sequential_noise
from efficiency_calculations import measure_execution_time, create_execution_time_table, create_efficiency_metrics_table
import multiprocessing

if __name__ == '__main__':
    folder_path = 'C:/Users/matas/Desktop/Images'
    n_processors = multiprocessing.cpu_count() - 2
    times_dict = {
        'Sequential thresholding': measure_execution_time(process_images_sequential_bw, folder_path),
        'Sequential blur': measure_execution_time(process_images_sequential_blur, folder_path),
        'Sequential noise': measure_execution_time(process_images_sequential_noise, folder_path),
        'Starmap async thresholding': measure_execution_time(process_images_multiproc_starmap_async_bw, folder_path),
        'Starmap async blur': measure_execution_time(process_images_multiproc_starmap_async_blur, folder_path),
        'Starmap async noise': measure_execution_time(process_images_multiproc_starmap_async_noise, folder_path),
        'Map thresholding': measure_execution_time(process_images_multiproc_map_bw, folder_path),
        'Map blur': measure_execution_time(process_images_multiproc_map_blur, folder_path),
        'Map noise': measure_execution_time(process_images_multiproc_map_noise, folder_path),
        'Apply async thresholding': measure_execution_time(process_images_multiproc_apply_async_bw, folder_path),
        'Apply async blur': measure_execution_time(process_images_multiproc_apply_async_blur, folder_path),
        'Apply async noise': measure_execution_time(process_images_multiproc_apply_async_noise, folder_path),
    }
    execution_time_table = create_execution_time_table(times_dict)
    sequential_time = sum(times_dict[key] for key in times_dict if 'Sequential' in key) / 3 
    efficiency_metrics_table = create_efficiency_metrics_table(sequential_time, times_dict, n_processors)