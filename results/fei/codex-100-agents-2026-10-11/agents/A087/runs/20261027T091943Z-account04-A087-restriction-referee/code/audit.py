from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, hashlib, time, itertools, sys

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[2]
SRC=ROOT/'A061/runs/20261027T044753Z-account04-A061-entropy-process'
def save(name,obj):
    p=RUN/name;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def prepare():
    (RUN/'out').mkdir(exist_ok=True)
    protocol=Path(r'math-open-problems/reports\fei-2026-10-11')
    supplement=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
    paths=[protocol/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
    paths += [supplement/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    paths += sorted((supplement/'sources').glob('*.txt'))+sorted((supplement/'sources').glob('*.md'))
    paths += sorted((ROOT.parents[0]/'context').glob('*.txt'))
    paths += [SRC/x for x in ['PROOF.md','REPORT.md','CLAIMS.json']]
    paths += [RUN.parent/'20261023T143823Z-account03-A087-restriction-referee'/x for x in ['PROOF.md','PROGRESS.json']]
    receipts=[];locators=[]
    for p in paths:
        if not p.exists():
            receipts.append({'path':str(p),'missing':True});continue
        raw=p.read_bytes();enc='utf-8-sig'
        try:s=raw.decode(enc)
        except UnicodeDecodeError:enc='cp1252';s=raw.decode(enc)
        receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'decoded_as':enc})
        hits=[{'line':i,'text':line[:350]} for i,line in enumerate(s.splitlines(),1) if any(w.lower() in line.lower() for w in ['A087','A061','C019','C024','restriction','composition identity','Proposition 8.1'])]
        locators.append({'path':str(p),'hits':hits[:18]})
    save('out/SOURCES.json',receipts);save('out/LOCATORS.json',locators)
    spec={'helper_version':'A087-audit-v1','helper_sha256':sha(Path(__file__)),
      'family':'labelled point signs; disjoint two-block products; rare activation of full point tensor',
      'domain':'point s=1..7 all physical coordinates and both children; two-block Bellman r=1..3, s1,s2=r..5; activated true tables (m,t)=(2,1..3),(3,1); compressed m=2..6,t=1..8,r=1..m',
      'case_count':{'point_coordinate_cases':28,'two_block_start_cases':50,'direct_activation_sources':4,'compressed_parameter_triples':160},
      'symmetry':'none on direct spectra; Bellman uses proven identical residual point laws and exchange of literal identical block states',
      'arithmetic':'integer Walsh/physical edges; Fraction probability; 50-term rational atanh logarithm enclosures with explicit geometric tails; interval comparisons',
      'memory_estimate_mb':90,'max_runtime_seconds':55,'pilot_max_seconds':55,
      'checks_that_can_fail':['wrong physical branch weights','inherited exact versus replaced product reference','source-zero atoms removed','adaptive stop above endpoint maximum','r=1 deterministic character','r=m immediate install','omitted full terminal H or KL','physical primeness without relevance','activation entropy formula','spent old debit reused']}
    save('FROZEN_SPEC.json',spec)
    print(json.dumps({'prepared':True,'sources':len(receipts),'missing':[x['path'] for x in receipts if x.get('missing')],'spec':spec},indent=2))

# Outward rational intervals. ln(x)=k ln(2)+2 atanh(z), y=x/2^k in [1,2).
@lru_cache(None)
def atanh_log(y):
    z=(y-1)/(y+1);n=50
    a=2*sum((z**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    err=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return a,a+err
@lru_cache(None)
def log2(x):
    x=F(x);assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(F(2)**k)
    if y<1:k-=1;y*=2
    if y>=2:k+=1;y/=2
    lo,hi=atanh_log(y);l2,u2=atanh_log(F(2))
    return F(k)+lo/u2,F(k)+hi/l2
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def entropy(p):
    z=(F(0),F(0))
    for x in p:
        if x:z=add(z,scale(log2(x),-x))
    return z
def cross(p,q):
    z=(F(0),F(0))
    for x,y in zip(p,q):
        if x:assert y>0;z=add(z,scale(log2(y),-x))
    return z
def maxiv(a,b):return max(a[0],b[0]),max(a[1],b[1])
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def ge(a,b):return a==b or a[0]>=b[1]
def walsh(f):
    v=list(f);h=1
    while h<len(v):
        for s in range(0,len(v),2*h):
            for j in range(s,s+h):a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
        h*=2
    return [F(x,len(v)) for x in v]
def direct_walsh(f):
    return [sum(F(y*(-1 if (s&x).bit_count()%2 else 1),len(f)) for x,y in enumerate(f)) for s in range(len(f))]
def child(f,i,b):
    return [f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2)]
def influence(f,i):return F(sum(y!=f[x^(1<<i)] for x,y in enumerate(f)),len(f))
def spectrum(f):return [x*x for x in walsh(f)]
def margprod(p):
    n=(len(p)-1).bit_length();m=[sum(v for s,v in enumerate(p) if s>>i&1) for i in range(n)]
    return [prod(m[i] if s>>i&1 else 1-m[i] for i in range(n)) for s in range(1<<n)]
def prod(v):
    z=F(1)
    for x in v:z*=x
    return z
def point(s):return [-1]+[1]*((1<<s)-1)
@lru_cache(None)
def H(s):return entropy(spectrum(point(s))) if s else (F(0),F(0))
@lru_cache(None)
def M(s):
    d=F(2)**(1-s);return scale(entropy([d,1-d]),s)
def K(s):return scale(M(s),F(2)**(s-1))

def run():
    t0=time.monotonic();checks=0
    def ck(b):
        nonlocal checks
        assert b;checks+=1
        assert time.monotonic()-t0<55,'frozen timeout'
    spec=json.loads((RUN/'FROZEN_SPEC.json').read_text(encoding='utf-8'))
    ck(spec['helper_sha256']==sha(Path(__file__)))
    # Every physical point child, exact-reference row masses and post-reset full CE.
    pointcases=0
    for s in range(1,8):
        f=point(s);a=walsh(f);p=[x*x for x in a];q=margprod(p);d=F(2)**(1-s)
        ck(sum(p)==sum(q)==1);ck(p[0]==(1-d)**2);ck(all(x==d*d for x in p[1:]))
        ck(overlap(cross(p,q),M(s)));ck(ge(M(s),H(s)))
        if s<=4:ck(a==direct_walsh(f))
        for i in range(s):
            pointcases+=1; ck(influence(f,i)==d)
            aa=[a[(j&((1<<i)-1))|((j>>i)<<(i+1))] for j in range(len(a)//2)]
            bb=[a[(j&((1<<i)-1))|((j>>i)<<(i+1))|(1<<i)] for j in range(len(a)//2)]
            laws=[]
            for b in (0,1):
                law=[(x+(-1 if b else 1)*y)**2 for x,y in zip(aa,bb)]
                ck(sum(law)==1);ck(law==spectrum(child(f,i,b)));laws.append(law)
            ck(ge(H(s),scale(add(entropy(laws[0]),entropy(laws[1])),F(1,2))))
        for r in range(1,s+1):
            v=maxiv(H(s),scale(M(r),F(2)**(r-s)))
            ck(ge(v,H(s)))
            if s>r:ck(ge(v,scale(maxiv(H(s-1),scale(M(r),F(2)**(r-s+1))),F(1,2))))
    # Independent Bellman recursion maximizes stopping, actual install, and either block query.
    # States are live dimensions >0, dead=0, installed=-1. Complete CE includes frozen Q atoms.
    states=0;starts=0
    for r in range(1,4):
        @lru_cache(None)
        def bell(state):
            nonlocal states
            states+=1
            current=(F(0),F(0))
            for s in state:current=add(current,M(r) if s==-1 else H(s))
            best=current
            for j,s in enumerate(state):
                if s==r:
                    ch=list(state);ch[j]=-1;best=maxiv(best,bell(tuple(ch)))
                elif s>r:
                    dead=list(state);dead[j]=0;live=list(state);live[j]=s-1
                    best=maxiv(best,scale(add(bell(tuple(dead)),bell(tuple(live))),F(1,2)))
            return best
        for s1 in range(r,6):
            for s2 in range(r,6):
                starts+=1
                expected=add(maxiv(H(s1),scale(M(r),F(2)**(r-s1))),maxiv(H(s2),scale(M(r),F(2)**(r-s2))))
                ck(overlap(bell((s1,s2)),expected))
    # Direct activated truth tables. No formula implementation imported from A061.
    direct=[]
    for m,t in [(2,1),(2,2),(2,3),(3,1)]:
        N=1<<(m-1);nb=m*N;delta=F(1,1<<t)
        g=[prod(point(m)[(x>>(m*j))&((1<<m)-1)] for j in range(N)) for x in range(1<<nb)]
        mu=sum(g,F(0))/len(g);a=1-mu
        z=[g[x>>t] if x&((1<<t)-1)==0 else 1 for x in range(1<<(nb+t))]
        p=spectrum(z);hz=entropy(p);inf=sum((influence(z,i) for i in range(nb+t)),F(0))
        ck(inf==delta*(m+t*a));ck(all(x>0 for x in p));ck(all(influence(z,i)>0 for i in range(nb+t)))
        ck(ge(scale((inf,inf),7),hz))
        gp=spectrum(g)
        for s,v in enumerate(p):
            c=s&((1<<t)-1);u=s>>t
            want=(1-delta*a)**2 if s==0 else delta*delta*a*a if u==0 else delta*delta*gp[u]
            ck(v==want)
        for i in range(t):ck(all(x==1 for x in child(z,i,1)))
        for r in range(1,m+1):
            ck(ge(maxiv(hz,scale(K(r),delta)),hz))
        direct.append({'m':m,'t':t,'n':nb+t,'I':str(inf),'H_interval':[str(x) for x in hz]})
    # Compressed all-dimensional formula controls on frozen finite parameter grid.
    triples=0
    for m in range(2,7):
        dm=F(2)**(1-m);N=1<<(m-1);mu=(1-dm)**N;a=1-mu;hg=scale(H(m),N)
        ck(ge((F(4*m),F(4*m)),hg))
        for t in range(1,9):
            de=F(1,1<<t);inf=de*(m+t*a)
            # Partition into empty, empty-core/nonempty-control, and nonempty-core sectors.
            hz=entropy([(1-de*a)**2])
            hz=add(hz,scale(entropy([de*de*a*a]),(1<<t)-1))
            nonempty=add(hg,scale(entropy([mu*mu]),-1))
            hz=add(hz,scale(nonempty,de))
            hz=add(hz,(2*t*de*(1-mu*mu),)*2)
            ck(ge((7*inf,7*inf),hz))
            for r in range(1,m+1):
                triples+=1;kr=K(r)
                ck(ge(kr,(F(r*(r-1)),)*2));ck(kr[1]<F(r*(2*r+1),2))
                if r*r<=m:
                    cap=maxiv(hz,scale(kr,de))
                    ck(ge((7*inf,7*inf),cap)) # 8I-old debit I, one original owner.
    result={'status':'PASS','assertions':checks,'point_coordinate_cases':pointcases,'bellman_start_cases':starts,'bellman_states':states,'direct_activation_sources':direct,'compressed_triples':triples,'elapsed_seconds':time.monotonic()-t0,'arithmetic':'exact rationals and outward atanh intervals','formal_rung':'analytic reconstruction + exact validation; no Lean certificate'}
    save('out/AUDIT.json',result);print(json.dumps({k:v for k,v in result.items() if k!='direct_activation_sources'},indent=2))

if __name__=='__main__':
    prepare() if sys.argv[1]=='prepare' else run()
