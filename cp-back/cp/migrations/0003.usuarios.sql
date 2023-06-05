CREATE TABLE usuarios
(
    id         INT AUTO_INCREMENT                NOT NULL,
    id_cliente INT,
    login      VARCHAR(255) UNIQUE               NOT NULL,
    password   VARCHAR(2048)                     NOT NULL,
    role       ENUM ('CLIENTE', 'ADMINISTRADOR') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE
);

INSERT INTO usuarios (id_cliente, login, password, role)
VALUES (1, 'cliente', '$2b$12$hoZLuZSddNEus21uyEtxFezKzVkEIgzAqfOODfiIMdYREWuJpnpV6', 'CLIENTE');
INSERT INTO usuarios (id_cliente, login, password, role)
VALUES (2, 'teste', '$2b$12$hoZLuZSddNEus21uyEtxFeauQb96lQKt0gdZPibgQUG', 'CLIENTE');
INSERT INTO usuarios (login, password, role)
VALUES ('administrador', '$2b$12$hoZLuZSddNEus21uyEtxFevLea2/.bfBZoL4YcFMDxSKc3/8i5kmS', 'ADMINISTRADOR');