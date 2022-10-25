# coletando dados do usuario
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2 # formula para calcular o imc

# saldo de dados
print("-" * 30)
print("OS DADOS COLETADOS FORAM:")
print("NOME",nome)
print("IDADE",idade,"anos")
print("ALTURA",altura,"cm")
print("PESO",peso, "Kg")
print("IMC: ", imc)
print("-" * 30)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5: 
    print("Magreza leve")
elif imc < 25: 
    print("Saudavel")
elif imc < 30: 
    print("Sobrepeso")
elif imc < 35: 
    print("Obesidade grau I")
elif imc < 40: 
    print("Obesidade grau II")
else: 
    print("Obesidade grau III")

print("-" * 30)   