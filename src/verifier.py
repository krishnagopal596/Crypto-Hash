from dec.shahash import sha_hashing
from dec.aesdec import aes_decryption
from dec.rsadec import rsa_decryption
from termcolor import cprint


encrypted_hash = aes_decryption()
hashsum_decrypted = rsa_decryption(encrypted_hash)
hashsum = sha_hashing()



print("-----------------------------------------------------------------------------------")
if hashsum_decrypted == hashsum:
    cprint("the image is safe 🆗", "green")
else:
    cprint("image has been corrupted!! ⚠️", "red")

print("-----------------------------------------------------------------------------------")