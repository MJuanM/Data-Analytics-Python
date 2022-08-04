from Descarga_Transformaciones import *

df_sala_de_cines = pd.read_csv(ruta + "\\" + "sala_de_cines" + "\\" + str(anio_mes) + "\\" + "sala_de_cines" + "-" + str(today) + '.csv', sep=',')
df_sala_de_cines = df_sala_de_cines.loc[ : , ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
df_sala_de_cines['espacio_INCAA'] = df_sala_de_cines ['espacio_INCAA'].str.lower()

pantallas = df_sala_de_cines.groupby(by=['Provincia']).sum()
espacios = df_sala_de_cines.loc[df_sala_de_cines ['espacio_INCAA'] == 'si']
espacios = espacios.groupby(by=['Provincia'])['espacio_INCAA'].count()

cines = pantallas.merge(espacios, on='Provincia')
cines = cines.assign (Fecha_carga = (fecha))
cines.to_csv(ruta + '//' +'cines.csv')