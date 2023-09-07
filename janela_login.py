#Importar biblioteca para criação da janela.
import customtkinter

#Criar janela
janela = customtkinter.CTk()
janela.geometry("500x300") #Tamanho da janela
janela.title("Cadastro de produtos") #Nome do programana.

#Essas variaveis são globais, podem ser chamadas dentro da função.
entrada_email = None
entrada_senha = None

'''Essa função roda dentro da DEF Cadastrar Usuario. Ela é responsavél por verificar se já existe um usuario
o login que está sendo cadastrado.'''

def validar_usuario(nome_usuario): #A função recebe o parametro novo usuario, que vem 
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
def cadastrar_usuario(user, passw):
    while True:
        novo_usuario = user
        
        if validar_usuario(novo_usuario):
            print('E-mail já cadastrado! informe um novo e-mail.')
        else:
            break
    
    '''# SE A FUNÇÃO RETORNAR "FALSE", O CODIGO PULA PARA O INPUT DE CRIAR SENHA.'''
    senha = passw

    with open('banco_de_dados.TXT', 'a') as arquivo:
        arquivo.write(novo_usuario +  ',' +  senha +'\n')
    print('Usuario cadastrado!')
entrada_senha = ''
entrada_email = ''

def finalizar_cadastro():
    #novo_email = entrada_email.get()
    #nova_senha = entrada_senha.get()
    #cadastrar_usuario(novo_email, nova_senha)
    print(entrada_senha.get(), entrada_email.get())

def tela_de_cadastro():
    #Criar janela para cadastro
    tela_cadastro = customtkinter.CTkToplevel() #Cria um nova janela para o cadastro
    tela_cadastro.title('Cadastrar novo usuario') #Titulo da janela
    tela_cadastro.geometry('500x300') #dimenções da janela

    #informações da janela de cadastro
    titulo_tela_cadastro = customtkinter.CTkLabel(tela_cadastro, text="Cadastre-se")
    titulo_tela_cadastro.pack(padx=10, pady=10) #tamanho do texto

    entrada_email = customtkinter.CTkEntry(tela_cadastro, placeholder_text='Digite seu e-mail')
    entrada_email.pack(padx=10, pady=10)#tamanho do texto

    entrada_senha = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Digite sua senha", show="*")
    entrada_senha.pack (padx=10, pady=10)

    botao = customtkinter.CTkButton(tela_cadastro, text="Finalizar", command=finalizar_cadastro)
    botao.pack(padx=10, pady=10)

    

#função de clique
def clique():
    print ("Login realizado com sucesso")

#informações que irão aparecer na janela.
texto = customtkinter.CTkLabel(janela, text="Faça seu login")
texto.pack(padx=10, pady=10) #tamanho do texto

#campo para credenciais
email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack (padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack (padx=10, pady=10)

#Adicionar botão de função.
botao = customtkinter.CTkButton(janela, text="Fazer Login", command=clique)
botao.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Cadastre-se", command=tela_de_cadastro)
botao.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack (padx=10, pady=10)

janela.mainloop() #Faz com  que a janela permanece aberta.