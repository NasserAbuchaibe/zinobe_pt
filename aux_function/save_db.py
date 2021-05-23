import sqlite3
import pandas as pd


def save_db(df, df_times):
    """[Almacena los DataFrames en la Base de datos]
    Args:
        df ([DataFrame]): [data paises]
        df_times ([[DataFrame]): [tiempos de ejecucion]
    """
    # conexion a la base de datos zinobe.db
    con = sqlite3.connect('zinobe.db')

    # almacena DataFrame en la tabla df de la DB zinobe.db
    df.to_sql('df', con, if_exists='replace')

    # almacena DataFrame en la tabla df_times de la DB zinobe.db
    df_times.to_sql('df_times', con, if_exists='replace')
