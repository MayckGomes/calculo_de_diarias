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

lista_arquivos = []

lista_tabelas = []

while True:
    os.system("cls")
    print("=="*50)
    print("Menu")
    print("1 - Adicionar um arquivo")
    print("2 - Ver um colaborador e adicionar um saldo")
    print("3 - Apenas ver um colaborador")
    print("4 - Mostrar saldos")

    try:
        decisao_menu = int(input("Digite a sua opção: "))

        if decisao_menu > 4 or decisao_menu < 1:
            print("Opção invalida")

    except:
        print("Opção invalida")

    else: 

        match decisao_menu:

            case 1:
                caminho_arquivo = input("Cole aqui o caminho para o arquivo, mais o tipo (C:/usuario/planilha.xlsx) :")

                lista_arquivos.append(caminho_arquivo)

                print("Caminho adicionado com sucesso!\n")

                nome_tabela = input("Agora digite o nome da tabela do arquivo: ")

                lista_tabelas.append(nome_tabela)

                print("Arquivo adicionado com sucesso")
                input()

            case 2:

                nome = input("digite o nome do colaborador(000 para parar): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(
                    nome= nome.upper(),
                    lista_arquivos=lista_arquivos,
                    lista_tabelas=lista_tabelas
                )

                colaborador_atual = verificar_lista_nomes(lista_nomes)

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


            case 3:
                
                nome = input("digite o nome do colaborador(000 para parar): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(
                    nome= nome.upper(),
                    lista_arquivos=lista_arquivos,
                    lista_tabelas=lista_tabelas
                )

                colaborador_atual = verificar_lista_nomes(lista_nomes)
                input()

            case 4:
                mostrar_saldo(saldo_placas)
                input()


