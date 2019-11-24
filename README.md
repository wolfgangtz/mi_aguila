# Prueba backend Mi Aguila

Este proyecto es la solución de la prueba tecnica de Mi Aguila. Para levantar los servicios porfavor siga los siguientes pasos:

1. Crear un entorno virtual, para eso puede correr esta linea:
```
	virtualenv -p python3 venv
```
2. Activar el entorno virtual, para ello puede correr esta linea:
```
	source venv/bin/activate 
```
3. instalar los requerimientos, para eso, corra esta linea:
```
	pip install -r requeriments.txt 
```
4. levante el servidor, para ello corra esta linea:
```
	python manage.py runserver
```

## Swagger

Una vez levantado el servidor, puede consultar la documentación de los servicios en la siguiente url:
```
	http://127.0.0.1:8000/swagger/
```


## Script para guardar los viajes

Con el objetivo de tomar el archivo JSON y cargar la información a la base de datos, se genero el script upload_trips_script.py, para ejecutarlo active el shell de python utilizando la siguiente linea:
```
	python manage.py shell
```

copie y pegue el contenido del archivo y presione enter para ejecutar el script, este generara apartir del archivo JSON las ciudades, paises y viajes que esten en el archivo.


## Pendientes

como pendientes, quedo por agregar a este proyecto:

1. test unitarios.
2. docker file.
3. jenkinsfile o archivos de circle CI para el despliegue continuo o algun script de despliegue directo a servidor.
4. configuración del administrador.
5. organizar modelos, serializadores y vistas en carpetas internas en las aplicaciones con el objetivo de manter mas ordenado el proyecto.
6. implementar GitFlow para el manejo del repositorio.
7. para agilizar las consultas se podria implementar una herramienta como elasticsearch para crear una copia de la base de datos con mucha información (como la tabla de viajes) y que los endpoints de consulta (GET) se hagan contra elasticsearch y no directamente a postgres.
8. implementar el changelog
9. implementar logs


como en la prueba no estaba escritos estos requerimientos, no se llevarón a cabo, cabe destacar que tengo los conocimientos para implementarlo y que no el tiempo estimado para la prueba no me permitia hacer todo lo antes mencionado.
