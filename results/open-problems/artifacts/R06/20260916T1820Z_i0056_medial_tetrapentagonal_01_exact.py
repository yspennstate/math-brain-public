from itertools import product
import sympy as sp

r3=sp.sqrt(3)
r5=sp.sqrt(5)
phi=(1+r5)/2

def transitions(bits):
    m=len(bits)
    return sum(bits[i]!=bits[(i+1)%m] for i in range(m))

def terminal(bits):
    # selected=1. Every unselected position has at most one selected cyclic neighbor.
    m=len(bits)
    return all(bits[i] or (bits[(i-1)%m]+bits[(i+1)%m] <= 1) for i in range(m))

print("R06 I0056 tetrapentagonal medial exact checker")

# A. Local partial-face inequality before closure: l <= 3 t / 2 on C4.
for bits in product([0,1], repeat=4):
    l=sum(bits); t=transitions(bits)
    if 0<l<4:
        assert 2*l <= 3*t
print("C4 partial-face incidence inequality: PASS")

# B. Terminal local patterns.
for m, max_l in [(4,2),(5,3)]:
    pats=[]
    for bits in product([0,1], repeat=m):
        l=sum(bits); t=transitions(bits)
        if 0<l<m and terminal(bits):
            assert t==2
            assert l<=max_l
            pats.append(("".join(map(str,bits)),l,t))
    print(f"C{m} terminal partial patterns: {len(pats)} PASS")
    print("  ", pats)

# C. Exact known dual vertex constant used in the lower bound.
hstar = 2/r3
assert sp.simplify(hstar**2-sp.Rational(4,3))==0

# Universal nonamenability lower bound (before closure).
c0 = sp.simplify(2/(2/hstar + sp.Rational(3,2)))
assert sp.simplify(c0 - 4/(3+2*r3))==0
assert c0>0

# Terminal/closure edge lower bound.
hedge = sp.simplify(2/(2/hstar+1))
assert sp.simplify(hedge-(r3-1))==0
assert hedge>0

# D. Closure-to-vertex lower-bound optimization.
h=hedge
tstar=sp.simplify(3*h/(4-3*h))
hv=sp.simplify(h/(4-3*h))
assert tstar>=0
assert sp.simplify(hv-(1+2*r3)/11)==0

# E. Ball construction asymptotic algebra.
assert sp.simplify(1+phi-phi**2)==0
g=sp.simplify(phi**2)
x=sp.simplify(5/(1+g))
assert sp.simplify(x-(5-r5)/2)==0
across_over_V=sp.simplify(x*phi)
assert sp.simplify(across_over_V-r5)==0
S_over_V=sp.simplify((5-across_over_V)/2)
assert sp.simplify(S_over_V-(5-r5)/2)==0
boundary_over_V=sp.simplify(2/phi)
upper=sp.simplify(boundary_over_V/S_over_V)
assert sp.simplify(upper-2/r5)==0
assert upper<1

# F. New certified intervals.
edge_width=sp.simplify(upper-hedge)
vertex_upper=upper
vertex_lower=hv
vertex_width=sp.simplify(vertex_upper-vertex_lower)
assert edge_width>0
assert vertex_width>0

print("h*(H_{4,5}) =", hstar)
print("universal medial edge lower before closure c0 =", c0, float(c0))
print("terminal closure edge lower =", hedge, float(hedge))
print("closure-derived vertex lower =", hv, float(hv))
print("ball-construction edge/vertex upper =", upper, float(upper))
print("edge interval width =", edge_width, float(edge_width))
print("vertex interval width =", vertex_width, float(vertex_width))
print("milestone Phi_E(T)>=1: REFUTED by certified asymptotic upper since 2/sqrt(5)<1")
print("PASS")
