usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    email = input("Digite o email: ").strip()
    idade = input("Digite a idade: ").strip()

    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }

    usuarios.append(usuario)
    print("✅ Usuário cadastrado com sucesso!\n")


def listar_usuarios():
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado.\n")
        return

    print("\n📋 Lista de usuários:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i} - Nome: {usuario['nome']}, "
              f"Email: {usuario['email']}, "
              f"Idade: {usuario['idade']}")
    print()


def menu():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.\n")


if __name__ == "__main__":
    menu()