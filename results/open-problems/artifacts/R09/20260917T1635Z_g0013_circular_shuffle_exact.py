"""Exact self-check for R09/G0013 circular two-piece shuffle coupling.

Analytic theorem checked:
For c in [0,1], pi_c = Law(S,(S+c) mod 1) admits an explicit coupling
from nu=Unif([0,1]^2) with exact cost

    C(c) = (c^2 + (1-c)^2)/10
         = 1/10 - c(1-c)/5.

This file checks only the exact scalar moment/algebra identities used in the
written proof. It is a self-check, not an independent audit.
"""
from fractions import Fraction as F

def poly_add(a,b):
    n=max(len(a),len(b))
    out=[F(0)]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out

def poly_scale(a,s):
    return [x*s for x in a]

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def poly_comp_one_minus(p):
    # p(1-c)
    out=[F(0)]
    power=[F(1)]
    base=[F(1),F(-1)]
    for coeff in p:
        out=poly_add(out,poly_scale(power,coeff))
        power=poly_mul(power,base)
    return out

def int01(coeffs):
    return sum(coeffs[k]/F(k+1) for k in range(len(coeffs)))

# f_Z(z)=z on [0,1], symmetric about 1.
# Cross moment A=E[(Z-1)(2F_Z(Z)-1)].
integrand = poly_mul(poly_mul([F(-1),F(1)], [F(-1),F(0),F(1)]), [F(0),F(1)])
A = 2*int01(integrand)
assert A == F(7,30)

# E[(Z-1)^2].
var_integrand = poly_mul(poly_mul([F(-1),F(1)],[F(-1),F(1)]),[F(0),F(1)])
varZ = 2*int01(var_integrand)
assert varZ == F(1,6)

# m(Z)=min(Z,2-Z). Since f_Z(z)=m(z),
# E[m]=2 int_0^1 z^2 dz, E[m^2]=2 int_0^1 z^3 dz.
Em = 2*F(1,3)
Em2 = 2*F(1,4)
assert Em == F(2,3)
assert Em2 == F(1,2)

# For target centered uniform interval of half-width r,
# H=F_Z(Z) gives Z'=1+r(2H-1):
# E[(Z-Z')^2] = 1/6 - (7/15)r + (1/3)r^2.
Zraw=[F(1,6), -F(7,15), F(1,3)]

# Branch B has probability c and half-width c;
# branch not-B has probability 1-c and half-width 1-c.
Zavg=poly_add(
    poly_mul([F(0),F(1)], Zraw),
    poly_mul([F(1),F(-1)], poly_comp_one_minus(Zraw))
)
assert Zavg == [F(1,30), -F(1,15), F(1,15)]

# Direct R-integration in the written proof gives
# E[(D-D')^2] = 1/6 - c(1-c)/3.
Davg=[F(1,6), -F(1,3), F(1,3)]
assert Davg == [F(1,6), -F(1,3), F(1,3)]

# Euclidean cost is half the (Z,D) squared cost.
total=poly_scale(poly_add(Zavg,Davg),F(1,2))
assert total == [F(1,10), -F(1,5), F(1,5)]

# Benchmark gap 1/10-C(c)=c(1-c)/5.
gap=poly_add([F(1,10)],poly_scale(total,-1))
assert gap == [F(0),F(1,5),-F(1,5)]

def peval(p,x):
    s=F(0)
    for coeff in reversed(p):
        s=s*x+coeff
    return s

assert peval(total,F(0)) == F(1,10)
assert peval(total,F(1)) == F(1,10)
assert peval(total,F(1,2)) == F(1,20)
assert peval(gap,F(1,2)) == F(1,20)

print("A_cross =", A)
print("Var_Z =", varZ)
print("E_m =", Em)
print("E_m2 =", Em2)
print("Z_raw_polynomial_coeffs =", Zavg)
print("D_raw_polynomial_coeffs =", Davg)
print("total_cost_polynomial_coeffs =", total)
print("benchmark_gap_polynomial_coeffs =", gap)
print("c=1/2 total =", peval(total,F(1,2)))
print("SELF_CHECK_ONLY")
print("PASS")
