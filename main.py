'''
O objetivo desse projeto é criar uma Ouvidoria para a faculdade, e posteriormente
integrá-lo com um Banco de dados para armazenamento desses dados, treinando os
comandos aprendidos na disciplina de Python.
'''

# listas
ocorrencias = []

# comandos importados
from operacoesbd import *

# banco de dados
conexao = abrirBancoDados('localhost','root','pastel1doce','ouvidoria01')

# mensagem automática de boas vindas:
print("Seja bem vindo à Ouvidoria da Unifacisa! \n")

# menu
opcao = 100
while opcao != 6:
    print("\n" + "MENU" + "\n")
    print()
    print("[ 1 ] Listar Ocorrências \n")
    print("[ 2 ] Cadastrar Ocorrências \n")
    print("[ 3 ] Consultar Ocorrência por Código \n")
    print("[ 4 ] Apagar Ocorrências \n")
    print("[ 5 ] Alterar Ocorrência \n")
    print("[ 6 ] Sair do Sistema \n")

    opcao = int(input('Escolha a sua opção: '))

 # listar ocorrências
    if opcao == 1:
        if len(ocorrencias) == 0:
            print("\n" + 'Ainda não existem ocorrências a serem exibidas!')

        elif len(ocorrencias) != 0:
            print("\n" + 'Ocorrências cadastradas até o momento: ')
            for i in range(len(ocorrencias)):
                print('-', (i + 1), (ocorrencias[i]))

# cadastrar ocorrências
    elif opcao == 2:
        novaOcorrencia = input("\n" + 'Digite a ocorrência que deseja adicionar: ')
        ocorrencias.append(novaOcorrencia)
        indice = len(ocorrencias)
        print("Sua ocorrência foi cadastrada com sucesso! Seu código é :", indice)

# consultar ocorrências por código
    elif opcao == 3:
        if len(ocorrencias) == 0:
            print("\n" + 'Ainda não existem ocorrências a serem exibidas!')

        else:
            codigo = int(input("\n" + 'Digite o código da ocorrência: '))
            if codigo <= len(ocorrencias):
                ocorrenciaPesquisada = ocorrencias[codigo - 1]
                print("\n" + ' A ocorrência pesquisada foi:', ocorrenciaPesquisada + '!')
            else:
                print("\n" + 'Código inválido!')

# apagar ocorrências

    elif opcao == 4:
        print("\n" + "[ 1 ] Apagar ocorrência por código" + "\n")
        print("[ 2 ] Apagar tudo do sistema" + "\n")

        apagar = int(input("Digite a sua opção: "))

        if apagar == 1:
            codigo = int(input("\n" + 'Digite o código da ocorrência que você deseja remover: '))
            if codigo <= len(ocorrencias):
                ocorrencias.pop(codigo - 1)
                print("\n" + 'A sua ocorrência foi removida com sucesso!')
            else:
                print("\n" + 'Código inválido!')

        elif apagar == 2:
            ocorrencias.clear()
            print("\n" + 'Todas as ocorrências foram removidas com sucesso!')

# editar ocorrência

    elif opcao == 5:
        if len(ocorrencias) == 0:
            print("\n" + 'Ainda não existem ocorrências a serem exibidas!')

        else:
            ocorrenciaEdit = int(input("\n" + 'Digite o código da ocorrência: '))
            if ocorrenciaEdit <= len(ocorrencias):
                ocorrenciaNova = input("\n" + 'Digite uma nova ocorrência: ')
                ocorrencias[ocorrenciaEdit - 1] = ocorrenciaNova
                print("\n" + "Ocorrência alterada com sucesso!")

            else:
                print("\n" + 'Código inválido!')

# sair do sistema

    else:
        print("\n" + "Agradecemos por ter utilizado o nosso sistema da Ouvidoria da Unifacisa.")
        print(" Entraremos em contato assim que obtivermos uma resposta para a reclamação ou sugestão.")

encerrarBancoDados(conexao)