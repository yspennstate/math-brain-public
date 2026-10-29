# controls for exact_pr.py: graphic matroids proved Potts-Rayleigh by Wagner (K4; K4 2-sums) - does coefficientwise hold there?
from exact_pr import run
def graphic(edges, nv):
    return [(1 << a) | (1 << b) for a, b in edges]
K4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
run('M(K4) adjacent', graphic(K4, 4), 0, 1)
run('M(K4) disjoint', graphic(K4, 4), 0, 5)
K5 = [(a,b) for a in range(5) for b in range(a+1,5)]
run('M(K5) adjacent', graphic(K5, 5), 0, 1)
