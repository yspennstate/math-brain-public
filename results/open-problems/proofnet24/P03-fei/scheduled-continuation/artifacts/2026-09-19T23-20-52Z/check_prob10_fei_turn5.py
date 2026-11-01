from itertools import product
from math import log2, comb
import json, hashlib, pathlib

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def entropy_probs(p):
    return -sum(x*log2(x) for x in p if x>0)

def fourier_probs(f):
    N=len(f); W=fwht(f)
    return [(w/N)**2 for w in W]

def influence_dir(f,v):
    N=len(f)
    return sum(1 for x in range(N) if f[x]!=f[x^v])/N

def rank_add(basis,v):
    x=v
    while x:
        i=x.bit_length()-1
        if i in basis: x^=basis[i]
        else: basis[i]=x; return True
    return False

def min_affine(f):
    N=len(f); n=N.bit_length()-1
    vals=[]
    for v in range(1,N):
        a=influence_dir(f,v); vals.append((min(a,1-a),v))
    vals.sort(); B={}; s=0.0
    for c,v in vals:
        if rank_add(B,v):
            s+=c
            if len(B)==n: break
    return s

def derivative(f,z):
    return [f[x]*f[x^z] for x in range(len(f))]

def dcross_and_delta(f):
    N=len(f); H=entropy_probs(fourier_probs(f)); M=min_affine(f)
    EH=EM=0.0
    for z in range(N):
        g=derivative(f,z)
        EH+=entropy_probs(fourier_probs(g))/N
        EM+=min_affine(g)/N
    return 2*H-EH,2*M-EM,H,M

def majority(n):
    N=1<<n
    return [1 if x.bit_count()>n//2 else -1 for x in range(N)]

def erasure_F(p,n,t):
    H=entropy_probs(p); val=0.0
    for mask in range(1<<n):
        k=mask.bit_count(); w=(t**k)*((1-t)**(n-k))
        comp=((1<<n)-1)^mask; d={}
        for s,ps in enumerate(p):
            y=s&comp; d[y]=d.get(y,0.0)+ps
        val+=w*(H-entropy_probs(d.values()))
    return val

def erasure_B(p,n):
    ans=0.0; full=(1<<n)-1
    for i in range(n):
        comp=full^(1<<i); groups={}
        for s,ps in enumerate(p):
            y=s&comp; bit=(s>>i)&1
            if y not in groups: groups[y]=[0.0,0.0]
            groups[y][bit]+=ps
        for a,b in groups.values():
            m=a+b
            if m>0:
                q=b/m
                if 0<q<1: ans+=m*(-q*log2(q)-(1-q)*log2(1-q))
    return ans

def algebraic_degree(f):
    N=len(f); n=N.bit_length()-1
    a=[0 if y==1 else 1 for y in f]
    for i in range(n):
        for m in range(N):
            if m&(1<<i): a[m]^=a[m^(1<<i)]
    return max((m.bit_count() for m,c in enumerate(a) if c),default=0)

def J(f):
    n=(len(f)).bit_length()-1
    return sum(min(influence_dir(f,1<<i),1-influence_dir(f,1<<i)) for i in range(n))

out={'status':'PASS','full_FEI_proved':False,'independent_audit':False,'checks':{}}
maj=[]
for n in (3,5,7,9):
    f=majority(n); D,Delta,H,M=dcross_and_delta(f)
    a=comb(n-1,(n-1)//2)/(2**(n-1))
    assert abs(M-(n-1)*a)<1e-12
    maj.append({'n':n,'M':M,'D_cross':D,'Delta_aff':Delta,'ratio':D/Delta})
out['checks']['majority_small_exact_enumeration']=maj
ers=[]
for n in (2,3):
    N=1<<n; tests=[]
    for code in range(min(1<<N,32)):
        f=[1 if ((code>>x)&1)==0 else -1 for x in range(N)]
        p=fourier_probs(f); B=erasure_B(p,n)
        vals=[erasure_F(p,n,t) for t in (0.0,0.25,0.5,0.75,1.0)]
        assert abs(vals[0])<1e-10 and abs(vals[-1]-entropy_probs(p))<1e-10
        slopes=[(vals[i+1]-vals[i])/0.25 for i in range(4)]
        assert all(slopes[i+1]+1e-9>=slopes[i] for i in range(3))
        tests.append((B,vals))
    ers.append({'n':n,'tested':len(tests)})
out['checks']['erasure_flow']=ers
rows=[]
for n in (1,2,3):
    N=1<<n; count=0
    for code in range(1<<N):
        f=[1 if ((code>>x)&1)==0 else -1 for x in range(N)]
        d=algebraic_degree(f); H=entropy_probs(fourier_probs(f)); j=J(f)
        assert H <= 3*d*j + 1e-9
        for z in range(N): assert algebraic_degree(derivative(f,z)) <= max(0,d-1)
        count+=1
    rows.append({'n':n,'tested':count})
out['checks']['algebraic_degree_descent']=rows
path=pathlib.Path(__file__)
out['script_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
print(json.dumps(out,indent=2))
