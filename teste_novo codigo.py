def validar_usuario():
    # Abre o arquivo para leitura e verifica se o usuário já existe
    with open('usuarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        novo_usuario = input('(VALIDAÇÃO) Digite um usuário: ')
        
        for linha in linhas:
            usuario, _ = linha.strip().split(',')
            
            if novo_usuario == usuario:
                print('O login já possui cadastro')

                return False  # Sai da função se o usuário já existe

# Função para cadastrar usuário.
def cadastrar_usuario():
    novo_usuario = input('(CADASTRAR PRINCIPAL)Digite um usuário: ')       
    # Se o usuário não existe, pede uma senha e adiciona ao arquivo
    nova_senha = input('Digite uma senha: ')
    with open('usuarios.txt', 'a') as usuarios:
        usuarios.write(novo_usuario + ',' + nova_senha + '\n')
    print('Usuário cadastrado!')
    return novo_usuario

# Chama a função de validação primeiro para verificar se o usuário já existe
validar_usuario()

# Se o usuário não existir, então permite o cadastro
if not validar_usuario():
    cadastrar_usuario()

# Abre o arquivo 'usuarios.txt' para leitura e exibe seus conteúdos
with open('usuarios.txt', 'r') as arquivo:
    print(arquivo.read())
