from enc.step1 import sha_hashing
from enc.step2 import rsa_encryption
from enc.step3 import aes_encryption


fn = input("enter image filename in images directory:")



hash = sha_hashing(fn)
rsa_enc_hash = rsa_encryption(hash)

aes_encryption(b'Very very secret', rsa_enc_hash)



