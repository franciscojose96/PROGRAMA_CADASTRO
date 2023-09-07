def validar_usuario():
    # Abre o arquivo para leitura e verifica se o usuário já existe
     with open('usuarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            usuario, nova_senha = linha.strip().split(',')

            # Verifica se o usuário já existe
            novo_usuario = input('Digite um usuário: ')
            while novo_usuario == usuario:
                print('O login já possui cadastro')
            novo_usuario = input('Digite um usuário: ')
                
                # Sai da função se o usuário já existe

# Função para cadastrar usuário.
def cadastrar_usuario():
    novo_usuario = input('Digite um usuário: ')       
    # Se o usuário não existe, pede uma senha e adiciona ao arquivo
    nova_senha = input('Digite uma senha: ')
    with open('usuarios.txt', 'a') as usuarios:
        usuarios.write(novo_usuario + ',' + nova_senha + '\n')
    print('Usuário cadastrado!')
    return novo_usuario

# Chamando a função de cadastro

cadastrar_usuario()
validar_usuario()


# Abre o arquivo 'usuarios.txt' para leitura e exibe seus conteúdos

