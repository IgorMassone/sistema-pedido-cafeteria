def receber_dados():
    nome = input("Digite o nome do cliente: ")
    tipoBebida = input("Digite o tipo de bebida: ").lower()
    tamanhoBebida = input("Digite o tamanho da bebida: ")
    quantidade = int(input("Digite a quantidade: "))
    verificaAluno = input("É aluno da FIAP: ").lower()

    return nome, tipoBebida, tamanhoBebida, quantidade, verificaAluno

precos = {
    "cafe": {"P": 4.00, "M": 5.50, "G": 7.00},
    "capuccino": {"P": 5.00, "M": 7.50, "G": 9.00},
    "chocolate": {"P": 5.50, "M": 7.00, "G": 8.50}
}