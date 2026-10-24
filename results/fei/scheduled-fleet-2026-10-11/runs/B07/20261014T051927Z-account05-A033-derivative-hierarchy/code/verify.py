from pathlib import Path
from itertools import product
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(v):
    global checks
    checks+=1;assert v
def W(h):
    return [sum(h[x]*(1-2*((s&x).bit_count()%2)) for x in range(len(h))) for s in range(len(h))]
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1);N=20
    L=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    E=2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return L,L+E
@lru_cache(None)
def log2(x):
    e=0
    while x>=2:x/=2;e+=1
    while x<1:x*=2;e-=1
    a,b=ln(x);c,d=ln(F(2));return F(e)+a/d,F(e)+b/c
def entropy(nums):
    T=sum(nums)
    if not T:return F(0),F(0)
    lo=hi=F(0)
    for v in nums:
        if v:
            a,b=log2(F(T,v));lo+=F(v,T)*a;hi+=F(v,T)*b
    return lo,hi
def signature(nums):
    T=sum(nums);d={}
    if not T:return d
    for v in nums:
        if not v:continue
        for value,coef in ((T,F(v,T)),(v,-F(v,T))):
            p=2
            while p*p<=value:
                while value%p==0:d[p]=d.get(p,F(0))+coef;value//=p
                p+=1
            if value>1:d[value]=d.get(value,F(0))+coef
    return {p:v for p,v in d.items() if v}
def audit(truth):
    L=len(truth);n=L.bit_length()-1;data=L//4
    full=W(truth);p=[v*v for v in full]
    ck(sum(p)==L*L)
    IF=F(sum(s.bit_count()*v for s,v in enumerate(p)),L*L)
    edges=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(L) for i in range(n)),L)
    ck(IF==edges)
    rows=[];mass=[];IY=F(0);IX=F(0);CHlo=CHhi=F(0);CS={}
    for J in range(4):
        sums=[sum(truth[a+4*y]*(1-2*((a&J).bit_count()%2)) for a in range(4)) for y in range(data)]
        ck(all(v%2==0 for v in sums));h=[v//2 for v in sums];z=[v*v for v in W(h)];T=sum(z)
        ck(all(abs(v)<=2 for v in h));mass.append(T)
        if not T:rows.append({'J':J,'w':'0','N':0});continue
        m=[sum(z[s] for s in range(data) if s>>i&1) for i in range(n-2)]
        for s,v in enumerate(z):
            # Full coordinate product, including deterministic frequencies.
            ck(v*T**max(n-3,0)==(T if n==2 else __import__('math').prod(m[i] if s>>i&1 else T-m[i] for i in range(n-2))))
        nf=sum(0<v<T and 2*v!=T for v in m);ck(nf<=2)
        weight=F(T,4*data*data);a,b=entropy(z);CHlo+=weight*a;CHhi+=weight*b
        for prime,v in signature(z).items():CS[prime]=CS.get(prime,F(0))+weight*v
        IY+=F(sum(s.bit_count()*v for s,v in enumerate(z)),4*data*data);IX+=J.bit_count()*weight
        rows.append({'J':J,'w':str(weight),'N':nf,'marginals':[str(F(v,T)) for v in m]})
    for y in range(data):
        hs=[sum(truth[a+4*y]*(1-2*((a&J).bit_count()%2)) for a in range(4))//2 for J in range(4)]
        ck(sorted(map(abs,hs)) in ([0,0,0,2],[1,1,1,1]))
        ck(len(set(4*v*v-v**4 for v in hs))==1)
    ck(IF==IY+IX);ck(sum(mass)==4*data*data)
    Hlo,Hhi=entropy(p);l,_=log2(F(65,64));Klo=6+2*l
    blo,_=entropy([1,9]);Kcondlo=F(3,2)+F(5,2)*blo
    target={2:4*IY,5:F(5,2)*IY,3:-F(9,2)*IY}
    equality={p:v for p,v in CS.items() if v}=={p:v for p,v in target.items() if v}
    ck(CHhi<=Kcondlo*IY or equality)
    ck(Hhi<=Klo*IF or Hhi==IF==0)
    return {'rows':rows,'I_Y':str(IY),'I_X':str(IX),'I':str(IF),'H_interval':[str(Hlo),str(Hhi)],'conditional_interval':[str(CHlo),str(CHhi)]}
# Different enumeration representation and a Fourier inversion certificate.
cert=json.loads((R/'out'/'endpoint.json').read_text(encoding='utf-8'))
allowed={tuple(row['h']):row for row in cert['certificate_rows']};found={}
for digits in range(625):
    x=digits;h=[]
    for _ in range(4):h.append(x%5-2);x//=5
    z=W(h);v=[a*a for a in z];T=sum(v)
    ck(W(z)==[4*a for a in h])
    if T and v[0]*v[3]==v[1]*v[2]:
        qs=[v[1]+v[3],v[2]+v[3]];N=sum(0<a<T and 2*a!=T for a in qs)
        ck(N<2);ck(tuple(h) in allowed);ck(z==allowed[tuple(h)]['W'])
        found[tuple(h)]=N
ck(set(found)==set(allowed))
ck(10**10>2**4*9**9 and 65**4<2**25 and 128>121)
actual=[audit(list(truth)) for truth in product((-1,1),repeat=8)]
source=Path(r'~\brain_workers\FEI100_20261011\agents\A032\runs\20261013T221334Z-account05-A032-boolean-phase-realizability\out\witness.json')
witness=json.loads(source.read_text(encoding='utf-8'));wa=audit(witness['truth_table'])
ck([row['w'] for row in wa['rows']]==witness['masses'])
ck(W(witness['truth_table'])==witness['walsh_integers'])
out={'result':'PASS','endpoint_rows_recomputed':625,'product_endpoint_rows':len(found),'actual_Boolean_truth_tables':256,'imported_witness_audit':wa,'assertions':checks,'runtime_seconds':time.perf_counter()-t0,'log_interval_terms':20,'external_independent_review':'not claimed'}
(R/'out'/'independent_validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='imported_witness_audit'},indent=2))
