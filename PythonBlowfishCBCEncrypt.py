import blowfish
import webbrowser
import base64
import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
mensaje = input("Inserte mensaje a cifrar de largo del multiplo 8 caracteres\n")
mensaje = mensaje.encode()
llave = input("Inserte llave para cifrar el mensaje, entre 4 y 56 caracteres\n")
llave = llave.encode()
cipher = blowfish.Cipher(llave)
#cipher = blowfish.Cipher(b"Esta llave es mas larga que mi carrera")
#mensaje = b"HolaBroComoEstas"
#stringa = stringa.decode().encode("utf-8",errors="ignore")
data = mensaje # data to encrypt
vectorr = input ("Inserte un vector de largo 8 caracteres, numerico\n")
vectorr = vectorr.encode()
iv = vectorr # initialization vector
#iv = b"12345678" # initialization vector

data_encrypted = b"".join(cipher.encrypt_cbc(data, iv))
data_decrypted = b"".join(cipher.decrypt_cbc(data_encrypted, iv))

print (data == data_decrypted)
print (data_decrypted.decode("utf-8"))
b = base64.b64encode(data_encrypted)
print (b)

f = open('Mensaje.html', 'w')

mensaje = """<p> Este sitio contiene un mensaje secreto</p>
<div class ="algorithm" id="msg_cifrado">""" + str(b) + """</div>
"""

f.write(mensaje)
f.close()

webbrowser.open("http://localhost/Mensaje.html")

server_object.serve_forever()