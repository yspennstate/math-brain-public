import math
import numpy as np

rng=np.random.default_rng(20260924)
max_q=0.0
max_det=0.0
min_star_slack=float('inf')
count=0

for _ in range(5000):
    n=int(rng.integers(4,12))
    G=rng.normal(size=(n,3))
    R,_=np.linalg.qr(G)
    vals=np.array([rng.uniform(1,4),rng.uniform(1,4),-rng.uniform(1,4)])
    rng.shuffle(vals)
    A=R@np.diag(vals)@R.T
    h=int(rng.integers(0,n))
    a=float(A[h,h])
    if abs(a)<1e-6:
        continue
    J=[j for j in range(n) if j!=h]
    b=A[J,h]
    C=A[np.ix_(J,J)]
    S=C-np.outer(b,b)/a
    ew,U=np.linalg.eigh(S)
    nz=np.where(np.abs(ew)>1e-7)[0]
    assert len(nz)==2
    UR=U[:,nz]
    bR=UR@(UR.T@b)
    b0=b-bR
    tau=float(np.linalg.norm(b0))
    rho=float(np.linalg.norm(bR))
    q_formula=a*a/(a*a+tau*tau)
    q_actual=float((R@R.T)[h,h])
    DeltaS=float(np.prod(ew[nz]))
    DeltaA=float(np.prod(vals))
    s=float(np.min(np.abs(vals)))
    max_q=max(max_q,abs(q_formula-q_actual))
    max_det=max(max_det,abs(a*DeltaS-q_actual*DeltaA)/max(1.0,abs(q_actual*DeltaA)))
    slack=rho*rho-(s*s*q_actual-a*a/q_actual)
    min_star_slack=min(min_star_slack,slack)
    assert slack>-2e-9
    count+=1

# Exact collar arithmetic.
q=63/64
a_over_s=1/64
collar=q-a_over_s*a_over_s/q
assert abs(collar-62/63)<1e-15
assert abs((1-q)/q-1/63)<1e-15
assert abs(q/a_over_s-63)<1e-15

# Designated fleet04/B16 control family: all 3 eigenvalues have |lambda|>=1.
for eta in [0.0,0.1,1.0,10.0]:
    B=np.array([[-1.0,eta,0.0],[eta,2.0,0.0],[0.0,0.0,2.0]])
    ev=np.linalg.eigvalsh(B)
    assert np.min(np.abs(ev))>=1-1e-12

print(f'random_trials={count}')
print(f'max_range_leverage_identity_error={max_q:.3e}')
print(f'max_pseudodeterminant_identity_relative_error={max_det:.3e}')
print(f'min_star_inequality_slack={min_star_slack:.3e}')
print(f'collar_rho2_lower_bound={collar:.15f}')
print(f'collar_tau2_over_a2={(1-q)/q:.15f}')
print(f'collar_abs_DeltaS_lower_factor={q/a_over_s:.15f}')
print(f'partner_control_bound_pi={math.pi:.15f}')
print('STATUS=PASS')
