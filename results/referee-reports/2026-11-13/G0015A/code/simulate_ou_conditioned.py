"""Exact conditioned Binomial(2,1/2) GW shapes with continuous OU types.

No discretisation, rejection, MCMC, or tail truncation in the shape sampler.
PDFs and source images are never written. One worker, one numerical thread.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse, ctypes, csv, itertools, json, math, pathlib, resource, time
import numpy as np
from scipy.optimize import brentq
ROOT=pathlib.Path(__file__).resolve().parents[1]
SIGMA=math.sqrt(0.5)


def audit_priority():
    libc=ctypes.CDLL(None,use_errno=True)
    ctypes.set_errno(0); priority=libc.getpriority(0,0)
    if ctypes.get_errno(): raise OSError(ctypes.get_errno(),'getpriority')
    if priority<10:
        if libc.setpriority(0,0,10): raise OSError(ctypes.get_errno(),'setpriority')
        priority=libc.getpriority(0,0)
    assert priority>=10
    return priority


def governor_check():
    p=pathlib.Path.home()/'.claude/compute/compute_state.json'
    if p.exists():
        state=json.loads(p.read_text())
        if state.get('status')=='distress': raise RuntimeError('Governor distress: compute stopped')
        return {k:state.get(k) for k in ('ts','status','mode','mem_free_pct')}
    return {'status':'unavailable'}


def conditioned_degrees(n,rng,model='binomial'):
    # Given sum_i Xi=n-1, independent Bin(2,.5) variables are a
    # uniform (n-1)-subset of the 2n Bernoulli slots, grouped by parent.
    if model=='binomial':
        chosen=rng.choice(2*n,n-1,replace=False)
        d=np.bincount(chosen//2,minlength=n).astype(np.int16)
    else:
        # Independent Pois(1) conditioned on their sum are multinomial.
        chosen=rng.integers(n,size=n-1)
        d=np.bincount(chosen,minlength=n).astype(np.int16)
    cut=(int(np.argmin(np.cumsum(d.astype(np.int64)-1)))+1)%n
    d=np.roll(d,-cut)
    s=np.cumsum(d.astype(np.int64)-1)
    assert len(d)==n and s[-1]==-1 and (n==1 or np.all(s[:-1]>=0))
    return d


def geometry_and_marks(d,rng,r=0.6):
    n=len(d); depth=np.zeros(n,dtype=np.int32); parent=np.full(n,-1,dtype=np.int32)
    stack=np.empty(n,dtype=np.int32); remaining=np.empty(n,dtype=np.int16)
    top=0; stack[0]=0;remaining[0]=d[0]
    noise=rng.standard_normal(n); a=np.empty(n);a[0]=noise[0]
    sd=math.sqrt(1-r*r)
    for v in range(1,n):
        while remaining[top]==0: top-=1
        assert top>=0
        par=int(stack[top]);parent[v]=par;depth[v]=depth[par]+1
        remaining[top]-=1;a[v]=r*a[par]+sd*noise[v]
        if d[v]:
            top+=1;stack[top]=v;remaining[top]=d[v]
    profile=np.bincount(depth)
    assert profile.sum()==n
    # Independent breadth-first reconstruction of generation sizes validates
    # the depth/stack implementation without using its parent array.
    by_parent=np.bincount(depth,weights=d,minlength=len(profile)+1)
    assert np.array_equal(by_parent[:len(profile)-1].astype(np.int64),profile[1:])
    assert by_parent[len(profile)-1]==0
    cov=float(np.mean(a[parent[1:]]*a[1:])) if n>1 else 0.0
    return depth,parent,profile,a,cov


def excursion_max_cdf(x):
    x=np.asarray(x,dtype=float); out=np.zeros_like(x)
    for i,y in enumerate(x.ravel()):
        if y<=0: f=0.0
        elif y<1:
            k=np.arange(1,31,dtype=float)
            f=math.sqrt(2*math.pi)*math.pi**2/y**3*float(np.sum(k*k*np.exp(-math.pi**2*k*k/(2*y*y))))
        else:
            k=np.arange(1,31,dtype=float)
            f=1-2*float(np.sum((4*k*k*y*y-1)*np.exp(-2*k*k*y*y)))
        out.ravel()[i]=np.clip(f,0,1)
    return out


def ks_distance(x):
    x=np.sort(x);f=excursion_max_cdf(x);m=len(x)
    return float(max(np.max(np.arange(1,m+1)/m-f),np.max(f-np.arange(m)/m)))


def self_checks():
    # Exhaust all degree bridges at n<=5 and check cycle-lemma multiplicities.
    audit=[]
    for n in range(1,6):
        grouped={};target={}
        for slots in itertools.combinations(range(2*n),n-1):
            d=np.bincount(np.array(slots,dtype=int)//2,minlength=n)
            cut=(int(np.argmin(np.cumsum(d-1)))+1)%n
            rotated=tuple(np.roll(d,-cut));grouped[rotated]=grouped.get(rotated,0)+1
        for tree,count in grouped.items():
            w=math.prod(math.comb(2,int(k)) for k in tree)
            assert count==n*w,(n,tree,count,w)
            target[tree]=w
        audit.append({'n':n,'trees':len(grouped),'subsets':sum(grouped.values()),'cycle_identity':True})
    for n in range(1,6):
        grouped={}
        for balls in itertools.product(range(n),repeat=n-1):
            d=np.bincount(balls,minlength=n)
            cut=(int(np.argmin(np.cumsum(d-1)))+1)%n
            rotated=tuple(np.roll(d,-cut));grouped[rotated]=grouped.get(rotated,0)+1
        for tree,count in grouped.items():
            assert count*math.prod(math.factorial(int(k)) for k in tree)==n*math.factorial(n-1)
        audit.append({'model':'poisson','n':n,'trees':len(grouped),'allocations':sum(grouped.values()),'cycle_identity':True})
    # CDF checked in both theta-series forms on an overlap.
    for x in (0.8,1.,1.2):
        k=np.arange(1,100,dtype=float)
        f1=1-2*np.sum((4*k*k*x*x-1)*np.exp(-2*k*k*x*x))
        f2=math.sqrt(2*math.pi)*math.pi**2/x**3*np.sum(k*k*np.exp(-math.pi**2*k*k/(2*x*x)))
        assert abs(f1-f2)<2e-13
    return audit


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--model',choices=['binomial','poisson'],default='binomial')
    args=parser.parse_args();model=args.model
    sigma=SIGMA if model=='binomial' else 1.
    prefix='ou' if model=='binomial' else 'ou_poisson'
    start=time.monotonic();priority=audit_priority();gov=governor_check()
    seed=151520261113+(model=='poisson');rng=np.random.default_rng(seed);checks=self_checks()
    mean=math.sqrt(math.pi/2); variance=math.pi**2/6-math.pi/2
    quantiles={str(p):brentq(lambda x:float(excursion_max_cdf(x))-p,.2,4) for p in (.1,.5,.9)}
    settings=[(1000,400),(3000,400),(10000,300),(30000,200),(100000,150 if model=='binomial' else 300)]
    rows=[];summaries=[]
    with (ROOT/f'data/{prefix}_conditioned_raw.csv').open('w',newline='') as f:
        writer=None
        for n,reps in settings:
            governor_check();hn=[];wn=[]
            for rep in range(reps):
                if rep%25==0: governor_check()
                d=conditioned_degrees(n,rng,model)
                depth,parent,profile,a,cov=geometry_and_marks(d,rng)
                h=int(depth.max());w=int(profile.max())
                row={'n':n,'rep':rep,'height':h,'width':w,'height_scaled':sigma*h/(2*math.sqrt(n)),
                     'width_scaled':w/(sigma*math.sqrt(n)),'type_mean':float(a.mean()),
                     'type_second_moment':float(np.mean(a*a)),'edge_type_product':cov}
                if writer is None: writer=csv.DictWriter(f,fieldnames=row);writer.writeheader()
                writer.writerow(row);hn.append(row['height_scaled']);wn.append(row['width_scaled'])
                if n==100000 and rep==0:
                    with (ROOT/f'data/{prefix}_example_profile.csv').open('w',newline='') as pf:
                        pw=csv.writer(pf);pw.writerow(['depth','vertices']);pw.writerows(enumerate(profile))
                    with (ROOT/f'data/{prefix}_example_vertices.csv').open('w',newline='') as vf:
                        vw=csv.writer(vf);vw.writerow(['vertex','parent','depth','offspring','type'])
                        vw.writerows(zip(range(n),parent,depth,d,a))
            item={'n':n,'replicates':reps}
            for name,vals in [('height',hn),('width',wn)]:
                vals=np.asarray(vals)
                item[name]={'mean':float(vals.mean()),'sd':float(vals.std(ddof=1)),
                            'se':float(vals.std(ddof=1)/math.sqrt(reps)),
                            'quantiles':{str(p):float(np.quantile(vals,p)) for p in (.1,.5,.9)},
                            'ks_to_crt_max':ks_distance(vals),'mean_minus_limit':float(vals.mean()-mean)}
            summaries.append(item);f.flush()
            print(json.dumps(item),flush=True)
    result={'model':('D=2' if model=='binomial' else 'D=Poisson(2), including root')+'; p(y)=1/2; Gamma(a,dy)=N(0.6a,0.64); root N(0,1)',
            'interpretation':'Chosen parameter specialization of source Definition 4.1; genealogical branching model, not a finite-graph SDE simulation',
            'seed':seed,'sigma_squared':sigma**2,'Sigma_c':sigma/2,'settings':settings,'nice':priority,
            'threads':1,'governor_at_start':gov,'elapsed_seconds':time.monotonic()-start,
            'max_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'sampler_checks':checks,'reference':{'mean_max_e':mean,'variance_max_e':variance,'quantiles_max_e':quantiles},
            'summaries':summaries}
    (ROOT/f'data/{prefix}_conditioned_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['elapsed_seconds'],'seconds; peak RSS',result['max_rss_bytes_macos'],flush=True)

if __name__=='__main__': main()
