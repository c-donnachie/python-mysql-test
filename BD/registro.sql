CREATE TABLE Cuentas_bancarias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titular VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    numero INT NOT NULL,
    saldo DECIMAL(10, 2) NOT NULL
);

INSERT INTO Cuentas_bancarias (titular, tipo, numero, saldo) VALUES
('Juan Perez', 'Corriente', 1*87, 1000.00, 1),
('Maria Lopez', 'Ahorro', 2*87, 500.00, 2),
;