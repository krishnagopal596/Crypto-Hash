from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from time import sleep
from termcolor import cprint

def rsa_encryption(data):
    rsa = RSA.generate(2048)
    private_key = rsa.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = rsa.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()

    cprint("Executing step 2 RSA encryption......", "cyan")
    cprint(f"p :", "green" )
    print(rsa.p)
    cprint(f"q :", "green" )
    print(rsa.q)
    cprint(f"n :", "green" )
    print(rsa.n)
    cprint(f"e :", "green" )
    print(rsa.e)
    cprint(f"d :", "green" )
    print(rsa.d)
    sleep(1)

    cipher_rsa = PKCS1_OAEP.new(rsa)
    enc_data = cipher_rsa.encrypt(data)
    hex_enc_data = enc_data.hex()
    
    cprint("encrypted rsa data is:", "green")
    print(hex_enc_data)
    cprint(f"length of encrypted data is {len(hex_enc_data)*4} bits", "yellow")
    

    return enc_data






