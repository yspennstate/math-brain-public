import sympy as sp

x = sp.symbols("x1:5")
edge_pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
y = sp.symbols("y12 y13 y14 y23 y24 y34")

L = sp.zeros(4)
for (u,v), w in zip(edge_pairs, y):
    L[u,u] += w
    L[v,v] += w
    L[u,v] -= w
    L[v,u] -= w

P = sp.Poly(sp.expand((L + sp.diag(*x)).det()), *y)

def coeff(indices):
    exps = [0]*len(y)
    for i in indices:
        exps[i] += 1
    return sp.factor(P.coeff_monomial(tuple(exps)))

# Forest y23*y34 has components {1} and {2,3,4}.
c13 = coeff([3,5])
# Forest y12*y34 has components {1,2} and {3,4}.
c22 = coeff([0,5])

assert sp.expand(c13 - x[0]*(x[1]+x[2]+x[3])) == 0
assert sp.expand(c22 - (x[0]+x[1])*(x[2]+x[3])) == 0

print("K4_ROOTED_DETERMINANT_COEFFICIENT_CHECK")
print("partition 1+3:", c13)
print("partition 2+2:", c22)
print("after permutation symmetrization:")
print("  E[1+3 coefficient] = 3*m2")
print("  E[2+2 coefficient] = 4*m2")
print("uniform unrooted coefficient c>0 would require 3*m2=c=4*m2")
print("hence m2=0 and c=0, contradiction")
print("DETERMINANT_MIXTURE_UNROOTING_NO_GO_PASS")
