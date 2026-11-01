import sympy as sp
import itertools

# Exact K4 forest polynomial.
a,b,c,d,e,f = sp.symbols("a b c d e f", positive=True)
ys = [a,b,c,d,e,f]
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def is_forest(sel):
    parent = list(range(4))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for j in sel:
        u,v = edges[j]
        ru,rv = find(u),find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True

Z = sp.expand(sum(
    sp.prod(ys[j] for j in sel)
    for r in range(7)
    for sel in itertools.combinations(range(6), r)
    if is_forest(sel)
))

def delta(i,j):
    return sp.expand(sp.diff(Z,ys[i])*sp.diff(Z,ys[j]) - Z*sp.diff(Z,ys[i],ys[j]))

D_adj = delta(0,1)     # marked 01,02
D_dis = delta(0,5)     # marked 01,23
adj_formula = sp.expand(
    d**2*(1+c+e+f)**2
    + d*(1+c+e+f)*(1+c+e+f+2*e*f)
    + e*f*(1+e)*(1+f)
)
dis_formula = sp.expand(
    (b*e-c*d)**2 + b*e*(1+b+e) + c*d*(1+c+d)
)
assert sp.expand(D_adj-adj_formula) == 0
assert sp.expand(D_dis-dis_formula) == 0

# Formal series-extension identities.  Q(z)=Z0+z Z1; replace z by a two-edge path x,y.
Z0,Z1,Z0h,Z1h,x,y = sp.symbols("Z0 Z1 Z0h Z1h x y")
A = 1+x+y
P = A*Z0 + x*y*Z1
Px = sp.diff(P,x)
Py = sp.diff(P,y)
Dxy = sp.expand(Px*Py - P*sp.diff(Px,y))
assert sp.expand(Dxy - Z0*(Z0-Z1)) == 0
Ph = A*Z0h + x*y*Z1h
Dxh = sp.expand(Px*Ph - P*sp.diff(Ph,x))
base_Dgh = sp.expand(Z1*Z0h - Z0*Z1h)
assert sp.expand(Dxh - y*(1+y)*base_Dgh) == 0

# Formal parallel-extension identities.  Replace z by parallel x,y.
Ppar = Z0 + (x+y)*Z1
Ppar_x = sp.diff(Ppar,x)
Ppar_y = sp.diff(Ppar,y)
Dpar_xy = sp.expand(Ppar_x*Ppar_y - Ppar*sp.diff(Ppar_x,y))
assert sp.expand(Dpar_xy - Z1**2) == 0
Ppar_h = Z0h + (x+y)*Z1h
Dpar_xh = sp.expand(Ppar_x*Ppar_h - Ppar*sp.diff(Ppar_h,x))
assert sp.expand(Dpar_xh - base_Dgh) == 0

# Exact nullity/parallel-excess root ladder from a^2+4(E+3)a<=1.
aa,E = sp.symbols("aa E", positive=True)
root = sp.sqrt(4*(E+3)**2 + 1) - 2*(E+3)
assert sp.expand(root**2 + 4*(E+3)*root - 1) == 0

print("K4_WEIGHTED_RAYLEIGH_CHECK=PASS")
print("ADJACENT_FORMULA=d^2(1+c+e+f)^2+d(1+c+e+f)(1+c+e+f+2ef)+ef(1+e)(1+f)")
print("DISJOINT_FORMULA=(be-cd)^2+be(1+b+e)+cd(1+c+d)")
print("SERIES_PAIR_FORMULA=Z0*(Z0-Z1)")
print("SERIES_MIXED_FORMULA=y*(1+y)*(Z1*Z0h-Z0*Z1h)")
print("PARALLEL_PAIR_FORMULA=Z1^2")
print("PARALLEL_MIXED_FORMULA=Z1*Z0h-Z0*Z1h")
for ev in range(4):
    print(f"E={ev} a_max={sp.N(root.subs(E,ev),18)}")
print("STATUS=PASS")
