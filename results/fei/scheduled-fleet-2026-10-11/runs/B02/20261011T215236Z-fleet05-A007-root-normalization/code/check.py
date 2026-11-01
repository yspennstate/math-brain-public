"""A007 exact root-normalization checker v1; no floating-point signs."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import json, time, hashlib

RUN = Path(__file__).resolve().parents[1]
cases = [(r, ws) for r in range(1,5) for m in range(1,4)
         for ws in combinations_with_replacement(range(1,4),m) if r+sum(ws)<=10]
spec = dict(helper_version='A007-check-v1', family='shared r-conjunction AND OR of disjoint conjunction petals',
            parameter_domain='r=1..4, m=1..3, sorted widths=1..3, n<=10', case_count=len(cases),
            symmetry='petal permutations preserve truth law and canonical root-count ledger; sorted widths only',
            arithmetic='integer FWHT, Fraction identities; analytic logarithm bounds in REPORT.md',
            memory_estimate_bytes=20_000_000, max_runtime_seconds=60,
            additional_domain='all 270 nonconstant truth tables on 1..3 data bits, each r=1..4; 1080 cases',
            automatic_dimension_escalation=False)
(RUN/'out').mkdir(exist_ok=True)
(RUN/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf8')
if '--freeze' in __import__('sys').argv:
    print(json.dumps(spec)); raise SystemExit
assert (RUN/'FROZEN_SPEC.json').exists()
start=time.perf_counter(); checks=0
def ck(value):
    global checks
    checks+=1
    assert value, checks
def fwht(vals):
    a=list(vals); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    # mask bit=1 denotes physical +1, so standard Walsh has a sign per degree
    return [F(z*(-1 if k.bit_count()%2 else 1),len(a)) for k,z in enumerate(a)]
def edge_influence(vals,n):
    return sum((F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
                for i in range(n)),F(0))
def activation_check(bvals,r,root_count=None):
    n=(len(bvals)).bit_length()-1; p=F(1,2**r); b=F(sum(bvals),len(bvals))
    bh=fwht(bvals); gh=fwht([2*z-1 for z in bvals]); ig=edge_influence([2*z-1 for z in bvals],n)
    vals=[2*bvals[x>>r]*int((x & ((1<<r)-1))==((1<<r)-1))-1 for x in range(2**(n+r))]
    fh=fwht(vals); v=1-fh[0]**2; ei=F(0); ek=F(0)
    ck(v==4*p*b*(1-p*b))
    ck(edge_influence(vals,n+r)==p*ig+2*r*p*b)
    for a,z in enumerate(fh):
        u=a&((1<<r)-1); t=a>>r
        ck(z==(2*p*bh[t] if a else 2*p*b-1))
        ei+=a.bit_count()*z*z
        if a:
            k=1 if u else (root_count(t) if root_count else 1)
            ck(1<=k<=a.bit_count())
            if not u: ck(k<=t.bit_count())
            ek+=k*z*z
    ck(ei==p*ig+2*r*p*b)
    ck(0<=ek-v<=p*p*ig)
    ck(r*(ek-v)<=F(1,2)*p*ig)
    ck(r*p<=F(1,2))
    return b,ig,v,ek

rows=[]
for r,ws in cases:
    masks=[]; offset=0
    for w in ws:
        masks.append(((1<<w)-1)<<offset); offset+=w
    bvals=[int(any(x&q==q for q in masks)) for x in range(2**offset)]
    rho=[F(1,2**w) for w in ws]; q=F(1)
    for z in rho: q*=1-z
    p=F(1,2**r)
    count=lambda t: sum(bool(t&q0) for q0 in masks)
    b,ig,v,ek=activation_check(bvals,r,count)
    ck(b==1-q)
    ck(ig==2*q*sum((w*z/(1-z) for w,z in zip(ws,rho)),F(0)))
    ck(ek-v==4*p*p*q*(sum(rho,F(0))-b))
    lam=F(1,len(ws)); s=sum((lam*z for z in rho),F(0)); d=F(1)
    for z in rho: d*=1+p*lam*z
    d-=1
    # D >= a, and D <= a/(1-a), an exact elementary normalizer enclosure.
    a=p*s
    ck(a<=d<=a/(1-a))
    total=F(0)
    for bits in product((0,1),repeat=len(ws)):
        if not any(bits): continue
        num=F(1)
        for bit,z in zip(bits,rho):
            if bit: num*=p*lam*z
        total+=num/d
    ck(total==1)
    # cancellation is an exact rational multiplicative identity, before taking logs
    for z in rho: ck(d/(p*lam*z)==(d/(p*s))*(s/(lam*z)))
    rows.append(dict(r=r,widths=ws,v=str(v),influence=str(p*ig+2*r*p*b),extra_roots=str(ek-v),D=str(d)))

arbitrary=0
for n in range(1,4):
    for table in range(1,(1<<(1<<n))-1):
        bvals=[(table>>x)&1 for x in range(1<<n)]
        for r in range(1,5):
            activation_check(bvals,r); arbitrary+=1

elapsed=time.perf_counter()-start
result=dict(helper_version='A007-check-v1',petal_cases=len(cases),arbitrary_activation_cases=arbitrary,
            assertions_passed=checks,elapsed_seconds=elapsed,arithmetic=spec['arithmetic'],cases=rows)
ck(elapsed<60)
(RUN/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
