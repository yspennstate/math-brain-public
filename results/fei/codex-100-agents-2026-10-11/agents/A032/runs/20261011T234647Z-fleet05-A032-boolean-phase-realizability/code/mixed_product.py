import json,time,itertools,math
import numpy as np
from collections import Counter
from pathlib import Path
from pure_product import fwht
ROOT=Path(__file__).resolve().parents[1]

def templates():
    m=4;N=16;limitmax=4*N*N
    primitive=[(a,b,a*a+b*b) for a in range(1,33) for b in range(1,33) if math.gcd(a,b)==1 and a*a+b*b<=limitmax]
    def ratios(r,limit,prefix=(),factor=1):
        if len(prefix)==r:yield prefix,factor;return
        for a,b,q in primitive:
            if factor*q*2**(r-len(prefix)-1)<=limit:yield from ratios(r,limit,prefix+((a,b),),factor*q)
    for r in range(5):
        for active in itertools.combinations(range(4),r):
            outside=[i for i in range(4) if i not in active]
            for fixedbits in itertools.product((0,1),repeat=4-r):
                shift=sum(b<<i for b,i in zip(fixedbits,outside))
                labels=[shift^sum(((mask>>j)&1)<<i for j,i in enumerate(active)) for mask in range(1<<r)]
                for c in (1,2,4,8,16,32):
                    for pairs,factor in ratios(r,limitmax//(c*c)):
                        norm=c*c*factor
                        if norm%N:continue
                        mags=[c*math.prod(pairs[j][mask>>j&1] for j in range(r)) for mask in range(1<<r)]
                        if max(mags)>32:continue
                        if r<4 and any(v%2 for v in mags):continue
                        if r==4 and len({v%2 for v in mags})>1:continue
                        yield active,labels,mags,norm//N

def generate():
    started=time.monotonic();records={};phase_count=template_count=admitted=0
    phase_batches={}
    for r in range(5):
        fixed={0}|{1<<j for j in range(r)};free=[j for j in range(1<<r) if j not in fixed]
        batch=np.ones((1<<len(free),1<<r),dtype=np.int64)
        for j,pos in enumerate(free):batch[:,pos]=1-2*((np.arange(len(batch))>>j)&1)
        phase_batches[r]=batch
    def save(status):
        groups=Counter(r['mixed_mask'] for r in records.values())
        output={'status':status,'helper':'A032-mixed-product-v2','m':4,'templates':template_count,'gauge_phases':phase_count,'admitted_gauge_phases':admitted,'slice_records_mod_global_sign':len(records),'mixed_mask_groups':len(groups),'group_sizes':dict(groups),'records':list(records.values()),'seconds':time.monotonic()-started}
        (ROOT/'out'/'mixed_slices_m4.json').write_text(json.dumps(output,separators=(',',':')))
        return output
    for active,labels,mags,norm in templates():
        template_count+=1;r=len(active);fixed={0}|{1<<j for j in range(r)};free=[j for j in range(1<<r) if j not in fixed]
        batch=np.zeros((len(phase_batches[r]),16),dtype=np.int64)
        batch[:,labels]=phase_batches[r]*np.array(mags,dtype=np.int64)
        inverse=batch.copy();h=1
        while h<16:
            for i in range(0,16,2*h):
                u=inverse[:,i:i+h].copy();v=inverse[:,i+h:i+2*h].copy()
                inverse[:,i:i+h]=u+v;inverse[:,i+h:i+2*h]=u-v
            h*=2
        phase_count+=len(batch)
        keep=np.flatnonzero(np.all((inverse%16==0)&(np.abs(inverse)<=32),axis=1))
        for idx in keep:
            W=batch[idx].tolist();physical=inverse[idx].tolist()
            admitted+=1;truth=[v//16 for v in physical]
            assert sum(v*v for v in truth)==norm
            hist=tuple(sorted(Counter(a*a for a in W if a).items()))
            influence=sum(s.bit_count()*a*a for s,a in enumerate(W))
            for translate in range(1<<r):
                t=sum(((translate>>j)&1)<<i for j,i in enumerate(active))
                shifted=[truth[x^t] for x in range(16)]
                if next(v for v in shifted if v)<0:shifted=[-v for v in shifted]
                key=tuple(shifted)
                if key not in records:
                    odd=sum((abs(v)==1)<<x for x,v in enumerate(shifted))
                    even=sum((abs(v)==2)<<x for x,v in enumerate(shifted))
                    signs=sum((v<0)<<x for x,v in enumerate(shifted) if abs(v)==1)
                    records[key]={'truth_h':shifted,'mixed_mask':odd,'pure_mask':even,'mixed_negative_mask':signs,'norm_integer':norm,'histogram':hist,'influence_numerator':influence}
            if len(records)>100000:raise RuntimeError('FROZEN_CATALOGUE_COUNT_LIMIT')
        if template_count%100==0:save('IN_PROGRESS')
        if time.monotonic()-started>180:
            save('PARTIAL_RUNTIME_CAP');raise RuntimeError('FROZEN_RUNTIME_LIMIT')
    output=save('COMPLETE');groups=Counter(r['mixed_mask'] for r in records.values())
    print(json.dumps({k:v for k,v in output.items() if k not in('records','group_sizes')}));print(json.dumps({'group_size_histogram':dict(Counter(groups.values()))}),flush=True)
if __name__=='__main__':generate()
