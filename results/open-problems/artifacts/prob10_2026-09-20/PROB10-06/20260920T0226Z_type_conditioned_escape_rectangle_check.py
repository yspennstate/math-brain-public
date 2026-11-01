from fractions import Fraction as F
import itertools
import math
import sympy as sp

lam = sp.symbols("lam")
p = sp.symbols("p")
L0 = sp.Rational(1847,1000)
L1 = sp.Rational(1851,1000)
R0 = sp.Rational(1979,200)

def bernstein_coeffs(poly, var):
    P = sp.Poly(sp.expand(poly), var, domain=sp.QQ)
    n = P.degree()
    a = [P.nth(k) for k in range(n+1)]
    out = []
    for j in range(n+1):
        s = sp.Rational(0)
        for k in range(j+1):
            s += a[k] * sp.Rational(math.comb(j,k), math.comb(n,k))
        out.append(sp.factor(s))
    return out

def bernstein_interval(poly, var, a, b):
    t = sp.symbols("_t")
    q = sp.expand(poly.subs(var, a + (b-a)*t))
    return bernstein_coeffs(q, t)

def certify_poly_positive(poly, var, a=sp.Rational(0), b=sp.Rational(1), depth=0, maxdepth=16):
    coeffs = bernstein_interval(poly, var, a, b)
    if min(coeffs) > 0:
        return True, depth, min(coeffs)
    if depth >= maxdepth:
        return False, depth, min(coeffs)
    mid = (a+b)/2
    ok1,d1,m1 = certify_poly_positive(poly,var,a,mid,depth+1,maxdepth)
    if not ok1:
        return False,d1,m1
    ok2,d2,m2 = certify_poly_positive(poly,var,mid,b,depth+1,maxdepth)
    return ok2,max(d1,d2),min(m1,m2)

def certify_rational_positive(expr, var, a, b):
    num, den = [sp.factor(x) for x in sp.together(expr).as_numer_denom()]
    mid = (a+b)/2
    denmid = sp.sign(sp.N(den.subs(var,mid),50))
    assert denmid in (-1,1)
    s = sp.Integer(int(denmid))
    okd,dd,md = certify_poly_positive(sp.expand(s*den),var,a,b)
    okn,dn,mn = certify_poly_positive(sp.expand(s*num),var,a,b)
    return okd and okn, max(dd,dn), min(md,mn)

a = lam-1
b2 = (2-lam)/2
b3 = 3*(2-lam)/(6-lam)
u2 = 2*(3-lam)/(lam+6)
u3 = (3-lam)/3
q2u = 1/(2-lam)
q3u = 4/((2-lam)*(6-lam))
q2l = 9/((3-lam)*(lam+6))
q3l = 1/(3-lam)

def pattern_expr(n,m,upper):
    smin = (n-m)*b2 + m*b3
    smax = (n-m)*u2 + m*u3
    ymin = sp.factor(smin/(a+smin))
    ymax = sp.factor(smax/(a+smax))
    if upper:
        Q = sp.factor(((n-m)*u2*q2u + m*b3*q3u)/((n-m)*u2 + m*b3))
        r = sp.factor((1+a*Q)/(a+smin))
    else:
        Q = sp.factor(((n-m)*b2*q2l + m*u3*q3l)/((n-m)*b2 + m*u3))
        r = sp.factor((1+a*Q)/(a+smax))
    return ymin,ymax,Q,r

# 1) exact monotonicity on the narrow lambda strip:
# y^- and y^+ decrease; upper-pattern r^+ and lower-pattern r^- increase.
monotone_records=[]
for n,upper in [(3,True),(4,False)]:
    for m in range(n+1):
        ymin,ymax,Q,r = pattern_expr(n,m,upper)
        for name,expr,sgn in [("ymin",sp.diff(ymin,lam),-1),
                              ("ymax",sp.diff(ymax,lam),-1),
                              ("r",sp.diff(r,lam),1)]:
            ok,d,mc = certify_rational_positive(sgn*expr,lam,L0,L1)
            assert ok
            monotone_records.append((n,m,upper,name,d,mc))

def endpoint_constants(n, upper):
    out=[]
    for m in range(n+1):
        ymin,ymax,Q,r = pattern_expr(n,m,upper)
        lo = sp.factor(ymin.subs(lam,L1))
        hi = sp.factor(ymax.subs(lam,L0))
        rr = sp.factor(r.subs(lam,L1 if upper else L0))
        assert lo>0 and hi>0 and lo<=hi and rr>0
        out.append((lo,hi,rr))
    return out

Uconst = endpoint_constants(3,True)
Lconst = endpoint_constants(4,False)

def ratio_corner(n,const,bits):
    num=sp.Rational(0); den=sp.Rational(0)
    for m,(lo,hi,r) in enumerate(const):
        x = hi if bits[m] else lo
        prob = sp.binomial(n,m)*p**m*(1-p)**(n-m)
        num += prob*x*r
        den += prob*x
    return sp.factor(num),sp.factor(den)

Ucorners=[ratio_corner(3,Uconst,b) for b in itertools.product([0,1],repeat=4)]
Lcorners=[ratio_corner(4,Lconst,b) for b in itertools.product([0,1],repeat=5)]

# 2) exact all-p certificate:
# for every choice of upper/lower box vertices,
# L1*(U-L) < R0 on p in [0,1].
pair_count=0
max_depth=0
min_bern=None
worst_pair=None
for i,(Nu,Du) in enumerate(Ucorners):
    for j,(Nl,Dl) in enumerate(Lcorners):
        # Du,Dl are positive by construction: weighted averages of positive endpoint x_m.
        poly = sp.factor(R0*Du*Dl - L1*(Nu*Dl-Nl*Du))
        ok,d,mb = certify_poly_positive(poly,p,maxdepth=16)
        assert ok, (i,j,d,mb)
        pair_count += 1
        max_depth=max(max_depth,d)
        if min_bern is None or mb<min_bern:
            min_bern=mb
            worst_pair=(i,j)

assert pair_count == 16*32

# 3) exact comparison with K=5+2sqrt(6).
# Since R0>5, R0 < 5+2sqrt(6) iff (R0-5)^2 < 24.
assert (R0-5)**2 < 24

# The resulting derivative margin on the new strip:
# f(theta)=2+theta-R0 theta(1-theta)
# has minimum 2-(R0-1)^2/(4R0).
fmin = sp.factor(2-(R0-1)**2/(4*R0))
assert fmin > 0
margin = sp.factor(2*fmin/(3+L1)**2)
assert margin > 0

# 4) exact obstruction to the naive scalar finite-depth contraction for central p.
# degree-2 local Lipschitz rho2=lambda/2;
# degree-3 local Lipschitz rho3=12lambda/(6-lambda)^2.
rho2 = sp.factor(L1/2)
rho3 = sp.factor(12*L1/(6-L1)**2)
pcrit = sp.factor((1-rho2)/(rho3-rho2))
assert 0 < pcrit < 1
assert sp.Rational(1,5) < pcrit < sp.Rational(21,100)

print("PROB10-06 exact type-conditioned child-pattern checker")
print("lambda strip =", L0, "to", L1)
print("all monotonicity certificates passed:", len(monotone_records))
print("corner pairs certified:", pair_count)
print("max Bernstein subdivision depth:", max_depth)
print("worst corner pair:", worst_pair)
print("smallest terminal Bernstein coefficient:", min_bern, "~", float(min_bern))
print("uniform lambda*(h2/c2-h3/c3) ceiling =", R0, "~", float(R0))
print("(R0-5)^2 =", (R0-5)**2, "< 24, so R0 < 5+2*sqrt(6)")
print("new-strip numerator margin fmin =", fmin, "~", float(fmin))
print("new-strip derivative margin -ell' >=", margin, "~", float(margin))
print("naive scalar truncation at lambda=L1:")
print(" rho2 =", rho2, "~", float(rho2))
print(" rho3 =", rho3, "~", float(rho3))
print(" mixture contraction requires p < pcrit =", pcrit, "~", float(pcrit))
print("ALL_EXACT_CHECKS_PASS")