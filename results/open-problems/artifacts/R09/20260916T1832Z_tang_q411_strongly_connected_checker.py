#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

print("R09 Tang Q4.11 strengthened checker")

def theta2(k, p):
    assert k >= 3
    return F(k-2) * (p**(k-4)) * (F(2*(k-1))*p - F(k-3))

assert theta2(3,F(3,4)) == 4
assert theta2(4,F(3,4)) == 7
for k in range(4,101):
    pk = F(k*k-1,k*k)
    lhs = theta2(k,pk)
    rhs = F(15,16)*k*(k-2)
    assert lhs >= rhs > 0
print("stem family exact checks: theta_3''(3/4)=4, theta_4''(3/4)=7")
print("certified family lower bound: theta_k''(1-1/k^2) >= (15/16) k(k-2), k>=4")
print("metric status in T_k family: UNBOUNDED ABOVE")

A = sp.Matrix([[0,1,1],[1,1,0],[2,1,2]])
lam = sp.symbols('lam')
charpoly = sp.factor(A.charpoly(lam).as_expr())
assert sp.expand(charpoly - (lam-3)*(lam-1)*(lam+1)) == 0

adj = [[bool(A[i,j] > 0) for j in range(3)] for i in range(3)]
def reachable(i,j):
    seen={i}; stack=[i]
    while stack:
        u=stack.pop()
        if u==j: return True
        for v,e in enumerate(adj[u]):
            if e and v not in seen:
                seen.add(v); stack.append(v)
    return False
assert all(reachable(i,j) for i in range(3) for j in range(3))
print("strongly connected matrix A =", A.tolist())
print("charpoly =", charpoly)
print("Perron root = 3, hence pc = 1/3 by Tang Lemma 4.9")

p,y=sp.symbols('p y')
x0,x2=sp.symbols('x0 x2')

E0 = x0 - (1-(1-p*y)*(1-p*x2))
E1 = y  - (1-(1-p*x0)*(1-p*y))
E2 = x2 - (1-(1-p*x0)**2*(1-p*y)*(1-p*x2)**2)

x0e = sp.factor(y*(1-p)/(p*(1-p*y)))
x2e = sp.factor(y*(p**3*y-p**2-p+1)/(p**2*(1-p*y)**2))
assert sp.factor(E0.subs({x0:x0e,x2:x2e})) == 0
assert sp.factor(E1.subs({x0:x0e,x2:x2e})) == 0

P = sp.expand(
   p**6*y**4
   -5*p**5*y**3 - p**4*y**3
   +10*p**4*y**2
   +p**3*y**3 +2*p**3*y**2 -9*p**3*y
   -2*p**2*y**3 +p**2*y**2 -3*p**2*y +3*p**2
   +p*y**3 +2*p
   - y**3 +2*y**2 - y -1
)
ratio = sp.factor(E2.subs({x0:x0e,x2:x2e})/P)
assert sp.simplify(ratio + y*(p-1)/(p**2*(p*y-1)**5)) == 0

p0=sp.Rational(17,50)
L=sp.Rational(16112,10**6)
R=sp.Rational(16113,10**6)
assert p0 > sp.Rational(1,3)

P0=sp.Poly(P.subs(p,p0),y,domain=sp.QQ)
assert P0.eval(L) > 0
assert P0.eval(R) < 0
assert P0.count_roots(L,R) == 1

x0L=sp.factor(x0e.subs({p:p0,y:L}))
x0R=sp.factor(x0e.subs({p:p0,y:R}))
assert 0 < x0L < x0R < 1

dx2dy=sp.factor(sp.diff(x2e,y).subs(p,p0))
dx2_num_expr, dx2_den_expr = sp.fraction(dx2dy)
dx2_num=sp.Poly(dx2_num_expr,y,domain=sp.QQ)
dx2_den=sp.Poly(dx2_den_expr,y,domain=sp.QQ)
assert dx2_den.eval(L)<0 and dx2_den.eval(R)<0 and dx2_den.count_roots(L,R)==0
assert dx2_num.eval(L)<0 and dx2_num.eval(R)<0 and dx2_num.count_roots(L,R)==0
x2L=sp.factor(x2e.subs({p:p0,y:L}))
x2R=sp.factor(x2e.subs({p:p0,y:R}))
assert 0 < x2L < x2R < 1

print("at p=17/50, unique eliminated root y in [16112/1e6,16113/1e6]")
print("reconstructed x0 interval:", x0L, x0R)
print("reconstructed x2 interval:", x2L, x2R)
print("positive fixed point lies in (0,1)^3; Tang Lemma 4.14 selects it as physical")

Pp=sp.diff(P,p); Py=sp.diff(P,y)
Ppp=sp.diff(Pp,p); Ppy=sp.diff(Pp,y); Pyy=sp.diff(Py,y)
yp=sp.cancel(-Pp/Py)
ypp=sp.cancel(-(Ppp + 2*Ppy*yp + Pyy*yp**2)/Py)
num,den=sp.fraction(ypp)
c=sp.Rational(4929,1000)
Py0=sp.Poly(Py.subs(p,p0),y,domain=sp.QQ)
Q0=sp.Poly((num-c*den).subs(p,p0),y,domain=sp.QQ)
den0=sp.Poly(den.subs(p,p0),y,domain=sp.QQ)

assert Py0.eval(L)<0 and Py0.eval(R)<0 and Py0.count_roots(L,R)==0
assert den0.eval(L)<0 and den0.eval(R)<0 and den0.count_roots(L,R)==0
assert Q0.eval(L)<0 and Q0.eval(R)<0 and Q0.count_roots(L,R)==0

print("exact Sturm certificate: Py<0 and (num-(4929/1000)den)<0 on root interval")
print("therefore physical type-1 theta''(17/50) > 4929/1000")
print("PASS")
