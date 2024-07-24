import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Funções de banco de dados
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
        messagebox.showinfo("Sucesso", "Cliente registrado com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

def registrar_veiculo(connection, veiculo):
    query = """
    INSERT INTO Veiculo (Placa, Chassis, Marca, Modelo, Cor, Tipo_Mecanizacao, Ar_Condicionado, Cadeirinha, Dimensoes, ID_Grupo) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, veiculo)
        connection.commit()
        messagebox.showinfo("Sucesso", "Veículo registrado com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

def registrar_locacao(connection, locacao):
    query = """
    INSERT INTO Locacao (Data_Hora_Retirada, Data_Hora_Devolucao, Patio_Saida, Patio_Chegada, ID_Cliente, Placa, Estado_Entrega, Estado_Devolucao) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, locacao)
        connection.commit()
        messagebox.showinfo("Sucesso", "Locação registrada com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

def deletar_cliente(connection, id_cliente):
    query = "DELETE FROM Cliente WHERE ID_Cliente = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_cliente,))
        connection.commit()
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

def deletar_veiculo(connection, placa):
    query = "DELETE FROM Veiculo WHERE Placa = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (placa,))
        connection.commit()
        messagebox.showinfo("Sucesso", "Veículo deletado com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

def deletar_locacao(connection, id_locacao):
    query = "DELETE FROM Locacao WHERE ID_Locacao = %s"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id_locacao,))
        connection.commit()
        messagebox.showinfo("Sucesso", "Locação deletada com sucesso")
    except Error as e:
        messagebox.showerror("Erro", f"O erro '{e}' ocorreu")

# Interface gráfica com tkinter
def criar_interface():
    def registrar_cliente_interface():
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        cliente = (nome, endereco, telefone, email)
        registrar_cliente(connection, cliente)

    def registrar_veiculo_interface():
        placa = entry_placa.get()
        chassis = entry_chassis.get()
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        cor = entry_cor.get()
        tipo_mecanizacao = entry_tipo_mecanizacao.get()
        ar_condicionado = entry_ar_condicionado.get()
        cadeirinha = entry_cadeirinha.get()
        dimensoes = entry_dimensoes.get()
        id_grupo = entry_id_grupo.get()
        veiculo = (placa, chassis, marca, modelo, cor, tipo_mecanizacao, ar_condicionado, cadeirinha, dimensoes, id_grupo)
        registrar_veiculo(connection, veiculo)

    def registrar_locacao_interface():
        data_hora_retirada = entry_data_hora_retirada.get()
        data_hora_devolucao = entry_data_hora_devolucao.get()
        patio_saida = entry_patio_saida.get()
        patio_chegada = entry_patio_chegada.get()
        id_cliente = entry_id_cliente_locacao.get()
        placa = entry_placa_locacao.get()
        estado_entrega = entry_estado_entrega.get()
        estado_devolucao = entry_estado_devolucao.get()
        locacao = (data_hora_retirada, data_hora_devolucao, patio_saida, patio_chegada, id_cliente, placa, estado_entrega, estado_devolucao)
        registrar_locacao(connection, locacao)

    def deletar_cliente_interface():
        id_cliente = entry_id_cliente_del.get()
        deletar_cliente(connection, id_cliente)

    def deletar_veiculo_interface():
        placa = entry_placa_del.get()
        deletar_veiculo(connection, placa)

    def deletar_locacao_interface():
        id_locacao = entry_id_locacao_del.get()
        deletar_locacao(connection, id_locacao)

    app = tk.Tk()
    app.title("Sistema de Locadora de Veículos")

    # Registro de Cliente
    frame_cliente = tk.Frame(app)
    frame_cliente.pack(pady=10)
    tk.Label(frame_cliente, text="Nome:").grid(row=0, column=0)
    entry_nome = tk.Entry(frame_cliente)
    entry_nome.grid(row=0, column=1)
    tk.Label(frame_cliente, text="Endereço:").grid(row=1, column=0)
    entry_endereco = tk.Entry(frame_cliente)
    entry_endereco.grid(row=1, column=1)
    tk.Label(frame_cliente, text="Telefone:").grid(row=2, column=0)
    entry_telefone = tk.Entry(frame_cliente)
    entry_telefone.grid(row=2, column=1)
    tk.Label(frame_cliente, text="Email:").grid(row=3, column=0)
    entry_email = tk.Entry(frame_cliente)
    entry_email.grid(row=3, column=1)
    btn_registrar_cliente = tk.Button(frame_cliente, text="Registrar Cliente", command=registrar_cliente_interface)
    btn_registrar_cliente.grid(row=4, columnspan=2)

    # Registro de Veículo
    frame_veiculo = tk.Frame(app)
    frame_veiculo.pack(pady=10)
    tk.Label(frame_veiculo, text="Placa:").grid(row=0, column=0)
    entry_placa = tk.Entry(frame_veiculo)
    entry_placa.grid(row=0, column=1)
    tk.Label(frame_veiculo, text="Chassis:").grid(row=1, column=0)
    entry_chassis = tk.Entry(frame_veiculo)
    entry_chassis.grid(row=1, column=1)
    tk.Label(frame_veiculo, text="Marca:").grid(row=2, column=0)
    entry_marca = tk.Entry(frame_veiculo)
    entry_marca.grid(row=2, column=1)
    tk.Label(frame_veiculo, text="Modelo:").grid(row=3, column=0)
    entry_modelo = tk.Entry(frame_veiculo)
    entry_modelo.grid(row=3, column=1)
    tk.Label(frame_veiculo, text="Cor:").grid(row=4, column=0)
    entry_cor = tk.Entry(frame_veiculo)
    entry_cor.grid(row=4, column=1)
    tk.Label(frame_veiculo, text="Tipo de Mecanização:").grid(row=5, column=0)
    entry_tipo_mecanizacao = tk.Entry(frame_veiculo)
    entry_tipo_mecanizacao.grid(row=5, column=1)
    tk.Label(frame_veiculo, text="Ar Condicionado:").grid(row=6, column=0)
    entry_ar_condicionado = tk.Entry(frame_veiculo)
    entry_ar_condicionado.grid(row=6, column=1)
    tk.Label(frame_veiculo, text="Cadeirinha:").grid(row=7, column=0)
    entry_cadeirinha = tk.Entry(frame_veiculo)
    entry_cadeirinha.grid(row=7, column=1)
    tk.Label(frame_veiculo, text="Dimensões:").grid(row=8, column=0)
    entry_dimensoes = tk.Entry(frame_veiculo)
    entry_dimensoes.grid(row=8, column=1)
    tk.Label(frame_veiculo, text="ID Grupo:").grid(row=9, column=0)
    entry_id_grupo = tk.Entry(frame_veiculo)
    entry_id_grupo.grid(row=9, column=1)
    btn_registrar_veiculo = tk.Button(frame_veiculo, text="Registrar Veículo", command=registrar_veiculo_interface)
    btn_registrar_veiculo.grid(row=10, columnspan=2)

    # Registro de Locação
    frame_locacao = tk.Frame(app)
    frame_locacao.pack(pady=10)
    tk.Label(frame_locacao, text="Data/Hora Retirada:").grid(row=0, column=0)
    entry_data_hora_retirada = tk.Entry(frame_locacao)
    entry_data_hora_retirada.grid(row=0, column=1)
    tk.Label(frame_locacao, text="Data/Hora Devolução:").grid(row=1, column=0)
    entry_data_hora_devolucao = tk.Entry(frame_locacao)
    entry_data_hora_devolucao.grid(row=1, column=1)
    tk.Label(frame_locacao, text="Pátio Saída:").grid(row=2, column=0)
    entry_patio_saida = tk.Entry(frame_locacao)
    entry_patio_saida.grid(row=2, column=1)
    tk.Label(frame_locacao, text="Pátio Chegada:").grid(row=3, column=0)
    entry_patio_chegada = tk.Entry(frame_locacao)
    entry_patio_chegada.grid(row=3, column=1)
    tk.Label(frame_locacao, text="ID Cliente:").grid(row=4, column=0)
    entry_id_cliente_locacao = tk.Entry(frame_locacao)
    entry_id_cliente_locacao.grid(row=4, column=1)
    tk.Label(frame_locacao, text="Placa:").grid(row=5, column=0)
    entry_placa_locacao = tk.Entry(frame_locacao)
    entry_placa_locacao.grid(row=5, column=1)
    tk.Label(frame_locacao, text="Estado Entrega:").grid(row=6, column=0)
    entry_estado_entrega = tk.Entry(frame_locacao)
    entry_estado_entrega.grid(row=6, column=1)
    tk.Label(frame_locacao, text="Estado Devolução:").grid(row=7, column=0)
    entry_estado_devolucao = tk.Entry(frame_locacao)
    entry_estado_devolucao.grid(row=7, column=1)
    btn_registrar_locacao = tk.Button(frame_locacao, text="Registrar Locação", command=registrar_locacao_interface)
    btn_registrar_locacao.grid(row=8, columnspan=2)

    # Deletar Cliente
    frame_del_cliente = tk.Frame(app)
    frame_del_cliente.pack(pady=10)
    tk.Label(frame_del_cliente, text="ID Cliente:").grid(row=0, column=0)
    entry_id_cliente_del = tk.Entry(frame_del_cliente)
    entry_id_cliente_del.grid(row=0, column=1)
    btn_deletar_cliente = tk.Button(frame_del_cliente, text="Deletar Cliente", command=deletar_cliente_interface)
    btn_deletar_cliente.grid(row=1, columnspan=2)

    # Deletar Veículo
    frame_del_veiculo = tk.Frame(app)
    frame_del_veiculo.pack(pady=10)
    tk.Label(frame_del_veiculo, text="Placa:").grid(row=0, column=0)
    entry_placa_del = tk.Entry(frame_del_veiculo)
    entry_placa_del.grid(row=0, column=1)
    btn_deletar_veiculo = tk.Button(frame_del_veiculo, text="Deletar Veículo", command=deletar_veiculo_interface)
    btn_deletar_veiculo.grid(row=1, columnspan=2)

    # Deletar Locação
    frame_del_locacao = tk.Frame(app)
    frame_del_locacao.pack(pady=10)
    tk.Label(frame_del_locacao, text="ID Locação:").grid(row=0, column=0)
    entry_id_locacao_del = tk.Entry(frame_del_locacao)
    entry_id_locacao_del.grid(row=0, column=1)
    btn_deletar_locacao = tk.Button(frame_del_locacao, text="Deletar Locação", command=deletar_locacao_interface)
    btn_deletar_locacao.grid(row=1, columnspan=2)

    app.mainloop()

# Configurações de conexão
connection = create_connection("127.0.0.1", "root", "password", "locadora_veiculos")

# Inicializar a interface
criar_interface()

# Fechar a conexão
connection.close()
print("Conexão fechada")
