from pathlib import Path
from math import sqrt,log,comb
from fractions import Fraction
import json,time
import numpy as np
from scipy.ndimage import minimum_filter1d
from check_first_passage import fp

ROOT=Path(__file__).resolve().parent
def occurrences(bits,n,h):
    s=np.concatenate([np.zeros((bits.shape[0],1),dtype=np.int32),np.cumsum(bits,axis=1,dtype=np.int32)],axis=1)
    minimum=minimum_filter1d(s,size=n,origin=(n-1)//2,axis=1,mode='constant',cval=2**30)
    ends=s[:,n:2*n]; starts=s[:,:n]
    return (ends-starts==-h)&(minimum[:,n-1:2*n-1]>ends)

def main():
    rng=np.random.default_rng(810012); start=time.monotonic()
    # Independently verify filter alignment, strictness and increment coding.
    for n in range(1,9):
        for h in range(1,n+1):
            if (n-h)%2: continue
            bits=rng.integers(0,2,size=(100,2*n-1),dtype=np.int8)*2-1
            got=occurrences(bits,n,h)
            for r,row in enumerate(bits):
                word=''.join('1' if x==1 else '0' for x in row)
                assert list(got[r])==[fp(word[i:i+n],h) for i in range(n)]
    rows=[]
    for n in [64,128,256,512,1024,2048,4096]:
        h=round(sqrt(n)); h+=(n-h)%2
        samples=16384; successes=total=total_sq=0
        for _ in range(samples//256):
            bits=rng.integers(0,2,size=(256,2*n-1),dtype=np.int8)*2-1
            count=occurrences(bits,n,h).sum(axis=1)
            successes+=int((count>0).sum()); total+=int(count.sum()); total_sq+=int((count*count).sum())
        q=successes/samples
        p=float(Fraction(h*comb(n,(n-h)//2),n*2**n))
        rows.append({'n':n,'h':h,'samples':samples,'q_hat':q,
                     'q_standard_error':sqrt(q*(1-q)/samples),'q_times_log_n':q*log(n),
                     'mean_N_hat':total/samples,'mean_N_exact':n*p,'mean_N2_hat':total_sq/samples,
                     'elapsed_seconds':time.monotonic()-start})
        ROOT.joinpath('first_passage_q_simulation.json').write_text(json.dumps({'seed':810012,'rows':rows},indent=2),encoding='utf-8')
        print(json.dumps(rows[-1]),flush=True)

if __name__=='__main__':main()
