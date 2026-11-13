# Neste arquivo serão desenvolvidos o esqueleto do codigo  e as funcionalidades do ApoIA

# A ideia central eh que este programa seja executado em loop e a cada vez que uma entrada for inserida

# Obrigatoriamente o codigo deve ter em si o "CRUD" (create, read, update e delete) e todos os conceitos visto nas aulas de fundamentos da programacao

# Requisitos: 
# Operadores Aritmeticos, Relacionais e Logicos;
# Estruturas Condicionais e de Repeticao;
# Arrays / Matrizes, Strings, Tuplas e Dicionarios;
# Funcoes e Automacao e Manipulacao de Arquivos.

# Funcionalidades Basicas (CRUD)

#Tainá
def criar_aluno():
    pass

#Tainá
def atualizar_aluno():
    pass

#Tainá
def deletar_aluno():
    pass

#Carol
def criar_turma():
    pass


#Carol
def atualizar_turma():
    pass

#Carol
def deletar_turma():
    pass

#mario
def atualizar_usuario():
    pass

#mario
def deletar_usuario():
    pass

#Jorge
def inserir_atividade():
    pass

#Jorge
def adaptar_atividade():
    pass

#Jorge
def revisar_atividade():
    pass


# Sistema de Acesso

#Mario
def menu():
    print(f"Bem-Vindo ao ApoIa\n") 
    print("Digite a opcao desejada ou 0 para sair\n\n")
    print( "="*5)
    print("Exibir o menu completo") 
    print("="*5)
    print(f"1. Cadastrar novo usuario")
    print(f"2. Fazer Login")

    opcao = int(input("digite a opcao desejada: "))



    return opcao
#mario
def criar_usuario():
    pass
#mario
def login():

    print("digite usuario e senha: ")

    user_info = []

    # Ler informacoes do usuario
    for i in range(2):
        user_info.append(i)

    #usuario_input = input("Usuario: ").strip()
    #senha_input = input("Senha: ").strip()


    # Consulta informacoes na lista de usuarios cadastrados
    try:
        with open("lista_usuarios.txt", "r", encoding='utf-8') as arquivo:
            lista = arquivo.read()

        verificador = all(item in lista for item in user_info)

        if verificador:
            print("Login realizado com sucesso!\n")
            return True

        else:
            print("Erro: Usuario ou senha incorretos\n")
            login()

    except FileNotFoundError:
        print("nenhum usuario cadastrado")

   
#todos
def iniciar():

    print(f"="*20)
    print(f"    Bem-Vindo ao ApoIA\n")
    print(f"="*20)

    print(f"Digite a opcao desejada:\n" + "1. Create\n2. Read\n3. Update\n4. Delete") 

    while(funcionalidade != 0):

        match funcionalidade:
            case 1:
                print(f"create")
                #chamar a funcao create

            case 2:
                print(f"read")
                #chamar a funcao read

            case 3:
                print(f"update")
                #chamar a funcao update

            case 4:
                print(f"delete")
                #chamar a funcao delete

    funcionalidade = int(input("digite a opcao desejada: "))


# Inicio da Funcao Principal
#mario
menu()


if menu() == 1:
    criar_usuario()
    
elif menu() == 2:
    login()

if login():
    print(f"Login realizado com sucesso!\n")
    iniciar()

