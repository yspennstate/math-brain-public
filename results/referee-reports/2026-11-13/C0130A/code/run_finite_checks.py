"""Several independently constructed finite-volume Dirichlet checks."""
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
from finite_volume import direct_walk, backward_finite

cases=[('m2_p08',['4/5']*2),('m3_p07',['7/10']*3),
       ('m3_p09',['9/10']*3),('m4_p075',['3/4']*4)]
out=[]
for name,params in cases:
    value,n=direct_walk(params,5)
    approx,error=backward_finite(params,5,640,85)
    diff=abs(mp.mpf(str(sp.N(value,85)))-approx)
    assert diff <= error+mp.mpf('1e-80')
    record=dict(name=name,params=params,N=5,K=640,states=n,
                exact_rational=str(value),direct=mp.nstr(value.evalf(70),70),
                backward=mp.nstr(approx,70),error_bound=mp.nstr(error,12),
                difference=mp.nstr(diff,12))
    out.append(record)
    Path('data/finite_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(name,n,str(value)[:75],mp.nstr(diff,5),flush=True)
