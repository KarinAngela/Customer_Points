CREATE TABLE clientes
(
    id      INT AUTO_INCREMENT  NOT NULL,
    nome    VARCHAR(256)        NOT NULL,
    cpf     VARCHAR(14) UNIQUE  NOT NULL,
    cnpj    VARCHAR(18) UNIQUE,
    salario FLOAT               NOT NULL,
    dividas ENUM ('SIM', 'NÃO') NOT NULL DEFAULT 'NÃO',
    PRIMARY KEY (id)
);

INSERT INTO clientes (nome, cpf, salario, dividas)
VALUES ('Cliente Um', '111.222.333-44', 3000.00, 'NÃO');
INSERT INTO clientes (nome, cpf, salario, dividas)
VALUES ('Cliente Dois', '222.333.444-55', 1500.00, 'SIM');
INSERT INTO clientes (nome, cpf, salario, dividas)
VALUES ('Cliente Tres', '333.444.555-66', 4500.00, 'NÃO');