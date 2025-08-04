print("Critério A = R$0,25 + R$7,50 fixo")
print("Critério B = R$0,50 + R$2,50 fixo")

x=int(input("Digite a quantidade de livros:"))

soma1=x*(0.25)+7.50
soma2=x*(0.5)+2.5

if x>20:
    print(f"Critério A. R${soma1}")
elif x==20:
    print("Tanto faz.")
else:
    print(f"Critério B. R${soma2}")