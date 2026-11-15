import os,json,time,math,resource,itertools
import numpy as np
from experiment import *
from composition import compose,state

def run():
    rows=[];base=json.load(open('structured.json'))['data']
    for name in ['Fano_STS7_DNF','Affine_STS9_DNF','PG23_DNF']:
        record=next(r for r in base if r['name']==name);n=record['n'];x=bits(n);terms=record['terms']
        F=np.where(np.any([x[:,L].all(axis=1) for L in terms],axis=0),-1.,1.)
        ss=state(np.array([1.,-1.]),1)
        for depth in range(1,41 if name=='Fano_STS7_DNF' else 9):
            ss=compose(F,[ss]*n);ss['rows']=ss['rows'][:1];r=ss['rows'][0]
            rows.append(dict(name=name,depth=depth,n=ss['n'],bias=ss['b'],F=r['L']/r['d'],E=r['E']/r['d'],gap=(r['L']-r['E'])/r['d'],d=r['d']))
            if abs(ss['b'])>1-1e-9:break
    # Fixed templates extending the strongest cyclic examples; exact DP, no inference of optimal geometric order.
    for n in [17,18,19,20]:
        x=bits(n)
        for offsets in [[0,1,4],[0,1,5],[0,2,5]]:
            terms=[[(j+c)%n for c in offsets] for j in range(n)]
            f=np.where(np.any([x[:,L].all(axis=1) for L in terms],axis=0),-1.,1.)
            rows.append(dict(name=f'cyclic_{n}_{offsets}',**analyse(f,n,[0])))
    return rows
if __name__=='__main__':
    start=time.time();d=run();out=dict(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=d)
    json.dump(out,open('extra.json','w'),indent=2);print(json.dumps(d,indent=2))
