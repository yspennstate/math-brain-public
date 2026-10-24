from fractions import Fraction as F
import sympy as sp

# Exact checker for P01/T06 critical-mixture static certificate.
# Parent-bias convention. Two-point offspring {1,D}, high-degree mass p.

def theta_bound(D, p):
    # lambda <= 2/3, so tau=(1+lambda)/(D+lambda) <= 5/(3D+2)
    tau = F(5, 3*D+2)
    return p*tau / (1-p+p*tau)

def delta(D, theta):
    # lower bound on r-lambda r' using a_1-a_D <= 1/(1-lambda)
    # and lambda/(1-lambda)<=2 on lambda<=2/3
    return F(1) - (D-1)*theta + 2*(D-1)*theta*theta

def deriv_margin(D, theta):
    # -ell' >= 2 delta /(r+lambda)^2,
    # with r<=1+(D-1)theta and lambda<=2/3.
    den = F(1) + (D-1)*theta + F(2,3)
    return 2*delta(D,theta)/(den*den)

def pcurve(D):
    # 3/8 + 35/(32D)
    return F(12*D+35, 32*D)

for D in [6,12,245,1000,10000]:
    p0=pcurve(D)
    th=theta_bound(D,p0)
    de=delta(D,th)
    ma=deriv_margin(D,th)
    # closed forms proved symbolically below
    th_expected=F(12*D+35, 12*D*D-D+21)
    de_expected=F(2*(1044*D*D+105*D-637), (12*D*D-D+21)**2)
    ma_expected=F(9*(1044*D*D+105*D-637), 256*D*D*(3*D+2)**2)
    assert th==th_expected
    assert de==de_expected
    assert ma==ma_expected
    print(f"D={D} p0={p0}={float(p0):.12f} Theta={th} delta={de} margin={ma}={float(ma):.12e}")

print("D=245 margin > 1/15000:", deriv_margin(245,theta_bound(245,pcurve(245))) > F(1,15000))
print("D=1000 margin > 1/250000:", deriv_margin(1000,theta_bound(1000,pcurve(1000))) > F(1,250000))

D=sp.symbols('D', integer=True, positive=True)
pcrit=sp.Rational(3,8)
tau=sp.Rational(5,1)/(3*D+2)
th=sp.factor(pcrit*tau/(1-pcrit+pcrit*tau))
de=sp.factor(1-(D-1)*th+2*(D-1)*th**2)
den=sp.factor(1+(D-1)*th+sp.Rational(2,3))
margin=sp.factor(2*de/den**2)
assert sp.simplify(margin - 9*(21*D+11)/(16*(3*D+2)**2))==0
print("critical-margin identity:", margin)

# Verify the pcurve closed forms and positivity for D>=6.
p0=(12*D+35)/(32*D)
th=sp.factor(p0*tau/(1-p0+p0*tau))
quarter_gap=sp.factor(sp.Rational(1,4)-th)
de=sp.factor(1-(D-1)*th+2*(D-1)*th**2)
den=sp.factor(1+(D-1)*th+sp.Rational(2,3))
margin=sp.factor(2*de/den**2)
assert sp.simplify(th-(12*D+35)/(12*D**2-D+21))==0
assert sp.simplify(quarter_gap-(12*D**2-49*D-119)/(4*(12*D**2-D+21)))==0
assert sp.simplify(de-2*(1044*D**2+105*D-637)/(12*D**2-D+21)**2)==0
assert sp.simplify(margin-9*(1044*D**2+105*D-637)/(256*D**2*(3*D+2)**2))==0
# For D>=6, quarter-gap numerator is positive at 6 and increasing thereafter;
# delta numerator is positive already at 1 and increasing.
assert (12*6**2-49*6-119)>0
assert (24*6-49)>0
assert (1044*6**2+105*6-637)>0

# General asymptotic obstruction for p=3/8+a/D under this same static certificate.
a=sp.symbols('a', real=True)
p=sp.Rational(3,8)+a/D
th=sp.factor(p*tau/(1-p+p*tau))
num=sp.factor(sp.together(1-(D-1)*th+2*(D-1)*th**2)).as_numer_denom()[0]
poly=sp.Poly(sp.expand(num),D)
lead=sp.factor(poly.LC())
print("general-delta-leading-coefficient:", lead)
assert sp.simplify(lead + 30*(32*a-35))==0
print("uniform-static asymptotic threshold a*=35/32")
# At threshold the leading term cancels and the remaining numerator is positive quadratic.
numstar=sp.factor(num.subs(a,sp.Rational(35,32)))
assert sp.simplify(numstar - sp.Rational(25,16)*(1044*D**2+105*D-637))==0

print("ALL_EXACT_CHECKS_PASS")
