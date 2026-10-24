from collections import deque
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import random
import time

root=Path(__file__).resolve().parent
start=time.perf_counter()
receipt={'command':'python -X utf8 ~/brain_workers/w332/check_extended.py','checks':[]}
def record(name,count,detail):
    receipt['checks'].append({'name':name,'cases':count,'passed':True,'detail':detail})
    print(name,count,'PASS',flush=True)

for d in [3,4,5,6]:
    increments=[]
    for i in range(d):
        for sign in [-1,1]:
            increments.append([F(sign) if j==i else F(0) for j in range(d)])
    for i in range(d):
        assert sum(x[i] for x in increments)==0
        for j in range(d):
            assert sum(x[i]*x[j] for x in increments)/(2*d)==(F(1,d) if i==j else 0)
record('C0089 zero-intensity increment covariance',4,'All 2d nearest-neighbor increments; exact I_d/d covariance.')

times=list(range(-3,5))
vectors={}
for t in times:
    vectors[t]=[int(t<0 and i<-t) if i<3 else int(t>0 and i-3<t) for i in range(7)]
dot=lambda x,y:sum(a*b for a,b in zip(x,y))
for s,t in product(times,repeat=2):
    expected=min(abs(s),abs(t)) if s*t>0 else 0
    assert dot(vectors[s],vectors[t])==expected
diffs=[[b-a for a,b in zip(vectors[s],vectors[t])] for s,t in zip(times,times[1:])]
for i,j in product(range(7),repeat=2):
    assert dot(diffs[i],diffs[j])==int(i==j)
record('P0030 independent bridge and two-sided covariance',113,'64 path covariances and 49 disjoint increment covariances, with L=2.')
steps=4000
h=10/steps
integrand=lambda x:x*math.exp(-x*x/2)/math.sqrt(2*math.pi)
integral=h*(sum(integrand(i*h) for i in range(1,steps))+integrand(10)/2)
expected=1/math.sqrt(2*math.pi)
assert abs(integral-expected)<1e-6 and integral>0
record('P0030 future-selected splice has biased mean',1,f'Trapezoid integral {integral:.9f}; exact mean {expected:.9f}; error {abs(integral-expected):.3g}.')

net_count=0
for m in [2,4,8,16]:
    delta=F(1,m)
    net=[F(i,m) for i in range(m+1)]
    assert len(net)<=2/delta
    for t in [F(i,80) for i in range(-40,121)]:
        R=max(F(0),-t,t-1)
        if R<=delta:
            assert min(abs(t-x) for x in net)<=2*delta
        net_count+=1
assert F(2)/(2-1)==1+F(1)/(2-1)
record('P0234 net-distance implication and inverse-moment boundary',net_count+1,'Rational grids plus exact gamma=2,p=1 comparison distribution moment 2.')

def inverse2(M):
    a,b=M[0]
    c,d=M[1]
    determinant=a*d-b*c
    assert determinant>0
    return [[d/determinant,-b/determinant],[-c/determinant,a/determinant]]
def energy(M,f):
    return sum(F(f[i])*M[i][j]*f[j] for i,j in product(range(2),repeat=2))
G0=inverse2([[F(2),F(-1)],[F(-1),F(2)]])
cases=0
for a,b,c in product([F(1),F(2),F(3)],repeat=3):
    L=[[a+c,-c],[-c,b+c]]
    G=inverse2(L)
    factor=F(7,3)
    scaled=inverse2([[factor*x for x in row] for row in L])
    assert scaled==[[x/factor for x in row] for row in G]
    low,high=min(a,b,c),max(a,b,c)
    for f in product(range(-2,3),repeat=2):
        baseline=energy(G0,f)
        assert baseline/high<=energy(G,f)<=baseline/low
        cases+=1
record('C0010 exact conductance scaling and covariance comparison',cases,'27 two-vertex networks times 25 linear functionals, exact rational inverses.')
for k in range(1,9):
    partial=sum(F(1,j) for j in range(1,2**k+1))
    assert partial>=1+F(k,2)
record('C0010 vanishing scale errors can accumulate without bound',8,'Harmonic sums at N=2^k obey H_N>=1+k/2; e_j=1/j -> 0.')

rng=random.Random(332)
def integer_quad(A,x):
    return sum(A[i][i]*(x[i]*(x[i]-1)//2) for i in range(len(x)))+sum(A[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))
count=0
for d in [3,4,5]:
    for case in range(5):
        A=[[0]*d for _ in range(d)]
        for i in range(d):
            for j in range(i,d):
                A[i][j]=A[j][i]=rng.randrange(-4,5)
        trace=sum(A[i][i] for i in range(d))
        for x in product(range(-1,2),repeat=d):
            lap=0
            for i in range(d):
                plus=list(x);minus=list(x)
                plus[i]+=1;minus[i]-=1
                lap+=integer_quad(A,plus)+integer_quad(A,minus)-2*integer_quad(A,x)
            assert lap==trace
            count+=1
record('C0101 integer quadratic witnesses in dimensions 3-5',count,'15 symmetric integer matrices, full {-1,0,1}^d grids; exact trace Laplacians.')
ceil_fraction=lambda q:-((-q.numerator)//q.denominator)
a=F(1,2)
round_values=[ceil_fraction(a*x*x/2) for x in [-1,0,1]]
lap=round_values[0]+round_values[2]-2*round_values[1]
assert lap==2 and lap>a+1 and lap<a+2
record('C0101 stored ceil-curvature bound is false',1,'a=1/2,x=0 gives 2 > a+1=3/2.')

def labelled_ball(d,R,m=None):
    origin=(0,)*d
    distance={origin:0};queue=deque([origin])
    def neighbor(x,i,s):
        y=list(x);y[i]+=s
        if m is not None:y[i]%=m
        return tuple(y)
    while queue:
        x=queue.popleft()
        if distance[x]==R:continue
        for i,s in product(range(d),[-1,1]):
            y=neighbor(x,i,s)
            if y not in distance:
                distance[y]=distance[x]+1;queue.append(y)
    edges={(x,i,s,neighbor(x,i,s)) for x in distance for i,s in product(range(d),[-1,1]) if neighbor(x,i,s) in distance}
    return set(distance),edges
for d,R in product([1,2,3],[1,2,3]):
    m=2*R+2
    points,edges=labelled_ball(d,R)
    qpoints,qedges=labelled_ball(d,R,m)
    wrap=lambda x:tuple(v%m for v in x)
    assert len(points)==len(qpoints) and {wrap(x) for x in points}==qpoints
    assert {(wrap(x),i,s,wrap(y)) for x,i,s,y in edges}==qedges
for R in [1,2,3]:
    m=2*R+1
    _,edges=labelled_ball(1,R)
    _,qedges=labelled_ball(1,R,m)
    assert len(qedges)>len(edges)
record('C0148 finite-quotient balls and smallest-size boundary',12,'9 exact labelled torus/lattice balls and 3 cycle boundary counterchecks.')

intervals=0
for i in range(10):
    for j in range(i+1,11):
        a,b=F(i,10),F(j,10)
        found=False
        for n in range(1,9):
            denom=4**n
            k=ceil_fraction(a*denom)
            if a<=F(k,denom)<F(k+1,denom)<=b:
                found=True;break
        assert found
        intervals+=1
q=math.log(4)/math.log(3)
assert q>1 and abs(4*(1/3)**q-1)<1e-14
record('P0022 base-four subarc inclusion and Koch scaling',intervals+1,f'55 rational parameter intervals; q={q:.12f}; does not model Brownian paths.')
receipt['elapsed_seconds']=time.perf_counter()-start
(root/'measurements_extended.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
