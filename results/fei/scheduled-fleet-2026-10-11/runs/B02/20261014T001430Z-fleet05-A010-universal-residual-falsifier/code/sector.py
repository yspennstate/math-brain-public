from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
import prime_poly as kernel
import json,time,sys
OUT=Path(__file__).resolve().parents[1]/'out'
def run(n):
    start=time.monotonic(); edges=[(1<<i)|(1<<j) for i,j in combinations(range(n),2)]; graphs=tables=cases=0
    for G in range(1,1<<len(edges)):
        supp=[m for i,m in enumerate(edges) if G>>i&1]; gates=[(m,0) for m in supp]; graphs+=1
        for flip in product([0,1],repeat=len(supp)):
            orders=[[j for j in range(n) if m>>j&1][::(-1 if f else 1)] for m,f in zip(supp,flip)]; tables+=1
            for A in range(1,1<<n):
                if any((m&A)==m for m in supp): continue
                js=[j for j in range(n) if A>>j&1]
                if any(not any(m>>j&1 for m in supp) for j in js): continue
                expected={(0,0):Q(1)}
                for j in js:
                    new={}
                    for l,m in enumerate(supp):
                        if not m>>j&1: continue
                        for (mask,d),c in expected.items():
                            assert not mask>>l&1
                            key=(mask|(1<<l),d+orders[l].index(j)); new[key]=new.get(key,Q(0))+c/4
                    expected=new
                actual=kernel.extract(A,gates,orders,n)
                assert actual==expected,(G,flip,A,actual,expected); cases+=1
                assert time.monotonic()-start<(60 if n==3 else 120)
        (OUT/'sector_checkpoint.json').write_text(json.dumps({'graphs':graphs,'tables':tables,'exact_polynomial_matches':cases}))
    result={'n':n,'graphs':graphs,'tables':tables,'exact_polynomial_matches':cases,'elapsed_seconds':time.monotonic()-start,'scope':'Formal identity for all weights, not sampled numerical weights'}
    (OUT/('sector_pilot.json' if n==3 else 'sector.json')).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=='__main__': run(3 if 'pilot' in sys.argv else 4)
