import os

'''
1.- Obtener la ruta del directorio para ordenar los archivos
2.- Crear los directorios de las diferentes categorias de archivos
3.- Obtener los nombre de los archivos para poder filtrar los mismos
4.- Mover cada archivo en su carpeta designada

'''

def obtener_tipo(file_name):
    pos = len(file_name) - 1
    while pos >= 0:
        if(file_name[pos] != '.'):
            pos -= 1
        else:
            return file_name[pos:]
# 1
path = input("Insert the absolute directory path that you want to :\n")

# 2
try:
    os.mkdir(path + '/Imagenes')
except FileExistsError:
    pass
try:
    os.mkdir(path + '/Videos')
except FileExistsError:
    pass
try:
    os.mkdir(path + '/Audios')
except FileExistsError:
    pass
try:
    os.mkdir(path + '/Otros')
except FileExistsError:
    pass


# 3
files = os.scandir(path)

# 4
for file in files:
    if(not os.path.isfile(path + f'/{file.name}')):
        continue
    tipo = obtener_tipo(file.name)
    if(tipo == '.jpg' or tipo == '.png' or tipo == '.jpeg'):
        ruta_nueva = path + '/Imagenes/' + file.name
        ruta_origen = path + f'/{file.name}'
        os.rename(ruta_origen, ruta_nueva)
    elif(tipo == '.mp3' or tipo == '.m4a' or tipo == '.aac' or tipo == '.wav'):
        ruta_nueva = path + '/Audios/' + file.name
        ruta_origen = path + f'/{file.name}'
        os.rename(ruta_origen, ruta_nueva)
    elif(tipo == '.mp4' or tipo == '.mov' or tipo == '.mkv'):
        ruta_nueva = path + '/Videos/' + file.name
        ruta_origen = path + f'/{file.name}'
        os.rename(ruta_origen, ruta_nueva)
    else:
        ruta_nueva = path + '/Otros/' + file.name
        ruta_origen = path + f'/{file.name}'
        os.rename(ruta_origen, ruta_nueva)

print('--- Tus archivos ya estan ordenados. ---')