"""Own exponential-series derivation and exact complete Bernstein leaf replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb,lcm,factorial
from datetime import datetime
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
OUT=HERE/'t067_fourth_own';OUT.mkdir(exist_ok=True)
started=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_bytes((json.dumps(d,indent=2)+'\n').encode('utf-8'))
proof=W/'proofs/T067-FOURTH-DERIVATIVES-001_v1.md'
assert sha(proof)=='c0f285f87e817086133cd22e9b1f6e3c690308124c7cd6aaa0f1f8867c2415da'
rp=W/'checks/fourth_derivative_v1/report.json'
assert sha(rp)=='ea392acae0bb563dbc963e902f17423b2387a589a3bd337763740d874a5c27bf'
report=json.loads(rp.read_text(encoding='utf-8'))
a,b,t,u,v=s.symbols('a b t u v');p=[a,b,1-a-b];h=[0,t,1]
def ex(f):return s.Poly(s.expand(f),a,b,t).as_expr()
# Expand sum p_i^2 exp(2 h_i e)/(sum p_i exp(h_i e))^2, then Q.
Z=[s.Integer(1)]+[ex(sum(p[i]*h[i]**k for i in range(3))/factorial(k)) for k in range(1,5)]
Z2=[ex(sum(Z[j]*Z[k-j] for j in range(k+1))) for k in range(5)]
inv=[s.Integer(1)]
for k in range(1,5):inv.append(ex(-sum(Z2[j]*inv[k-j] for j in range(1,k+1))))
num=[ex(sum(p[i]**2*(2*h[i])**k for i in range(3))/factorial(k)) for k in range(5)]
AA=[ex(9*sum(num[j]*inv[k-j] for j in range(k+1))-(3 if k==0 else 0)) for k in range(5)]
der=[ex(factorial(k)*sum(AA[j]*AA[k-j] for j in range(k+1))) for k in range(5)]
def D(i,f):return ex(a*(int(i==0)-p[i])*s.diff(f,a)+b*(int(i==1)-p[i])*s.diff(f,b))
V=[D(i,der[2]) for i in range(3)];assert ex(sum(V))==0
N=s.Rational(2,3)*(1-t+t*t);gv=D(0,der[0])/2
polys={'Gv_-1':8-gv,'Gv_+1':8+gv,
       'D2_-1':20*N-der[2],'D2_+1':20*N+der[2],
       'D4_-1':99*N*N-der[4],'D4_+1':99*N*N+der[4],
       'D3_squared':38**2*N**3-der[3]**2,
       'D3_mixed_squared':38**2*N*N-sum(q*q for q in V)}
save(OUT/'phase.json',{'phase':'series formed','seconds':time.monotonic()-started})
def indices(shape):return product(*(range(n) for n in shape))
def root_bern(power,shape):
    arr={ix:power.get(ix,F(0)) for ix in indices(shape)}
    for axis,n1 in enumerate(shape):
        nxt={}
        for ix in indices(shape):
            j=ix[axis];acc=F(0)
            for i in range(j+1):
                old=list(ix);old[axis]=i
                acc+=arr[tuple(old)]*F(comb(j,i),comb(n1-1,i))
            nxt[ix]=acc
        arr=nxt
    den=lcm(*(q.denominator for q in arr.values()))
    return {ix:int(q*den) for ix,q in arr.items()}
def split(arr,shape,axis):
    n=shape[axis]-1;other=[i for i in range(3) if i!=axis];left={};right={}
    for rest in product(*(range(shape[i]) for i in other)):
        ix=[0,0,0]
        for i,q in zip(other,rest):ix[i]=q
        line=[]
        for j in range(n+1):ix[axis]=j;line.append(arr[tuple(ix)])
        for level in range(n+1):
            ix[axis]=level;left[tuple(ix)]=line[0]*(1<<(n-level))
            ix[axis]=n-level;right[tuple(ix)]=line[-1]*(1<<(n-level))
            line=[line[j]+line[j+1] for j in range(len(line)-1)]
    return left,right
receipts=[]
assert len(report['jobs'])==len(polys)==8
for number,job in enumerate(report['jobs']):
    f=polys[job['name']]
    name=job['name'];dest=OUT/(name+'.json')
    polynomial=s.Poly(s.expand(f.subs({a:u,b:(1-u)*v},simultaneous=True)),u,v,t)
    power={ix:F(int(c.p),int(c.q)) for ix,c in polynomial.terms() if c}
    saved={tuple(ix):F(c) for ix,c in job['root_power_terms'] if F(c)}
    assert power==saved,(name,'independent raw polynomial mismatch')
    shape=tuple(d+1 for d in polynomial.degree_list());assert shape==tuple(job['shape'])
    leaves={q['path'] for q in job['leaves']}
    assert len(leaves)==len(job['leaves']) and not job['stack']
    assert all(set(path)<={'0','1'} for path in leaves)
    assert all(not any(path[:j] in leaves for j in range(len(path))) for path in leaves)
    assert sum((F(1,1<<len(path)) for path in leaves),F(0))==1
    needed={path[:j] for path in leaves for j in range(len(path)+1)}
    stack=[('',root_bern(power,shape))];passed=[]
    while stack:
        path,arr=stack.pop()
        if path in leaves:
            minimum=min(arr.values());assert minimum>=0,(name,path,minimum)
            passed.append({'path':path,'minimum':str(minimum)});continue
        lower,upper=split(arr,shape,len(path)%3)
        assert path+'0' in needed and path+'1' in needed
        stack.extend([(path+'1',upper),(path+'0',lower)])
    result={'name':name,'shape':shape,'leaves':len(passed),'exact_cover':True,
            'status':'PASS own polynomial and all complete-cover leaf signs',
            'leaf_results':passed,'elapsed_seconds':time.monotonic()-started}
    save(dest,result);receipts.append({'file':dest.name,'sha256':sha(dest),'leaves':len(passed)})
    save(OUT/'phase.json',{'phase':name,'completed':number+1,'seconds':time.monotonic()-started})
    print(name,len(passed),'PASS',flush=True)
assert sum(r['leaves'] for r in receipts)==124
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS independent exponential-series polynomials, all124 leaves and exact whole-cube covers',
     'proof_sha256':sha(proof),'report_sha256':sha(rp),'script_sha256':sha(Path(__file__)),
     'files':receipts,'seconds':time.monotonic()-started,
     'scope':'Global Q derivative bounds only. No compensated Gaussian gate or cutoff admission. Lead account4.'}
save(HERE/'T067_FOURTH_DERIVATIVES_LEAD_RECEIPT.json',out)
print(json.dumps({k:out[k] for k in ['status','seconds']}),flush=True)
