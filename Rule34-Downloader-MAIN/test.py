import os
import requests  # We'll use requests to download the image manually
from rule34 import Sync

# --- CONFIG ---
API_KEY = "your_key"
USER_ID = "your_id"
TEST_TAG = "foxgirl"
DOWNLOAD_DIR = r"your_output_folder_here"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_image(url, post_id, folder):
    ext = os.path.splitext(url)[1]  # Get extension from URL
    filename = f"{post_id}{ext}"
    path = os.path.join(folder, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        return path
    else:
        raise Exception(f"Failed to download image: {response.status_code}")

def main():
    sync = Sync(api_key=API_KEY, user_id=USER_ID)

    total = sync.totalImages(TEST_TAG)
    print(f"Total images for tag '{TEST_TAG}': {total}")

    images = sync.getImages(TEST_TAG, singlePage=True)
    if not images:
        print("No images found.")
        return

    print(f"Fetched {len(images)} images")
    for i, img in enumerate(images[:5]):
        print(f"{i+1}: {img.file_url}")

    post_id = images[0].id
    post_data = sync.getPostData(post_id)
    print(f"\nPost data for ID {post_id}:")
    for k, v in post_data.items():
        print(f"{k}: {v}")

    print("\nDownloading first image...")
    filepath = download_image(images[0].file_url, post_id, DOWNLOAD_DIR)
    print(f"Downloaded to {filepath}")

    sync.sessionClose()
    print("\nTest completed.")

if __name__ == "__main__":
    main()