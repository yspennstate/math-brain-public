#!/usr/bin/env python3
"""
R20/I0100 exact self-check for the projection-DPP / volume-sampling reformulation.

This is NOT a proof of Randomstrasse Conjecture 26. It verifies at p=17
unbiased projection-volume sampling identities used in the accompanying report,
the composite-DFT second-moment defect, and the exact positive-basis geometry.
All arithmetic is exact in Q(sqrt(2), i).
"""
import itertools
import sympy as sp

p=17
n=(p-1)//2
m=n//2
I=sp.I
rt2=sp.sqrt(2)
zeta=(1+I)/rt2
U=sp.Matrix([[sp.simplify(zeta**(r*c)/sp.sqrt(n)) for c in range(n)] for r in range(n)])

S=[1,4,7]
R=[0]+S
M=U.extract(R,range(n))
b=sp.Matrix([1/sp.sqrt(n)]+[0]*(m-1))

def abs2(z):
    return sp.simplify(sp.expand_complex(z*sp.conjugate(z)))

total=sp.Integer(0)
inc=[sp.Integer(0) for _ in range(n)]
first=[sp.Integer(0) for _ in range(n)]
second=[sp.Integer(0) for _ in range(n)]
norm2=sp.Integer(0)
positive_count=0
positive_mass=sp.Integer(0)
max_positive_atom=sp.Integer(0)

for A in itertools.combinations(range(n),m):
    MA=M.extract(range(m),A)
    det=sp.simplify(MA.det())
    D=abs2(det)
    if D==0:
        continue
    x=MA.inv()*b
    x=[sp.simplify(sp.expand_complex(v)) for v in x]
    assert all(sp.simplify(sp.im(v))==0 for v in x)
    total=sp.simplify(total+D)
    sq=sp.Integer(0)
    for pos,j in enumerate(A):
        v=sp.simplify(sp.re(x[pos]))
        inc[j]=sp.simplify(inc[j]+D)
        first[j]=sp.simplify(first[j]+D*v)
        second[j]=sp.simplify(second[j]+D*v*v)
        sq=sp.simplify(sq+v*v)
    norm2=sp.simplify(norm2+D*sq)

    vals=[sp.simplify(sp.re(v)) for v in x]
    if all(sp.ask(sp.Q.positive(v)) is True for v in vals):
        positive_count += 1
        positive_mass=sp.simplify(positive_mass+D)
        for v in vals:
            if float(sp.N(v,50)) > float(sp.N(max_positive_atom,50)):
                max_positive_atom=v

assert total==1
assert all(sp.simplify(v-sp.Rational(m,n))==0 for v in inc)
assert all(sp.simplify(v-sp.Rational(1,n))==0 for v in first)

# Composite DFT sizes can have singular square minors.  Their missing
# replacement-minor mass makes the generic-position inverse-moment identity a
# strict upper bound.  At p=17 the exact second moment is 35/512.
assert all(sp.simplify(v-sp.Rational(35,512))==0 for v in second)
generic_second_ceiling=sp.Rational(1,2*n)+sp.Rational(1,n*n)
assert all(v <= generic_second_ceiling for v in second)
assert sp.simplify(norm2-n*sp.Rational(35,512))==0

conditional_mean=sp.simplify(sp.Rational(1,n)/sp.Rational(m,n))
conditional_second=sp.simplify(sp.Rational(35,512)/sp.Rational(m,n))
conditional_var=sp.simplify(conditional_second-conditional_mean**2)
assert conditional_mean==sp.Rational(2,n)
assert conditional_second==sp.Rational(35,256)
assert conditional_var==sp.Rational(19,256)

assert positive_count==20
assert sp.simplify(positive_mass-sp.Rational(7,16))==0
assert sp.simplify(max_positive_atom-(sp.Rational(1,4)+rt2/8))==0
theta=sp.simplify(1/max_positive_atom)
assert sp.simplify(theta-(8-4*rt2))==0

print("R20 I0100 p=17 projection-DPP exact self-check")
print("n =",n,"m =",m,"S =",S)
print("DPP_total_mass =",total)
print("all_inclusion_probabilities =",inc)
print("all_unconditional_means =",first)
print("all_unconditional_second_moments =",second)
print("conditional_mean_given_inclusion =",conditional_mean)
print("conditional_second_given_inclusion =",conditional_second)
print("conditional_variance_given_inclusion =",conditional_var)
print("expected_signed_basic_l2_squared =",norm2)
print("positive_basis_count =",positive_count,"of",sp.binomial(n,m))
print("positive_basis_DPP_mass =",positive_mass)
print("largest_positive_atom =",max_positive_atom)
print("theta_from_positive_atom =",theta)
print("PASS")
