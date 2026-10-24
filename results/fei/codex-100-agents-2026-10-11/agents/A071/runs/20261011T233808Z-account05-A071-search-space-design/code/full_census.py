import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from sparse_search import g, PREC, exact_min, encode, SCALE

ROOT=Path(__file__).resolve().parents[1]
SHIFT=PREC-40; FAST_SCALE=1<<40
LOW=np.array([0x55555555,0x33333333,0x0f0f0f0f,0x00ff00ff,0x0000ffff],dtype=np.uint32)

def translate(m,a):
    for i in range(5):
        if a>>i&1:
            d=1<<i; low=LOW[i]
            m=((m>>d)&low)|((m&low)<<d)
    return m

def run(pilot):
    start=time.perf_counter();stop=1<<20 if pilot else 1<<32;cap=55 if pilot else 1200
    chunk=131072;expected_raw=stop//2;counts={'raw':0,'minority_le_16':0,'sorted_influence':0,'translation_minimal':0,'entropy_evaluated':0,'strict_upper_passes':0,'candidates':0}
    seed=json.loads((ROOT/'out/search.json').read_text())['global_best']
    seedlo=int(seed['lo'])//(seed['L']*(1<<SHIFT))
    gl=np.empty((17,17),dtype=np.int64);gh=np.empty_like(gl)
    for a in range(17):
        for b in range(17):
            l,h=g(a*a,b*b);gl[a,b]=l>>SHIFT;gh[a,b]=(h+(1<<SHIFT)-1)>>SHIFT
    indices=np.arange(32,dtype=np.uint32)
    candidates=[];enumhash=hashlib.sha256()
    checkpoint_path=ROOT/'out'/('full_pilot_checkpoint.json' if pilot else 'full_checkpoint.json')
    for first in range(1,stop,2*chunk):
        if time.perf_counter()-start>cap:raise RuntimeError('Frozen runtime cap reached; checkpoint retained')
        m=np.arange(first,min(first+2*chunk,stop),2,dtype=np.uint64).astype(np.uint32)
        counts['raw']+=len(m)
        m=m[np.bitwise_count(m)<=16];counts['minority_le_16']+=len(m)
        prev=np.bitwise_count((m^(m>>1))&LOW[0])
        for i in range(1,5):
            ei=np.bitwise_count((m^(m>>(1<<i)))&LOW[i]);ok=prev<=ei;m=m[ok];prev=ei[ok]
        counts['sorted_influence']+=len(m)
        for a in range(1,32):
            if not len(m):break
            t=translate(m,a)
            m=m[((t&1)==0)|(m<=t)]
        counts['translation_minimal']+=len(m)
        if len(m):
            enumhash.update(m.tobytes())
            # Full sign-valued physical table -> independent batched integer FWHT.
            w=(1-2*((m[:,None]>>indices)&1).astype(np.int16)).astype(np.int32)
            for h in (1,2,4,8,16):
                blocks=w.reshape(-1,32//(2*h),2,h)
                a=blocks[:,:,0,:].copy();b=blocks[:,:,1,:].copy()
                blocks[:,:,0,:]=a+b;blocks[:,:,1,:]=a-b
            assert np.all((w&1)==0)
            c=w//2;squares=c*c
            assert np.all(np.sum(squares,axis=1)==256)
            upper=np.full(len(m),np.iinfo(np.int64).max,dtype=np.int64)
            for i in range(5):
                left=np.array([s for s in range(32) if not s>>i&1]);right=left|(1<<i)
                a=np.abs(c[:,left]);b=np.abs(c[:,right]);num=np.sum(gh[a,b],axis=1);den=np.sum(squares[:,right],axis=1).astype(np.int64)
                physical_edges=np.bitwise_count((m^(m>>(1<<i)))&LOW[i]).astype(np.int64)
                assert np.all(den==16*physical_edges)
                rel=den!=0;u=np.full(len(m),np.iinfo(np.int64).max,dtype=np.int64);u[rel]=(num[rel]+den[rel]-1)//den[rel]
                upper=np.minimum(upper,u)
            counts['entropy_evaluated']+=len(m)
            survivors=m[upper>seedlo];counts['strict_upper_passes']+=len(m)-len(survivors)
            candidates.extend(int(x) for x in survivors);counts['candidates']=len(candidates)
            if len(candidates)>100000:raise RuntimeError('Frozen 100000-candidate artifact cap reached')
        if counts['raw']%(chunk*128)==0:
            checkpoint={'counts':counts,'last_mask':first,'runtime_seconds':time.perf_counter()-start,'candidate_masks':candidates,'enumeration_sha256':enumhash.hexdigest(),'complete':False}
            checkpoint_path.write_text(json.dumps(checkpoint,indent=2),encoding='utf-8')
        # Save candidates the moment any new one is found.
        if len(m) and len(survivors):
            (ROOT/'out'/('full_pilot_candidates.json' if pilot else 'full_candidates.json')).write_text(json.dumps(candidates),encoding='utf-8')
    assert counts['raw']==expected_raw
    if not pilot:assert counts['minority_le_16']==1<<30
    result={'mode':'pilot' if pilot else 'full','counts':counts,'raw_expected':expected_raw,'mask_stop':stop,'seed_lower_scaled':seedlo,'entropy_scale':FAST_SCALE,'candidate_masks':candidates,'enumeration_sha256':enumhash.hexdigest(),'runtime_seconds':time.perf_counter()-start,'complete':True,'remaining_obligation':'Certify all survivors against seed using exact prime-log forms; equalities cannot be resolved by a floating tolerance'}
    (ROOT/'out'/('full_pilot.json' if pilot else 'full_census.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='candidate_masks'},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');run(ap.parse_args().pilot)
