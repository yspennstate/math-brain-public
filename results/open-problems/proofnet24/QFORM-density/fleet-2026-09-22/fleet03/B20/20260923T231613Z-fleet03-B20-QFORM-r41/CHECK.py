import numpy as np

SEED = 20260923
TRIALS = 10000
TOL_KERNEL = 1e-7
TOL_STABLE = 1e-6
rng = np.random.default_rng(SEED)
choices = np.array([-2.2,-1.0,-0.8,-0.15,0.4,0.93,1.0,1.3,2.1])
checked = skipped = violations = 0

for trial in range(TRIALS):
    m = int(rng.integers(1,8))
    ell = int(rng.integers(0,8))
    B = rng.normal(size=(m,m)); B = (B+B.T)/2
    if ell:
        U,_ = np.linalg.qr(rng.normal(size=(ell,ell)))
        d_exact = rng.choice(choices,size=ell)
        D = U @ np.diag(d_exact) @ U.T
        C = rng.normal(size=(m,ell))
        A = np.block([[B,C],[C.T,D]])
    else:
        d_exact = np.array([])
        D = np.zeros((0,0)); C = np.zeros((m,0)); A = B
    evalA = np.linalg.eigvalsh(A)

    for sigma in (1.0,-1.0):
        # Numerical regression only: omit cases where floating point makes
        # the closed threshold count unstable.  The proof in REPORT.md is exact.
        if np.min(np.abs(sigma*evalA-1.0)) < TOL_STABLE:
            skipped += 1
            continue
        if ell:
            evalD,V = np.linalg.eigh(D)
            mask = np.abs(evalD-sigma) < TOL_KERNEL
            P = V[:,mask] @ V[:,mask].T if mask.any() else np.zeros((ell,ell))
            inv = np.zeros_like(evalD)
            inv[~mask] = 1.0/(evalD[~mask]-sigma)
            R = V @ np.diag(inv) @ V.T
            S = -np.eye(m) + sigma*(B-C@R@C.T)
            G = C@P
            _,sv,vh = np.linalg.svd(G.T,full_matrices=True)
            rank = int(np.sum(sv>TOL_KERNEL))
            N = vh[rank:].T
            evalT = np.linalg.eigvalsh(N.T@S@N) if N.shape[1] else np.array([])
            if evalT.size and np.min(np.abs(evalT)) < TOL_STABLE:
                skipped += 1
                continue
            q = int(np.sum(evalT >= 0.0))
            base = int(np.sum(sigma*d_exact >= 1.0))
        else:
            evalT = np.linalg.eigvalsh(-np.eye(m)+sigma*B)
            if np.min(np.abs(evalT)) < TOL_STABLE:
                skipped += 1
                continue
            q = int(np.sum(evalT >= 0.0)); base = 0
        full = int(np.sum(sigma*evalA >= 1.0))
        checked += 1
        if full != base + q:
            violations += 1
            raise AssertionError((trial,sigma,full,base,q))

rho = 1/64
epsH = (3+122*np.sqrt(10))*2**(-20)
delta0 = epsH + rho
partner_cap = np.exp(1.5)*np.sqrt(1728/61)
print(f"seed={SEED}")
print(f"trials={TRIALS}")
print(f"stable_sign_checks={checked}")
print(f"numerically_threshold_ambiguous_skipped={skipped}")
print(f"violations={violations}")
print(f"epsilon_H={epsH:.18f}")
print(f"delta0={delta0:.18f}")
print(f"one_minus_delta0={1-delta0:.18f}")
print(f"partner_cap={partner_cap:.15f}")
print("QFORM_B20_R41_CHECK_PASS")
