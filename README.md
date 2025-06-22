# Construcciones_1711_ca_ft

## En windows

### Para iniciar el proyecto primero debemos tener instalado Python y Pip

En un terminal/consola (en la raiz del proyecto) que tenga disponible python, actualizamos pip y demás dependencias de instalación lo haremos con el siguiente comando en windows

        python -m pip install --upgrade pip setuptools virtualenv

### Generamos el entorno virtual

        python -m virtualenv kivy_venv

### Iniciamos el entorno virtual

Para hacerlo es necesario ejecutar el siguiente comando

        kivy_venv\Scripts\activate

### Instalamos kivy en su ultima version (Master)

Usando el siguiente comando

        python -m pip install "kivy[base]" kivy_examples

### Finalmente debemos instalar KivyMD

Usaremos el siguiente comando

        pip install kivymd

### Por último para ejecutar la app en tu escritorio escribiremos en la terminal

        py main.py

#### ó

        python main.py
