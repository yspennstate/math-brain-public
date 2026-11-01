#!/usr/bin/env python3
import sympy as sp

q,S,y,u,v = sp.symbols('q S y u v', positive=True, real=True)
sqrt5 = sp.sqrt(5)
alpha = (5-sqrt5)/50
beta  = (5+sqrt5)/50

assert sp.simplify(alpha+beta-sp.Rational(1,5)) == 0
assert sp.simplify(alpha*beta-sp.Rational(1,125)) == 0
assert sp.simplify((beta-alpha)**2-alpha*beta) == 0

# B20 exact obstruction to arbitrary pairwise geometric smoothing.
def Dw(vec, swap=False):
    aa,bb=(beta,alpha) if swap else (alpha,beta)
    return sp.expand(aa*sum(vec[i]*vec[(i+1)%5] for i in range(5))+
                     bb*sum(vec[i]*vec[(i+2)%5] for i in range(5)))

def FP(vec, swap=False):
    r=vec[0]
    return sp.simplify(Dw([1/z for z in vec],swap)-1-r*(Dw(vec,swap)-1))

avec=[sp.Rational(1,4),sp.Rational(1,4),sp.Rational(1),sp.Rational(2),sp.Rational(8)]
bvec=[sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(2),sp.Rational(8)]
obs=sp.factor(FP(bvec)-FP(avec))
assert sp.simplify(obs-3*(9*sqrt5-17)/128)==0
assert sp.N(obs)>0

# B6/B24 reflection-smoothing identities.
# Half-angle form for H1: U=sinh(s/2), V=sinh(t/2),
# A=U sqrt(1+V^2), B=V sqrt(1+U^2).
U,V,A,B=sp.symbols('U V A B', real=True)
Hhalf=(alpha+beta)*(A**2+B**2)+2*(alpha-beta)*A*B-beta*U**2-alpha*V**2
Hhalf=sp.expand(Hhalf.subs({A**2:U**2*(1+V**2),B**2:V**2*(1+U**2)}))
claimed=alpha*U**2*(1+V**2)+beta*V**2*(1+U**2)-2*sp.sqrt(alpha*beta)*A*B+(alpha+beta)*U**2*V**2
claimed=sp.expand(claimed)
assert sp.simplify(Hhalf-claimed)==0

# Palindromic triple functional exact formula.
r,uu,vv=sp.symbols('r uu vv', positive=True, real=True)
X=r+uu; Y=r+vv
D1=alpha*(2*r*X+2*X*Y+Y**2)+beta*(2*r*Y+2*X*Y+X**2)
m=(r+2*X+2*Y)/5
FT=sp.expand(D1-1-r*(m-1))
FT_formula=beta*uu**2+alpha*vv**2+sp.Rational(2,5)*uu*vv+sp.Rational(2,5)*r*(uu+vv)-(1-r)
assert sp.simplify(FT-FT_formula)==0

# Triple lower bound factorization with q=r^(1/4).
triple_lb=sp.Rational(4,25)*(q**-1-q**4)**2+sp.Rational(2,5)*(q**-2-q**8)-(1-q**4)
triple_factor=(1-q)**3*(6*q**7+18*q**6+36*q**5+60*q**4+65*q**3+59*q**2+42*q+14)/(25*q**2)
assert sp.simplify(triple_lb-triple_factor)==0

# Pair functional on the palindromic family: verify B +/- sqrt(5) P D / 25.
U0=sp.symbols('U0', positive=True, real=True)
rr=q**4
XX=rr+U0
YY=1/(q**2*XX)
VV=sp.factor(YY-rr)
pal=[rr,XX,YY,YY,XX]
def Dws(vec, swap=False):
    aa,bb=(beta,alpha) if swap else (alpha,beta)
    return sp.expand(aa*sum(vec[i]*vec[(i+1)%5] for i in range(5))+
                     bb*sum(vec[i]*vec[(i+2)%5] for i in range(5)))
def FPs(vec, swap=False):
    return sp.factor(Dws([1/z for z in vec],swap)-1-rr*(Dws(vec,swap)-1))
SS=sp.factor(U0+VV)
PP=sp.factor(U0*VV)
DD=sp.factor(U0-VV)
cc=q**-2-q**8
BB=sp.factor(cc*SS/sp.Integer(5)+sp.Rational(2,5)*(q**2-q**12)+q**4-1)
assert sp.simplify(FPs(pal,False)-(BB+sqrt5*PP*DD/25))==0
assert sp.simplify(FPs(pal,True) -(BB-sqrt5*PP*DD/25))==0

# Pair functional on palindromic family: B +/- sqrt(5) P D / 25.
c=q**-2-q**8
P=c-q**4*S
D2=S**2+4*q**4*S-4*c
Bbase=c*S/sp.Integer(5)+sp.Rational(2,5)*(q**2-q**12)+q**4-1

# Bbase positivity: linear in S; verify value at S_min factor.
smin=2*(q**-1-q**4)
smax=q**-6-q**4
Hq=S*(q**8+q**6+q**4+q**2+1)+2*q**12+2*q**10+2*q**8+2*q**6-3*q**4-5*q**2
L=sp.factor(25*Bbase)
assert sp.simplify(L-5*(1-q)*(1+q)*Hq/q**2)==0
Hq_min=sp.factor(Hq.subs(S,smin))
Hq_min_expected=(q-1)**2*(2*q**6+4*q**5+8*q**4+7*q**3+8*q**2+4*q+2)/q
assert sp.simplify(Hq_min-Hq_min_expected)==0

# Squared domination certificate. Delta=(25 B)^2 - 5 P^2 D^2.
Delta=sp.factor(L**2-5*P**2*D2)
width=sp.factor(smax-smin)
width_expected=(q-1)**2*(q**4+q**3+q**2+q+1)**2/q**6
assert sp.simplify(width-width_expected)==0
Dy=sp.factor(sp.together(Delta.subs(S,smin+width*y)))
num,den=sp.together(Dy).as_numer_denom()
assert sp.factor(den)==q**16
poly=sp.Poly(sp.expand(num),y)
assert poly.degree()==4
power=[sp.expand(poly.coeff_monomial(y**k)) for k in range(5)]
bern=[]
for j in range(5):
    bj=sp.factor(sum(power[k]*sp.binomial(j,k)/sp.binomial(4,k) for k in range(j+1)))
    bern.append(bj)

P24=8*q**24+48*q**23+168*q**22+423*q**21+858*q**20+1523*q**19+2488*q**18+3883*q**17+5788*q**16+8123*q**15+10498*q**14+12313*q**13+13008*q**12+12313*q**11+10498*q**10+8123*q**9+5788*q**8+3883*q**7+2488*q**6+1523*q**5+858*q**4+423*q**3+168*q**2+48*q+8
P32=2*q**32+8*q**31+24*q**30+56*q**29+116*q**28+238*q**27+464*q**26+880*q**25+1507*q**24+2432*q**23+3612*q**22+5092*q**21+6797*q**20+8612*q**19+10312*q**18+11482*q**17+11982*q**16+11482*q**15+10312*q**14+8612*q**13+6797*q**12+5092*q**11+3612*q**10+2432*q**9+1507*q**8+880*q**7+464*q**6+238*q**5+116*q**4+56*q**3+24*q**2+8*q+2
P16=q**16+2*q**15+4*q**14+6*q**13+9*q**12+14*q**11+20*q**10+28*q**9+27*q**8+28*q**7+20*q**6+14*q**5+9*q**4+6*q**3+4*q**2+2*q+1
expected=[
25*q**10*(q-1)**6*(q+1)**2*(2*q**6+4*q**5+8*q**4+7*q**3+8*q**2+4*q+2)**2,
sp.Rational(5,2)*q**5*(q-1)**6*P24,
sp.Rational(5,3)*(q-1)**6*(q+1)**2*P32,
sp.Rational(25,2)*(q-1)**6*(q+1)**4*(q**2+1)**3*(q**8+3*q**4+1)*P16,
25*(q-1)**6*(q+1)**6*(q**2+1)**6*(q**8+3*q**4+1)**2]
for got,want in zip(bern,expected):
    assert sp.simplify(got-want)==0

positive_polys=[
2*q**6+4*q**5+8*q**4+7*q**3+8*q**2+4*q+2,
P24,P32,P16,q**8+3*q**4+1]
for polyexpr in positive_polys:
    coeffs=sp.Poly(polyexpr,q).all_coeffs()
    assert all(cc>=0 for cc in coeffs) and any(cc>0 for cc in coeffs)

print('C0036 Z5 FULL EXACT SYMBOLIC SELF-CHECK')
print('alpha+beta=1/5; alpha*beta=1/125; beta-alpha=sqrt(alpha*beta): PASS')
print('B20 arbitrary pair-smoothing obstruction:', obs)
print('reflection and palindromic identities: PASS')
print('triple lower-bound factorization: PASS')
print('pair B>=0 factorization: PASS')
print('Delta Bernstein denominator:', den)
print('Delta Bernstein degree:', poly.degree())
print('Delta Bernstein coefficients: 5/5 exact positive-form identities PASS')
print('ALL_EXACT_CHECKS_PASS')
