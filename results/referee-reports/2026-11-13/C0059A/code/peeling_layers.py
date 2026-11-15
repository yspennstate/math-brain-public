#!/usr/bin/env python3
"""Exact canonical perimeter/layer simulation (BC17, Lemma 6.1, eq. 34).
No tail cutoff, no full maps, no effective-resistance estimator.
One thread; all output confined to data/.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import math,random,csv,json,time,statistics
from pathlib import Path
from functools import lru_cache

@lru_cache(maxsize=4096)
def logh(n):
    assert n>=1
    if n>=10000:
        return math.log(2/math.sqrt(math.pi))+.5*math.log(n)-1/(8*n)+1/(192*n**3)
    return math.log(2/math.sqrt(math.pi))+math.lgamma(n+.5)-math.lgamma(n)

def beta_geometric(rng,alpha,beta):
    b=rng.betavariate(alpha,beta)
    if b==1:return 1
    if b==0:raise ArithmeticError('Floating point beta underflow; no silent tail truncation.')
    return max(1,math.ceil(math.log1p(-rng.random())/math.log1p(-b)))

class Sampler:
    def __init__(self,a,seed):
        self.a=a; self.rng=random.Random(seed);self.proposals=0;self.accepted=0
        self.negmass=1/(2*(a-1))
    def step(self,p):
        while True:
            self.proposals+=1
            if self.rng.random()<1/(1+self.negmass):
                k=beta_geometric(self.rng,self.a-1.5,2.5-self.a)
                z=0.0 if p==1 else logh(p+k)-logh(p)-logh(k+1)
            else:
                j=beta_geometric(self.rng,self.a-1,.5)
                if j>=p:continue
                k=-j;z=logh(p-j)-logh(p)
            assert z<1e-9,(p,k,z)
            if math.log(max(self.rng.random(),1e-300))<=min(0,z):
                self.accepted+=1
                return k

def layer_update(p,d,height,k,side):
    newp=p+k
    assert newp>0 and 1<=d<=2*p
    if k>=0:
        d-=1
    elif side==0:
        d-=2*(-k)
    else:
        d=min(d-1,2*newp)
    if d<=0:
        height+=1;d=2*newp
    assert 1<=d<=2*newp
    return newp,d,height

def run():
    start=time.monotonic();rows=[];layerrows=[];checks=[]
    checkpoints={100,1000,5000,20000};reps=32
    for ai,a in enumerate([1.8,2.,2.2,2.4]):
        for rep in range(reps):
            seed=590000+10000*ai+rep;s=Sampler(a,seed)
            p,d,height=1,2,0;clock=0.;lower=.5
            for n in range(1,max(checkpoints)+1):
                clock+=1/(2*p)
                k=s.step(p)
                oldheight=height
                p,d,height=layer_update(p,d,height,k,s.rng.randrange(2))
                if height>oldheight:
                    lower+=1/(2*p)
                    if rep<3:
                        layerrows.append(dict(a=a,rep=rep,n=n,height=height,p=p,layer_lower=lower))
                if n in checkpoints:
                    rows.append(dict(a=a,rep=rep,seed=seed,n=n,p=p,height=height,
                                     clock_sum=clock,layer_lower=lower))
            checks.append(dict(a=a,rep=rep,proposals=s.proposals,accepted=s.accepted,
                               acceptance=s.accepted/s.proposals,expected_acceptance=1/(1+s.negmass)))
        print('finished',a,flush=True)
    def save(name,records):
        with open('data/'+name,'w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    save('peeling_runs.csv',rows);save('peeling_layers.csv',layerrows);save('sampler_acceptance.csv',checks)
    summary=[]
    for a in [1.8,2.,2.2,2.4]:
        for n in sorted(checkpoints):
            rr=[r for r in rows if r['a']==a and r['n']==n]
            out=dict(a=a,n=n,reps=reps)
            for key in ['p','height','clock_sum','layer_lower']:
                xs=sorted(r[key] for r in rr)
                out[key+'_median']=statistics.median(xs)
                out[key+'_q25']=xs[7];out[key+'_q75']=xs[24]
            out['clock_sum_mean']=statistics.mean(r['clock_sum'] for r in rr)
            summary.append(out)
    save('peeling_summary.csv',summary)
    meta=dict(seed_scheme='590000+10000*parameter_index+rep',replicates=reps,
              checkpoints=sorted(checkpoints),a_values=[1.8,2.,2.2,2.4],steps_total=len(checks)*max(checkpoints),
              niceness=os.getpriority(os.PRIO_PROCESS,0),threads=1,
              elapsed_seconds=time.monotonic()-start,
              limitations='Canonical BC17 family only. Exact infinite perimeter/layer kernel, floating-point sampling. Layer lower bound, not effective resistance. No face fillings sampled. Quartiles are empirical dispersion, not confidence intervals.')
    Path('data/simulation_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta),flush=True)

if __name__=='__main__':run()
