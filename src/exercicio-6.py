"""
Considere
N = {1.5,2.0,2.5,3.0,3.5,4.0}
O = {2.0,3.0,4.5,5.0}
P = {3.0,3.5,4.0,4.5}

Determine N ∪ (O ∩ P).
Determine (N ∩ O) − P.

Determine a cardinalidade dos conjuntos obtidos.

Verifique:
3.5 ∈ N ?
5.0 ∈ P ?
(N ∩ O) ⊆ N ?
"""

N = {1.5,2.0,2.5,3.0,3.5,4.0}
O = {2.0,3.0,4.5,5.0}
P = {3.0,3.5,4.0,4.5}

resultado=(N | (O & P))
print("O resultado de N ∪ (O ∩ P) é :", resultado)

resultado2=((N & O) - P)
print("O resultado de (N ∩ O) − P é",resultado2)

cardresultado=len(resultado)
print("A cardinalidade do primeiro resultado é :",cardresultado)

cardresultado2=len(resultado2)
print("A cardinalidade do segundo resultado é :",cardresultado2)

print(3.5 in N)
print(5.0 in P)

print((N & O) <= N)