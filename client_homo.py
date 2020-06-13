import sys
import json
import time

import requests

from phe import paillier
from phe.paillier import PaillierPublicKey, EncryptedNumber

import matplotlib.pyplot as plt 


no_of_elements=[]
time = [] 

plt.plot(x, y) 
  
plt.xlabel('x - axis') 

plt.ylabel('y - axis') 
  
plt.title('My first graph!') 
  
plt.show() 


with open("data1","r") as file1:
    value1 = file1.read().split("\n")
    value1 = [int(x) for x in (value1)]
# print(value1)

with open("data2","r") as file1:
    value2 = file1.read().split("\n")
    value2 = [int(x) for x in (value1)]
# print(value1)

# value1 = [1,2,3,4,5]
# value2 = [1,2,3,4,5]
for i in range(len(value1),10):
	start = time.process_time()

	public_key ,private_key = paillier.generate_paillier_keypair()

	encrp_data1 = [public_key.encrypt(x).ciphertext() for x in value1]
	encrp_data2 = [public_key.encrypt(x).ciphertext() for x in value2]

	data = {
		'n': public_key.n,
		'cipher_texts': [
							encrp_data1,
							encrp_data2
						]}

	jsonData = json.dumps(data)
	# sending request
	res = requests.post("http://127.0.0.1:8000/getdata/", json=jsonData).json()

	ret_value=[]
	# evaluating response
	for i in res['sum_cipher_text']:
		sum_cipher_text = EncryptedNumber(public_key, i)
		ret_value.append(private_key.decrypt(sum_cipher_text))

	time_taken = time.process_time() - start


	print(
		"Sum of "
		+ str(value1)
		+ " and "
		+ str(value2)
		+ " is "
		+ str(ret_value)
	)

print(time_taken)