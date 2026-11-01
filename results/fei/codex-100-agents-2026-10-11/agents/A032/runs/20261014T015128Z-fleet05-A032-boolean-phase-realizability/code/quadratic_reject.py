import json,time
from collections import Counter
from pilot import ROOT
start=time.monotonic();monomials=[0,1,2,4,8,3,5,9,6,10,12]
evaluation=[[int(s&m==m) for m in monomials] for s in range(16)]
chars=[[(-1 if (s&x).bit_count()%2 else 1) for s in range(16)] for x in range(16)]
certificates=[];types=Counter()
for phase in range(2048):
    W=[(8 if s&1 else 2)*(-1 if sum(v for j,v in enumerate(evaluation[s]) if phase>>j&1)%2 else 1) for s in range(16)]
    inverse=[sum(v*c for v,c in zip(W,char)) for char in chars]
    bad=next((x for x,t in enumerate(inverse) if t%16 or abs(t)>32),None)
    assert bad is not None
    reason='NONINTEGER_INVERSE' if inverse[bad]%16 else 'HEIGHT_EXCEEDS_TWO'
    types[reason]+=1;certificates.append({'phase_code':phase,'first_bad_physical_mask':bad,'inverse_numerator':inverse[bad],'denominator':16,'reason':reason})
assert time.monotonic()-start<60
out={'status':'ALL_QUADRATIC_PHASES_REJECTED','phase_basis_monomials':monomials,'Walsh_magnitudes':[8 if s&1 else 2 for s in range(16)],'phase_codes_checked':2048,'reason_counts':dict(types),'rejections':certificates,'seconds':time.monotonic()-start}
(ROOT/'out/quadratic_rejections.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='rejections'}))
