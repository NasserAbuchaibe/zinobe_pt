""" get_region """
import requests

# endpoint informacion paises
URL = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-key': "1667516e6amshc4aaf5a5a03bdb8p1fd923jsn482cb39515e0",
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
}


def get_region():
    """[Consulta endpoint y obtiene data de donde filtra las regiones
        existentes]

        Returns:
        [list]: [lista con las regiones existentes]
    """
    response = requests.request("GET", URL, headers=headers)

    try:
        response.raise_for_status()

        countries = response.json()
        return list(set([country['region'].lower()
                        for country in countries if country['region'] != ""]))

    except requests.exceptions.HTTPError as error_messages:
        return(error_messages)
