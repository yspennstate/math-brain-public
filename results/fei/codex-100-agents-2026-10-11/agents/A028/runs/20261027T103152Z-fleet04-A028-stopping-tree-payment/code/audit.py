"""Separate direct-character and prime-log audit; imports no main checker."""
import itertools,json,time
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]; count=0
def ck(v):
    global count
    count+=1; assert v,count
def spectrum(f):
    return [sum(Q(f[t])*(-1)**((t&s).bit_count()) for t in range(len(f)))/len(f) for s in range(len(f))]
def factors(n):
    d={}; k=2
    while k*k<=n:
        while n%k==0: d[k]=d.get(k,0)+1; n//=k
        k+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def logterm(out,coef,x):
    if not coef:return
    assert x>0
    for n,sgn in ((x.numerator,1),(x.denominator,-1)):
        for k,v in factors(n).items(): out[k]=out.get(k,Q(0))+coef*sgn*v
def clean(d):return {k:v for k,v in d.items() if v}
def add(*ds):
    out={}
    for d in ds:
        for k,v in d.items():out[k]=out.get(k,Q(0))+v
    return clean(out)
def scale(d,a):return clean({k:v*a for k,v in d.items()})
def kl(p,q):
    out={}
    for a,b in zip(p,q):
        if a:logterm(out,a,a/b)
    return clean(out)
def ce(p,q):
    out={}
    for a,b in zip(p,q):
        if a:logterm(out,-a,b)
    return clean(out)
def ent(p):return ce(p,p)
def delete(t,i):return (t&((1<<i)-1))|((t>>(i+1))<<i)
start=time.monotonic(); profiles=0; query_checks=0
for f2 in itertools.product((-1,1),repeat=4):
    h=(-1,1,1,1); f=[a*b for b in f2 for a in h]
    a=spectrum(f); p=[z*z for z in a]; q=[z/2 for z in p]; q[-1]+=Q(1,2)
    for x in (Q(1,3),Q(1),Q(2)):
        profiles+=1; rho=p[0]
        if rho==1:continue
        z=sum(q[t]*x**t.bit_count() for t in range(1,16)); A=(1-rho)/z
        u=[rho]+[A*q[t]*x**t.bit_count() for t in range(1,16)]
        Ip=sum(z*t.bit_count() for t,z in enumerate(p)); Iu=sum(z*t.bit_count() for t,z in enumerate(u))
        correction={};logterm(correction,Ip-Iu,x)
        ck(add(ce(p,q),scale(ce(p,u),-1))==add(kl(u,q),correction))
        for i in range(4):
            jointp=[]; jointq=[]; children=[]; normals=[]
            for s in (-1,1):
                cp=[Q(0)]*8;cq=[Q(0)]*8
                for t in range(16):
                    base=t&~(1<<i); aa,bb=a[base],a[base|(1<<i)]; den=2*(aa*aa+bb*bb)
                    k=(aa+s*bb)**2/den if den else Q(1,2)
                    cp[delete(t,i)]+=p[t]*k;cq[delete(t,i)]+=u[t]*k
                mass=sum(cq); ck(mass>0);ck(sum(cp)==Q(1,2))
                # Direct restriction characters, independent of component transport.
                vals=[]
                for t in range(8):
                    full=(t&((1<<i)-1))|((t>>i)<<(i+1))|((0 if s==1 else 1)<<i)
                    vals.append(f[full])
                pc=[v*v for v in spectrum(vals)];qc=[v/mass for v in cq]
                ck(cp==[v/2 for v in pc]);jointp+=cp;jointq+=cq
                children.append((pc,qc));normals.append(mass)
            O=kl([Q(1,2)]*2,normals)
            avgD=scale(add(*(kl(pc,qc) for pc,qc in children)),Q(1,2))
            ck(kl(jointp,jointq)==add(O,avgD))
            L=add(kl(p,u),scale(kl(jointp,jointq),-1))
            dH=add(ent(p),scale(add(*(ent(pc) for pc,qc in children)),Q(-1,2)))
            ck(ce(p,u)==add(scale(add(*(ce(pc,qc) for pc,qc in children)),Q(1,2)),dH,L,O))
            query_checks+=1
# Fault control: omitting the vacuum correction fails exact reconstruction.
n=4;M=1<<n;x=Q(2);A=2*Q(M-1)/((1+x)**n-1+M*x**n)
uncorrected=A/(2*M);corrected=uncorrected+(1-A/2)/M
ck(corrected==Q(1,M));ck(uncorrected!=Q(1,M))
out={'status':'PASS','profiles':profiles,'physical_queries':query_checks,'assertions':count,'seconds':time.monotonic()-start,'method':'direct characters and exact prime-log coefficient vectors','fault_control':'omitted vacuum correction rejected'}
(root/'out'/'audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
