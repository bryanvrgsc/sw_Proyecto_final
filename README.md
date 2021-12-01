# Proyecto Final SW

## Instalación de Python VENV
Crea una carpeta vacía en donde estará en VENV que vamos a crear, junto a la carpeta del proyecto
```sh
mkdir ProyectoFinal_SW
cd ProyectoFinal_SW
pyton3 -m venv venv
```

## Instalación de las dependencias

```sh
pip3 -r install requirements.txt
```

## Creación de la base de datos, en python
Comentar del archivo ___init___.py la linea 26: # from webapp import routes
```sh
python3
>>> from webapp import db
>>> from webapp.models import Laboratorista, EquipoLab, Farinografo, Alveografo, Cliente, Orden, Lote, Inspeccion, Certificado
>>> db.create_all()
```
Si clonaste este repositorio, no es necesario crear la base de datos, a menos que hayas modificado alguna tabla de la dbs (class del documento models.py)

## Puedes correr el proyecto con el comando

```sh
python3 run.py
```

## Screens del Proyecto

![alt text](https://i.postimg.cc/YCvZPcn9/Screen-Shot-2021-11-30-at-3-17-56-p-m.png)
![alt text](https://i.postimg.cc/LsCTFhJF/Screen-Shot-2021-11-30-at-3-26-00-p-m.png)
