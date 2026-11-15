#!/usr/bin/env python3
"""Independent exact small-instance and move checks; saves the outcomes."""
import itertools
import json
import subprocess
import time
from pathlib import Path
import numpy as np
from experiment import instance, ROOT

def exact(xy):
    n=len(xy)
    delta=np.abs(xy[:,None,:]-xy[None,:,:]);delta=np.minimum(delta,1-delta)
    dist=np.sqrt((delta*delta).sum(axis=2))
    # Held-Karp dynamic programming with vertex 0 fixed.
    dp=np.full((1<<(n-1),n-1),np.inf)
    for j in range(n-1):dp[1<<j,j]=dist[0,j+1]
    for mask in range(1,1<<(n-1)):
        js=[j for j in range(n-1) if mask>>j&1]
        for j in js:
            previous=mask^(1<<j)
            if previous:
                ks=[k for k in js if k!=j]
                dp[mask,j]=min(dp[previous,k]+dist[k+1,j+1] for k in ks)
    return float(min(dp[-1,j]+dist[j+1,0] for j in range(n-1)))

def bound(xy,upper,iterations=160):
    payload=f'{len(xy)} {iterations} {upper:.17g}\n'
    payload+='\n'.join(f'{x:.17g} {y:.17g}' for x,y in xy)+'\n'
    p=subprocess.run([str(ROOT/'code/held_karp_bound')],input=payload,text=True,
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    return json.loads(p.stdout)

def main():
    results=[];start=time.monotonic()
    for n,count in [(5,8),(8,8),(12,12),(16,4)]:
        for index in range(count):
            row,xy,tour=instance(n,index,kicks=20,audit=True,seed_base=880003)
            optimum=exact(xy)
            lower=bound(xy,row['best'],80)
            assert lower['lower_bound']<=optimum+1e-9
            assert row['best']>=optimum-1e-9
            results.append({'n':n,'index':index,'optimum':optimum,
                            'heuristic':row['best'],'gap':row['best']-optimum,
                            'hk_lower':lower['lower_bound'],'cap_hits':row['cap_hits']})
    for index in range(4):
        row,_,_=instance(100,index,kicks=8,audit=True,seed_base=880003)
        results.append({'n':100,'index':index,'move_audit':True,'cap_hits':row['cap_hits']})
    out={'elapsed_seconds':time.monotonic()-start,'checks':results,
         'exact_instances':sum('optimum' in r for r in results),
         'max_exact_gap':max(r.get('gap',0) for r in results)}
    (ROOT/'data/validation.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='checks'}),flush=True)

if __name__=='__main__':main()
