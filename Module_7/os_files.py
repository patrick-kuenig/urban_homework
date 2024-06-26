import os
import time

path = 'C:\\Windows\\Logs'

for root, dirs, files in os.walk(path, topdown=True):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        time_formatted = time.strftime('%Y-%m-%d %H:%M', time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Found file {file}, Path: {file_path}, Size: {file_size} bytes, Last change: {time_formatted},'
              f'Parent directory: {parent_dir}')
