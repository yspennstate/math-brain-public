from pathlib import Path
from fractions import Fraction as F
import itertools,json,time
R=Path(__file__).resolve().parents[1]; begin=time.perf_counter(); count=0
def check(v):
    global count
    count+=1
    assert v,count
def log(x):
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    def series(z):
        a=sum((2*z**(2*j+1)/F(2*j+1) for j in range(48)),F(0))
        return a,a+2*z**97/(97*(1-z*z))
    l,u=series((x-1)/(x+1)); a,b=series(F(1,3))
    return k+l/b,k+u/a
def spectrum(table):
    return [sum(v*(-1 if (i&s).bit_count()%2 else 1) for i,v in enumerate(table)) for s in range(len(table))]
def H(table):
    N=len(table); ans=[F(0),F(0)]
    for w in spectrum(table):
        if w:
            p=F(w*w,N*N); a,b=log(1/p); ans[0]+=p*a; ans[1]+=p*b
    return ans
def query_table(history):
    # Independent coordinate assignment, not restriction slicing.
    names=['y0','y1','y2','y3','x','z','A','B']; free=[k for k in names if k not in history]
    out=[]
    for row in range(1<<len(free)):
        d=dict(history); d.update({k:(row>>i)&1 for i,k in enumerate(free)})
        val=(-1)**(d['z']+d['y0']*d['y1']+d['y2']*d['y3'])
        label=0 if d['A'] else (1 if d['B'] else 2)
        y=sum(d['y'+str(i)]*(1<<i) for i in range(4))
        if label and not d['x'] and y==label-1: val=-val
        out.append(val)
    return out,free
f,names=query_table({'x':0}); i=names.index('y0')
d=F(sum(v!=f[j^(1<<i)] for j,v in enumerate(f)),len(f)); check(d==F(9,16))
children=[query_table({'x':0,'y0':b})[0] for b in (0,1)]
hf=H(f); hh=[H(g) for g in children]; D=[hf[0]-(hh[0][1]+hh[1][1])/2,hf[1]-(hh[0][0]+hh[1][0])/2]
check(D[1]<5*d)
f,names=query_table({'x':0,'y0':0}); i=names.index('y1'); spec=spectrum(f); N=len(f)
dr=F(sum(v!=f[j^(1<<i)] for j,v in enumerate(f)),N); check(dr==F(1,16))
B=[F(0),F(0)]
for s in range(N):
    if (s>>i)&1: continue
    a=F(spec[s]**2,N*N); b=F(spec[s|(1<<i)]**2,N*N)
    for q in (a,b):
        if q:
            lo,hi=log((a+b)/q); B[0]+=q*lo; B[1]+=q*hi
check(B[0]>F(5,2)*dr)
pi=(F(1,2),F(1,4),F(1,4))
for bits in itertools.product((0,1),repeat=3):
    q=sum(p*b for p,b in zip(pi,bits))
    lhs=2*sum(pi[j]*pi[k]*(bits[j]!=bits[k]) for j in range(3) for k in range(j+1,3))
    check(lhs==2*q*(1-q))
record={'status':'PASS','assertions':count,'second_query_decrement_interval':list(map(str,D)),'rebound_erasure_interval':list(map(str,B)),'rebound_influence':str(dr),'seconds':time.perf_counter()-begin,'method':'direct DFT, independently generated assignments; no production helper import'}
(R/'out/REPLAY.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline=''); print(json.dumps(record))
