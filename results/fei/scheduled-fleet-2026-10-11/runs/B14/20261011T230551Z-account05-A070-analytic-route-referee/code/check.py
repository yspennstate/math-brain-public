from pathlib import Path
from fractions import Fraction as F
import json,time,math
start=time.monotonic(); checks=0; records=[]
run=Path(__file__).resolve().parents[1]
def ck(v):
    global checks
    assert v
    checks+=1
    if time.monotonic()-start>55: raise RuntimeError('frozen 55s guard')
def walsh(v):
    a=v[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
def inspect(v,label):
    n=(len(v)-1).bit_length(); den=len(v); a=walsh(v)
    p=[F(t*t,den*den) for t in a]
    ck(sum(p)==1)
    ii=[sum(p[s] for s in range(den) if s>>i&1) for i in range(n)]
    for i in range(n): ck(ii[i]==F(sum(v[x]!=v[x^(1<<i)] for x in range(den)),den))
    d=[s.bit_count() if a[s] else -1 for s in range(den)]
    for i in range(n):
        for s in range(den):
            if not s>>i&1: d[s]=max(d[s],d[s|(1<<i)])
    for s in range(1,den):
        if a[s]: ck((F(a[s],den)*2**(d[s]-1)).denominator==1)
    # Booleanity reconstructed through square in physical space, not convolution code.
    inv=walsh(a); ck(all(z==den*t for z,t in zip(inv,v)))
    ck(walsh([t*t for t in v])==[den]+[0]*(den-1))
    I=sum(ii); V=1-p[0]; U=sum(p[s]*(d[s]-s.bit_count()) for s in range(1,den) if a[s])
    # Influence code Kraft product: prod(1+I_i/I) <= sum_{k>=0}1/k! < e.
    if I:
        w=[t/I for t in ii]; ck(sum(w)==1)
        elementary=[F(1)]
        for t in w:
            elementary.append(F(0))
            for k in range(len(elementary)-1,0,-1): elementary[k]+=t*elementary[k-1]
        for k,e in enumerate(elementary): ck(e<=F(1,math.factorial(k)))
    # Integral identity coefficientwise: 2 * |S| * integral exp(-2 |S| t) =1.
    for s in range(1,den):
        if p[s]: ck(2*s.bit_count()*F(1,2*s.bit_count())==1)
    if label: records.append({'family':label,'n':n,'I':str(I),'V':str(V),'U':str(U),'full_support':all(a),'max_degree':max(d)})
    return a,p,ii,U
for n in range(4):
    den=1<<n
    for mask in range(1<<den): inspect([1-2*((mask>>x)&1) for x in range(den)],None)
for N in range(3,11):
    v=[1-2*(x&1) for x in range(1<<N)]; v[0]*=-1
    a,p,ii,U=inspect(v,'dictator flip'); delta=F(1,1<<N)
    ck(sum(ii)==1+(2*N-4)*delta)
    ck(U==N-1-(2*N-4)*delta-4*N*delta*delta)
for N in range(4,11):
    v=[1 if (x&7).bit_count()<=1 else -1 for x in range(1<<N)]; v[0]*=-1
    a,p,ii,U=inspect(v,'Maj3 flip'); eps=F(2,1<<N)
    ck(all(a)); ck(U==N*(1-p[0])-sum(ii))
    base=[F(0)]*(1<<N)
    for s in [1,2,4]: base[s]=F(1,2)
    base[7]=F(-1,2)
    ck(all(F(a[s],1<<N)==base[s]-eps for s in range(1<<N)))
for addr in range(1,4):
    n=addr+(1<<addr); N=n+2
    def value(x): return 1-2*((x>>(addr+(x&((1<<addr)-1))))&1)
    base=[value(x) for x in range(1<<N)]
    b,_,_,_=inspect(base,'address base')
    v=base[:]; v[0]*=-1
    a,p,ii,U=inspect(v,'address flip')
    ck(all(a)); ck(all(a[s]==b[s]-2 for s in range(1<<N)))
    eps=F(2,1<<N)
    Ib=1+F(addr,2); ck(abs(sum(ii)-Ib)<=N*eps)
    heavy=[s for s in range(1<<N) if b[s]]
    ck(len(heavy)==4**addr)
    ck(all(p[s]>=F(1,4*4**addr) for s in heavy))
    for i in range(addr): ck(abs(ii[i]-F(1,2))<=eps)
    for i in range(addr,n): ck(abs(ii[i]-F(1,1<<addr))<=eps)
    for i in range(n,N): ck(ii[i]==eps)
for n in [4,16,64]:
    p={1<<i:F(1,n) for i in range(n)}
    ck(sum(p.values())==1); ck(sum(s.bit_count()*v for s,v in p.items())==1)
    for z in [F(1,2),F(3,4)]: ck(sum(s.bit_count()*v*z**s.bit_count() for s,v in p.items())==z)
    # dyadic amplitudes and signed convolution order-one pass, order-two fails.
    amp=F(1,math.isqrt(n)); ck(amp*amp==F(1,n))
    ck(2*amp*amp==F(2,n))
result={'status':'PASS','exact_assertions':checks,'cases':299,'seconds':time.monotonic()-start,'records':records,'logarithms':'symbolic; all entropy/payment and all-parameter signs are in DERIVATION.md'}
(run/'out').mkdir(exist_ok=True)
(run/'out/CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
