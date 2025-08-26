#5. Escreva um programa que leia 5 números e mostre o maior deles.
maior_numero = float('-inf')  

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número é: {maior_numero}")
