"""PROVED: exact replay of both all-N cell banks and coverage."""
import json
from fractions import Fraction as F
from moment_polytope import vertices
from cells import check
from padding import check_allN

def main():
    vs=vertices(True)
    for name in ('allN_cells.json','allN_optimized_cells.json'):
        records=json.load(open(name))
        assert len(records)==10 and F(records[0]['rlo'])==0 and F(records[-1]['rhi'])==1
        for rec in records:
            assert check(rec,vs)==F(rec['margin'])
            assert check_allN(rec,vs)==list(map(F,rec['all_N_margins']))
        assert all(F(x['rhi'])==F(y['rlo'])for x,y in zip(records,records[1:]))
        ceiling=min(F(c['ahi'])for c in records)
        print('PROVED:',name,len(records),'all-N cells, uniform ceiling',ceiling)
    assert min(F(c['ahi'])for c in records)==F(64,125)
if __name__=='__main__':main()
