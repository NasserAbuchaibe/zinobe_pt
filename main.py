from aux_function.get_region import get_region
from aux_function.data_countries import data_countries
from aux_function.to_data_frame import to_data_frame

# Obteniendo lista con las regiones  existentes desde la APi:
# https://rapidapi.com/apilayernet/api/rest-countries-v1
region_list = get_region()

# Consulta https://restcountries.eu/  y obtiene
# la informacion de un pais por region
data_countries_list = [data_countries(region) for region in region_list]

df, df_times = to_data_frame(data_countries_list)

print(df)
print()
print(df_times)