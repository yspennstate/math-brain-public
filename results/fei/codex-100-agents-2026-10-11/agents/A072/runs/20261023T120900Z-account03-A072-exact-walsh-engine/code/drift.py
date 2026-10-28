"""Independent full-cube review and signed composition-drift certificates."""
from arithmetic import F,Q,log2,ceildiv,ROOT
from functools import lru_cache
from itertools import product
import json,time,sys

CHECKS=0
def ck(x):
    global CHECKS
    assert x
    CHECKS+=1
def add(*ps):
    d={}
    for p in ps:
        for k,v in p.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def times(p,c):return {k:v*c for k,v in p.items() if c*v}
def sub(a,b):return add(a,times(b,-1))
def mean(ps):return times(add(*ps),F(1,len(ps)))
def factor(n):
    d={};k=2
    while k*k<=n:
        while n%k==0:d[k]=d.get(k,0)+1;n//=k
        k+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def logprofile(p,c):
    out={}
    for k,v in factor(p.numerator).items():out=add(out,{k:c*v})
    for k,v in factor(p.denominator).items():out=add(out,{k:-c*v})
    return out
def entropy(ps):
    ck(sum(ps,F(0))==1)
    return add(*(logprofile(p,-p) for p in ps if p))
def phi(a,b):
    return add(logprofile(a+b,a+b),logprofile(a,-a) if a else {},logprofile(b,-b) if b else {}) if a+b else {}
@lru_cache(None)
def logs(k):return log2(F(k))
def iv(p):
    lo=hi=0
    for k,v in p.items():
        a,b=logs(k)
        if v<0:a,b=b,a
        lo+=a*v.numerator//v.denominator;hi+=ceildiv(b*v.numerator,v.denominator)
    return lo,hi
def nonnegative(p):ck(not p or iv(p)[0]>=0)
def pack(p):return {str(k):str(v) for k,v in sorted(p.items())}
def rec(p):return {'prime_log':pack(p),'bounds_2pow192':iv(p)}
def save(n,v):(ROOT/'out'/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def g(n):return tuple(-1 if x==0 else 1 for x in range(1<<n))
def restrict(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))

@lru_cache(None)
def spectral(t):
    N=len(t);n=N.bit_length()-1;W=list(t);h=1
    while h<N:
        for j in range(0,N,2*h):
            for x in range(j,j+h):a,b=W[x],W[x+h];W[x],W[x+h]=a+b,a-b
        h*=2
    # Independent direct characters, every inverse sign, separate physical edges.
    direct=[sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
    ck(W==direct);ck(sum(w*w for w in W)==N*N)
    for x in range(N):ck(sum(W[s]*(-1 if (x&s).bit_count()%2 else 1) for s in range(N))==N*t[x])
    edges=[];ds=[]
    for i in range(n):
        e=sum(t[x]!=t[x|1<<i] for x in range(N) if not x>>i&1);d=F(2*e,N)
        ck(d==sum(F(w*w,N*N) for s,w in enumerate(W) if s>>i&1));edges.append(e);ds.append(d)
    # Entropy follows the integer validation, never precedes it.
    H=entropy([F(w*w,N*N) for w in W])
    return dict(truth=t,W=W,H=H,I=sum(ds,F(0)),ds=ds,edges=edges)

def compose(ts,outer=None):
    r=len(ts);outer=tuple(1 if x==0 else -1 for x in range(1<<r)) if outer is None else outer
    ns=[len(t).bit_length()-1 for t in ts];offs=[];z=0
    for n in ns:offs.append(z);z+=n
    truth=tuple(outer[sum((ts[j][(x>>offs[j])&((1<<ns[j])-1)]==-1)<<j for j in range(r))] for x in range(1<<z))
    # Validate ALL core integer spectra and full integers before their entropies are used.
    cs=[spectral(t) for t in ts];s=spectral(truth);mus=[F(sum(t),len(t)) for t in ts];qs=[]
    for j in range(r):
        q=F(0)
        for x in range(1<<r):
            if x>>j&1 or outer[x]==outer[x|1<<j]:continue
            p=F(1)
            for k,m in enumerate(mus):
                if k!=j:p*=(1-m)/2 if x>>k&1 else (1+m)/2
            q+=p
        qs.append(q);ck(sum(s['ds'][offs[j]:offs[j]+ns[j]],F(0))==q*cs[j]['I'])
    C=sub(s['H'],add(*(times(c['H'],q) for c,q in zip(cs,qs))))
    return dict(s,cores=cs,q=qs,C=C,ns=ns,offs=offs,outer=outer,ts=ts)

def erasure(s,i):
    N=len(s['truth']);W=s['W'];ps=[];B={}
    for x in range(N):
        if x>>i&1:continue
        a,b=F(W[x],N),F(W[x|1<<i],N);ps.append(a*a+b*b);B=add(B,phi(a*a,b*b))
    children=[spectral(restrict(s['truth'],i,b)) for b in [0,1]]
    JS=sub(entropy(ps),mean([c['H'] for c in children]));Delta=sub(s['H'],mean([c['H'] for c in children]))
    ck(Delta==add(B,JS));nonnegative(JS)
    return B,JS,Delta

def row(p,j,i):
    bit=p['offs'][j]+i;ts=p['ts'];kids=[]
    for b in [0,1]:
        tt=list(ts);tt[j]=restrict(tt[j],i,b);kids.append(compose(tuple(tt),p['outer']))
    d=p['ds'][bit];ck(d==p['q'][j]*p['cores'][j]['ds'][i]);ck(p['I']-sum(k['I'] for k in kids)/2==d)
    bf,jf,df=erasure(p,bit);bg,jg,dg=erasure(p['cores'][j],i)
    mu=F(sum(ts[j]),len(ts[j]));t=F(p['cores'][j]['W'][1<<i],len(ts[j]));ph=phi(mu*mu,t*t)
    others=((1<<p['ns'][j])-1)<<p['offs'][j];others^=1<<bit;special={};N=len(p['truth'])
    for x in range(N):
        if x>>bit&1 or x&others:continue
        special=add(special,phi(F(p['W'][x]**2,N*N),F(p['W'][x|1<<bit]**2,N*N)))
    ck(bf==add(times(sub(bg,ph),p['q'][j]),special))
    drift=sub(mean([k['C'] for k in kids]),p['C']);ck(drift==sub(times(dg,p['q'][j]),df))
    ck(drift==sub(times(add(ph,jg),p['q'][j]),add(special,jf)))
    nonnegative(sub(times(add(ph,jg),p['q'][j]),drift))
    reserve={2:6*d};nonnegative(sub(reserve,drift))
    bank=add(p['C'],{2:6*p['I']});childbanks=[add(k['C'],{2:6*k['I']}) for k in kids]
    for a in [bank]+childbanks:nonnegative(a)
    excess=sub(bank,mean(childbanks));nonnegative(excess)
    credit=[add(a,excess) for a in childbanks];ck(mean(credit)==bank)
    # At K=3 these source inner hulls vanish. Preserve full-function solvency.
    for k,a in zip(kids,credit):nonnegative(add({2:3*k['I']},sub(a,k['H'])))
    return dict(core=j,coordinate=i,physical_bit=bit,influence=str(d),C_drift=rec(drift),inner_zero_row=rec(ph),inner_JS=rec(jg),full_JS=rec(jf),full_special_erasure=rec(special),reserve_released=str(6*d),coherence_surplus=rec(excess),child_credits=[rec(a) for a in credit],integer_children=[dict(W=k['W'],edge_counts=k['edges'],I=str(k['I'])) for k in kids])

def main():
    start=time.perf_counter();p=compose((g(3),g(2),g(2)))
    rows=[row(p,0,0)] if '--pilot' in sys.argv else [row(p,j,i) for j in range(3) for i in range(p['ns'][j])]
    kids=[compose((g(2),g(2),g(2))),compose(((1,)*4,g(2),g(2)))]
    cp={2:F(57,8),3:F(-1431,1024),7:F(-3087,2048)}
    c0={2:F(53,8),3:F(-1701,512),5:F(-25,512)};c1={2:F(3),3:F(-27,16)}
    G={2:F(-37,16),3:F(-567,512),5:F(-25,1024),7:F(3087,2048)}
    ck(p['C']==cp);ck(kids[0]['C']==c0);ck(kids[1]['C']==c1);ck(sub(mean([c0,c1]),cp)==G)
    for c in [cp,c0,c1,G]:ck(iv(c)[0]>0)
    ck(p['I']==F(111,64));ck(p['ds'][0]==F(9,64));ck([k['I'] for k in kids]==[F(27,16),F(3,2)])
    powers=[2**14592>3**2862*7**3087,2**3392>3**1701*5**25,2**48>3**27,7**3087>2**4736*3**2268*5**50,3**9>2**14]
    for b in powers:ck(b)
    corrupt=add(G,{2:F(1,1024)});ck(corrupt!=sub(mean([kids[0]['C'],kids[1]['C']]),p['C']))
    save('PILOT.json' if '--pilot' in sys.argv else 'VALIDATION.json',dict(verdict='PASS',checks=CHECKS,rows=len(rows),runtime_seconds=time.perf_counter()-start,source_claim='A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1',source_C=[rec(c) for c in [cp,c0,c1]],source_drift=rec(G),integer_power_checks=powers,corrupt_drift_rejected=True,source_W=p['W'],source_edges=p['edges'],physical_rows=rows))
    print(json.dumps(dict(verdict='PASS',checks=CHECKS,rows=len(rows),runtime_seconds=time.perf_counter()-start,drift=rec(G))))
if __name__=='__main__':main()
