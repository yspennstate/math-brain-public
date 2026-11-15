"""Q2 searches; no subprocesses/network, one numerical-library thread.
All exact claims use fractions. Each invocation stops after 230 seconds.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys, json, time, random, resource
from fractions import Fraction as Q
from itertools import combinations
import numpy as np
from q1_core import exact, solve, lump, numeric, serialize
START=time.monotonic()
LIMIT=230

def log(s):
    with open('LOG.md','a') as f: f.write('\n'+time.strftime('%Y-%m-%d %H:%M:%S')+' '+s+'\n')
    print(s,flush=True)

def partitions(n,q):
    def go(bs,k):
        if k==n:
            if len(bs)==q: yield tuple(tuple(b) for b in bs)
            return
        if len(bs)>q or len(bs)+n-k<q:return
        for a in range(len(bs)):
            bs[a].append(k);yield from go(bs,k+1);bs[a].pop()
        if len(bs)<q:
            bs.append([k]);yield from go(bs,k+1);bs.pop()
    yield from go([],0)

def correction(F,bs):
    """Fhat=F-F C (C^t F C)^-1 C^t F, evaluated on reps."""
    n=len(F);reps=[b[0] for b in bs]
    diffs=[(a,b[0]) for b in bs for a in b[1:]]
    if not diffs:return [[F[i][j] for j in reps] for i in reps]
    V=[[F[i][a]-F[i][b] for a,b in diffs] for i in range(n)]
    S=[[V[a][k]-V[b][k] for k in range(len(diffs))] for a,b in diffs]
    invV={j:solve(S,V[j]) for j in reps}
    return [[F[i][j]-sum(a*b for a,b in zip(V[i],invV[j])) for j in reps] for i in reps]

def fork(N,t):
    t=Q(t);R=t**3;alpha=t;n=2*N+4
    # a,b,c,z0..zN,y0..y(N-1)
    w=[[Q(0)]*n for _ in range(n)]
    def edge(i,j,v):
        w[i][j]+=v
        if i!=j:w[j][i]+=v
    edge(0,3,1);edge(0,0,t-1)
    for k in range(N):
        edge(3+k,4+k,R**(k+1));edge(4+N+k,4+k,alpha*R**(k+1))
        edge(4+N+k,4+N+k,(t-1)*alpha*R**(k+1))
    edge(1,3+N,alpha*R**(N+1));edge(1,1,(t-1)*alpha*R**(N+1))
    edge(2,3+N,R**(N+2));edge(2,2,(N+2)*R**(N+4))
    return w

def split_leaf(w,host,eps=Q(1,1000000)):
    v=[row[:] + [Q(0)] for row in w]+[[Q(0)]*(len(w)+1)]
    v[host][-1]=v[-1][host]=eps
    return v

def structures(n):
    for t in (10,100,1000,1000000):
        for N in range(3):
            if 2*N+4>n:continue
            w=fork(N,t)
            while len(w)<n:w=split_leaf(w,2)
            yield 'fork_N%d_t%d'%(N,t),w
        for typ in ('path','star','k5_extra'):
            w=[[Q(0)]*n for _ in range(n)]
            def edge(i,j,a):
                w[i][j]=w[j][i]=Q(a)
            if typ=='path':
                for i in range(n-1):edge(i,i+1,t**(2*i))
                w[0][0]=t;w[-1][-1]=t**(2*n)
            elif typ=='star':
                for i in range(n-1):edge(i,n-1,t**i);w[i][i]=(t-1)*t**i
                w[-1][-1]=t**(n+3)
            else:
                edge(0,2,1);edge(1,2,1);edge(2,3,t*t)
                w[0][0]=w[1][1]=t-1;w[3][3]=t**6
                for i in range(4,n):edge(i,2,t**(i-3));w[i][i]=(t-1)*t**(i-3)
            yield typ+'_t'+str(t),w

def loadbest():
    try:
        with open('q2_best.json') as f:return json.load(f)
    except FileNotFoundError:return {}

def record(best,n,r,w,bs,orig,hat,source):
    ratio=hat/orig;key=f'{n},{r}'
    if key not in best or ratio>Q(best[key]['ratio']):
        best[key]=serialize(dict(n=n,r=r,w=w,partition=bs,T=orig,That=hat,ratio=ratio,source=source))
        with open('q2_best.json','w') as f:json.dump(best,f,indent=2)
        print('BEST',key,float(ratio),source,flush=True)
        if ratio>r+1:
            log('EXACT COUNTEREXAMPLE '+key+' ratio='+str(ratio));raise RuntimeError('COUNTEREXAMPLE')

def exact_scan(w,rs,best,source,audit=False):
    n=len(w);x=exact(w);count=0
    for r in rs:
        if n-r<1:continue
        for bs in partitions(n,n-r):
            Fh=correction(x['F'],bs);Th=max(map(max,Fh));count+=1
            if audit:
                z=exact(lump(w,bs));assert Fh==z['F']
            record(best,n,r,w,bs,x['t'],Th,source)
    return count

def random_w(n,rng):
    w=[[Q(0)]*n for _ in range(n)]
    # Connected random tree with extra edges and independently varied loops.
    for i in range(1,n):
        j=rng.randrange(i);w[i][j]=w[j][i]=Q(10)**rng.randint(-3,3)*rng.randint(1,7)
    for i in range(n):
        w[i][i]=Q(10)**rng.randint(-3,5)*rng.randrange(5)
        for j in range(i):
            if not w[i][j] and rng.random()<.35:w[i][j]=w[j][i]=Q(10)**rng.randint(-3,3)*rng.randint(1,7)
    return w

def run_exact(mode,n,seed=20261112):
    best=loadbest();cnt=net=0;rng=random.Random(seed+n)
    seq=structures(n) if mode=='structured' else ((f'random_seed{seed}_trial{k}',random_w(n,rng)) for k in range(100000))
    for name,w in seq:
        if time.monotonic()-START>LIMIT:break
        cnt+=exact_scan(w,(2,3),best,name,audit=(mode=='random' and net==0));net+=1
        if mode=='random' and net>=20:break
    s=f'Exact {mode} n={n}: {net} networks, {cnt} partitions; elapsed {time.monotonic()-START:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.'
    log(s)
    with open('q2_counts.jsonl','a') as f:f.write(json.dumps(dict(mode=mode,n=n,networks=net,partitions=cnt,seconds=time.monotonic()-START))+'\n')

class Deadline(Exception):pass

def run_opt(n,r,seed):
    from scipy.optimize import differential_evolution, minimize
    rng=np.random.default_rng(seed);best=loadbest();neval=0;verified=0
    # Every shape of non-singleton blocks with deficit r.
    shapes={2:[(3,),(2,2)],3:[(4,),(3,2),(2,2,2)]}[r]
    for sizes in shapes:
        if sum(sizes)>n:continue
        bs=[];k=0
        for sz in sizes:bs.append(list(range(k,k+sz)));k+=sz
        bs += [[i] for i in range(k,n)]
        if len(bs)==1:continue
        for topology in ('full','tree','path'):
            if time.monotonic()-START>LIMIT:break
            edges=list(combinations(range(n),2)) if topology=='full' else ([(i,int(rng.integers(i))) for i in range(1,n)] if topology=='tree' else [(i,i+1) for i in range(n-1)])
            edges += [(i,i) for i in range(n)]
            def weights(v):
                w=np.zeros((n,n))
                for (i,j),x in zip(edges,v):w[i,j]=w[j,i]=10.**x
                return w
            top=[0,None]
            def obj(v):
                nonlocal neval
                if time.monotonic()-START>LIMIT:raise Deadline
                neval+=1
                try:
                    w=weights(v);a=numeric(w);b=numeric(np.array(lump(w,bs)));rat=b/a
                    if not np.isfinite(rat) or rat<0 or rat>20:return 0
                    if rat>top[0]:top[:]=[rat,v.copy()]
                    return -rat
                except np.linalg.LinAlgError:return 0
            try:
                res=differential_evolution(obj,[(-5,5)]*len(edges),popsize=5,maxiter=65,polish=False,seed=int(rng.integers(2**31)))
                res=minimize(obj,res.x,method='Nelder-Mead',options={'maxiter':1500,'xatol':.002})
            except Deadline:pass
            if top[1] is not None:
                # Nine significant digits of each positive weight, then exact all-partition scan.
                w=[[Q(format(float(x),'.9g')) for x in row] for row in weights(np.clip(top[1],-12,12))]
                exact_scan(w,(r,),best,f'optim_seed{seed}_shape{sizes}_{topology}');verified+=1
                print('OPT',n,r,sizes,topology,top[0],flush=True)
        if time.monotonic()-START>LIMIT:break
    log(f'Optimized n={n}, r={r}, seed={seed}: {neval} numerical evaluations; {verified} rounded candidates scanned over every r-merge partition exactly; elapsed {time.monotonic()-START:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
    with open('q2_counts.jsonl','a') as f:f.write(json.dumps(dict(mode='opt',n=n,r=r,seed=seed,evaluations=neval,candidates=verified,seconds=time.monotonic()-START))+'\n')

if __name__=='__main__':
    mode=sys.argv[1];n=int(sys.argv[2])
    if mode in ('random','structured'):run_exact(mode,n,int(sys.argv[3]) if len(sys.argv)>3 else 20261112)
    elif mode=='opt':run_opt(n,int(sys.argv[3]),int(sys.argv[4]) if len(sys.argv)>4 else 20261112)
