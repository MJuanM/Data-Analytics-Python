from Descarga_Transformaciones import *


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

