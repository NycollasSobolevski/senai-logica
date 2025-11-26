# Condicionais e LOOPS


# 1- Condicionais

# EXEMPLO AND
# Quando eu preciso fazer um pure de batatas, eu preciso
# descascar batatas e para isso eu preciso de Batata E Faca

# batata = True
# faca = False 

# if batata == True and faca == True:
#     print("E possivel fazer um pure!!")
# else: 
#     print("Não é possivel fazer um pure!")

# EXEMPLO OR
# eu preciso comprar batatas, e preciso ter qualquer meio
# de pagamento (debito, credito, pix, dinheiro)

# dinheiro = True
# credito = False
# pix = True
# debito = True

# if dinheiro == True or credito == True or pix == True or debito == True:
#     print("É possivel comprar batatas")
# else: 
#     print("nao tenho nenhum meio de pagar as batatas!")


# numero_secreto = 42

# palpite = input("Insira seu palpite: ")
# if palpite.isdigit():
#     if int(palpite) == numero_secreto: # "42" == 42
#         print("Acertou na mosca!")
#     else: 
#         print("Errou o numero!")

# else: 
#     print("O palpite é um numero invalido! ")


# ano = int(input("Insira o ano que nasceu: "))
# idade = 2025 - ano
# print(f"Idade: {idade} anos")
# if idade < 16: 
#     print("Não é permitido votar, pois a pessoa é mais nova!")
# elif idade >= 16 and idade < 18:
#     print("o voto é facultativo")
# elif idade < 70:
#     print("o voto é obrigatório")
# else: 
#     print("O voto é facultativo pois a pessoa é idosa!")


# a = 0

# while a <= 5:
#     print(a)
#     a = a + 1


# contador = 0

# while contador <= 20: 
#     print(contador)
#     contador += 2


# contador = 0
# soma = 0

# final = int(input("insira o limite maximo: "))

# while contador <= final: 
#     print(f"+ {contador}",end=" ")
#     soma += contador
#     contador += 1

# print(f"= {soma}")


# atividade entrega while: 

# para a atividade de hoje, faça igual a atividade de dicionários, porem com while. Ou seja, primeiramente pergunte quantos alunos o usuário quer inserir no dicionário, em seguida peça os seus dados. por fim mostre o dicionário e as medias dos respectivos alunos:
# Solucao de aluno
# alunos = {}

# quantidade = int(input("Insira a quantidade de alunos: "))
# index = 0

# while index < quantidade: # enquanto index for menor que a quantidade de alunos
#     nome = input(f"Insira o nome do {index + 1}° aluno: ").title()
#     # notas = input("Insira as notas separadas por ' ': ").split(' ')
#     notas = []
#     notas.append(int(input("Insira a Primeira nota: ")))
#     notas.append(int(input("Insira a Segunda nota: ")))
#     notas.append(int(input("Insira a Terceira nota: ")))

#     alunos[nome] = notas

#     index += 1

# lista = list(alunos.items()) # [('nycollas', [1,2,3]), ('joaosinho', [3,2,1])]
# index = 0
# while index < len(lista):
#     aluno, notas = lista[index] 
#     soma = 0
#     j = 0
#     while j < len(notas):
#         soma += notas[j]
#         media = soma / len(notas)
#         print(f'{aluno}: {media:.2f}')
#         index += 1
    
import math


alunos = {}
nomes = []
quantidade = int(input("Insira a quantidade de alunos: "))
index = 0

while index < quantidade: # enquanto index for menor que a quantidade de alunos
    nome = input(f"Insira o nome do {index + 1}° aluno: ").title()

    notas = []
    notas.append(int(input("Insira a Primeira nota: ")))
    notas.append(int(input("Insira a Segunda nota: ")))
    notas.append(int(input("Insira a Terceira nota: ")))

    alunos[nome] = notas
    nomes.append(nome)

    index += 1

index = 0
while index < quantidade: 
    aluno = nomes[index]
    media = sum(alunos[aluno]) / len(alunos[aluno])
    print(f'{aluno}: {media}')
    index += 1