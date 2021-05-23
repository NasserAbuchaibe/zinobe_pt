from aux_function.get_region import get_region
from aux_function.data_countries import data_countries
from aux_function.to_data_frame import to_data_frame
from aux_function.save_db import save_db

# Obteniendo lista con las regiones  existentes desde la APi:
# https://rapidapi.com/apilayernet/api/rest-countries-v1
region_list = get_region()

# Consulta https://restcountries.eu/  y obtiene
# la informacion de un pais por region
data_countries_list = [data_countries(region) for region in region_list]

# Genera 2 DataFrame df con la data de los paises y
# df_times con los calculos de los tiempos de ejecucion
df, df_times = to_data_frame(data_countries_list)

print(df)
print()
print(df_times)

# db
save_db(df, df_times)
