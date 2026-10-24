from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(b):
    global checks
    checks+=1;assert b,checks
def add(*terms):
    z={}
    for k,v in terms:
        for p,a in v.items(): z[p]=z.get(p,F(0))+k*a
    return {p:a for p,a in z.items() if a}
def fac(n):
    z={};p=2
    while p*p<=n:
        while not n%p: z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def log(x):
    x=F(x);z={p:F(a) for p,a in fac(x.numerator).items()}
    for p,a in fac(x.denominator).items():z[p]=z.get(p,F(0))-a
    return {p:a for p,a in z.items() if a}
def phi(x):return add((-x,log(x))) if x else {}
def walsh(v):
    # Direct character sum, independent of the main butterfly implementation.
    return [F(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(v)),len(v)) for s in range(len(v))]
def H(v):return add(*[(1,phi(a*a)) for a in walsh(v)])
ctrl=[]
for z in range(8):
    x,a,b=z&1,(z>>1)&1,(z>>2)&1
    ctrl.append(0 if x==0 and a==1 else 1 if x==0 and a==0 and b==1 else 2)
q0,q1=F(ctrl.count(0),8),F(ctrl.count(1),8)
check((q0,q1)==(F(1,4),F(1,8)))
u=v=(1,1,1,-1)
actual={}
for x in range(4):
    for y in range(4):
        leaf=tuple(u[x] if j==0 else v[y] if j==1 else 1 for j in ctrl)
        actual=add((1,actual),(F(1,16),H(leaf)))
controlfirst=add((q0,H(u)),(q1,H(v)))
check(actual=={2:F(11,8),3:-F(9,32)})
check(controlfirst=={2:F(3,4)})
check(3<4) # log2(3)<2 implies frontier gap >1/16.
gap=add((1,actual),(-1,controlfirst));check(gap=={2:F(5,8),3:-F(9,32)})
q,m,beta=F(1,4),F(1,2),F(1,2)
cv=tuple(F(j==0) for j in ctrl)
av=tuple(m if j==0 else F(1) for j in ctrl)
a,c=walsh(av),walsh(cv)
Pplus=[(x+beta*y)**2 for x,y in zip(a,c)];Pminus=[(x-beta*y)**2 for x,y in zip(a,c)]
Mplus,Mminus=sum(Pplus,F(0)),sum(Pminus,F(0));M=(Mplus+Mminus)/2
check((Mplus,Mminus,M)==(F(1),F(3,4),F(7,8)))
rho=Mplus/(2*M);check(rho==F(4,7))
J=add(*[(1,add((1,phi((s+t)/2)),(-F(1,2),phi(s)),(-F(1,2),phi(t)))) for s,t in zip(Pplus,Pminus)])
normalized={}
for s,t in zip(Pplus,Pminus):
    normalized=add((1,normalized),(M,phi((s+t)/(2*M))),(-M*rho,phi(s/Mplus)),(-M*(1-rho),phi(t/Mminus)))
mass=add((1,phi(M)),(-F(1,2),phi(Mplus)),(-F(1,2),phi(Mminus)))
check(mass=={2:F(15,8),3:F(3,8),7:-F(7,8)})
check(J==add((1,normalized),(1,mass)))
check(2**15*3**3>7**7)
check((3+F(48,65))*F(81,56)<F(11,2))
out={'status':'PASS','exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'data_first_terminal_H':{str(p):str(x) for p,x in actual.items()},'control_first_terminal_H':{str(p):str(x) for p,x in controlfirst.items()},'frontier_gap':{str(p):str(x) for p,x in gap.items()},'projected_mass_correction':{str(p):str(x) for p,x in mass.items()},'physical_branch_weights':['1/2','1/2'],'spectral_sector_weights':['4/7','3/7'],'strict_sign_certificate':'2^15*3^3=884736>7^7=823543; frontier gap >1/16 because 3<4','kappa_rational_upper':str((3+F(48,65))*F(81,56))}
(R/'out'/'REVIEW_WITNESSES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
