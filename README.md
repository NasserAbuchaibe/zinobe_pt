# zinobe

## En esta rama master se encuentra la primera version funcional sin manejo de errores
## En la rama zinobe_v1 esta la nueva version con manejo de errores.

## Este proyecto se desarrollo en un ambiente virtual utilizando virtualenv con python 3.8.5
### Para realizar pruebas sugiero utilizar virtualenv y realizar las instalaciones de las librerias necesarias utilizando el archivo requirements.txt  

### - Para probar app, ingresar al directorio zinobe_pt y ejeutar el comando:
```
python3 main.py
```

###  - Para ejecutar unittest, ingresar al directorio zinobe_pt y ejeutar el comando:
```
python -m unittest discover
```

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json  

### Autor: Nasser Abuchaibe
