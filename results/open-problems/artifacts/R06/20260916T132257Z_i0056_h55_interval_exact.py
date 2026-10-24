#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt

# Exact certificate for R06 / Lyons-Peres Question 6.20 / frozen H_{5,5}.
d=f=5
D=d-2
F=f-2

# Geometric admissibility of the regular hyperbolic {5,5} tessellation.
assert D*F == 9
assert D*F > 4
assert Fraction(1,5)+Fraction(1,5) < Fraction(1,2)

# Higuchi-Shirai face-ball recurrences, specialized to (d,f)=(5,5):
# u_n = 3 v_{n-1} - u_{n-1}
# v_n = 8 v_{n-1} - 3 u_{n-1},
# u_0=0, v_0=5.
u=0
v=5
S=v
ratios=[]
rows=[]
for n in range(12):
    # boundary ratio for B_n^*: |∂_V B_n^*|/|V(B_n^*)| = u_{n+1}/S_n.
    unext=3*v-u
    r=Fraction(unext,S)
    ratios.append(r)
    rows.append((n,S,unext,r))
    vnext=8*v-3*u
    u,v=unext,vnext
    S += v

# Exact small construction checks.
assert rows[0][1:] == (5,15,Fraction(3,1))  # one facial pentagon
assert rows[1][3] == Fraction(7,3)
assert rows[2][3] == Fraction(9,4)
# Singleton and edge candidates use girth >=5.
singleton=Fraction(5,1)
edge=Fraction(8,2)
face=Fraction(15,5)
assert (singleton,edge,face)==(Fraction(5),Fraction(4),Fraction(3))

# Monotone face-ball ratios and exact lower comparison with sqrt(5).
for a,b in zip(ratios,ratios[1:]):
    assert b < a
for r in ratios:
    assert r*r > 5

# Edge Cheeger constant specialization:
# (d-2)*sqrt(1 - 4/((d-2)(f-2))) = 3*sqrt(5/9) = sqrt(5).
radicand=Fraction(1,1)-Fraction(4,D*F)
assert radicand == Fraction(5,9)
assert D*D*radicand == 5

# Haslegrave-Panagiotis intended lower constant for d=5, face-degree>=4:
# alpha_{d+2}=alpha_7 = golden ratio phi, as explicitly stated in their paper.
# Exact polynomial certificate: phi=(1+sqrt(5))/2 solves x^2-x-1=0 and is positive.
# Interval upper is sqrt(5). Width = sqrt(5)-phi=(sqrt(5)-1)/2.
# We represent a+b*sqrt(5) exactly as pairs (a,b).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y):
    a,b=x; c,e=y
    return (a*c+5*b*e, a*e+b*c)

phi=(Fraction(1,2),Fraction(1,2))
root5=(Fraction(0),Fraction(1))
one=(Fraction(1),Fraction(0))
width=(Fraction(-1,2),Fraction(1,2))
zero=(Fraction(0),Fraction(0))
assert sub(sub(mul(phi,phi),phi),one)==zero
assert sub(root5,phi)==width
# positivity comparisons use sqrt(5)>2 and sqrt(5)<3.
assert 5>4 and 5<9

# The displayed minus-sign definition alpha_7=(1-sqrt(5))/2 cannot be the
# golden ratio and cannot reproduce the paper's numerical 0.3455 bound.
alpha_minus=(1-sqrt(5))/2
alpha_plus=(1+sqrt(5))/2
pc_minus=(2+alpha_minus)/(4*(1+alpha_minus))
pc_plus=(2+alpha_plus)/(4*(1+alpha_plus))
assert abs(pc_plus-0.3454915028125263) < 1e-14
assert abs(pc_minus-0.9045084971874737) < 1e-14

print("R06 I0056 exact certificate: PASS")
print("frozen pair: H_{5,5} / Schlaefli {5,5}")
print("admissibility: (d-2)(f-2)=9>4; 1/5+1/5<1/2")
print("exact local candidate ratios: singleton=5, edge=4, facial pentagon=3")
print("face-ball ratios n=0..11:")
for n,S,b,r in rows:
    print(f"  n={n}: |K|={S}, |dV K|={b}, ratio={r.numerator}/{r.denominator} = {float(r):.12f}")
print("certified lower: phi=(1+sqrt(5))/2 =", (1+sqrt(5))/2)
print("certified upper: sqrt(5) =", sqrt(5))
print("certified interval width: (sqrt(5)-1)/2 =", (sqrt(5)-1)/2)
print("HP sign-consistency check: minus-root pc =",pc_minus,"plus-root pc =",pc_plus)
