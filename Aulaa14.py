#Exercicios AULA14

#Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.
l1 = [1, 2, 3, 4, 5]
result = l1.pop(4)
print(result)

#Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante
l2 = [10, 20, 30, 40, 50]
result2 = l1.pop(2)
print(result2)

#Exercício 3: Crie uma lista e implemente a operação pop().
l3 = [1, 2, 3, 4, 5]
result3 = l3.pop(1)
print(result3)

#Exercício 4: Remova o primeiro elemento de uma lista e o último elemento usando `pop()` e imprima a lista resultante.
list4 = [1, 2, 3, 4, 5]
resultado4 = list4.pop(0)
print ("Primeiro elemento é: ",resultado4)
resultado4 = list4.pop(3)
print ("Último elemento é: ",resultado4)

#Exercício 5: Acesse os três primeiros caracteres de uma string.
text ="Corinthians"
parte = text[:3]
print(parte)

#Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.
text1 ="Corinthians"
parte1 = text1[2:10] # Pode-se usar [1:-1]
print(parte1)


#<Desafio: Calculadora de Média >

portugues = float(input('Digite a note de Portugês: '))
matematica = float(input('Digite a note de matematica: '))
inglês = float(input('Digite a note de inglês: '))

media = (portugues + matematica + inglês) / 3
print (media)

if media >= 7:
 print ("Aprovado")
elif media >=5:
  print ("Reperação")
else:
 print ("Reprovado")


# Instruções:
# Peça ao usuário que insira três notas (por exemplo, de 0 a 10).
# Use a função input() para obter as notas como entrada do usuário e converta-as em números de ponto flutuante.
# Cal das três ncule a médiaotas.
# Com base na média, forneça uma avaliação:
# Se a média for maior ou igual a 7, imprima "Aprovado".
# Se a média for maior ou igual a 5 e menor do que 7, imprima "Recuperação".
# Se a média for menor do que 5, imprima "Reprovado".
#### Certifique-se de lidar com possíveis erros, como entradas inválidas (por exemplo, notas fora do intervalo de 0 a 10).
# A SAÍDA PRECISA FICAR ASSIM NÃO COM OS MESMOS NÚMEROS, MAS
# PRECISA SER ASSIM: 

# Por favor, insira a primeira nota: 8.5
# Por favor, insira a segunda nota: 6.0
# Por favor, insira a terceira nota: 4.5

# Sua média é 6.33 e você está em Recuperação.