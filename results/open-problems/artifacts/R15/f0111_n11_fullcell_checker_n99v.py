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

# N=11 scalar roof and rational walls.
s0=sp.Rational(2323,250000)      # 0.009292 > exact s_11 cutoff
lower0=sp.Rational(1791,4000)    # 0.44775
lower_slope=sp.Rational(11,40)   # lower(s)=.44775-.275 s
upper0=sp.Rational(5,11)         # upper(s)=5/11-s
lower=lambda ss: lower0-lower_slope*ss
upper=lambda ss: upper0-ss

# Transform the slanted band to the unit square: s=s0*V and
# delta=lower(s)+(upper(s)-lower(s))*U.
def transformed_poly(P):
    sv=s0*V
    lo=lower(sv)
    hi=upper(sv)
    dv=lo+(hi-lo)*U
    return sp.Poly(sp.expand(P.subs({D:dv,S:sv})),U,V,domain=sp.QQ)

def bernstein_values(Q):
    m=Q.degree(U); n=Q.degree(V)
    coeff={(i,j):Q.coeff_monomial(U**i*V**j)
           for i in range(m+1) for j in range(n+1)}
    out=[]
    for p in range(m+1):
        for q in range(n+1):
            val=sp.Rational(0)
            for i in range(p+1):
                for j in range(q+1):
                    val += (coeff[i,j]*sp.binomial(p,i)/sp.binomial(m,i)
                            *sp.binomial(q,j)/sp.binomial(n,j))
            out.append(sp.factor(val))
    return out

def subpoly(Q,u0,u1,v0,v1):
    uu,vv=sp.symbols('uu vv')
    ex=sp.expand(Q.as_expr().subs({U:u0+(u1-u0)*uu,
                                   V:v0+(v1-v0)*vv}))
    return sp.Poly(ex.subs({uu:U,vv:V}),U,V,domain=sp.QQ)

def prove_positive(name,expr,subdiv=1):
    num,den=map(sp.factor,sp.together(sp.cancel(expr)).as_numer_denom())
    Qn=transformed_poly(num); Qd=transformed_poly(den)
    margin=None; dmargin=None; count=0
    for ii in range(subdiv):
        for jj in range(subdiv):
            u0=sp.Rational(ii,subdiv); u1=sp.Rational(ii+1,subdiv)
            v0=sp.Rational(jj,subdiv); v1=sp.Rational(jj+1,subdiv)
            bn=bernstein_values(subpoly(Qn,u0,u1,v0,v1))
            bd=bernstein_values(subpoly(Qd,u0,u1,v0,v1))
            if min(bd)>0:
                signed=bn; dsigned=bd
            elif max(bd)<0:
                signed=[-q for q in bn]; dsigned=[-q for q in bd]
            else:
                raise AssertionError((name,'denominator sign failure',ii,jj,min(bd),max(bd)))
            if min(signed)<=0:
                raise AssertionError((name,'nonpositive Bernstein coefficient',ii,jj,min(signed)))
            mm=min(signed); dm=min(dsigned)
            margin=mm if margin is None or mm<margin else margin
            dmargin=dm if dmargin is None or dm<dmargin else dmargin
            count += len(signed)
    print(f'PASS {name}: exact Bernstein certificate, subdiv={subdiv}, coeffs={count}, margin={margin}, den_margin={dmargin}')

# The carried scalar theorem says LK and UK increase in delta. These exact
# walls therefore contain every N=11 scalar survivor.
prove_positive('lower wall has U_K<11', 11-UK.subs(D,lower(S)))
prove_positive('upper wall has L_K>11 for s>0', (LK.subs(D,upper(S))-11)/S)

kap=sp.factor(-k/S)
Sq_times_s=sp.factor(-29*S/k)       # physical S(q)*s
Tcap=sp.factor(y*(11-LK))
Umax=sp.factor((b**2/a**2*Tcap-x+AJ*x**2)/2)
Vmax=sp.factor((Tcap-y+AK*y**2)/2)
Wmax=sp.factor((b/a*Tcap+AJK*x*y))

bounds={
    '29/20 < kappa=-k/s': kap-sp.Rational(29,20),
    'kappa < 3/2': sp.Rational(3,2)-kap,
    '0 < (x-1)/s': (x-1)/S,
    '(x-1)/s < 91/100': sp.Rational(91,100)-(x-1)/S,
    'Umax/s < 91/100': sp.Rational(91,100)-Umax/S,
    'Vmax/s < 3': 3-Vmax/S,
    'Wmax/s < 3': 3-Wmax/S,
    'Q_K > 14295/500': QK-sp.Rational(14295,500),
    'S(q)*s < 20': 20-Sq_times_s,
    '(A_J-1)/s > 0': (AJ-1)/S,
}
for name,expr in bounds.items():
    prove_positive(name,expr)

# Heavy-coordinate exclusion with C=25.
C=sp.Rational(25)
r=1-C*S
ell=sp.factor(x-r)
e=sp.factor(r*(1-AJ*r))
Delta=sp.factor(S*(x-2*ell)/b - (b/a)*Tcap - AJK*ell*y)
quartic_gap=sp.factor(Delta**2-e*Tcap)
prove_positive('e/s > 0', e/S)
prove_positive('2 A_J r > 1', 2*AJ*r-1)
prove_positive('Delta/s > 0', Delta/S)
# One 2x2 exact subdivision is enough for the quartic gap; no floating point.
prove_positive('(Delta^2-e*Tcap)/s^2 > 0', quartic_gap/S**2,subdiv=2)

# K-coordinate bound q_j<1/70. From residual positivity,
# S(q) r_j <= 29/Q_K < 14500/14295. Prove that ratio < exp(1/70)
# using a rational Taylor lower bound.
ratio=Fraction(14500,14295)
exp1_70_lower=Fraction(1)+Fraction(1,70)+Fraction(1,2*70*70)
assert exp1_70_lower > ratio
print('PASS q_K-coordinate logarithm bound: 29/Q_K < exp(1/70), margin=',exp1_70_lower-ratio)

# Exact rational exponential bounds for all logarithms used below.
def exp_lower(q,n):
    q=Fraction(q)
    return sum((q**j)/factorial(j) for j in range(n+1))

def exp_upper(q,n):
    q=Fraction(q)
    partial=exp_lower(q,n)
    first=(q**(n+1))/factorial(n+1)
    ratio=q/Fraction(n+2,1)
    assert ratio<1
    return partial+first/(1-ratio)

def log_lower(name,x,a,n=24):
    # certifies log(x)>a
    assert exp_upper(a,n)<Fraction(x), (name,'failed')
    print('PASS',name,': log(x) >',a)

def log_upper(name,x,a,n=30):
    # certifies log(x)<a
    assert exp_lower(a,n)>Fraction(x), (name,'failed')
    print('PASS',name,': log(x) <',a)

s0F=Fraction(2323,250000)
c0=Fraction(122500,2323)  # (49/100)/s0
A25=1/(s0F*(Fraction(25)+Fraction(3,2)))
Ac0=1/(s0F*(c0+Fraction(3,2)))
Bc0=20*(c0+1)
Carg=Fraction(20,1)/s0F
qJarg=Fraction(51,5)/s0F

log_lower('log A25',A25,Fraction(7,5),20)
log_upper('log 520',520,Fraction(63,10),30)
log_lower('log Ac0',Ac0,Fraction(17,25),20)
log_upper('log Bc0',Bc0,Fraction(7),25)
log_upper('log(20/s0)',Carg,Fraction(31,4),30)
log_upper('case-B q_J roof',qJarg,Fraction(71,10),30)
log_lower('log(100/51)',Fraction(100,51),Fraction(2,3),20)
log_lower('log(100/49)',Fraction(100,49),Fraction(7,10),20)
log_upper('log 1020',1020,Fraction(7),25)
log_upper('log(100000/49)',Fraction(100000,49),Fraction(8),30)

# Case A endpoint lower bounds for G(c,s0).
def G_endpoint_lower(c,poslog_lower,M_upper):
    c=Fraction(c); poslog_lower=Fraction(poslog_lower); M_upper=Fraction(M_upper)
    A=Fraction(3,2)+Fraction(91,100)*M_upper+Fraction(3,70)
    return (c-c*c*s0F/2-c*c*c*s0F*s0F/2
            +c*poslog_lower-Fraction(31,4)*A-Fraction(3,4900))

g25=G_endpoint_lower(25,Fraction(7,5),Fraction(63,10))
gc0=G_endpoint_lower(c0,Fraction(17,25),Fraction(7))
assert g25>0 and gc0>0
print('PASS case-A G(25,s0)>0 rational margin=',g25)
print('PASS case-A G(c0,s0)>0 rational margin=',gc0)

# Concavity of G(c,s0) on [25,c0].
concavity_upper=-Fraction(2,109)+Fraction(91,100)*Fraction(31,4)/Fraction(26*26)
assert concavity_upper<0
print('PASS case-A strict concavity upper bound=',concavity_upper)

# For c>=c0, Psi(c)=G(c,(49/100)/c) has positive derivative.
A50_upper=Fraction(3,2)+Fraction(91,100)*7+Fraction(3,70)
psi_derivative_lower=(Fraction(63,100)+Fraction(67,100)
                      -A50_upper/Fraction(50)
                      -Fraction(91,100)*8/Fraction(51))
assert psi_derivative_lower>0
print('PASS case-A Psi derivative rational lower bound=',psi_derivative_lower)

# Case B: if all masses <=51/100, entropy > log(100/51)>2/3.
Q=Fraction(71,10)
caseB_lower=Fraction(2,3)-Fraction(3,2)*s0F*Fraction(31,4)
caseB_upper=s0F*(Fraction(91,100)*Q*Q+Fraction(3,70)*Q+Fraction(3,4900))
assert caseB_lower>caseB_upper
print('PASS case-B entropy-energy gap=',caseB_lower-caseB_upper)

print('ALL_EXACT_CHECKS_PASS')
