"""
C = {2,4,6,8,10,12}
D = {1,2,3,4,5,6,7,8,9}

Determine (C ∪ D) − C.
Determine D − (C ∩ D).

Determine a cardinalidade do conjunto obtido em (1).
Compare a cardinalidade de C com a de D.

Verifique:
6 ∈ C ?
11 ∈ D ?
C ⊆ D ?

"""

C = {2,4,6,8,10,12}
D = {1,2,3,4,5,6,7,8,9}

resultado = ((C | D) - C)
print("Resultado da uniao de C e D, e diferença de  C é :", resultado)

resultado2 = (D - (C & D))
print("Resultado da interseçao de C e D, e diferença de D é :", resultado2)

cardresultado=len(resultado)
print("O resultado da cardinalidade do primeiro conjunto é :", cardresultado)

cardresultado2=len(C)
cardresultado3=len(D)
resultadocard=(cardresultado2,cardresultado3)
print("A cardinalidade de de C com D é :",resultadocard)



print(6 in C)
# If e else pode ser substituido por print (x in y) pertence, e print(x not in y), nao pertece.

print(11 not in D)

print(C <= D)

