import qrcode
from PIL import Image
# Generar codigo QR:
cadena = input("Introduzca el texto para el codigo QR: ")
imagen = qrcode.make(cadena)
# Generar imagen:
nombre_imagen = input("Introduzca el nombre de la imagen: ") + '.png'
archivo_imagen = open(nombre_imagen, 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()
# Abrir imagen
ruta_imagen = './' + nombre_imagen
Image.open(ruta_imagen).show()
