usuarios = []

def email_ja_existe(email: str) -> bool:
    email = email.strip().lower()
    return any(u["email"].lower() == email for u in usuarios)

def pedir_idade() -> int:
    while True:
        idade_txt = input("Digite a idade: ").strip()
        if idade_txt.isdigit():
            return int(idade_txt)
        print("Idade invalida. Digite apenas numeros.\n")

def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    email = input("Digite o email: ").strip().lower()

    if not nome:
        print("Nome nao pode ser vazio.\n")
        return

    if not email or "@" not in email:
        print("Email invalido.\n")
        return

    if email_ja_existe(email):
        print("Esse email ja esta cadastrado.\n")
        return

    idade = pedir_idade()

    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado.\n")
        return

    print("\nLista de usuarios (total: {})".format(len(usuarios)))
    print("-" * 40)
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i} - Nome: {usuario['nome']} | Email: {usuario['email']} | Idade: {usuario['idade']}")
    print("-" * 40 + "\n")

def menu():
    while True:
        print("1 - Cadastrar usuario")
        print("2 - Listar usuarios")
        print("3 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.\n")

if __name__ == "__main__":
    menu()