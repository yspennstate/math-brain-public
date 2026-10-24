from itertools import combinations
import sympy as s
import numpy as np
from scipy.optimize import linprog

n=6
pairs=list(combinations(range(n),2))
triples=list(combinations(range(n),3))
edges=[]
for a in pairs:
    for j in combinations(sorted(set(range(n))-set(a)),2):
        b=tuple(sorted(set(range(n))-set(a)-set(j)))
        edges.append((a,j,b))
nodes=[0,1,2,3,4,6]
v=[s.Matrix([x**k for x in nodes]) for k in range(6)]
for k in range(6):
    for z in v[:k]:
        v[k]-=z*(z.dot(v[k])/z.dot(z))
norm=[z.dot(z) for z in v]
V=s.Matrix.hstack(*v)
def minor(rows,cols): return V.extract(rows,cols).det()
def law(cols):
    return {r:s.factor(minor(r,cols)**2/s.prod(norm[c] for c in cols)) for r in combinations(range(n),len(cols))}
a,h,c=law([0,1]),law([2,3]),law([4,5])
g1,g2=law([0,1,2]),law([0,1,3])
g={m:g1[m]+g2[m] for m in triples}
rows=[('a',p) for p in pairs]+[('h',p) for p in pairs]+[('c',p) for p in pairs]+[('g',m) for m in triples]
A=s.zeros(len(rows),len(edges))
for k,(a0,j0,b0) in enumerate(edges):
    A[rows.index(('a',a0)),k]=1
    A[rows.index(('h',j0)),k]=1
    A[rows.index(('c',b0)),k]=1
    for i in j0: A[rows.index(('g',tuple(sorted(a0+(i,))))),k]=1
rhs=s.Matrix([{'a':a,'h':h,'c':c,'g':g}[kind][r] for kind,r in rows])
print('norms',norm,'minlaws',min(a.values()),min(h.values()),min(c.values()))
_,ind=A.T.rref()
AA=np.array(A.tolist(),dtype=float)
bb=np.array(rhs,dtype=float).ravel()
res=linprog(np.r_[np.zeros(90),-1.0],A_ub=np.c_[-np.eye(90),np.ones(90)],b_ub=np.zeros(90),A_eq=np.c_[AA,np.zeros(len(rows))],b_eq=bb,bounds=[(None,None)]*91,method='highs')
print('rank',len(ind),'LP',res.success,'min',res.x[-1] if res.success else res.message)
if res.success:
    print('min tight',[i for i,x in enumerate(res.x[:-1]) if abs(x-res.x[-1])<1e-9])
    np.save('explore.npy',res.x)
    tight=[i for i,x in enumerate(res.x[:-1]) if abs(x-res.x[-1])<1e-9]
    exactA=A.row_join(s.zeros(len(rows),1))
    exactb=rhs
    for i in tight:
        row=s.zeros(1,91);row[0,i]=1;row[0,90]=-1
        exactA=exactA.col_join(row);exactb=exactb.col_join(s.zeros(1,1))
    sol=exactA.gauss_jordan_solve(exactb)[0]
    print('free',set().union(*[x.free_symbols for x in sol]))
    print('exact min',sol[-1],min(sol[:-1]),'denominator',s.ilcm(*[x.q for x in sol]))
    print('values',list(sol))
