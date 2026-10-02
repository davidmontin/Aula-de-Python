contador = 1

# A pergunta é: 1 é menor ou igual a 3? Sim.
while contador <= 3:
    print("O programa travou neste print!")

    # ERRO GRAVE: O contador nunca aumenta.
    # Ele vai valer 1 para sempre, e a condição do while nunca será falsa.
