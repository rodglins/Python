num1 = int (input("Digite um número: "))
num2 = int (input("Digite outro número: "))

mmc = num1 if num1 > num2 else num2
while mmc % num1 != 0 or mmc % num2 != 0:
    mmc += 1

print("O MMC é: ", mmc,)