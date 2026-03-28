litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo == "A":
    if litros <= 20:
        preco = litros * 2.90 * 0.97 # 3% de desconto
    else:
        preco = litros * 2.90 * 0.95 # 5% de desconto
elif tipo == "G":
    if litros <= 20:
        preco = litros * 3.30 * 0.96 # 4% de desconto
    else:
        preco = litros * 3.30 * 0.94 # 6% de desconto
print(f"O preco a ser pagar é: R$ {preco:.2f}")