"""Exact rational symbolic partition-state proof for K_{4,s} forest Rayleigh differences.

Polynomial dictionaries use exponent pairs (s degree, lambda degree).
No external symbolic dependency is required.
"""
from fractions import Fraction
from itertools import combinations
import json


def clean(p): return {k:v for k,v in p.items() if v}
def const(v): return {(0,0):Fraction(v)} if v else {}
def mono(i,j,v=1): return {(i,j):Fraction(v)} if v else {}
def add(*args):
    ans={}
    for p in args:
        for k,v in p.items(): ans[k]=ans.get(k,0)+v
    return clean(ans)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
    ans={}
    for (i,j),a in p.items():
        for (k,l),b in q.items(): ans[i+k,j+l]=ans.get((i+k,j+l),0)+a*b
    return clean(ans)
def power(p,n):
    ans=const(1)
    for _ in range(n): ans=mul(ans,p)
    return ans
def binomial_shift(delta,k):
    ans=const(1)
    for j in range(k): ans=scale(mul(ans,add(mono(1,0),const(-delta-j))),Fraction(1,j+1))
    return ans
def shift_s(p,base):
    ans={}
    for (i,j),v in p.items():
        for k in range(i+1):
            from math import comb
            ans=add(ans,mono(k,j,v*comb(i,k)*base**(i-k)))
    return ans
def fmt(p):
    return ' + '.join(f'{v}*s^{i}*x^{j}' for (i,j),v in sorted(p.items())) or '0'


def partitions(n):
    def go(p):
        if len(p)==n: yield tuple(p); return
        for x in range(max(p,default=-1)+2): yield from go(p+[x])
    yield from go([])


P=list(partitions(4)); index={p:i for i,p in enumerate(P)}; size=len(P)
def canonical(p):
    names={}; out=[]
    for a in p:
        if a not in names:names[a]=len(names)
        out.append(names[a])
    return tuple(out)
def star(required=()):
    M=[[{} for _ in P] for _ in P]
    for i,p in enumerate(P):
        for mask in range(16):
            S=[v for v in range(4) if mask>>v&1]
            if any(v not in S for v in required):continue
            blocks=[p[v] for v in S]
            if len(set(blocks))<len(blocks):continue
            q=canonical([min(blocks) if a in blocks else a for a in p]) if blocks else p
            M[i][index[q]]=add(M[i][index[q]],mono(0,len(S)-len(required)))
    return M
def matmul(A,B):
    return [[add(*(mul(A[i][k],B[k][j]) for k in range(size))) for j in range(size)] for i in range(size)]
def ident():return [[const(i==j) for j in range(size)] for i in range(size)]
def summands(M):return add(*M[index[(0,1,2,3)]])


T=star(); a=add(const(1),mono(0,1,4)); N=[[add(T[i][j],scale(a,-1) if i==j else {}) for j in range(size)] for i in range(size)]
Np=[ident()]
for _ in range(4):Np.append(matmul(Np[-1],N))
assert not any(p for row in Np[4] for p in row)
I=ident(); U=star((0,)); V=star((1,)); W=star((0,1))
def core(delta,after):
    """a^(s-delta-3) times this equals start*T^(s-delta)*after*1."""
    out={}
    for k in range(4):
        out=add(out,mul(mul(binomial_shift(delta,k),power(a,3-k)),summands(matmul(Np[k],after))))
    return out


Z=core(0,I); E=core(1,U)
joint_samehub=core(1,W)
joint_sameleft=core(2,matmul(U,U))
joint_disjoint=core(2,matmul(U,V))
R={
    'same_hub':add(power(E,2),scale(mul(mul(a,Z),joint_samehub),-1)),
    'same_left':add(power(E,2),scale(mul(Z,joint_sameleft),-1)),
    'disjoint':add(power(E,2),scale(mul(Z,joint_disjoint),-1)),
}
if __name__=='__main__':
    for typ,p in R.items():
        base=1 if typ=='same_hub' else 2
        shifted=shift_s(p,base)
        neg=[(k,str(v)) for k,v in shifted.items() if v<0]
        print(typ,'core coefficients',len(p),'shift',base,'shifted coefficients',len(shifted),'negative',neg)
        print('Rcore=',fmt(p))
        print('shifted=',fmt(shifted))
    with open('/workspace/scratch/61b7096f9f41/forest_k4s_symbolic_coefficients.json','w') as f:
        json.dump({typ:[{'s':i,'lambda':j,'num':v.numerator,'den':v.denominator} for (i,j),v in sorted(p.items())] for typ,p in R.items()},f,indent=2)
