#!/usr/bin/env python3
"""
R20/I0100 exact SELF-CHECK for the dyadic pair / zonotope reformulation at p=17.

This is not a proof of Randomstrasse Conjecture 26.  It verifies the exact
decomposition of the known p=17 theta-optimal probability measure into pair
sum/difference variables a,b, shows that the even-frequency relaxation has
optimal a_0=1/2, and computes exactly the odd-frequency zonotope radius
rho=sqrt(2)/4.  Therefore the two-scale variational formula returns
mu_0=1/4+sqrt(2)/8 and theta=8-4*sqrt(2).
"""
import sympy as sp

rt2=sp.sqrt(2)
I=sp.I
p=17
n=8
m=4
zeta=sp.exp(2*sp.pi*I/n)
S=[1,4,7]

# Exact theta-optimal measure from the previously certified p=17 basis
mu=[sp.Integer(0)]*n
mu[0]=sp.Rational(1,4)+rt2/8
mu[3]=sp.Rational(1,4)
mu[4]=sp.Rational(1,4)-rt2/8
mu[5]=sp.Rational(1,4)

assert sp.simplify(sum(mu)-1)==0
for s in S:
    F=sp.simplify(sum(mu[j]*zeta**(s*j) for j in range(n)))
    assert sp.simplify(sp.expand_complex(F))==0

a=[sp.simplify(mu[j]+mu[j+m]) for j in range(m)]
b=[sp.simplify(mu[j]-mu[j+m]) for j in range(m)]
assert a == [sp.Rational(1,2),sp.Rational(1,4),0,sp.Rational(1,4)]
assert b == [rt2/4,-sp.Rational(1,4),0,sp.Rational(1,4)]
assert sp.simplify(sum(a)-1)==0
assert sp.simplify(mu[0]-(a[0]+b[0])/2)==0

# Even frequency s=4 becomes ordinary Z_4 frequency k=2.
eta=sp.exp(2*sp.pi*I/m)
even_moment=sp.simplify(sum(a[j]*eta**(2*j) for j in range(m)))
assert sp.simplify(sp.expand_complex(even_moment))==0

# For any nonnegative a with sum 1 and this even moment zero,
# a0+a2=a1+a3=1/2, hence a0<=1/2.  Our a attains 1/2.
left=sp.simplify(a[0]+a[2])
right=sp.simplify(a[1]+a[3])
assert left==right==sp.Rational(1,2)
even_opt_a0=sp.Rational(1,2)

# Odd frequencies s=1,7 are conjugate.  Realify s=1:
# v_j=(cos(pi*j/4), sin(pi*j/4)).
v=[]
for j in range(m):
    v.append(sp.Matrix([sp.cos(sp.pi*j/4),sp.sin(sp.pi*j/4)]))
oddvec=sp.zeros(2,1)
for j in range(m):
    oddvec += b[j]*v[j]
assert all(sp.simplify(x)==0 for x in oddvec)

# Z_a=sum_{j!=0}[-a_j v_j,a_j v_j].
# Here a2=0 and v1=(1,1)/sqrt2, v3=(-1,1)/sqrt2.
# Solving t v0 + c1 v1+c3 v3=0 forces c3=-c1,
# c1=-t/sqrt2.  The box bounds |c1|,|c3|<=1/4 give t<=sqrt2/4.
assert v[0] == sp.Matrix([1,0])
assert v[1] == sp.Matrix([rt2/2,rt2/2])
assert v[3] == sp.Matrix([-rt2/2,rt2/2])
rho=rt2/4
c1=-rho/rt2
c3=rho/rt2
assert abs(c1)==sp.Rational(1,4)
assert abs(c3)==sp.Rational(1,4)
zcheck=sp.simplify(rho*v[0]+c1*v[1]+c3*v[3])
assert all(sp.simplify(x)==0 for x in zcheck)
assert sp.simplify(rho-even_opt_a0)<0

mu0_from_two_scale=sp.simplify((even_opt_a0+rho)/2)
assert sp.simplify(mu0_from_two_scale-mu[0])==0
theta=sp.simplify(1/mu0_from_two_scale)
assert sp.simplify(theta-(8-4*rt2))==0

print("R20 I0100 p=17 dyadic-zonotope exact self-check")
print("p =",p,"n =",n,"m =",m,"S =",S)
print("a =",a)
print("b =",b)
print("even_opt_a0 =",even_opt_a0)
print("odd_zonotope_radius_rho =",rho)
print("rho_less_than_even_opt =",bool(sp.N(rho-even_opt_a0)<0))
print("mu0_two_scale =",mu0_from_two_scale)
print("theta =",theta)
print("theta_numeric =",sp.N(theta,30))
print("PASS")
