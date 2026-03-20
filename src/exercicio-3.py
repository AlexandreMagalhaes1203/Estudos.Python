"""
Considere
E = {1,2,3,4,5}
F = {3,4,5,6,7}
G = {5,6,7,8,9}
Determine (E ∪ F) ∩ G.
Determine E ∪ (F ∩ G).
Determine a cardinalidade dos dois conjuntos obtidos.
Os resultados são iguais?
Verifique:
5 ∈ E ?
8 ∈ F ?
E ⊆ (E ∪ F) ?
"""

E = {1,2,3,4,5}
F = {3,4,5,6,7}
G = {5,6,7,8,9}

resultado =((E | F ) & G)
print(" O resultado de (E U F) & G é :", resultado)

resultado2 = (E | (F & G))
print(" O resultado de E U(F & G) é :", resultado2)

cardresultado=len(resultado)
cardresultado2=len(resultado2)
Card2Conj = (cardresultado,cardresultado2)
print("A cardinalidade dos dois conjuntos obtidos é :", Card2Conj)
# Os resultado nao sao iguais.

print (5 in E)
print (8 not in F)

print (E <= (E | F))