"""PROVED: exact interval-box discovery; export only replayed positive boxes."""
import json
from fractions import Fraction as F
from face_intervals import source_chart,evaluate
from cells import vector_from_record,lower_value
sources=json.load(open('source_rays.json'))['residual']
cells=json.load(open('moment_cells.json'))
records=[];uncovered=0;allN=0
for number,source in enumerate(sources):
    coords,perm,data=source_chart(source)
    assert data['T']>0 and data['lam']>data['a'] and min(data['weights'])==0
    rr=F(source['r']);aa=data['a']
    vals=[lower_value(data['moments'],aa,rr,vector_from_record(c))for c in cells if F(c['rlo'])<=rr<=F(c['rhi'])]
    missed=max(vals)<0
    uncovered+=missed
    centers=[(v.lo+v.hi)/2 for v in coords]
    accepted=None
    low,high=0,20001
    while low+1<high:
        mid=(low+high)//2;radius=F(mid,10**6)
        box=[(x-radius,x+radius)for x in centers]
        t,de,D,ps=evaluate(box)
        if min(t.lo,de.lo,D.lo,ps[0].lo)>0:
            accepted=dict(source=number,permutation=perm,box=[[str(lo),str(hi)]for lo,hi in box],radius=str(radius),
                lower_delta=str(de.lo),lower_D=str(D.lo),lower_coefficients=[str(v.lo)for v in ps],
                missed_by_cells=missed,all_N=min(v.lo for v in ps)>0)
            low=mid
        else:high=mid
    assert accepted is not None
    # If the largest N=6 box fails other coefficients, shrink for all-N coverage.
    if not accepted['all_N']:
        radius=F(accepted['radius'])
        for _ in range(12):
            radius/=2;box=[(x-radius,x+radius)for x in centers]
            t,de,D,ps=evaluate(box)
            if min(t.lo,de.lo,D.lo,*(p.lo for p in ps))>0:
                accepted.update(box=[[str(lo),str(hi)]for lo,hi in box],radius=str(radius),lower_delta=str(de.lo),lower_D=str(D.lo),lower_coefficients=[str(v.lo)for v in ps],all_N=True)
                break
    assert all(lo<=v.lo<=v.hi<=hi for (lo,hi),v in zip([(F(x),F(y))for x,y in accepted['box']],coords))
    records.append(accepted);allN+=accepted['all_N']
    print('PROVED: box',number,'radius',accepted['radius'],'all N>=6',accepted['all_N'],'missed by cells',missed,flush=True)
    with open('face_boxes.json','w')as out:json.dump(records,out,indent=2)
print('PROVED: boxes',len(records),'new beyond cells',uncovered,'all N>=6',allN)
