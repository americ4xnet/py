num=int(input("Digite o melhor resultado obtido numa prova de olimpíada:"))
num2=int(input("Digite o recorde mundial para a prova:"))
num3=int(input("Digite o recorde olímpico para a prova:"))

if num>num2 and num<num3:
    print("*")
    print("RO")
elif num<num2 and num<num3:
    print("RM")
    print("RO")
else:
    print("*")
    print("*")