print("Indique os níveis dos jogadores:")

play=int(input("A:"))
play2=int(input("B:"))
play3=int(input("C:"))
play4=int(input("D:"))

dupla1=play+play4
dupla2=play2+play3
if play<play2 and  play<play3 and play<play4 and play4>play3 and play4>play2:
    diferenca=dupla1-dupla2
    print(f"A menor diferença é: {diferenca}")
elif play>=play2 and play<play3 and play<play4 and play4>play3 and play4>play2:
    diferenca=dupla1-dupla2
    print(f"A menor diferença é: {diferenca}")
else:
    diferenca=dupla1-dupla2
    print(f"A menor diferença é: {diferenca}")