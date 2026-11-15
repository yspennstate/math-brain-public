"""Structured families, greedy reveal policy, and invertible F2 coordinate changes."""
import json,itertools,math,time,os,resource
import numpy as np
from experiment import *

def greedy(p,q):
    a,b=zeta(p),zeta(q);N=len(p);m=(N-1).bit_length();R=0;order=[]
    while R<N-1:
        choices=[]
        for j in range(m):
            if (R>>j)&1:continue
            S=R|(1<<j);da=max(0,a[S]-a[R]);db=max(0,b[S]-b[R])
            score=float(phi(da,db)+phi(max(0,a[-1]-a[S]),max(0,b[-1]-b[S])))
            choices.append((score,j))
        j=min(choices)[1];R|=1<<j;order.append(j)
    return order_cost(p,q,order)[0],order

def policy_compare():
    import importlib.util
    src='~/fei_solve_agent/code/local_cs.py'
    spec=importlib.util.spec_from_file_location('inherited',src);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    functions=list(mod.families(12))
    srcdir='~/fei_solve_agent/code/hill_out'
    for name in sorted(os.listdir(srcdir)):
        if not name.startswith('best_'):continue
        import re
        text=open(srcdir+'/'+name).read();v=int(re.search(r'tt=([0-9a-fA-F]+)',text).group(1),16)
        n=int(re.search(r'_n(\d+)_',name).group(1))
        functions.append((name,n,np.array([-1. if (v>>x)&1 else 1. for x in range(1<<n)])))
    rows=[]
    for name,n,f in functions:
        mu=wht(f)**2;best=math.inf;rule=math.inf;bestE=math.inf
        for i in range(n):
            p,q=masses(mu,i);delta=float(q.sum())
            if not delta:continue
            best=min(best,best_order(p,q)[0]/delta);rule=min(rule,greedy(p,q)[0]/delta);bestE=min(bestE,float(phi(p,q).sum())/delta)
        rows.append(dict(name=name,n=n,opt=best,rule=rule,additive=rule-best,factor=rule/best if best>1e-10 else None,E=bestE))
    return rows

def families_scan():
    rng=np.random.default_rng(191912);rows=[]
    for n in range(8,17):
        x=bits(n)
        for a,b in itertools.combinations(range(1,min(n,8)),2):
            terms=[[(j+c)%n for c in [0,a,b]] for j in range(n)]
            f=np.where(np.any([x[:,L].all(axis=1) for L in terms],axis=0),-1.,1.)
            rr=analyse(f,n,[0]);rows.append(dict(name=f'cyclic_{n}_0_{a}_{b}',terms=terms,truth=truthhex(f),**rr))
    for n in [10,12,14,16]:
        x=bits(n)
        for t in range(8):
            k=[3,4,5,6][t%4];m=min(math.comb(n,k),round(math.log(2)*2**k));terms=set()
            while len(terms)<m:terms.add(tuple(sorted(rng.choice(n,k,replace=False).tolist())))
            terms=sorted(terms);f=np.where(np.any([x[:,L].all(axis=1) for L in terms],axis=0),-1.,1.)
            rr=analyse(f,n);rows.append(dict(name=f'random_DNF_{n}_{k}_{t}',terms=terms,truth=truthhex(f),**rr))
        for t in range(3):
            parity=(x[:,::2]*x[:,1::2]).sum(axis=1)%2;f=1.-2.*parity
            ids=rng.choice(1<<n,1 if t==0 else n,replace=False);f[ids]*=-1.
            rows.append(dict(name=f'quadratic_patch_{n}_{t}',flips=ids.tolist(),**analyse(f,n)))
    return rows

def linear_scan():
    rng=np.random.default_rng(191913);rows=[]
    for n in [6,8,9,10,12]:
        x=bits(n);bases=[('MAJ',np.where(x.sum(axis=1)*2>n,-1.,1.))]
        if n%2==0:bases.append(('TRIBES2',np.where(x.reshape(-1,n//2,2).all(axis=2).any(axis=1),-1.,1.)))
        if n==9:
            tok=open('~/fei_solve_agent/code/hill_out/pm_k33_host_n9.txt').read().split()[-1];v=int(tok,16)
            bases.append(('PMhost',np.array([-1. if(v>>j)&1 else 1. for j in range(1<<n)])))
        for name,f in bases:
            rows.append(dict(name=name,n=n,change='identity',**{k:v for k,v in analyse(f,n).items() if k!='n'}))
            for t in range(16):
                y=np.arange(1<<n).copy();ops=[]
                for z in range(n*3):
                    a,b=rng.choice(n,2,replace=False).tolist();y^=((y>>a)&1)<<b;ops.append([a,b])
                ff=f[y];rr=analyse(ff,n)
                rows.append(dict(name=name,change=t,ops=ops,entropy_residual=float(np.max(np.sort(wht(f)**2)-np.sort(wht(ff)**2))),**rr))
    return rows

if __name__=='__main__':
    mode=sys.argv[1];start=time.time();d=policy_compare() if mode=='policy' else linear_scan() if mode=='linear' else families_scan()
    out=dict(mode=mode,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=d)
    json.dump(out,open(mode+'.json','w'),indent=2)
    print(json.dumps(dict(mode=mode,count=len(d),best=sorted([{k:r[k] for k in ['name','F','E','gap'] if k in r} for r in d],key=lambda x:x.get('F',0),reverse=True)[:15]),indent=2))
