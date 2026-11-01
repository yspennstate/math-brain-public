from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json,sys,time
R=Path(__file__).resolve().parents[1]; COUNT=0
def ck(t):
    global COUNT
    COUNT+=1
    if not t: raise AssertionError(COUNT)
def walsh(a):
    a=a[:]; h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def rank(vs):
    b={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in b: v^=b[j]
            else: b[j]=v; break
    return len(b)
@lru_cache(None)
def factors(x):
    d={}; q=2
    while q*q<=x:
        while x%q==0: d[q]=d.get(q,0)+1; x//=q
        q+=1
    if x>1: d[x]=d.get(x,0)+1
    return d
def add(*terms):
    d={}
    for v,c in terms:
        for p,x in v.items(): d[p]=d.get(p,F(0))+c*x
    return {p:c for p,c in d.items() if c}
def constant(x): return {2:F(x)} if x else {}
def hamp(x):
    x=abs(F(x))
    if not x: return {}
    return add((factors(x.numerator),-2*x*x),(factors(x.denominator),2*x*x))
def entropy(f):
    a=walsh(f); N=len(f)
    return add(*[(hamp(F(v,N)),1) for v in a])
def inf(f):
    a=walsh(f); N=len(f)
    return F(sum(s.bit_count()*v*v for s,v in enumerate(a)),N*N)
def minority(f):
    N=len(f); d=N.bit_length()-1; a=walsh(f)
    w=[F(sum(a[s]**2 for s in range(N) if (s&v).bit_count()%2),N*N) for v in range(N)]
    m=[min(x,1-x) for x in w]
    return w,m
def release(f,exhaust=False,physical=False):
    d=len(f).bit_length()-1; w,m=minority(f); coords=[1<<j for j in range(d)]
    if physical:
        for v in range(1,len(f)):
            ck(w[v]==F(sum(f[x]!=f[x^v] for x in range(len(f))),len(f)))
    basis=[]; a=F(0)
    for v in sorted(range(1,len(f)),key=lambda v:(m[v],v)):
        if rank(basis+[v])>len(basis): basis.append(v); a+=m[v]
    ck(len(basis)==d)
    levels=sorted(set([F(0),F(1,2)]+m[1:])); integral=F(0); bins=[]
    for lo,hi in zip(levels,levels[1:]):
        rr=rank([v for v in range(1,len(f)) if m[v]<=lo]); nn=sum(m[v]<=lo for v in coords)
        ck(rr>=nn); integral+=(hi-lo)*(rr-nn)
        bins.append([str(lo),str(hi),rr,nn])
    chi=sum(w[v]-m[v] for v in coords)
    ck(inf(f)-a==chi+integral)
    if exhaust:
        costs=[sum(m[v] for v in vs) for vs in combinations(range(1,len(f)),d) if rank(vs)==d]
        ck(min(costs)==a)
    return {'I':inf(f),'a':a,'rho':inf(f)-a,'chi':chi,'bins':bins,'basis':basis}
def series(z):
    t=z; s=F(0)
    for j in range(32): s+=2*t/(2*j+1); t*=z*z
    return s,s+2*t/(65*(1-z*z))
@lru_cache(None)
def lnprime(p):
    k=p.bit_length()-1; unit=1<<k
    l2,h2=series(F(1,3)); l,h=series(F(p-unit,p+unit)); l+=k*l2; h+=k*h2
    sc=1<<96
    return F(l.numerator*sc//l.denominator,sc),F(-(-h.numerator*sc//h.denominator),sc)
def interval(v):
    lo=hi=F(0)
    for p,c in v.items():
        l,h=lnprime(p); lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
    l2,h2=lnprime(2); corners=[x/y for x in [lo,hi] for y in [l2,h2]]
    return min(corners),max(corners)
def positive(v):
    if not v: return False
    return interval(v)[0]>0
def E(k,H,mu):
    p=F(1,1<<k); b=1-mu
    return add((H,p),(hamp(1-p*b),1),(hamp(mu),-p),(hamp(b),p*(1-p)),(constant(2*k*p*((1-mu*mu)+(1-p)*b*b)),1))
def root(k):
    f=[]
    for x in range(1<<(k+4)):
        a,b,c,z=[x>>j&1 for j in range(4)]
        q=(-1)**((a*b+a*c+b*c+z*a)%2)
        f.append(q if x>>4==0 else 1)
    return f
def children(f): return [[f[x] for x in range(len(f)) if x&3==u] for u in range(4)]
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,list): return [encode(v) for v in x]
    return x
def main():
    start=time.perf_counter(); pilot='--pilot' in sys.argv; ns=range(3) if pilot else range(4)
    roots=0; eligible=0; profiles=[]
    for n in ns:
        for t in range(1<<(1<<n)):
            f=[1-2*(t>>x&1) for x in range(1<<n)]
            release(f,exhaust=True,physical=True); roots+=1
        ck(time.perf_counter()-start<52)
    for d in ([3] if pilot else [3,5,7]):
        f=[]
        for x in range(1<<d):
            last=x>>(d-1)&1
            e=sum(((x>>(2*j)&1)^last)*((x>>(2*j+1)&1)^last) for j in range((d-1)//2))%2
            f.append((-1)**e)
        info=release(f)
        ck(info['rho']==F(1,2) and info['chi']==0)
        ck(info['I']==F(d,2) and info['a']==F(d-1,2))
        ck(sum(F(1,2) for _ in range(d))==d*info['rho'])
    for k in ([2] if pilot else [2,3,4]):
        p=F(1,1<<k); f=root(k); H=entropy(f); w,m=minority(f)
        ck(H==E(k,constant(4),F(1,4))); ck(inf(f)==p*(2+F(3*k,4)))
        ck(w[1]==w[2]==p/2)
        for v in range(1,len(f)):
            ck(m[v]>=max(w[1<<j] for j in range(k+4) if v>>j&1))
        ch=children(f); infos=[release(g) for g in ch]
        ck([z['rho'] for z in infos]==[0,p,0,0]); ck(all(z['chi']==0 for z in infos))
        ck([inf(g) for g in ch]==[0,(k+2)*p,(k+1)*p,(k+1)*p])
        ck([entropy(g) for g in ch]==[{},E(k,{},F(0)),E(k,{},F(0)),E(k,{},F(0))])
        L=add((H,1),*[(entropy(g),F(-1,4)) for g in ch])
        Delta=add((hamp(1-3*p/4),1),(hamp(1-p),F(-3,4)))
        exact=add((constant(15*p/4+3*k*p*p/8),1),(hamp(F(3,4)),p*(1-p)),(Delta,1))
        ck(L==exact)
        rho=sum(z['rho'] for z in infos)/4; ck(rho==p/4)
        K=F(15,4); paid=add((constant(K*(p+rho)),1),(L,-1))
        ck(positive(add((paid,1),(constant(5*p/128),-1))))
        ck(positive(add((L,1),(constant(K*p),-1))))
        # Exact whole-terminal signed account, including any negative terminal.
        D=add((H,1),(constant(K*inf(f)),-1))
        S=add(*[(constant(K*z['a']),F(1,4)) for z in infos],*[(entropy(g),F(-1,4)) for g in ch])
        ck(add((D,1),(S,1),(paid,1))=={})
        profiles.append({'k':k,'rho':rho,'physical_I_A':p,'paid_margin_bits':list(interval(paid)),'L_bits':list(interval(L)),'child_banks':infos})
    for k in ([2,16] if pilot else range(2,21)):
        p=F(1,1<<k); L=add((E(k,constant(4),F(1,4)),1),(E(k,{},F(0)),F(-3,4)))
        ck(positive(add((constant(F(595,128)*p),1),(L,-1))))
        if k>=16: ck(positive(add((E(k,{},F(0)),1),(constant(F(15,4)*(k+1)*p),-1))))
        ck(time.perf_counter()-start<52)
    ck(3**9>2**14); ck(F(15,4)*F(5,4)-F(595,128)==F(5,128))
    out={'status':'PASS','pilot':pilot,'small_tables':roots,'checks':COUNT,'profiles':profiles,'seconds':time.perf_counter()-start}
    (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(encode(out),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='profiles'}))
if __name__=='__main__': main()
