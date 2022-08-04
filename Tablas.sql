CREATE DATABASE IF NOT EXISTS challenge_data;

CREATE TABLE IF NOT EXISTS archivo_maestro (
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
    fecha_carga DATE
);

CREATE TABLE IF NOT EXISTS cines (
    id_cines INT NOT NULL PRIMARY KEY,
    provinvia VARCHAR,
    pantallas INT,
    butacas INT,
    espacios_incca INT,
    fecha_carga DATE
);

CREATE TABLE IF NOT EXISTS conteo (
    id_conteo INT NOT NULL PRIMARY KEY,
    categoria VARCHAR,
    cantidad INT,
    fecha_carga DATE
);

