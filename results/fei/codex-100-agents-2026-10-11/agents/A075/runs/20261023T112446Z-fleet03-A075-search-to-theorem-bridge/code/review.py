"""Independent A075 reconstruction; executes no A084/A072 code."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json, hashlib, time, sys
import review_log as ar
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[3]
SOURCE=BASE/'agents/A084/runs/20261023T105943Z-fleet03-A084-continuum-parameters'
def write(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def pack(x):return {str(k):str(v) for k,v in sorted(x.items()) if v}
def unpack(x):return {int(k):F(v) for k,v in x.items() if F(v)}
checks=0
start=time.perf_counter()
def ck(x):
    global checks
    assert x
    checks+=1
def add(a,b,c=F(1)):return ar.add(a,b,c)
def scale(a,c):return ar.scale(a,c)
def cmp(a,b):
    z=add(a,b,F(-1))
    if not z:return 0
    lo,hi=ar.enclose(z)
    ck(lo>0 or hi<0)
    return 1 if lo>0 else -1
def maxf(a,b):return a if cmp(a,b)>=0 else b
def avg(a,b):return scale(add(a,b),F(1,2))
@lru_cache(None)
def factors(n):
    ck(n>0)
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,F(0))+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,F(0))+1
    return out
def logq(q):return add(factors(q.numerator),factors(q.denominator),F(-1))
def eta(q):return scale(logq(q),-q) if q else {}
def entropy(t):
    w=ar.fwht(t);N=len(t);h={}
    for a in w:h=add(h,eta(F(a*a,N*N)))
    return h,w
def influence(t):
    N=len(t)
    return sum((F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range((N-1).bit_length())),F(0))
def prod(xs):
    ans=F(1)
    for x in xs:ans*=x
    return ans
def guard(t,d,r):
    n=(len(t)-1).bit_length()
    return tuple((-1)**((z>>(d+n)).bit_count())*(t[(z>>d)&(len(t)-1)] if z&((1<<d)-1)==0 else 1) for z in range(1<<(n+d+r)))
def guarded_h(t,d):
    H,w=entropy(t);N=len(t);mu=F(w[0],N);a=1-mu;v=1-mu*mu;delta=F(1,1<<d)
    h=eta((1-delta*a)**2)
    h=add(h,add(eta(a*a),{2:2*d*a*a}),delta-delta*delta)
    h=add(h,add(add(H,eta(mu*mu),F(-1)),{2:2*d*v}),delta)
    return h,delta*(influence(t)+d*a)
def frozen():
    spec={'version':'A075-independent-guard-review-v1','actual_family':'G_d=disjoint parity times seed if all d physical selectors zero, else parity; full24bit seed Fplus retained',
      'pilot':'4 one-bit seeds,d=0,1,r=0,1:16 complete Walsh/edge/entropy checks',
      'domain':'all16 two-bit seeds,d=0,1,2,r=0,1,2:144 complete spectra; seed24 by16 occupied sectors; toy seed negativeonly00,d=0,1,2,r=2,K=1,3/2:6 complete augmented DAGs; no automatic expansion',
      'case_count':{'pilot':16,'spectra':144,'seed':1,'augmented_DAGs':6},
      'symmetry':'none; every physical admission/query retained in toy DAGs',
      'arithmetic':'integer FWHT/direct characters, Fraction edges, prime-log exact identities, own192bit80term atanh directed intervals; floating time only',
      'memory_estimate_mb':180,'pilot_max_seconds':55,'maximum_runtime_seconds_per_command':180,
      'helper_sha256':hashlib.sha256((ROOT/'code/review_log.py').read_bytes()).hexdigest(),'peer_executable_imported':False}
    write('FROZEN_SPEC.json',spec)
    pins=[]
    for n in ['REPORT.md','PROOF.md','CLAIMS.json','out/SEED_CERTIFICATE.json','out/RATE_EXTENSION.json','out/EXPLICIT_WITNESS.json']:
        p=SOURCE/n;pins.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    write('SOURCE_PINS.json',pins)
def spectra(pilot=False):
    n=1 if pilot else 2;dmax=1 if pilot else 2;rmax=dmax;cases=[]
    for table in range(1<<(1<<n)):
        t=tuple(-1 if table>>x&1 else 1 for x in range(1<<n));ht,wt=entropy(t);mu=F(wt[0],len(t));a=1-mu
        for d in range(dmax+1):
            for r in range(rmax+1):
                gt=guard(t,d,r);h,w=entropy(gt);N=len(gt);totalbits=(N-1).bit_length();D=1<<d
                ck(sum(x*x for x in w)==N*N)
                # Independent direct character reconstruction of every integer coefficient.
                for A in range(N):
                    ck(w[A]==sum(v*(-1)**((A&x).bit_count()) for x,v in enumerate(gt)))
                for x in range(N):ck(sum(v*(-1)**((A&x).bit_count()) for A,v in enumerate(w))==N*gt[x])
                Ih=influence(gt);ck(Ih==sum((F(v*v,N*N)*A.bit_count() for A,v in enumerate(w)),F(0)))
                expectH,expectI=guarded_h(t,d);ck(h==expectH);ck(Ih==expectI+r)
                # Check the coefficient formula including the empty atom and parity shift.
                for A in range(N):
                    sel=A&(D-1);B=(A>>d)&((1<<n)-1);par=A>>(d+n)
                    coeff=F(0)
                    if par==(1<<r)-1:
                        coeff=(1-F(a,D)) if sel==B==0 else (-F(a,D) if B==0 else F(wt[B],D*len(t)))
                    ck(F(w[A],N)==coeff)
                cases.append({'table':table,'n':n,'d':d,'r':r,'I':str(Ih),'H':pack(h)})
                ck(time.perf_counter()-start<(55 if pilot else 180))
    out={'status':'PASS','case_count':len(cases),'checks':checks,'seconds':time.perf_counter()-start,'cases':cases}
    write('PILOT.json' if pilot else 'SPECTRA.json',out)
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
def seed():
    g=tuple(-1 if x in {0,1,2} else 1 for x in range(64));Hg,Wg=entropy(g);Ig=influence(g)
    ck(Ig==F(7,16));ck(sum(z*z for z in Wg)==4096)
    for A in range(64):ck(Wg[A]==sum(v*(-1)**((A&x).bit_count()) for x,v in enumerate(g)))
    hh={0,1,2,4,8,16,32,6,17,40};K=tuple(1 if x<<2 in hh else -1 for x in range(16));WK=ar.fwht(K)
    mu=F(sum(g),64);v=1-mu*mu;ps=F(1-mu,2);masses=[];coeffs=[];H={};I=F(0)
    # Centered four-variable expansion: only16 occupied sectors, independent of source's50625 literal groups.
    for T in range(16):
        c=sum((F(w,16)*mu**((U^T).bit_count()) for U,w in enumerate(WK) if U&T==T),F(0))
        coeffs.append(c);mass=c*c*v**T.bit_count();masses.append(mass);H=add(H,eta(mass))
    ck(sum(masses)==1)
    for x in range(16):ck(sum((coeffs[T]*prod(((-1 if x>>j&1 else 1)-mu) for j in range(4) if T>>j&1) for T in range(16)),F(0))==K[x])
    q=[]
    for j in range(4):
        qj=sum((ps**x.bit_count()*(1-ps)**(3-x.bit_count()) for x in range(16) if not(x>>j&1) and K[x]!=K[x^(1<<j)]),F(0))
        q.append(qj);ck(sum(masses[T] for T in range(16) if T>>j&1)==qj*v)
        H=add(H,add(Hg,add(eta(v),eta(1-v)),F(-1)),qj);I+=qj*Ig
    # Independent bias derivative / physical pivot check of each outer coefficient.
    for j in range(4):
        ck(q[j]==sum((prod(ps if x>>k&1 else 1-ps for k in range(4) if k!=j) for x in range(16) if not(x>>j&1) and K[x]!=K[x^(1<<j)]),F(0)))
    original=json.loads((SOURCE/'out/SEED_CERTIFICATE.json').read_text(encoding='utf-8'))
    ck(H==unpack(original['H']));ck(I==F(original['I']));ck(I==F(98637,524288))
    A4=add(H,{2:4*I},F(-1));ck(A4==unpack(original['A4']))
    endpoint=add(H,{2:F(33,8)*I},F(-1));ck(cmp(A4,{2:F(7,256)})>0);ck(cmp(endpoint,{2:F(1,256)})>0)
    ck(F(4,1<<20)*(26+40)==F(33,131072));ck(F(33,131072)<F(1,256));ck(4*7>=24+3)
    result={'status':'PASS','method':'own16 centered occupied sectors, direct inner characters/edges and outer literal pivots; no peer executable imported','H':pack(H),'I':str(I),'mean':str(coeffs[0]),'sector_mass':[str(x) for x in masses],
      'A4':pack(A4),'endpoint_A_33_over_8':pack(endpoint),'endpoint_interval':[str(x) for x in ar.enclose(endpoint)],'strict_floor':'1/256',
      'closed_real_rate_interval':['4','33/8'],'d20_hull_upper':'33/131072','d20_reach':'1/1048576','physical_bits':51,'checks':checks,'seconds':time.perf_counter()-start}
    write('SEED_REVIEW.json',result);print(json.dumps({k:result[k] for k in ['status','I','checks','seconds']}))
def toy(d,k):
    t=(-1,1,1,1);r=2;f=guard(t,d,r);n=d+4
    @lru_cache(None)
    def stats(state):
        tt=tuple(f[x] for x in range(1<<n) if all(s<2 or ((x>>i)&1)==s-2 for i,s in enumerate(state)))
        H,w=entropy(tt);I=influence(tt);b=maxf({},add(H,{2:k*I},F(-1)))
        ck(sum(z*z for z in w)==len(tt)**2);return H,I,b
    def change(state,i,b):return state[:i]+(b,)+state[i+1:]
    @lru_cache(None)
    def rho(state):
        ans=stats(state)[2]
        for i,s in enumerate(state):
            if s==1:ans=maxf(ans,avg(rho(change(state,i,2)),rho(change(state,i,3))))
        return ans
    # All4^n augmented states, forward minimum arrival offsets, independent of author's backward capital.
    states=sorted(product(range(4),repeat=n),key=lambda s:sum(2 if x==0 else 1 if x==1 else 0 for x in s),reverse=True)
    root=(0,)*n;arrivals={root:{}};witness={root:[]};T={};worst=[];rows=0
    for state in states:
        ck(state in arrivals);a=arrivals[state];need=add(stats(state)[2],a,F(-1))
        if cmp(need,T)>0:T=need;worst=witness[state]
        def push(child,value,edge):
            if child not in arrivals or cmp(value,arrivals[child])<0:
                arrivals[child]=value;witness[child]=witness[state]+[edge]
        for i,s in enumerate(state):
            if s==0:push(change(state,i,1),a,['admit',i])
            elif s==1:
                children=[change(state,i,b) for b in (2,3)];rs=[rho(c) for c in children];mean=avg(*rs)
                for b,c in enumerate(children):push(c,add(a,add(rs[b],mean,F(-1))),['query',i,b])
                rows+=1
        ck(time.perf_counter()-start<180)
    R=rho((1,)*n);A=add(entropy(t)[0],{2:k*influence(t)},F(-1));ck(cmp(A,{})>0);ck(cmp(T,A)>=0)
    # Actual selector-only past: every possible admission/order prefix, BOTH outcomes retained.
    selectorstates=[]
    for sel in product(range(4),repeat=d):
        state=sel+(0,)*4;ck(not rho(state));selectorstates.append(list(sel))
    ck(not arrivals[(2,)*d+(0,)*4]);ck(cmp(rho((2,)*d+(1,)*4),A)>=0)
    result={'d':d,'rate':str(k),'parity_bits':r,'physical_bits':n,'states':len(states),'query_rows':rows,'R':pack(R),'T':pack(T),'seed_need':pack(A),'worst_original_path':worst,'selector_prefixes_checked':len(selectorstates),'checks':checks,'seconds':time.perf_counter()-start,'status':'PASS'}
    write('TOY_d'+str(d)+'_K'+str(k).replace('/','_')+'.json',result);print(json.dumps({a:result[a] for a in ['d','rate','states','checks','seconds','status']}))
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='freeze':frozen()
    elif mode=='pilot':spectra(True)
    elif mode=='spectra':spectra()
    elif mode=='seed':seed()
    elif mode=='toy':toy(int(sys.argv[2]),F(sys.argv[3]))
    else:raise ValueError(mode)
