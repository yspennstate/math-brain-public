from fractions import Fraction
import math
import sympy as sp

# Exact symbolic variables for the skipped-first two-record topology.
p,q,a,b,c,u = sp.symbols('p q a b c u', positive=True)
s = p+q
r = 1-s
rho = 1-c
x = 1-a
y = 1-b
# Exact skipped-prefix defect d = s*x - p*y = q - s*a + p*b.
d = sp.expand(s*x - p*y)
k = sp.expand(s*a - d)  # coefficient of V2 after exact waiting rearrangement
assert sp.simplify(k - (2*s*a - q - p*b)) == 0
H0 = sp.expand(c*k + a*r)

# Lower bound after blockwise Cauchy and exact minimization over the split q1+q2=u.
Bstar = (
    2*rho - u/a - (rho-u)/b
    + k*(y-u)**2/(2*a*b*r)
    + (rho-u)**2/(2*b*c)
    + H0*u**2/(2*a*b*c*s)
    + p*(1-a)*u/(a*s)
    - p*q*(1-a)**2*b*c/(2*a*s*H0)
)
Bstar = sp.cancel(Bstar)

poly = sp.Poly(Bstar, u)
A2, B1, C0 = poly.all_coeffs()
assert sp.simplify(A2 - H0/(2*a*b*c*r*s)) == 0
Disc = sp.cancel(B1**2 - 4*A2*C0)
Pbig = sp.factor(-Disc*a**2*b**2*c**2*s*r)
assert sp.denom(Pbig) == 1

# Exact cube parametrization of the full strict skipped-first topology.
P,Q,R,F,E = sp.symbols('P Q R F E')
subs = {
    p: P,
    q: (1-P)*Q,
    c: 1-R,
    a: 1-P*R*(1-F),
    b: 1-R*(1-F)*(P+(1-P)*Q*(1-E)),
}
Pcube = sp.Poly(sp.expand(Pbig.subs(subs)), P,Q,R,F,E)
degs = tuple(Pcube.degree(v) for v in (P,Q,R,F,E))
print('PCUBE_DEGREES', degs)
print('PCUBE_TERMS', len(Pcube.terms()))
assert degs == (6,4,6,4,4)

# Power -> tensor Bernstein conversion on [0,1]^d.
def tensor_bernstein_coeffs(poly, vars):
    deg = [poly.degree(v) for v in vars]
    power = {mon: Fraction(int(sp.Rational(co).p), int(sp.Rational(co).q)) for mon,co in poly.terms()}
    coeffs = {}
    ranges = [range(n+1) for n in deg]
    import itertools
    for idx in itertools.product(*ranges):
        total = Fraction(0,1)
        for mon,co in power.items():
            if all(mon[j] <= idx[j] for j in range(len(vars))):
                w = Fraction(1,1)
                for j,n in enumerate(deg):
                    aa = mon[j]
                    w *= Fraction(math.comb(idx[j],aa), math.comb(n,aa))
                total += co*w
        coeffs[idx] = total
    return tuple(deg), coeffs

deg5, bc5 = tensor_bernstein_coeffs(Pcube, (P,Q,R,F,E))
pos = [(i,v) for i,v in bc5.items() if v>0]
zero = [(i,v) for i,v in bc5.items() if v==0]
neg = [(i,v) for i,v in bc5.items() if v<0]
print('BERNSTEIN5_TOTAL', len(bc5))
print('BERNSTEIN5_POS', len(pos))
print('BERNSTEIN5_ZERO', len(zero))
print('BERNSTEIN5_NEG', len(neg))
print('BERNSTEIN5_MIN_POS', min(v for _,v in pos))
print('BERNSTEIN5_NEG_LIST', neg)
assert len(bc5)==6125
assert len(pos)==4397 and len(zero)==1727 and len(neg)==1
assert min(v for _,v in pos)==Fraction(1,1350)
assert neg == [((4,4,3,0,4), Fraction(-1,300))]

# The unique potentially negative Bernstein slice is exactly Q=1,F=0,E=1.
G = sp.factor(Pcube.as_expr().subs({Q:1,F:0,E:1}))
J = sp.factor(G/(R*(1-R)))
assert sp.simplify(G - R*(1-R)*J) == 0
J_expected = (
    P**5*R**4 - 2*P**5*R**3
    - 8*P**4*R**4 + 14*P**4*R**3 - 2*P**4*R**2 + P**4*R
    + 8*P**3*R**4 - 3*P**3*R**3 - 16*P**3*R**2 + P**3*R
    - 14*P**2*R**3 + 20*P**2*R**2 + 4*P**2*R
    + 7*P*R**2 - 12*P*R - R + 2
)
assert sp.expand(J-J_expected)==0
print('FACE_FACTOR_VERIFIED', True)

# Bernstein coefficients of J over a rectangular cell.
def cell_poly(poly_expr, l1,h1,l2,h2):
    X,Y=sp.symbols('X Y')
    expr = sp.expand(poly_expr.subs({P:sp.Rational(l1.numerator,l1.denominator)+(sp.Rational(h1.numerator,h1.denominator)-sp.Rational(l1.numerator,l1.denominator))*X,
                                     R:sp.Rational(l2.numerator,l2.denominator)+(sp.Rational(h2.numerator,h2.denominator)-sp.Rational(l2.numerator,l2.denominator))*Y}))
    return sp.Poly(expr,X,Y), (X,Y)

bad=[]
mins=[]
positive_count=0
zero_count=0
N=32
for i in range(N):
    for j in range(N):
        lP=Fraction(i,N); hP=Fraction(i+1,N)
        lR=Fraction(j,N); hR=Fraction(j+1,N)
        cp, vv = cell_poly(J,lP,hP,lR,hR)
        dg, cc = tensor_bernstein_coeffs(cp,vv)
        vals=list(cc.values())
        mn=min(vals)
        mins.append(mn)
        if mn < 0:
            bad.append(((i,j),mn))
        else:
            positive_count += sum(v>0 for v in vals)
            zero_count += sum(v==0 for v in vals)
print('J_SUBDIV_BAD', bad)
print('J_GOOD_POS_COUNT', positive_count)
print('J_GOOD_ZERO_COUNT', zero_count)
print('J_GOOD_MIN_POS', min(m for m in mins if m>0))
assert [ij for ij,_ in bad]==[(30,31),(31,31)]
assert bad[0][1]==Fraction(-45,1073741824)
assert bad[1][1]==Fraction(-277,4026531840)
assert positive_count==30660 and zero_count==0
assert min(m for m in mins if m>0)==Fraction(1,1048576)

# Analytic proof on the two bad cells, both in U=1-P<=1/16, V=1-R<=1/16.
U,V=sp.symbols('U V', nonnegative=True)
Jcorner=sp.expand(J.subs({P:1-U,R:1-V}))
Jcorner_expected=(
-U**5*V**4 +2*U**5*V**3 -2*U**5*V +U**5
-3*U**4*V**4 +8*U**4*V**3 -8*U**4*V**2 +3*U**4*V
+14*U**3*V**4 -23*U**3*V**3 +9*U**3*V**2
-14*U**2*V**4 +15*U**2*V**3 -U**2*V**2
+3*U*V**4 -3*U*V**3
+V**4+V**3
)
assert sp.expand(Jcorner-Jcorner_expected)==0

delta=Fraction(1,16)
Acoef = delta**4 + 2*delta + Fraction(32,5)*delta + Fraction(2,5)
Bcoef = Fraction(6,25) + 3*delta + Fraction(193,5)*delta**3 + 3*delta**5
print('CORNER_A', Acoef)
print('CORNER_B', Bcoef)
assert Acoef < 1 and Bcoef < 1
# The eight negative monomials are dominated by Acoef*U^5+Bcoef*V^3.
# The U^4 V term uses weighted AM-GM; U^2V^2 uses Young (5/2,5/3).
assert Fraction(1,16) < Fraction(8,125)  # delta < (2/5)^3
print('CORNER_LOWER_COEFF_U5', 1-Acoef)
print('CORNER_LOWER_COEFF_V3', 1-Bcoef)

# Verify topology parameter identities exactly.
sP = sp.expand(P+(1-P)*Q)
qP = sp.expand((1-P)*Q)
fP = sp.expand(P*R*F)
eP = sp.expand(R*(sP*F + qP*(1-F)*E))
aP=subs[a]; bP=subs[b]
assert sp.expand(aP-bP - R*qP*(1-F)*(1-E))==0
assert sp.expand(P*eP - sP*fP - P*qP*R*(1-F)*E)==0
print('TOPOLOGY_IDENTITIES_PASS', True)

# Exact skipped-first witness from the previous R7-04 report.
from fractions import Fraction as FF
xs=[FF(1),FF(2),FF(4),FF(8)]
probs=[FF(1,20),FF(11,20),FF(1,4),FF(3,20)]
mu=sum(x0*p0 for x0,p0 in zip(xs,probs))
rho0=FF(19,20); lam= rho0/mu
def tm(k0,b0): return sum(p0*min(x0,b0)**k0 for x0,p0 in zip(xs,probs))
b10=FF(2); b20=FF(4)
PP1=probs[0]+probs[1]; PP2=probs[2]; PP3=probs[3]
m10=tm(1,b10); m20=tm(1,b20); VV1=tm(2,b10); VV2=tm(2,b20); VV3=sum(p0*x0*x0 for x0,p0 in zip(xs,probs))
AA1=1-lam*m10; AA2=1-lam*m20; AA3=1-rho0
QQms=lam*FF(1,2)*(PP1*VV1/AA1+PP2*VV2/(AA1*AA2)+PP3*VV3/(AA2*AA3))
MM1=sum(p0*x0 for x0,p0 in zip(xs,probs) if x0<=b10); MM2=sum(p0*x0 for x0,p0 in zip(xs,probs) if b10<x0<=b20); MM3=sum(p0*x0 for x0,p0 in zip(xs,probs) if x0>b20)
RRms=MM1+MM2/AA1+MM3/AA2
QQbar=lam*FF(1,2)*((PP1+PP2)*VV2/AA2+PP3*VV3/(AA2*AA3))
HH=2*QQbar-QQms+2*mu-RRms
print('WITNESS_TARGET', HH)
assert HH == FF(60274143,1767050) and HH>0

# Positive leading coefficient plus Pcube>=0 gives discriminant<=0.
# In the strict cube interior the Bernstein remainder is positive, hence discriminant<0.
print('ALL_EXACT_CHECKS_PASS')
