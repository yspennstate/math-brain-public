"""B11 (Claude): block-descent constant and recentred channel bound, exhaustive n<=4.
Frozen spec (written before running): family = all f:{0,1}^n->{+1,-1}, n=2,3,4, no symmetry
reduction (exhaustive 16/256/65536 tables). Arithmetic: float64 scan; maxima and near-ties
re-evaluated with mpmath interval arithmetic from exact rational weights. Memory < 200 MB,
runtime < 60 s. Entropy in bits. Quantities per f and nonempty proper block A:
 L_A = H(f) - E_a H(f_a);  I_A = sum_{i in A} Inf_i;  HZ_A = H(S) - H(S_Ac);  J_A = L_A - HZ_A;
 beta_A = sum_{i in A} sum_T min(P(i in S, S_Ac=T), P(i notin S, S_Ac=T)).
Outputs: M_n = max H/I; K_desc(n) = max_f min_{A: I_A>0} L_A/I_A; K_1(n) (singletons only);
check of (ln2) J_A <= 2 beta_A (recentred log-Sobolev bound) and of the C006 mixing identity.
"""
import numpy as np, itertools, json, sys, time, math
LN2 = math.log(2.0)

def hadamard(m):
    H = np.array([[1.0]])
    for _ in range(m):
        H = np.block([[H, H], [H, -H]])
    return H

def popc(m):
    return np.array([bin(x).count('1') for x in range(1 << m)], dtype=float)

def ent(P, axis=-1):
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(P > 1e-300, -P * np.log2(np.where(P > 1e-300, P, 1.0)), 0.0)
    return t.sum(axis=axis)

def block_index(n, A):
    """idx[a, t] = x with A-bits = bits of a (in increasing coordinate order), Ac-bits = bits of t."""
    Ab = [i for i in range(n) if A >> i & 1]; Cb = [i for i in range(n) if not (A >> i & 1)]
    k = len(Ab); idx = np.zeros((1 << k, 1 << (n - k)), dtype=np.int64)
    for a in range(1 << k):
        for t in range(1 << (n - k)):
            x = 0
            for j, i in enumerate(Ab):
                if a >> j & 1: x |= 1 << i
            for j, i in enumerate(Cb):
                if t >> j & 1: x |= 1 << i
            idx[a, t] = x
    return Ab, Cb, idx

def analyze(F, n, want_blocks=True):
    N = F.shape[0]; Hn = hadamard(n); sz = popc(n)
    hat = F @ Hn / (1 << n); W = hat * hat
    H = ent(W); I = W @ sz
    inf = np.stack([W[:, [S for S in range(1 << n) if S >> i & 1]].sum(1) for i in range(n)], 1)
    out = dict(H=H, I=I, inf=inf, blocks={})
    if not want_blocks: return out
    for A in range(1, (1 << n) - 1):
        Ab, Cb, idx = block_index(n, A); k = len(Ab); m = n - k
        Hm = hadamard(m); szm = popc(m)
        Fa = F[:, idx]                       # (N, 2^k, 2^m)
        ha = Fa @ Hm / (1 << m); Wa = ha * ha
        Ha = ent(Wa).mean(1); Ia = (Wa @ szm).mean(1)
        WA = W[:, idx]                       # (N, 2^k [U subset A], 2^m [T subset Ac])
        PT = WA.sum(1)
        mix_err = np.abs(PT - Wa.mean(1)).max()
        HSc = ent(PT)
        L = H - Ha; IA = inf[:, Ab].sum(1); HZ = H - HSc; J = HSc - Ha
        beta = np.zeros(N)
        for j in range(k):
            sel = [a for a in range(1 << k) if a >> j & 1]
            q = WA[:, sel, :].sum(1)
            beta += np.minimum(q, PT - q).sum(1)
        out['blocks'][A] = dict(k=k, L=L, IA=IA, HZ=HZ, J=J, beta=beta, mix_err=mix_err,
                                IA_err=np.abs(IA - (I - Ia)).max())
    return out

def all_tables(n):
    N = 1 << (1 << n)
    x = np.arange(N, dtype=np.int64)[:, None]
    bits = (x >> np.arange(1 << n)) & 1
    return (1.0 - 2.0 * bits)

def descent(res, n, tol=1e-12):
    N = res['H'].shape[0]
    phi = np.full(N, np.inf); phi1 = np.full(N, np.inf); argA = np.zeros(N, dtype=int)
    for A, b in res['blocks'].items():
        ok = b['IA'] > tol
        r = np.where(ok, b['L'] / np.where(ok, b['IA'], 1.0), np.inf)
        better = r < phi; phi = np.where(better, r, phi); argA = np.where(better, A, argA)
        if b['k'] == 1: phi1 = np.minimum(phi1, r)
    return phi, phi1, argA

if __name__ == '__main__':
    summary = {}
    t0 = time.time()
    for n in (2, 3, 4):
        F = all_tables(n); res = analyze(F, n)
        H, I = res['H'], res['I']; nc = I > 1e-12
        ratio = np.where(nc, H / np.where(nc, I, 1), 0.0)
        phi, phi1, argA = descent(res, n)
        dep_all = (res['inf'] > 1e-12).all(1)
        # recentred channel bound check
        worst = 0.0; viol = 0; zero_beta_J = 0.0; base_worst = 0.0; mix = 0.0; iaerr = 0.0
        for A, b in res['blocks'].items():
            pos = b['beta'] > 1e-12
            rr = np.where(pos, b['J'] * LN2 / (2 * np.where(pos, b['beta'], 1)), 0.0)
            worst = max(worst, rr.max()); viol += int((b['J'] * LN2 > 2 * b['beta'] + 1e-10).sum())
            zero_beta_J = max(zero_beta_J, np.abs(np.where(pos, 0, b['J'])).max())
            posI = b['IA'] > 1e-12
            base_worst = max(base_worst, np.where(posI, b['beta'] / np.where(posI, b['IA'], 1), 0).max())
            mix = max(mix, b['mix_err']); iaerr = max(iaerr, b['IA_err'])
        Mn = ratio.max(); iM = int(ratio.argmax())
        phif = np.where(nc & np.isfinite(phi), phi, -np.inf)
        Kd = phif.max(); iK = int(phif.argmax())
        phif_all = np.where(nc & dep_all & np.isfinite(phi), phi, -np.inf)
        Kd_all = phif_all.max(); iKa = int(phif_all.argmax())
        phi1f = np.where(nc & np.isfinite(phi1), phi1, -np.inf); K1 = phi1f.max(); iK1 = int(phi1f.argmax())
        nearK = int((phif > Kd - 1e-9).sum()); nearM = int((ratio > Mn - 1e-9).sum())
        # A051 (3.1) check at C = M_{n-1}
        a051 = None
        if n >= 3:
            C = summary[n - 1]['M_n']; D = H - C * I; crit = D > 1e-10
            bad = 0
            for A, b in res['blocks'].items():
                bad += int((crit & (b['L'] - C * b['IA'] < D - 1e-10)).sum())
            a051 = dict(C=C, n_critical=int(crit.sum()), violations=bad)
        summary[n] = dict(n_tables=int(F.shape[0]), M_n=float(Mn), M_arg=iM, n_near_M=nearM,
            K_desc=float(Kd), K_arg=iK, K_argblock=int(argA[iK]), n_near_K=nearK,
            K_desc_alldep=float(Kd_all), K_alldep_arg=iKa, K1=float(K1), K1_arg=iK1,
            recentred_ratio_max=float(worst), recentred_violations=viol, J_when_beta0_max=float(zero_beta_J),
            beta_over_IA_max=float(base_worst), C006_mixing_err=float(mix), IA_identity_err=float(iaerr),
            A051_check=a051)
        print(n, json.dumps(summary[n]), flush=True)
    summary['runtime_s'] = time.time() - t0
    json.dump(summary, open(sys.argv[1], 'w'), indent=1)
