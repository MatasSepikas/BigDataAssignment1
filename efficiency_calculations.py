import time
import pandas as pd

def measure_execution_time(func, path):
    start_time = time.time()
    func(path)
    end_time = time.time()
    return round(end_time - start_time, 2)

def calculate_metrics(sequential_time, parallel_time, n_processors):
    speedup = sequential_time / parallel_time
    efficiency = speedup / n_processors
    total_parallel_overhead = (n_processors * parallel_time) - sequential_time    
    return speedup, total_parallel_overhead, efficiency

def create_execution_time_table(times_dict):
    df = pd.DataFrame(list(times_dict.items()), columns=['Method', 'Execution time (seconds)'])
    print("Execution times for all methods:")
    print(df)
    return df

def create_efficiency_metrics_table(sequential_time, times_dict, n_processors):
    metrics = []
    for method, parallel_time in times_dict.items():
        if not method.startswith('Sequential'):  # Filter out the sequential methods
            speedup, overhead, efficiency = calculate_metrics(sequential_time, parallel_time, n_processors)
            metrics.append([method, round(speedup, 2),  round(overhead, 2), round(efficiency, 2)])
    df = pd.DataFrame(metrics, columns=['Method', 'Speedup', 'Total parallel overhead', 'Efficiency'])
    print("Efficiency metrics for parallel methods:")
    print(df)
    return df
