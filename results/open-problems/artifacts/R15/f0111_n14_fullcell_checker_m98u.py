from fractions import Fraction
from math import factorial
import sympy as sp

D,S,U,V=sp.symbols('D S U V')
z=1+S
a=1+D; b=1-D
k=sp.factor(2*z*(1-z**2)/((1-D**2)*(D+3*z)))
y=sp.factor((D+z)*(1-z)*(1-D-2*z)/(2*(1-D)*(D+3*z)))
x=sp.factor(1-k-y)
K2=sp.factor((D+z)*(1-z**2)/(D+3*z))
tJ=sp.factor((1-z)**2-K2)
tK=sp.factor((1+z)**2-K2)
R=sp.factor(-2*(D+z)*(1-z**2)*(D**2*z+3*D*z**2+D+3*z**3)/(D+3*z)**2)
AJ=sp.factor(1+3*tJ**2/R)
AK=sp.factor(1+3*tK**2/R)
AJK=sp.factor(1+3*tJ*tK/R)
LK=sp.factor(y*AK)
QK=sp.factor(-k*AK)
UK=sp.factor(-29*y/k)

s0=sp.Rational(217,50000)
dhi=sp.Rational(4,7)
dl0=sp.Rational(5689,10000)
dline=dl0-sp.Rational(11,50)*S


def bernstein_values_on_slant(P):
    sv=s0*V
    lo=dl0-sp.Rational(11,50)*sv
    dv=lo+(dhi-lo)*U
    Q=sp.Poly(sp.expand(P.subs({D:dv,S:sv})),U,V,domain=sp.QQ)
    m=Q.degree(U); n=Q.degree(V)
    coeff={(i,j):Q.coeff_monomial(U**i*V**j) for i in range(m+1) for j in range(n+1)}
    out=[]
    for p in range(m+1):
        for q in range(n+1):
            val=sp.Rational(0)
            for i in range(p+1):
                for j in range(q+1):
                    val += coeff[i,j]*sp.binomial(p,i)/sp.binomial(m,i)*sp.binomial(q,j)/sp.binomial(n,j)
            out.append(sp.factor(val))
    return Q,out


def positive_rational_on_slant(name, expr):
    num,den=map(sp.factor,sp.together(sp.cancel(expr)).as_numer_denom())
    _,bn=bernstein_values_on_slant(num)
    _,bd=bernstein_values_on_slant(den)
    if min(bd)>0:
        assert min(bn)>0, (name,'numerator not positive',min(bn))
        margin=min(bn); dmargin=min(bd)
    elif max(bd)<0:
        assert max(bn)<0, (name,'numerator not negative with negative denominator',max(bn))
        margin=-max(bn); dmargin=-max(bd)
    else:
        raise AssertionError((name,'denominator Bernstein sign not fixed',min(bd),max(bd)))
    print(f"PASS {name}: {len(bn)} numerator Bernstein coeffs, strict sign; raw margin={margin}; denominator margin={dmargin}")

line_gap=sp.factor(14-UK.subs(D,dline))
positive_rational_on_slant('U_K(dline(S),S) < 14', line_gap)

kap=sp.factor(-k/S)
SS=sp.factor(-29*S/k)
Tcap=sp.factor(y*(14-LK))
Umax=sp.factor((b**2/a**2*Tcap-x+AJ*x**2)/2)
Vmax=sp.factor((Tcap-y+AK*y**2)/2)
Wmax=sp.factor((b/a*Tcap+AJK*x*y))

bounds={
    '3/2 < -k/S': kap-sp.Rational(3,2),
    '-k/S < 167/100': sp.Rational(167,100)-kap,
    '0 < (x-1)/S': (x-1)/S,
    '(x-1)/S < 7/8': (sp.Rational(7,8)*S-(x-1))/S,
    '0 < y/S': y/S,
    'y/S < 13/16': (sp.Rational(13,16)*S-y)/S,
    '0 < (A_J-1)/S': (AJ-1)/S,
    '(A_J-1)/S < 7/8': (sp.Rational(7,8)*S-(AJ-1))/S,
    '0 < A_JK': AJK,
    'A_JK < 5': 5-AJK,
    'Umax < S': (S-Umax)/S,
    'Vmax < 11S/2': (sp.Rational(11,2)*S-Vmax)/S,
    'Wmax < 17S/4': (sp.Rational(17,4)*S-Wmax)/S,
    'Q_K > 144/5': QK-sp.Rational(144,5),
    'S(q)*s < 18': 18-SS,
}
for name,expr in bounds.items():
    positive_rational_on_slant(name,expr)

c=sp.Rational(50)
r=1-c*S
ell=sp.factor(x-r)
e=sp.factor(r*(1-AJ*r))
T=Tcap
lower=sp.factor(S*(x-2*ell)/b)
base=sp.factor((b/a)*T+AJK*ell*y)
Delta=sp.factor(lower-base)
Sq=sp.factor(Delta**2-e*T)

Dn,Dd=map(sp.factor,sp.together(Delta).as_numer_denom())
Sn,Sd=map(sp.factor,sp.together(Sq).as_numer_denom())
assert sp.expand(Dn).subs(S,0)==0
assert sp.expand(Sn).subs(S,0)==0
assert sp.diff(sp.expand(Sn),S).subs(S,0)==0
PD=sp.factor(sp.cancel(Dn/S))
PS=sp.factor(sp.cancel(Sn/S**2))
_,bd=bernstein_values_on_slant(PD)
_,bs=bernstein_values_on_slant(PS)
assert max(bd)<0
assert min(bs)>0
print(f"PASS c=50 Delta>0: {len(bd)} Bernstein coeffs, max={max(bd)}")
print(f"PASS c=50 Delta^2-e*Tcap>0: {len(bs)} Bernstein coeffs, min={min(bs)}")


def exp_lower(q,n):
    q=Fraction(q)
    return sum((q**j)/factorial(j) for j in range(n+1))


def exp_upper(q,n):
    q=Fraction(q)
    partial=exp_lower(q,n)
    first=(q**(n+1))/factorial(n+1)
    ratio=q/Fraction(n+2,1)
    assert ratio < 1
    return partial + first/(1-ratio)


def prove_log_upper(x,a,n=24):
    assert exp_lower(a,n) > Fraction(x)


def prove_log_lower(x,a,n=20):
    assert exp_upper(a,n) < Fraction(x)

c0=Fraction(25000,217)
s0F=Fraction(217,50000)
A0=1/(s0F*(c0+Fraction(167,100)))
A50=1/(s0F*(Fraction(50)+Fraction(167,100)))
M0=Fraction(18)*(c0+1)
Larg=Fraction(18,1)/s0F

prove_log_upper(Larg,Fraction(8331,1000),24)
prove_log_lower(A0,Fraction(6787,10000),14)
prove_log_upper(M0,Fraction(3823,500),24)
prove_log_lower(A50,Fraction(149,100),20)
prove_log_upper(Fraction(918),Fraction(7),20)
prove_log_lower(Fraction(400,201),Fraction(2,3),14)
prove_log_upper(Fraction(500000,217),Fraction(31,4),24)
print('PASS all exact logarithm bounds via rational Taylor enclosures')

alph=Fraction(167,100)
b0=Fraction(17,576)
d0=Fraction(11,41472)
Lup=Fraction(8331,1000)
M0up=Fraction(3823,500)

g50=Fraction(50)*Fraction(149,100)-alph*Lup-Lup*(Fraction(7)+b0)-d0
gc0=c0*Fraction(6787,10000)-alph*Lup-Lup*(M0up+b0)-d0
deriv=Fraction(6787,10000)-alph/c0-(M0up+b0)/c0-Lup/(c0+1)
caseB_lower=Fraction(2,3)-alph*s0F*Lup
caseB_upper=s0F*(Fraction(31,4)**2+b0*Fraction(31,4)+d0)
assert g50>0 and gc0>0 and deriv>0 and caseB_lower>caseB_upper
print('PASS case-A endpoint gap c=50:',g50)
print('PASS case-A endpoint gap c=c0:',gc0)
print('PASS case-A derivative lower bound for c>=c0:',deriv)
print('PASS case-B entropy-energy gap:',caseB_lower-caseB_upper)
print('ALL_EXACT_CHECKS_PASS')