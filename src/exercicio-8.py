"""
T = {1,2,3,4,5,6}
U = {3,4,5}
V = {5,6,7,8}
W = {6,7,8,9}

Determine (T ∩ U) ∪ (V ∩ W ).
Determine (T ∪ V) ∩ W .
Determine T − (U ∪ V).

Determine a cardinalidade de cada resultado.

Verifique:
5 ∈ U ?
2 ∈ W ?
U ⊆ T ?
"""
T = {1,2,3,4,5,6}
U = {3,4,5}
V = {5,6,7,8}
W = {6,7,8,9}

resultado=((T & U) | (V & W))
print("A União das diferenças das variaveis é ", resultado)

resultado2=((T | V) & W)
print("O resultado 2 é:", resultado2)

resultado3=(T - (U | V))
print("O resultado 3 é:", resultado3)

cardresultado=len(resultado)
cardresultado2=len(resultado2)
cardresultado3=len(resultado3)
print("A cardinalidade dos resultados em ordem são:",cardresultado,cardresultado2,cardresultado3)
print(5 in U)
print(2 in W)
print(U <= T)