#6. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.
texto = input("Digite uma string: ")

contador_vogais = 0

for letra in texto.lower():  
    if letra in 'aeiou':  
        contador_vogais += 1

print(f"A string possui {contador_vogais} vogais.")