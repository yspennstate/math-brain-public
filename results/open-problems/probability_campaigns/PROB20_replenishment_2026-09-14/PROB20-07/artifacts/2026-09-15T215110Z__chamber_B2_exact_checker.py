import sympy as sp

X,Y,A,B,S,P,Z,tau=sp.symbols('X Y A B S P Z tau', real=True)
a=sp.Rational(1,12)
b=sp.Rational(3,4)

Sxy=X+Y
Pxy=X*Y
Cxy=1-Sxy
u=X-Y
t=(Cxy-B)/(A-B)
x2=sp.factor(t*(A+Y)); y2=sp.factor(t*(A+X))
x3=sp.factor((1-t)*(B+Y)); y3=sp.factor((1-t)*(B+X))
r1=Y/X; r2=(A+X)/(A+Y); r3=(B+X)/(B+Y)

# B2 ordering formula.
D0xy=(A+Sxy)**2-Pxy
branch=sp.factor(r1*r3-r2**2)
expected_branch=-(X-Y)*(B*D0xy+Pxy*(2*A+Sxy))/(X*(A+Y)**2*(B+Y))
assert sp.simplify(branch-expected_branch)==0

# Coordinate-floor lower bound B>=F and B2 upper bound B<=G.
F=sp.factor((a*A-Y*(A-Cxy))/(A-Cxy+a))
G=sp.factor(-Pxy*(2*A+Sxy)/D0xy)
H=12*A**2*Y-A**2+12*A*Sxy*Y-2*A*Sxy+12*A*Y**2-11*A*Y-Sxy**2+12*Sxy*Y**2+Sxy*Y-12*Y**2
assert sp.simplify(F-G + (A+Y)*H/((12*A+12*Sxy-11)*D0xy))==0

# H endpoint identities proving B2 forces A>2/3.
Ss,Ys,As=sp.symbols('Ss Ys As', real=True)
Hs=12*As**2*Ys-As**2+12*As*Ss*Ys-2*As*Ss+12*As*Ys**2-11*As*Ys-Ss**2+12*Ss*Ys**2+Ss*Ys-12*Ys**2
assert sp.factor(Hs.subs(As,1-Ss)-(Ys-1))==0
K=9*Ss**2-108*Ss*Ys**2-81*Ss*Ys+12*Ss+36*Ys**2+18*Ys+4
assert sp.factor(Hs.subs(As,sp.Rational(2,3))+K/9)==0
assert sp.factor(K.subs(Ys,a)-(36*Ss**2+18*Ss+23)/4)==0
assert sp.factor(K.subs(Ys,Ss/2)+(3*Ss-2)*(3*Ss+4)*(6*Ss+1)/2)==0
assert sp.factor(sp.diff(K,Ys,2)+72*(3*Ss-1))==0

# lambda=r1*r2 source and target formulas.
lam=r1*r2
Ux=[X**2,2*X*x2,2*X*x3,x2**2,2*x2*x3,x3**2]
Uy=[Y**2,2*Y*y2,2*Y*y3,y2**2,2*y2*y3,y3**2]
source=sp.factor(sum(Uy[i]-lam*Ux[i] for i in [2,3,4,5]))
assert sp.factor(source-u*(A*(1+Pxy)+Pxy*Sxy)/(X*(A+Y)))==0
T1=sp.factor((X-a)-lam*(Y-a))
T2=sp.factor((x2-a)-lam*(y2-a))
T3=sp.factor((x3-a)-lam*(y3-a))
D=sp.factor(t*(A**2-Pxy))
assert sp.factor(T1-u*(A*(Sxy-a)+Pxy)/(X*(A+Y)))==0
assert sp.factor(T2-u*(D-a*A)/(X*(A+Y)))==0
assert sp.factor(T3+u*(D-A*(1-Sxy-a)+Pxy)/(X*(A+Y)))==0

# Endpoint stop-loss polynomial and B-linear decomposition.
E=12*D+A*(12*Sxy-11-9*Pxy)+Pxy*(12-9*Sxy)
N=sp.factor((A-B)*E)
N0=A**2*(1-9*Pxy)+A*Pxy*(12-9*Sxy)-12*Pxy*(1-Sxy)
N1=A*(11-12*A-12*Sxy+9*Pxy)+9*Pxy*Sxy
assert sp.factor(N-(N0+B*N1))==0

# Abstract Phi = D0*(N0+G*N1), concave in P.
Aa,Sv,Pv=sp.symbols('Aa Sv Pv', real=True)
Cv=1-Sv
N0a=Aa**2*(1-9*Pv)+Aa*Pv*(12-9*Sv)-12*Pv*Cv
N1a=Aa*(11-12*Aa-12*Sv+9*Pv)+9*Pv*Sv
D0=(Aa+Sv)**2-Pv
Ga=-Pv*(2*Aa+Sv)/D0
Phi=sp.factor(sp.together(D0*(N0a+Ga*N1a)))
assert sp.factor(sp.expand(Phi).coeff(Pv,2)+3*(Aa+Sv+2)*(3*Aa+3*Sv-2))==0

# Upper endpoint P=S^2/4.
Q=9*Sv**2*(Aa+Sv-2)**2-4*Aa*(Aa+Sv)
assert sp.factor(Phi.subs(Pv,Sv**2/4)+(2*Aa+Sv)**2*Q/16)==0
assert sp.factor(Q.subs(Aa,1-Sv)-(9*Sv**2+4*Sv-4))==0
R=81*Sv**4-216*Sv**3+144*Sv**2-24*Sv-16
assert sp.factor(Q.subs(Aa,sp.Rational(2,3))-R/9)==0
assert sp.expand(R.subs(Sv,(1+tau)/3))==tau**4-4*tau**3-2*tau**2+4*tau-15

# Lower endpoint P=a(S-a): exact positive-coefficient expansions.
Pmin=a*(Sv-a)
Phi_min=sp.expand(Phi.subs(Pv,Pmin))
expr1=sp.Poly(sp.expand(Phi_min.subs(Aa,1-Sv+Z)),Z)
expr2=sp.Poly(sp.expand(Phi_min.subs(Aa,sp.Rational(2,3)+Z)),Z)
expected1=[
    (17-12*Sv)/16,
    (12*Sv**2-33*Sv+64)/16,
    (432*Sv**2-10008*Sv+13519)/2304,
    (3456*Sv**3+3024*Sv**2-19800*Sv+13771)/3456,
    11*(12*Sv-13)*(28*Sv-17)/2304,
]
expected2=[
    (17-12*Sv)/16,
    (124+153*Sv-108*Sv**2)/48,
    (-5184*Sv**3+6048*Sv**2+11448*Sv+5935)/2304,
    (3*Sv+4)*(-864*Sv**3+2232*Sv**2+696*Sv+1079)/3456,
    (9072*Sv**4+9720*Sv**3+9783*Sv**2+648*Sv+5056)/20736,
]
for got,want in zip(expr1.all_coeffs(),expected1):
    assert sp.factor(got-want)==0
for got,want in zip(expr2.all_coeffs(),expected2):
    assert sp.factor(got-want)==0

print('ALL EXACT CHAMBER-B2 CHECKS PASSED')
