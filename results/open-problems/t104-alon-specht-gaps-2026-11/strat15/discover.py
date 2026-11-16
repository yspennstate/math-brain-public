"""Float LP discovery; every accepted certificate is replayed exactly."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,time,importlib.util,sys
from fractions import Fraction as F
from pathlib import Path
import exact_bernstein as ex
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('old_discover',ex.S12/'discover.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def attempt(r):
    box=[tuple(map(F,x))for x in r['box']];certs={}
    for key in ('c2','d1','C1'):
        ex.select(key)
        # Reuse the inherited candidate multipliers at the natural leading
        # normalization. This is only a proposal, checked against the new target.
        weights=r['old'].get('lambda',{})
        factors=dict(c2=F(1,16),d1=F(5,8),C1=F(25,16))
        proposal=dict(kind='positivity',box=r['box'],coefficient=key,
                      **{'lambda':{k:str(F(v)*factors[key])for k,v in weights.items()}})
        try:
            lo,method=ex.verify_certificate(proposal)
            if lo>0:proposal.update(lower=str(lo),verification=method);certs[key]=proposal;continue
        except (AssertionError,KeyError):pass
        ex.select(key);cert=old.attempt(box)
        if cert is None:return None,certs,key
        cert['coefficient']=key;certs[key]=cert
    return True,certs,None

if __name__=='__main__':
    inputs=json.loads((HERE/'inventory.json').read_text())['records']
    start=time.monotonic();out=[]
    for r in inputs[:30]:
        if r['old']['kind']=='collar':continue
        ok,certs,failed=attempt(r);out.append(dict(source=r['source'],node=r['node'],path=r.get('path',''),box=r['box'],certificates=certs,failed=failed))
        print(r['source'],r['node'],r.get('path',''),ok,failed,'seconds',time.monotonic()-start,flush=True)
    (HERE/'discovery_pilot.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
