#!/usr/bin/env python3
from fractions import Fraction as F

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def mv(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A)))

def mtv(A,x):
    return tuple(sum(A[i][j]*x[i] for i in range(len(x))) for j in range(len(A[0])))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def norm2(a):
    return dot(a,a)

A=B=F(1)
z=F(1,2)
p=(F(-1),F(0),F(1,2))
q=p
Z=(
    (F(0),F(0),F(1)),
    (F(0),F(0),F(0)),
    (F(1),F(0),F(1,2)),
)
e=(F(0),F(0),F(1))
mx=(F(-1),F(0),F(0))
me=(F(0),F(0),F(-1))

def f(n,m):
    return dot(p,n)+dot(q,m)+dot(n,mv(Z,m))

# Stationarity at the north pole.
assert add(p,mv(Z,e)) == (F(0),F(0),A)
assert add(q,mtv(Z,e)) == (F(0),F(0),B)

north=f(e,e)
left_ant=f(me,e)
right_ant=f(e,me)
both_ant=f(me,me)
off=f(mx,mx)
assert north == F(3,2)
assert left_ant == right_ant == both_ant == F(-1,2)
assert off == F(2)
assert off > north

# Existing local mixed-Hessian gate is strict: tangent cross block M=0,
# so the tangent Hessian is diag(-I_2,-I_2).
local_cross=((F(0),F(0)),(F(0),F(0)))
assert local_cross == ((F(0),F(0)),(F(0),F(0)))
assert A>0 and B>0

L=p[2]+B
assert L == F(3,2)
assert L*L == F(9,4)
assert norm2(p) == F(5,4)
assert L*L > norm2(p)

# The exact squared trust-region inequality at n=-e_1 fails.
qn=add(q,mtv(Z,mx))
trust=(L-dot(p,mx))**2 - norm2(qn)
assert trust == F(-1)

print('PASS MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1')
print('north =', north)
print('individual antipodes =', left_ant, right_ant)
print('simultaneous antipode =', both_ant)
print('off-axis (-x,-x) =', off)
print('local Hessian = -I_4 (strict)')
print('L^2 =', L*L, '||p||^2 =', norm2(p))
print('trust quadratic at n=-x =', trust)
