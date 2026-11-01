"""Exact finite witnesses for the T336 projection/perturbation argument.

Only Python's standard library is used. Finite tests are not a proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, comb
from pathlib import Path
import json
import random
import time

start = time.time()
rng = random.Random(2336)
counts = {}
worst_mean = Q(0)
worst_var = Q(0)

def record(name, n=1):
    counts[name] = counts.get(name, 0) + n

def transpose(A):
    return [list(row) for row in zip(*A)]

def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def sub(A,B):
    return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]

def identity(n):
    return [[Q(i==j) for j in range(n)] for i in range(n)]

def inverse(A):
    n=len(A)
    M=[list(row)+I for row,I in zip(A,identity(n))]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j])
        M[j],M[p]=M[p],M[j]
        v=M[j][j]
        M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i!=j and M[i][j]:
                v=M[i][j]
                M[i]=[x-v*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]

def rank(A):
    M=[list(row) for row in A]
    r=0
    for j in range(len(M[0])):
        piv=next((i for i in range(r,len(M)) if M[i][j]),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        v=M[r][j]
        M[r]=[x/v for x in M[r]]
        for i in range(r+1,len(M)):
            if M[i][j]:
                v=M[i][j]
                M[i]=[x-v*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M): break
    return r

def posterior(K,y,s):
    t=len(y)
    if not t: return Q(0),s+K[0][0]
    A=[[K[i][j]+(s if i==j else 0) for j in range(t)] for i in range(t)]
    Ainv=inverse(A)
    b=[[K[i][t]] for i in range(t)]
    bt=transpose(b)
    m=mm(mm(bt,Ainv),[[x] for x in y])[0][0]
    v=s+K[t][t]-mm(mm(bt,Ainv),b)[0][0]
    return m,v

# Empty/repeated contexts, zero labels, both kernel-error signs, varied noise,
# and singular unregularized Gram matrices.
for trial in range(150):
    t=trial%5
    d=1+trial%4
    s=[Q(1,7),Q(1),Q(5)][trial%3]
    B=Q(0 if trial%13==0 else 2)
    F=[[Q(rng.randint(-2,2),2*d) for _ in range(d)] for _ in range(t+1)]
    if t>=2 and trial%3==0: F[1]=list(F[0])
    Ft=[[F[i][j]+Q(rng.randint(-1,1),10*d) for j in range(d)] for i in range(t+1)]
    K,Kt=mm(F,transpose(F)),mm(Ft,transpose(Ft))
    S=Q(2)
    assert all(K[i][i]<=S*S and Kt[i][i]<=S*S for i in range(t+1))
    y=[B*Q(rng.randint(-2,2),2) for _ in range(t)]
    a=max(abs(K[i][j]-Kt[i][j]) for i in range(t+1) for j in range(t+1))
    m,v=posterior(K,y,s)
    mt,vt=posterior(Kt,y,s)
    H=1+t*S*S/s
    Cm=t*B*H/s
    Cv=H*H
    assert abs(m-mt)<=Cm*a
    assert abs(v-vt)<=Cv*a
    assert v>=s and vt>=s
    assert v<=s+S*S and vt<=s+S*S
    record('exact_posterior_inequalities',7)
    if Cm*a: worst_mean=max(worst_mean,abs(m-mt)/(Cm*a))
    if Cv*a: worst_var=max(worst_var,abs(v-vt)/(Cv*a))

# Brownian kernel min(x,y) is genuinely infinite rank. Its net includes 0,
# a zero section. Removing just that zero section is the Moore-Penrose
# projection, so only the strictly positive block needs inversion.
for grid_m in range(1,7):
    G=[Q(i,grid_m) for i in range(grid_m+1)]
    Gpos=G[1:]
    X=[Q(i,8*grid_m) for i in range(8*grid_m+1)]
    KG=[[min(x,y) for y in Gpos] for x in Gpos]
    C=[[min(x,y) for y in Gpos] for x in X]
    K=[[min(x,y) for y in X] for x in X]
    K0=mm(mm(C,inverse(KG)),transpose(C))
    E=sub(K,K0)
    h=Q(1,2*grid_m)
    assert rank(K0)<=len(G)
    record('brownian_rank')
    for i in range(len(X)):
        assert 0<=E[i][i]<=h
        assert E[i][i]<=Q(1,4*grid_m)
        record('brownian_diagonal',2)
        for j in range(len(X)):
            assert E[i][j]**2<=E[i][i]*E[j][j]
            assert abs(E[i][j])<=h
            record('brownian_offdiagonal',2)

# Multinomial identity and finite feature rank for RBF total-degree truncation.
for d in range(1,5):
    u=[Q(j+1,2*d+1) for j in range(d)]
    for degree in range(8):
        alphas=[a for a in product(range(degree+1),repeat=d) if sum(a)==degree]
        lhs=Q(0)
        for a in alphas:
            term=Q(1)
            for j in range(d): term*=u[j]**(2*a[j])/factorial(a[j])
            lhs+=term
        rhs=sum(x*x for x in u)**degree/factorial(degree)
        assert lhs==rhs
        assert len(alphas)==comb(d+degree-1,degree)
        record('rbf_multinomial',2)
    for r in range(1,8):
        assert sum(comb(d+j-1,j) for j in range(r))==comb(d+r-1,d)
        record('rbf_rank_count')

for r in range(1,16):
    for h in range(30):
        assert factorial(r+h)>=factorial(r)*factorial(h)
        record('factorial_tail_inequality')

for a,b in [(Q(-2),Q(3)),(Q(0),Q(0)),(Q(1,7),Q(8,7))]:
    for t in [Q(i,7) for i in range(-30,31)]:
        assert t+max(a-t,0)-max(t-b,0)==min(max(t,a),b)
        record('residual_clip')

out={
    'status':'PASS','seed':2336,
    'assertions_by_family':counts,
    'total_counted_assertions':sum(counts.values()),
    'mean_bound_max_ratio':str(worst_mean),
    'variance_bound_max_ratio':str(worst_var),
    'elapsed_seconds':time.time()-start,
    'limits':'Finite exact checks, not proof or independent theorem audit.'
}
Path(__file__).with_name('extension_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
