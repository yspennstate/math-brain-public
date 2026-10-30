"""Independent physical-product enumeration and symbolic prime-log audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import time,json
R=Path(__file__).resolve().parents[1]
spec={'version':'audit22-v1','family':'all truth tables n<=2, physical product m=2,3; normalized real controls k=2..33','cases':44,'symmetry':'none','arithmetic':'integer direct Walsh; Fraction coefficients of formal prime logarithms','memory_mb':40,'runtime_cap_seconds':55}
(R/'out/AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
t0=time.monotonic(); checks=0
def ck(ok):
    global checks
    checks+=1; assert ok; assert time.monotonic()-t0<55
def factors(k):
    q=2; d={}
    while q*q<=k:
        while k%q==0: d[q]=d.get(q,0)+1; k//=q
        q+=1
    if k>1:d[k]=d.get(k,0)+1
    return d
def addlog(out,w,x):
    if not w or not x:return
    for q,e in factors(x.numerator).items():out[q]+=w*e
    for q,e in factors(x.denominator).items():out[q]-=w*e
def clean(out): return {q:v for q,v in out.items() if v}
def mul(out,m):return clean({q:v*m for q,v in out.items()})
def metrics(p,n):
    H=defaultdict(F); B=[]; L=[]
    for v in p:addlog(H,-v,v)
    for i in range(n):
        b=defaultdict(F); l=defaultdict(F)
        for s in range(1<<n):
            if s>>i&1:continue
            u,v=p[s],p[s|(1<<i)]
            addlog(b,u+v,u+v);addlog(b,-u,u);addlog(b,-v,v)
            addlog(l,v,u+v);addlog(l,-v,v)
        B.append(clean(b));L.append(clean(l))
    return clean(H),B,L
def spectrum(vals,n):
    N=1<<n
    return [F(sum(vals[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N)**2 for s in range(N)]
cases=0
for n in range(3):
    N=1<<n
    for mask in range(1<<N):
        vals=[1-2*(mask>>x&1) for x in range(N)]
        p=spectrum(vals,n); H,B,L=metrics(p,n)
        for m in (2,3):
            phys=[]
            for x in range(1<<(m*n)):
                v=1
                for block in range(m):v*=vals[(x>>(block*n))&(N-1)]
                phys.append(v)
            q=spectrum(phys,m*n); HH,BB,LL=metrics(q,m*n)
            ck(HH==mul(H,m))
            for block in range(m):
                for i in range(n):ck(BB[block*n+i]==B[i]);ck(LL[block*n+i]==L[i])
            # Deliberately mismatched complete reference, including vacuum.
            ref=[(v+F(1,N))/2 for v in p]
            dr=defaultdict(F);dq=defaultdict(F)
            for v,r in zip(p,ref):addlog(dr,v,v);addlog(dr,-v,r)
            for S in product(range(N),repeat=m):
                v=F(1);r=F(1)
                for s in S:v*=p[s];r*=ref[s]
                addlog(dq,v,v);addlog(dq,-v,r)
            ck(clean(dq)==mul(clean(dr),m));cases+=1
for k in range(2,34):
    a=F(k*k-1,k*k+1);b=F(2*k,k*k+1)
    ck(a*a+b*b==1);ck(2*a*b>0);ck(b*b==F(4*k*k,(k*k+1)**2))
result={'status':'PASS','physical_tensor_cases':cases,'rational_nonBoolean_controls':32,'exact_assertions':checks,'seconds':time.monotonic()-t0,'scope':'exact symbolic H/B/L tensor identities and linear full-reference KL mismatch; not FEI'}
(R/'out/INDEPENDENT_IMPLEMENTATION_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
