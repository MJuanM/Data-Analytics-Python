import psycopg2

con = psycopg2.connect(database="challenge_data", user="postgres", password="123456", host="127.0.0.1", port="5432")
print("Conectado a base de dato 'challenge_data'")

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS archivo_maestro (
    id_maestro INT NOT NULL PRIMARY KEY,
    cod_localidad INT NOT NULL,
    id_provincia INT NOT NULL,
    id_departamento INT NOT NULL,
    categoría VARCHAR,
    provinvia VARCHAR,
    localidad VARCHAR,
    nombre  VARCHAR,
    domicilio VARCHAR,
    código_postal VARCHAR,
    número_de_teléfono VARCHAR,
    mail VARCHAR,
    web VARCHAR,
    fecha_carga DATE);""")

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS cines (
    id_cines INT NOT NULL PRIMARY KEY,
    provinvia VARCHAR,
    pantallas INT,
    butacas INT,
    espacios_incca INT,
    fecha_carga DATE);""")

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS conteo (
    id_conteo INT NOT NULL PRIMARY KEY,
    categoria VARCHAR,
    cantidad INT,
    fecha_carga DATE);""")

print("Table created successfully")

con.commit()
con.close()