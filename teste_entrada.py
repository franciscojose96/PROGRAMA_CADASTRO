#Importar biblioteca para criação da janela.
import customtkinter

#Criar janela
janela = customtkinter.CTk()
janela.geometry("500x300") #Tamanho da janela
janela.title("Cadastro de produtos") #Nome do programana.

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

def tela_de_cadastro():
    # Criar janela para cadastro
    tela_cadastro = customtkinter.CTkToplevel()
    tela_cadastro.title('Cadastrar novo usuário')
    tela_cadastro.geometry('500x300')

    # Informações da janela de cadastro
    label_usuario = customtkinter.CTkLabel(tela_cadastro, text="Cadastre-se")
    label_usuario.pack(padx=10, pady=10) # Tamanho do texto

    entrada_email = customtkinter.CTkEntry(tela_cadastro, placeholder_text='Digite seu e-mail')
    entrada_email.pack(padx=10, pady=10) # Tamanho do texto

    entrada_senha = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Digite sua senha", show="*")
    entrada_senha.pack(padx=10, pady=10)

    def finalizar_cadastro():
        novo_email = entrada_email.get()
        nova_senha = entrada_senha.get()

        # Aqui você pode adicionar a lógica para salvar as informações no arquivo 'banco_de_dados.TXT'

        print("Cadastro finalizado com sucesso!")

    botao_finalizar = customtkinter.CTkButton(tela_cadastro, text="Finalizar", command=finalizar_cadastro)
    botao_finalizar.pack(padx=10, pady=10)



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