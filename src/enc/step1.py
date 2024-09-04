from Crypto.Hash import SHA256
from PIL import Image
from time import sleep
from termcolor import cprint
from pathlib import Path


def sha_hashing(file: str):

    sha_hash = SHA256.new()
    sha_hash_filename = SHA256.new()

    img_path = Path(f'images/{file}')
    byteRepOfImage = Image.open(img_path).tobytes()

    sha_hash.update(byteRepOfImage)
    sha_hash_filename.update(bytes(file, 'utf-8'))

    cprint("Executing STEP 1...........", 'cyan')
    print(f"Given file is {file}")
    sleep(1)
    cprint("The SHA hash of image is:", "green")
    print(sha_hash.hexdigest())
    cprint(f"length:{len(sha_hash.hexdigest())*4} bits", "yellow")
    cprint("The SHA hash of filename is:", "green")
    print(sha_hash_filename.hexdigest())
    cprint(f"length:{len(sha_hash_filename.hexdigest())*4} bits", "yellow")

    return sha_hash.digest() + sha_hash_filename.digest()
