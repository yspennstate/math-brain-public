import sympy as sp

# Symbolic exact contact-jump algebra.
lam, mu_u, L, p, q, M, mu_b, vc, vb = sp.symbols(
    "lam mu_u L p q M mu_b vc vb", positive=True
)
mu_c = mu_u + L*p
Au = 1-lam*mu_u
Ac = 1-lam*mu_c
Ab = 1-lam*mu_b

W0 = lam*vb/(2*Ab*Au)
Wc = lam*vc/(2*Ac*Au)
W1 = lam*vb/(2*Ab*Ac)

J_raw = sp.factor(
    p*(Wc-W0)
    + q*(W1-W0)
    + M*(1/Ac-1/Au)
)
H = sp.expand(Ab*(vc+2*L*M)-vb*(Ac-lam*L*q))
J_factored = sp.factor(lam*p*H/(2*Au*Ac*Ab))
assert sp.factor(J_raw-J_factored) == 0
print("SYMBOLIC_JUMP_FACTORIZATION_PASS")

# Critical-load endpoint identity.
m, Sb, Nb, H0 = sp.symbols("m Sb Nb H0", positive=True)
# At lambda=1/m: Ab=Nb/m and Ac-(Lq)/m=L Sb/m.
Hcrit = sp.factor((Nb/m)*(H0+vb) - vb*(L*Sb/m))
target = sp.factor((Nb*H0 + vb*(Nb-L*Sb))/m)
assert sp.factor(Hcrit-target) == 0
print("CRITICAL_LOAD_ENDPOINT_IDENTITY_PASS")

def moments(xs, ps, t):
    mt = sp.factor(sum(pi*min(xi,t) for pi,xi in zip(ps,xs)))
    vt = sp.factor(sum(pi*min(xi,t)**2 for pi,xi in zip(ps,xs)))
    return mt,vt

def contact_jump(xs, ps, lam0, u, c, b, L0):
    mu_u0, _ = moments(xs,ps,u)
    mu_c0, vc0 = moments(xs,ps,c)
    mu_b0, vb0 = moments(xs,ps,b)
    p0 = sp.factor(sum(pi for pi,xi in zip(ps,xs) if u < xi <= c))
    q0 = sp.factor(sum(pi for pi,xi in zip(ps,xs) if c < xi <= b))
    M0 = sp.factor(sum(pi*xi for pi,xi in zip(ps,xs) if c < xi <= b))
    assert sp.factor(mu_c0-mu_u0-L0*p0) == 0
    Au0,Ac0,Ab0 = 1-lam0*mu_u0,1-lam0*mu_c0,1-lam0*mu_b0
    H0v = sp.factor(Ab0*(vc0+2*L0*M0)-vb0*(Ac0-lam0*L0*q0))
    return sp.factor(lam0*p0*H0v/(2*Au0*Ac0*Ab0))

# Previous exact four-point obstruction.
ps1=[sp.Rational(1,3),sp.Rational(1,12),sp.Rational(1,2),sp.Rational(1,12)]
xs1=[sp.Rational(1),sp.Rational(5,2),sp.Rational(7,2),sp.Rational(17,2)]
J1=contact_jump(xs1,ps1,sp.Rational(1,10),sp.Rational(0),sp.Rational(1),sp.Rational(7,2),sp.Rational(3))
assert J1 == sp.Rational(65,712)
print("FOURPOINT_CONTACT_JUMP_1", J1)

# Independent second exact contact family.
ps2=[sp.Rational(8,23),sp.Rational(7,23),sp.Rational(6,23),sp.Rational(2,23)]
xs2=[sp.Rational(1),sp.Rational(5,2),sp.Rational(3),sp.Rational(181,16)]
mean2=sp.factor(sum(pi*xi for pi,xi in zip(ps2,xs2)))
assert mean2 == sp.Rational(23,8)
lam2=sp.Rational(8,69)  # rho = 1/3
assert sp.factor(lam2*mean2) == sp.Rational(1,3)
J2=contact_jump(xs2,ps2,lam2,sp.Rational(0),sp.Rational(1),sp.Rational(3),sp.Rational(23,8))
assert J2 == sp.Rational(62092,556991)
print("FOURPOINT_CONTACT_JUMP_2", J2)

# Exact zero-load endpoint decomposition for the two examples.
def survival(xs,ps,x):
    return sp.factor(sum(pi for pi,xi in zip(ps,xs) if xi>x))
def residual(xs,ps,x):
    return sp.factor(sum(pi*(xi-x) for pi,xi in zip(ps,xs) if xi>x))
def integrate_g(xs,ps,c,b,L0):
    pts=[c]+sorted({xi for xi in xs if c<xi<b})+[b]
    total=sp.Rational(0)
    for A,B in zip(pts[:-1],pts[1:]):
        mid=(A+B)/2
        S=survival(xs,ps,mid)
        C=sp.factor(sum(pi*xi for pi,xi in zip(ps,xs) if xi>mid))
        # N(x)=C-S*x on this open support interval.
        total += sp.factor((L0*S-C)*(B-A)+S*(B**2-A**2)/2)
    return sp.factor(total)

for xs,ps,c,b,L0 in [
    (xs1,ps1,sp.Rational(1),sp.Rational(7,2),sp.Rational(3)),
    (xs2,ps2,sp.Rational(1),sp.Rational(3),sp.Rational(23,8)),
]:
    _,vc0=moments(xs,ps,c)
    _,vb0=moments(xs,ps,b)
    M0=sp.factor(sum(pi*xi for pi,xi in zip(ps,xs) if c<xi<=b))
    hz=sp.factor(vc0+2*L0*M0-vb0)
    rhs=sp.factor(2*(integrate_g(xs,ps,c,b,L0)+b*(residual(xs,ps,b)-L0*survival(xs,ps,b))))
    assert sp.factor(hz-rhs)==0
    assert hz>=0
print("ZERO_LOAD_DEFICIT_OVERSHOOT_DECOMPOSITION_PASS")

print("ALL_EXACT_CHECKS_PASS")
