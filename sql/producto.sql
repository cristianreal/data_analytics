drop table if exists producto;

-- Crear la tabla producto
CREATE TABLE producto (
    id INTEGER PRIMARY KEY,
    categoria_id INTEGER NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    marca_id INTEGER NOT NULL,
    volumen INTEGER NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- Insertar los datos
INSERT INTO producto (id, categoria_id, nombre, marca_id, volumen, precio) VALUES
(356475, 9, 'Crown Royal Honey', 1, 750, 22.49),
(15335, 9, 'Crown Royal Regal Apple Mini', 1, 300, 11.03),
(81345, 9, 'Crown Royal Regal Apple', 1, 200, 7.08),
(150318, 9, 'Crown Royal Xr Canadian Whiskey', 1, 750, 98.99),
(310791, 9, 'Crown Royal Canadian Whisky Mini', 1, 300, 11.03),
(54058, 9, 'Crown Royal Canadian Whisky', 1, 200, 7.25),
(284871, 9, 'Crown Royal Canadian Whisky', 1, 375, 11.63),
(150100, 9, 'Crown Royal Canadian Whisky', 1, 1000, 28.13),
(243566, 9, 'Crown Royal Canadian Whisky', 1, 1750, 47.99),
(245400, 9, 'Crown Royal', 1, 200, 7.08),
(336832, 9, 'Seagrams V.o. Bl Canadian Whisky', 1, 750, 11.25),
(202052, 5, 'Captain Morgan Mango With Pitcher', 1, 750, 10.64),
(7943, 5, 'Captain Morgan Pineapple With Pitcher', 1, 750, 10.64),
(185598, 14, 'Club Cocktails Brass Monkey', 1, 750, 5.21),
(338308, 14, 'Club Cocktails Gin Martini', 1, 750, 5.19),
(318333, 14, 'Club Cocktails Manhattan', 1, 750, 5.19),
(68242, 14, 'Club Mudslide', 1, 1750, 9.6),
(185896, 14, 'Club Lime Margarita', 1, 1750, 12.75),
(277119, 14, 'Club Orange Craze', 1, 1750, 8.19),
(251130, 14, 'Club Peach Daiquiri Pouch', 1, 200, 1.5),
(63769, 14, 'Club Strawberry Margarita Pouch', 1, 200, 1.5);
