import os,json,subprocess,struct,math,time,resource
import numpy as np
import mpmath as mp
from experiment import bits,masses,wht,analyse,phi
from experiment import zeta
from large import P
mp.mp.dps=90

def pair_file(name,p,q,n):
    scale=2**(2*n);p=np.rint(p*scale).astype(np.uint64);q=np.rint(q*scale).astype(np.uint64)
    with open(name,'wb') as f:f.write(struct.pack('i',(len(p)-1).bit_length()));f.write(p.tobytes());f.write(q.tobytes())
    return scale
def native(file,c,scale):return json.loads(subprocess.check_output(['./native',file,str(c),str(scale)],text=True))
def main():
    start=time.time();out={};n=16;x=bits(n);f=np.where(np.any([x[:,[(j+a)%n for a in [0,1,4]]].all(axis=1) for j in range(n)],axis=0),-1.,1.)
    p,q=masses(wht(f)**2,0);scale=pair_file('pair_scratch.bin',p,q,n);r=native('pair_scratch.bin',1,scale);delta=q.sum();py=analyse(f,n,[0]);out['native_precision']=dict(bytes=r['long_double_bytes'],mantissa_bits=r['long_double_mantissa_bits']);out['cyclic16']=dict(native_F=r['L']/delta,native_E=r['E']/delta,python_F=py['F'],residual=r['L']/delta-py['F'],E_residual=r['E']/delta-py['E'],order=r['order'])
    # Independent long-double DP for every edge along the all-core candidate path.
    spec=np.load('../FEIB16/pm_record_spectrum.npy');p,q=masses(spec**2,0);scale=pair_file('pair_scratch.bin',p,q,18)
    vals=[];F=0.;alpha=57/256;FM=mp.mpf(0);alphaM=mp.mpf(57)/256
    ap=zeta(np.rint(p*scale).astype(np.uint64));bq=zeta(np.rint(q*scale).astype(np.uint64))
    for depth in range(1,21):
        c=alpha**(depth-1);r=native('pair_scratch.bin',c,scale);inc=r['L']/(alpha*c);F+=inc
        cm=alphaM**(depth-1);v=P(mp.mpf(int(ap[0])),cm*cm*mp.mpf(int(bq[0])));R=0
        for j in r['order']:
            old=R;R|=1<<j;v+=P(mp.mpf(int(ap[R])-int(ap[old])),cm*cm*mp.mpf(int(bq[R])-int(bq[old])))
        FM+=v/(scale*alphaM*cm)
        vals.append(dict(depth=depth,increment=inc,F=F,chosen_order_F_90digit=str(FM),order=r['order']))
    pm=json.load(open('pm.json'))['data'];out['PM_all_core']=dict(rows=vals,python_min=pm['rows'][-1]['F'],native_candidate=F,residual=F-pm['rows'][-1]['F'],candidate_90digit=str(FM),mp_residual=float(FM)-pm['rows'][-1]['F'],note='Native DP independently optimizes every outside ordering on this path; Python DP separately optimizes over all coordinate type paths. Selected native orders are evaluated with exact dyadic inputs and 90-digit arithmetic; optimality comparisons remain binary64 on this platform.')
    os.remove('pair_scratch.bin');out.update(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('native_audit.json','w'),indent=2);print(json.dumps(out,indent=2))
if __name__=='__main__':main()
