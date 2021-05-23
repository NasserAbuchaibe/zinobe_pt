import hashlib
import timeit

import requests

# endpoint informacion paises
url = "https://restcountries.eu/rest/v2/region/"


def data_countries(region):
    """[consulta el endpoint de la region recibida, obtiene
        de un pais de la region el nombre, lengua hablada (esta inforcion
        se encripta en SHA1) y calcula el tiempo de ejecucion de esta tarea]

    Args:
        region ([string]): [nombre region]

    Returns:
        [dict]: [diccionario con la informacion del pais de la region recibida]
    """

    start = timeit.timeit()

    data_dict = {}

    # forma url completa del endpoint a consultar
    url_region = url + region

    countrie_data = requests.request("GET", url_region)
    countrie_data_list = countrie_data.json()

    # filtra data recibida y almacena los datos solicitados en un diccionario
    data_dict['Region'] = countrie_data_list[0]['region']
    data_dict['Name'] = countrie_data_list[0]['name']

    # encriptacion con SHA1 de la lengua hablada en el pais
    encrip = hashlib.sha1(
        (countrie_data_list[0]['languages'][0]['name']).encode())
    data_dict['Languaje'] = encrip.hexdigest()

    # Calculando y almacenando el tiempo de ejecucion
    data_dict['Time'] = (timeit.timeit() - start)

    return data_dict
