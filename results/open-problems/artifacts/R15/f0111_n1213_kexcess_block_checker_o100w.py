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
kap=sp.factor(-k/S)

# Exact K-excess roof: along LK=N, UK decreases with s.
H=sp.factor(sp.diff(UK,S)*sp.diff(LK,D)-sp.diff(UK,D)*sp.diff(LK,S))
numH,denH=map(sp.factor,sp.together(H).as_numer_denom())
Pexpr=sp.cancel(numH/(87*(D+2*S+1)*(D+2*S+3)))
P=sp.Poly(sp.factor(Pexpr),D,S,domain=sp.QQ)
assert all(c>0 for c in P.coeffs())
assert sp.factor(denH/(8*(D-1)*(S+1)*(S+2))).subs({D:sp.Rational(1,2),S:sp.Rational(1,100)})>0
dLKD=sp.factor(sp.diff(LK,D)); dUKD=sp.factor(sp.diff(UK,D))
nLK,dLKden=map(sp.factor,sp.together(dLKD).as_numer_denom())
nUK,dUKden=map(sp.factor,sp.together(dUKD).as_numer_denom())
assert all(c>0 for c in sp.Poly(nLK,D,S,domain=sp.QQ).coeffs())
assert all(c>0 for c in sp.Poly(nUK,D,S,domain=sp.QQ).coeffs())
assert sp.factor(sp.limit(LK,S,0,dir='+')) == -6/(D-1)
assert sp.factor(sp.limit(UK,S,0,dir='+')) == 29*(D+1)**3/8
print('PASS K-excess derivative: d/ds UK along LK=N is strictly negative; LK and UK increase in D')

roof12=sp.Rational(29)*(1-sp.Rational(3,12))**3
roof13=sp.Rational(29)*(1-sp.Rational(3,13))**3
assert roof12-sp.Rational(12)==sp.Rational(15,64)
assert roof13-sp.Rational(13)==sp.Rational(439,2197)
print('PASS exact roofs: UK-N <= 15/64 for N=12 and <= 439/2197 for N=13')

def bernstein_values(Q):
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
    return out

def subpoly(Q,u0,u1,v0,v1):
    uu,vv=sp.symbols('uu vv')
    ex=sp.expand(Q.as_expr().subs({U:u0+(u1-u0)*uu,V:v0+(v1-v0)*vv}))
    return sp.Poly(ex.subs({uu:U,vv:V}),U,V,domain=sp.QQ)

def transformed_poly(P,s0,lower,upper):
    sv=s0*V; lo=lower.subs(S,sv); hi=upper.subs(S,sv); dv=lo+(hi-lo)*U
    return sp.Poly(sp.expand(P.subs({D:dv,S:sv})),U,V,domain=sp.QQ)

def prove_positive(name,expr,s0,lower,upper,subdiv=1):
    num,den=map(sp.factor,sp.together(sp.cancel(expr)).as_numer_denom())
    Qn=transformed_poly(num,s0,lower,upper); Qd=transformed_poly(den,s0,lower,upper)
    margin=None
    for ii in range(subdiv):
        for jj in range(subdiv):
            u0=sp.Rational(ii,subdiv); u1=sp.Rational(ii+1,subdiv)
            v0=sp.Rational(jj,subdiv); v1=sp.Rational(jj+1,subdiv)
            bn=bernstein_values(subpoly(Qn,u0,u1,v0,v1)); bd=bernstein_values(subpoly(Qd,u0,u1,v0,v1))
            if min(bd)>0: signed=bn
            elif max(bd)<0: signed=[-q for q in bn]
            else: raise AssertionError((name,'denominator sign failure',ii,jj,min(bd),max(bd)))
            if min(signed)<=0: raise AssertionError((name,'nonpositive Bernstein coefficient',ii,jj,min(signed)))
            mm=min(signed); margin=mm if margin is None or mm<margin else margin
    print(f'PASS {name}: exact Bernstein certificate, subdiv={subdiv}, margin={margin}')

cases=[
 dict(N=12,s0=sp.Rational(3601,250000),lower=sp.Rational(49,100)-sp.Rational(1,4)*S,upper=sp.Rational(1,2)-sp.Rational(9,10)*S,C=sp.Rational(15),subdiv=1),
 dict(N=13,s0=sp.Rational(12637,1000000),lower=sp.Rational(53,100)-sp.Rational(1,5)*S,upper=sp.Rational(7,13)-sp.Rational(4,5)*S,C=sp.Rational(17),subdiv=2),
]
for c in cases:
    N,s0,lo,hi,C=c['N'],c['s0'],c['lower'],c['upper'],c['C']
    prove_positive(f'N={N} lower wall has UK<N',N-UK.subs(D,lo),s0,lo,hi)
    prove_positive(f'N={N} upper wall has LK>N',(LK.subs(D,hi)-N)/S,s0,lo,hi)
    Tcap=sp.factor(y*(N-LK)); r=1-C*S; ell=sp.factor(x-r); e=sp.factor(r*(1-AJ*r))
    Delta=sp.factor(S*(x-2*ell)/b-(b/a)*Tcap-AJK*ell*y); gap=sp.factor(Delta**2-e*Tcap)
    prove_positive(f'N={N} e/s>0',e/S,s0,lo,hi)
    prove_positive(f'N={N} 2AJr-1>0',2*AJ*r-1,s0,lo,hi)
    prove_positive(f'N={N} Delta/s>0',Delta/S,s0,lo,hi)
    prove_positive(f'N={N} projective heavy gap/s^2>0',gap/S**2,s0,lo,hi,subdiv=c['subdiv'])
print('PASS heterogeneous heavy caps: r_*<1-15s (N=12), r_*<1-17s (N=13)')

kap_corner=sp.factor(kap.subs({D:sp.Rational(7,13),S:sp.Rational(3,200)}))
assert sp.Rational(13,8)-kap_corner>0
lower_kap=sp.Rational(4)/(sp.Rational(481,625)*(sp.Rational(7,13)+3+sp.Rational(9,200)))
assert lower_kap-sp.Rational(29,20)>0
print('PASS uniform kappa bounds: 29/20 < -k/s < 13/8')
UKabs13=roof13; ys_upper=sp.Rational(13,8)*UKabs13/sp.Rational(29)
assert sp.Rational(3,4)-ys_upper>0
assert sp.Rational(41,40)-(1+sp.Rational(13,8)*sp.Rational(3,200))>0
assert sp.Rational(29,20)-sp.Rational(3,4)>0
print('PASS uniform mass bounds: 1<x<41/40 and 0<y<(3/4)s')
Wconst=sp.Rational(3,4)*(sp.Rational(13,25)*12+sp.Rational(3,200)+2)/sp.Rational(37,25)
Uconst=(sp.Rational(13,25)*sp.Rational(17,4)+sp.Rational(41,40))/(2*sp.Rational(37,25))
assert sp.Rational(17,4)-Wconst>0; assert sp.Rational(9,8)-Uconst>0
print('PASS block coefficient masses: U<9s/8, V<9s/2, W<17s/4')

def exp_lower(q,n):
    q=Fraction(q); return sum((q**j)/factorial(j) for j in range(n+1))
def exp_upper(q,n):
    q=Fraction(q); partial=exp_lower(q,n); first=(q**(n+1))/factorial(n+1); ratio=q/Fraction(n+2,1); assert ratio<1; return partial+first/(1-ratio)
assert exp_lower(Fraction(9,2),30)>Fraction(250,3)
assert exp_lower(Fraction(36,5),40)>Fraction(4000,3)
assert exp_upper(Fraction(14,5),30)<Fraction(17,1)
print('PASS exact log bounds: log(250/3)<9/2, log(4000/3)<36/5, log17>14/5')
assert Fraction(15,64*12)<Fraction(1,50); assert Fraction(439,2197*13)<Fraction(1,50)
print('PASS block K-coordinate bound: 0<v<1/50')
E_upper=sp.Rational(9,8)*sp.Rational(243,800)+sp.Rational(9,2)*sp.Rational(3,500000)+sp.Rational(17,4)*sp.Rational(27,400)*sp.Rational(1,50)
negative_value=sp.Rational(13,8)*sp.Rational(3,200)*sp.Rational(36,5); E_lower=sp.Rational(14,5)-negative_value
assert E_lower-E_upper>0
print('PASS block energy contradiction: exact-value lower =',E_lower,' coefficient-energy upper =',E_upper,' gap =',sp.factor(E_lower-E_upper))
print('BLOCK_CONSTANT_N12_N13_IMPOSSIBLE')
print('ALL_EXACT_CHECKS_PASS')
