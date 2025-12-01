# Aula 05 - Manipulação de Strings

1. Método Split
2. Método Join 
3. Fatiamento de Strings
4. Maiúscula / Minúscula
5. Atividades


## Método Split

Em python quando queremos desmembrar um texto em várias partes, podemos utilizar o método **split** para fazer isso. Este método transforma uma **string** em uma **lista de strings**, ou seja eu consigo tratar do começo do texto até o delimitador, que vai ser o caractér que queremos definir que vai deividir o nosso texto. 
Exemplo:
```python
nome = "Nycollas Wenndy"
lista = nome.split(" ")
print(lista)
# ['Nycollas', 'Wenndy']
```

## Método Join

O método join, faz o contrário do método split, ou seja, invés de ele dividir o texto, ele vai juntar o texto, podendo ser com um deplimitador padrão com base em uma lista. Podendo ser da seguinte forma:

```python
lista = ['Nycollas', 'Wenndy']
nome_completo = ' '.join(lista)
print(nome_completo)
# Nycollas Wenndy
```

Assim eu tambem posso definir qualquer outro delimitador, como '-' por exemplo:

```python
lista = ['Nycollas', 'Wenndy']
nome_completo = '-'.join(lista)
print(nome_completo)
# Nycollas-Wenndy
```


## Fatiamento de Strings

O fatiamento de strings, serve para quando eu preciso retirar uma parte precisa do texto, literalmente cortar em um ponto específico. Ou seja, se eu tenho a palavra 'banana' eu posso pegar somente as **duas** primeiras letras **ou** as 4 **ultimas**, para isso eu utilizo da seguinte sintaxe: `texto[começo:fim]`, onde o **texto** é a minha variável ou string feita, **começo** é apartir de onde do texto eu quero que comece e fim é **até** onde eu quero que vá


```python
fruta = 'banana'
comeco = fruta[:2]
print(comeco) # ba

final = fruta[2:]
print(final) # nana

meio = fruta[2:5]
print(meio) # nan
```

# Maiúscula / Minúscula

Quando eu tenho um texto e quero deixar os caractéres em **MAIÚSCULO** podemos utilizar do método `.upper()` e quando queremos deixar **MINÚSCULO** podemos utilizar do méotodo `.lower()`.

```python
nome = 'Nycollas'
print(nome.upper()) # NYCOLLAS
print(nome.lower()) # nycollas
```

isto pode servir até para tratamento de texto pra podemos fazer comparações, por exemplo:

```python
nome = 'NycOllas'
if(nome == "nycollas") 
# falso
if(nome.lower() == "nycollas") 
# verdadeiro
```