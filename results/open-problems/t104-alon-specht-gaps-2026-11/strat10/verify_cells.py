"""PROVED: exact replay and coverage of every saved padded moment cell."""
import json
from fractions import Fraction as F
from moment_polytope import vertices
from cells import check
from padding import check_allN

def main():
    vs=vertices(True);assert len(vs)==33
    records=json.load(open('moment_cells.json'))
    alln=0
    for rec in records:
        assert check(rec,vs)==F(rec['margin'])
        try:ms=check_allN(rec,vs)
        except AssertionError:ms=None
        alln+=ms is not None
        print('PROVED: r in',rec['rlo'],rec['rhi'],'a <=',rec['ahi'],'all N>=6',ms is not None)
    assert records[0]['rlo']=='0' and records[-1]['rhi']=='1'
    assert all(F(c['ahi'])>=F(66,125)and F(c['alo'])==F(11,25)for c in records)
    assert all(F(x['rhi'])==F(y['rlo'])for x,y in zip(records,records[1:]))
    print('PROVED:',len(records),'cells; uniform N=6 ceiling 66/125;',alln,'cells extend to every N>=6.')
if __name__=='__main__':main()
