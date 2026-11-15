import os,json,time,resource
import numpy as np
from experiment import bits,analyse,truthhex
def run():
    rng=np.random.default_rng(191916);rows=[]
    for n in [10,12,14,16]:
        x=bits(n)
        for k in [3,4,5,6]:
            for repeat in range(2):
                covered=np.zeros(1<<n,bool);terms=[];before=0.
                while float(covered.mean())<.5:
                    ids=rng.choice(n,k,replace=False);sign=rng.integers(0,2,k)
                    before=float(covered.mean());covered|=(x[:,ids]==sign).all(axis=1);terms.append(dict(ids=ids.tolist(),values=sign.tolist()))
                f=np.where(covered,-1.,1.);r=analyse(f,n)
                rows.append(dict(name=f'random_signed_threshold_{n}_{k}_{repeat}',width=k,term_count=len(terms),probability_before=before,probability_after=float(covered.mean()),terms=terms,truth=truthhex(f),**r))
    return rows
if __name__=='__main__':
    start=time.time();d=run();out=dict(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=d)
    json.dump(out,open('random_threshold.json','w'),indent=2);print(json.dumps([{k:r[k] for k in ['name','term_count','F','E','gap','probability_before','probability_after']} for r in d],indent=2))
