maior_idade = 0
maiores = 0
menores = 0

for i in range(1,11):
    while True:
        idade = int(input(f"Digite a idade do cliente[{i}]: "))
        if idade >= 0:
            break
        else:
            print("a idade não pode ser negativa")

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

    if idade> maior_idade:
        maior_idade = idade
        cliente = i

        print(f"Clientes com 18 anos ou mais: {maiores}")
        print(f"Cliente com menos de 18 anos: {menores}")
        print(f"Cliente mais velho: Cliente [{cliente}] com {maior_idade} anos")
