"""
Considere x ∈ N com 1 ≤ x ≤ 40.

C = {x | x é ímpar e x > 15}
D = {x | x é múltiplo de 5 e x < 30}

Determine C − D.
Determine D − C.
Determine a cardinalidade dos conjuntos obtidos.

Verifique:
21 ∈ C ?
25 ∈ D ?
(C − D) ⊆ C ?
"""

C ={x for x in range(1,41) if x % 2 != 0 and x > 15}
print(C)


D = {x for x in range(1,41) if x % 5 == 0 and x < 30}
print(D)

difCeD=(C - D)
print("Diferença de C e D é :", difCeD)

difDeC=(D - C)
print("A diferença de D e C é:",difDeC)

cardCdeD=len(difCeD)
cardDdeC=len(difDeC)

print("A cardinalidade das 2 diferenças é:", cardCdeD,cardDdeC)

print(21 in C)
print(25 in D)
print(difCeD <= C)