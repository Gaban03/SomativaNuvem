USE aero_solutions;

CREATE TABLE aeronaves (
    id_aeronave INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(60),
    fabricante VARCHAR(60),
    horas_voo FLOAT
);

CREATE TABLE mecanico (
    id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR (60),
    cpf VARCHAR (14)
);

CREATE TABLE certificacao (
	id_certificacao INT AUTO_INCREMENT PRIMARY KEY,
    id_mecanico INT,
    apto BOOL,
    FOREIGN KEY (id_mecanico) REFERENCES mecanico(id_mecanico)
);

CREATE TABLE manutencao (
	id_manutencao INT AUTO_INCREMENT PRIMARY KEY,
    id_aeronave INT,
    id_certificacao INT,
    OS VARCHAR(15),
    responsavel VARCHAR(60),
    tipo_de_manutencao VARCHAR(30),
    data_manutencao DATETIME DEFAULT NOW(),
    FOREIGN KEY (id_aeronave) REFERENCES aeronaves(id_aeronave),
    FOREIGN KEY (id_certificacao) REFERENCES certificacao(id_certificacao)
);

CREATE TABLE pecas (
	id_pecas INT AUTO_INCREMENT PRIMARY KEY,
    id_manutencao INT,
    peca VARCHAR(150),
    quantidade INT,
    FOREIGN KEY (id_manutencao) REFERENCES manutencao(id_manutencao)
);

INSERT INTO certificacao(id_mecanico, apto) VALUES 
('1', true),
('2', false);