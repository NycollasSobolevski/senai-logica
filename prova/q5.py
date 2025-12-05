list = [
    {
        'coluna': 'CP',
        'linha': 4,
        'letra': 'l'
    },
    {
        'coluna': 'CQ',
        'linha': 4,
        'letra': 'z'
    },
    {
        'coluna': 'BC',
        'linha': 4,
        'letra': 'f'
    },
    {
        'coluna': 'CP',
        'linha': 4,
        'letra': 'i'
    },
    {
        'coluna': 'EH',
        'linha': 4,
        'letra': 'a'
    },
    {
        'coluna': 'DF',
        'linha': 4,
        'letra': ' '
    },
    {
        'coluna': 'CN',
        'linha': 4,
        'letra': 'e'
    },
    {
        'coluna': 'EI',
        'linha': 4,
        'letra': 't'
    },
    {
        'coluna': 'DG',
        'linha': 4,
        'letra': 'n'
    },
    {
        'coluna': 'EK',
        'linha': 4,
        'letra': 'l'
    },
    {
        'coluna': 'EJ',
        'linha': 4,
        'letra': 'a'
    },
    {
        'coluna': 'A',
        'linha': 5,
        'letra': '\n'
    },
    {
        'coluna': 'GF',
        'linha': 6,
        'letra': 's'
    },
    {
        'coluna': 'FF',
        'linha': 6,
        'letra': 's'
    },
    {
        'coluna': 'FG',
        'linha': 6,
        'letra': 't'
    },
    {
        'coluna': 'FH',
        'linha': 6,
        'letra': 'a'
    },
    {
        'coluna': 'DG',
        'linha': 6,
        'letra': 'o'
    },
    {
        'coluna': 'EJ',
        'linha': 6,
        'letra': ' '
    },
    {
        'coluna': 'FE',
        'linha': 6,
        'letra': 'e'
    },
    {
        'coluna': 'DF',
        'linha': 6,
        'letra': 'b'
    },
    {
        'coluna': 'EH',
        'linha': 6,
        'letra': 'a'
    },
    {
        'coluna': 'EK',
        'linha': 6,
        'letra': 'f'
    },
    {
        'coluna': 'EI',
        'linha': 6,
        'letra': 's'
    },
    {
        'coluna': '',
        'linha': 7,
        'letra': '!'
    },
]

#organizando uma lista para cada linha

l4 = []
l5 = []
l6 = []
l7 = []

# Adicionando os objetos nas respectivas listas
for i in list:
    if i['linha'] == 4:
        l4.append(i)
    elif i['linha'] == 5:
        l5.append(i)
    else :
        l6.append(i)

l4.sort(key=lambda x: x['coluna'])
l6.sort(key=lambda x: x['coluna'])

#mostrando na tela o valor das a
for i in l4:
    print(i['letra'], end='')
for i in l5:
    print(i['letra'], end='')
for i in l6:
    print(i['letra'], end='')


list.sort(key=lambda x: x['coluna'])
list.sort(key=lambda x: x['linha'])
print('\n\n')
for i in list:
    print(i['letra'], end='')