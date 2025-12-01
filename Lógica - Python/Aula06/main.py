# desenvolvimento = ["Nycollas", "José", "Jonathan"]
# excel = desenvolvimento[:]
# del(excel[1])

# print(desenvolvimento)
# print(excel)

# #Atividade 01 - insira 10 valores, mostre a quantidade de items e retorne a lista ordenada
# lista = [0,0,0,0,0,0,0,0,0,0]
# lista[0] = int(input("Insira o 01º valor: "))
# lista[1] = int(input("Insira o 02º valor: "))
# lista[2] = int(input("Insira o 03º valor: "))
# lista[3] = int(input("Insira o 04º valor: "))
# lista[4] = int(input("Insira o 05º valor: "))
# lista[5] = int(input("Insira o 06º valor: "))
# lista[6] = int(input("Insira o 07º valor: "))
# lista[7] = int(input("Insira o 08º valor: "))
# lista[8] = int(input("Insira o 09º valor: "))
# lista[9] = int(input("Insira o 10º valor: "))

# print(f"A minha lista tem {len(lista)} valores")
# print(sorted(lista))
# lista.sort()
# print(lista)



# top10 = (
#     "Bezos ",
#     "Gates",
#     "Buffet",
#     "Arnault",
#     "Slim",
#     "ortega",
#     "ellison",
#     "Zuckerberg",
#     "Bloomberg",
#     "Page"
# )
# print("Os 10 mais ricos do mundo são: ", top10)
# print("Os 3 mais ricos do mundo são: ", top10[:3])
# print("O mai rico do mundo é: ", top10[0])



# eng2sp = {
#     "one": "uno",
#     "two": 12,
#     "three": False
# }

# print(eng2sp['two'])


# menu = {
#     "hamburguer": 10,
#     "hotdog": 6.5,
#     "salada": 4,
#     'suco': 4,
#     'refri': 4.5,
#     'agua': 2
# }

# print("Menu FastFood: ", menu)
# comida = input("Digite a comida que deseja: ").lower()
# bebida = input("Digite a bebida que deseja: ").lower()

# valor_total = menu[comida] + menu[bebida]
# print(f"Valor total é de {valor_total} reais")



turma = {}

aluno01 = input("Insira o nome do primeiro aluno: ")

nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a segunda nota: "))
nota03 = float(input("Insira a terceira nota: "))

notas = [nota01, nota02, nota03]

turma[aluno01] = notas

aluno02 = input("Insira o nome do segundo aluno: ")

nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a segunda nota: "))
nota03 = float(input("Insira a terceira nota: "))

notas = [nota01, nota02, nota03]

turma[aluno02] = notas
aluno03 = input("Insira o nome do segundo aluno: ")

nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a segunda nota: "))
nota03 = float(input("Insira a terceira nota: "))

notas = [nota01, nota02, nota03]

turma[aluno03] = notas

print(f"Aluno: {aluno01} - Média: {sum(turma[aluno01])/3}")
print(f"Aluno: {aluno02} - Média: {sum(turma[aluno02])/3}")
print(f"Aluno: {aluno03} - Média: {sum(turma[aluno03])/3}")