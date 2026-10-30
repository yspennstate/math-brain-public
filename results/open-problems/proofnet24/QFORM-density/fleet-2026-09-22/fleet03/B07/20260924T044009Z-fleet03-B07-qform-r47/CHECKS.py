import math, random
from fractions import Fraction
import numpy as np

random.seed(4707)
np.random.seed(4707)

def e2(x):
    x=np.asarray(x,dtype=float)
    return (x.sum()**2-(x*x).sum())/2.0

def e3(x):
    x=np.asarray(x,dtype=float)
    s1=x.sum(); s2=(x*x).sum(); s3=(x*x*x).sum()
    return (s1**3-3*s1*s2+2*s3)/6.0

eps=Fraction(1,2**12)
m=2**41
packet=Fraction(m)*eps**4
normalized=Fraction(m)*eps**2/Fraction(2)
assert packet==Fraction(1,128)
assert normalized==2**16
assert math.sqrt(2)*float(eps) < 2**-10
assert float(eps)*math.sqrt(2*m)==512.0

max_cross_rank=0
for mm in (2,5,10,25):
    n=mm+3; p=mm+1; q=mm+2
    A=np.zeros((n,n)); A[0,0]=1.0
    for k in range(1,mm+1):
        A[k,p]=A[p,k]=0.17
        A[k,q]=A[q,k]=0.17
    for _ in range(300):
        mask=np.random.random(n)<0.5
        L=np.where(mask)[0]; R=np.where(~mask)[0]
        max_cross_rank=max(max_cross_rank,np.linalg.matrix_rank(A[np.ix_(L,R)],tol=1e-10))
assert max_cross_rank<=2

def greedy_color(edges,D):
    used_by=[set() for _ in range(max(max(u,v) for u,v,_ in edges)+1)] if edges else []
    cols=[]
    for u,v,w in edges:
        used=used_by[u]|used_by[v]
        c=next(c for c in range(2*D-1) if c not in used)
        cols.append(c); used_by[u].add(c); used_by[v].add(c)
    return cols

min_color_ratio=10.0
for _ in range(250):
    D=16; N=60; deg=[0]*N; edges=[]
    pairs=[(i,j) for i in range(N) for j in range(i+1,N)]
    random.shuffle(pairs)
    for u,v in pairs:
        if deg[u]<D and deg[v]<D and random.random()<0.12:
            w=10**random.uniform(-5,3)
            edges.append((u,v,w)); deg[u]+=1; deg[v]+=1
    cols=greedy_color(edges,D)
    assert (not cols) or max(cols)<2*D-1
    for c in set(cols):
        seen=set()
        for (u,v,w),cc in zip(edges,cols):
            if cc==c:
                assert u not in seen and v not in seen
                seen.add(u); seen.add(v)
    total=sum(w for _,_,w in edges)
    if total:
        cw=[0.0]*(2*D-1)
        for (_,_,w),c in zip(edges,cols): cw[c]+=w
        ratio=max(cw)/(total/(2*D-1))
        min_color_ratio=min(min_color_ratio,ratio)
        assert ratio>=1-1e-12

max_comp_violation=0.0
for _ in range(400):
    nr=9; nh=12
    C=np.random.normal(size=(nr,nh))
    G=np.zeros((nh,6))
    for j in range(6):
        z=np.random.normal(size=2); z/=np.linalg.norm(z)
        G[2*j,j]=z[0]; G[2*j+1,j]=z[1]
    W=C@G
    ec=e3(np.linalg.svd(C,compute_uv=False)**2)
    ew=e3(np.linalg.svd(W,compute_uv=False)**2)
    max_comp_violation=max(max_comp_violation,ew-ec)
    assert ew<=ec+1e-8*max(1.0,ec)

fork_cases=0
max_r2_ratio=0.0
max_r1_ratio=0.0
Tmin=8192/31
for _ in range(30000):
    r=random.randint(1,24)
    x=np.exp(np.random.uniform(-14,5,size=r))
    x=x/x.sum()*(Tmin*(1+4*random.random()))
    E2=e2(x); E3=e3(x)
    if E3 < 1/64:
        fork_cases+=1
        xs=np.sort(x)[::-1]
        if E2>=4:
            dist=math.sqrt(xs[2:].sum()) if len(xs)>2 else 0.0
            bd=3*math.sqrt(max(E3,0.0)/E2)
            assert dist<=bd+1e-5
            assert dist<3/16+1e-5
            max_r2_ratio=max(max_r2_ratio,dist/(3/16))
        else:
            dist=math.sqrt(xs[1:].sum()) if len(xs)>1 else 0.0
            bd=math.sqrt(31)/32
            assert dist<bd+1e-5
            max_r1_ratio=max(max_r1_ratio,dist/bd)

C3=3*2**(4/3)*math.e**(1/3)
print('counterexample_packet =', packet)
print('counterexample_normalized_energy =', normalized)
print('counterexample_large_eigenvalues = +/-512; isolated = +1')
print('counterexample_pair_scale =', math.sqrt(2)/2**12)
print('max_sampled_physical_cross_rank =', max_cross_rank)
print('matching_trials = 250')
print('minimum_best_color_weight_ratio_to_R_over_31 =', min_color_ratio)
print('compression_trials = 400')
print('maximum_e3_compression_violation =', max_comp_violation)
print('low_rank_fork_cases =', fork_cases)
print('maximum_rank2_distance_ratio_to_3_over_16 =', max_r2_ratio)
print('maximum_rank1_distance_ratio_to_sqrt31_over_32 =', max_r1_ratio)
print('Z3_exit_density_constant =', 2*C3)
print('STATUS=PASS')
