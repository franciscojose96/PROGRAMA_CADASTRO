# Importar biblioteca para criação da janela.
import customtkinter

# Criar janela
janela = customtkinter.CTk()
janela.geometry("500x300") # Tamanho da janela
janela.title("Cadastro de produtos") # Nome do programa.

# Variáveis globais para campos de entrada
entrada_senha = None
entrada_email = None

def validar_usuario(nome_usuario):
    with open('banco_de_dados.TXT', 'r') as arquivo:
        lista_usuarios = arquivo.readlines() # Transforma o arquivo em uma lista.

        # Tratando a lista criada acima.
        for linha in lista_usuarios: # Cada linha corresponde a um usuário, senha.
            usuario, _ = linha.strip().split(',')

            # Se o novo usuário for igual ao novo usuário, retorne True para ser tratado dentro da função de cadastro.
            if nome_usuario == usuario:
                return True # Se o usuário já estiver cadastrado.

    return False # Se o login estiver disponível para usar.

'''Função para cadastrar usuário.
ENQUANTO A FUNÇÃO VALIDAR USUÁRIO RETORNAR TRUE A FUNÇÃO DE CADASTRAR VAI SOLICITAR UM NOVO USUÁRIO.'''
def cadastrar_usuario(user, passw):
    while True:
        novo_usuario = user

        if validar_usuario(novo_usuario):
            print('E-mail já cadastrado! Informe um novo e-mail.')
        else:
            break

    '''# SE A FUNÇÃO RETORNAR "FALSE", O CÓDIGO PULA PARA O INPUT DE CRIAR SENHA.'''
    senha = passw

    with open('banco_de_dados.TXT', 'a') as arquivo:
        arquivo.write(novo_usuario +  ',' +  senha +'\n')
    print('Usuário cadastrado!')

def finalizar_cadastro():
    global entrada_email, entrada_senha
    novo_email = entrada_email.get()
    nova_senha = entrada_senha.get()
    cadastrar_usuario(novo_email, nova_senha)
    print("Cadastro finalizado com sucesso!")

def tela_de_cadastro():
    global entrada_email, entrada_senha
    # Criar janela para cadastro
    tela_cadastro = customtkinter.CTkToplevel() # Cria uma nova janela para o cadastro
    tela_cadastro.title('Cadastrar novo usuário') # Título da janela
    tela_cadastro.geometry('500x300') # Dimensões da janela

    # Informações da janela de cadastro
    titulo_tela_cadastro = customtkinter.CTkLabel(tela_cadastro, text="Cadastre-se")
    titulo_tela_cadastro.pack(padx=10, pady=10) # Tamanho do texto

    entrada_email = customtkinter.CTkEntry(tela_cadastro, placeholder_text='Digite seu e-mail')
    entrada_email.pack(padx=10, pady=10) # Tamanho do texto

    entrada_senha = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Digite sua senha", show="*")
    entrada_senha.pack(padx=10, pady=10)

    botao = customtkinter.CTkButton(tela_cadastro, text="Finalizar", command=finalizar_cadastro)
    botao.pack(padx=10, pady=10)

# Função de clique
def clique():
    print ("Login realizado com sucesso")

# Informações que irão aparecer na janela.
texto = customtkinter.CTkLabel(janela, text="Faça seu login")
texto.pack(padx=10, pady=10) # Tamanho do texto

# Campo para credenciais
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack (padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack (padx=10, pady=10)

# Adicionar botão de função.
botao = customtkinter.CTkButton(janela, text="Fazer Login", command=clique)
botao.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Cadastre-se", command=tela_de_cadastro)
botao.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack (padx=10, pady=10)

janela.mainloop() # Faz com que a janela permaneça aberta.
