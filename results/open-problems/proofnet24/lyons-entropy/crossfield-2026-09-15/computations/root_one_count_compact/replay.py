"""Replay every positive box and verify exact coverage of the analytic remainder.

The proof of the interval bounds is documented in the root completion report.
This checker reconstructs the subdivision without trusting stored counts.
"""
from fractions import Fraction
from pathlib import Path
import json
import certify as c

p=Path(__file__).with_name('certificate.json')
data=json.loads(p.read_text())
assert data['status']=='PASS' and int(data['scale'])==c.SCALE
initial=tuple(map(Fraction,data['initial_box']))
assert initial==(Fraction(2,3),Fraction(14),Fraction(1,5),Fraction(5))
leaves={tuple(map(Fraction,row['box'])):row for row in data['leaves']}
assert len(leaves)==len(data['leaves'])
used=set()
skipped=0
depth_max=0

def visit(box,depth=0):
    global skipped,depth_max
    assert depth<60, 'Missing positive leaf or bad subdivision'
    depth_max=max(depth_max,depth)
    rl,rh,sl,sh=box
    assert rl<rh and sl<sh
    if rh<sl or rl>2*sh+4:
        skipped+=1
        return
    if box in leaves:
        assert box not in used
        used.add(box)
        m11,m22,m12,det=c.matrix_box(*box)
        assert m11.lo>0 and det.lo>0
        assert str(m11.lo)==leaves[box]['m11_lower']
        assert str(det.lo)==leaves[box]['det_lower']
        return
    if rh-rl>=sh-sl:
        mid=(rl+rh)/2
        visit((rl,mid,sl,sh),depth+1)
        visit((mid,rh,sl,sh),depth+1)
    else:
        mid=(sl+sh)/2
        visit((rl,rh,sl,mid),depth+1)
        visit((rl,rh,mid,sh),depth+1)

visit(initial)
assert used==set(leaves)
out={'status':'PASS','positive_boxes_recomputed':len(used),
     'outside_boxes':skipped,'max_partition_depth':depth_max,
     'coverage':'Exact closed bisections cover every S<=R<=2*S+4 in the initial rectangle',
     'arithmetic':'Outward integer intervals; all transcendental bounds use rational series'}
Path(__file__).with_name('replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
