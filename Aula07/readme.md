# Aula 07 - Condicionais e Loops

## Condicionais

Quando queremos executar um conjunto de instruções com base numa condição, ou seja, se algo for verdadeiro, execute isso, senão aquilo. Para isso podemos utilizar 

### Condicional IF

A estrutura condicional `if` irá verificar se uma condição é verdadeira, se ela for, ele executa o bloco de instruções dentro dela. Ou seja, para que a condição seja verdadeira, tem que resultar em True. 

Para podermos definir as condições, podemos utilizar a seguinte tabela com os operadores lógicos

| operador  | Definição          | Exemplo                           |
|---------- |--------------------|-----------------------------------|
|    >      | Maior que          | `A > B` # A maior que B           |
|    >=     | Maior ou igual que | `A >= B` # A Maior ou igual que B |
|    <      | menor que          | `A < B` # A menor que B           |
|    <=     | menor ou igual que | `A <= B` # A menor ou igual que B |
|    ==     | Igual a            | `A == B` # A é igual à B          |
|    !=     | Diferente de       | `A != B` # A é diferente de B     |

### Exemplo prático
```python

# verificando idade
joao = 18
jose = 20

if joao > jose: 
    print("Joao e mais velho que jose")
elif joao == jose:
    print("Joao tem a mesma idade que jose")
else: 
    print("Joao e mais novo que jose")
    
if joao != jose: 
    print("Joao tem a idade diferente de jose" )


```



