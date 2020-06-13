from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def enc(dat):
    data = str(dat).encode()
    cipher_rsa = PKCS1_OAEP.new(key)
    enc_data = cipher_rsa.encrypt(data)
    arr1.append(enc_data)

def dec(dat):
    cipher_rsa = PKCS1_OAEP.new(key)
    data_dec = cipher_rsa.decrypt(dat)
    arr2.append(int(data_dec))

def main(arr):
    dict = {}

    key = RSA.generate(2048)
    
    
    dict['publickey'] = key.publickey().exportKey()
    dict['privatekey'] = key.exportKey()
    dict['data'] = arr
    print(dict,"\n\n")
    for i in arr:
        enc(i)
    print(arr1,"\n\n")
    for i in arr1:
        dec(i)
    print(arr2)

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    arr1 = []
    arr2 = []

    main(arr)