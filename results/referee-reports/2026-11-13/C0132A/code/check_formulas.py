"""Check the exit-time and hitting formulas by exact finite-chain linear algebra."""
from fractions import Fraction as F

def solve(A,b):
    A=[list(map(F,row))+[F(y)] for row,y in zip(A,b)]
    n=len(A)
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j])
        A[j],A[pivot]=A[pivot],A[j]
        s=A[j][j];A[j]=[v/s for v in A[j]]
        for i in range(n):
            if i!=j:
                s=A[i][j];A[i]=[a-s*b for a,b in zip(A[i],A[j])]
    return [row[-1] for row in A]

checks=0
for a in range(-5,1):
    for b in range(0,6):
        states=list(range(a,b+1));index={y:i for i,y in enumerate(states)}
        A=[[F(0)]*len(states) for _ in states]
        for y in states:
            i=index[y];A[i][i]=1
            for z in (y-1,y+1):
                if z in index:A[i][index[z]]-=F(1,2)
        h=solve(A,[1]*len(states))
        for y in states:
            assert h[index[y]]==(y-a+1)*(b+1-y);checks+=1
        A=[[F(0)]*len(states) for _ in states];rhs=[F(0)]*len(states)
        for y in states:
            i=index[y];A[i][i]=1
            if y==0:rhs[i]=1;continue
            for z in (y-1,y+1):
                if z in index:A[i][index[z]]-=F(1,2)
        q=solve(A,rhs)
        for y in states:
            formula=F(1) if y==0 else (F(b+1-y,b+1) if y>0 else F(y-a+1,1-a))
            assert q[index[y]]==formula;checks+=1
print(f'Exact rational finite-chain checks passed: {checks} exit-time and hitting-probability values.')
