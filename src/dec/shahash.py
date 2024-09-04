from Crypto.Hash import SHA256
from PIL import Image
from time import sleep
from termcolor import cprint
from pathlib import Path


def sha_hashing():
    
    file = input("Enter the name of the file you want to verify?:")

    sha_hash = SHA256.new()
    sha_hash_filename = SHA256.new()

    img_path = Path(f'images/{file}')
    byteRepOfImage = Image.open(img_path).tobytes()

    sha_hash.update(byteRepOfImage)
    sha_hash_filename.update(bytes(file, 'utf-8'))

    cprint(f"Hashing the image {file}...........", 'cyan')
    

    return sha_hash.digest() + sha_hash_filename.digest()
