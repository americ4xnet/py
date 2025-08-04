import math

x=int(input("Digite o valor de A:"))
y=int(input("Digite o valor de B:"))
z=int(input("Digite o valor de C:"))

delta=y**2-4*x*z

if delta>0:
    raiz1=(-y+math.sqrt(delta))/(2*x)
    raiz2=(-y-math.sqrt(delta))/(2*x)
    print(f"As raízes reais são: {raiz1} e {raiz2}")
elif delta==0:
    raiz=-y/(2*x)
    print(f"A equação possui uma raíz real: {raiz}")
elif delta<0:
    print("A equação não possui raízes reais.")
