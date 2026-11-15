"""Finite, equal-cell deferred acceptance in both directions.

A grid cell is a single site with mass h and each centre has integer quota
alpha/h. These are finite discrete problems, not exact continuum solvers.
Both algorithms terminate; an exhaustive blocking-pair check follows each.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import collections, csv, heapq, json, math, pathlib, resource, time
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[1]

def sites_propose(dist, quota):
    ns,nc=dist.shape
    prefs=np.argsort(dist,axis=1,kind='stable')
    nxt=np.zeros(ns,dtype=np.int32)
    match=np.full(ns,-1,dtype=np.int32)
    held=[[] for _ in range(nc)]
    queue=collections.deque(range(ns)); proposals=0
    while queue:
        s=queue.popleft()
        while nxt[s]<nc:
            c=int(prefs[s,nxt[s]]); nxt[s]+=1; proposals+=1
            key=(-float(dist[s,c]),-s)
            if len(held[c])<quota:
                heapq.heappush(held[c],key); match[s]=c; break
            if key>held[c][0]:
                _,minus_old=heapq.heapreplace(held[c],key)
                old=-minus_old; match[old]=-1; queue.append(old)
                match[s]=c; break
    return match,proposals

def centres_propose(dist, quota):
    ns,nc=dist.shape
    prefs=np.argsort(dist,axis=0,kind='stable')
    nxt=np.zeros(nc,dtype=np.int32)
    counts=np.zeros(nc,dtype=np.int32)
    match=np.full(ns,-1,dtype=np.int32)
    queue=collections.deque(range(nc)); proposals=0
    while queue:
        c=queue.popleft()
        while counts[c]<quota and nxt[c]<ns:
            s=int(prefs[nxt[c],c]); nxt[c]+=1; proposals+=1
            old=int(match[s])
            if old<0 or (dist[s,c],c)<(dist[s,old],old):
                match[s]=c; counts[c]+=1
                if old>=0:
                    counts[old]-=1
                    if nxt[old]<ns: queue.append(old)
    return match,proposals

def verify(dist,match,quota):
    ns,nc=dist.shape
    counts=np.bincount(match[match>=0],minlength=nc)
    assert np.all(counts<=quota)
    worst=np.full(nc,-np.inf)
    rows=np.flatnonzero(match>=0)
    np.maximum.at(worst,match[rows],dist[rows,match[rows]])
    worst[counts<quota]=np.inf
    assigned=np.full(ns,np.inf); assigned[rows]=dist[rows,match[rows]]
    blockers=0
    for start in range(0,ns,128):
        d=dist[start:start+128]
        blockers+=int(np.count_nonzero((d<assigned[start:start+128,None])&(d<worst[None,:])))
    assert blockers==0,blockers
    return {'blocking_pairs':blockers,'sated':int(np.count_nonzero(counts==quota)),
            'unclaimed':int(np.count_nonzero(match<0))}

def candidate(n):
    # Nested prefixes. N(r)=Theta(r^3), yet locally finite. A common
    # irrational translation removes receiver distance ties on rational grids.
    out=[]
    shift=math.sqrt(2)/1000
    for k in range(1,n+1):
        for sign in (-1,1):
            out.extend(sign*(k+np.arange(k*k)/(10*k*k))+shift)
    return np.array(out)

def self_check():
    rng=np.random.default_rng(83)
    # Arbitrary strict shared costs as well as geometric distances;
    # asymmetric supply and quotas, including unused capacity.
    cases=0
    for ns,nc,q in [(7,3,1),(7,3,2),(7,3,4),(3,7,2),(20,6,3)]:
        for _ in range(8):
            d=rng.uniform(size=(ns,nc))
            a,_=sites_propose(d,q); b,_=centres_propose(d,q)
            verify(d,a,q); verify(d,b,q)
            assert np.array_equal(a,b)
            cases+=1
    return cases

def run():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    # On this Mac ru_maxrss is bytes. No worker pools or subprocesses.
    rows=[]; tests=self_check()
    for res in (32,64,128):
        previous=None
        for n in (4,8,12,16):
            start=time.monotonic(); h=1/res; L=n+2
            x=np.arange(-L*res,L*res,dtype=float)/res+h/2
            c=candidate(n)
            d=np.abs(x[:,None]-c[None,:])
            # Confirm strict preferences at every receiver.
            ds=np.sort(d,axis=1); dc=np.sort(d,axis=0)
            min_gap=min(float(np.min(np.diff(ds,axis=1))),float(np.min(np.diff(dc,axis=0))))
            assert min_gap>1e-13,min_gap
            del ds,dc
            a,pa=sites_propose(d,res); b,pb=centres_propose(d,res)
            va=verify(d,a,res); vb=verify(d,b,res)
            core=np.abs(x)<=2
            core_assign=a[core]
            changes=None if previous is None else int(np.count_nonzero(core_assign!=previous))
            previous=core_assign.copy()
            row=dict(n=n,h=h,window=L,centres=len(c),sites=len(x),quota=res,
                algorithm_difference_cells=int(np.count_nonzero(a!=b)),
                algorithm_difference_measure=h*int(np.count_nonzero(a!=b)),
                core_difference_cells=int(np.count_nonzero(a[core]!=b[core])),
                core_change_from_previous_window=changes,
                unclaimed_cells=va['unclaimed'],sated_centres=va['sated'],
                site_proposals=pa,centre_proposals=pb,min_preference_gap=min_gap,
                site_blockers=va['blocking_pairs'],centre_blockers=vb['blocking_pairs'],
                seconds=time.monotonic()-start,
                max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            rows.append(row)
            # Plain text numerical data, both terminal allocations retained.
            np.savetxt(ROOT/'data'/f'grid_n{n}_r{res}.csv',
                       np.column_stack((x,a,b)),delimiter=',',
                       header='site,site_proposing_centre_index,centre_proposing_centre_index',
                       comments='',fmt=['%.10f','%d','%d'])
            np.savetxt(ROOT/'data'/f'centres_n{n}.csv',c,delimiter=',',header='centre',comments='',fmt='%.15f')
            (ROOT/'data'/'grid_results.json').write_text(json.dumps({'self_checks':tests,'results':rows},indent=2))
            print(json.dumps(row),flush=True)
            del d
    with (ROOT/'data'/'grid_results.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
if __name__=='__main__': run()
