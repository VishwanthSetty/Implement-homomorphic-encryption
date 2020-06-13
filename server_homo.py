from flask import Flask,request
import json


from phe.paillier import PaillierPublicKey, EncryptedNumber

app = Flask(__name__)

@app.route('/getdata/',methods=['POST'])
def getdata():
    
    jsondata = request.get_json()
    data = json.loads(jsondata)
    m = 10                                               # m is constant 
    print("Request recieved and started evaluating")

    # Use the data here
    public_key = PaillierPublicKey(data['n'])

    sum_cipher_text =[]
    for i in range(0,len(data['cipher_texts'][0])):

        # operation : a+mb 
        # a is EncryptedNumber1
        # b is EncryptedNumber2
        # and m is constant
        encrp_numb1 = EncryptedNumber(public_key, data['cipher_texts'][0][i])
        encrp_numb2 = EncryptedNumber(public_key, data['cipher_texts'][1][i])
        sum_cipher_text.append((encrp_numb1 + m*encrp_numb2).ciphertext())
    
    results = { 'sum_cipher_text': sum_cipher_text }
    return json.dumps(results)
    

if __name__ == "__main__":
    app.run(debug = True ,port=8000)