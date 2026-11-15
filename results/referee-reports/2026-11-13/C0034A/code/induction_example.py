"""Check the failed composition using only exact rational arithmetic."""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import defaultdict
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
Q=[[F(x,2) for x in row] for row in [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]]
def det(M):
    n=len(M)
    return sum(((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))*
               prod(M[i][p[i]] for i in range(n)) for p in permutations(range(n)))
def prod(xs):
    r=F(1)
    for x in xs: r*=x
    return r
def law(cols):
    return {B:det([[Q[i][j] for j in cols] for i in B])**2 for B in combinations(range(4),len(cols))}
def marginal(rows,idx):
    out=defaultdict(F)
    for row in rows: out[tuple(row[idx])]+=F(1,4)
    return dict(out)
def same(a,b):
    return all(a.get(k,0)==b.get(k,0) for k in a.keys()|b.keys())
# Columns are a,u,b,c. Rows give A, B, S, e, T, A+e, respectively.
rows=[[(0,),(1,),(0,1),(2,),(0,1,2),(0,2)],
      [(3,),(0,),(0,3),(1,),(0,1,3),(1,3)],
      [(1,),(2,),(1,2),(3,),(1,2,3),(1,3)],
      [(2,),(3,),(2,3),(0,),(0,2,3),(0,2)]]
assert all(sum(Q[i][j]*Q[i][k] for i in range(4))==int(j==k) for j in range(4) for k in range(4))
for row in rows:
    A,B,S,e,T,D=map(set,row)
    assert A.isdisjoint(B) and A|B==S and S.isdisjoint(e) and S|e==T and A|e==D
for idx,cols in [(0,[0]),(1,[2]),(2,[0,2]),(3,[1]),(4,[0,1,2])]:
    assert same(marginal(rows,idx),law(cols))
observed=marginal(rows,5); target=law([0,1])
assert not same(observed,target)
record={'meaning':'Failure of arbitrary composition, not a counterexample to C0034',
        'coordinate_convention':'0,1,2,3', 'Q':[[str(x) for x in row] for row in Q],
        'columns':'a,u,b,c', 'row_fields':['A','B','S','e','T','A_plus_e'],
        'rows':[{'sets':row,'mass':'1/4'} for row in rows],
        'observed':{','.join(map(str,k)):str(v) for k,v in observed.items()},
        'target':{','.join(map(str,k)):str(v) for k,v in target.items()}}
(ROOT/'data/induction_failure.json').write_text(json.dumps(record,indent=2)+'\n')
print('Exact composition check passed: all five stage marginals correct; composed marginal wrong.')
print('observed:',observed,'target:',target)
