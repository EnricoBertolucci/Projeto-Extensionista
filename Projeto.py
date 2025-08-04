from datetime import datetime

# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Cadastro de Contribuintes!")

# Lista que armazenará os contribuintes cadastrados
lista_contribuintes = []

# Variável global para gerar IDs únicos para os contribuintes
id_global = 0

def cadastrar_contribuinte():
    global id_global
    id_global += 1

    nome = input("Digite o nome do contribuinte: ")

    # Validação da data de contribuição
    while True:
        data_input = input("Digite a data da primeira contribuição (formato DD/MM/AAAA): ")
        try:
            primeira_contribuicao = datetime.strptime(data_input, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")

    valor = float(input("Digite o valor contribuído mensalmente (em Reais): "))
    bairro = input("Digite o bairro do contribuinte: ")

    contribuinte = {
        'id': id_global,
        'nome': nome,
        'primeira_contribuicao': primeira_contribuicao.strftime("%d/%m/%Y"),
        'valor': valor,
        'bairro': bairro
    }

    lista_contribuintes.append(contribuinte)
    print(f"Contribuinte '{nome}' (ID: {id_global}) cadastrado com sucesso!\n")

def consultar_contribuinte():
    while True:
        print("\n--- Menu de Consulta ---")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Nome")
        print("4. Retornar ao menu principal")
        opcao_consulta = input("Escolha uma opção: ")

        if opcao_consulta == '1':
            if not lista_contribuintes:
                print("Nenhum contribuinte cadastrado para exibir.")
            else:
                print("\n--- Contribuintes Cadastrados ---")
                for contribuinte in lista_contribuintes:
                    print(f"ID: {contribuinte['id']}")
                    print(f"Nome: {contribuinte['nome']}")
                    print(f"Bairro: {contribuinte['bairro']}")
                    print(f"Primeira contribuição: {contribuinte['primeira_contribuicao']}")
                    print(f"Valor mensal: R$ {contribuinte['valor']:.2f}\n")

        elif opcao_consulta == '2':
            try:
                id_consulta = int(input("Digite o ID do contribuinte: "))
                encontrado = False
                for contribuinte in lista_contribuintes:
                    if contribuinte['id'] == id_consulta:
                        print(f"\n--- Detalhes do Contribuinte (ID: {contribuinte['id']}) ---")
                        print(f"Nome: {contribuinte['nome']}")
                        print(f"Bairro: {contribuinte['bairro']}")
                        print(f"Primeira contribuição: {contribuinte['primeira_contribuicao']}")
                        print(f"Valor mensal: R$ {contribuinte['valor']:.2f}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print(f"Nenhum contribuinte com ID '{id_consulta}' foi encontrado.")
            except ValueError:
                print("Entrada inválida. Digite um número para o ID.")

        elif opcao_consulta == '3':
            nome_busca = input("Digite o nome do contribuinte: ").lower()
            encontrados = [c for c in lista_contribuintes if c['nome'].lower() == nome_busca]
            if encontrados:
                print(f"\n--- Contribuintes Encontrados com o nome '{nome_busca}' ---")
                for contribuinte in encontrados:
                    print(f"ID: {contribuinte['id']}")
                    print(f"Nome: {contribuinte['nome']}")
                    print(f"Bairro: {contribuinte['bairro']}")
                    print(f"Primeira contribuição: {contribuinte['primeira_contribuicao']}")
                    print(f"Valor mensal: R$ {contribuinte['valor']:.2f}\n")
            else:
                print(f"Nenhum contribuinte com o nome '{nome_busca}' foi encontrado.")

        elif opcao_consulta == '4':
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")

def remover_contribuinte():
    if not lista_contribuintes:
        print("Não há contribuintes cadastrados para remover.")
        return

    try:
        id_remover = int(input("Digite o ID do contribuinte que deseja remover: "))
        for i, contribuinte in enumerate(lista_contribuintes):
            if contribuinte['id'] == id_remover:
                nome_removido = lista_contribuintes.pop(i)['nome']
                print(f"Contribuinte '{nome_removido}' (ID: {id_remover}) removido com sucesso!")
                return
        print(f"Contribuinte com ID '{id_remover}' não encontrado.")
    except ValueError:
        print("Entrada inválida. Digite um número para o ID.")

def main():
    while True:
        print("\n--- Menu Principal do Sistema de Cadastro de Contribuintes ---")
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
            print("Obrigado por usar o sistema! Até logo.")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")

# Executar o sistema
main()