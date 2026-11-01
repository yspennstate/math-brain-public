from fractions import Fraction
from math import sqrt

d = 6
q = d - 1

# Polynomial coefficients low-to-high.
def add(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else Fraction(0))+(b[i] if i<len(b) else Fraction(0)) for i in range(n)]
def scale(a,c):
    return [c*x for x in a]
def mul_x(a):
    return [Fraction(0)] + a
def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

p=[ [Fraction(1)], [Fraction(0),Fraction(1)] ]
for r in range(1,4):
    nxt = add(scale(mul_x(p[r]), Fraction(d,q)), scale(p[r-1], Fraction(-1,q)))
    p.append(trim(nxt))

assert p[3] == [Fraction(0),Fraction(-11,25),Fraction(0),Fraction(36,25)]
assert p[4] == [Fraction(1,25),Fraction(0),Fraction(-96,125),Fraction(0),Fraction(216,125)]

def peval(poly,x):
    out=Fraction(0)
    powx=Fraction(1)
    for c in poly:
        out += c*powx
        powx *= x
    return out

D3=d*q**2
D4=d*q**3
D=D3+D4
w3=Fraction(D3,D)
w4=Fraction(D4,D)
assert (D3,D4,D)==(150,750,900)
assert (w3,w4)==(Fraction(1,6),Fraction(5,6))

F = add(scale(p[3],w3), scale(p[4],w4))
assert peval(F,Fraction(1)) == 1
assert peval(F,Fraction(-1)) == Fraction(2,3)

# Ramanujan-interval envelope B_{d,r}=q^{-r/2}[2+(d-2)(r+1)]/d.
# For d=6: B3 = 3/(5 sqrt(5)), B4 = 11/75.
# Weighted bulk envelope = 1/(10 sqrt(5)) + 11/90 < 2/3.
lhs_sq = Fraction(1,500)
rhs_sq = Fraction(49,90)**2
assert lhs_sq < rhs_sq

def shell_counts(k):
    out={k:q**k}
    for a in range(1,k):
        out[k-2*a]=(q-1)*q**(k-a-1)
    out[-k]=1
    assert sum(out.values()) == d*q**(k-1)
    return out

c3=shell_counts(3)
c4=shell_counts(4)
assert c3 == {3:125,1:20,-1:4,-3:1}
assert c4 == {4:625,2:100,0:20,-2:4,-4:1}

combined={}
for z,c in c3.items(): combined[z]=combined.get(z,0)+c
for z,c in c4.items(): combined[z]=combined.get(z,0)+c
assert sum(combined.values())==D

v=Fraction(sum(z*c for z,c in combined.items()),D)
m2=Fraction(sum(z*z*c for z,c in combined.items()),D)
tau2=m2/(v**3)
assert v == Fraction(769,225)
assert m2 == Fraction(1159,90)
assert tau2 == Fraction(293371875,909513218)

assert q**4 == 625
assert D-1 == 899
assert q**4 < D-1

print("p3 =", p[3])
print("p4 =", p[4])
print("D3,D4,D =", D3,D4,D)
print("weights =", w3,w4)
print("F(-1) =", peval(F,Fraction(-1)))
print("bulk_envelope = 1/(10*sqrt(5)) + 11/90 =", 1/(10*sqrt(5))+11/90)
print("bulk_envelope < 2/3 = PASS")
print("combined_radial_counts =", dict(sorted(combined.items())))
print("v =", v)
print("M2 =", m2)
print("tau^2 =", tau2)
print("profile_coefficient =", (float(1/tau2))**0.5)
print("branching =", q**4, "<", D-1)
print("P26_T08_TRIMMED_GREEN_BIPARTITE_SPHERICAL_EXACT_PASS")
