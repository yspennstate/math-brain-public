"""Independent exact checks of the E0066 stored mathematical certificates."""
import os
for var in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[var]='1'
import itertools as it
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp


def tensor(rows,m):
    p={}
    for row,(i,j) in zip(rows,it.combinations_with_replacement(range(m),2)):
        for k,value in enumerate(row):p[i,j,k]=p[j,i,k]=F(int(value),2)
    return p


def step(p,x):
    m=len(x)
    return tuple(sum(p[i,j,k]*x[i]*x[j] for i,j in it.product(range(m),repeat=2))
                 for k in range(m))


def scalar_conditions(p,m):
    assert all(p[i,j,k]>=0 and p[i,j,k]==p[j,i,k]
               for i,j,k in it.product(range(m),repeat=3))
    assert all(sum(p[i,j,k] for k in range(m))==1
               for i,j in it.product(range(m),repeat=2))
    assert all(sum(p[i,j,k] for i,j in it.product(range(m),repeat=2))==m
               for k in range(m))
    for mask in range(1,1<<m):
        J=[i for i in range(m) if mask>>i&1]
        assert all(sum(p[i,j,k] for i,j in it.product(J,repeat=2))<=len(J)
                   for k in range(m))


def exact_active_rank(rows,m):
    p=tensor(rows,m)
    coords=[(i,j,k) for i,j in it.combinations_with_replacement(range(m),2)
            for k in range(m)]
    equations=[]
    for i,j in it.combinations_with_replacement(range(m),2):
        equations.append([int((a,b)==(i,j)) for a,b,k in coords])
    for k in range(m):
        equations.append([(1 if a==b else 2)*int(c==k) for a,b,c in coords])
        for mask in range(1,(1<<m)-1):
            J=[i for i in range(m) if mask>>i&1]
            if sum(p[i,j,k] for i,j in it.product(J,repeat=2))==len(J):
                equations.append([(1 if a==b else 2)*int(c==k and a in J and b in J)
                                  for a,b,c in coords])
    for index,c in enumerate(coords):
        if p[c]==0:equations.append([int(j==index) for j in range(len(coords))])
    return sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(equations)).rank()


findings={}
for record in json.loads(Path('data/exact_cycles.json').read_text()):
    m=record['m'];p=tensor(record['coefficients_twice'],m)
    scalar_conditions(p,m)
    x=tuple(map(F,record['x']));y=step(p,x)
    assert sum(x)==1 and min(x)>0 and y!=x and step(p,y)==x
    assert list(map(str,y))==record['Vx']
    rank=exact_active_rank(record['coefficients_twice'],m)
    assert rank==m*m*(m+1)//2
    # Direct coefficient reconstruction of the analytic formula, independently
    # of the permutation-generator routine in experiments.py.
    perm=[2,3,0,1]+list(range(4,m))
    expected={}
    for i,j in it.combinations_with_replacement(range(m),2):
        v=[F(0)]*m
        if (i,j) in ((0,0),(1,1)):v[1]=F(1)
        elif (i,j)==(0,1):v[0]=F(1)
        else:v[i]+=F(1,2);v[j]+=F(1,2)
        for k in range(m):expected[i,j,perm[k]]=expected[j,i,perm[k]]=v[k]
    assert p==expected
    findings[f'm{m}_cycle_and_extreme']=dict(period=2,exact_active_rank=int(rank))

# Algebraic variance identity, without substituting sampled initial points.
x=sp.symbols('x1:5');a,b,c,d=x
v=(c,d,a-a*a+a*b,b+a*a-a*b)
loss=sp.expand(sum(z*z for z in x)-sum(z*z for z in v))
assert sp.expand(loss-2*a*(1-a)*(a-b)**2)==0
# Independent return-map calculation in pair sums and pair differences.
s,t,h,k=sp.symbols('s t h k')
pair=( (s+h)/2,(s-h)/2,(t+k)/2,(t-k)/2 )
def V(z):
    a,b,c,d=z
    return (c,d,a-a*a+a*b,b+a*a-a*b)
ret=V(V(pair))
assert sp.expand(ret[0]+ret[1]-s)==0
assert sp.expand(ret[2]+ret[3]-t)==0
assert sp.expand(ret[0]-ret[1]-(1-s-h)*h)==0
assert sp.expand(ret[2]-ret[3]-(1-t-k)*k)==0
findings['return_map_transverse_multipliers']=['1-s','1-t']
findings['variance_identity']='2*x1*(1-x1)*(x1-x2)^2'

w=json.loads(Path('data/outer_polytope_witness.json').read_text())
p=tensor(w['coefficients_twice'],4);scalar_conditions(p,4)
xx=tuple(map(F,w['x']));yy=step(p,xx)
assert yy==tuple(map(F,w['Vx']))
assert sum(sorted(yy,reverse=True)[:2])-sum(sorted(xx,reverse=True)[:2])==F(7,400)
Ts=[(0,1,0,1),(1,0,0,1),(3,2,3,3),(3,2,2,2)]
assert all(p[i,j,k]==F(int(Ts[k][i]==j)+int(Ts[k][j]==i),2)
           for i,j,k in it.product(range(4),repeat=3))
findings['outer_polytope_control']='exact gap 7/400; four row-stochastic symmetrisations checked'

vertices=json.loads(Path('data/m3_vertices.json').read_text())
assert len(vertices['vertices'])==222
assert len(set(map(tuple,vertices['vertices'])))==222
for numerators in vertices['vertices']:
    rows=[numerators[i:i+3] for i in range(0,len(numerators),3)]
    scalar_conditions(tensor(rows,3),3)
    assert exact_active_rank(rows,3)==18
findings['m3_vertices']='222 distinct feasible tensors, each of exact rational active rank 18'

summary=json.loads(Path('data/summary.json').read_text())
details=json.loads(Path('data/trajectory_details.json').read_text())
assert sum(len(d['starts']) for d in details)==sum(r['starts'] for r in summary['tables'])==7705
assert len(details)==sum(r['operators'] for r in summary['tables'])==457
assert summary['peak_rss_bytes']<4*1024**3
followup=json.loads(Path('data/followup.json').read_text())
assert len(followup)==2 and all(r['numerical_tail_period'] in (1,2) for r in followup)
findings['numerics']=dict(trajectories=7705,operator_instances=457,
                         initially_unresolved=2,unresolved_after_extension=0)
Path('data/audit.json').write_text(json.dumps(findings,indent=2)+'\n')
print(json.dumps(findings,indent=2))
