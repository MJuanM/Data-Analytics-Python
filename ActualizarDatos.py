import pandas as pd
from sqlalchemy import create_engine
from Descarga_Transformaciones import ruta

engine = create_engine("postgresql://postgres:123456@127.0.0.1:5432/challenge_data")

df_maestro = pd.read_csv(ruta + "\\" + "archivo_maestro.csv")
df_maestro.to_sql("archivo_maestro", con=engine, if_exists="replace")

df_cines = pd.read_csv(ruta + "\\" + "cines.csv")
df_cines.to_sql("cines", con=engine, if_exists="replace")

df_conteos = pd.read_csv(ruta + "\\" + "conteos.csv")
df_conteos.to_sql("conteos", con=engine, if_exists="replace")