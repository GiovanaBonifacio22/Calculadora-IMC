gasolina= float(input("Digite o preço do litro da gasolina: "))
alcool = float(input("Digite o preço do litro do alcool: "))
divisão = alcool/gasolina

if divisão <0.7:
    print("Alcool")
else:
    print("gasolina")