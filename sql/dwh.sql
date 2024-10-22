-- Crear la tabla Producto (Dimensiones)
CREATE TABLE Producto (
    productoid INT PRIMARY KEY,
    categoria VARCHAR(255),
    nombre VARCHAR(255),
    marca VARCHAR(255)
);

-- Crear la tabla Cliente (Dimensiones)
CREATE TABLE Cliente (
    clientid INT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    nacimiento DATE,
    genero VARCHAR(50),
    empresa VARCHAR(255),
    idioma VARCHAR(50),
    Nit VARCHAR(100),
    Puesto VARCHAR(255),
    Ciudad VARCHAR(255),
    Correo VARCHAR(255)
);

-- Crear la tabla Evento (Hechos)
CREATE TABLE Evento (
    transactionid INT PRIMARY KEY,
    visitorid INT,
    itemid INT,
    timestamp TIMESTAMP,
    event VARCHAR(255),
    volumen INT,
    precio DOUBLE PRECISION,
    FOREIGN KEY (itemid) REFERENCES Producto(productoid),
    FOREIGN KEY (visitorid) REFERENCES Cliente(clientid)
);

-- Agregar algunos índices útiles para mejorar el rendimiento de las consultas
CREATE INDEX idx_evento_timestamp ON Evento(timestamp);
CREATE INDEX idx_evento_event ON Evento(event);
CREATE INDEX idx_producto_categoria ON Producto(categoria);
CREATE INDEX idx_cliente_ciudad ON Cliente(Ciudad);

-- Agregar un comentario para explicar el propósito de este esquema
COMMENT ON SCHEMA public IS 'Esquema de almacén de datos para analizar eventos de clientes e interacciones con productos';