"""PROVED only after exact interval/Bernstein bounds pass; no numerical signs."""
import json
from pathlib import Path
from fractions import Fraction as F
from face_intervals import evaluate
from precise_charts import source_chart
from cover_face import polynomials,prove_box
from residual_witness import verify

def main():
    sources=[r['source']for r in json.load(open('exact_samples.json'))['records']]+[json.load(open('residual_witness.json'))]
    polys=polynomials();out=[]
    for i,source in enumerate(sources):
        proof=verify(source);coords,perm,data=source_chart(source);centers=[(c.lo+c.hi)/2 for c in coords]
        radius=F(1,20);record=None
        for step in range(32):
            box=[(x-radius,x+radius)for x in centers]
            if not all(lo<=c.lo<=c.hi<=hi for (lo,hi),c in zip(box,coords)):break
            rec,impact=prove_box(polys,box,True)
            if rec is not None and rec['all_N']:
                record=dict(source=source,old_residual_verification=proof,permutation=perm,box=[[str(a),str(b)]for a,b in box],certificate=rec,radius=str(radius));break
            radius/=2
        if record is None:
            print('OPEN: no all-N local box for source',i,flush=True);continue
        out.append(record)
        msg=f'PROVED: new all-N local box {i}, radius {radius}, exact (11) endpoint inside; replay verify_new_boxes.py.'
        print(msg,flush=True)
        Path('new_face_boxes.json').write_text(json.dumps(out,indent=2)+'\n')
        with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
    assert out
if __name__=='__main__':main()
