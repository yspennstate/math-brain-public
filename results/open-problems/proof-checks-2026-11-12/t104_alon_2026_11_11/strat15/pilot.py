"""Exact first pass over the requested positivity frontier."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time
from fractions import Fraction as F
from exact_bernstein import *

def main():
    inputs=json.loads((HERE/'inventory.json').read_text())['records']
    out=[];counts={};start=time.monotonic()
    for i,r in enumerate(inputs):
        if r['old']['kind']=='collar':continue
        box=[tuple(map(F,x))for x in r['box']];certs={}
        for key in ('c2','d1','C1'):
            select(key);p=data()[0]
            tr,den=normal(p,box)
            lo=F(tr.get((0,)*6,0)-sum(abs(c)for m,c in tr.items()if any(m)),den)
            if lo>0:certs[key]=dict(kind='positivity',coefficient=key,box=r['box'],**{'lambda':{}},lower=str(lo),verification='absolute-envelope')
        counts[len(certs)]=counts.get(len(certs),0)+1
        out.append(dict(source=r['source'],node=r['node'],path=r.get('path',''),box=r['box'],certificates=certs))
        if (i+1)%500==0:print('exact envelope pilot',i+1,counts,'seconds',time.monotonic()-start,flush=True)
    (HERE/'pilot.json').write_text(json.dumps(dict(counts=counts,records=out),separators=(',',':'))+'\n')
    print(counts,time.monotonic()-start)
if __name__=='__main__':main()
