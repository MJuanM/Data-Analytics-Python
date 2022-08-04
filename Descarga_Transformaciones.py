from codecs import ignore_errors
import csv
from unittest import skip
import requests
import os
from datetime import date

url_teatros = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
url_cines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

urls = [url_teatros, url_cines, url_bibliotecas]
nombres = ['teatros', 'sala_de_cines', 'bibliotecas_publicas']
ruta = "C:\\Users\\mjuan\\Documents\\Proyectos\\ChallegeDataAnalytics"
today = date.today()
meses = ("enero", "febrero", "marzo", "abri", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
mes_actual = meses[today.month - 1]
anio_mes = format(today.year) + "-" + mes_actual
fecha = date.today()

# Descarga de informacion
for url, nombre in zip(urls, nombres): 
    response = requests.get(url) 
    if response.status_code == 200:
        print("Descarga con exito archivo: ", nombre)
        if os.path.exists(ruta + "\\" + nombre):
            os.path.exists(ruta + "\\" + nombre + "\\" + str(anio_mes))
        else:
            os.mkdir(nombre)
            os.mkdir(nombre + "\\" + str(anio_mes))
        with open(ruta + "\\" + nombre + "\\" + str(anio_mes) + "\\" + nombre + "-" + str(today) + '.csv', 'wb') as f:
            f.write(response.content)
            
    else:
        print(response.status_code, nombre)

# Leer archivo
import pandas as pd

col = ['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web']

df_bibliotecas_publicas = pd.read_csv(ruta + "\\" + "bibliotecas_publicas" + "\\" + str(anio_mes) + "\\" + "bibliotecas_publicas" + "-" + str(today) + '.csv', sep=',')
df_bibliotecas_publicas = df_bibliotecas_publicas.loc[ : , ['Cod_Loc', 'IdProvincia', 'IdDepartamento','Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio','CP','Teléfono','Mail','Web']]
df_bibliotecas_publicas = df_bibliotecas_publicas.set_axis(['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'], axis=1)


df_sala_de_cines = pd.read_csv(ruta + "\\" + "sala_de_cines" + "\\" + str(anio_mes) + "\\" + "sala_de_cines" + "-" + str(today) + '.csv', sep=',')
df_sala_de_cines = df_sala_de_cines.loc[ : , ['Cod_Loc', 'IdProvincia', 'IdDepartamento','Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección','CP','Teléfono','Mail','Web']]
df_sala_de_cines = df_sala_de_cines.set_axis(['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'], axis=1)

df_teatros = pd.read_csv(ruta + "\\" + "teatros" + "\\" + str(anio_mes) + "\\" + "teatros" + "-" + str(today) + '.csv', sep=',')
df_teatros = df_teatros.loc[ : , ['Cod_Loc', 'IdProvincia', 'IdDepartamento','categoria', 'provincia', 'localidad', 'nombre', 'direccion','CP','telefono','Mail','Web']]
df_teatros = df_teatros.set_axis(['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'], axis=1)


df_maestro = pd.concat([df_teatros,df_bibliotecas_publicas,df_sala_de_cines])
df_maestro = df_maestro.assign (Fecha_carga = (fecha))
df_maestro.to_csv(ruta + "\\" + "archivo_maestro.csv", index=None)