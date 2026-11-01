import json,itertools,time
from pathlib import Path
from collections import Counter
from pure_product import fwht
ROOT=Path(__file__).resolve().parents[1]

def product_ok(W,m):
    C=[a*a for a in W];Z=sum(C)
    if Z==0:return False
    marg=[sum(v for s,v in enumerate(C) if s>>j&1) for j in range(m)]
    return all(c*Z**(m-1)==__import__('math').prod(marg[j] if s>>j&1 else Z-marg[j] for j in range(m)) for s,c in enumerate(C))

def direct_transform(truth):
    return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(truth)) for s in range(len(truth))]

def check():
    started=time.monotonic();data=json.loads((ROOT/'out'/'mixed_slices_m4.json').read_text())
    assert data['status']=='COMPLETE'
    keys=set()
    for row in data['records']:
        truth=row['truth_h'];W=direct_transform(truth)
        assert product_ok(W,4)
        assert tuple(sorted(Counter(v*v for v in W if v).items()))==tuple(map(tuple,row['histogram']))
        assert sum(s.bit_count()*v*v for s,v in enumerate(W))==row['influence_numerator']
        assert sum(v*v for v in truth)==row['norm_integer']
        assert all(v in(-2,-1,0,1,2) for v in truth)
        keys.add(tuple(truth))
    catalogue_seconds=time.monotonic()-started
    pilot_start=time.monotonic();product_slices=nonzero=0
    for i,truth in enumerate(itertools.product((-2,-1,0,1,2),repeat=8)):
        if not any(truth):continue
        nonzero+=1;W=fwht(truth)
        if not product_ok(W,3):continue
        product_slices+=1
        canon=truth if next(v for v in truth if v)>0 else tuple(-v for v in truth)
        lifted=canon+canon
        assert lifted in keys,('missing lifted three-bit product slice',truth)
        if i%1000==0 and time.monotonic()-pilot_start>60:raise RuntimeError('PILOT_RUNTIME_LIMIT')
    result={'status':'PASS','direct_catalogue_rows':len(keys),'catalogue_seconds':catalogue_seconds,'pilot_all_vectors':390625,'pilot_nonzero':nonzero,'pilot_product_slices_including_global_signs':product_slices,'pilot_seconds':time.monotonic()-pilot_start,'independent_review':'author different transform representation; external review pending'}
    (ROOT/'out'/'slice_direct_verification.json').write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
if __name__=='__main__':check()
