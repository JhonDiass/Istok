produtos_Cadastrados = [
    {"nome": "arroz", "codigo": 7896006711117, "valor": 3.89, "quantidade": 15},
    {"nome": "feijao", "codigo": 7898994011187 , "valor": 6.90, "quantidade": 10},
    {"nome": "macarrao", "codigo": 7896022200213 , "valor": 3.49, "quantidade": 19},
    {"nome": "leite", "codigo": 7896256600223 , "valor": 3.49, "quantidade": 24}
]

print("Olá! Bem vindo ao seu Istok!")

# funcao calcular 

def calcular_Total():
    total_Itens = []

    # percorrendo a lista de produtos cadastrados.
    for produto in produtos_Cadastrados: 
        
        # Adicionando especificamente a "quantidade" na variavel total_itens.
        total_Itens.append(produto["quantidade"]) 
        
        # Funcao para somar todos os itens da lista total_itens e printando o valor no console.
    print(f"O total de itens no seu estoque atualmente é de: {sum(total_Itens)} itens.") 
    
def cadastrar_Produto():
    
    # Criando uma lista com os codigos existentes.
    codigos_verificados = []
    for produto in produtos_Cadastrados:
        codigos_verificados.append(produto["codigo"])

    # Nome do produto a ser adicionado.
    nome = str(input("Digite o nome do produto que deseja adicionar: "))
    
    # Verificador de código existente
    while True:
        # Codigo do produto a ser adicionado.
        codigo = int(input("Digite agora o código de barras deste produto: "))
        # Caso o codigo NAO for existente, o mesmo será adicionado e o programa continua
        if not codigo in codigos_verificados:
            break
        # Caso o codigo for existente, o loop se repete.
        print("Código inválido ou já está cadastrado!")
    

    # Verificador de valor valido.
    while True:
        # Valor de produtos a ser adicionado
        valor = float(input("Digite agora o valor deste produto: ").replace(",", "."))
        # Se o produto valer mais ou igual a 0 o programa segue.
        if valor > 0:
            break
        # Caso o valor digitado seja invalido o loop se repete.
        print("Valor invalido!")

    # Verificador de quantidade valida
    while True:
        # Quantidade de produtos a ser adicionado
        quantidade = int(input("Digite, por fim, a quantidade deste produto: "))
        # Se o produto for maior ou igual a 0 o mesmo concluira o cadastro.
        if quantidade >= 0:
            break
        # Caso a quantidade digitada seja invalida o loop se repete.
        print("Quantidade invalida!")


    # Transforma as informacoes em dicionario
    produto = {"nome": nome, "codigo": codigo , "valor": valor, "quantidade": quantidade}

    # Adiciona o produto recem criado à lista de produtos cadastrados.
    produtos_Cadastrados.append(produto)

    print("Produto cadastrado com sucesso!")

def exibir_Itens():
    for produtos in produtos_Cadastrados:
        print(produtos, sep='\n')

def exibir_Menu():

    print("O que voce gostaria de fazer?")
    mensagem = """
    [1] - Exibir itens em estoque.
    [2] - Cadastrar novo produto.
    [3] - Exibir quantidade total de itens em estoque.
    
    
    [0] - Fechar programa.
"""
    print(mensagem)
    menu = int(input("Digite aqui o numero desejado: "))
    match menu:
        case 1:
            exibir_Itens()
        case 2:
            cadastrar_Produto()
        case 3:
            calcular_Total()
        case 0: 
            return True
        case _:
            print("Digite um dos valores correspondentes ao que deseja!")

    return False

while True:
    if exibir_Menu():
        break