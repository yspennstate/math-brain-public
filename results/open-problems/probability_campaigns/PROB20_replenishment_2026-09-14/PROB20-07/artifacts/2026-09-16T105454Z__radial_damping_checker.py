#!/usr/bin/env python3
"""
Exact checker for PROB20-07 radial damping theorem.

Verifies:
1. the two neutral endpoint tensors' centered recurrences;
2. barycentric homotopy scales the centered map by lambda;
3. coefficient floor along the homotopy;
4. radial derivative identity for the common Lyapunov function;
5. the explicit global geometric factor q(lambda)=lambda^2(8-3lambda)/5;
6. an exact strict-floor control at lambda=99/100.
"""
import sympy as sp

u, v, lam, t, U, V = sp.symbols("u v lam t U V", real=True)
a = sp.Rational(1, 12)
b = sp.Rational(3, 4)
one3 = sp.Matrix([sp.Rational(1,3)]*3)
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]

def e(k):
    z=[sp.Integer(0)]*3
    z[k]=sp.Integer(1)
    return sp.Matrix(z)

plus_labels = [0,0,1,1,2,2]
minus_labels = [1,2,1,0,0,2]

def endpoint_rows(labels):
    return [a*sp.ones(3,1)+b*e(k) for k in labels]

def homotopy_rows(labels):
    rows0=endpoint_rows(labels)
    return [sp.simplify((1-lam)*one3 + lam*r) for r in rows0]

def qso(x, rows):
    y=sp.zeros(3,1)
    for idx,(i,j) in enumerate(pairs):
        wt=x[i]*x[j]*(1 if i==j else 2)
        y += wt*rows[idx]
    return sp.simplify(y)

# +1 chart
xplus = sp.Matrix([
    sp.Rational(1,3)-v/2+u/2,
    sp.Rational(1,3)+v,
    sp.Rational(1,3)-v/2-u/2,
])
yp0=qso(xplus, endpoint_rows(plus_labels))
up0=sp.simplify(yp0[0]-yp0[2])
vp0=sp.simplify(yp0[1]-sp.Rational(1,3))
assert sp.simplify(up0-u*(4+3*v)/4)==0
assert sp.simplify(vp0+sp.Rational(3,8)*(u**2-3*v**2))==0

yp=qso(xplus, homotopy_rows(plus_labels))
up=sp.simplify(yp[0]-yp[2])
vp=sp.simplify(yp[1]-sp.Rational(1,3))
assert sp.simplify(up-lam*up0)==0
assert sp.simplify(vp-lam*vp0)==0

# -1 chart
xminus = sp.Matrix([
    sp.Rational(1,3)-v/2+u/2,
    sp.Rational(1,3)-v/2-u/2,
    sp.Rational(1,3)+v,
])
ym0=qso(xminus, endpoint_rows(minus_labels))
um0=sp.simplify(ym0[0]-ym0[1])
vm0=sp.simplify(ym0[2]-sp.Rational(1,3))
assert sp.simplify(um0+u*(4+3*v)/4)==0
assert sp.simplify(vm0+sp.Rational(3,8)*(u**2-3*v**2))==0

ym=qso(xminus, homotopy_rows(minus_labels))
um=sp.simplify(ym[0]-ym[1])
vm=sp.simplify(ym[2]-sp.Rational(1,3))
assert sp.simplify(um-lam*um0)==0
assert sp.simplify(vm-lam*vm0)==0

# coefficient floor/high value
low=sp.simplify((1-lam)*sp.Rational(1,3)+lam*sp.Rational(1,12))
high=sp.simplify((1-lam)*sp.Rational(1,3)+lam*sp.Rational(5,6))
assert sp.simplify(low-(sp.Rational(1,3)-lam/4))==0
assert sp.simplify(high-(sp.Rational(1,3)+lam/2))==0
assert sp.simplify(high+2*low-1)==0

# Lyapunov and radial derivative
def L(A,B):
    return sp.expand(A**2+sp.Rational(3,2)*A**2*B+B**2)

radial=sp.factor(sp.diff(L(t*U,t*V), t))
target=sp.factor(t*(2*V**2 + U**2*(2+sp.Rational(9,2)*t*V)))
assert sp.simplify(radial-target)==0

# q(lambda)
q=sp.factor(lam**2*(8-3*lam)/5)
dq=sp.factor(sp.diff(q,lam))
assert sp.simplify(dq-lam*(16-9*lam)/5)==0
assert sp.simplify(q.subs(lam,1)-1)==0
assert sp.simplify(q.subs(lam,0))==0

# Exact strict-floor control lambda=99/100
lc=sp.Rational(99,100)
floor=sp.factor(low.subs(lam,lc))
qc=sp.factor(q.subs(lam,lc))
assert floor == sp.Rational(103,1200)
assert qc == sp.Rational(4929903,5000000)
assert floor > sp.Rational(1,12)
assert qc < 1

print("ALL EXACT RADIAL-DAMPING CHECKS PASSED")
print("low(lambda) =", low)
print("high(lambda) =", high)
print("radial derivative =", radial)
print("q(lambda) =", q)
print("q'(lambda) =", dq)
print("lambda=99/100 floor =", floor)
print("lambda=99/100 q =", qc)
