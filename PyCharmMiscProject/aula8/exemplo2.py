total_economizado = 0
mes = 1

while mes <= 3:
    valor_digitado = float(input(f"Quanto você guardou no mês {mes}? R$ "))

    total_economizado = total_economizado + valor_digitado

    mes = mes + 1

print("---")
print("Parabéns! No total, você guardou R$", total_economizado)
