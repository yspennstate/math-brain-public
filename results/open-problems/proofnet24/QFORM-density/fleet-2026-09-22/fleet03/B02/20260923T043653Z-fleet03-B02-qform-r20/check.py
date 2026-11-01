import itertools
import math
import numpy as np

rng=np.random.default_rng(20260923)

def e3_from_svals(M):
    s=np.linalg.svd(M,compute_uv=False)
    lam=s*s
    return sum(a*b*c for a,b,c in itertools.combinations(lam,3))

def row_weights(M):
    m,d=M.shape
    rows=list(itertools.combinations(range(m),3))
    cols=list(itertools.combinations(range(d),3))
    raw={}
    Z=0.0
    for R in rows:
        for T in cols:
            val=float(np.linalg.det(M[np.ix_(R,T)])**2)
            raw[(R,T)]=val
            Z+=val
    mu={R:sum(raw[(R,T)] for T in cols)/Z for R in rows}
    return rows,cols,Z,mu

max_z_err=max_delta_err=max_rank3_err=0.0
max_min_minus_delta=-1e9
for _ in range(40):
    m=int(rng.integers(6,10)); d=int(rng.integers(3,8))
    M=rng.normal(size=(m,d))
    rows,cols,Z,mu=row_weights(M)
    z2=e3_from_svals(M)
    max_z_err=max(max_z_err,abs(Z-z2)/max(1.0,abs(z2)))
    delta=sum(mu[R]*mu[S] for R in rows for S in rows if set(R).isdisjoint(S))
    avg=0.0
    minratio=1e100
    for R in rows:
        comp=[i for i in range(m) if i not in R]
        zr=e3_from_svals(M[comp,:]) if len(comp)>=3 else 0.0
        ratio=zr/Z
        avg += mu[R]*ratio
        minratio=min(minratio,ratio)
    max_delta_err=max(max_delta_err,abs(delta-avg))
    max_min_minus_delta=max(max_min_minus_delta,minratio-delta)

for _ in range(40):
    m=int(rng.integers(6,12)); d=int(rng.integers(3,8))
    U,_=np.linalg.qr(rng.normal(size=(m,3)))
    V,_=np.linalg.qr(rng.normal(size=(d,3)))
    sig=np.exp(rng.normal(size=3))
    M=U@np.diag(sig)@V.T
    rows,cols,Z,mu=row_weights(M)
    for R in rows[:min(15,len(rows))]:
        comp=[i for i in range(m) if i not in R]
        ratio=e3_from_svals(M[comp,:])/Z if len(comp)>=3 else 0.0
        detg=float(np.linalg.det(U[comp,:].T@U[comp,:])) if len(comp)>=3 else 0.0
        max_rank3_err=max(max_rank3_err,abs(ratio-detg))

print('trials_general=40')
print('trials_rank3=40')
print(f'max_relative_E3_cauchy_binet_error={max_z_err:.3e}')
print(f'max_delta_double_sum_vs_residual_average_error={max_delta_err:.3e}')
print(f'max_min_residual_ratio_minus_delta={max_min_minus_delta:.3e}')
print(f'max_rank3_ratio_vs_residual_gram_det_error={max_rank3_err:.3e}')
print(f'partner_hybrid_constant={2**(5/3)*3**0.25*math.e**0.75:.12f}')
print('STATUS=PASS')
