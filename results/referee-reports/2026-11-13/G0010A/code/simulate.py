#!/usr/bin/env python3
"""Exact independent bond-percolation samples on implicit/sparse simple hosts.
One process, one numerical thread, inherited nice >=10, 3 GiB memory guard.
Run from the G0010 directory: python3 code/simulate.py --reps 40
"""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[name]='1'
import argparse, csv, hashlib, json, math, resource, time, threading
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh

ROOT=Path(__file__).resolve().parents[1]
CAP=3*1024**3
try:
    resource.setrlimit(resource.RLIMIT_AS,(CAP,CAP))
    LIMIT_METHOD='RLIMIT_AS'
except (ValueError, OSError) as exc:
    # This managed macOS shell rejects setrlimit. Bound arrays and stop at 3 GiB RSS.
    LIMIT_METHOD='3 GiB peak-RSS watchdog; setrlimit unavailable: '+str(exc)
    def memory_watch():
        while True:
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >= CAP:
                os.write(2,b'RSS guard reached 3 GiB; stopping\n')
                os._exit(70)
            time.sleep(.05)
    threading.Thread(target=memory_watch,daemon=True).start()
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)


def governor():
    p=Path('~/.claude/compute/compute_state.json')
    if not p.exists(): return {'status':'unavailable'}
    s=json.loads(p.read_text())
    if s.get('status')=='distress':
        raise RuntimeError('Compute governor distress: stopping at checkpoint')
    return {k:s.get(k) for k in ('status','mode','t_epoch')}


def bernoulli_indices(total,p,rng):
    """Geometric waiting times: exactly the open indices among total Bern(p) trials."""
    if total==0 or p<=0: return np.empty(0,dtype=np.int64)
    if p>=1: return np.arange(total,dtype=np.int64)
    parts=[]; last=-1
    while True:
        expected=max(0,(total-last-1)*p)
        batch=max(64,min(262144,int(expected+10*math.sqrt(expected+1)+64)))
        a=last+np.cumsum(rng.geometric(p,size=batch),dtype=np.int64)
        keep=a[a<total]
        if len(keep): parts.append(keep)
        if len(keep)<batch: break
        last=int(a[-1])
    return np.concatenate(parts) if parts else np.empty(0,dtype=np.int64)


def upper_pairs(n,index):
    """Decode lexicographic upper-triangle indices, with integer boundary correction."""
    a=2*n-1
    u=np.floor((a-np.sqrt(float(a*a)-8*index))/2).astype(np.int64)
    base=u*(2*n-u-1)//2
    mask=base>index; u[mask]-=1
    nextbase=(u+1)*(2*n-u-2)//2
    mask=index>=nextbase; u[mask]+=1
    base=u*(2*n-u-1)//2
    v=u+1+index-base
    return u,v


def largest(n,u,v):
    if not len(u): return 1
    # csgraph treats directed=False as undirected; one stored orientation suffices.
    a=csr_matrix((np.ones(len(u),dtype=np.int8),(u,v)),shape=(n,n))
    _,labels=connected_components(a,directed=False)
    return int(np.bincount(labels).max())


def tree_core_edges(k,b,h):
    nt=(b**(h+1)-1)//(b-1); nc=k+1
    cu,cv=np.triu_indices(nc,1)
    child=np.arange(1,nt,dtype=np.int64)
    parent=(child-1)//b
    u=np.concatenate([cu,parent+nc,np.array([0],dtype=np.int64)])
    v=np.concatenate([cv,child+nc,np.array([nc],dtype=np.int64)])
    return nc+nt,u,v


def tree_core_radius(k,b,h):
    # Orthonormal class indicators: connector, other clique vertices, tree levels.
    q=np.zeros((h+3,h+3))
    q[1,1]=k-1; q[0,1]=q[1,0]=math.sqrt(k)
    q[0,2]=q[2,0]=1
    for i in range(2,h+2): q[i,i+1]=q[i+1,i]=math.sqrt(b)
    return float(np.linalg.eigvalsh(q)[-1])


def star_clique_radius(m,t):
    q=np.array([[0,math.sqrt(m-1),math.sqrt(t)],
                [math.sqrt(m-1),m-2,0],[math.sqrt(t),0,0]])
    return float(np.linalg.eigvalsh(q)[-1])


@dataclass
class Host:
    family:str
    n:int
    delta:int
    lam:float
    potential_edges:int
    params:dict
    kind:str
    u:object=None
    v:object=None
    radius_residual:float=0.0
    host_hash:str='analytic'

    def sample(self,p,rng):
        if self.kind=='bipartite':
            s,t=self.params['s'],self.params['t']
            idx=bernoulli_indices(s*t,p,rng)
            return idx//t,idx%t+s
        if self.kind=='star_clique':
            m,t=self.params['m'],self.params['t']
            idx=bernoulli_indices(m*(m-1)//2,p,rng)
            u,v=upper_pairs(m,idx)
            leaves=bernoulli_indices(t,p,rng)+m
            return np.concatenate([u,np.zeros(len(leaves),dtype=np.int64)]),np.concatenate([v,leaves])
        if self.kind=='blowup':
            m=self.params['multiplicity']; idx=bernoulli_indices(self.potential_edges,p,rng)
            edge=idx//(m*m); offset=idx%(m*m)
            return self.u[edge]*m+offset//m,self.v[edge]*m+offset%m
        idx=bernoulli_indices(self.potential_edges,p,rng)
        return self.u[idx],self.v[idx]


def planted_host(n,seed):
    rng=np.random.default_rng(seed)
    u,v=upper_pairs(n,bernoulli_indices(n*(n-1)//2,6/(n-1),rng))
    uu=[u];vv=[v]
    degrees=[]
    for hub in range(4):
        d=min(n-4,max(1,round(n**.6/(2**hub))))
        neighbors=rng.choice(n-4,size=d,replace=False)+4
        uu.append(np.full(d,hub,dtype=np.int64));vv.append(neighbors);degrees.append(d)
    u=np.concatenate(uu);v=np.concatenate(vv)
    keys=np.unique(np.minimum(u,v)*n+np.maximum(u,v))
    h=hashlib.sha256(keys.tobytes()).hexdigest()
    u=keys//n;v=keys%n
    deg=np.bincount(np.concatenate([u,v]),minlength=n)
    a=csr_matrix((np.ones(2*len(u)),(np.concatenate([u,v]),np.concatenate([v,u]))),shape=(n,n))
    val,vec=eigsh(a,k=1,which='LA',v0=np.full(n,1/math.sqrt(n)),tol=1e-10,ncv=12)
    lam=float(val[0]);res=float(np.linalg.norm(a@vec[:,0]-lam*vec[:,0]))
    return Host('planted_hubs',n,int(deg.max()),lam,len(u),
                {'host_seed':seed,'base_expected_degree':6,'planted_degrees':degrees},
                'sparse',u,v,res,h)


def hosts():
    for n in (1000,10000,100000,1000000):
        yield Host('balanced_bipartite',n,n//2,n/2,n*n//4,
                   {'s':n//2,'t':n//2},'bipartite')
    for s in (8,16,32,64,100):
        t=s**3
        yield Host('bipartite_s_s3',s+t,t,float(s*s),s*t,{'s':s,'t':t},'bipartite')
    for n in (1000,10000,100000,1000000):
        t=n-1
        yield Host('star',n,t,math.sqrt(t),t,{'s':1,'t':t},'bipartite')
    for n in (1000,10000,100000,1000000):
        m=round(math.sqrt(n));t=n-m
        yield Host('star_plus_clique',n,n-1,star_clique_radius(m,t),m*(m-1)//2+t,
                   {'m':m,'t':t,'core':'complete graph (dense expander)'},'star_clique')
    for n in (1000,10000,100000,1000000):
        governor()
        yield planted_host(n,2026111300+n)
    k,b=12,16
    for h in (1,2,3,4,5):
        n,u,v=tree_core_edges(k,b,h)
        yield Host('near_regular_tree',n,b+1,tree_core_radius(k,b,h),len(u),
                   {'k':k,'b':b,'h':h,'multiplicity':1},'sparse',u,v)
    for h in (1,2,3,4):
        nb,u,v=tree_core_edges(k,b,h);m=2**h
        yield Host('near_regular_tree_blowup',nb*m,m*(b+1),m*tree_core_radius(k,b,h),len(u)*m*m,
                   {'k':k,'b':b,'h':h,'multiplicity':m},'blowup',u,v)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--reps',type=int,default=40)
    args=parser.parse_args()
    out=ROOT/'data';out.mkdir(exist_ok=True)
    meta={'numpy':np.__version__,'scipy':scipy.__version__,'seed':20261113,
          'priority':os.getpriority(os.PRIO_PROCESS,0),'memory_guard_bytes':CAP,
          'memory_guard_method':LIMIT_METHOD,'worker_processes':1,
          'numerical_threads':1,'rss_watchdog_threads':int(LIMIT_METHOD!='RLIMIT_AS'),
          'governor_start':governor(),
          'reps':args.reps,'method':'geometric skipping, exact Bernoulli edges; scipy connected_components'}
    (out/'simulation_metadata.json').write_text(json.dumps(meta,indent=2))
    fields=['family','n','delta','lambda','epsilon','p','trial','seed','open_edges','largest','elapsed_s']
    summaries=[];hostmeta=[];start=time.monotonic()
    with (out/'trials.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for hi,host in enumerate(hosts()):
            governor()
            epsilon=.1 if host.family.startswith('near_regular') else .2
            p=(1-epsilon)/host.lam
            reps=args.reps
            sizes=[];edges=[]
            hostmeta.append({k:getattr(host,k) for k in ['family','n','delta','lam','potential_edges','params','radius_residual','host_hash']})
            for trial in range(reps):
                seed=20261113+10000*hi+trial
                rng=np.random.default_rng(seed);t0=time.monotonic()
                u,v=host.sample(p,rng);l=largest(host.n,u,v)
                writer.writerow(dict(family=host.family,n=host.n,delta=host.delta,**{'lambda':host.lam},epsilon=epsilon,p=p,
                                     trial=trial,seed=seed,open_edges=len(u),largest=l,elapsed_s=time.monotonic()-t0))
                sizes.append(l);edges.append(len(u))
            f.flush()
            sd=float(np.std(sizes,ddof=1)); mean=float(np.mean(sizes))
            se=sd/math.sqrt(reps)
            e_mean=host.potential_edges*p
            e_se=math.sqrt(host.potential_edges*p*(1-p)/reps)
            row=dict(family=host.family,n=host.n,delta=host.delta,**{'lambda':host.lam},epsilon=epsilon,p=p,
                     delta_over_lambda=host.delta/host.lam,reps=reps,mean=mean,median=float(np.median(sizes)),
                     q10=float(np.quantile(sizes,.1)),q90=float(np.quantile(sizes,.9)),sd=sd,
                     mean_ci95_low=mean-1.96*se,mean_ci95_high=mean+1.96*se,
                     mean_open_edges=float(np.mean(edges)),expected_open_edges=e_mean,
                     edge_count_z=(float(np.mean(edges))-e_mean)/e_se if e_se else 0)
            summaries.append(row)
            with (out/'summary.csv').open('w',newline='') as g:
                w=csv.DictWriter(g,fieldnames=list(row));w.writeheader();w.writerows(summaries)
            (out/'hosts.json').write_text(json.dumps(hostmeta,indent=2))
            print(json.dumps({'family':host.family,'n':host.n,'median':row['median'],'q10':row['q10'],'q90':row['q90'],
                              'edge_z':round(row['edge_count_z'],2),'elapsed_s':round(time.monotonic()-start,2)}),flush=True)
            del u,v,host
    meta.update(elapsed_s=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                governor_end=governor(),host_cases=len(summaries),total_trials=sum(r['reps'] for r in summaries))
    (out/'simulation_metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta),flush=True)

if __name__=='__main__': main()
