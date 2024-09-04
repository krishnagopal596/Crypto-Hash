from Crypto.Cipher import AES
from termcolor import cprint

def aes_decryption():

    cprint("decrypting using AES....", "cyan")
    cprint("key given is 'Very very secret'", "green")

    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    cipher = AES.new(b"Very very secret", AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    cprint("decrypted data is:", "green")
    print(data.hex())

    return data

