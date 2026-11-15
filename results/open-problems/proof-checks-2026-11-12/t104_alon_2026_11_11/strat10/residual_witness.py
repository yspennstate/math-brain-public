"""PROVED: exact witness of the remaining certificate gap, not a counterexample."""
import json,itertools
from fractions import Fraction as F
from cells import lower_value,vector_from_record
from face_intervals import source_chart
from rational_rays import frame_data

def verify(source):
    rr=F(source['r']);data=frame_data(source['U'],source['W'],rr);aa=data['a']
    assert rr>F(3,20) and aa>F(14,25) and data['lam']>aa and min(data['weights'])==0
    cells=json.load(open('moment_cells.json'))+json.load(open('allN_optimized_cells.json'))
    vals=[lower_value(data['moments'],aa,rr,vector_from_record(rec))for rec in cells if F(rec['rlo'])<=rr<=F(rec['rhi'])]
    assert vals and max(vals)<0
    boxes=[[(F(x),F(y))for x,y in rec['box']]for rec in json.load(open('face_boxes.json'))]
    pairs=list(itertools.combinations(range(5),2));charts=0
    for edge,weight in zip(pairs,data['weights']):
        if weight:continue
        for ordered in (edge,edge[::-1]):
            rest=[i for i in range(5)if i not in edge]
            for first in itertools.permutations(rest):
                coords,perm,_=source_chart(source,first+ordered)
                for sign in (1,-1):
                    signed=[v if sign==1 or j not in(2,4,5)else -v for j,v in enumerate(coords)]
                    assert all(any(v.hi<lo or hi<v.lo for v,(lo,hi)in zip(signed,box))for box in boxes)
                    charts+=1
    assert charts>0 and data['T']>0
    return dict(a=str(aa),T6=str(data['T']),largest_cell_lower_bound=str(max(vals)),excluded_charts=charts)

def main():
    source=json.load(open('residual_witness.json'));result=verify(source)
    assert result==source['verification']
    print('PROVED: exact connected zero-face endpoint outside all cell tests and all face boxes in every chart:',result)
if __name__=='__main__':main()
