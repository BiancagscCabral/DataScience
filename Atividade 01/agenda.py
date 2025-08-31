#Atividade Python - Agenda 

#cadastrar contatos

agenda = []
def cadastrar():
    print("Cadastramento de Contato")
    nome = input ("Digite seu Nome:")
    telefone = input ("Digite seu Telefone:")
    email = input ("Digite seu Email:")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato)
    print("Contato cadastrado com sucesso!")


#listar contatos

def listar():
    if not agenda:
        print("Nenhum contato cadastrado.")
        return
    for i, contato in enumerate(agenda):
         print(f"{i} - {contato['nome']} | {contato['telefone']} | {contato['email']}")
    print("Lista de contatos exibida com sucesso!")


 #atualizar contatos

def atualizar():
    indice = int(input("Digite o número do contato que deseja atualizar: "))
    if 0 <= indice < len(agenda):
        agenda[indice]["nome"] = input("Novo nome: ")
        agenda[indice]["telefone"] = input("Novo telefone: ")
        agenda[indice]["email"] = input("Novo e-mail: ")
        print("Contato atualizado!\n")
    else:
        print("Índice inválido.\n")

#Excluir contatos

def excluir():
    listar()
    indice = int(input("Digite o número do contato que deseja excluir: "))
    if 0 <= indice < len(agenda):
        del agenda[indice]
        print("Contato excluído com sucesso!\n")
    else:
        print("Índice inválido.\n")


        #Menu

while True:
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Atualizar contato")
    print("4 - Excluir contato")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        excluir()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.\n")

