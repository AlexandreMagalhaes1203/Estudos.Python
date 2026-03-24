"""
Considere
Q = {1,3,5,7,9}
R = {2,3,5,7,11}
S = {1,2,3,4,5}

Determine (Q ∩ R) ∪ S.
Determine Q ∩ (R ∪ S).

Determine a cardinalidade dos resultados.
Os conjuntos obtidos são iguais?

Verifique:
3 ∈ Q ?
11 ∈ Q ?
(Q ∩ R) ⊆ Q ?
"""

Q = {1,3,5,7,9}
R = {2,3,5,7,11}
S = {1,2,3,4,5}

resultado=((Q & R) | S)
print("O resultado de (Q ∩ R) ∪ S é:", resultado)

resultado2=(Q & (R | S))
print("O resutado de Q ∩ (R ∪ S) é :", resultado2)

cardresultado=len(resultado)
cardresultado2=len(resultado2)

print("A cardinalidade dos resultados é",cardresultado,cardresultado2)

print(3 in Q)

print(11 not in Q)

print(Q <= (Q & R))
