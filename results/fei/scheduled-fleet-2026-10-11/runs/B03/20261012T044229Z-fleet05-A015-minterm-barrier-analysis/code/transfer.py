from fractions import Fraction as F
from pathlib import Path
from math import comb
import importlib.util,json,time
# Import only this stage's own checked arithmetic, without rerunning its pilot.
# The helper below is standalone to avoid any executable upstream import.
start=time.perf_counter(); checks=0
out=Path(__file__).resolve().parents[1]/'out'
def ck(v):
    global checks
    assert v; checks+=1
    assert time.perf_counter()-start<60
def walsh(t):
    a=list(t); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [F(x,len(a)) for x in a]
def ln(q):
    k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    def series(y):
        z=(y-1)/(y+1); z2=z*z; term=z; total=F(0); terms=24
        for j in range(terms): total+=term/(2*j+1);term*=z2
        lo=2*total; return lo,lo+2*term/((2*terms+1)*(1-z2))
    a,b=series(q);c,d=series(F(2))
    return (a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)
def log(q):
    a,b=ln(q);c,d=ln(F(2));grid=1<<48
    if a>=0:l,u=a/d,b/c
    elif b<=0:l,u=a/c,b/d
    else:l,u=a/c,b/c
    return F((l*grid).__floor__(),grid),F((u*grid).__ceil__(),grid)
def core_ref(n):
    R=[F(0)]*(1<<n)
    for s in range(1,n+1):
        weights=[min(F(1),F(s,j)**2) for j in range(1,n+1)]
        coeff=[F(1)]+[F(0)]*s
        for w in weights:
            for j in range(s,0,-1): coeff[j]+=w*coeff[j-1]
        for A in range(1,1<<n):
            if A.bit_count()!=s: continue
            product=F(1)
            for j,w in enumerate(weights):
                if A>>j&1: product*=w
            R[A]=product/(2*s*(s+1)*coeff[s])
    return R
records=[]
for n in [1,3,5,7,9]:
    threshold=(n+1)//2
    table=[-1 if n-x.bit_count()>=threshold else 1 for x in range(1<<n)]
    P=[x*x for x in walsh(table)]; I=sum(F(A.bit_count())*q for A,q in enumerate(P))
    R=core_ref(n); z=sum(R)
    ck(z==F(n,2*(n+1)));ck(P[0]==0)
    c_lo=c_hi=F(0)
    coreKL={}
    for A,prob in enumerate(P):
        if not prob:continue
        L,U=log(1/R[A]);c_lo+=prob*L;c_hi+=prob*U
        ratio=prob/R[A]
        if ratio!=1:coreKL[ratio]=coreKL.get(ratio,F(0))+prob
    ck(c_hi<F(101,10)*I)
    for r in [1,2,3,4]:
        p=F(1,1<<r)
        parent=table+[1]*(len(table)*((1<<r)-1));PF=[x*x for x in walsh(parent)]
        Q=[]
        for S in range(len(PF)):
            T=S&((1<<n)-1);U=S>>n
            Q.append(p*p*R[T] if T else (p*p if U else (1-p)**2))
        ck(sum(Q)==1-p+p*z)
        ck(sum(F(S.bit_count())*prob for S,prob in enumerate(PF))==p*(I+r))
        inducedKL={}
        for S,prob in enumerate(PF):
            if not prob:continue
            ratio=prob/Q[S]
            if ratio!=1:inducedKL[ratio]=inducedKL.get(ratio,F(0))+prob
        ck(inducedKL=={q:p*mass for q,mass in coreKL.items()})
        L,U=log(1/(1-p));A_lo=2*r*p*(2-p)+2*(1-p)**2*L;A_hi=2*r*p*(2-p)+2*(1-p)**2*U
        CElo=p*c_lo+A_lo;CEhi=p*c_hi+A_hi;IF=p*(I+r)
        ck(CEhi<F(101,10)*IF)
        records.append({'n':n,'r':r,'core_I':str(I),'core_reference_mass':str(z),
                        'activation_reference_mass':str(sum(Q)),'core_CE_interval':[str(c_lo),str(c_hi)],
                        'activation_CE_interval':[str(CElo),str(CEhi)],'activation_I':str(IF),
                        'exact_KL_transfer':'D(P_F||Q_F)=p D(P_g||R_g)'})
result={'status':'PASS','exact_assertions':checks,'core_references':5,'activated_references':20,
        'max_dimension':13,'elapsed_seconds':time.perf_counter()-start,'records':records}
(out/'TRANSFER_RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
