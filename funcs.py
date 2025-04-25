from openpyxl import *

lista_nomes = []

colaborador = {}

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

def buscar_colaborador(
        nome: str,
        lista_arquivos: list,
        lista_tabelas: list
        ):

    for index in range(len(lista_tabelas)):

        arquivo = load_workbook(lista_arquivos[index])

        planilha = arquivo[lista_tabelas[index]]

        lista_motoristas = planilha["B"]

        lista_ajudantes1 = planilha["E"]

        lista_ajudantes2 = planilha["F"]

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

def verificar_lista_nomes(lista: list):

    global colaborador

    if len(lista_nomes) == 0:
        colaborador = {}
        print("Não foi encontrado um colaborador com esse nome!")

    elif len(lista_nomes) == 1:

        nome = list(lista_nomes[0].keys())[0]
        placa = list(lista_nomes[0].values())[0]

        colaborador = {nome: placa}

        lista_nomes.clear()

        print("\n")
        print(f"nome: {nome}, placa: {placa}")

    if len(lista_nomes) > 1:

        while True:

            try:

                print("=" * 100)

                print("Existe mais de um colaborador com este nome, qual seria o certo: ")
                print("\n")
                for id_nome in range(len(lista_nomes)):
                    nomebusca = list(lista_nomes[id_nome].keys())[0]

                    print(f"id: {id_nome}, nome: {nomebusca}")

                input_id = int(input("id do colaborador: "))

                nome = list(lista_nomes[input_id].keys())[0]
                placa = list(lista_nomes[input_id].values())[0]

                colaborador = {nome: placa}
                lista_nomes.clear()

                print(f"nome: {nome}, placa: {placa}")

                break

            except:
                print("=-" * 50)
                print("id invalido")
                print("=-" * 50)
                
    return colaborador
                            
