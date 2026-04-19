def receber_dados():
    nome = input("Digite o nome do cliente: ")
    tipoBebida = input("Digite o tipo de bebida: ").lower()
    tamanhoBebida = input("Digite o tamanho da bebida: ")
    quantidade = int(input("Digite a quantidade: "))
    verificaAluno = input("É aluno da FIAP: ").lower()

    return nome, tipoBebida, tamanhoBebida, quantidade, verificaAluno

precos = {
    "cafe": {"P": 4.00, "M": 5.50, "G": 7.00},
    "capuccino": {"P": 6.00, "M": 7.50, "G": 9.00},
    "chocolate": {"P": 5.50, "M": 7.00, "G": 8.50}
}

def calcular_preco(tipoBebida, tamanhoBebida, quantidade, verificaAluno):
    preco_unitario = precos[tipoBebida][tamanhoBebida]
    preco_total = preco_unitario * quantidade
    desconto = 0

    if verificaAluno == "sim" and preco_total >= 15:
        desconto = preco_total * 0.10
        preco_total = preco_total - desconto

    if preco_total >= 20:
        print("Produto com brinde")
    
    return preco_total, desconto


nome, tipoBebida, tamanhoBebida, quantidade, verificaAluno = receber_dados()
preco_total, desconto = calcular_preco(tipoBebida, tamanhoBebida, quantidade, verificaAluno)

def mostrar_resultado(nome, tipoBebida, tamanhoBebida, quantidade, preco_total, desconto):
    print("-=-" * 20)
    print(f"Cliente: {nome}")
    print(f"Bebida: {tipoBebida}")
    print(f"Tamanho: {tamanhoBebida}")
    print(f"Quantidade: {quantidade}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total: R$ {preco_total:.2f}")

    if preco_total >= 20:
        print("Pedido com brinde!")
    else:
        print("Pedido sem brinde.")

mostrar_resultado(nome, tipoBebida, tamanhoBebida, quantidade, preco_total, desconto)