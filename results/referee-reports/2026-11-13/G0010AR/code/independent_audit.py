"""Independent graph, spectral, proof-identity and percolation checks.

No code from claim_files is imported or copied. Bernoulli sampling uses a
binomial edge count followed by a uniform subset, not geometric waiting times.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import csv, json, math, resource, time
from pathlib import Path
import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
import sympy as sp


def base_graph(k,b,h):
    """Tree vertices in breadth-first order, then k+1 clique vertices."""
    nt=(b**(h+1)-1)//(b-1)
    child=np.arange(1,nt,dtype=np.int64)
    us=[(child-1)//b, np.array([0],dtype=np.int64)]
    vs=[child, np.array([nt],dtype=np.int64)]
    ci,cj=np.triu_indices(k+1,1)
    us.append(nt+ci); vs.append(nt+cj)
    return nt+k+1,np.concatenate(us),np.concatenate(vs)


def quotients(k,b,h):
    # Classes: clique bridge endpoint, other k clique vertices, tree levels.
    qi=np.zeros((h+3,h+3),dtype=np.int64)
    qi[0,1]=k; qi[1,0]=1; qi[1,1]=k-1
    qi[0,2]=qi[2,0]=1
    for level in range(h):
        qi[level+2,level+3]=b; qi[level+3,level+2]=1
    sizes=np.array([1,k]+[b**j for j in range(h+1)],dtype=float)
    qs=qi*np.sqrt(sizes[:,None]/sizes[None,:])
    assert np.max(np.abs(qs-qs.T))<1e-10
    return qi,qs


def radius(k,b,h):
    return float(np.linalg.eigvalsh(quotients(k,b,h)[1])[-1])


def component_max(n,us,vs):
    a=coo_matrix((np.ones(2*len(us),dtype=np.int8),
                  (np.concatenate([us,vs]),np.concatenate([vs,us]))),shape=(n,n)).tocsr()
    _,labels=connected_components(a,directed=False)
    return int(np.bincount(labels).max())


def slow_bfs(n,us,vs):
    adj=[[] for _ in range(n)]
    for u,v in zip(us,vs): adj[u].append(v); adj[v].append(u)
    seen=set(); best=0
    for root in range(n):
        if root in seen: continue
        queue=[root]; seen.add(root)
        for u in queue:
            for v in adj[u]:
                if v not in seen: seen.add(v); queue.append(v)
        best=max(best,len(queue))
    return best


def sample_open(rng,us,vs,m,p):
    # There are E*m^2 distinct edges, ordered by base edge then two endpoints.
    total=len(us)*m*m
    count=int(rng.binomial(total,p))
    ids=rng.choice(total,size=count,replace=False,shuffle=False)
    block,within=np.divmod(ids,m*m)
    left,right=np.divmod(within,m)
    return us[block]*m+left, vs[block]*m+right


def proof_checks():
    checks={}; spectra=[]
    x=sp.Symbol('x')
    for k,b,h,m in [(4,4,1,1),(4,4,2,2),(6,8,1,2),(8,12,1,1),(12,16,1,1)]:
        n,us,vs=base_graph(k,b,h)
        adj=np.zeros((n,n),dtype=np.int64)
        adj[us,vs]=1; adj[vs,us]=1
        full=np.kron(adj,np.ones((m,m),dtype=np.int64))
        actual=float(np.linalg.eigvalsh(full)[-1])
        qi,qs=quotients(k,b,h)
        poly=sp.Matrix(qi).charpoly(x).as_expr()
        roots=sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**24))
        interval=roots[-1][0]
        lo,hi=map(str,interval)
        algebraic=float(sp.N(interval[0]+interval[1],30)/2)
        expected=m*radius(k,b,h)
        delta=int(full.sum(axis=1).max())
        assert delta==m*(b+1)
        assert abs(actual-expected)<1e-10
        assert abs(actual/m-algebraic)<1e-10
        assert k<=actual/m<=k+1
        # Exact factorisation certificate for the full host, at most 26 vertices.
        factorisation=None
        if n<=26:
            factorisation=str(sp.factor(sp.Matrix(adj).charpoly(x).as_expr()))
            assert sp.rem(sp.Matrix(adj).charpoly(x).as_expr(),poly,x)==0
        spectra.append(dict(k=k,b=b,h=h,m=m,n=n*m,Delta=delta,lambda_numeric=actual,
             quotient_charpoly=str(poly),lambda_H_rational_interval=[lo,hi],full_charpoly_factorisation=factorisation,
             spectral_absolute_error=abs(actual-expected)))
    checks['small_exact_spectra']=spectra
    # Arbitrarily narrow positive gaps tested; a constructive witness suffices.
    parameters=[]
    for q,delta in [(.9,.5),(.98,.1),(.8,.2501),(.5,1.01),(.01,100.)]:
        r=(1/q+1+delta)/2
        k=1
        while True:
            b=math.floor(r*k)
            mu=-b*math.expm1(-q/(k+1))
            if k*k>=4*b and b>=k and b+1<(1+delta)*k and mu>1: break
            k*=2
        parameters.append(dict(q=q,delta=delta,k=k,b=b,mu=mu))
    checks['parameter_witnesses']=parameters
    # Re-derive the normalized second moment by the independent recurrence.
    b=16; q=.9; k=12; prob=-math.expm1(-q/(k+1)); mu=b*prob; var=b*prob*(1-prob)
    ez=ezz=1.; error=0.
    for depth in range(1,101):
        ezz=mu*mu*ezz+var*ez; ez*=mu
        formula=1+var/(mu*(mu-1))*(1-mu**(-depth))
        error=max(error,abs(ezz/ez**2-formula))
    assert error<1e-10
    checks['second_moment_max_error']=error
    # Audit (16) against long directly summed series in all R:a regimes.
    errs=[]
    for R,a,B in [(1,1.1,100),(1.05,1.1,100),(1.1,1.1,100),(1.5,1.1,100),(2,1.2,1),(1.5,1.1,1.5**5)]:
        direct=1+sum(math.exp(-j*math.log(a)+min(j*math.log(R),math.log(B))) for j in range(1,20001))
        if R==1: closed=a/(a-1)
        else:
            J=math.floor(math.log(B)/math.log(R))
            closed=1+sum((R/a)**j for j in range(1,J+1))+B*a**(-J)/(a-1)
        errs.append(abs(direct-closed)/closed)
    assert max(errs)<1e-12
    checks['resolvent_sum_max_relative_error']=max(errs)
    # Exact recursion of truncated total-progeny MGFs, including the root.
    rng=np.random.default_rng(7052); induction=[]
    for n in (3,8,19,31):
        adj=(rng.random((n,n))<.3).astype(float); adj=np.triu(adj,1); adj+=adj.T
        lam=float(np.linalg.eigvalsh(adj)[-1]); Delta=float(adj.sum(axis=1).max())
        p=min(.83/lam,1/Delta)
        u=np.linalg.solve(np.eye(n)-p*adj,np.ones(n)); U=float(u.max())
        a=1/(2*U**2); theta=1/(4*U**2)
        mgf=np.full(n,math.exp(theta))
        for _ in range(100):
            mgf=np.exp(theta+adj@np.log1p(p*(mgf-1)))
            assert np.max(np.log(mgf)-a*u)<1e-12
        B=math.sqrt(n*Delta)/lam; J=math.ceil(math.log(B)/math.log(1/.83))
        assert U<=1+J+1/(1-.83)
        induction.append(dict(n=n,U=U,max_log_mgf_minus_au=float(np.max(np.log(mgf)-a*u))))
    checks['mgf_recursion']=induction
    # Decoder and component checks on actual blow-ups using a separate BFS.
    for _ in range(150):
        n,us,vs=base_graph(4,4,1)
        ou,ov=sample_open(rng,us,vs,2,.15)
        assert len(set(zip(ou,ov)))==len(ou)
        assert component_max(n*2,ou,ov)==slow_bfs(n*2,ou,ov)
    checks['independent_bfs_agreements']=150
    Path('data/proof_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    print('Proof and spectral checks passed',flush=True)


def simulations():
    rng=np.random.default_rng(260819145)
    cases=[]
    for h in (2,3,4,5): cases.append(('A_plain',12,16,h,1,'fixed'))
    for h in (1,2,3,4): cases.append(('A_blowup',12,16,h,2**h,'fixed'))
    for h in (2,3,4,5): cases.append(('boundary',12,16,h,1,'boundary'))
    for h in (1,2,3,4): cases.append(('boundary_blowup',12,16,h,2**h,'boundary'))
    for h in (2,3): cases.append(('boundary_ratio_1.09',100,108,h,1,'boundary'))
    rows=[]; summaries=[]; reps=60
    for family,k,b,h,m,mode in cases:
        nb,us,vs=base_graph(k,b,h); n=nb*m
        lam=m*radius(k,b,h); Delta=m*(b+1)
        q=.9 if mode=='fixed' else lam/Delta
        p=q/lam; delta=Delta/lam-1
        E=len(us)*m*m
        results=[]; edges=[]
        for rep in range(reps):
            ou,ov=sample_open(rng,us,vs,m,p)
            L=component_max(n,ou,ov); results.append(L); edges.append(len(ou))
            rows.append(dict(family=family,k=k,b=b,h=h,m=m,n=n,Delta=Delta,lambda_host=lam,q=q,delta=delta,
                        p=p,q_times_1plusdelta=q*(1+delta),rep=rep,L1=L,open_edges=len(ou)))
        B=math.sqrt(n*Delta)/lam
        rec=dict(family=family,k=k,b=b,h=h,m=m,n=n,Delta=Delta,lambda_host=lam,q=q,
            delta=delta,p=p,q_times_1plusdelta=q*(1+delta),median=float(np.median(results)),
            p10=float(np.quantile(results,.1)),p90=float(np.quantile(results,.9)),maximum=max(results),
            median_over_logn=float(np.median(results)/math.log(n)),
            median_over_log3n=float(np.median(results)/math.log(n)**3),
            source_B_logn=B*math.log(n),mean_open_edges=float(np.mean(edges)),
            edge_mean_z=(np.mean(edges)-E*p)/math.sqrt(E*p*(1-p)/reps))
        summaries.append(rec); print(json.dumps(rec),flush=True)
    with Path('data/independent_trials.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    Path('data/independent_summary.json').write_text(json.dumps(summaries,indent=2)+'\n')
    with Path('data/independent_summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(summaries[0])); w.writeheader(); w.writerows(summaries)


if __name__=='__main__':
    start=time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    proof_checks(); simulations()
    metadata=dict(nice=os.getpriority(os.PRIO_PROCESS,0),numpy=np.__version__,scipy=scipy.__version__,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            wall_seconds=time.monotonic()-start,seed=260819145,repetitions_per_case=60,
            numerical_threads_requested=1)
    assert metadata['peak_rss_bytes']<4_000_000_000
    Path('data/independent_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata),flush=True)
