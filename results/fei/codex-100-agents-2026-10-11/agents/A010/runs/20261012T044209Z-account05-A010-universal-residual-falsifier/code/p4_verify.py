from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import prod
import verify_continuum as check
import json,time
OUT=Path(__file__).resolve().parents[1]/'out'; TARGET=Q(32,25)

def decode(path):
    lo=[Q(0)]*3; hi=[Q(1)]*3
    for digit in path:
        axis=max(range(3),key=lambda j:hi[j]-lo[j]); mid=(lo[axis]+hi[axis])/2
        assert digit in '01'
        if digit=='0': hi[axis]=mid
        else: lo[axis]=mid
    return lo,hi

def leaf_bound(leaf,rec):
    lo,hi=decode(leaf['path'])
    if leaf['verdict']=='packing_excluded':
        assert any(sum(lo[l] for l,(m,v) in enumerate(rec['gates']) if m>>j&1)>1 for j in range(4)); return None
    maxima={int(A):Q(0) for A in rec['polynomials']}
    for lam in product(*[(x,y) for x,y in zip(lo,hi)]):
        T=prod(1+l/4 for l in lam)-1
        for A,terms in rec['polynomials'].items():
            val=max((4*Q(c)*check.ZUP**d for m,d,c in terms if m.bit_count()==1),default=Q(0)) if not T else sum(Q(c)*check.ZUP**d*prod(lam[j] for j in range(3) if m>>j&1) for m,d,c in terms)/T
            maxima[int(A)]=max(maxima[int(A)],val)
    if any(not v for v in maxima.values()): return None
    a=rec['walsh']; I=sum(A.bit_count()*v*v for A,v in enumerate(a))
    lower=-sum(Q(a[A]**2,I)*check.log_bounds(v)[1] for A,v in maxima.items())
    assert lower>=TARGET,(leaf['path'],float(lower)); return lower

if __name__=='__main__':
    import reference_v1 as ref
    import sys
    pilot='pilot' in sys.argv
    start=time.monotonic(); rows=json.loads((OUT/'p4_candidates.json').read_text())['rows']; matches=leaves=0; minimum=None
    if pilot: rows=rows[:1]
    for index,rec in enumerate(rows):
        rec['walsh']=ref.walsh(rec['truth'],4)
        for A,terms in rec['polynomials'].items():
            assert time.monotonic()-start<120
            assert check.queue_poly(int(A),rec)=={(m,d):Q(c) for m,d,c in terms}; matches+=1
        cert=json.loads((OUT/f'p4_continuum_{index:02}.json').read_text()); paths=sorted(leaf['path'] for leaf in cert['leaves'])
        assert cert['truth']==rec['truth'] and cert['orders']==rec['orders']
        assert len(set(paths))==len(paths) and sum(Q(1,1<<len(p)) for p in paths)==1
        assert all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
        for leaf in cert['leaves']:
            assert time.monotonic()-start<120
            lower=leaf_bound(leaf,rec); leaves+=1
            if lower is not None: minimum=lower if minimum is None else min(minimum,lower)
        check.log_bounds.cache_clear()
    result={'tables':len(rows),'exact_polynomial_matches':matches,'verified_leaves':leaves,'minimum_independent_lower':str(minimum),'minimum_independent_lower_float':float(minimum),'target':str(TARGET),'elapsed_seconds':time.monotonic()-start,'scope':'Distinct implementation within A010; independent-agent review pending'}
    (OUT/('p4_independent_pilot.json' if pilot else 'p4_independent_check.json')).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
