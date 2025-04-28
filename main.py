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

                nome = input("digite o nome do colaborador(000 para sair): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(nome= nome.upper())
                            
                colaborador_atual = verificar_lista(lista_nomes)

                if colaborador_atual != {}:

                    while True:    
                        decisao_saldo = input("Deseja colocar um saldo nesta placa?(S/N): ").upper()

                        if decisao_saldo == "S" or decisao_saldo == "N":
                            break

                        else:
                            print("resposta invalida")

                    if decisao_saldo == "S":
                        
                        saldo = str(input("Digite o saldo: "))

                        adicionar_saldo(
                            valor = saldo,
                            colaborador = colaborador_atual,
                            saldo_list = saldo_placas, 
                        )

                        input()


            case 2:
                
                nome = input("digite o nome do colaborador(000 para parar): ")

                if nome == "000":
                    break
                
                lista_nomes = buscar_colaborador(nome= nome.upper())

                colaborador_atual = verificar_lista(lista_nomes)            
                
                input()

            case 3:
                
                mostrar_saldo(saldo_placas)
                input()


