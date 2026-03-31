nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Voce está aprovado.")
elif media >= 5:
    print("Você está de recuperação.")
else:
    print("Você está reprovado.")
