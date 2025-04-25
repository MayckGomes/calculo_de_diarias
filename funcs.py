from openpyxl import *

lista_nomes = []

arquivo = load_workbook("motoristas.xlsx")

planilha = arquivo["Planilha1"]

lista_motoristas = planilha["B"]

lista_ajudantes1 = planilha["E"]

lista_ajudantes2 = planilha["F"]

def mostrar_saldo(saldo_placas: dict):
    print("==" * 50)
    print("SALDOS")
    print("\n")

    acumulador = 0

    for saldo in saldo_placas.items():
        placasaldo = saldo[0]
        valorsaldo = saldo[1]

        acumulador += valorsaldo

        print(f"placa: {placasaldo}, saldo: {valorsaldo}")

    print("=-" * 50)
    print(f"Total = {acumulador}")

def buscar_colaborador(nome: str):

    for motorista in range(3, len(lista_motoristas) + 1):

        nome_motorista = planilha.cell(row=motorista, column=2).value

        if nome_motorista == None:
            continue

        if nome in nome_motorista:
            placa = planilha.cell(row=motorista, column=3).value

            lista_nomes.append({nome_motorista: placa})

    for ajudante1 in range(3, len(lista_ajudantes1) + 1):

        nome_ajudante1 = planilha.cell(row=ajudante1, column=5).value

        if nome_ajudante1 is None:
            continue

        if nome in nome_ajudante1:
            placa = planilha.cell(row=ajudante1, column=3).value

            lista_nomes.append({nome_ajudante1: placa})

    for ajudante2 in range(3, len(lista_ajudantes2) + 1):

        nome_ajudante2 = planilha.cell(row=ajudante2, column=6).value

        if nome_ajudante2 is None:
            continue

        if nome in nome_ajudante2:
            placa = planilha.cell(row=ajudante2, column=3).value

            lista_nomes.append({nome_ajudante2: placa})

    return lista_nomes