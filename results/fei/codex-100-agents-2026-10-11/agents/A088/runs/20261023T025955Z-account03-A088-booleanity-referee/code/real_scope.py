import json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v,s):
    global checks
    checks+=1
    if not v:raise AssertionError(s)
    if time.perf_counter()-start>55:raise TimeoutError(s)
def signs(v):
    n=len(v)
    return [sum((a*(-1)**((s&x).bit_count()) for x,a in enumerate(v)),F())/n for s in range(n)]
def dirichlet(v,j):return sum(((v[x]-v[x^(1<<j)])**2 for x in range(len(v))),F())/(4*len(v))
def root():
    out=[]
    # Original labels: first pair 0,1; second pair 2,3; w 4; selector z 5.
    for x in range(64):
        b=(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1)))
        out.append(F(b)-2*((x&31)==0 and bool(x&32)))
    return out
def cut(v,labels,q,b):
    j=labels.index(q)
    return [v[x] for x in range(len(v)) if (x>>j)&1==b],[q for i,q in enumerate(labels) if i!=j]
def transform(v,labels):
    j,k=labels.index(2),labels.index(3)
    return [v[x]-sum((v[(x&~((1<<j)|(1<<k)))|(a<<j)|(b<<k)] for a in (0,1) for b in (0,1)),F())/2 for x in range(len(v))]
v=root();lab=list(range(6));tv=transform(v,lab)
cases=[('root',[]),('clean',[(5,0)]),('edited',[(5,1)]),('edited_zero',[(5,1),(0,0)]),('edited_exit',[(5,1),(0,1)]),('partner_zero',[(5,1),(0,0),(1,0)]),('partner_one',[(5,1),(0,0),(1,1)])]
rows=[]
for name,path in cases:
    a=v;b=tv;labels=lab
    for q,value in path:
        old=labels;a,labels=cut(a,old,q,value);b,_=cut(b,old,q,value)
    ck(b==transform(a,labels),'commutation with actual physical restrictions')
    ca,cb=signs(a),signs(b)
    ck([x*x for x in ca]==[x*x for x in cb],'complete actual Fourier spectrum preserved')
    ck(sum(x*x for x in b)==len(b),'actual real child normalized')
    for j in range(len(labels)):ck(dirichlet(a,j)==dirichlet(b,j),'every physical Dirichlet influence preserved')
    ck(any(x not in (-1,1) for x in b),'actual nonBoolean node')
    rows.append({'name':name,'physical_values':sorted({str(x) for x in b}),'norm_squared':str(sum(x*x for x in b)/len(b))})
c=signs(tv)
failures=[]
for t in range(1,64):
    conv=sum((c[s]*c[s^t] for s in range(64)),F())
    if conv:failures.append({'shift':t,'convolution':str(conv)})
ck(bool(failures),'nonempty Boolean phase convolution must fail')
out={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-start,'nodes':rows,'failed_Boolean_convolutions':failures,'interpretation':'All laws, full references, entropy and Dirichlet energies coincide; all nodes actual normalized nonBoolean real functions. Untouched-pair prefixes only.'}
(R/'out'/'REAL_SCOPE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
