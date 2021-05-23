import pandas as pd


def to_data_frame(data_countries_list):
    """[summary]

    Args:
        data_countries_list ([list]): [lista con informacion para generar el DataFrame]

    Returns:
        [type]: [data frame con infomracion paises, data
        frame con promedio del tiempo de ejecucion]
    """

    # Generando DataFrame data paises
    df = pd.DataFrame(data_countries_list)

    # Calculando tiempos y guardando la informacion en un DataFrame
    df_times = pd.DataFrame()
    df_times['Tiempo total'] = df.sum(numeric_only=True)
    df_times['Tiempo promedio'] = df['Time'].mean()
    df_times['Tiempo minimo'] = df.min(numeric_only=True)
    df_times['Tiempo maximo'] = df.max(numeric_only=True)

    return df, df_times
