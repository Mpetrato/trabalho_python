print('Bem-Vindo ao Controle de Estoque da Mercearia do Matheus Petrato Rocha') # Identificador pessoal

codigo = 0 
lista_de_produtos = [] # listagem com todos os produtos

def contador(codigo): # Função para formatar o codigo 
    if(codigo < 10):
        return '00{}'.format(codigo)
    elif(codigo < 100):
        return '0{}'.format(codigo)
    else:
        return '{}'.format(codigo)

def cadastrar_produto(codigo): # Função para cadastro de produtos
    while True:
        try: 
            print('Você selecionou a opção de Cadastrar Produto')
            print('Código do Produto {}'.format(contador(codigo)))
            nome_do_produto = input('Por favor entre com o NOME do Produto: ')
            fabricante_do_produto = input('Por favor entre com o FABRICANTE do Produto: ')
            valor_do_produto = float(input('Por favor entre com o VALOR(R$) do Produto: '))

            dicionario_produto = {  'codigo': codigo,
                                    'nome': nome_do_produto,
                                    'fabricante': fabricante_do_produto,
                                    'valor': valor_do_produto } # Adicionando produto ao dicionario
            
            lista_de_produtos.append(dicionario_produto.copy()) # adicionando dicionario a lista
            break
        except: # tratamento de erro
            print('Pare de digitar valores não númericos')

def consultar_produto(): # Função para consulta de produtos já cadastrados
    while True:
        try:
            print('Você selecionou a opção de Consultar Produto')
            print(  'Escolha a opção desejada : \n'
                    '1- Consultar Todos os Produtos \n'
                    '2- Consultar Produtos por Código \n'
                    '3- Consultar Produtos por Fabricante \n'
                    '4- Retornar'
                    )
            opcao = int(input('>> '))


            if(opcao == 1): # Consulta todos os produtos 
                print('-' * 20)
                for produto in lista_de_produtos:
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                print('-' * 20)

            elif(opcao == 2): # Consulta os produtos por código
                entrada = int(input('Digite o código do produto: '))
                for produto in lista_de_produtos:
                    if(produto['codigo'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))

            elif(opcao == 3): # Consulta os produtos por fabricante
                entrada = input('Digite o fabricante do produto: ')
                for produto in lista_de_produtos:
                    if(produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))

            elif(opcao == 4): # Sair do menu
                break

            else: 
                print('Digite uma opção válida')
                continue
        except: # Tratamento de erros
            print()

def remover_produto(): # Função para remover produtos
    print('Você selecionou a opção de Remover Produto')
    entrada = int(input('Digite o codigo do produto a ser removido: '))
    for produto in lista_de_produtos:
        if(produto['codigo'] == entrada):
            lista_de_produtos.remove(produto)

while True: # Laço de repetição para o menu principal
    try:    
        print(  'Escolha a opção desejada: \n'
                '1- Cadastrar Produto \n'
                '2- Consultar Produto(s) \n'
                '3- Remover Produto \n'
                '4- Sair \n'
                )
        opcao = int(input('>> '))


        if(opcao == 1):
            codigo += 1
            cadastrar_produto(codigo)
        elif(opcao == 2):
            consultar_produto()
        elif(opcao == 3):
            remover_produto()
        elif(opcao == 4):
            print('Finalizando aplicação')
            break
        else:
            print('Opção invalida')
            continue
    except:
        print('Digite um valor númerico')
