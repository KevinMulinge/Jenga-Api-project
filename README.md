I developed this web application to be able to Send money within
Equity accounts and to mobile wallets.
It would be used by vendors and sale's people in easily transacting
with their suppliers.
How to run : 
For linux :
pip install requests,
pip install pycrypto,
Host it on an apache server

For windows :
First install python,
pip install requests,
pip install pycryptodome,
Then run by : 
Host it in a webserver like xampp and run

Generate the public and private key as below:
openssl genrsa -out privatekey.pem 2048 -nodes,
openssl rsa -in privatekey.pem -outform PEM -pubout -out publickey.pem

Copy the public key to your jenga api account .

Fill in the entries of :username,Password,Api key,Account Number on SME.py and TMW.py
