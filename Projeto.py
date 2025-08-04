# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Cadastro de Contribuintes cao!")

#Lista que armazenará os contribuintes cadastrados
lista_contribuintes = []

#Variável global para gerar IDs únicos para os contribuintes
#Começa em 0 e será incrementada para cada novo contribuinte
id_global = 0

def cadastrar_contribuinte():
#Função para cadastrar um novo contribuinte.
#Gera um ID único para o contribuinte automaticamente.
    global id_global #Declara que estamos usando a variável global id_global
    id_global += 1   

    #Pergunta os detalhes do contribuinte ao usuário
    nome = input("Digite o nome do contribuinte: ")
    primeira_contribuicao = input("Digite a data em que o contribuinte fez sua primeira contribuição: ")
    valor = input(int("Digite o valor contribuído mensalmente: "))

    #Cria um dicionário com os dados do contribuinte
    contribuinte = {
        'id': id_global,
        'nome': nome,
        'primeira contribuição': primeira_contribuicao,
        'valor': valor
    }
    #Adiciona o dicionário à lista de contribuintes
    lista_contribuintes.append(contribuinte)
    print(f"Contribuinte '{nome}' (ID: {id_global}) cadastrado com sucesso!\n")

def consultar_contribuinte():
    #Função para consultar contribuinte.
    #Permite consultar todos, por ID ou por nome.
    while True:
        print("\n--- Menu de Consulta ---")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por nome")
        print("4. Retornar ao menu principal")
        opcao_consulta = input("Escolha uma opção: ")

        if opcao_consulta == '1':
            #Consultar todos os ccontribuintes
            if not lista_contribuintes:
                print("Nenhum contribuinte cadastrado para exibir.")
            else:
                print("\n--- Contribuintes Cadastrados ---")
                for contribuinte in lista_contribuintes:
                    print(f"ID: {contribuinte['id']}")
                    print(f"Nome: {contribuinte['nome']}")
                    print(f"Bairro: {contribuinte['bairro']}")
                    print(f"Porte: {contribuinte['porte']}\n")
        elif opcao_consulta == '2':
            #Consultar por ID
            try:
                id_consulta = int(input("Digite o ID do contribuinte que deseja consultar: "))
                encontrado = False
                for contribuinte in lista_contribuintes:
                    if contribuinte['id'] == id_consulta:
                        print(f"\n--- Detalhes do contribuinte (ID: {contribuinte['id']}) ---")
                        print(f"Nome: {contribuinte['nome']}")
                        print(f"contribuinte: {contribuinte['contribuinte']}")
                        print(f"Valor: {contribuinte['Reais']}\n")
                        encontrado = True
                        break # Sai do loop assim que encontra o contribuinte
                if not encontrado:
                    print(f"contribuinte com ID '{id_consulta}' não encontrado.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para o ID.")
        elif opcao_consulta == '3':
            #Consultar por contribuinte
            contribuinte_consulta = input("Digite o nome do contribuinte que deseja consultar: ")
            #Filtra nome cujo contribuinte corresponde
            encontrados = [contribuinte for contribuinte in lista_contribuintes if contribuinte['contribuinte'].lower() == contribuinte.lower()]
            if encontrados:
                print(f"\n--- Dados do contribuinte: {contribuinte_consulta} ---")
                for ccontribuinte in encontrados:
                    print(f"ID: {contribuinte['id']}")
                    print(f"Nome: {contribuinte['nome']}")
                    print(f"Bairro: {contribuinte['editora']}\n")
            else:
                print(f"Nenhum contribuinte encontrado. '{contribuinte_consulta}'.")
        elif opcao_consulta == '4':
            #Retornar ao menu principal
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

def remover_contribuinte():
#Função para remover um contribuinte da lista pelo seu ID.
    if not lista_contribuintes:
        print("Não há contribuintes cadastrados para remover.")
        return

    try:
        id_remover = int(input("Digite o ID do contribuinte que deseja remover: "))
        removido = False
        #Itera sobre a lista usando enumerate para ter acesso ao índice
        for i, contribuintes in enumerate(lista_contribuintes):
            if contribuintes['id'] == id_remover:
                nome_contribuintes_removido = lista_contribuintes.pop(i)['nome'] # Remove o contribuinte e pega o nome
                print(f"contribuinte '{nome_contribuintes_removido}' (ID: {id_remover}) removido com sucesso!")
                removido = True
                break
        if not removido:
            print(f"contribuinte com ID '{id_remover}' não encontrado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID.")

#Menu Principal da Aplicação
def main():
#Função principal que gerencia o menu de interação com o usuário.
    while True:
        print("\n--- Menu Principal do Sistema de Cadastro de Cães Comunitários ---")
        print("1. Cadastrar contribuinte")
        print("2. Consultar contribuinte")
        print("3. Remover contribuinte")
        print("4. Sair")
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == '1':
            cadastrar_contribuinte()
        elif opcao_menu == '2':
            consultar_contribuinte()
        elif opcao_menu == '3':
            remover_contribuinte()
        elif opcao_menu == '4':
            print("Obrigado por usar o Sistema de Cadastro de Contribuintes! Até mais.")
            break # Sai do loop principal e encerra o programa
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

main()