"""
Considere
H = {2,4,6,8,10}
I = {1,2,3,4,5,6}
J = {4,6,8}

Determine (H ∩ I) ∪ J.
Determine H ∩ (I ∪ J).
Determine H − (I ∩ J).

Determine a cardinalidade de cada resultado.

Verifique:
6 ∈ H ?
3 ∈ H ?
J ⊆ H ?
"""

H = {2,4,6,8,10}
I = {1,2,3,4,5,6}
J = {4,6,8}

resultado=((H & I) | J)
print("O resultado de (H ∩ I) ∪ J é:", resultado)

resultado2=(H & (I | J))
print("O resultado de H ∩ (I ∪ J) é :", resultado2)

resultado3=(H - (I & J))
print("O resultado de H − (I ∩ J) é:", resultado3)

cardresultado=len(resultado)
cardresultado2=len(resultado2)
cardresultado3=len(resultado3)
print("A cardinalidade de cada uma das alternativas em ordem é :", cardresultado,cardresultado2,cardresultado3)

print(6 in H)
print (3 in H)
print(J <= H)