------------------------------------------------------------------------------------
-- Platform:          MySQL
-- Author:            Paulo Victor Innocencio
-- DRE:               116213599
-- Email:             pv.innocencio@poli.ufrj.br
-- GitHub:            https://github.com/xxpaulo-victorxx
------------------------------------------------------------------------------------

CREATE DATABASE locadora_veiculos;
USE locadora_veiculos;


CREATE TABLE Grupo_Veiculos (
    ID_Grupo INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Grupo VARCHAR(50) NOT NULL,
    Faixa_Valor_Aluguel DECIMAL(10, 2) NOT NULL
);


CREATE TABLE Veiculo (
    Placa VARCHAR(10) PRIMARY KEY,
    Chassis VARCHAR(50) NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(50) NOT NULL,
    Cor VARCHAR(20) NOT NULL,
    Tipo_Mecanizacao ENUM('Manual', 'Automática') NOT NULL,
    Ar_Condicionado BOOLEAN NOT NULL,
    Cadeirinha BOOLEAN NOT NULL,
    Dimensoes VARCHAR(50),
    ID_Grupo INT,
    FOREIGN KEY (ID_Grupo) REFERENCES Grupo_Veiculos(ID_Grupo)
);


CREATE TABLE Acessorio (
    ID_Acessorio INT AUTO_INCREMENT PRIMARY KEY,
    Descricao VARCHAR(100) NOT NULL
);


CREATE TABLE Veiculo_Acessorio (
    Placa VARCHAR(10),
    ID_Acessorio INT,
    PRIMARY KEY (Placa, ID_Acessorio),
    FOREIGN KEY (Placa) REFERENCES Veiculo(Placa),
    FOREIGN KEY (ID_Acessorio) REFERENCES Acessorio(ID_Acessorio)
);


CREATE TABLE Cliente (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) NOT NULL
);


CREATE TABLE Pessoa_Fisica (
    ID_Cliente INT PRIMARY KEY,
    CPF VARCHAR(11) NOT NULL,
    Data_Nascimento DATE NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);


CREATE TABLE Pessoa_Juridica (
    ID_Cliente INT PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);


CREATE TABLE Funcionario (
    ID_Funcionario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    ID_Pessoa_Juridica INT,
    FOREIGN KEY (ID_Pessoa_Juridica) REFERENCES Pessoa_Juridica(ID_Cliente)
);


CREATE TABLE CNH (
    Numero_CNH VARCHAR(20) PRIMARY KEY,
    Data_Expiracao DATE NOT NULL,
    ID_Funcionario INT,
    FOREIGN KEY (ID_Funcionario) REFERENCES Funcionario(ID_Funcionario)
);


CREATE TABLE Reserva (
    ID_Reserva INT AUTO_INCREMENT PRIMARY KEY,
    Data_Reserva DATE NOT NULL,
    Data_Retirada DATE NOT NULL,
    Data_Devolucao DATE NOT NULL,
    ID_Cliente INT,
    Placa VARCHAR(10),
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (Placa) REFERENCES Veiculo(Placa)
);


CREATE TABLE Locacao (
    ID_Locacao INT AUTO_INCREMENT PRIMARY KEY,
    Data_Hora_Retirada DATETIME NOT NULL,
    Data_Hora_Devolucao DATETIME,
    Patio_Saida VARCHAR(100) NOT NULL,
    Patio_Chegada VARCHAR(100),
    ID_Cliente INT,
    Placa VARCHAR(10),
    Estado_Entrega TEXT,
    Estado_Devolucao TEXT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (Placa) REFERENCES Veiculo(Placa)
);


CREATE TABLE Foto (
    ID_Foto INT AUTO_INCREMENT PRIMARY KEY,
    URL_Foto VARCHAR(255) NOT NULL,
    Placa VARCHAR(10),
    FOREIGN KEY (Placa) REFERENCES Veiculo(Placa)
);


CREATE TABLE Prontuario (
    ID_Prontuario INT AUTO_INCREMENT PRIMARY KEY,
    Data_Registro DATE NOT NULL,
    Descricao TEXT NOT NULL,
    Placa VARCHAR(10),
    FOREIGN KEY (Placa) REFERENCES Veiculo(Placa)
);


CREATE TABLE Protecao_Adicional (
    ID_Protecao INT AUTO_INCREMENT PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL,
    Valor DECIMAL(10, 2) NOT NULL
);


CREATE TABLE Locacao_Protecao (
    ID_Locacao INT,
    ID_Protecao INT,
    PRIMARY KEY (ID_Locacao, ID_Protecao),
    FOREIGN KEY (ID_Locacao) REFERENCES Locacao(ID_Locacao),
    FOREIGN KEY (ID_Protecao) REFERENCES Protecao_Adicional(ID_Protecao)
);
