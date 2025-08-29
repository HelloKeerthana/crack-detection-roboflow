import os

folder_path = "C:\\Users\\satya\\OneDrive\\Desktop\\keerthana\\DL_APSAC\\ds\\tiled_dataset"

# Size threshold in bytes (200kB = 200 * 1024)
size_threshold = 190 * 1024
deleted_count = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        
        if file_size > size_threshold:
            os.remove(file_path)
            deleted_count += 1
            print(f"Deleted: {filename} ({file_size // 1024} kB)")

print(f"\nTotal files deleted: {deleted_count}")

