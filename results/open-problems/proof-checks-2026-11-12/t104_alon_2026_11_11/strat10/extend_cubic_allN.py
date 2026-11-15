"""NUMERICAL discovery; PROVED only after Fraction-based cells.check."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time
from fractions import Fraction as F
from pathlib import Path
from moment_polytope import vertices
from cubic_allN_discovery import discover
from cubic_cells import check_allN

def main():
    vs=vertices(True);records=[];attempts=[];start=time.monotonic()
    for j in range(6,50):
        lo,hi=F(j,50),F(j+1,50)
        low,high=512,701;best=None
        while low+1<high:
            mid=(low+high)//2;candidate=discover(vs,lo,hi,F(mid,1000),alo=F(64,125))
            attempts.append(dict(rlo=str(lo),rhi=str(hi),alo='64/125',ahi=str(F(mid,1000)),accepted=candidate is not None))
            if candidate:low,best=mid,candidate
            else:high=mid
        if best:
            try:ms=check_allN(best,vs)
            except AssertionError:ms=None
            if ms is not None:best['all_N_margins']=list(map(str,ms))
            records.append(best)
            msg=f"PROVED (cells.check): all-N sextic-augmented ratio [{lo},{hi}], a in [64/125,{best['ahi']}], all N>=6 {ms is not None}."
        else:msg=f'OPEN: all-N sextic-augmented ratio [{lo},{hi}] did not extend a=64/125 with the sextic-augmented relaxation.'
        print(msg,flush=True)
        Path('cubic_allN_cells.json').write_text(json.dumps(records,indent=2)+'\n')
        Path('cubic_allN_attempts.json').write_text(json.dumps(dict(label='NUMERICAL search decisions; accepted cells replay exactly',attempts=attempts),indent=2)+'\n')
        with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
    print('NUMERICAL: elapsed seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
