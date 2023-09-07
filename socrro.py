'''FUNÇÃO DE VALIDAÇÃO. ESSA É CRIADA PARA TRANSFORMAR O BD (ARQUVO TXT) EM UMA LISTA E COMPARAR SE O INPUT DO USUARIO JÁ EXISTE DENTRO DO DB.
CASO JÁ EXISTA UM USUARIO COM AQUELE LOGIN A FUNÇÃO RETORNA "TRUE" E ENVIA PARA O CADASTRO SOLICITAR UM NOVO INPUT.'''
def validar_usuario(nome_usuario):
    with open('usuarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

            #Tratando a lista criada acima.
        for linha in linhas:
            usuario, _ = linha.strip().split(',')
            
            #Se o novo usuario for igual ao novo usuario retorne True para ser tratado dentro da função cadastro.
            if nome_usuario == usuario:
                return True  # Retorna True se o usuário já existe

    return False  # Retorna False se o usuário não existe

'''Função para cadastrar usuário.
ENQUANTO A FUNÇÃO VALIDAR USUARIO RETORNAR TRUE A FUNÇAÕ DE CADASTRAR VAI SOLICITAR UM NOVO USUARIO.'''
def cadastrar_usuario():
    while True:
        novo_usuario = input('(CADASTRAR PRINCIPAL) Digite um usuário: ')       

        if validar_usuario(novo_usuario): 
            print('O login já possui cadastro. Escolha outro nome de usuário.')
        else:
            break

    '''# SE A FUNÇÃO RETORNAR "FALSE", O CODIGO PULA PARA O INPUT DE CRIAR SENHA.'''
    nova_senha = input('Digite uma senha: ')

    '''APOS O USUARIO CRIAR SEU LOGIN O CODIGO VAI ADICIONAR AS INFORMAÇÕES DENTRO DO ARQUIVO TXT.'''
    with open('usuarios.txt', 'a') as usuarios:
        usuarios.write(novo_usuario + ',' + nova_senha + '\n')
    print('Usuário cadastrado!')

# Chama a função de cadastro
cadastrar_usuario()

''' Abre o arquivo 'usuarios.txt' para leitura e exibe seus conteúdos
Essa linha de código não é necessaria para cadastro, apenas para criação.'''
with open('usuarios.txt', 'r') as arquivo:
    print(arquivo.read())
