# curso-python-PIP
Proyecto de curso  Curso de Python: PIP y Entornos Virtualesde Python: PIP y Entornos Virtuales

Lista de miniproyectos

## Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 main.py
```

## App Project

Para este proyecto, use un entorno virtual para instalar matplotlib.

1. Crear entono virtual:

```sh
python3 -m venv ~/py_envs

```
2. Activar entorno virtual:

```sh
source ~/py_envs/bin/activate

```

3. Instalar la libreria:

```sh
pip install <package_name>

```
Despues para correr el codigo use:

```sh
source ~/py_envs/bin/activate #Si es que no esta activo el entorno virtual.
python3 app/main.py
```


## Webserver Project

Para este proyecto se crear nuevamente un entorno virtual.

1. Crear entono virtual:

```sh
python3 -m venv ~/py_envs

```
2. Activar entorno virtual:

```sh
source ~/py_envs/bin/activate

```

3. Instalar la libreria:

```sh
pip install pip install -r webserver/requirements.txt

```
4. Despues para correr el codigo use:

```sh
source ~/py_envs/bin/activate #Si es que no esta activo el entorno virtual.
uvicorn main:app --reload
```


## App Project (Docker)

Para ejecutar el proyecto app con docker se usan los sigueintes comandos:

1. Contruimos el contenedor:

```sh
cd app
sudo docker-compose build

```

2. Activamos el servicio:

```sh
sudo docker-compose up -d 
```

3. Corremos el bash:
```sh
sudo docker-compose exec app-csv bash
```
4. Despues para correr el codigo use:

```sh
python app/main.py
```

## webserver Project (Docker)

Para ejecutar el proyecto app con docker se usan los sigueintes comandos:

1. Contruimos el contenedor:

```sh
cd webserver
sudo docker-compose build

```
2. Validamos la creacion del contenedor:

```sh
sudo docker-compose ps

```

3. Activamos el servicio:

```sh
sudo docker-compose up -d 
```
4. ir a http://127.0.0.1/contacto

