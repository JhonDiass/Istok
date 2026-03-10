produtos_Cadastrados = [
    {"nome": "arroz", "codigo": 7896006711117, "valor": 3.89, "quantidade": 15},
    {"nome": "feijao", "codigo": 7898994011187 , "valor": 6.90, "quantidade": 10},
    {"nome": "macarrao", "codigo": 7896022200213 , "valor": 3.49, "quantidade": 19},
    {"nome": "leite", "codigo": 7896256600223 , "valor": 3.49, "quantidade": 24}
]
codigos_verificados = []
print("Olá! Bem vindo ao seu Istok!")

# funcoes 

def calcular_Total():
    total_Itens = 0
    
    # percorrendo a lista de produtos cadastrados.
    for produto in produtos_Cadastrados: 
        # Realizando a soma da quantidade dos itens.
        total_Itens += produto["quantidade"] 
    print(f"O total de itens no seu estoque atualmente é de: {total_Itens} itens.") 
    
def atualizar_Lista_Codigos():
    # Atualizando a lista de codigos com os produtos cadastrados.
    for produto in produtos_Cadastrados:
        codigos_verificados.append(produto["codigo"])

def verifica_Codigo(codigo):
    # Retorna True se o código NAO estiver utilizado.
    return codigo not in codigos_verificados
def solicitar_Codigo():
    while True:
        
        try: 
            c = int(input("Digite o código de barras deste produto: "))
        except ValueError:
            print("Por favor, digite apenas números")
            continue
        if verifica_Codigo(c):
            return c
        else:
            print("Este código já está em uso! Verifique e digite novamente.")

def validar_Valor(valor):
    # Retorna True se o valor for maior que zero.
    return valor > 0
def solicitar_Valor():
    # Solicita ao usuário um valor.
    while True:
        try:
            v = float(input("Digite agora o valor deste produto: ").replace(",", "."))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue
        if validar_Valor(v):
            return v
        print("Valor inválido! Verifique e digite novamente.")

def validar_Quantidade(quantidade):
    # Retornará True se a quantidade for maior ou igual a zero.
    return quantidade >= 0
def solicitar_Quantidade():
    # Solicitando ao usuário a quantidade do produto.
    while True:
        try:
            q = int(input("Digite, por fim, a quantidade deste produto: "))
        except ValueError:
            # Caso o usuário digite algo que nao seja um numero, o programa emitirá um aviso e repetirá a pergunta.
            print("Por favor, digite apenas números.")
            # O comando continue faz com que o loop se repita, voltando para o início do while, sem executar o restante do código abaixo.
            continue
        if validar_Quantidade(q):
            return q

def cadastrar_Produto():

    atualizar_Lista_Codigos()

    # Nome do produto a ser adicionado.
    nome = str(input("Digite o nome do produto que deseja adicionar: "))
    codigo = solicitar_Codigo()
    valor = solicitar_Valor()
    quantidade = solicitar_Quantidade()

    # Transforma as informacoes em dicionario
    produto = {"nome": nome, "codigo": codigo , "valor": valor, "quantidade": quantidade}

    # Adiciona o produto recem criado à lista de produtos cadastrados.
    produtos_Cadastrados.append(produto)

    print("Produto cadastrado com sucesso!")

    # Limpa a lista de verificacao do código após o cadastro realizado, evitando duplicatas de códigos em futuras verificações.
    codigos_verificados.clear()

def exibir_Itens():
    
    # Percorrendo os itens cadastrados.
    for produto in produtos_Cadastrados:
        # Criando uma mensagem formatada adicionando a chave do dicionario correspondente a informacao a ser exibida.
        mensagem = f"""Nome: {produto["nome"]};
Código: {produto["codigo"]};
Valor: R$ {produto["valor"]:.2f}:
Quantidade: {produto["quantidade"]}.

==========================
"""
        print(mensagem)

def exibir_Menu():

    while True:
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
                break
            case _:
                print("Digite um dos valores correspondentes ao que deseja!")

exibir_Menu()
input("Pressione Enter para finalizar")