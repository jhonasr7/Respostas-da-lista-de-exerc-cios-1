#Questão 9
kg_morango = float(input("Quantos Kg de morango? "))
kg_maca = float(input("Quantos Kg de maçã? "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total = preco_morango + preco_maca
peso_total = kg_morango + kg_maca
desconto = total - total * 0.10

if peso_total > 8 or total > 25:
    total = desconto

print("Valor a pagar: R$", total)


#Questão 10
codigo_correto = 1234

codigo = int(input("Digite o código: "))

if codigo != codigo_correto:
    print("Usuário inválido!")
else:
    senha = int(input("Digite a senha: "))
    
    if senha != 9999:
        print("Senha incorreta! Acesso bloqueado!")
    else:
        print("Senha correta! Acesso permitido!")