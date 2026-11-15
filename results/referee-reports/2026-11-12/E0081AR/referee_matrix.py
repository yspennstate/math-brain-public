"""Independent fraction-free matching calculation for the last two table rows."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import json,resource

def solve(A):
    n=len(A); A=[r[:] + [1] for r in A];prev=1
    for k in range(n-1):
        if not A[k][k]:
            j=next(j for j in range(k+1,n) if A[j][k]);A[k],A[j]=A[j],A[k]
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n+1):
                num=pivot*A[i][j]-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    x=[Fraction(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(Fraction(A[i][-1])-sum(A[i][j]*x[j] for j in range(i+1,n)))/A[i][i]
    return x

rows=[]
for n,a,expected in ((11,3,'317290872798/8937933785'),(12,2,'17663784686/445122589')):
    words=[]
    for w in product((-1,1),repeat=n):
        h=[0]
        for v in w:h.append(h[-1]+v)
        if h[-1]==-a and min(h[:-1])>-a:words.append(w)
    # A = 2^n M; solution A x=1 implies E T =1 / sum(x).
    A=[[sum(2**(n-s) for s in range(n) if v[:n-s]==w[s:]) for w in words] for v in words]
    et=1/sum(solve(A))
    assert et==Fraction(expected)
    rows.append(dict(n=n,a=a,words=len(words),ET=str(et),decimal=float(et)))
result=dict(rows=rows,maxrss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('referee_results/matrix.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
