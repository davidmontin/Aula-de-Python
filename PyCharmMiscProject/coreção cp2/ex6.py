faturamento = 0
while True:

    print("---------- MENU ----------")
    print("1 - Registrar nova venda")
    print("2 - Fechar o caixa")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("-- Registrar nova venda --")
        qtd = int(input("Digite a quantidade de itens diferentes: "))
        preco = float(input("Digite o preço do item R$: "))

        subtotal = qtd * preco

        if subtotal > 500:
            desconto = subtotal * 0.15
        else:
            desconto = subtotal * 0.05

        total_venda = subtotal - desconto
        faturamento += total_venda

        print(f"subtotal: R$ {subtotal:.2f}")
        print(f"desconto: R$ {desconto:.2f}")




        print(f"total venda: R$ {total_venda:.2f}")
    elif opcao == "2":
        print("opção invalida, digite 1 ou 2")
