import json,time,math
from fractions import Fraction as F
from pilot import ROOT,OLD
start=time.monotonic();rows=json.loads((OLD/'out/mixed_slices_m4.json').read_text())['records']
chars=[[(-1 if (s&x).bit_count()%2 else 1) for x in range(16)] for s in range(16)]
stats={}
for r in rows:
    W=[sum(a*b for a,b in zip(r['truth_h'],char)) for char in chars]
    z=sum(v*v for v in W);assert z==16*r['norm_integer']
    N=sum(t not in (0,z) and 2*t!=z for t in [sum(v*v for s,v in enumerate(W) if s>>i&1) for i in range(4)])
    assert N<=1
    stats.setdefault(r['norm_integer'],set()).add(N)
assert all(len(v)==1 for v in stats.values())
cover=json.loads((ROOT/'out/heavy_cover.json').read_text())
assert {r['mixed_mask'] for r in cover['groups']}=={r['mixed_mask'] for r in rows}-{0,65535}
assert len(cover['groups'])==690
for objective in cover['objective_signatures']:
    hs=[rows[i]['truth_h'].copy() for i in objective['row_indices']];M=objective['mixed_mask']
    if M:
        x=(M&-M).bit_length()-1
        if math.prod(h[x] for h in hs)==1:hs[0]=[-t for t in hs[0]]
    hs+= [[0]*16]*(4-len(hs))
    assert all(sum(h[x]*(-1 if (J&y).bit_count()%2 else 1) for J,h in enumerate(hs)) in (-2,2) for x in range(16) for y in range(4))
    masses=sorted([sum(v*v for v in h) for h in hs],reverse=True)
    assert masses==objective['masses']
    assert sum(rows[i]['norm_integer']*next(iter(stats[rows[i]['norm_integer']])) for i in objective['row_indices'])==objective['Q_numerator']
out={'status':'PASS','direct_character_sum_rows':len(rows),'mask_groups':690,'objective_representatives':len(cover['objective_signatures']),'norm_determines_N_on_this_catalogue':True,'seconds':time.monotonic()-start,'scope':'author alternate representation; not an independent external review'}
(ROOT/'out/verification.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
