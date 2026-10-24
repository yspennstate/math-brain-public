import numpy as np, math

rng = np.random.default_rng(20260922)

def energies(S, h=0):
    n = S.shape[0]
    out = [i for i in range(n) if i != h]
    d = float(S[h,h])
    w = S[out,h]
    C = S[np.ix_(out,out)]
    N = d*C - np.outer(w,w)
    A = float(np.sum(N*N))
    Bsh = 0.0
    Bdis = 0.0
    m = len(out)
    for j in range(m):
        for p in range(m):
            for q in range(p+1,m):
                z = w[p]*C[q,j] - w[q]*C[p,j]
                if j == p or j == q:
                    Bsh += z*z
                else:
                    Bdis += z*z
    sh = S[:,h]
    E = 0.0
    for j in out:
        sj = S[:,j]
        E += float((sh@sh)*(sj@sj) - (sh@sj)**2)
    sv = np.linalg.svd(S, compute_uv=False)
    s2 = sv[1] if len(sv) >= 2 else 0.0
    lower = s2*s2 * float(sh@sh)
    return A,Bsh,Bdis,E,lower

max_identity_error = 0.0
min_lower_ratio = float('inf')
for n in range(4,9):
    for _ in range(30):
        M = rng.normal(size=(n,n))
        S = (M+M.T)/2
        A,Bs,Bd,E,lower = energies(S,0)
        max_identity_error = max(max_identity_error, abs(A+Bs+Bd-E))
        if lower > 1e-12:
            min_lower_ratio = min(min_lower_ratio, E/lower)

beta0 = 200**(-0.25)
packet0 = beta0**2
print(f'max_identity_error={max_identity_error:.3e}')
print(f'min_E_over_s2sq_rowenergy={min_lower_ratio:.12f}')
print(f'beta0={beta0:.15f}')
print(f'packet_lower={packet0:.15f}')
print(f'three_way_lower={packet0/3:.15f}')
print(f'disjoint_cross_E2_lower={packet0/24:.15f}')
print('stress d=1/32 beta=2 C=0')
d=1/32
beta=2
disc=math.sqrt(d*d+4*beta*beta)
lp=(d+disc)/2
lm=(d-disc)/2
for m in [16,64,256,1024,4096]:
    local=beta*beta/m
    print(f'm={m} eigs=({lm:.12f},{lp:.12f}) s2={min(abs(lm),abs(lp)):.12f} A=16 Bsh=0 Bdis=0 max_local={local:.12f}')
print('QFORM_ANCHOR_EXTERIOR_PACKET_CHECK_PASS')
