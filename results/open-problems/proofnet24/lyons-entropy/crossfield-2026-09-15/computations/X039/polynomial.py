from itertools import combinations
import sympy as s
import numpy as np
from scipy.optimize import linprog
import json
from pathlib import Path

u=s.symbols('u')
T=6
nodes=[0,1,2,3,4,T+u]
pairs=list(combinations(range(6),2)); triples=list(combinations(range(6),3))
quads=list(combinations(range(6),4))
edges=[]
for a in pairs:
    for j in combinations(sorted(set(range(6))-set(a)),2):
        b=tuple(sorted(set(range(6))-set(a)-set(j)));edges.append((a,j,b))
def vd(r):return s.prod(nodes[j]-nodes[i] for i,j in combinations(r,2))
v2={r:s.expand(vd(r)**2) for r in pairs+triples+quads}
ss={m:sum(nodes[i] for i in m) for m in triples}
G2=s.expand(sum(v2[r] for r in pairs));G4=s.expand(sum(v2[r] for r in quads));D=s.Poly(G2*G4,u)
a={r:s.Poly(v2[r]*G4,u) for r in pairs}
c={r:s.Poly(v2[tuple(sorted(set(range(6))-set(r)))]*G2,u) for r in pairs}
g={m:s.Poly(v2[m]*sum(v2[n]*(ss[m]-ss[n])**2 for n in triples),u) for m in triples}
rows=[('a',p) for p in pairs]+[('c',p) for p in pairs]+[('g',m) for m in triples]
A=s.zeros(len(rows),len(edges))
for k,(a0,j0,b0) in enumerate(edges):
    A[rows.index(('a',a0)),k]=1;A[rows.index(('c',b0)),k]=1
    for i in j0:A[rows.index(('g',tuple(sorted(a0+(i,))))),k]=1
_,ind=A.T.rref();Ar=A[list(ind),:]
print('T',T,'rank',len(ind),'degree',D.degree(),flush=True)
tables=[]
for k in range(D.degree()+1):
    denom=D.nth(k)
    rhs=s.Matrix([{'a':a,'c':c,'g':g}[kind][r].nth(k)/denom for kind,r in rows])
    scale=1/float(min(x for x in rhs if x>0))
    b=np.array(rhs[list(ind),:],dtype=float).ravel()*scale
    AA=np.array(Ar,dtype=float)
    res=linprog(np.arange(90,dtype=float)**2,A_eq=AA,b_eq=b,bounds=[(0,None)]*90,method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    print('coefficient',k,'D',denom,'minrhs',min(rhs),'success',res.success,flush=True)
    if not res.success:continue
    active=[i for i,x in enumerate(res.x) if x>1e-10]
    sol=A[:,active].gauss_jordan_solve(rhs)[0]
    free=set().union(*[x.free_symbols for x in sol])
    print(' support',len(active),'free',free,'min',min(sol) if not free else 'free','exact',A[:,active]*sol==rhs,flush=True)
    if free:continue
    assert min(sol)>=0 and A[:,active]*sol==rhs
    table=s.zeros(90,1)
    for j,x in zip(active,sol):table[j]=x*denom
    tables.append(table)
print('completed',len(tables),flush=True)
if len(tables)==D.degree()+1:
    den=s.ilcm(*[x.q for z in tables for x in z])
    support=[i for i in range(90) if any(z[i] for z in tables)]
    print('coefficient denominator',den,'union support',len(support),flush=True)
    payload={'description':'Exact polynomial diamond certificate; discovery LP is not needed for verification.',
             'base':T,'nodes':['0','1','2','3','4','6+u'],
             'coefficient_denominator':int(den),
             'D_ascending':[str(D.nth(k)) for k in range(D.degree()+1)],
             'edges':[[list(a),list(j),list(b)] for a,j,b in edges],
             'coefficients_ascending':[[str(tables[k][i]) for k in range(len(tables))] for i in range(90)]}
    Path('certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
    Path('coefficient_table.md').write_text('\n'.join('| '+''.join(map(str,edges[i][0]))+' | '+''.join(map(str,edges[i][1]))+' | '+', '.join(str(tables[k][i]) for k in range(len(tables)))+' |' for i in support)+'\n')
