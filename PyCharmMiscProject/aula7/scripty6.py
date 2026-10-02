nomevend = input("Digite o sue nome: ")
quant_prod_vendido = float(input("Digite a quantidade de produtos vendidos: "))
vlt = float(input("Digite o valor total das vendas: "))
salario_base = 1800
comissao = 150*quant_prod_vendido
#valor_total_vendas = salario_base+comissao+ (*0.03)

salariofinal = (salario_base+comissao+(vlt*0.03))

print(nomevend)
print(quant_prod_vendido)
print(salariofinal)