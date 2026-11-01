#!/usr/bin/env python3
import sympy as sp
import itertools

c = sp.symbols("c", nonnegative=True, real=True)
x = sp.symbols("x")
d = 2*c/(1+c**2)

def heatbath_matrix(n, edges):
    states = list(itertools.product([-1,1], repeat=n))
    idx = {s:i for i,s in enumerate(states)}
    nbr = [[] for _ in range(n)]
    for a,b in edges:
        nbr[a].append(b); nbr[b].append(a)
    P = sp.zeros(2**n)
    def th(k):
        if k == 0: return sp.Integer(0)
        if abs(k) == 1: return sp.sign(k)*c
        if abs(k) == 2: return sp.sign(k)*d
        raise RuntimeError("degree/field outside n<=3 checker")
    for si,s in enumerate(states):
        for i in range(n):
            t = th(sum(s[j] for j in nbr[i]))
            pplus = (1+t)/2
            sp1=list(s); sp1[i]=1
            sm1=list(s); sm1[i]=-1
            P[si,idx[tuple(sp1)]] += pplus/sp.Integer(n)
            P[si,idx[tuple(sm1)]] += (1-pplus)/sp.Integer(n)
    return sp.simplify(P)

graphs = {
    "empty": [],
    "one_edge": [(0,1)],
    "path": [(0,1),(1,2)],
    "triangle": [(0,1),(1,2),(0,2)],
}
expected = {
    "empty": x*(x-1)*(3*x-2)**3*(3*x-1)**3 / sp.Integer(729),
    "path": x*(x-1)*(3*x-2)*(3*x-1)
        *(9*c**2*x**2 - 12*c**2*x + 2*c**2 + 9*x**2 - 12*x + 4)
        *(9*c**2*x**2 - 6*c**2*x - c**2 + 9*x**2 - 6*x + 1)
        /(sp.Integer(729)*(1+c**2)**2),
    "triangle": x*(x-1)
        *(3*c**2*x - 2*c**2 - 2*c + 3*x - 2)
        *(3*c**2*x - 2*c**2 + c + 3*x - 2)**2
        *(3*c**2*x - c**2 - 2*c + 3*x - 1)
        *(3*c**2*x - c**2 + c + 3*x - 1)**2
        /(sp.Integer(729)*(1+c**2)**6),
}

P1 = heatbath_matrix(3, graphs["one_edge"])
cp1 = sp.factor(P1.charpoly(x).as_expr())
print("one_edge_charpoly =", cp1)

for name in ("empty","path","triangle"):
    P = heatbath_matrix(3, graphs[name])
    cp = sp.factor(P.charpoly(x).as_expr())
    assert sp.simplify(cp - expected[name]) == 0, name
    print(name + "_charpoly =", cp)

lam_edge = (2+c)/3
assert sp.simplify(cp1.subs(x, lam_edge)) == 0

s2 = 2*c**2/(1+c**2)
lam_path = sp.Rational(2,3) + sp.sqrt(s2)/3
lam_tri = sp.Rational(2,3) + d/3
assert sp.simplify(heatbath_matrix(3,graphs["path"]).charpoly(x).as_expr().subs(x,lam_path)) == 0
assert sp.simplify(heatbath_matrix(3,graphs["triangle"]).charpoly(x).as_expr().subs(x,lam_tri)) == 0

print("s_squared_minus_c_squared =", sp.factor(s2-c**2))
print("d_squared_minus_s_squared =", sp.factor(d**2-s2))
assert sp.simplify((s2-c**2) - c**2*(1-c**2)/(1+c**2)) == 0
assert sp.simplify((d**2-s2) - 2*c**2*(1-c**2)/(1+c**2)**2) == 0

print("ALL_EXACT_CHECKS_PASS")
