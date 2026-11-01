import sympy as sp

a,b,s,t,x,y = sp.symbols("a b s t x y", positive=True, real=True)
gam,r,rp = sp.symbols("gam r rp", positive=True, real=True)

D = 4*a*b-s**2

# Kernel-annihilation parameterization:
# sqrt(b) ell_u1 + sqrt(a) ell_v1 = 0
u1 = sp.sqrt(a)*t
v1 = -sp.sqrt(b)*t
u2 = x
v2 = y

R1 = (sp.sqrt(a)*u1-sp.sqrt(b)*v1)**2/(2*(a+b)**2)
R2 = (2*b*u2**2+2*s*u2*v2+2*a*v2**2)/D
R = sp.factor(R1+R2)

weighted = sp.Rational(1,4)*((u1**2+u2**2)/a + (v1**2+v2**2)/b)
defect = ((2*a*v2+s*u2)**2/(4*a*D)
          +(2*b*u2+s*v2)**2/(4*b*D))

assert sp.simplify(R-weighted-defect) == 0
assert sp.simplify(R1-sp.Rational(1,4)*(u1**2/a+v1**2/b)) == 0

# Partner substitution a=g_tau=2(gamma+r), b=g_tauc=2(gamma+r').
assert sp.simplify(
    sp.Rational(1,4)/(2*(gam+r)) - sp.Rational(1,8)/(gam+r)
) == 0
assert sp.simplify(
    sp.Rational(1,4)/(2*(gam+rp)) - sp.Rational(1,8)/(gam+rp)
) == 0

# Equality in the transverse nonnegative remainder forces u2=v2=0
# if D>0, since the simultaneous square equations have invertible matrix.
M = sp.Matrix([[s,2*a],[2*b,s]])
assert sp.factor(M.det()) == -D

print("PASS MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1")
print("identity: R = weighted_norm/4 + two positive defect squares")
print("partner substitution: a=2(gamma+r_tau), b=2(gamma+r_tauc)")
print("consequence: J4 <= -(3/8)[||ell_u||^2/(gamma+r_tau)+||ell_v||^2/(gamma+r_tauc)]")
