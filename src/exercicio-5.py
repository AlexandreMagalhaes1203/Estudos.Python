"""
K = {casa, carro, livro, mesa, cadeira, porta}
L = {livro, mesa, quadro, caneta, escola}
M = {mesa, escola, cadeira}

Determine (K ∪ L) − M.
Determine K ∩ (L ∪ M).

Determine a cardinalidade dos conjuntos obtidos.
Quais elementos aparecem em mais de um conjunto?

Verifique:
mesa ∈ K ?
porta ∈ L ?
M ⊆ (K ∪ L) ?
"""
K = {"casa", "carro", "livro", "mesa", "cadeira", "porta"}
L = {"livro", "mesa", "quadro", "caneta", "escola"}
M = {"mesa", "escola", "cadeira"}

resultado=((K | L) - M)
print("O resultado de (K ∪ L) − M é :", resultado)

resultado2=(K & (L | M))
print("O resultado de K ∩ (L ∪ M) é", resultado2)

cardresultado=len(resultado)
print("A cardinalidade do primeiro resultado é :",cardresultado)

cardresultado2=len(resultado2)
print("A cardinalidade do segundo resultado é :",cardresultado2)

print("mesa" in K)
print("porta" in L)
print(M <= (K | L))

