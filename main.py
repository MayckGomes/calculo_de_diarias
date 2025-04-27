from funcs import *

import os

nome = ""

decisao_saldo = ""

caminho_arquivo = ""

nome_tabela = ""

input_id = 0

saldo = 0

decisao_menu = 0

colaborador_atual = {}

saldo_placas = {}

lista_nomes = []

while True:
    os.system("cls")
    print("=="*50)
    print("Menu")
    print("1 - Ver um colaborador e adicionar um saldo")
    print("2 - Apenas ver um colaborador")
    print("3 - Mostrar saldos")

    try:
        decisao_menu = int(input("Digite a sua opção: "))

        if decisao_menu > 4 or decisao_menu < 1:
            print("Opção invalida")

    except:
        print("Opção invalida")

    else: 

        match decisao_menu:

            case 1:

                nome = input("digite o nome do colaborador(000 para parar): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(nome= nome.upper())


                if len(lista_nomes) == 0:
        
                    print("Não foi encontrado um colaborador com esse nome!")

                elif len(lista_nomes) == 1:

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
                    decisao_saldo = input("Deseja colocar um saldo nesta placa?(S/N): ").upper()

                    if decisao_saldo == "S" or decisao_saldo == "N":
                        break

                    else:
                        print("resposta invalida")

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
                    input()


            case 2:
                
                nome = input("digite o nome do colaborador(000 para parar): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(nome= nome.upper())

                if len(lista_nomes) == 0:
            
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
                            
                
                input()

            case 3:
                mostrar_saldo(saldo_placas)
                input()


