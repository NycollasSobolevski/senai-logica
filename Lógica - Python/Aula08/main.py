#funções 

# def saudacoes(): 
#     print('Hello, world!')
# saudacoes()



# def contagem(init):
#     for i in range(init, 0, -1):
#         print(i)
#         time.sleep(1)

# contagem(5)
# print()
# contagem(3)



# def velocidade(distancia, tempo):
#     vel = distancia / tempo
#     return vel


# vel = velocidade(100,2)
# print(vel)



import math


pessoas = {
    123: {
        'nome':'Nycollas Sobolevski',
        'nascimento': '05/10/2003',
        'telefone': '41 99999-999'
    },
    222: {
        'nome':'João Pereira',
        'nascimento': '10/02/2000',
        'telefone': '41 99888-999'
    },
    333: {
        'nome':'Maria da Silva',
        'nascimento': '14/02/2001',
        'telefone': '41 99999-0000'
    }
}

# def get_usuario_by_matricula(matricula):
#     global pessoas
#     usuario = pessoas[matricula]
#     return usuario

# escolha = int(input("insira a matricula do usuario: "))
# escolhido = get_usuario_by_matricula(escolha)
# # print(f'Nome: {escolhido['nome']}')
# # print(f'Nascimento: {escolhido['nascimento']}')
# # print(f'Fone: {escolhido['telefone']}')
# print(escolhido['nome'])

# print(pessoas)

# print()
# print(pessoas[123]['nome'][:10], pessoas[123]['nascimento'], pessoas[123]['telefone'], sep=' - ')
# print(pessoas[333]['nome'][:10], pessoas[333]['nascimento'], pessoas[333]['telefone'], sep=' - ')
# print()

pontos = [(1,1), (3,1), (1,3)]

def calcular_poligono(coordenadas):
    ABx = abs(coordenadas[0][0] - coordenadas[1][0])
    ACy = abs(coordenadas[0][1] - coordenadas[2][1])
    hipotenusa = math.sqrt((ACy ** 2) + (ABx ** 2))
    area = (ABx * ACy) / 2
    return hipotenusa, area
    


h = calcular_poligono(pontos)
print('Hipotenusa:', h[0])
print('Área:', h[1])

hipotenusa, area = calcular_poligono(pontos)
print('Hipotenusa:', hipotenusa)
print('Área:', area)