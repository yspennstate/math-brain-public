from itertools import permutations
from fractions import Fraction
import math

a=(0,-5,3,2); b=(-1,2,4,3)
P4=list(permutations(range(4)))
pairs=(frozenset((0,1)),frozenset((0,2)),frozenset((0,3)))
E=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def pclass(S):
    S=frozenset(S); all4={0,1,2,3}
    for q,T in enumerate(pairs):
        if S==T or S==frozenset(all4-set(T)): return q
    raise AssertionError

def rho(sig): return tuple(pclass(sig[i] for i in T) for T in pairs)
rhos=sorted({rho(s) for s in P4})
fib={r:[s for s in P4 if rho(s)==r] for r in rhos}
def H(sig): return Fraction(math.prod(a[i]+b[sig[i]] for i in range(4)))
Hv={s:H(s) for s in P4}; M=max(Hv.values())
B={r:sum((Hv[s] for s in fib[r]),Fraction(0))/4 for r in rhos}
Q=max(B.values()); Delta=M-Q
kappa={s:Hv[s]-B[rho(s)] for s in P4}
ks=sorted(set(kappa.values()),reverse=True)
K,second=ks[:2]; delta=K-second
stars=[s for s in P4 if kappa[s]==K]; assert len(stars)==1
star=stars[0]; r=K-Delta; dstar=M-Hv[star]

def channel_coeffs():
    Aplus=[]; Aminus=[]; Bplus=[]; Bminus=[]; all4={0,1,2,3}
    for S in pairs:
        Sc=all4-set(S)
        xa=math.prod(a[i] for i in S); xac=math.prod(a[i] for i in Sc)
        xb=math.prod(b[i] for i in S); xbc=math.prod(b[i] for i in Sc)
        Aplus.append(xa+xac); Aminus.append(xac-xa)
        Bplus.append(xb+xbc); Bminus.append(xb-xbc)
    EA=[sum(E[i][q]*Aminus[q] for q in range(3)) for i in range(4)]
    EB=[sum(E[j][q]*Bminus[q] for q in range(3)) for j in range(4)]
    ca=[math.prod(a[j] for j in range(4) if j!=i) for i in range(4)]
    db=[math.prod(b[j] for j in range(4) if j!=p) for p in range(4)]
    C=[[Fraction(ca[i]*b[p]+a[i]*db[p])+Fraction(EA[i]*EB[p],8) for p in range(4)] for i in range(4)]
    J=[[Fraction(Aplus[x]*Bplus[y],2) for y in range(3)] for x in range(3)]
    return C,J
C,J=channel_coeffs()
c=lambda s: sum((C[i][s[i]] for i in range(4)),Fraction(0))
j=lambda rr: sum((J[i][rr[i]] for i in range(3)),Fraction(0))
Lp=max(c(s) for s in P4)-c(star); Rho=rho(star)
Lr=max(j(rr) for rr in rhos)-j(Rho); L=Lp+2*Lr
T=r-delta/2; Bceil=(L*r-delta*dstar)/(L+delta)
Gamma=max(Fraction(0),T,Bceil)
trans=[]
for i in range(4):
    for jj in range(i+1,4):
        t=list(range(4)); t[i],t[jj]=t[jj],t[i]; trans.append(tuple(t))
compose=lambda t,s: tuple(t[s[i]] for i in range(4))
gaps=[2*M-max(Hv[s]+Hv[compose(t,s)] for s in P4) for t in trans]
m=sum(Hv.values(),Fraction(0))/24
pairceil=(3*(M-m)-Delta-sum(gaps,Fraction(0))/2)/4
assert (M,Delta,K,r,second,delta,Hv[star],dstar)==(108,202,210,8,Fraction(413,2),Fraction(7,2),56,52)
assert (Lp,Lr,L)==(0,60,120)
assert T==Fraction(25,4)
assert Bceil==Fraction(1556,247)
assert Gamma==Fraction(1556,247) and Gamma<r
print('PASS MOC4-STANDARD-PR-LOCKING-v1')
print('star =',''.join(str(i+1) for i in star))
print('M =',M,'Delta =',Delta,'K =',K,'r =',r)
print('second_kappa =',second,'delta =',delta,'Hstar =',Hv[star],'dstar =',dstar)
print('Lp =',Lp,'Lr =',Lr,'L =',L)
print('branch_threshold =',T)
print('locking_branch_ceiling =',Bceil)
print('new_ceiling =',Gamma)
print('old_standard_ceiling =',r)
print('pair_ceiling =',pairceil)
