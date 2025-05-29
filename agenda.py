def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome}, {telefone} e {email} foi adicionado com sucesso!")

def ver_contatos(contatos):
    print("\nLista de contatos:")
    if not contatos:
        print("Nenhum contato cadastrado.")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] {nome}, {telefone}, {email}")

def atualizar_nome_telefone_email(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado para {novo_nome}, {novo_telefone}, {novo_email}")
    else:
        print("Índice de contato inválido.")

def marcar_como_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito.")
    else:
        print("Índice de contato inválido.")

def deletar_contatos_favoritos(contatos):
    contatos[:] = [contato for contato in contatos if not contato["favorito"]]
    print("Contatos favoritos foram deletados.")

contatos = []
while True:
    print("\nMenu do Gerenciador de Agenda")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar como favorito")
    print("5. Deletar contatos favoritos")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        atualizar_nome_telefone_email(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
        marcar_como_favorito(contatos, indice_contato)

    elif escolha == "5":
        deletar_contatos_favoritos(contatos)
        ver_contatos(contatos)

    elif escolha == "6":
        break

    else:
        print("Opção inválida, tente novamente.")

print("Programa finalizado.")
