"""Repair numerical boundary error by moving a tiny mass to the full set.

This increases every up(R); bisection imposes relative, not only absolute feasibility.
"""
import json
from pathlib import Path
import numpy as np
from common import tables,check,mv

def repair(mu,n):
    pc,z,L,fac,meta=tables(n); rr=np.array([r for r,k in meta])
    mu=np.asarray(mu)
    def test(eps):
        x=(1-eps)*mu.copy(); x[-1]+=eps
        up=mv(z,x); left=mv(L,x); right=fac*up[rr]**1.5
        rel=np.divide(left,right,out=np.zeros_like(left),where=right>0)
        return x,float(rel.max())
    x,rat=test(0.)
    if rat<=1-1e-11: return x,0.,rat
    hi=1e-12
    while test(hi)[1]>1-1e-11: hi*=2
    lo=0.
    for _ in range(60):
        mid=(lo+hi)/2
        if test(mid)[1]<=1-1e-11: hi=mid
        else: lo=mid
    x,rat=test(hi)
    return x,hi,rat

if __name__=='__main__':
    data=json.load(open('small_output.json'))
    out=[]
    for item in data['results']:
        n=item['n']; mu,eps,rat=repair(item['mu'],n)
        row={'n':n,'mix_to_full':eps,'max_C_left_right':rat,'mu':mu.tolist(),'quantities':check(mu,n),
             'scope':'best repaired local multistart result; not a global supremum certificate'}
        out.append(row)
        print(n,row['quantities']['A_I'],eps,rat)
    Path('small_repaired.json').write_text(json.dumps(out,indent=2)+'\n')
