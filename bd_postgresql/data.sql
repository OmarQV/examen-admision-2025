-- POSTGRESQL

-- Crear la base de datos
CREATE DATABASE gestion_biblioteca;

-- Tabla usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    rol VARCHAR(50) DEFAULT 'usuario'
);

INSERT INTO usuarios (nombre, correo, telefono, rol) VALUES
('Juan Pérez', 'juan.perez@example.com', '1234567890', 'usuario'),
('María García', 'maria.garcia@example.com', '0987654321', 'usuario'),
('Carlos López', 'carlos.lopez@example.com', '1122334455', 'admin'),
('Ana Martínez', 'ana.martinez@example.com', '5566778899', 'usuario'),
('Luis Rodríguez', 'luis.rodriguez@example.com', '6677889900', 'usuario'),
('Sofía Fernández', 'sofia.fernandez@example.com', '7788990011', 'usuario'),
('Pedro Gómez', 'pedro.gomez@example.com', '8899001122', 'usuario'),
('Laura Sánchez', 'laura.sanchez@example.com', '9900112233', 'admin'),
('Marta Díaz', 'marta.diaz@example.com', '0011223344', 'usuario'),
('Jorge Ruiz', 'jorge.ruiz@example.com', '2233445566', 'usuario');



-- Tabla libros
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    categoria VARCHAR(100),
    stock INT CHECK (stock >= 0)
);

INSERT INTO libros (titulo, autor, categoria, stock) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 'Ficción', 5),
('1984', 'George Orwell', 'Ciencia Ficción', 3),
('El principito', 'Antoine de Saint-Exupéry', 'Literatura Infantil', 8),
('Orgullo y prejuicio', 'Jane Austen', 'Romance', 7),
('La sombra del viento', 'Carlos Ruiz Zafón', 'Misterio', 4),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Clásico', 6),
('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', 10),
('Crónica de una muerte anunciada', 'Gabriel García Márquez', 'Ficción', 2),
('El código Da Vinci', 'Dan Brown', 'Thriller', 9),
('Los juegos del hambre', 'Suzanne Collins', 'Distopía', 5);


-- Tabla prestamos
CREATE TABLE prestamos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    libro_id INT REFERENCES libros(id) ON DELETE CASCADE,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    estado VARCHAR(20) DEFAULT 'activo'
);

INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, fecha_devolucion, estado) VALUES
(1, 1, '2024-01-01', '2024-01-15', 'devuelto'),
(2, 3, '2024-01-05', NULL, 'activo'),
(3, 5, '2024-01-10', '2024-01-25', 'devuelto'),
(4, 2, '2024-02-01', NULL, 'activo'),
(5, 7, '2024-02-05', NULL, 'activo'),
(6, 4, '2024-02-10', '2024-02-20', 'devuelto'),
(7, 6, '2024-03-01', NULL, 'activo'),
(8, 9, '2024-03-05', '2024-03-15', 'devuelto'),
(9, 10, '2024-03-10', NULL, 'activo'),
(10, 8, '2024-03-15', NULL, 'activo');


-- Consultas SQL
-- Libros disponibles
SELECT * FROM libros WHERE stock > 0;

--Préstamos activos:
SELECT COUNT(*) FROM prestamos WHERE estado = 'activo';

-- Libros más prestados (último mes):
SELECT l.titulo, COUNT(p.id) AS total_prestamos
FROM prestamos p
JOIN libros l ON p.libro_id = l.id
WHERE p.fecha_prestamo >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY l.titulo
ORDER BY total_prestamos DESC
LIMIT 5;

-- TRIGGER para stock
CREATE OR REPLACE FUNCTION actualizar_stock()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.estado = 'activo' THEN
        UPDATE libros SET stock = stock - 1 WHERE id = NEW.libro_id;
    ELSIF NEW.estado = 'devuelto' THEN
        UPDATE libros SET stock = stock + 1 WHERE id = NEW.libro_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER gestion_stock
AFTER INSERT OR UPDATE ON prestamos
FOR EACH ROW EXECUTE FUNCTION actualizar_stock();