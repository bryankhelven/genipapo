import os
import requests
import hashlib
import sys

def download_genipapo_model():
    # Direct download URL from GitHub Releases
    model_url = 'https://github.com/bryankhelven/genipapo/releases/download/Publishing/genipapo.pt'
    model_dir = os.path.join('models')
    model_path = os.path.join(model_dir, 'genipapo.pt')

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    if os.path.exists(model_path):
        print("Genipapo model already exists. Verifying checksum...")
        with open(model_path, 'rb') as f:
            data = f.read()
            checksum = hashlib.md5(data).hexdigest()
        if checksum == model_checksum:
            print("Checksum verified. Model is ready to use.")
            return
        else:
            print("Checksum mismatch. Redownloading the model...")
            os.remove(model_path)

    print("Downloading Genipapo model...")
    response = requests.get(model_url, stream=True)
    if response.status_code != 200:
        print("Failed to download the model. Please check the URL.")
        sys.exit(1)
    with open(model_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Download completed. Model is ready to use.")


if __name__ == '__main__':
    download_genipapo_model()

