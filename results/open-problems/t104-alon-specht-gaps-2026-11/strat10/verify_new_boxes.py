"""PROVED: replay all new rational face boxes and residual witnesses."""
import json
from fractions import Fraction as F
from new_boxes import polynomials,source_chart,prove_box,verify
polys=polynomials();records=json.load(open('new_face_boxes.json'))
for rec in records:
    assert verify(rec['source'])==rec['old_residual_verification']
    coords,perm,data=source_chart(rec['source']);assert perm==rec['permutation']
    box=[tuple(map(F,p))for p in rec['box']]
    assert all(lo<=c.lo<=c.hi<=hi and lo<hi for (lo,hi),c in zip(box,coords))
    cert,_=prove_box(polys,box,True);assert cert==rec['certificate']and cert['all_N']and F(cert['lower'])>0
assert records
print('PROVED:',len(records),'new rational boxes positive for every N>=6; every exact witness satisfied inherited (11).')
