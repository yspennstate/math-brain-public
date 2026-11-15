"""Two bounded discovery workers; exact acceptance of every LP proposal."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,resource,multiprocessing as mp
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from discover import attempt
from exact_bernstein import HERE

def work(r):
    ok,certs,failed=attempt(r)
    return dict(source=r['source'],node=r['node'],path=r.get('path',''),box=r['box'],
                certificates=certs,failed=failed,peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

def main():
    start=time.monotonic();inputs=json.loads((HERE/'inventory.json').read_text())['records']
    inputs=[r for r in inputs if r['old']['kind']!='collar']
    if (HERE/'domain_audit.json').exists():inputs+=json.loads((HERE/'domain_audit.json').read_text())['need_new_sign']
    key=lambda r:(r['source'],r['node'],r.get('path',''))
    records=[]
    if(HERE/'certificates.json').exists():records=json.loads((HERE/'certificates.json').read_text())['records']
    done={key(r)for r in records};todo=[r for r in inputs if key(r)not in done]
    def save():
        count=Counter('open'if r['failed']else 'positive'for r in records)
        result=dict(label='OPEN: exact accepted partial bank; full partition replay pending',total=len(inputs),processed=len(records),counts=dict(count),records=records,
                    elapsed_seconds_NUMERICAL=time.monotonic()-start,
                    conservative_peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss+2*max((r['peak_bytes_NUMERICAL']for r in records),default=0)+128000000)
        tmp=HERE/'certificates.tmp.json';tmp.write_text(json.dumps(result,separators=(',',':'))+'\n');tmp.replace(HERE/'certificates.json')
        msg=f"OPEN: discovery {len(records)}/{len(inputs)}; {dict(count)}; NUMERICAL seconds {result['elapsed_seconds_NUMERICAL']:.1f}, conservative memory {result['conservative_peak_bytes_NUMERICAL']} bytes"
        print(msg,flush=True)
        with(HERE/'LOG.md').open('a')as f:f.write('\n'+msg+'\n')
        assert result['conservative_peak_bytes_NUMERICAL']<2500000000
    with mp.get_context('spawn').Pool(2)as pool:
        for r in pool.imap_unordered(work,todo,chunksize=1):
            records.append(r)
            if len(records)%100==0:save()
    save()
if __name__=='__main__':main()
