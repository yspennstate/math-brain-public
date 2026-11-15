"""PROVED: exact truncation of N=6 cells into all-N cells."""
import json
from fractions import Fraction as F
from moment_polytope import vertices
from padding import check_allN
recs=json.load(open('moment_cells.json'));vs=vertices(True);out=[]
for rec in recs:
    low,high=440,int(F(rec['ahi'])*1000)+1;best=None
    while low+1<high:
        mid=(low+high)//2;c=dict(rec,ahi=str(F(mid,1000)))
        try:ms=check_allN(c,vs)
        except AssertionError:high=mid
        else:low,best=mid,c;best['all_N_margins']=list(map(str,ms))
    assert best is not None
    from cells import check
    best['margin']=str(check(best,vs))
    out.append(best)
    print('PROVED: all N>=6 ratio',best['rlo'],best['rhi'],'scale',best['ahi'],flush=True)
    with open('allN_cells.json','w')as output:json.dump(out,output,indent=2)
