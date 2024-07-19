'''
------------------------------------------------------------------------------------
-- Platform:          Python + MySQL
-- Author:            Paulo Victor Innocencio
-- DRE:               116213599
-- Email:             pv.innocencio@poli.ufrj.br
-- GitHub:            https://github.com/xxpaulo-victorxx
------------------------------------------------------------------------------------
'''

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão ao MySQL DB bem sucedida")
    except Error as e:
        print(f"O erro '{e}' ocorreu")
    return connection

def registrar_cliente(connection, cliente):
    query = """
    INSERT INTO Cliente (Nome, Endereco, Telefone, Email) VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, cliente)
        connection.commit()
        print("Cliente registrado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def registrar_veiculo(connection, veiculo):
    query = """
    INSERT INTO Veiculo (Placa, Chassis, Marca, Modelo, Cor, Tipo_Mecanizacao, Ar_Condicionado, Cadeirinha, Dimensoes, ID_Grupo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, veiculo)
        connection.commit()
        print("Veículo registrado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def registrar_locacao(connection, locacao):
    query = """
    INSERT INTO Locacao (Data_Hora_Retirada, Data_Hora_Devolucao, Patio_Saida, Patio_Chegada, ID_Cliente, Placa, Estado_Entrega, Estado_Devolucao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, locacao)
        connection.commit()
        print("Locação registrada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def registrar_pagamento(connection, pagamento):
    query = """
    INSERT INTO Pagamentos (ID_Locacao, Data_Pagamento, Valor_Pago) VALUES (%s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, pagamento)
        connection.commit()
        print("Pagamento registrado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def consultar_locacoes_atuais(connection):
    query = """
    SELECT * FROM Locacao WHERE Data_Hora_Devolucao >= CURDATE()
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        locacoes = cursor.fetchall()
        for locacao in locacoes:
            print(locacao)
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def consultar_historico_locacoes(connection, id_cliente):
    query = """
    SELECT * FROM Locacao WHERE ID_Cliente = %s
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_cliente,))
        locacoes = cursor.fetchall()
        for locacao in locacoes:
            print(locacao)
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def deletar_cliente(connection, id_cliente):
    query = """
    DELETE FROM Cliente WHERE ID_Cliente = %s
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_cliente,))
        connection.commit()
        print("Cliente deletado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def deletar_veiculo(connection, placa):
    query = """
    DELETE FROM Veiculo WHERE Placa = %s
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (placa,))
        connection.commit()
        print("Veículo deletado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def deletar_locacao(connection, id_locacao):
    query = """
    DELETE FROM Locacao WHERE ID_Locacao = %s
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_locacao,))
        connection.commit()
        print("Locação deletada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def deletar_pagamento(connection, id_pagamento):
    query = """
    DELETE FROM Pagamento WHERE ID_Pagamento = %s
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_pagamento,))
        connection.commit()
        print("Pagamento deletado com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

# Configurações de conexão
connection = create_connection("127.0.0.1", "root", "password", "locadora_veiculos")

# Exemplos de uso
novo_cliente = ("Maria Silva", "Rua A, 123", "555-1234", "maria@example.com")
registrar_cliente(connection, novo_cliente)

novo_veiculo = ("ABC-1234", "1HGCM82633A123456", "Honda", "Civic", "Preto", "Automática", True, False, "4.5x1.8x1.4m", 1)
registrar_veiculo(connection, novo_veiculo)

nova_locacao = ("2023-07-01 10:00:00", "2023-07-10 10:00:00", "Patio A", "Patio B", 1, "ABC-1234", "Bom", "Bom")
registrar_locacao(connection, nova_locacao)

novo_pagamento = (1, "2023-07-01", 1500.00)
registrar_pagamento(connection, novo_pagamento)

consultar_locacoes_atuais(connection)

consultar_historico_locacoes(connection, 1)

# Exemplos de deletar dados
deletar_cliente(connection, 1)
deletar_veiculo(connection, "ABC-1234")
deletar_locacao(connection, 1)
deletar_pagamento(connection, 1)

# Fechar a conexão
connection.close()
print("Conexão fechada")
