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
