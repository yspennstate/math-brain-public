#!/usr/bin/env python3
"""Uniform peeled face skeleton: omit pocket fillings, wire unfinished half-edges.
Run-length boundary representation handles arbitrarily large sampled faces.
Forcing one BLAS thread avoids hidden numerical thread pools.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import csv,math,json,time
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from peeling_layers import Sampler

def split_at(runs,index):
    left=[];right=[]
    for v,c in runs:
        if index>=c:
            left.append((v,c));index-=c
        elif index>0:
            left.append((v,index));right.append((v,c-index));index=0
        else:right.append((v,c))
    assert index==0
    return left,right

def rotate(runs,index):
    l,r=split_at(runs,index)
    return r+l

def label_at(runs,index):
    for v,c in runs:
        if index<c:return v
        index-=c
    raise IndexError(index)

def statistics_for(runs,parents,glue_edges,p):
    nv=len(parents);legs=[0]*nv
    for v,c in runs:legs[v]+=c
    assert sum(legs)==2*p
    desc=legs.copy()
    for v in range(nv-1,0,-1):desc[parents[v]]+=desc[v]
    assert desc[0]==2*p
    energy=sum((x/(2*p))**2 for x in desc[1:])+1/(4*p)
    cond=[2.*x for x in legs]
    for v in range(nv-1,0,-1):
        if cond[v]>0:cond[parents[v]]+=cond[v]/(1+cond[v])
    tree_r=1/cond[0]
    diag=[2.*x for x in legs];ii=[];jj=[];vv=[]
    edges=[(v,parents[v]) for v in range(1,nv)]+glue_edges
    for u,v in edges:
        if u==v:continue
        diag[u]+=1;diag[v]+=1
        ii.extend([u,v]);jj.extend([v,u]);vv.extend([-1.,-1.])
    ii.extend(range(nv));jj.extend(range(nv));vv.extend(diag)
    lap=coo_matrix((vv,(ii,jj)),shape=(nv,nv)).tocsc()
    rhs=np.zeros(nv);rhs[0]=1
    voltage=spsolve(lap,rhs)
    skeleton_r=float(voltage[0])
    # Independently evaluate dissipated energy at the solution.
    effective_energy=sum((voltage[u]-voltage[v])**2 for u,v in edges)
    effective_energy+=sum(2*c*voltage[v]**2 for v,c in enumerate(legs))
    relerr=abs(effective_energy-skeleton_r)/max(1.,skeleton_r)
    assert relerr<1e-7,(relerr,skeleton_r,effective_energy)
    assert 0<skeleton_r<=tree_r+1e-8<=energy+2e-8
    return dict(vertices=nv,active_run_count=len(runs),uniform_tree_energy=energy,
                tree_resistance=tree_r,skeleton_resistance=skeleton_r,
                electrical_energy_relative_error=relerr)

def run():
    start=time.monotonic();rows=[];checkpoints={100,500,2000};reps=12
    for ai,a in enumerate([1.8,2.,2.2,2.4]):
        for rep in range(reps):
            seed=1590000+10000*ai+rep;s=Sampler(a,seed)
            p=1;runs=[(0,2)];parents=[-1];glue_edges=[];previous=0
            for n in range(1,max(checkpoints)+1):
                k=s.step(p)
                j=s.rng.randrange(2*p)
                runs=rotate(runs,j)
                if k>=0:
                    parent=runs[0][0];v=len(parents);parents.append(parent)
                    _,runs=split_at(runs,1)
                    runs=[(v,2*k+1)]+runs
                else:
                    # The orientation is immaterial: a cyclic block has uniform starting position.
                    u=runs[0][0];v=label_at(runs,2*(-k)-1)
                    glue_edges.append((u,v))
                    _,runs=split_at(runs,2*(-k))
                p+=k
                if n in checkpoints:
                    stats=statistics_for(runs,parents,glue_edges,p)
                    assert stats['skeleton_resistance']+1e-7>=previous
                    previous=stats['skeleton_resistance']
                    rows.append(dict(a=a,rep=rep,seed=seed,n=n,p=p,**stats))
        print('finished skeleton',a,flush=True)
    with open('data/skeleton_runs.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    meta=dict(replicates=reps,checkpoints=sorted(checkpoints),a_values=[1.8,2.,2.2,2.4],
              elapsed_seconds=time.monotonic()-start,niceness=os.getpriority(os.PRIO_PROCESS,0),threads=1,
              model='Exact canonical uniform peeling skeleton, finite pocket fillings omitted, active half-edges of resistance 1/2 wired. These are not full finite Boltzmann maps.',
              interpretation='Finite resistances increase to the skeleton resistance to infinity, which is at least that of the full dual. Finite values do not upper-bound the full infinite resistance.')
    Path('data/skeleton_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta),flush=True)

if __name__=='__main__':run()
