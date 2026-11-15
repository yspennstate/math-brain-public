import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np,math,json,time,resource
from pathlib import Path
from experiments import unpack
from composition import fw,ph
def bin_ratio(a,b):
    if a==0:return 'lower_zero'
    if b==0:return 'upper_zero'
    k=a.bit_length()-b.bit_length()
    if (a<(b<<k)) if k>=0 else ((a<<(-k))<b):k-=1
    return k
def main():
    rng=np.random.default_rng(141432);cases=0;low=high=0;cellcount=0;start=time.time()
    funcs=[]
    for n in range(1,6):funcs.extend(unpack(hex(int(t)),n) for t in np.fromfile(f'../FEIB12/npn{n}.bin',dtype='<u4')[:512])
    for n in range(6,11):funcs.extend(rng.choice([-1,1],1<<n).astype(np.int8) for _ in range(64))
    for f in funcs:
        n=len(f).bit_length()-1;mu=[int(round(x*len(f)))**2 for x in fw(f)]
        for i in range(n):
            exact=0.;cells={};delta=0
            for t in range(1<<n):
                if t>>i&1:continue
                a,b=mu[t],mu[t|(1<<i)];exact+=ph(a,b);delta+=b
                label=bin_ratio(a,b);aa,bb=cells.get(label,(0,0));cells[label]=(aa+a,bb+b)
            coarse=sum(ph(a,b) for a,b in cells.values());low=max(low,(exact-coarse)/len(f)**2);high=max(high,(coarse-exact-delta)/len(f)**2);cellcount=max(cellcount,len(cells));assert len(cells)<=4*n-1
        cases+=1
    z=dict(cases=cases,lower_violation_bits=float(low),upper_violation_bits=float(high),maximum_observed_cells=cellcount,seed=141432,elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
    assert low<1e-10 and high<1e-10;Path('quantized.json').write_text(json.dumps(z,indent=2)+'\n');print('QUANTIZED PASS',json.dumps(z))
if __name__=='__main__':main()
