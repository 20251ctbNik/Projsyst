# __________ CEBEÇALHO ________________________________
# Alunos: Nickolas Kinceski, Gabriele Martins e Nathaly Ananias
# Data de conclusão: 04/03/2026
# Descrição: Um sistema de impréstimos, com sistema de Login, Registro,
# Solicitação de Impréstimo e Cadastro de itens.

# PARTE DO NICKOLAS ----------------------------------------

import getpass

# Contas pré-cadastradas (para teste) (incluindo uma pro senhor, professor)
contas = {
    "Nathaly": "4215", 
    "Gabi": "Caleb",
    "Niko": "Ni",
    "Profe_Berssa": "Berssa123"
}
# ---------------------------------------------------------------------------

#PARTE GABRIELE ---------------------------------------------------------------------------

# Itens já adicionados
estoque_materiais = [
    {"nome": "Estojo Completo", "produto": "101", "status": "Disponível"},
    {"nome": "Calculadora Científica", "produto": "102", "status": "Disponível"},
    {"nome": "Régua 30cm", "produto": "103", "status": "Disponível"},
    {"nome": "Dicionário de Inglês", "produto": "104", "status": "Disponível"}
]
# ---------------------------------------------------------------------------------------------------

#Parte do Nickolas ----------------------------------------------------------------------------
# ===== FUNÇÃO MAIN/PRINCIPAL =====

def main():
    print("\nBem-vindo ao sistema ImprestaAí IFPR!\n")

    while True:
        choice = menu_inicial()

        if choice == "1":
            if login():
                while True:
                    sub_choice = menu_gerenciar()
                    if sub_choice == "1":
                        cadastrar_item()
                    elif sub_choice == "2":
                        solicitar_emprestimo()
                    elif sub_choice == "3":
                        listar_estoque()
                    elif sub_choice == "4":
                        print("Fazendo logout...")
                        break
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.\n")

# ===== FUNÇÕES DE MENU =====

def menu_inicial():
    print("\n--- MENU INICIAL ---")
    print("1. Login")
    print("2. Registrar")
    print("3. Sair")
    return input("Escolha uma opção (1, 2 ou 3): ")


def menu_gerenciar():
    print("\n--- GERENCIAR MATERIAIS ---")
    print("1. Cadastrar Novo Item")
    print("2. Solicitar Empréstimo")
    print("3. Ver Lista de Itens")
    print("4. Logout")
    return input("Escolha: ")


# ===== FUNÇÕES DE LOGIN E REGISTRO =====

# Função de fazer login
def login():
    while True:
        username = input("Digite seu nome de usuário: ")
        try:
            password = getpass.getpass("Digite sua senha: ")
        except Exception:
            password = input("Digite sua senha: ")

        if username in contas and contas[username] == password:
            print(f"\nBem-vindo, {username}!")
            return True
        else:
            print(f"Credenciais inválidas. Digite 1 para tentar novamente ou digite 2 para sair.")
            choice = input("Escolha uma opção: ")
            if choice == "1":
                continue
            elif choice == "2":
                print("\nSaindo do programa.")
                return False
            else:
                print("\nOpção inválida. Saindo do programa.")
                return False

# Função de registrar um novo usuário
def register_user():
    while True:
        new_username = input("Escolha um nome de usuário: ")
        if not new_username:
            print("Nome de usuário não pode ficar vazio.")
            continue
        if new_username in contas:
            print("Usuário já existe. Escolha outro nome.")
            continue
        try:
            new_password = getpass.getpass("Escolha uma senha: ")
            confirm = getpass.getpass("Confirme a senha: ")
        except Exception:
            new_password = input("Escolha uma senha: ")
            confirm = input("Confirme a senha: ")

        if new_password != confirm:
            print("As senhas não conferem. Tente novamente.")
            continue
        contas[new_username] = new_password
        print(f"Usuário {new_username} registrado com sucesso!")
        break
# --------------------------------------------------------------------------------------

# PARTE DA GABI -------------------------------------------------------------------
# Funçao de cadastrar um item
def cadastrar_item():
    print("\n" + "="*10 + " NOVO CADASTRO " + "="*10)
    nome = input("Nome do material escolar: ")
    produto = input("Número de ID (escolha um de sua preferência): ")
    
    # Verifica duplicidade
    for item in estoque_materiais:
        if item['produto'] == produto:
            print("\n❌ ERRO: Este produto já está cadastrado!")
            return

    novo_item = {
        "nome": nome,
        "produto": produto,
        "status": "Disponível"
    }

    estoque_materiais.append(novo_item)
    print(f"\n✅ Item '{nome}' cadastrado com sucesso!")
# -------------------------------------------------------------------------

# PARTE DA NATHALY ---------------------------------------------------------------------

# Função de solicitar um empréstimo
def solicitar_emprestimo():
    print("\n" + "="*10 + " SOLICITAR EMPRÉSTIMO " + "="*10)
    cod = input("Digite o ID do material: ")
    
    for item in estoque_materiais:
        if item['produto'] == cod:
            if item['status'] == "Disponível":
                item['status'] = "Emprestado"
                print(f"✅ Sucesso! O item '{item['nome']}' foi emprestado.")
                return
            else:
                print(f"❌ O item '{item['nome']}' já está emprestado.")
                return
    print("❌ Item não encontrado no sistema.")

# Função para listar o estoque
def listar_estoque():
    print("\n" + "-"*10 + " MATERIAIS NO SISTEMA " + "-"*10)
    if not estoque_materiais:
        print("Estoque vazio.")
    for i in estoque_materiais:
        print(f"ID: {i['produto']} | Item: {i['nome']} | Status: {i['status']}")

if __name__ == "__main__":
    main()
# -------------------------------------------------------------------------------------------