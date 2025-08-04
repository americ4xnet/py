x=int(input("Digite a posição P(0 ou 1):"))
y=int(input("Digite a posição R(0 ou 1):"))

if x==1 and y==1:
    print("CAMINHO A.")
elif x==1 and y==0:
    print("CAMINHO B.")
else:
    print("CAMINHO C.")

if x>1 or x<0 and y>1 or y<0:
    print("ERRO!!")
