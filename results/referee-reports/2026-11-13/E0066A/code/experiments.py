"""Reproducible E0066 computations. Run from the report directory.

One thread; no worker pools. Coefficients are indexed p[i,j,k].
All extremality certificates use necessary linear constraints only.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import itertools as it
import json
import platform
import resource
import time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
import sympy as sp
from scipy.linalg import null_space
from scipy.spatial import HalfspaceIntersection
from polytope_probe import system

OUT = Path('data')
SEED = 6602026


def pack(p):
    m = len(p)
    return np.array([p[i,j] for i,j in it.combinations_with_replacement(range(m),2)])


def unpack(v,m):
    p=np.zeros((m,m,m))
    for row,(i,j) in zip(np.asarray(v).reshape(-1,m),it.combinations_with_replacement(range(m),2)):
        p[i,j]=p[j,i]=row
    return p


def affine_permutations(perms):
    """V(x)=sum_i x_i P_i x. Permutations map input index to output index."""
    m=len(perms); p=np.zeros((m,m,m))
    for i in range(m):
        for j in range(m):
            p[i,j,perms[i][j]] += .5
            p[i,j,perms[j][i]] += .5
    return p


def counterexample(m):
    assert m>=4
    perm=list(range(m));perm[:4]=[2,3,0,1]
    perms=[perm.copy() for _ in range(m)]
    perms[0][0],perms[0][1]=perms[0][1],perms[0][0]
    return affine_permutations(perms)


def evaluate_exact(p,x):
    m=len(x)
    return tuple(sum(F(str(p[i,j,k]))*x[i]*x[j]
                     for i in range(m) for j in range(m)) for k in range(m))


def modular_rank(a,prime=1000003):
    a=np.asarray(a,dtype=np.int64).copy()%prime
    rank=0
    for col in range(a.shape[1]):
        candidates=np.flatnonzero(a[rank:,col])
        if not len(candidates):continue
        r=rank+int(candidates[0]);a[[rank,r]]=a[[r,rank]]
        a[rank]=(a[rank]*pow(int(a[rank,col]),-1,prime))%prime
        ids=np.flatnonzero(a[:,col]);ids=ids[ids!=rank]
        a[ids]=(a[ids]-a[ids,col,None]*a[rank])%prime
        rank+=1
        if rank==min(a.shape):break
    return rank


def vertex_certificate(v,m):
    """Exact half-integer feasibility; full rank modulo prime proves Q-rank."""
    pairs,eq,rhs,ub,bound=system(m)
    h=np.rint(2*np.asarray(v).reshape(-1)).astype(np.int64)
    assert np.max(abs(h-2*np.asarray(v).reshape(-1)))<1e-7
    eq=eq.astype(np.int64);rhs=rhs.astype(np.int64)
    ub=ub.astype(np.int64);bound=bound.astype(np.int64)
    feasible=(np.all(h>=0) and np.array_equal(eq@h,2*rhs)
              and np.all(ub@h<=2*bound))
    active=np.vstack([eq,ub[ub@h==2*bound],np.eye(len(h),dtype=np.int64)[h==0]])
    rank=modular_rank(active)
    return dict(feasible=bool(feasible),active_rank=rank,variables=len(h),
                vertex=bool(feasible and rank==len(h)))


def enumerate_m3():
    m=3;pairs,eq,rhs,ub,bound=system(m)
    basis=null_space(eq);center=np.full(eq.shape[1],1/m)
    a=np.vstack([ub,-np.eye(len(center))]);b=np.r_[bound,np.zeros(len(center))]
    hs=np.c_[np.einsum('ij,jk->ik',a,basis),np.einsum('ij,j->i',a,center)-b]
    verts=HalfspaceIntersection(hs,np.zeros(basis.shape[1])).intersections
    keys=set()
    for y in verts:
        v=center+basis@y
        h=tuple(map(int,np.rint(2*v)))
        assert np.max(abs(2*v-h))<1e-7
        cert=vertex_certificate(np.array(h)/2,3)
        assert cert['vertex']
        keys.add(h)
    # Independent exhaustive half-grid cross-check. Completeness of this grid
    # uses the published m=3 half-integrality theorem, not floating Qhull.
    grid=set();feasible=0
    e=np.eye(3,dtype=int)*2
    off=list(e)+[np.array(a) for a in ((1,1,0),(1,0,1),(0,1,1))]
    for diag in it.product(e,repeat=3):
        for mix in it.product(off,repeat=3):
            h=np.array([diag[0],mix[0],mix[1],diag[1],mix[2],diag[2]]).reshape(-1)
            if not np.array_equal(eq@h,2*rhs) or np.any(ub@h>2*bound):continue
            feasible+=1
            if vertex_certificate(h/2,3)['vertex']:grid.add(tuple(map(int,h)))
    assert keys==grid and len(keys)==222
    keys=sorted(keys)
    (OUT/'m3_vertices.json').write_text(json.dumps(dict(
        coefficient_order=[[i,j,k] for i,j in pairs for k in range(3)],
        denominator=2,vertices=keys),indent=2)+'\n')
    return [unpack(np.array(k)/2,3) for k in keys],dict(
        qhull_vertices=len(keys),grid_candidates=3**3*6**3,
        grid_feasible=feasible,grid_vertices=len(grid),rank_modulus=1000003)


def symbolic_checks():
    results=[]
    for m in range(4,7):
        p=counterexample(m)
        if m==4:x=(F(1,3),F(1,3),F(1,6),F(1,6))
        else:x=(F(1,4),F(1,4),F(1,8),F(1,8))+tuple(F(1,4*(m-4)) for _ in range(m-4))
        y=evaluate_exact(p,x);z=evaluate_exact(p,y)
        assert z==x and x!=y and y[:4]==x[2:4]+x[:2]
        cert=vertex_certificate(pack(p).reshape(-1),m)
        assert cert['vertex']
        # Independently derive the homogeneous polynomial from its coefficients.
        xs=sp.symbols('x1:'+str(m+1));total=sum(xs)
        polys=[sum(sp.Rational(str(p[i,j,k]))*xs[i]*xs[j]
                   for i in range(m) for j in range(m)) for k in range(m)]
        expected=[xs[2]*total,xs[3]*total,
                  xs[0]*total-xs[0]**2+xs[0]*xs[1],
                  xs[1]*total+xs[0]**2-xs[0]*xs[1]]+[xs[k]*total for k in range(4,m)]
        assert all(sp.expand(a-b)==0 for a,b in zip(polys,expected))
        results.append(dict(m=m,x=list(map(str,x)),Vx=list(map(str,y)),
                            V2x=list(map(str,z)),vertex_certificate=cert,
                            coefficients_twice=np.rint(2*pack(p)).astype(int).tolist()))
    (OUT/'exact_cycles.json').write_text(json.dumps(results,indent=2)+'\n')
    # Rational witness against the insufficient single-slice inequalities.
    p=unpack(np.array(json.loads((OUT/'subset_condition_probe.json').read_text())[0]['p']),4)
    x=(F(3,5),F(1,4),F(1,10),F(1,20))
    y=evaluate_exact(p,x)
    gap=sum(y[:2])-sum(x[:2])
    pairs,eq,rhs,ub,bound=system(4)
    assert vertex_certificate(pack(p).reshape(-1),4)['feasible'] and gap>0
    # Independently evaluate the four explicit formulas in REPORT.md.
    a,b,c,d=x
    assert y==(a*a+b*b+a*c+b*d,2*a*b+a*c+b*d,
               d*d+a*d+b*c+c*d,c*c+a*d+b*c+c*d)
    witness=dict(x=list(map(str,x)),Vx=list(map(str,y)),gap=str(gap),
                 slice_totals=(eq@pack(p).reshape(-1)).tolist(),
                 vertex_certificate=vertex_certificate(pack(p).reshape(-1),4),
                 coefficients_twice=np.rint(2*pack(p)).astype(int).tolist())
    (OUT/'outer_polytope_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    return results,witness


def chamber_matrix(p,permutation,outputs):
    """Exact Q with z^T Q z = top_r(x)*sum(x)-sum_{k in K}V_k(x).

    x=T z, x[permutation[j]]=z[j]+...+z[m-1].
    Copositivity of all these matrices is an exact full-class criterion.
    """
    m=len(p);T=sp.zeros(m);a=sp.zeros(m,1);one=sp.ones(m,1)
    for j,i in enumerate(permutation):
        for l in range(j,m):T[i,l]=1
    for i in permutation[:len(outputs)]:a[i]=1
    B=sp.Matrix(m,m,lambda i,j:sum(sp.Rational(str(p[i,j,k])) for k in outputs))
    return T.T*((a*one.T+one*a.T)/2-B)*T


def simulate(p,starts,steps=1024,tail=96,tol=1e-8):
    m=len(p);x=np.array(starts,float);history=[];maxmass=0.;maxmajor=0.
    for n in range(steps):
        y=np.einsum('ijk,si,sj->sk',p,x,x,optimize=False)
        mass=y.sum(axis=1);maxmass=max(maxmass,float(np.max(abs(mass-1))))
        y/=mass[:,None]  # Remove floating total-mass drift from quadratic evaluation.
        major=np.cumsum(np.sort(y,axis=1)[:,::-1],axis=1)-np.cumsum(np.sort(x,axis=1)[:,::-1],axis=1)
        maxmajor=max(maxmajor,float(major.max()))
        x=y
        if n>=steps-tail:history.append(x.copy())
    h=np.array(history);periods=[];residuals=[]
    for s in range(len(x)):
        found=0;best=1.
        for lag in range(1,49):
            err=float(np.max(abs(h[lag:,s]-h[:-lag,s])))
            best=min(best,err)
            if err<tol:found=lag;break
        periods.append(found);residuals.append(best)
    return periods,residuals,maxmass,maxmajor


def latin(m,rng):
    alpha=rng.permutation(m);beta=rng.permutation(m)
    p=np.zeros((m,m,m))
    for i in range(m):
        for j in range(m):p[i,j,beta[(alpha[i]+alpha[j])%m]]=1
    return p


def main():
    start=time.time();OUT.mkdir(exist_ok=True)
    rng=np.random.default_rng(SEED)
    extremes,enumeration=enumerate_m3()
    exact,witness=symbolic_checks()
    tables=[];operators={};details=[]
    for m in range(3,7):
        pairs,eq,rhs,ub,bound=system(m)
        if m<=5:
            (OUT/f'm{m}_outer_H.json').write_text(json.dumps(dict(
                meaning='Exact for m=3; necessary outer polytope for m>=4',
                pairs=pairs,variables=len(pairs)*m,
                affine_dimension=(m-1)*(len(pairs)-1),
                Aeq=eq.astype(int).tolist(),beq=rhs.astype(int).tolist(),
                Aub=ub.astype(int).tolist(),bub=bound.astype(int).tolist(),
                lower_bound=0),indent=2)+'\n')
        families={}
        families['all_m3_extremes' if m==3 else 'latin_extremes']=(
            extremes if m==3 else [latin(m,rng) for _ in range(24)])
        families['affine_permutation_random']=[affine_permutations([rng.permutation(m) for _ in range(m)]) for _ in range(24)]
        families['convex_random']=[.2*np.full((m,m,m),1/m)+.8*affine_permutations([rng.permutation(m) for _ in range(m)]) for _ in range(12)]
        families['permutation_controls']=[affine_permutations([rng.permutation(m)]*m) for _ in range(4)]
        if m>=4:families['nonlinear_extreme_counterexample']=[counterexample(m)]
        for family,ps in families.items():
            counts={};maxmass=maxmajor=maxunresolved=0.;nstarts=0
            for j,p in enumerate(ps):
                if family=='nonlinear_extreme_counterexample':
                    x=np.array([float(F(s)) for s in exact[m-4]['x']])
                    starts=np.vstack([rng.dirichlet(np.ones(m),size=12),x,np.ones(m)/m,np.eye(m)])
                else:starts=np.vstack([rng.dirichlet(np.ones(m),size=12),np.ones(m)/m,np.eye(m)])
                periods,resids,mass,major=simulate(p,starts)
                for t in periods:counts[str(t)]=counts.get(str(t),0)+1
                for t,e in zip(periods,resids):
                    if t==0:maxunresolved=max(maxunresolved,e)
                maxmass=max(maxmass,mass);maxmajor=max(maxmajor,major);nstarts+=len(starts)
                key=f'{m}_{family}_{j}'
                operators[key]=p
                details.append(dict(key=key,starts=starts.tolist(),periods=periods,tail_residuals=resids))
            row=dict(m=m,family=family,operators=len(ps),unique_operators=len({p.tobytes() for p in ps}),
                     starts=nstarts,steps=1024,period_counts=counts,max_mass_error=maxmass,
                     max_majorisation_error=maxmajor,max_unresolved_tail_residual=maxunresolved)
            tables.append(row);print(row,flush=True)
    np.savez_compressed(OUT/'operators.npz',**operators)
    (OUT/'trajectory_details.json').write_text(json.dumps(details,indent=2)+'\n')
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if platform.system()=='Darwin' else rss*1024
    summary=dict(seed=SEED,numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
                 python=platform.python_version(),threads=1,worker_pools=0,
                 elapsed_seconds=time.time()-start,peak_rss_bytes=rss_bytes,
                 enumeration=enumeration,tables=tables)
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    md=['| m | family | operators (unique) | starts | tail period counts |',
        '|---:|---|---:|---:|---|']
    for row in tables:
        md.append(f"| {row['m']} | {row['family']} | {row['operators']} ({row['unique_operators']}) | {row['starts']} | "+', '.join(f'{k}: {v}' for k,v in sorted(row['period_counts'].items(),key=lambda q:int(q[0])))+' |')
    (OUT/'tables.md').write_text('\n'.join(md)+'\n')
    print('enumeration',enumeration,'peak RSS bytes',rss_bytes,'seconds',time.time()-start,flush=True)


if __name__=='__main__':main()
