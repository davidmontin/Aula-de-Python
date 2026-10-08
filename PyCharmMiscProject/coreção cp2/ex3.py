soma: 0
qtd: 0

while True:
    numero = int(input("Diigite um numero: "))

    if numero == 0:
        break

    elif numero > 0:
        somar = soma + numero
        qts = qts + 1

    else:
        print("numero invalido")


print(f"Somatório dos numeros: {soma}")

media = soma / qts
print(f"media: {media:.2f}")