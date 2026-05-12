# matrices-tarea-11-de-mayo
1-como usar este codigo:
2-copie el repositorio
3-abra la carpeta "matrices"
4a-descargue los archivos en su computador e importelos en colab con el siguiente codigo:

from google.colab import files

print("Selecciona los archivos .py desde tu ordenador local:")
uploaded = files.upload()

for fn in uploaded.keys():
  print('Archivo subido: "{name}" con tamaño {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

4b-copie desde github el codigo y peguelo en colab para despues ejecutarlos

5-use la linea de codigo: !python main.py

6-siga las instrucciones del codigo
