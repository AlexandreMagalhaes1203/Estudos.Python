"""
Considere x ∈ N com 1 ≤ x ≤ 30.

A = {x | x é par e x > 10}
B = {x | x é múltiplo de 3 e x < 25}

Determine A.
Determine B.
Determine A ∩ B.
Determine A ∪ B.

Verifique:
12 ∈ A ?
15 ∈ B ?
A ∩ B ⊆ A ?
"""
 
A = { x for x in range(1,31) if x % 2 ==0 and x > 10}
print(A)
B= { x for x in range(1,31) if x % 3 ==0 and x < 25}
print(B)

intersecao=(A & B)
print("A intersecçao entre A e B é:",intersecao)


uniaoAeB=(A | B)
print("A uniao entre A e B é", uniaoAeB)


print(12 in A)
print(15 in B)
print(A & B <= A)