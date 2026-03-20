"""
Considere os conjuntos

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

Determine A ∪ B.
Determine A − B.

Determine a cardinalidade de A ∪ B.
Determine a cardinalidade de A ∩ B.

Verifique:
4 ∈ A ?
7 ∈ A ?
A ∩ B ⊆ A ? 
"""

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

print(" Conjunto A",A)
print("Conjunto B",B)

uniao =A|B
print("A uniao dos conjuntos ", uniao)

dfAB = A - B
print("A diferença dos conjuntos", dfAB)


cardAUB=len(uniao)
print("A Uniao entre A e B é ", cardAUB)

cardAIB=len(A & B)
print("A Intersecçao entre A e B é",cardAIB)



if 7 in A:
    print("O valor está dentro do conjunto A ")

else: 
    print("O valor nao está ")

if 4 in A:
    print("O valor está dentro do conjunto A ")

else: 
    print("O valor nao está ")


cardAxB=(A & B)


resultado = cardAxB <= A
print("O resultado ",resultado)

# Pode ser tbm print ((A & B ) <= A)

# (A & B ).intersection(A)