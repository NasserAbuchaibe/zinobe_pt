""" main """
import json
import sys

from requests import HTTPError

from aux_function.data_countries import data_countries
from aux_function.get_region import get_region
from aux_function.save_db import save_db
from aux_function.to_data_frame import to_data_frame

# Obteniendo lista con las regiones  existentes desde la APi:
# https://rapidapi.com/apilayernet/api/rest-countries-v1
region_list = get_region()

if isinstance(region_list, HTTPError):
    print(region_list)
    sys.exit()

# Consulta https://restcountries.eu/  y obtiene
# la informacion de un pais por region
data_countries_list = []

if region_list == []:
    sys.exit("No se encontraron las regiones requeridas")

data_countries_list = [data_countries(region) for region in region_list]

# Filtra None que se hallan podido generar en el momento de consultar un pais
data_countries_list = list(filter(None, data_countries_list))

# Genera 2 DataFrame df con la data de los paises y
# df_times con los calculos de los tiempos de ejecucion
if data_countries_list != []:
    df, df_times = to_data_frame(data_countries_list)

    print(df)
    print()
    print(df_times)

    # Almacena los DataFrames en sqlite
    save_db(df, df_times)

    # Generando un json con las tablas creadas
    json_list = []
    json_list.append(df.to_json())
    json_list.append(df_times.to_json())

    # guardando el json en archivo data.json
    with open('data.json', 'w') as file:
        json.dump(json_list, file)
