#!/usr/bin/env python3
# Exact symbolic checker for R09 Tang Q4.11 recovery:
# G = Cay(C2 * C4, {a,b,b^{-1}}), simple-graph convention.
# Uses exact SymPy integer/rational polynomial arithmetic only.

import sympy as sp
from itertools import product

p,t,u=sp.symbols('p t u')

# Exact C4 factor-cluster PGF by exhaustive enumeration of its 2^4 bond states.
edges=[(0,1),(1,2),(2,3),(3,0)]
dist={k:sp.Integer(0) for k in range(4)}
for bits in product([0,1], repeat=4):
    prob=sp.Integer(1)
    adj={i:[] for i in range(4)}
    for bit,(a,b) in zip(bits,edges):
        prob *= p if bit else (1-p)
        if bit:
            adj[a].append(b); adj[b].append(a)
    seen={0}; stack=[0]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    dist[len(seen)-1]+=sp.expand(prob)

expected_dist={
    0:(1-p)**2,
    1:2*p*(1-p)**2,
    2:3*p**2*(1-p)**2,
    3:p**3*(4-3*p),
}
for k in range(4):
    assert sp.expand(dist[k]-expected_dist[k])==0
assert sp.expand(sum(dist.values())-1)==0

F4=sp.expand(sum(dist[k]*t**k for k in range(4)))
mu4=sp.factor(sp.diff(F4,t).subs(t,1))
assert sp.expand(mu4 - p*(2+2*p+2*p**2-3*p**3))==0

# C2 block PGF and two-type critical polynomial.
F2=1-p+p*t
mu2=p
H=sp.expand(mu2*mu4-1)
H_expected=-3*p**5+2*p**4+2*p**3+2*p**2-1
assert sp.expand(H-H_expected)==0

# Exact critical bracket.
lo=sp.Rational(11151,20000)   # 0.55755
hi=sp.Rational(13939,25000)   # 0.55756
assert H.subs(p,lo)<0
assert H.subs(p,hi)>0

# Fixed-point elimination: u = F2(v), v=F4(u).
v=(u-1+p)/p
elim=sp.factor(sp.together(F4.subs(t,u)-v))
Q=p**4*(3*p-4)*u**2+p**3*(2*p-3)*u+(p**3-2*p**2+1)
assert sp.factor(elim + (u-1)*Q/p)==0
assert sp.factor(Q.subs(u,1)+H)==0  # Q(1)=-H

# Explicit positive physical root.
D=-8*p**4+28*p**3-23*p**2-12*p+16
u_phys=-(2*p**2-3*p+sp.sqrt(D))/(2*p**2*(3*p-4))
assert sp.simplify(Q.subs(u,u_phys))==0
v_phys=sp.simplify((u_phys-1+p)/p)
theta=sp.simplify(1-u_phys*v_phys)

# Exact second derivative closed form.
theta2=sp.factor(sp.diff(theta,p,2))
A=54*p**8-477*p**7+1674*p**6-3288*p**5+3841*p**4-1338*p**3-3360*p**2+4800*p-1920
B=(1728*p**13-25632*p**12+150606*p**11-437346*p**10+546471*p**9
   +294186*p**8-1911180*p**7+2300491*p**6-370272*p**5-1577694*p**4
   +1281040*p**3-480*p**2-374784*p+122880)
claimed=(D**2*A+p*B*sp.sqrt(D))/(p**7*(3*p-4)**4*D**2)
assert sp.simplify(theta2-claimed)==0

# Bernstein coefficients on [0,1].
def bernstein_coeffs(poly):
    P=sp.Poly(sp.expand(poly),p)
    n=P.degree()
    a=[P.nth(k) for k in range(n+1)]
    b=[]
    for j in range(n+1):
        bj=sp.Integer(0)
        for k in range(j+1):
            bj += a[k]*sp.binomial(j,k)/sp.binomial(n,k)
        b.append(sp.factor(bj))
    recon=sp.expand(sum(b[j]*sp.binomial(n,j)*p**j*(1-p)**(n-j) for j in range(n+1)))
    assert sp.expand(recon-poly)==0
    return b

bD=bernstein_coeffs(D)
bmA=bernstein_coeffs(-A)
bB=bernstein_coeffs(B)
assert all(x>0 for x in bD)
assert all(x>0 for x in bmA)
assert all(x>0 for x in bB)

T=(13824*p**23-315648*p**22+3123072*p**21-17394720*p**20
   +58539929*p**19-113818081*p**18+84186710*p**17+136515571*p**16
   -365453213*p**15+150787765*p**14+418270231*p**13-397180184*p**12
   -446325581*p**11+674284977*p**10+421102215*p**9-1098358635*p**8
   +153376275*p**7+846351135*p**6-511305216*p**5-214036224*p**4
   +280304640*p**3-29491200*p**2-47923200*p+14745600)
bT=bernstein_coeffs(T)
assert all(x>0 for x in bT)

# Squared domination identity used in the analytic sign proof.
S=sp.expand(D**3*A**2-p**2*B**2)
assert sp.factor(S + 4*(p-1)*(3*p-4)**4*T)==0
# Since p in (0,1): D>0, -A>0, B>0, T>0 and
# D^3 A^2 > p^2 B^2, hence -D^2 A > p B sqrt(D),
# so D^2 A + p B sqrt(D) < 0.

print("R09 Tang Q4.11 C2*C4 exact checker")
print("C4 factor distribution:", [sp.factor(dist[k]) for k in range(4)])
print("mu4 =", mu4)
print("critical polynomial H =", H)
print("critical bracket =", lo, hi)
print("fixed-point elimination = PASS")
print("physical-root residual = PASS")
print("theta'' symbolic identity = PASS")
print("positive Bernstein certificates:")
print("  D:", bD)
print("  -A:", bmA)
print("  B:", bB)
print("  T:", bT)
print("square-domination identity = PASS")
print("CONCLUSION_FINITE_CORE: theta''(p)<0 on the physical branch for pc<p<1")
print("PASS")
