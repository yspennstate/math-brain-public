#!/usr/bin/env python3
# R04 exact-arithmetic SELF-CHECK.
# This checks finite algebra and metric constant simplification only.
# It does NOT prove the spectral-averaging or Minami inequalities cited in the report.
import sympy as sp

# 1. Exact projection/factorial-count algebra core.
A=sp.Matrix([[1,0],[0,1],[1,1],[2,-1]])
P=A*(A.T*A).inv()*A.T
assert P*P == P
r=sp.trace(P)
lhs=(sp.trace(P))**2-sp.trace(P)
rhs=sp.Integer(0)
for i in range(P.rows):
    for j in range(P.rows):
        if i!=j:
            rhs += P[i,i]*P[j,j]-P[i,j]*P[j,i]
assert sp.simplify(lhs-rhs)==0
assert sp.simplify(lhs-r*(r-1))==0
assert r==2 and lhs==2

# 2. Exact simplification of the R04 metric coefficient.
N,W=sp.symbols('N W', positive=True, integer=True)
pi=sp.pi
rho_star=sp.sqrt((2*W+1)/(2*pi))
Ilen=2*pi/N
a=sp.simplify(N*rho_star*Ilen)
assert sp.simplify(a-sp.sqrt(2*pi*(2*W+1)))==0
a2=sp.simplify(a*a)
assert sp.simplify(a2-2*pi*(2*W+1))==0
B=sp.simplify(a+a2)
assert sp.simplify(B-(2*pi*(2*W+1)+sp.sqrt(2*pi*(2*W+1))))==0

# 3. Numerical exact-domain examples (symbolic pi retained).
for n,c_num,c_den in [(100,1,1),(400,3,2),(1024,5,4)]:
    c=sp.Rational(c_num,c_den)
    w=int(sp.floor(c*sp.sqrt(n)))
    assert 2*w+1 <= n
    b=2*pi*(2*w+1)+sp.sqrt(2*pi*(2*w+1))
    print(f"N={n} c={c} W={w} domain=PASS B={sp.sstr(b)}")

print("projection_identity=PASS rank=2 factorial=2")
print("metric_identity=PASS a=sqrt(2*pi*(2W+1))")
print("bound_identity=PASS B=2*pi*(2W+1)+sqrt(2*pi*(2W+1))")
print("SELF-CHECK PASS")
