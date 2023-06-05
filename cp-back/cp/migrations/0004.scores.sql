CREATE TABLE scores
(
    id         INT AUTO_INCREMENT                                  NOT NULL,
    timestamp  DATETIME                                            NOT NULL DEFAULT NOW(),
    id_cliente INT                                                 NOT NULL,
    desempenho ENUM ('PÉSSIMO', 'RUIM', 'REGULAR', 'BOM', 'ÓTIMO') NOT NULL,
    risco      ENUM ('BAIXO', 'MÉDIO', 'ALTO')                     NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_cliente) REFERENCES clientes (id) ON DELETE CASCADE
);

INSERT INTO scores (id_cliente, desempenho, risco)
VALUES (1, 'BOM', 'BAIXO');

INSERT INTO scores (id_cliente, desempenho, risco)
VALUES (2, 'REGULAR', 'MÉDIO');

INSERT INTO scores (id_cliente, desempenho, risco)
VALUES (3, 'PÉSSIMO', 'ALTO');