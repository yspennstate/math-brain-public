"""PROVED: replay all final cell certificates and their combined coverage."""
import json
from fractions import Fraction as F
from moment_bounds import vertices,check
from directional_bounds import check as directional_check

base,enhanced=vertices(),vertices(enhanced=True)
assert len(base)==19 and len(enhanced)==33
assert set(enhanced)=={tuple(map(F,p))for p in json.load(open('enhanced_vertices.json'))}
records=[]
for filename,polytope in [('strong_moment_cells.json',base),('enhanced_moment_cells.json',enhanced)]:
    data=json.load(open(filename))
    for rec in data:
        margin=check(rec,polytope)
        assert isinstance(margin,F) and margin==F(rec['margin'])
    records+=data
    print('PROVED:',filename,len(data),'cells; every rational block and minimum verified.')
data=json.load(open('directional_moment_cells.json'))
for rec in data:
    assert directional_check(rec,enhanced)==F(rec['margin'])
records+=data
print('PROVED: directional_moment_cells.json',len(data),'cells; every rational block and minimum verified.')


def cap(r):
    ceilings=[F(c['ahi'])for c in records if F(c['rlo'])<=r<=F(c['rhi'])]
    assert ceilings
    return max(ceilings)


def interval_cap(lo,hi):
    cuts=sorted({lo,hi}|{F(c[k])for c in records for k in ('rlo','rhi')if lo<F(c[k])<hi})
    return min(cap(x)for x in cuts+[(a+b)/2 for a,b in zip(cuts,cuts[1:])])


uniform=interval_cap(F(3,25),F(1))
print('PROVED: combined uniform scale ceiling',uniform)
summary=[]
for lo,hi in [(F(3,25),F(1,5)),(F(1,5),F(2,5)),(F(2,5),F(3,5)),
              (F(3,5),F(4,5)),(F(4,5),F(9,10)),(F(9,10),F(19,20)),(F(19,20),F(1))]:
    ceiling=interval_cap(lo,hi)
    summary.append(dict(rlo=str(lo),rhi=str(hi),ceiling=str(ceiling)))
    print('PROVED: ratios',lo,'through',hi,'scale ceiling',ceiling)
with open('cell_coverage_summary.json','w')as out:
    json.dump(dict(uniform=str(uniform),intervals=summary),out,indent=2)
