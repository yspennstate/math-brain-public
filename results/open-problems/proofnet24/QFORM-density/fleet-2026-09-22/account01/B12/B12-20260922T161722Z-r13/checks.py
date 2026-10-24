import numpy as np

rng = np.random.default_rng(20260922)

def schur(M):
    a = M[0,0]
    b = M[1:,0]
    return M[1:,1:] - np.outer(b,b)/a

mins = []
for _ in range(600):
    d = 5
    a = 0.25 + rng.random()*3
    b = rng.normal(size=d-1)
    C = rng.normal(size=(d-1,d-1)); C=(C+C.T)/2
    M = np.block([[np.array([[a]]), b[None,:]], [b[:,None], C]])
    Z = rng.normal(size=(d,d))
    P = Z@Z.T
    D = schur(M+P)-schur(M)
    mins.append(np.linalg.eigvalsh((D+D.T)/2).min())

maxrank=0
for _ in range(600):
    d=7
    # make a generic SPD base so all tested base pivots are positive
    Z=rng.normal(size=(d,d)); B=Z@Z.T+np.eye(d)
    v=rng.normal(size=d)
    tau=rng.normal()*10
    A=B+tau*np.outer(v,v)
    curB=B.copy(); curA=A.copy()
    ok=True
    for _j in range(3):
        if abs(curA[0,0])<1e-8 or abs(curB[0,0])<1e-8:
            ok=False; break
        curB=schur(curB); curA=schur(curA)
    if ok:
        s=np.linalg.svd(curA-curB,compute_uv=False)
        rank=int(np.sum(s>1e-8*max(1.0,s[0] if len(s) else 1.0)))
        maxrank=max(maxrank,rank)

Cstar=24.183038289961516
out={
    'semidefinite_trials':600,
    'minimum_eigenvalue_of_schur_increment':float(min(mins)),
    'rankone_chain_trials_with_nonzero_pivots':600,
    'maximum_numerical_rank_of_terminal_difference':maxrank,
    'four_over_Cstar':4/Cstar,
}
print(out)
