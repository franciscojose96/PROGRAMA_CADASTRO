''' Essa função é chamada quando o usuario vai cadastrar um novo item no sistema'''
def cadastro_item():
    novo_item = [] #Lista com o novo item
    descricao_item = input('Descrição do produto: ')
    cod_ean = input('Código de barras: ')
    qtd_cx = input('Quantidade da caixa: ')
    '''Adicionando os as informações dentro de uma lista'''
    novo_item.append(descricao_item)
    novo_item.append(cod_ean)
    novo_item.append(qtd_cx)
    
    return novo_item

novo_produto = cadastro_item()
print(novo_produto)
