# Aula 06 - Listas

Nesta aula iremos ver mais profundamente o conceito de **listas**, **Tuplas** e **dicionarios**. 

## Listas

Em python podemos consideirar uma lista um conjunto numerável e sequencial de elementos, onde cada elemento é numerado por um **índice** que começa em 0, ou seja, se eu tenho uma lista com três elementos, o terceiro elemento tem o índice 2, pois o primeiro é zero, o segundo é 1 e o terceiro é 2.

```python
alunos = ["nycollas", "Jose", "Jonathan"]
print(alunos[0]) # "nycollas"
print(alunos[1]) # "Jose"
print(alunos[2]) # "Jonathan"
print(alunos[3]) # ERRO! index out of range (ou seja, não tem esse elemento na lista)
```

Se queremos modificar uma lista, mas também ter a cópia da original, precisamos ter condições para que copiemos os valores da lista original, e não copiar de fato a referencia da primeira. Pois se eu copiar a referencia, se eu modifico a segunda, ele modifica a primeira.

Para resolver este problema precisamos dizer que queremos os valores da primeira lista, e não todo o contexto.

A forma mais fácil de **Copiarmos valores de lista** é utilizando o operador `:`, a qual já vimos em texto que iremos definir que queremos a quantidade de itens antes e depois do operador, ou seja, `minha_lista[:]`, se eu não tenho nenhum numero definindo os valores antes e depois, significa que eu quero todos os valores no começo e todos os valores do final.

```python
turma_desenvolvimento = ["nycollas", "Jose", "Jonathan"]
turma_excel = turma_desenvolvimento[:]
```

<img src="./files/image.png" />


## Tupla

A tupla, assim como a lista, é uma estrutura de dados que pode conter vários elementos, definidos por um index. Porém, diferente da lista, os seus valores são imutáveis, ou seja a partir do momento em que ela é definida, não podemos alterar seus valores. a sua forma de acesso é igual a lista, onde utilizamos colchetes com o index dentro.

### Exemplo: 

```python
lista = ["a", "b", "c"]
tupla = ("a", "b", "c")

print(lista[1]) # b
print(tupla[1]) # b

lista[0] = "A"
tupla[0] = "A" # ERRO!!
```

Mas ai levantamos a pergunta, como podemos alterar o valor de uma tupla?

Apesar de não ser recomendado, pois ela é feita para ser imutável, podemos modificar o seu valor, copiando ela mesma a partir de um index. Como segue o exemplo:


```python
tupla = ("a", "b", "c")
# modificando o primeiro valor de "a" para "A"
tupla = ("A",) + tupla[1:]
print(tupla)  # ("A", "b", "c")
```

No código acima, basicamente criamos uma nova tupla `("A",)` e concatenamos ela com a anterior, a partir do primeiro index `tupla[1:]`