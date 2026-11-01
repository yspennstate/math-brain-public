from fractions import Fraction
from math import comb
import sympy as sp

# Exact algebraic certificate for the three-block residence inequality.
a,b,c = sp.symbols("a b c")
rho = 1-c
Sden = a + a*b + b*c
Psi = (
    2*rho
    - sp.Rational(1,2)*(a + b/a + c/b)
    + sp.Rational(1,2)*(rho-a-b-c)**2/Sden
)
P = sp.factor(2*a*b*Sden*Psi)
P_expected = (
    -a**3*b**2
    -5*a**2*b**2*c
    +6*a**2*b**2
    -a**2*b*c
    +2*a**2*b
    -a**2*c
    -4*a*b**2*c**2
    +8*a*b**2*c
    -3*a*b**2
    +3*a*b*c**2
    -4*a*b*c
    +a*b
    -b**3*c
)
assert sp.expand(P-P_expected) == 0

# Nested cube parametrization of 0 <= c <= b <= a <= 1:
# c=Z, b=Z+(1-Z)Y, a=b+(1-b)X.
X,Y,Z = sp.symbols("X Y Z")
cmap = Z
bmap = Z + (1-Z)*Y
amap = bmap + (1-bmap)*X
Pc = sp.Poly(sp.expand(P.subs({a:amap,b:bmap,c:cmap})), X,Y,Z, domain=sp.QQ)
power_degrees = Pc.degree_list()
assert power_degrees == (3,5,5)
power = {mon:coef for mon,coef in Pc.terms()}

# Exact degree-elevated tensor Bernstein coefficients.
target = (5,8,8)
bernstein = []
for i in range(target[0]+1):
    for j in range(target[1]+1):
        for k in range(target[2]+1):
            coeff = sp.Rational(0)
            for ii in range(min(i,power_degrees[0])+1):
                for jj in range(min(j,power_degrees[1])+1):
                    for kk in range(min(k,power_degrees[2])+1):
                        pcoef = power.get((ii,jj,kk),sp.Rational(0))
                        if pcoef:
                            coeff += (
                                pcoef
                                * sp.Rational(comb(i,ii),comb(target[0],ii))
                                * sp.Rational(comb(j,jj),comb(target[1],jj))
                                * sp.Rational(comb(k,kk),comb(target[2],kk))
                            )
            bernstein.append(sp.factor(coeff))

pos = [q for q in bernstein if q > 0]
zero = [q for q in bernstein if q == 0]
neg = [q for q in bernstein if q < 0]
assert len(bernstein) == 486
assert len(pos) == 422
assert len(zero) == 64
assert len(neg) == 0
assert min(pos) == sp.Rational(1,40)

# Exact four-atom sanity check in the genuinely unresolved topology:
# M-SERPT has two records (2,4), while Gittins skips the first.
F = Fraction
xs = [F(1),F(2),F(4),F(8)]
ps = [F(1,20),F(11,20),F(1,4),F(3,20)]

def SN(age):
    surv = sum((p for x,p in zip(xs,ps) if x > age), F(0))
    tail = sum((p*(x-age) for x,p in zip(xs,ps) if x > age), F(0))
    return surv, tail

ages = [F(0),F(1),F(2),F(4)]
rS=[]
rG=[]
for age in ages:
    Sa,Na=SN(age)
    rs=Na/Sa
    rS.append(rs)
    candidates=[rs]
    for stop in xs:
        if stop>age:
            Ss,Ns=SN(stop)
            den=Sa-Ss
            if den>0:
                candidates.append((Na-Ns)/den)
    rG.append(min(candidates))

assert rS == [F(67,20),F(47,19),F(7,2),F(4)]
assert rG == [F(55,17),F(19,11),F(16,5),F(4)]
assert rS[2] > rS[0] and rS[3] > rS[2]
assert rG[2] < rG[0] and rG[3] > rG[0]

rhoF=F(19,20)
mu=sum((x*p for x,p in zip(xs,ps)),F(0))
lam=rhoF/mu
b1,b2=F(2),F(4)
m1=sum((p*min(x,b1) for x,p in zip(xs,ps)),F(0))
m2=sum((p*min(x,b2) for x,p in zip(xs,ps)),F(0))
V1=sum((p*min(x,b1)**2 for x,p in zip(xs,ps)),F(0))
V2=sum((p*min(x,b2)**2 for x,p in zip(xs,ps)),F(0))
V=sum((p*x*x for x,p in zip(xs,ps)),F(0))
A1=1-lam*m1
A2=1-lam*m2
alpha=1-rhoF
P1=sum((p for x,p in zip(xs,ps) if x<=b1),F(0))
P2=sum((p for x,p in zip(xs,ps) if b1<x<=b2),F(0))
P3=sum((p for x,p in zip(xs,ps) if x>b2),F(0))
M1=sum((p*x for x,p in zip(xs,ps) if x<=b1),F(0))
M2=sum((p*x for x,p in zip(xs,ps) if b1<x<=b2),F(0))
M3=sum((p*x for x,p in zip(xs,ps) if x>b2),F(0))

Q = lam*F(1,2)*(P1*V1/A1 + P2*V2/(A1*A2) + P3*V/(A2*alpha))
R = M1 + M2/A1 + M3/A2
K = Q + 2*mu - R
assert Q == F(12183427,353410)
assert R == F(6246811,706820)
assert K == F(22855737,706820)
assert K > 0

q1,q2,q3 = lam*M1,lam*M2,lam*M3
Phi = (
    2*rhoF
    +F(1,2)*(q1*q1/A1 + q2*q2/(A1*A2) + q3*q3/(A2*alpha))
    -(q1 + q2/A1 + q3/A2)
)
assert Phi == F(490758581,94713880)
Klower = Phi/lam
assert Klower == F(25829399,1413640)
assert K >= Klower > 0

print("POWER_DEGREES", power_degrees)
print("BERNSTEIN_TARGET_DEGREES", target)
print("BERNSTEIN_TOTAL", len(bernstein))
print("BERNSTEIN_POSITIVE", len(pos))
print("BERNSTEIN_ZERO", len(zero))
print("BERNSTEIN_NEGATIVE", len(neg))
print("BERNSTEIN_MIN_POSITIVE", min(pos))
print("EXAMPLE_SERPT_RANKS", rS)
print("EXAMPLE_GITTINS_RANKS", rG)
print("EXAMPLE_Q_MS", Q)
print("EXAMPLE_R_MS", R)
print("EXAMPLE_K", K)
print("EXAMPLE_CERTIFIED_LOWER_BOUND", Klower)
print("ALL_EXACT_CHECKS_PASS")
