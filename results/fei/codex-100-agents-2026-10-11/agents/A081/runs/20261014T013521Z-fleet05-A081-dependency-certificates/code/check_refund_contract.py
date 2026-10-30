"""Independent complete-row/coarsening audit; direct character sums and rational logs."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib,sys,math
R=Path(__file__).resolve().parents[1]
def save(name,obj):(R/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
pilot='--pilot' in sys.argv
spec={'helper_version':'A081-row-coarsening-v1','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'actual_Boolean_family':'24 named core signs (all 4 one-bit, all 16 two-bit, four n3 masks 1,7,105,150) tensored with six named spectators; one actual tribes width4,m16 compressed spectrum','domain':{'cores':24,'spectators':['constant','dictator','AND2 point defect','quadratic bent2','three-bit point defect','quadratic bent4'],'partitions':['total residual degree','core degree and spectator degree','full core residual subset and spectator degree'],'tribes_width':4,'tribes_blocks':16},'case_count':{'actual_tensor_functions':144,'coarsening_cases_per_relevant_core_row':3,'tribes_degree_packets':64},'pilot':'one three-bit point defect core, six spectators, same three partitions and width4 tribes fixture','symmetry':'No tensor symmetry reduction; tribes uses proved coordinate transitivity only, not fixed-degree exchangeability','arithmetic':'direct integer character sums; Fraction laws; exact prime-log coefficient cancellation; integer occupancy-polynomial mixtures for tribes','memory_estimate_MB':64,'maximum_runtime_seconds':60,'automatic_dimension_escalation':False}
save('FROZEN_SPEC.json',spec);start=time.perf_counter();checks=0
def ck(b):
    global checks
    assert b;checks+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen runtime cap')
@lru_cache(None)
def factors(n):
    d=2;out={}
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(a,b,s=F(1)):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,F(0))+s*v
    return {k:v for k,v in out.items() if v}
def log(q,s=F(1)):
    q=F(q);return add({k:s*v for k,v in factors(q.numerator).items()},{k:s*v for k,v in factors(q.denominator).items()},F(-1))
def KL(p,q):
    out={}
    for t,v in p.items():
        if v:out=add(out,log(v/q[t],v))
    return out
def law(vals):
    N=len(vals);a=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(vals)) for s in range(N)]
    P=[F(v*v,N*N) for v in a];ck(sum(P)==1);return P
def row(P,i):
    e=sum(v for s,v in enumerate(P) if s&(1<<i));N=len(P)
    if not e:return None
    mu={s:P[s|(1<<i)]/e for s in range(N) if not s&(1<<i)}
    rr={s:P[s]+P[s|(1<<i)] for s in mu};ck(sum(mu.values())==sum(rr.values())==1)
    return e,mu,rr
def coarse(mu,rr,C):
    a={};b={}
    for t,v in mu.items():
        c=C(t);a[c]=a.get(c,F(0))+v;b[c]=b.get(c,F(0))+rr[t]
    cond={};hybrid={}
    for t,v in mu.items():
        c=C(t)
        hybrid[t]=b[c]*v/a[c] if a[c] else rr[t]
        if v:cond=add(cond,log((v/a[c])/(rr[t]/b[c]),v))
    ck(sum(a.values())==sum(b.values())==sum(hybrid.values())==1)
    ck(KL(mu,rr)==add(KL(a,b),cond))
    ck(KL(mu,hybrid)==KL(a,b))
    return KL(a,b),cond
cores=[(n,mask,[(-1 if mask>>x&1 else 1) for x in range(1<<n)]) for n in [1,2] for mask in range(1<<(1<<n))]
cores += [(3,m,[(-1 if m>>x&1 else 1) for x in range(8)]) for m in [1,7,105,150]]
def bent(n):return [(-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(n//2))%2 else 1) for x in range(1<<n)]
spectators=[('constant',[1]),('dictator',[1,-1]),('AND2',[-1,1,1,1]),('bent2',bent(2)),('defect3',[-1]+[1]*7),('bent4',bent(4))]
if pilot:cores=cores[20:21]
funcs=0;rows=0;partitions=0;nonzero_defects=0;witness=None
for n,mask,f in cores:
    Pf=law(f)
    for name,g in spectators:
        Pg=law(g); product=[f[x&(len(f)-1)]*g[x>>n] for x in range(len(f)*len(g))];P=law(product)
        ck(P==[Pf[x&(len(f)-1)]*Pg[x>>n] for x in range(len(P))]);funcs+=1
        for i in range(n):
            source=row(Pf,i)
            if source is None:continue
            e,a,b=source;ee,mu,rr=row(P,i);ck(e==ee);D=KL(a,b);ck(KL(mu,rr)==D)
            for t in mu:ck(mu[t]==a[t&(len(f)-1)]*Pg[t>>n] and rr[t]==b[t&(len(f)-1)]*Pg[t>>n])
            seed_degree,unused=coarse(a,b,lambda t:t.bit_count())
            for policy in range(3):
                C=(lambda t:t.bit_count()) if policy==0 else ((lambda t:((t&(len(f)-1)).bit_count(),(t>>n).bit_count())) if policy==1 else (lambda t:(t&(len(f)-1),(t>>n).bit_count())))
                Dc,W=coarse(mu,rr,C);partitions+=1
                if W:nonzero_defects+=1
                if policy==1:ck(Dc==seed_degree)
                if policy==2:ck(Dc==D and W=={})
                if policy==0 and n==3 and mask==1 and name=='bent4' and i==0:
                    witness={'core_mask':mask,'core_dimension':n,'spectator':name,'coordinate':i,'influence':str(e),'full_divergence_prime_log':{str(k):str(v) for k,v in D.items()},'degree_divergence_prime_log':{str(k):str(v) for k,v in Dc.items()},'discarded_conditional_prime_log':{str(k):str(v) for k,v in W.items()},'full_core_spectator_degree_discarded':'0'}
            rows+=1
def conv(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def occupancy(w,m):
    p=F(1,1<<w);beta=1-p;z=[F(1)];out=[F(0)]*(m*w+1)
    for L in range(m+1):
        weight=math.comb(m,L)*p**L*beta**(m-L)
        for t,v in enumerate(z):out[t]+=weight*v
        z=conv(z,[F(0)]+[F(math.comb(w,t),(1<<w)-1) for t in range(1,w+1)])
    ck(sum(out)==1);return out
w=4;m=1<<w;n=w*m;p=F(1,m);beta=1-p;nu=occupancy(w,m);other=occupancy(w,m-1)
W=[F(0)]*(n+1);W[0]=(1-2*beta**m)**2
for t in range(1,n+1):W[t]=4*beta**m*nu[t]
eps=2*p*beta**(m-1);I=2*w*beta**(m-1);ck(sum(W)==1 and I==n*eps)
mu=conv([F(math.comb(w-1,t),1<<(w-1)) for t in range(w)],other)
rr=[(1-F(t,n))*W[t]+F(t+1,n)*W[t+1] for t in range(n)]
ck(sum(mu)==sum(rr)==1);ck(mu[0]==eps);ck(sum(t*v for t,v in enumerate(mu))==F(2*w-1,2))
for t in range(n):
    ck(mu[t]==F(t+1)*W[t+1]/I);ck(rr[t]>=eps*mu[t])
    if t:ck(mu[t]<=(2*p/beta+2*beta*t)*nu[t])
    if 1<=t<=n//2:ck(mu[t]<=4*(t+1)*rr[t])
ck(sum(mu[t] for t in range(n//2+1,n))<=F(2,m));ck(W[0]>=F(1,16));ck(mu[0]<=rr[0]);ck(beta**m>=F(1,4));ck(beta**m<=F(3,8));ck(beta**(m-1)<=F(1,2))
out={'status':'PASS','pilot':pilot,'assertions':checks,'tensor_functions':funcs,'relevant_core_rows':rows,'partition_cases':partitions,'nonzero_conditional_defects':nonzero_defects,'tribes_width':w,'tribes_dimension':n,'tribes_degree_packets':n,'runtime_seconds':time.perf_counter()-start,'named_nonproduct_row_witness':witness,'arithmetic':'Exact rational identities and inequalities; analytic proof, not finite extrapolation, establishes all widths and divergent ratios.'}
save('PILOT.json' if pilot else 'EXACT_CONTRACT_AUDIT.json',out);print(json.dumps(out,indent=2))
