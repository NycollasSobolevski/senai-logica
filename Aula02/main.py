# aula 02 - Manipulação de Strings

# nome_completo = "Nycollas Wenndy Sobolevski"

# lista = nome_completo.split(" ") #['Nycollas', 'Wenndy', 'Sobolevski']

# print("Primeiro nome: " + lista[0])
# print("Sobrenome: " + lista[2])

# email = "nycollassobolevski@yahoo.com.br"
# lista = email.split("@") #['nycollassobolevski', 'gmail.com']
# dominio = lista[1].split('.') #['gmail', 'com']
# print(dominio[0])

# nome_completo = input("Insira seu nome completo: ")
# #nycollas wenndy sobolevski

# lista = nome_completo.split(" ")
# #['nycollas', 'wenndy', 'sobolevski']

# nome_do_email = lista[0] + lista[2]
# #nycollassobolevski

# dominio = "@sesisenaipr.org.br"

# email_institucional = nome_do_email + dominio
# #nycollassobolevski@sesisenaipr.org.br

# print(email_institucional)


# s = 'Python'
# # ['P', 'y', 't', 'h', 'o', 'n']
# print(s[1:4]) # yth

# nome = 'nycollas'
# print(nome[2:6]) # coll

# print(nome[2:]) # collas
# print(nome[:1]) # n


nome = 'nycollas'
print(nome.upper())
nome = 'NYCOLLAS'
print(nome.lower())


# atividade 1 ( 5-10 min) primeira letra maiuscula 
# "nycollas wenndy sobolevski" => "Nycollas Wenndy Sobolevski"
#split, upper, fatiamento