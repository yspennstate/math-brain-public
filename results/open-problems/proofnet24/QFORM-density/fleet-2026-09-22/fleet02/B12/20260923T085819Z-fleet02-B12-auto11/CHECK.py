import math
import numpy as np

# Exact rational baseline, arranged on triples H0=(0,1,2), H1=(3,4,5), H2=(6,7,8).
C1=np.array([[-2,2.5,0.5],[2.5,0,-1.5],[0.5,-1.5,2.0]],float)
C2=np.array([[-2,0.5,2.5],[0.5,2,-1.5],[2.5,-1.5,0.0]],float)
A0=np.zeros((9,9))
idx1=[0,3,6]; idx2=[1,4,7]
A0[np.ix_(idx1,idx1)]=C1
A0[np.ix_(idx2,idx2)]=C2
for i in [2,5,8]: A0[i,i]=4
v1=np.zeros(9); v1[idx1]=1/math.sqrt(3)
v2=np.zeros(9); v2[idx2]=1/math.sqrt(3)
H=[np.array([0,1,2]),np.array([3,4,5]),np.array([6,7,8])]

assert np.linalg.norm(A0@v1-v1)<1e-12
assert np.linalg.norm(A0@v2-v2)<1e-12
assert abs(v1@v2)<1e-12
expected=[np.diag([-2.,-2.,4.]),np.diag([0.,2.,4.]),np.diag([2.,0.,4.])]
for h,e in zip(H,expected): assert np.linalg.norm(A0[np.ix_(h,h)]-e)<1e-12

# Fixed spectrum away from the two update eigenvectors.
ev=np.linalg.eigvalsh(A0)
print('baseline eigenvalues', np.array2string(ev, precision=12))
print('density cap at delta=1/4', 8*math.sqrt(math.pi))

# Targeted deterministic Monte Carlo sanity check near all local resonances.
rng=np.random.default_rng(20260923)
min_max_core=1e99; min_s3=1e99; violations=0
for _ in range(10000):
    t1=rng.uniform(-7,7); t2=rng.uniform(-7,7)
    S=t1*np.outer(v1,v1)+t2*np.outer(v2,v2)
    G=rng.normal(size=(9,9)); T=(G+G.T)/2
    op=np.linalg.norm(T,2)
    if op: T*=0.25/op
    A=A0+S+T
    max_core=max(np.linalg.svd(A[np.ix_(h,h)],compute_uv=False)[-1] for h in H)
    s3=np.linalg.svd(A,compute_uv=False)[2]
    min_max_core=min(min_max_core,max_core)
    min_s3=min(min_s3,s3)
    if max_core < 0.75-1e-9 or s3 < 3.75-1e-9: violations+=1
print('tests',10000)
print('violations',violations)
print('minimum observed max physical-triple gap',min_max_core)
print('minimum observed s3',min_s3)
assert violations==0
