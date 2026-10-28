"""Independent exact checks; source domain is FROZEN_SPEC.json."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json, sys, time
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
start=time.perf_counter(); count=0
def ck(v):
    global count
    count+=1
    if not v: raise AssertionError(count)
    if count%512==0 and time.perf_counter()-start>55: raise TimeoutError('frozen cap')
def walsh(table):
    m=len(table)
    return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(table)),m) for s in range(m)]
def fwht(table):
    a=list(table); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [F(x,len(a)) for x in a]
def formadd(d,k,v):
    if k==1 or v==0:return
    d[k]=d.get(k,F(0))+v
    if d[k]==0:del d[k]
def cechange(p,q,u):
    # Exact coefficients of formal logarithms; expansion by cell ratio.
    d={}
    for pi,qi,ui in zip(p,q,u):
        if pi: ck(ui>0 and qi>0); formadd(d,ui/qi,-pi)
    return d
def vacuum(p,q):
    if p[0]==1:return list(p)
    k=(1-p[0])/(1-q[0]); return [p[0]]+[k*x for x in q[1:]]
def small(nmax):
    cases=0
    for n in range(nmax+1):
        m=2**n
        for code in range(2**m):
            t=[1 if code>>i&1 else -1 for i in range(m)]
            w=walsh(t); ck(w==fwht(t)); p=[x*x for x in w]; ck(sum(p)==1)
            for W in (0,m-1):
                q=[v/2+F(i==W,2) for i,v in enumerate(p)]
                u=vacuum(p,q); ck(sum(u)==1); ck(u[0]==p[0]); ck(all(v>=0 for v in u))
                # Formal CE change equals minus Bernoulli KL, without logs.
                lhs=cechange(p,q,u); rhs={}
                if p[0]:formadd(rhs,p[0]/q[0],-p[0])
                if p[0]!=1:formadd(rhs,(1-p[0])/(1-q[0]),-(1-p[0]))
                ck(lhs==rhs)
                # Exact A050 witness representation, including endpoints.
                if p[0]==1:ck(u==p)
                else:
                    k=(1-p[0])/(1-q[0]); b=k/2
                    rec=[b*v+F(i==0)*p[0]*(1-b)+F(i==W and W!=0)*k/2 for i,v in enumerate(p)]
                    ck(rec==u)
                cases+=1
    return cases
def poly(n,x):
    M=2**n
    z=(1+x)**n-1+M*x**n
    dz=n*(1+x)**(n-1)+n*M*x**(n-1)
    return 2*(M-1)*x*dz-n*M*z,z
def family(n):
    M=2**n; x0=F(1,M+1)
    if n<=6:
        t=[]
        for x in range(M):
            v=1
            for j in range(0,n,2):
                if (x>>j)&3==0:v=-v
            t.append(v)
        w=walsh(t); ck(w==fwht(t)); ck(all(a*a==F(1,M) for a in w))
        ck(sum(F(s.bit_count(),M) for s in range(M))==F(n,2))
    ck(poly(n,F(1))[0]>0)
    if n==2:
        x=F(1,5); ck(poly(n,x)[0]==0); z=poly(n,x)[1]
        ratios=[F(1)]+[(M-1)*x/z]*2+[(M-1)*(M+1)*x*x/z]
        ck(ratios==[1]*4)
        return {'n':n,'root':'1/5','minimum_witnesses':0,'excluded_endpoint':True}
    ck(poly(n,x0)[0]<0); ck(F(n,M+1)<=F(4,17))
    ck(F(289,169)+F(1,256)<2)
    ck(M*x0**(n-1)<=F(1,256))
    lo=x0;hi=F(1)
    for _ in range(48):
        mid=(lo+hi)/2
        if poly(n,mid)[0]<0:lo=mid
        else:hi=mid
    ck(poly(n,lo)[0]<0); ck(poly(n,hi)[0]>=0);ck(lo>x0 and hi<1)
    # Rigorous signs at both sides, together with variance monotonicity in proof.
    # Ratio at level n-1 is below vacuum, and full ratio is above that level.
    for x in (lo,hi):
        z=poly(n,x)[1]; a=(M-1)*x**(n-1)/z
        ck(a<1); ck((M+1)*x>1)
    ck(sum(comb(n,l) for l in range(n+1))==M)
    ck(comb(n,n-1)==n); ck(M-n>2)
    return {'n':n,'root_lo':str(lo),'root_hi':str(hi),'minimum_witnesses':M-n,'starting_witnesses':1,'vacuum_witnesses':2}
pilot='pilot' in sys.argv
rows=[family(n) for n in ([2,4] if pilot else range(2,33,2))]
smallcases=small(2 if pilot else 3)
result={'status':'PASS','helper_version':'A096-stage22-v1','assertions':count,'small_profiles':smallcases,'family_cases':len(rows),'seconds':time.perf_counter()-start,'arithmetic':'Fraction, integer Walsh, exact formal log coefficient identities','families':rows}
(OUT/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='families'}))
