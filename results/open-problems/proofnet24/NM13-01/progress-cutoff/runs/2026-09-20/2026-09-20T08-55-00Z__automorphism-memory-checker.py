#!/usr/bin/env python3
from itertools import product, permutations
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import expm

# ------------------------------------------------------------
# A. Automorphism-memory semidirect lift toy
# Gamma=(F_2)^3, S=all nonzero vectors (base K_8, d=7).
# Hidden K=S_3 acts by permuting coordinates.
# Cross move uses the involution tau=(12); vertical hidden noise
# uses T={(12),(23)}, so the hidden cross permutation does NOT
# commute with the vertical walk.
# ------------------------------------------------------------

Gamma = list(product([0,1], repeat=3))
gidx = {g:i for i,g in enumerate(Gamma)}
eG=(0,0,0)
S=[g for g in Gamma if g != eG]
d=len(S)

K=list(permutations(range(3)))
kidx={p:i for i,p in enumerate(K)}
eK=(0,1,2)

def comp(p,q):
    # p o q
    return tuple(p[q[i]] for i in range(3))

def invp(p):
    r=[0]*3
    for i,j in enumerate(p):
        r[j]=i
    return tuple(r)

def act(p,x):
    pi=invp(p)
    return tuple(x[pi[j]] for j in range(3))

tau=(1,0,2)      # (12)
sigma=(0,2,1)    # (23)
T=[tau,sigma]
s=len(T)
D=d+s
a=Fraction(d,D)
b=Fraction(s,D)

assert comp(tau,tau)==eK
assert all(act(p,u) in S for p in K for u in S)

def add2(x,y):
    return tuple(i^j for i,j in zip(x,y))

states=[(g,k) for g in Gamma for k in K]
idx={z:i for i,z in enumerate(states)}
N=len(states)

def zmat(n,m):
    return [[Fraction(0) for _ in range(m)] for __ in range(n)]

P=zmat(len(Gamma),len(Gamma))
for g in Gamma:
    for u in S:
        P[gidx[g]][gidx[add2(g,u)]] += Fraction(1,d)

Rt=zmat(len(K),len(K))
for k in K:
    Rt[kidx[k]][kidx[comp(k,tau)]] = Fraction(1)

W=zmat(len(K),len(K))
for k in K:
    for t in T:
        W[kidx[k]][kidx[comp(k,t)]] += Fraction(1,s)

C=zmat(N,N)
V=zmat(N,N)
for g,k in states:
    i=idx[(g,k)]
    for u in S:
        # right multiplication by (u,tau):
        # (g,k)(u,tau)=(g rho(k)(u), k tau)
        h=add2(g,act(k,u))
        kp=comp(k,tau)
        C[i][idx[(h,kp)]] += Fraction(1,d)
    for t in T:
        V[i][idx[(g,comp(k,t))]] += Fraction(1,s)

# Exact cross identity C=P \otimes R_tau after relabeling the uniform
# base generator through rho(k).
KR=zmat(N,N)
for g in Gamma:
    for k in K:
        i=idx[(g,k)]
        for gp in Gamma:
            for kp in K:
                KR[i][idx[(gp,kp)]]=P[gidx[g]][gidx[gp]]*Rt[kidx[k]][kidx[kp]]
assert C==KR

# Hidden cross and hidden vertical walk genuinely do not commute.
def mm(A,B):
    n=len(A); p=len(B); m=len(B[0])
    out=zmat(n,m)
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                for j in range(m):
                    out[i][j]+=A[i][k]*B[k][j]
    return out

RW=mm(Rt,W); WR=mm(W,Rt)
comm_max=max(abs(RW[i][j]-WR[i][j]) for i in range(len(K)) for j in range(len(K)))
assert comm_max == Fraction(1,2)

Q=zmat(N,N)
for i in range(N):
    for j in range(N):
        Q[i][j]=a*C[i][j]+b*V[i][j]
assert all(sum(row)==1 for row in Q)

# Exact strong lumping of the original Gamma coordinate:
# projected discrete kernel = a P + b I.
for g,k in states:
    i=idx[(g,k)]
    probs=[sum(Q[i][idx[(gp,kp)]] for kp in K) for gp in Gamma]
    expect=[a*P[gidx[g]][gidx[gp]] + b*Fraction(int(gp==g),1) for gp in Gamma]
    assert probs==expect

# One-sided gaps and theorem lower bound (numerical spectral sanity).
Pf=np.array([[float(x) for x in row] for row in P])
Wf=np.array([[float(x) for x in row] for row in W])
Qf=np.array([[float(x) for x in row] for row in Q])
base_eigs=np.linalg.eigvalsh(Pf)
fiber_eigs=np.linalg.eigvalsh(Wf)
out_eigs=np.linalg.eigvalsh(Qf)
gapG=1-sorted(base_eigs)[-2]
gapF=1-sorted(fiber_eigs)[-2]
gapH=1-sorted(out_eigs)[-2]
bound=min(float(a)*gapG,float(b)*gapF)
assert gapH+1e-12 >= bound
assert abs(gapG-Fraction(8,7)) < 1e-12
assert abs(gapF-Fraction(1,2)) < 1e-12

# Compare with the obvious direct Cartesian product K8 square C6:
# its second eigenvalue is 8/9, unlike the skew lift.
direct_lam2=Fraction(8,9)
skew_lam2=1-gapH
assert abs(skew_lam2-float(direct_lam2)) > 1e-4

# Numerical source-continuous-time TV sandwich.
Lg=Pf-np.eye(len(Gamma))
Lh=Qf-np.eye(N)
p0g=np.zeros(len(Gamma)); p0g[gidx[eG]]=1
p0h=np.zeros(N); p0h[idx[(eG,eK)]]=1
ug=np.ones(len(Gamma))/len(Gamma)
uh=np.ones(N)/N

def tv(p,u):
    return 0.5*np.abs(p-u).sum()

CK=0.5*math.sqrt(len(K)-1)
rate=float(b)*gapF
spot=[]
for t in [0.5,1.0,2.0,4.0,8.0,16.0]:
    pg=p0g@expm(float(a)*t*Lg)
    ph=p0h@expm(t*Lh)
    dg=tv(pg,ug)
    dh=tv(ph,uh)
    err=CK*math.exp(-rate*t)
    assert dg <= dh + 1e-11
    assert dh <= dg + err + 1e-11
    spot.append((t,dg,dh,dg+err))

# ------------------------------------------------------------
# B. Exact gauge-triviality check for the preceding provisional
# semidirect strong-product toy:
# Gamma=C2 acts on Lambda=C3^2 by swapping coordinates and
# the fiber generator set is action-invariant. The moving-frame
# map (g,x)->(g,theta(g^{-1})x) conjugates it exactly to the
# ordinary strong product K2 boxtimes Cay(C3^2,T).
# ------------------------------------------------------------

Agrp=[0,1]
Lam=[(i,j) for i in range(3) for j in range(3)]
Tlam=[(1,0),(2,0),(0,1),(0,2)]
def add3(x,y):
    return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def theta(g,x):
    return x if g==0 else (x[1],x[0])
def smul(z,w):
    g,x=z; h,y=w
    return ((g+h)%2, add3(x,theta(g,y)))
Sigma=[(1,(0,0))]+[(0,t) for t in Tlam]+[(1,t) for t in Tlam]
oldstates=[(g,x) for g in Agrp for x in Lam]
oidx={z:i for i,z in enumerate(oldstates)}
Adj=np.zeros((18,18),dtype=int)
for z in oldstates:
    for sig in Sigma:
        Adj[oidx[z],oidx[smul(sig,z)]]+=1

# Gauge coordinates phi(g,x)=(g,theta(g,x)); g^{-1}=g in C2.
newstates=oldstates
nidx={z:i for i,z in enumerate(newstates)}
GAdj=np.zeros((18,18),dtype=int)
for z in oldstates:
    gz=(z[0],theta(z[0],z[1]))
    i=nidx[gz]
    for sig in Sigma:
        w=smul(sig,z)
        gw=(w[0],theta(w[0],w[1]))
        GAdj[i,nidx[gw]]+=1

# Direct strong product adjacency: base K2 (degree1), fiber 4-reg.
Strong=np.zeros((18,18),dtype=int)
for g,x in newstates:
    i=nidx[(g,x)]
    # base only
    Strong[i,nidx[(1-g,x)]]+=1
    # fiber only
    for t in Tlam:
        Strong[i,nidx[(g,add3(x,t))]]+=1
    # simultaneous
    for t in Tlam:
        Strong[i,nidx[(1-g,add3(x,t))]]+=1
assert np.array_equal(GAdj,Strong)

# ------------------------------------------------------------
# C. Explicit Kaufman-Lubotzky q=5 constants.
# Hidden K=C6, vertical generating set +/-1,+/-2 has one-sided gap 1.
# ------------------------------------------------------------

dKL=6; sKL=4; DKL=10
aKL=Fraction(3,5); bKL=Fraction(2,5)
center_base=Fraction(3,2)     # times log_5 n
center_out=center_base/aKL
assert center_out==Fraction(5,2)

# hidden normalized eigenvalues for Cay(C6,{+/-1,+/-2})
hidden_vals=[]
for j in range(6):
    val=(math.cos(math.pi*j/3)+math.cos(2*math.pi*j/3))/2
    hidden_vals.append(round(val,12))
lam2_hidden=sorted(hidden_vals)[-2]
assert abs(lam2_hidden-0.0)<1e-12
gap_hidden=1.0

gap_ram=1-math.sqrt(5)/3
gap_out_bound=min(float(aKL)*gap_ram,float(bKL)*gap_hidden)
assert abs(gap_out_bound-(3-math.sqrt(5))/5)<1e-12

print("AUTOMORPHISM_MEMORY_TOY_STATES=",N)
print("AUTOMORPHISM_MEMORY_TOY_DEGREE=",D)
print("EXACT_CROSS_IDENTITY=P_tensor_Rtau")
print("HIDDEN_CROSS_VERTICAL_COMMUTATOR_MAX=",comm_max)
print(f"TOY_GAPS base={gapG:.12f} hidden={gapF:.12f} output={gapH:.12f} theorem_lower={bound:.12f}")
print(f"TOY_SKEW_LAMBDA2={skew_lam2:.12f} DIRECT_CARTESIAN_LAMBDA2={float(direct_lam2):.12f}")
for t,dg,dh,up in spot:
    print(f"TV_SANDWICH t={t:g} lower={dg:.12f} actual={dh:.12f} upper={up:.12f}")
print("PREVIOUS_SEMIDIRECT_STRONG_PRODUCT_GAUGE_EQUALS_DIRECT_STRONG=True")
print("KL_Q5_OUTPUT_DEGREE=",DKL)
print("KL_Q5_BASE_SPEED=",aKL)
print("KL_Q5_HIDDEN_RATE=",bKL)
print("KL_Q5_CENTER_COEFF_LOG5_N=",center_out)
print(f"KL_Q5_GAP_LOWER={(3-math.sqrt(5))/5:.12f}")
print("KL_Q5_LRE_GROWTH_BASE=5 OUTPUT_TREE_BASE=9")
print("ALL_CHECKS_PASS")
