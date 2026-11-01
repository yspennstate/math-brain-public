#!/usr/bin/env python3
"""Exploratory FEI erasure-entropy calculations; no global certification.

Truth tables have integer values +/-1. Walsh transforms are exact int64.
Entropy comparisons use floating point and are explicitly exploratory.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from pathlib import Path
import numpy as np


def walsh(f):
    a = np.array(f, dtype=np.int64, copy=True)
    n = a.shape[-1]
    h = 1
    while h < n:
        b = a.reshape(*a.shape[:-1], -1, 2*h)
        x, y = b[..., :h].copy(), b[..., h:].copy()
        b[..., :h], b[..., h:] = x+y, x-y
        h *= 2
    return a


def ent_terms(p):
    return -p * np.log2(np.where(p > 0, p, 1.0))


def stats_walsh(w):
    w = np.asarray(w)
    N = w.shape[-1]
    n = N.bit_length()-1
    p = (w.astype(float)/N)**2
    H = ent_terms(p).sum(axis=-1)
    Is, Bs, Ds, JSs = [], [], [], []
    for i in range(n):
        block = w.reshape(*w.shape[:-1], -1, 2, 1 << i)
        u = block[..., 0, :].reshape(*w.shape[:-1], -1).astype(float)/N
        v = block[..., 1, :].reshape(*w.shape[:-1], -1).astype(float)/N
        r, s = u*u, v*v
        m = r+s
        B = (ent_terms(r)+ent_terms(s)-ent_terms(m)).sum(axis=-1)
        qp, qm = (u+v)**2, (u-v)**2
        JS = (ent_terms(m)-0.5*ent_terms(qp)-0.5*ent_terms(qm)).sum(axis=-1)
        Is.append(s.sum(axis=-1)); Bs.append(B); JSs.append(JS); Ds.append(B+JS)
    if not n:
        return {"H":H,"I":H*0,"J":H*0,"B":H*0,"D":H*0}
    Is, Bs, Ds, JSs = map(lambda x:np.stack(x,axis=-1),(Is,Bs,Ds,JSs))
    I, J, B, D = Is.sum(axis=-1), np.minimum(Is,1-Is).sum(axis=-1), Bs.sum(axis=-1), Ds.sum(axis=-1)
    nz = np.where(J > 0,J,1)
    return {"H":H,"I":I,"J":J,"B":B,"D":D,"B_over_J":B/nz,"D_over_J":D/nz,
            "H_over_J":H/nz,"influences":Is,"erasure":Bs,"defects":Ds,"JS":JSs}


def stats(f):
    return stats_walsh(walsh(f))


def plain(d):
    return {k:np.asarray(v).tolist() for k,v in d.items()}


def exhaustive(n, batch=2048):
    N=1 << n
    best={k:(-1,None,None) for k in ['B_over_J','D_over_J','H_over_J']}
    max_identity_error=0.0
    for start in range(0,1 << N,batch):
        labels=np.arange(start,min(start+batch,1 << N),dtype=np.uint64)
        f=1-2*((labels[:,None]>>np.arange(N,dtype=np.uint64))&1).astype(np.int64)
        w=walsh(f)
        assert np.all((w*w).sum(axis=1)==N*N)
        st=stats_walsh(w)
        assert np.min(st['B'])>=-1e-10
        assert np.max(st['B']-st['H'])<=1e-10
        assert np.min(st['JS'])>=-1e-10
        assert np.max(st['JS']-(2/math.log(2))*np.minimum(st['influences'],1-st['influences']))<=1e-10
        for i in range(n):
            fblock=f.reshape(len(f),-1,2,1 << i)
            fp=fblock[:,:,0,:].reshape(len(f),-1)
            fm=fblock[:,:,1,:].reshape(len(f),-1)
            hp=ent_terms((walsh(fp)/(N/2))**2).sum(axis=-1)
            hm=ent_terms((walsh(fm)/(N/2))**2).sum(axis=-1)
            err=np.max(np.abs(st['defects'][:,i]-st['H']+0.5*(hp+hm)))
            max_identity_error=max(max_identity_error,float(err))
            assert err<1e-10
        for k in best:
            ix=int(np.argmax(st[k]))
            if st[k][ix]>best[k][0]:
                best[k]=(float(st[k][ix]),int(labels[ix]),plain(stats(f[ix])))
    return {'n':n,'truth_tables':1 << N,'arithmetic':'exact integer Walsh; floating entropy only',
            'max_restriction_identity_error':max_identity_error,
            'maxima_exploratory':best}


def random_search(n, seed=91317, samples=10000):
    rng=np.random.default_rng(seed+n)
    N=1 << n
    best={k:(-1,None,None) for k in ['B_over_J','D_over_J','H_over_J']}
    for j in range(samples):
        if j%3==0:
            m=int(rng.integers(1,max(2,N//2)))
        else:
            m=min(N//2,max(1,int(2**rng.uniform(0,n-1))))
        f=np.ones(N,dtype=np.int64)
        f[rng.choice(N,m,replace=False)]=-1
        st=stats(f)
        for k in best:
            if st[k]>best[k][0]:
                best[k]=(float(st[k]),np.flatnonzero(f<0).tolist(),plain(st))
    return {'n':n,'seed':seed+n,'samples':samples,'maxima_exploratory':best}


def local_search(n,seed=4481,restarts=16,steps=300):
    rng=np.random.default_rng(seed+n)
    N=1 << n
    idx=np.arange(N,dtype=np.uint64)
    h=np.array([[1-2*(int(x&y).bit_count()%2) for y in idx] for x in idx],dtype=np.int64)
    best=(-1,None,None)
    for r in range(restarts):
        f=np.ones(N,dtype=np.int64)
        f[rng.choice(N,int(rng.integers(1,N//2+1)),replace=False)]=-1
        w=walsh(f)
        score=float(stats_walsh(w)['B_over_J'])
        for k in range(steps):
            if N<=256:
                picks=np.arange(N)
            else:
                picks=rng.choice(N,256,replace=False)
            proposals=w[None,:]-2*f[picks,None]*h[picks]
            scores=stats_walsh(proposals)['B_over_J']
            ix=int(np.argmax(scores))
            if scores[ix]>score+1e-12:
                at=int(picks[ix]); w=proposals[ix]; f[at]*=-1; score=float(scores[ix])
            else:
                if score>best[0]: best=(score,np.flatnonzero(f<0).tolist(),plain(stats_walsh(w)))
                break
        if score>best[0]: best=(score,np.flatnonzero(f<0).tolist(),plain(stats_walsh(w)))
    return {'n':n,'seed':seed+n,'restarts':restarts,'steps_limit':steps,'best_exploratory':best}


def bent_marker(m):
    assert m%2==0
    N=1 << m
    g=np.array([1-2*(sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(m//2))%2) for x in range(N)])
    h=g.copy(); h[0]*=-1
    f=np.concatenate([g,h])
    st=stats(f)
    return {'base_dimension':m,'selector_influence':float(st['influences'][-1]),
            'selector_defect_ratio':float(st['defects'][-1]/st['influences'][-1]),
            'stats':plain(st)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['baseline','search'],default='baseline')
    ap.add_argument('--output',type=Path,default=Path('experiment_results.json'))
    args=ap.parse_args()
    started=time.time()
    if args.mode=='baseline':
        result={'exhaustive':[exhaustive(n) for n in range(1,5)],
                'bent_marker':[bent_marker(m) for m in range(2,17,2)],
                'random':[random_search(n,samples=1500) for n in range(5,11)]}
    else:
        result={'local_search':[local_search(n,restarts=30) for n in range(5,11)]}
    result['elapsed_seconds']=time.time()-started
    result['status']='EXPLORATORY; finite tests do not prove FEI or a uniform bound'
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'elapsed_seconds':result['elapsed_seconds']}))
    for row in result.get('exhaustive',[])+result.get('random',[]):
        print(json.dumps({'n':row['n'],'maxima':{k:v[0] for k,v in row['maxima_exploratory'].items()}}))
    for row in result.get('local_search',[]):
        print(json.dumps({'n':row['n'],'B_over_J':row['best_exploratory'][0]}))
    for row in result.get('bent_marker',[]):
        print(json.dumps({k:row[k] for k in ['base_dimension','selector_influence','selector_defect_ratio']}))


if __name__=='__main__':main()
