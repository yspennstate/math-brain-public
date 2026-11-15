#!/usr/bin/env python3
"""Exact finite KCM kernels and independent numerical stationary equations.

Only binary heat-bath models. A bit set to 1 means occupied, matching the paper.
For short periodic sides, repeated images of a neighbor count as one vertex.
No source PDFs, plots, external writes, or multiprocessing are used.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import csv
import itertools
import json
import pathlib
import resource
import time
from collections import defaultdict
from fractions import Fraction
import numpy as np
import sympy as sp

ROOT=pathlib.Path(__file__).resolve().parent.parent


def geometry(shape):
    return list(itertools.product(*(range(n) for n in shape)))


def constraints(shape, model, boundary):
    """Return a list of update-rule bitmasks at each site, incorporating boundary."""
    sites=geometry(shape); index={x:i for i,x in enumerate(sites)}; d=len(shape)
    directions=[]
    for j in range(d):
        for sign in (-1,1):
            u=[0]*d; u[j]=sign; directions.append(tuple(u))
    negative=[tuple(-int(j==k) for j in range(d)) for k in range(d)]
    rules=[]
    for x in sites:
        dirs=negative if model in ('East','NE') else directions
        # Convert the requested neighbor positions to distinct graph vertices or
        # distinct frozen boundary vertices before applying the threshold rule.
        neighbors={}
        for u in dirs:
            y=tuple(a+b for a,b in zip(x,u))
            if boundary=='torus':
                y=tuple(a%n for a,n in zip(y,shape))
            if y in index:
                if y==x:
                    raise ValueError('periodic rule queries the updated site')
                neighbors[('in',index[y])]=None
            else:
                if boundary=='filled': occupied=True
                elif boundary=='empty': occupied=False
                elif boundary=='checker': occupied=bool(sum(y)%2)
                else: raise ValueError(boundary)
                neighbors[('out',y)]=occupied
        vals=list(neighbors.items())
        threshold=2 if model=='FA2' else (len(vals) if model=='NE' else 1)
        allowed=[]
        for choice in itertools.combinations(vals,threshold):
            mask=0
            for (kind,key),occupied in choice:
                if kind=='out' and occupied:
                    break
                if kind=='in': mask|=1<<key
            else:
                allowed.append(mask)
        rules.append(sorted(set(allowed)))
    return sites,rules


def legal(s,i,rules):
    return any((s&mask)==0 for mask in rules[i])


def bootstrap(s,rules):
    while True:
        nxt=s
        for i in range(len(rules)):
            if (s>>i)&1 and legal(s,i,rules): nxt&=~(1<<i)
        if nxt==s: return s
        s=nxt


def generator(rules,a,b):
    n=len(rules); size=1<<n
    M=sp.zeros(size,size)
    edges=[[] for _ in range(size)]
    for s in range(size):
        for i in range(n):
            if legal(s,i,rules):
                t=s^(1<<i); rate=a if (s>>i)&1 else b-a
                M[s,t]=rate; M[s,s]-=rate
                edges[s].append(t)
    return M,edges


def components(edges):
    unseen=set(range(len(edges))); ans=[]
    while unseen:
        start=min(unseen); unseen.remove(start); found=[start]
        for s in found:
            for t in edges[s]:
                if t in unseen: unseen.remove(t); found.append(t)
        ans.append(sorted(found))
    return ans


def solve_case(shape,model,boundary,a,b):
    start=time.monotonic()
    sites,rules=constraints(shape,model,boundary); n=len(sites); size=1<<n
    M,edges=generator(rules,a,b)
    fibers=defaultdict(list)
    for s in range(size): fibers[bootstrap(s,rules)].append(s)
    fs=sorted(fibers.items())
    # Connectivity and BP are constructed separately, then compared as partitions.
    comps=components(edges)
    assert sorted(map(tuple,comps))==sorted(tuple(v) for _,v in fs)
    weights=[a**(n-s.bit_count())*(b-a)**s.bit_count() for s in range(size)]
    vectors=[]; extremals=[]; residual_max=0.0
    for beta,states in fs:
        z=sum(weights[s] for s in states)
        v=sp.zeros(size,1)
        for s in states: v[s]=sp.Rational(weights[s],z)
        assert M.T*v==sp.zeros(size,1)
        assert sum(v)==1
        vectors.append(v)
        # Solve the independent floating-point normalized generator equations.
        if len(states)==1:
            numerical=np.ones(1)
        else:
            sub=np.array(M.extract(states,states).T.tolist(),dtype=float)/b
            rhs=np.zeros(len(states)); rhs[-1]=1.0
            sub[-1,:]=1.0
            numerical=np.linalg.solve(sub,rhs)
        expected=np.array([weights[s]/z for s in states])
        residual_max=max(residual_max,float(np.max(np.abs(numerical-expected))))
        extremals.append({'beta':beta,'states':states,'probabilities':[str(v[s]) for s in states]})
    # An actual exact linear-algebra kernel computation, not just counting classes.
    null=M.T.nullspace()
    assert len(null)==len(fs)
    # Certify that *every* independently returned kernel vector decomposes.
    for u in null:
        rebuilt=sp.zeros(size,1)
        for (_,states),v in zip(fs,vectors):
            rebuilt+=sum(u[s] for s in states)*v
        assert rebuilt==u
    # Exact nontrivial convex combination, with all fibers represented.
    denom=len(fs)*(len(fs)+1)//2
    mixture=sp.zeros(size,1)
    for k,v in enumerate(vectors,1): mixture+=sp.Rational(k,denom)*v
    assert M.T*mixture==sp.zeros(size,1)
    assert sum(mixture)==1 and all(x>=0 for x in mixture)
    # Detailed balance for every legal edge, checked without forming a dense diag.
    for s,neighbors in enumerate(edges):
        for t in neighbors: assert weights[s]*M[s,t]==weights[t]*M[t,s]
    nonproduct=[]
    for e in extremals:
        states=e['states']; ps=[Fraction(p) for p in e['probabilities']]
        marg=[sum(p for s,p in zip(states,ps) if (s>>i)&1) for i in range(n)]
        for i in range(n):
            for j in range(i):
                joint=sum(p for s,p in zip(states,ps) if ((s>>i)&1) and ((s>>j)&1))
                cov=joint-marg[i]*marg[j]
                if cov:
                    nonproduct.append({'beta':e['beta'],'pair':[j,i],'occupied_covariance':str(cov)})
                    break
            if nonproduct and nonproduct[-1]['beta']==e['beta']: break
    result={'shape':shape,'model':model,'boundary':boundary,'q':f'{a}/{b}',
            'n_sites':n,'n_states':size,'bp_fibers':len(fs),'graph_components':len(comps),
            'exact_kernel_dimension':len(null),'exact_rank':size-len(null),
            'largest_fiber':max(len(v) for _,v in fs),
            'absorbing_singletons':sum(len(v)==1 for _,v in fs),
            'exact_kernel_decomposition':True,'exact_stationarity_residual':'0',
            'numeric_max_error':residual_max,'nonproduct_fibers':len(nonproduct),
            'elapsed_s':time.monotonic()-start}
    artifact={**result,'site_order':sites,'rules_as_bitmasks':rules,'extremal_stationary_measures':extremals,
              'nonproduct_examples':nonproduct,
              'mixture_weights':[f'{k}/{denom}' for k in range(1,len(fs)+1)]}
    name=f'{model}_{"x".join(map(str,shape))}_{boundary}_q{a}-{b}'
    (ROOT/'data'/f'{name}.json').write_text(json.dumps(artifact,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return result


def main():
    configs=[]
    for model in ('East','FA1','FA2'):
        for boundary in ('torus','filled','empty','checker'):
            configs.append(((4,),model,boundary))
    for model in ('East','FA1','FA2','NE'):
        for boundary in ('torus','filled','empty','checker'):
            configs.append(((3,2),model,boundary))
    results=[]
    for shape,model,boundary in configs:
        for a,b in ((1,3),(2,3)):
            results.append(solve_case(shape,model,boundary,a,b))
    results.append(solve_case((3,3),'FA2','torus',1,3))
    with (ROOT/'data'/'finite_summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(results[0])); w.writeheader(); w.writerows(results)
    metadata={'cases':len(results),'max_sites':max(x['n_sites'] for x in results),
              'max_states':max(x['n_states'] for x in results),
              'max_numeric_error':max(x['numeric_max_error'] for x in results),
              'all_exact_passed':True,'nice':os.getpriority(os.PRIO_PROCESS,0),
              'numeric_threads':1,'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'python_version':os.sys.version,'numpy_version':np.__version__,'sympy_version':sp.__version__}
    (ROOT/'data'/'verification.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2),flush=True)

if __name__=='__main__': main()
