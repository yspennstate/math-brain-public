"""Exact inactivity of inherited residual filters at the named eigenframe."""
import json,itertools,os,sys
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode=True
SOURCE=Path(__file__).resolve().parent/'STRAT10'
sys.path.insert(0,str(SOURCE))
from cells import lower_value,vector_from_record
from face_intervals import source_chart


def build():
    bank=json.loads((SOURCE/'moment_cells.json').read_text())+json.loads((SOURCE/'allN_optimized_cells.json').read_text())
    moments=(F(13,20),F(1,4),F(1,20))
    values=[]
    for i,c in enumerate(bank):
        if F(c['rlo'])<=1<=F(c['rhi']):
            value=lower_value(moments,F(1),F(1),vector_from_record(c))
            assert value<0
            if i<10:assert F(c['ahi'])<1
            values.append(dict(record=i,value=str(value),ahi=c['ahi']))
    boxes=[[(F(a),F(b)) for a,b in c['box']] for c in json.loads((SOURCE/'face_boxes.json').read_text())]
    U=[-4,1,1,1,1];W=[0,1,-1,-1,1]
    edges=[(i,j) for i in range(5) for j in range(i+1,5) if F(1,5)+F(U[i]*U[j],20)+F(W[i]*W[j],4)==0]
    assert len(edges)==8
    proofs=[]
    for edge in edges:
        for ordered in (edge,edge[::-1]):
            for rest in itertools.permutations([i for i in range(5) if i not in edge]):
                coords,perm,data=source_chart(dict(U=U,W=W,r='1'),rest+ordered)
                assert data['a']==data['lam']==1 and data['T']==0
                for sign in (-1,1):
                    signed=[v if sign==1 or j not in (2,4,5) else -v for j,v in enumerate(coords)]
                    separation=[]
                    for box in boxes:
                        choices=[j for j,(value,(lo,hi)) in enumerate(zip(signed,box)) if value.hi<lo or value.lo>hi]
                        assert choices
                        separation.append(choices[0])
                    proofs.append(dict(permutation=perm,sign=sign,separating_coordinates=separation))
    assert len(proofs)==192
    return dict(label='PROVED by verify_filters.py',moment_values=values,
                chart_count=192,box_count=len(boxes),chart_separations=proofs,
                conclusion='All inherited moment, scale ceiling and chart-exclusion filters are strictly inactive at P0; endpoint/actual connectivity and a<lambda are boundary conditions.')


if __name__=='__main__':
    data=build();Path('filter_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PROVED: inherited filters at P0, 192 chart choices.')
