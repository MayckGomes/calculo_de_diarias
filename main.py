from funcs import *

nome = ""

input_id = 0

decisao_saldo = ""

saldo = 0

colaborador_atual = {}

saldo_placas = {}

lista_nomes = []

while True:

    print("=" * 100)
    nome = input("Digite o nome do colaborador (000 para finalizar): ").upper()

    if nome == "000":

        mostrar_saldo(saldo_placas)

        break


    lista_nomes = buscar_colaborador(nome)

    if len(lista_nomes) == 0:
        print("Não foi encontrado esse colaborador")

    if len(lista_nomes) == 1:
        nome = list(lista_nomes[0].keys())[0]
        placa = list(lista_nomes[0].values())[0]

        colaborador_atual = {nome: placa}

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

                colaborador_atual = {nome: placa}
                lista_nomes.clear()

                print(f"nome: {nome}, placa: {placa}")

                break

            except:
                print("=-" * 50)
                print("id invalido")
                print("=-" * 50)

    while True:
        print("==" * 50)

        decisao_saldo = input("deseja adicionar um saldo nesta placa?(S/N): ").upper()

        if decisao_saldo == "S" or decisao_saldo == "N":
            break

        else:
            print("=-" * 50)
            print("resposta invalida")
            print(decisao_saldo)
            print("=-" * 50)

    if decisao_saldo == "S":
        print("==" * 50)
        saldo = str(input("Digite o saldo: "))

        if "," in saldo:
            saldo = saldo.replace(",", ".")
            saldo = float(saldo)

        else:
            saldo = float(saldo)

        placa = list(colaborador_atual.values())[0]

        if placa in saldo_placas:

            saldo_placas[placa] += saldo
        else:
            saldo_placas[placa] = saldo

        mostrar_saldo(saldo_placas)