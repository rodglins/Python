n = int(input("Digite um número para calcular o fatorial: "))

i = 1 
n_fat = 1  

while i <= n:
	n_fat = n_fat * i
	i = i + 1

print("%d! = %d" %(n, n_fat))  