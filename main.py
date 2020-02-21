import logging
from api import PixabayAPI
import threading


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
#query = input('Que imagenes desea buscar??\n')
query = 'auto'
cant = 3
#cant = int(input(f'Cuantas imagenes de {query} quiere descargar??\n'))
api = PixabayAPI('15310524-79ecdd78fa84e569387772c5e', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cant)

#for u in urls:
  #t = threading.Thread(target = api.descargar_imagen, args=[u])
  #logging.info(f'Descargando {u}')
  #t.start()

for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)
print(api.imagenes)

