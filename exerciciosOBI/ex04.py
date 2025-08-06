num=int(input("Digite a posição A:"))
num2=int(input("Digite a posição B:"))
num3=int(input("Digite a posição C:"))

dis1=num2-num
dis2=num3-num2

if dis1<dis2:
    print("1")
elif dis1>dis2:
    print("-1")
else:
    print("0")