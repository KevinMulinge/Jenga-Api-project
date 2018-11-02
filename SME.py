import requests
import random
import datetime
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--destination_name","-dn",type=str)
parser.add_argument("--destination_account_number","-dan",type=str)
parser.add_argument("--transfer_amount","-ta",type=str)
parser.add_argument("--Country","-c",type=str)
args = parser.parse_args()
#Generating tokens
now = datetime.datetime.now()
url = "https://uat.jengahq.io/identity/v2/token"
source_account_number= " "
transfer_amount= args.transfer_amount
transfer_currency_code= "KES"
transfer_reference=str(random.randint(100000000000,999999999999))
sig=source_account_number+transfer_amount+transfer_currency_code+transfer_reference
#print(now.strftime("%Y-%m-%d"))
#print(sig) print input of signature
headers = {
    'Authorization': "Basic c0xEVnBxSE1ndFVHcXZjVUZXTEZFUUE5UjlNeExuYkQ6N1JQTXlMYjJTS2pZcGVKcA==",
    'content-type': "application/x-www-form-urlencoded"
    }
payload = {'username':' ','password':' '}

#session = requests.Session()
#session.post('https://admin.example.com/login.php',headers=headers,data=payload)
response = requests.request("POST", url, headers=headers,data=payload)

#print(response.text)  Print the token
text=response.text
ext = "access_token"
end = " }"
TokName= "Bearer "+text[text.find(ext)+16:text.find(end)-13]
#print(TokName) print the bearer token
#Generating Signature
message = sig.encode('utf-8') # See separate instruction on how to create this concatenation
digest = SHA256.new()
digest.update(message)

private_key = False
with open("privatekey.pem", "r") as myfile:
    private_key = RSA.importKey(myfile.read())

signer = PKCS1_v1_5.new(private_key)
sigBytes = signer.sign(digest)
signBase64 = b64encode(sigBytes)
#print(signBase64) Print the signature

#Sending money
url = "https://uat.jengahq.io/transaction/v2/remittance"

headers = {
    'Authorization': TokName,
    'content-type': "application/json",
    'signature': signBase64
    }

payload ={
   "source": {
      "countryCode": "KE",
      "name": "John Doe",
      "accountNumber": " "
   },
   "destination": {
      "type": "bank",
      "countryCode": "KE",
      "name": args.destination_name,
      "accountNumber": args.destination_account_number
   },
   "transfer": {
      "type": "InternalFundsTransfer",
      "amount": args.transfer_amount,
      "currencyCode": "KES",
      "reference": transfer_reference,
      "date": now.strftime("%Y-%m-%d"),
      "description": "Some remarks here"
   }
}

response = requests.post(url, headers=headers,json=payload)

print(response.text)
