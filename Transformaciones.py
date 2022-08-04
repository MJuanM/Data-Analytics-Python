import pandas as pd
from Descarga_archivos import *

#Creación de tabla principal

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

#Creación de tabla conteo
df_bibliotecas_pub = pd.read_csv(ruta + "\\" + "bibliotecas_publicas" + "\\" + str(anio_mes) + "\\" + "bibliotecas_publicas" + "-" + str(today) + '.csv', sep=',')
df_bibliotecas_pub = df_bibliotecas_pub.loc[ : , ['Categoría', 'Provincia', 'Fuente']]
df_bibliotecas_pub = df_bibliotecas_pub.set_axis(['categoría', 'provincia', 'fuente'], axis=1)


df_sala_de_cines = pd.read_csv(ruta + "\\" + "sala_de_cines" + "\\" + str(anio_mes) + "\\" + "sala_de_cines" + "-" + str(today) + '.csv', sep=',')
df_sala_de_cines = df_sala_de_cines.loc[ : , ['Categoría', 'Provincia', 'Fuente']]
df_sala_de_cines = df_sala_de_cines.set_axis(['categoría', 'provincia', 'fuente'], axis=1)

df_teatros = pd.read_csv(ruta + "\\" + "teatros" + "\\" + str(anio_mes) + "\\" + "teatros" + "-" + str(today) + '.csv', sep=',')
df_teatros = df_teatros.loc[ : , ['categoria', 'provincia', 'fuente']]
df_teatros = df_teatros.set_axis(['categoría', 'provincia', 'fuente'], axis=1)

df_conteo = pd.concat([df_teatros,df_bibliotecas_pub,df_sala_de_cines])

df_fuentes = df_conteo["fuente"].value_counts()
df_categoria = df_conteo["categoría"].value_counts()
df_provincia = df_conteo[["categoría", "provincia"]].value_counts()

df_conteo = pd.concat([df_fuentes, df_categoria, df_provincia]).reset_index()
df_conteo = df_conteo.assign (Fecha_carga = (fecha))
df_conteo = df_conteo.set_axis(['Nombre', 'Valor', 'Fecha de carga'], axis=1)
df_conteo.to_csv(ruta + '//' + 'conteos.csv', index = None)

#Creación tabla Cines
df_sala_de_cines = pd.read_csv(ruta + "\\" + "sala_de_cines" + "\\" + str(anio_mes) + "\\" + "sala_de_cines" + "-" + str(today) + '.csv', sep=',')
df_sala_de_cines = df_sala_de_cines.loc[ : , ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
df_sala_de_cines['espacio_INCAA'] = df_sala_de_cines ['espacio_INCAA'].str.lower()

pantallas = df_sala_de_cines.groupby(by=['Provincia']).sum()
espacios = df_sala_de_cines.loc[df_sala_de_cines ['espacio_INCAA'] == 'si']
espacios = espacios.groupby(by=['Provincia'])['espacio_INCAA'].count()

cines = pantallas.merge(espacios, on='Provincia')
cines = cines.assign (Fecha_carga = (fecha))
cines.to_csv(ruta + '//' +'cines.csv')