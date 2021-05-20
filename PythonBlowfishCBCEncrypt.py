import blowfish #se importa la librería de Blowfish para python
import webbrowser 
import base64 #se importa base 64
import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler) #Se inicia un servidor local
mensaje = input("Inserte mensaje a cifrar de largo del multiplo 8 caracteres\n")
mensaje = mensaje.encode() #encode al mensaje
llave = input("Inserte llave para cifrar el mensaje, entre 4 y 56 caracteres\n")
llave = llave.encode() #encode a la llave
cipher = blowfish.Cipher(llave)
#cipher = blowfish.Cipher(b"llave secreta")
#mensaje = b"HolaComoEstas"
#stringa = stringa.decode().encode("utf-8",errors="ignore")
data = mensaje # data a encriptar
vectorr = input ("Inserte un vector de largo 8 caracteres, numerico\n")
vectorr = vectorr.encode() #encode al vector
iv = vectorr # vector de inicialización, necesario para usar CBC en Blowfish
#iv = b"12345678" # initialization vector

data_encrypted = b"".join(cipher.encrypt_cbc(data, iv)) #con la librería Blowfish, se crea la función para encriptar
data_decrypted = b"".join(cipher.decrypt_cbc(data_encrypted, iv)) #al igual que arriba, pero para descencriptar

print (data == data_decrypted) #imprime si la data es igual a la data decrypted, en consola
print (data_decrypted.decode("utf-8")) #imprime la data decrypted usando decodificación utf8, en consola
b = base64.b64encode(data_encrypted) #se le asgina una variable la tarea de hacer encode a la información encriptada, esto para que luego en JS se
# reciba con base 64, para luego desencriptar con blowfish js
print (b) #imprime esta variable b, en conso,a

f = open('Mensaje.html', 'w') #se abre una página web con nombre mensaje

mensaje = """<p> Este sitio contiene un mensaje secreto</p>
<div class ="algorithm" id="msg_cifrado">""" + str(b) + """</div>
"""
#se imprime el mensaje en la página, encriptado en base64

f.write(mensaje) #escribe el mensaje
f.close() #termina el proceso de escribir

webbrowser.open("http://localhost/Mensaje.html") #el server corre la página en el link localhost/mensaje.html

server_object.serve_forever() #el server queda siempre corriendo, sin cerrarse a excepción de que uno lo cierre de forma manual
