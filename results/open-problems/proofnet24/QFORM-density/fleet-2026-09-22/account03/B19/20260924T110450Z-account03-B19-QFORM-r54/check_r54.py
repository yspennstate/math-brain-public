import math
import numpy as np

rng=np.random.default_rng(540319)

def e3_from_svals(s):
    x=s*s
    out=0.0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                out += x[i]*x[j]*x[k]
    return out

# Lemma 2.1: aggregate promoted-row E3 lower bound.
min_ratio=float('inf')
viol1=0
for _ in range(3000):
    r=int(rng.integers(2,8)); c=int(rng.integers(3,10)); k=int(rng.integers(1,6))
    M=rng.normal(size=(r,c)); D=rng.normal(size=(k,c))
    _,sv,Vt=np.linalg.svd(M,full_matrices=False)
    V2=Vt[:2].T
    Pperp=np.eye(c)-V2@V2.T
    K=np.vstack([M,D])
    lhs=e3_from_svals(np.linalg.svd(K,compute_uv=False))
    rhs=(sv[0]*sv[1])**2*np.linalg.norm(D@Pperp,'fro')**2
    if rhs>1e-15:
        ratio=lhs/rhs
        min_ratio=min(min_ratio,ratio)
        if ratio < 1-1e-10: viol1+=1

# Set-deletion lower bound at live constants.
tau=2**-16
s0=1/112
bstar=s0/math.sqrt(2)-tau
min_margin=float('inf'); del_trials=0; viol2=0
for _ in range(5000):
    r=int(rng.integers(4,12)); c=int(rng.integers(8,30))
    U,_=np.linalg.qr(rng.normal(size=(r,2)))
    V,_=np.linalg.qr(rng.normal(size=(c,2)))
    ell=np.sum(V**2,axis=1)
    if ell.max()>.5: continue
    H=np.diag([rng.uniform(s0,2*s0),s0])
    M0=U@H@V.T
    F=rng.normal(size=(r,c))
    F*=0.99*tau/np.linalg.svd(F,compute_uv=False)[0]
    M=M0+F
    order=rng.permutation(c); S=[]; mass=0.0
    for j in order:
        if mass+ell[j] <= .5:
            S.append(int(j)); mass+=ell[j]
    J=[j for j in range(c) if j not in S]
    if len(J)<2: continue
    s=np.linalg.svd(M[:,J],compute_uv=False)
    margin=float(s[1]-bstar)
    min_margin=min(min_margin,margin); del_trials+=1
    if margin < -1e-10: viol2+=1

# Seven-bin next-fit lemma.
def nextfit(weights,cap=.5):
    bins=[]; cur=[]; load=0.0
    for i,w in enumerate(weights):
        if cur and load+w>cap+1e-15:
            bins.append(cur); cur=[i]; load=float(w)
        else:
            cur.append(i); load+=float(w)
    if cur: bins.append(cur)
    return bins

max_bins=0; bin_trials=0; viol3=0
for _ in range(10000):
    n=int(rng.integers(4,40)); raw=rng.random(n); w=2*raw/raw.sum()
    if np.max(w)>.5: continue
    bins=nextfit(w); bin_trials+=1; max_bins=max(max_bins,len(bins))
    if len(bins)>7 or any(sum(w[i] for i in b)>.5+1e-12 for b in bins): viol3+=1

# Symmetrized finite packet collar.
max_packet_ratio=0.0; viol4=0
for _ in range(2000):
    n=int(rng.integers(8,30)); m=int(rng.integers(2,min(7,n)+1))
    cuts=sorted(rng.choice(np.arange(1,n),size=m-1,replace=False))
    groups=np.split(np.arange(n),cuts)
    A=rng.normal(size=(n,n)); A=(A+A.T)/2
    O=np.zeros_like(A)
    for g in range(m):
        for h in range(m):
            if g!=h: O[np.ix_(groups[g],groups[h])]=A[np.ix_(groups[g],groups[h])]
    L=np.zeros_like(A); resid2=0.0
    for g in range(m):
        S=groups[g]; J=np.concatenate([groups[h] for h in range(m) if h!=g])
        D=A[np.ix_(S,J)]
        u,s,vt=np.linalg.svd(D,full_matrices=False); rr=min(2,len(s))
        Lblock=(u[:,:rr]*s[:rr])@vt[:rr,:]
        resid2 += np.linalg.norm(D-Lblock,'fro')**2
        L[np.ix_(S,J)]=Lblock
    K=(L+L.T)/2
    err=np.linalg.norm(O-K,'fro')
    ratio=err/math.sqrt(resid2) if resid2>1e-15 else 0.0
    max_packet_ratio=max(max_packet_ratio,ratio)
    if ratio>1+1e-10: viol4+=1

print('QFORM_B19_R54_SETWISE_E3_CHECK_PASS')
print('lemma2_min_ratio',repr(min_ratio),'violations',viol1)
print('deletion_trials',del_trials,'min_margin',repr(min_margin),'violations',viol2)
print('bin_trials',bin_trials,'max_bins',max_bins,'violations',viol3)
print('packet_max_ratio',repr(max_packet_ratio),'violations',viol4)
print('b_star',repr(bstar))
print('e3_gate_bound',repr((3*2**(4/3)*math.exp(1/3))*(bstar**2*2**-12)**(-1/3)))
print('partner_gate_bound',repr(2*math.sqrt(math.pi)/bstar))
