CREATE DATABASE IF NOT EXISTS banco_db;

USE banco_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO Usuarios (usuario, password) VALUES
('usuario1', MD5('password1')),
('usuario2', MD5('password2'))
;