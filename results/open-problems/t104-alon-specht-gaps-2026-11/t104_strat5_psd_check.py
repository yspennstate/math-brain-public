# Independent exact check (Fractions only, no sympy) that every exported 3x3
# coefficient matrix in the STRAT5 certificates is positive semidefinite
# (all principal minors >= 0), and that every monomial has degree 8.
import json, sys, itertools
from fractions import Fraction as F
def det(m):
    n=len(m)
    if n==1: return m[0][0]
    if n==2: return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def check(path):
    D=json.load(open(path)); bad=0; minmin=None; n=0
    for rec in D['records']:
        if 'matrix_times_1000' in rec: M=[[F(x,1000) for x in row] for row in rec['matrix_times_1000']]
        else: M=[[F(x,rec['denominator']) for x in row] for row in rec['matrix']]
        assert sum(rec['monomial'])==8 and all(M[i][j]==M[j][i] for i in range(3) for j in range(3))
        for k in (1,2,3):
            for I in itertools.combinations(range(3),k):
                v=det([[M[i][j] for j in I] for i in I]); n+=1
                if v<0: bad+=1
        # smallest leading-diagonal entry, as a sanity number
        d=min(M[i][i] for i in range(3)); minmin=d if minmin is None else min(minmin,d)
    print(path, 'param', D.get('c',D.get('r')), 'matrices', len(D['records']), 'minors', n, 'negative', bad, 'least diagonal', float(minmin))
    return bad
b=sum(check(p) for p in sys.argv[1:]); print('ALL PSD' if b==0 else 'FAILED')
