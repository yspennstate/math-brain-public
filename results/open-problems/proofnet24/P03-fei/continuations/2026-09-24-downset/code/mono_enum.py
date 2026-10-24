# Exhaustive FEI quantities over ALL monotone Boolean functions on n <= 6 variables (Dedekind numbers 3, 6, 20, 168,
# 7581, 7828354).  For each nonconstant f: spectral entropy H (bits, all sets including the empty set), total influence
# I, the ratio H/I, and the restriction-step constant rho_0(f) = min over relevant i of Delta_i/Inf_i, where
# Delta_i = H(f) - (H(f|x_i=0) + H(f|x_i=1))/2 (the "key inequality" of Gonzalez-MacManus-Pereyra, arXiv:2606.00246).
# Truth tables are bit masks: bit x of the mask is f(x), x read as an integer with bit j = x_j.
import sys, time, numpy as np

def monotone_masks(n):
    """All monotone functions on n variables as integer masks of length 2^n (new variable = top bit)."""
    M = [0, 1]                                   # n = 0: the two constants on the single point
    for m in range(1, n + 1):
        half = 1 << (m - 1)
        prev = np.array(M, dtype=np.uint64)
        out = []
        for f1 in M:                             # f0 <= f1 pointwise  <=>  f0 & ~f1 == 0
            sub = prev[(prev & np.uint64(~f1 & ((1 << half) - 1))) == 0]
            out.append(sub | np.uint64(f1 << half))
        M = np.concatenate(out).tolist() if m < n else np.concatenate(out)
    return np.asarray(M, dtype=np.uint64)

def walsh(masks, n):
    N = 1 << n
    bits = ((masks[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)
    G = 1.0 - 2.0 * bits                          # +1 where f = 0, -1 where f = 1
    h = 1
    while h < N:                                  # in-place fast Walsh-Hadamard transform along axis 1
        G = G.reshape(G.shape[0], N // (2 * h), 2, h)
        a = G[:, :, 0, :].copy(); b = G[:, :, 1, :]
        G[:, :, 0, :] = a + b; G[:, :, 1, :] = a - b
        G = G.reshape(G.shape[0], N)
        h *= 2
    return G / N

def phi(p):
    out = np.zeros_like(p)
    nz = p > 1e-300
    out[nz] = -p[nz] * np.log2(p[nz])
    return out

def analyse(masks, n):
    N = 1 << n
    G = walsh(masks, n)
    P = G * G
    H = phi(P).sum(1)
    sizes = np.array([bin(s).count('1') for s in range(N)], dtype=np.float64)
    I = (P * sizes[None, :]).sum(1)
    rho = np.full(len(masks), np.inf)
    infs = np.zeros((len(masks), n))
    for i in range(n):
        idx0 = np.array([s for s in range(N) if not (s >> i) & 1])
        a = G[:, idx0]; b = G[:, idx0 | (1 << i)]
        inf = (b * b).sum(1)
        hch = 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)).sum(1)
        d = H - hch
        rel = inf > 1e-12
        r = np.where(rel, d / np.where(rel, inf, 1.0), np.inf)
        rho = np.minimum(rho, r)
        infs[:, i] = inf
    return H, I, rho, infs, P.sum(1)

if __name__ == '__main__':
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    for n in [int(v) for v in sys.argv[1].split(',')]:
        t0 = time.time()
        masks = monotone_masks(n)
        best_ratio = (-1.0, 0); best_rho = (-1.0, 0); maxpars = 0.0; maxinfid = 0.0
        chunk = 200000
        for s in range(0, len(masks), chunk):
            mk = masks[s:s + chunk]
            H, I, rho, infs, pars = analyse(mk, n)
            maxpars = max(maxpars, float(np.abs(pars - 1).max()))
            maxinfid = max(maxinfid, float(np.abs(infs.sum(1) - I).max()))
            nc = I > 1e-12
            r = np.where(nc, H / np.where(nc, I, 1.0), 0.0)
            k = int(np.argmax(r))
            if r[k] > best_ratio[0]: best_ratio = (float(r[k]), int(mk[k]))
            rr = np.where(nc & np.isfinite(rho), rho, 0.0)
            k = int(np.argmax(rr))
            if rr[k] > best_rho[0]: best_rho = (float(rr[k]), int(mk[k]))
        print('n %d: %d monotone functions (%.1f s); max H/I %.6f (mask %s); max rho_0 %.6f (mask %s); '
              'Parseval err %.1e; sum Inf_i vs I err %.1e' % (n, len(masks), time.time() - t0, best_ratio[0],
              hex(best_ratio[1]), best_rho[0], hex(best_rho[1]), maxpars, maxinfid), flush=True)
