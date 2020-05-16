from flask import Flask,request
import json

from phe.paillier import PaillierPublicKey, EncryptedNumber

app = Flask(__name__)

@app.route('/getdata/',methods=['POST'])
def getdata():
    
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
    print("Request recieved and started evaluating")

    # Use the data here
    public_key = PaillierPublicKey(data['n'])

    encrp_numb1 = EncryptedNumber(public_key, data['cipher_texts'][0])
    encrp_numb2 = EncryptedNumber(public_key, data['cipher_texts'][1])

    sum_cipher_text = encrp_numb1 + encrp_numb2
    
    results = { 'sum_cipher_text': sum_cipher_text.ciphertext() }
    return json.dumps(results)
    

if __name__ == "__main__":
    app.run(debug = True ,port=8000)