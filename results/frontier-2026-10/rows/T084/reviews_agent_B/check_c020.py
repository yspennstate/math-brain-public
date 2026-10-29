import itertools, sympy as sp
from fractions import Fraction as Fr
q=t=Fr(1,2); V=range(4); E=list(itertools.combinations(V,2)); co=[Fr(0)]*4
for m in range(1<<6):
    A=[E[i] for i in range(6) if m>>i&1]; p=list(V)
    def f(x):
        while p[x]!=x: x=p[x]
        return x
    for a,b in A:
        ra,rb=f(a),f(b)
        if ra!=rb: p[ra]=rb
    k=len({f(x) for x in V}); deg=sum(1 for e in A if 0 in e)
    co[deg]+=q**k*t**len(A)
z=sp.symbols('z'); print("coeffs", co, [c/Fr(3,128) for c in co])
P=9*z**3+42*z**2+60*z+20; print("disc", sp.discriminant(P,z), "real roots", len(sp.real_roots(P)))
qq,tt=sp.Rational(1,2),sp.Rational(1,2)
H2=qq*((qq+tt*z)**3+3*tt*((1+tt*z)**2+qq-1)*(qq+tt*z)+(3*tt**2+tt**3)*((1+tt*z)**3+qq-1))
print("(2) at 1/2:", sp.expand(H2-sp.Rational(3,128)*P)==0)
