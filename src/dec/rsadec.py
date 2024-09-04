from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
from time import sleep
from termcolor import cprint

def rsa_decryption(data:bytes):

    private_key = RSA.import_key(open("private.pem").read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    sha_hash = cipher_rsa.decrypt(data)

    cprint("decrypting using RSA.......", "cyan")
    cprint("reading 'receiver.pem'", "blue")
    sleep(1)
    hex_sha_hash = sha_hash.hex()
    cprint("decrypted message:", "green" )
    print(hex_sha_hash)
    cprint(f"length of decrypted message : {len(hex_sha_hash)*4} bits", "yellow")
    
    return sha_hash