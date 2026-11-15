#!/usr/bin/env python3
import nested as N
import numpy as np, math, time, json, sys

def zeta(p):
    v=p.copy();h=1
    while h<len(v):
        a=v.reshape(-1,2,h);a[:,1]+=a[:,0];h*=2
    return v

def phi(p,q):
    p=max(0.,float(p));q=max(0.,float(q))
    if p==0 or q==0:return 0.
    return (p*math.log1p(q/p)+q*math.log1p(p/q))/math.log(2)

def score(a,b,order):
    mask=0;v=phi(a[0],b[0])
    for j in order:
        new=mask|(1<<j);v+=phi(a[new]-a[mask],b[new]-b[mask]);mask=new
    return v

def climb(a,b,orders,rng):
    best=math.inf;bestorder=None;m=len(orders[0]);evaluations=0
    for initial in orders:
        order=initial[:];v=score(a,b,order)
        for sweep in range(20):
            improved=False
            # Swap any pair, evaluating only the segment whose prefixes change.
            for u,vpos in rng.permutation([(u,v) for u in range(m) for v in range(u+1,m)]):
                u,vpos=int(u),int(vpos)
                trial=order[:];trial[u],trial[vpos]=trial[vpos],trial[u]
                new=score(a,b,trial);evaluations+=1
                if new<v-1e-14:order,v=trial,new;improved=True
            if not improved:break
        if v<best:best,bestorder=v,order[:]
    return best,bestorder,evaluations

def dp(a,b,m):
    v=np.full(1<<m,np.inf);v[0]=phi(a[0],b[0])
    for mask in range(1,1<<m):
        bits=mask
        while bits:
            bit=bits&-bits;prev=mask^bit
            x=v[prev]+phi(a[mask]-a[prev],b[mask]-b[prev])
            if x<v[mask]:v[mask]=x
            bits-=bit
    return float(v[-1])

def run():
    out=[]
    for w,D in [(3,2),(2,4)]:
        T=N.Model(w,D);mu=N.spectrum(T);rng=np.random.default_rng(20261110);rows=[]
        for i in range(T.n):
            start=time.time();p,q=N.paired(mu,i);delta=float(q.sum());E=N.entropy(p,q)/delta
            a,b=zeta(p),zeta(q);orders=[]
            for kind in ['leaves_first','mates_first','clause','block','random','private_last']:
                orders.append([j if j<i else j-1 for j in T.order(kind) if j!=i])
            orders += [rng.permutation(T.n-1).tolist() for _ in range(10)]
            best,order,evals=climb(a,b,orders,rng)
            row={'w':w,'D':D,'n':T.n,'i':i,'type':T.decode(i)[0],'inf':delta,'E_ratio':E,'hill_ratio':best/delta,'order':[j if j<i else j+1 for j in order],'evaluations':evals,'seconds':time.time()-start}
            if T.n<=13:row['exact_min_ratio']=dp(a,b,T.n-1)/delta
            rows.append(row);out.append(row);print(json.dumps(row),flush=True)
            with open('hill.json','w') as f:json.dump(out,f,indent=2)
    return out
if __name__=='__main__':run()
