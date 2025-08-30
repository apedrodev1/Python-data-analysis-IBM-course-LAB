import json
import xlwt
from classes.cliente import Cliente

CUSTOMERS_PATH = "data/customers.json"
EXPORT_CUSTOMERS_PATH = "data/clientes.xls"

def carregar_clientes():
    try:
        with open(CUSTOMERS_PATH, "r") as file:
            data = json.load(file)
            clientes = []
            for c in data.values():
                cliente = Cliente(
                    id_cliente=c["id_cliente"],
                    nome=c["nome"],
                    email=c["email"]
                )
                clientes.append(cliente)
            return clientes
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_clientes(clientes):
    data = {cliente.id_cliente: cliente.to_dict() for cliente in clientes}
    with open(CUSTOMERS_PATH, "w") as file:
        json.dump(data, file, indent=4)

def adicionar_cliente(id_cliente, nome, email):
    clientes = carregar_clientes()
    if any(c.id_cliente == id_cliente for c in clientes):
        raise ValueError("ID de cliente já cadastrado.")
    novo = Cliente(id_cliente, nome, email)
    clientes.append(novo)
    salvar_clientes(clientes)

def listar_clientes():
    return carregar_clientes()

def buscar_cliente_por_id(id_cliente):
    clientes = carregar_clientes()
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None

def editar_cliente(id_cliente, novo_nome=None, novo_email=None):
    clientes = carregar_clientes()
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            if novo_nome:
                cliente.nome = novo_nome
            if novo_email:
                cliente.email = novo_email
            salvar_clientes(clientes)
            return
    raise ValueError("Cliente não encontrado.")

def remover_cliente(id_cliente):
    clientes = carregar_clientes()
    clientes = [c for c in clientes if c.id_cliente != id_cliente]
    salvar_clientes(clientes)

def exportar_clientes_para_xls():
    clientes = carregar_clientes()
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Clientes")
    headers = ["ID", "Nome", "Email"]
    for col, header in enumerate(headers):
        sheet.write(0, col, header)
    for row, cliente in enumerate(clientes, start=1):
        sheet.write(row, 0, cliente.id_cliente)
        sheet.write(row, 1, cliente.nome)
        sheet.write(row, 2, cliente.email)
    workbook.save(EXPORT_CUSTOMERS_PATH)
    print(f"✅ Clientes exportados para {EXPORT_CUSTOMERS_PATH}")
