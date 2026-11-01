from fractions import Fraction
from itertools import product

V = [
    (1,1,0,0),
    (1,0,1,0),
    (0,1,1,0),
    (1,1,1,0),
    (1,0,0,1),
    (0,1,0,1),
    (1,1,0,1),
    (0,0,1,1),
    (1,0,1,1),
    (0,1,1,1),
]

def rank_cols(cols):
    if not cols:
        return 0
    m=len(cols[0]); n=len(cols)
    A=[[Fraction(cols[j][i]) for j in range(n)] for i in range(m)]
    row=0
    for col in range(n):
        pivot=next((i for i in range(row,m) if A[i][col]),None)
        if pivot is None: continue
        A[row],A[pivot]=A[pivot],A[row]
        p=A[row][col]
        A[row]=[x/p for x in A[row]]
        for i in range(m):
            if i!=row and A[i][col]:
                f=A[i][col]
                A[i]=[A[i][j]-f*A[row][j] for j in range(n)]
        row+=1
        if row==m: break
    return row

def dissociated(indices):
    sums={(0,0,0,0)}
    for i in indices:
        shifted={tuple(a+b for a,b in zip(s,V[i])) for s in sums}
        if sums & shifted:
            return False
        sums |= shifted
    return True

def neg_width(S,t):
    best=None
    for coeff in product((-1,0,1), repeat=len(S)):
        if not any(coeff): continue
        vec=tuple(sum(c*V[i][d] for c,i in zip(coeff,S)) for d in range(4))
        if vec==V[t]:
            w=sum(c==-1 for c in coeff)
            if best is None or w<best: best=w
    assert best is not None
    return best

assert rank_cols(V)==4
maximal=[]
for mask in range(1<<len(V)):
    S=[i for i in range(len(V)) if (mask>>i)&1]
    if not dissociated(S): continue
    if all((mask>>j)&1 or not dissociated(S+[j]) for j in range(len(V))):
        omitted=[j for j in range(len(V)) if not((mask>>j)&1)]
        widths={j:neg_width(S,j) for j in omitted}
        maximal.append((tuple(S),widths,sum(widths.values())))

assert len(maximal)==150
minimum=min(e for _,_,e in maximal)
assert minimum==5
witness=next(item for item in maximal if item[2]==minimum)
print('RANK',4)
print('MAXIMAL_DISSOCIATED_SETS',len(maximal))
print('MIN_TOTAL_NEGATIVE_WIDTH',minimum)
print('MINIMIZER',witness)
print('ALL_CHECKS_PASSED')
