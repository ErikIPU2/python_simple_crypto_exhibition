from flask import Flask, render_template, jsonify
import Crypto
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import hashlib
import ast
import base64

app = Flask(__name__)

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

public_key = key.publickey()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/cifre/<message>/<key>')
def cifre(message, key):
    key = int(key)
    if message and key:
        cifred_message = ""
        for letter in message:
            l_num = ord(letter)
            l_num += key
            l_num = chr(l_num)
            cifred_message += l_num
    else:
        cifred_message = "Parametros invalidos"

    return jsonify(cifred_message)


@app.route('/descifre/<message>/<key>')
def descifre(message, key):
    key = int(key)
    if message and key:
        cifred_message = ""
        for letter in message:
            l_num = ord(letter)
            l_num -= key
            l_num = chr(l_num)
            cifred_message += l_num
    else:
        cifred_message = "Parametros invalidos"

    return jsonify(cifred_message)


@app.route('/hash/<message>')
def hash_c(message):
    if message:
        sha_signature = hashlib.sha256(message.encode()).hexdigest()
    else:
        sha_signature = "Parametros invalidos"

    return jsonify(sha_signature)


@app.route('/simetric_encrypt/<message>/<key>')
def simetric_encrypt(message, key):
    if len(message) == 16 and len(key) == 16:
        encryption_suit = AES.new(key, AES.MODE_CBC, "This is an IV456")
        cipher_text = encryption_suit.encrypt(message)
    else:
        cipher_text = "Parametros invalidos"

    return cipher_text


@app.route('/simetric_decrypt/<message>/<key>')
def simetric_decrypt(message, key):
    if len(message) == 16 and len(key) == 16:
        encryption_suit = AES.new(key, AES.MODE_CBC, "This is an IV456")
        cipher_text = encryption_suit.decrypt(message)
    else:
        cipher_text = "Parametros invalidos"

    return cipher_text


@app.route('/get_public_key')
def get_public_key():
    return jsonify(str(key.publickey().exportKey()))


@app.route('/get_private_key')
def get_private_key():
    return jsonify(str(key.exportKey()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
