# Proyecto Final SW
Sistema de Gestión de Laboratorio – Proyecto Final SW

Este proyecto final implementa un sistema de gestión para un laboratorio, desarrollado en Python con un entorno virtual (venv) y una base de datos integrada. El sistema permite gestionar información crítica del laboratorio, incluyendo:

* Laboratoristas y clientes
* Equipos de laboratorio
* Instrumentos específicos: farinógrafo, alveógrafo
* Órdenes de laboratorio, lotes, inspecciones y certificados

El proyecto incluye la creación de la base de datos a través de Python, así como la instalación de dependencias mediante requirements.txt y la ejecución del sistema con run.py. Está pensado para facilitar la administración de datos, automatizar procesos internos del laboratorio y mantener un registro detallado de todas las operaciones.

Además, el repositorio incluye instrucciones para configurar el entorno virtual y la base de datos, así como capturas de pantalla que muestran la interfaz y funcionalidades del sistema.

## Instalación de Python VENV
Crea una carpeta vacía en donde estará en VENV que vamos a crear, junto a la carpeta del proyecto
```sh
mkdir ProyectoFinal_SW
cd ProyectoFinal_SW
python3 -m venv venv_proyecto
```

## Instalación de las dependencias

```sh
pip3 install -r requirements.txt
```

## Creación de la base de datos, en python
Comentar del archivo ___init___.py la linea 26: # from webapp import routes

Utilizando el env creado previamente, es necesario activarlo en terminal. Antes de realizar los siguientes pasos.
```sh
source venv_proyecto_sw/bin/activate
```

Con la terminal con en venv, en el directorio del proyecto, ingresar los siguientes comandos
```sh
python3
```
```sh
from webapp import db
```
```sh
from webapp.models import Laboratorista, EquipoLab, Farinografo, Alveografo, Cliente, Orden, Lote, Inspeccion, Certificado
```
```sh
db.create_all()
```


Si clonaste este repositorio, no es necesario crear la base de datos, a menos que hayas modificado alguna tabla de la dbs (class del documento models.py)

## Puedes correr el proyecto con el comando

```sh
python3 run.py
```

## Screenshots del Proyecto

![alt text](https://i.postimg.cc/YCvZPcn9/Screen-Shot-2021-11-30-at-3-17-56-p-m.png)
![alt text](https://i.postimg.cc/LsCTFhJF/Screen-Shot-2021-11-30-at-3-26-00-p-m.png)
