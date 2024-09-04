from Crypto.Cipher import AES
from time import sleep
from termcolor import cprint

def aes_encryption(key:bytes, data:bytes):

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    

    

    cprint("Executing STEP 3...........", "cyan")
    cprint(f"the 16 byte key is: {key}","green")
    sleep(1)
    
    cprint("The AES cipher of data given is:", "green")
    print(ciphertext.hex())
    cprint(f"length: {len(ciphertext.hex())*4} bits", "yellow")

    cprint(f"saving the data into 'encrypted.bin'", "green")

    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
