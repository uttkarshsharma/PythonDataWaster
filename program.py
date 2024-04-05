import os
import random
import requests
from tqdm import tqdm

def generate_random_filename():
    return f"deleteme-{random.randint(1, 100000)}.zip"

def download_and_delete_file(url):
    filename = generate_random_filename()
    print(f"Downloading Large File to {filename}...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, ncols=80)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                progress_bar.update(len(chunk))
    progress_bar.close()
    print("File Downloaded. Deleting Large File...")
    os.remove(filename)
    print("File Deleted.")

if __name__ == "__main__":
    url = "https://dl.google.com/dl/android/aosp/husky-ud1a.230803.022.a3-factory-a95417f6.zip"
    while True:
        download_and_delete_file(url)
