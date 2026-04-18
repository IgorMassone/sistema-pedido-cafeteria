def receber_dados():
    nome = input("Digite o nome do cliente: ")
    tipoBebida = input("Digite o tipo de bebida: ")
    tamanhoBebida = input("Digite o tamanho da bebida: ")
    quantidade = int(input("Digite a quantidade: "))
    verificaAluno = input("É aluno da FIAP: ").lower()

    return nome, tipoBebida, tamanhoBebida, quantidade, verificaAluno