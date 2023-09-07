'''FUNÇÃO DE VALIDAÇÃO. ESSA É CRIADA PARA TRANSFORMAR O BD (ARQUVO TXT) EM UMA LISTA E COMPARAR SE O INPUT DO USUARIO JÁ EXISTE DENTRO DO DB.
CASO JÁ EXISTA UM USUARIO COM AQUELE LOGIN A FUNÇÃO RETORNA "TRUE" E ENVIA PARA O CADASTRO SOLICITAR UM NOVO INPUT.'''
def validar_usuario(nome_usuario):
    with open('banco_de_dados.TXT', 'r') as arquivo:
        lista_usuarios = arquivo.readlines() #transforma o arquivo em uma lista.

            #Tratando a lista criada acima.
        for linha in lista_usuarios: #cada linha corresponde a um usuario, senha.
            usuario, _ = linha.strip().split(',')

            #Se o novo usuario for igual ao novo usuario retorne True para ser tratado dentro da função cadastro.
            if nome_usuario == usuario:
                return True #Se o usuario já estiver cadastrado.
            
    return False #Se o login estiver diponivel para usar. 

'''Função para cadastrar usuário.
ENQUANTO A FUNÇÃO VALIDAR USUARIO RETORNAR TRUE A FUNÇAÕ DE CADASTRAR VAI SOLICITAR UM NOVO USUARIO.'''
def cadastrar_usuario():
    while True:
        novo_usuario = input("Digite seu e-mail: ")
        
        if validar_usuario(novo_usuario):
            print('E-mail já cadastrado! informe um novo e-mail.')
        else:
            break
    
    '''# SE A FUNÇÃO RETORNAR "FALSE", O CODIGO PULA PARA O INPUT DE CRIAR SENHA.'''
    senha = input('Digite uma senha.')

    with open('banco_de_dados.TXT', 'a') as arquivo:
        arquivo.write(novo_usuario +  ',' +  senha +'\n')
    print('Usuario cadastrado!')
    

cadastrar_usuario()

with open ('banco_de_dados.TXT', 'r') as arquivo:
    print(arquivo.read())
