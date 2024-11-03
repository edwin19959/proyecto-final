-- Active: 1730662046468@@127.0.0.1@3306@nuevadata
REATE DATABASE IF NOT EXISTS nuevaData;
CREAR BASE DE DATOS SI NO EXISTE nuevaData;
USE nuevaData;

-- Crear la tabla de comentarios
CREATE TABLE IF NOT EXISTS comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    comentario NVARCHAR(500) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_fecha (fecha DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


SELECT * from comentarios