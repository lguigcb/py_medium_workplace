"""
Iterando strings com while
"""
nome = input('Digite o seu nome aqui:')
indice = 0
novo_nome = ''

while (indice < len(nome)):
    letra = nome[indice]
    novo_nome += f'-{letra}'
    indice += 1

print(f'Seu novo nome é: {novo_nome}')