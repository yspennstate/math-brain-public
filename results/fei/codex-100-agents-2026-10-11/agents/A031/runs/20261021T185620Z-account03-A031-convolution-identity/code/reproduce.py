"""Direct characters, physical edges, and a separate rational logarithm kernel."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic();checks=0;cache={}
def ck(b):
    global checks
    assert b
    checks+=1
def log(x):
    x=Q(x)
    if x in cache:return cache[x]
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def ln(z):
        t=(z-1)/(z+1)
        s=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
        return s,s+2*t**49/(49*(1-t*t))
    a,b=ln(x);c,d=ln(Q(2));v=Q(k)+a/d,Q(k)+b/c
    cache[(Q(2)**k)*x]=v
    return v
def cost(terms):
    lo=hi=Q(0)
    for c,x in terms:
        a,b=log(x)
        if c<0:a,b=b,a
        lo+=c*a;hi+=c*b
    return lo,hi
def add(*xs):return sum(x[0] for x in xs),sum(x[1] for x in xs)
def mul(v,c):return (v[0]*c,v[1]*c) if c>=0 else (v[1]*c,v[0]*c)
def entropy(p):return cost([(-z,z) for z in p if z])
def row(p,i):
    M=[];B=[]
    for s in range(len(p)):
        if s>>i&1:continue
        a,b=p[s],p[s|1<<i];r=a+b
        if b:M.append((b,r/b));B.append((b,r/b))
        if a:B.append((a,r/a))
    return cost(M),cost(B)
def characters(f):
    N=len(f)
    return [sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(f)) for s in range(N)]
def bounds(v):
    den=1<<80
    return [str(Q(v[0].numerator*den//v[0].denominator,den)),str(Q(-((-v[1].numerator*den)//v[1].denominator),den))]
def overlap(a,b):return a[0]<=Q(b[1]) and Q(b[0])<=a[1]
old=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
records=[]
for L in [1,2,3]:
    assert time.monotonic()-start<55
    n=2*L+4;N=1<<n
    clauses=[1|4|8,1|2|(((1<<L)-1)<<4),2|4|(((1<<L)-1)<<(L+4))]
    f=[-1 if any(not x&e for e in clauses) else 1 for x in range(N)]
    a=characters(f);p=[Q(z*z,N*N) for z in a]
    ck(sum(p)==1)
    if L==1:
        for u in range(N):ck(sum(a[s]*a[s^u] for s in range(N))==(N*N if not u else 0))
    for i in range(n):
        ck(Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N)==sum(p[s] for s in range(N) if s>>i&1))
    M=add(*(row(p,i)[0] for i in range(n)));Bx=row(p,3)[1]
    epriv=Q(sum(sum(f[x]!=f[x^(1<<i)] for x in range(N)) for i in range(3,n)),N)
    childcost=[];children=[];incoming=[]
    for s in [0,1]:
        # retain ambient labels; x is a dummy in each physical restriction.
        g=[f[(x&~8)|(s<<3)] for x in range(N)]
        b=characters(g);ps=[Q(z*z,N*N) for z in b]
        ck(sum(ps)==1)
        for t in range(N):
            if t&8:ck(b[t]==0)
            else:ck(Q(b[t],N)==Q(a[t]+(1 if s==0 else -1)*a[t|8],N))
        qs=[(ps[t&~2]+ps[t|2])/2 for t in range(N)]
        ck(sum(qs)==1)
        ce=cost([(-z,qs[t]) for t,z in enumerate(ps) if z]);childcost.append(ce);children.append(entropy(ps))
        inc=cost([(-z,p[t]+p[t|8]) for t,z in enumerate(ps) if z]);incoming.append(inc)
    bill=add(M,Bx,mul(add(*childcost),Q(1,2)))
    ck(bill[1]<17*epriv)
    reset=add(mul(add(*childcost),Q(1,2)),mul(add(*incoming),-Q(1,2)))
    ck(reset[1]<0 if L==1 else reset[0]>0)
    saved=next(z for z in old['cases'] if z['L']==L)
    ck(overlap(bill,saved['total_bill']));ck(overlap(M,saved['M_old_debit']))
    ck(overlap(reset,saved['signed_reset_price']))
    records.append({'L':L,'dimension':n,'bill':bounds(bill),'positive_margin':bounds((17*epriv-bill[1],17*epriv-bill[0])),'reset':bounds(reset)})
# Non-Boolean control: norm-one physical restrictions, but nonzero full convolution.
n=1<<18;L=(n-4)//2
ck(2*L+4==n);ck(19*n-2>17*(n-3));ck(Q(2,n)>0)
ans={'records':records,'assertions':checks,'runtime_seconds':time.monotonic()-start,'nonBoolean_control':{'n':n,'L':L,'full_bill':'19-2/n','source_bank':'17(n-3)/n','nonempty_convolution':'2/n'},'method':'independent direct-character spectra and physical edges; independent 24-term log bounds'}
ck(ans['runtime_seconds']<55)
(R/'out/REPRODUCTION.json').write_text(json.dumps(ans,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(records),'assertions':checks,'seconds':ans['runtime_seconds']}))
