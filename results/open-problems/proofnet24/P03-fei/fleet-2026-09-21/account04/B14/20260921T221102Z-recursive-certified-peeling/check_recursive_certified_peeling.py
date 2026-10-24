import itertools, math, random
from functools import lru_cache

def fwht(v):
    a=[float(x) for x in v]; n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def entropy(ps):
    return sum(p*math.log2(1/p) for p in ps if p>1e-15)

def spectrum(v):
    return [x*x for x in fwht(v)]

def H(v): return entropy(spectrum(v))

def h2(p):
    if p<=0 or p>=1: return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def influences(v,n):
    out=[]
    for i in range(n):
        c=0
        for x in range(1<<n):
            if ((x>>i)&1)==0:
                c += (v[x]!=v[x^(1<<i)])
        out.append(c/(1<<(n-1)))
    return out

def center(v,n):
    p=influences(v,n); T=[i for i,x in enumerate(p) if x>0.5+1e-12]
    g=list(v)
    for x in range(1<<n):
        if sum((x>>i)&1 for i in T)&1: g[x]*=-1
    return tuple(g)

def restrict(v,n,Z,a):
    Z=tuple(Z); rem=[i for i in range(n) if i not in Z]; out=[]
    for y in range(1<<len(rem)):
        x=0
        for t,i in enumerate(rem):
            if (y>>t)&1: x|=1<<i
        for t,i in enumerate(Z):
            if (a>>t)&1: x|=1<<i
        out.append(v[x])
    return tuple(out),rem

def block_B(v,n,Z):
    ps=spectrum(v); comp=[i for i in range(n) if i not in Z]; m={}
    for S,p in enumerate(ps):
        key=tuple((S>>i)&1 for i in comp); m[key]=m.get(key,0.0)+p
    return H(v)-entropy(m.values())

def pivotal(v,n,j):
    others=[i for i in range(n) if i!=j]; eta=[]
    for y in range(1<<(n-1)):
        x=0
        for t,i in enumerate(others):
            if (y>>t)&1: x|=1<<i
        eta.append(int(v[x]!=v[x^(1<<j)]))
    return eta,others

def subcube(others,Z,a):
    pos=[others.index(i) for i in Z]; out=[]
    for y in range(1<<len(others)):
        out.append(int(all(((y>>p)&1)==((a>>t)&1) for t,p in enumerate(pos))))
    return out

def crossing(v,n,j,Z):
    s=0.0
    for a in range(1<<len(Z)):
        ch,rem=restrict(v,n,Z,a); jj=rem.index(j); p=influences(ch,n-len(Z))[jj]
        s+=max(2*p-1,0.0)
    return s/(1<<len(Z))

def find_cert(v,n):
    v=center(v,n)
    if n<=1: return v,None
    p=influences(v,n); mx=max(p,default=0.0)
    for j,x in enumerate(p):
        if x<=1e-12 or abs(x-mx)>1e-12: continue
        eta,others=pivotal(v,n,j)
        for r in range(1,len(others)+1):
            q=2.0**(-r); thr=q/(16*r)
            for Z in itertools.combinations(others,r):
                for a in range(1<<r):
                    Q=subcube(others,Z,a); e=sum(x!=y for x,y in zip(eta,Q))/len(eta)
                    if e<=thr+1e-12: return v,(j,tuple(Z),e,x,r)
    return v,None

def step(v,n,c):
    j,Z,e,pj,r=c; p=influences(v,n); Iz=sum(p[i] for i in Z); cr=crossing(v,n,j,Z)
    Hp=H(v); Hc=Jc=0.0
    for a in range(1<<r):
        ch,_=restrict(v,n,Z,a); Hc+=H(ch)/(1<<r)
        pc=influences(ch,n-r); Jc+=sum(min(x,1-x) for x in pc)/(1<<r)
    J=sum(min(x,1-x) for x in p); return {
        'B':block_B(v,n,Z),'dH':Hp-Hc,'I':Iz,'D':J-Jc,'cross':cr,'p':pj,
        'v_cross':(1-1/(16*r-1))*pj-cr,'v_h':Iz-h2(pj),'v_c1':Hp-Hc-12*Iz,'v_d':Iz-(J-Jc)}

@lru_cache(None)
def tree(v,n):
    v,c=find_cert(v,n); p=influences(v,n) if n else []; J=sum(min(x,1-x) for x in p)
    if c is None: return dict(B=0.0,dH=0.0,I=0.0,D=0.0,h=0.0,leafH=H(v),leafJ=J)
    s=step(v,n,c); out=dict(B=s['B'],dH=s['dH'],I=s['I'],D=s['D'],h=h2(s['p']),leafH=0.0,leafJ=0.0)
    Z=c[1]; r=c[4]
    for a in range(1<<r):
        ch,_=restrict(v,n,Z,a); z=tree(ch,n-r); w=1/(1<<r)
        for k in out: out[k]+=w*z[k]
    return out

def check_case(v,n,agg):
    v=center(v,n); p=influences(v,n); J=sum(p); rootH=H(v); vc,c=find_cert(v,n)
    if c:
        agg['cert_roots']+=1; s=step(vc,n,c); agg['cert_steps']+=1
        for key,sk in [('cross','v_cross'),('h','v_h'),('c1','v_c1'),('drift','v_d')]: agg['max_'+key]=max(agg['max_'+key],s[sk])
    z=tree(v,n); agg['cases']+=1
    agg['max_B12J']=max(agg['max_B12J'],z['B']-12*J)
    agg['max_dH12J']=max(agg['max_dH12J'],z['dH']-12*J)
    agg['max_IJ']=max(agg['max_IJ'],z['I']-J); agg['max_DJ']=max(agg['max_DJ'],z['D']-J)
    agg['max_h']=max(agg['max_h'],z['h']-(32/15)*J)
    agg['max_Htel']=max(agg['max_Htel'],abs(z['dH']-(rootH-z['leafH'])))
    agg['max_Jtel']=max(agg['max_Jtel'],abs(z['D']-(J-z['leafJ'])))

def blank():
    return {'cases':0,'cert_roots':0,'cert_steps':0,'max_cross':-1e9,'max_h':-1e9,'max_c1':-1e9,'max_drift':-1e9,
            'max_B12J':-1e9,'max_dH12J':-1e9,'max_IJ':-1e9,'max_DJ':-1e9,'max_Htel':0.0,'max_Jtel':0.0}

small=blank()
for n in range(1,4):
    for mask in range(1<<(1<<n)):
        check_case(tuple(1 if (mask>>x)&1 else -1 for x in range(1<<n)),n,small)
print('exhaustive_n_le_3',small)

sample=blank(); rng=random.Random(20260921)
for _ in range(2000):
    check_case(tuple(1 if rng.getrandbits(1) else -1 for _ in range(16)),4,sample)
print('random_n_4',sample)
