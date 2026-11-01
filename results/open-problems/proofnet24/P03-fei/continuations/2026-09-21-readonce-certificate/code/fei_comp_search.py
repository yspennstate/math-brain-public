"""Lower bounds on the FEI constant by biased recursive composition (O'Donnell-Tan 2013, Hod 2017), as a
search objective over small Boolean functions.

Conventions (Hod): true = -1, Pr[f] = Pr[f = true]; a bias p means each input is true with probability p,
so E[x_i] = eta = 1 - 2p. F on k inputs is eta-balanced when Pr_{x~p}[F = true] = p (a fixed point).
For a base g with Pr[g] = p and an eta-balanced composer F, f_m = F o (f_{m-1}, ..., f_{m-1}) with f_0 = g has
(Lemma 3.1 of Hod = Prop 3.2 of O'Donnell-Tan)  I[f] = It[F] I+[g],  H[f] = It[F] H+[g] + Ht[F],
with V = 4p(1-p), I+ = I/V, H+ = (H - h(V))/V and It, Ht the eta-biased total influence and spectral entropy of F.
Iterating, the ratio converges to

    R(F, g) = H[g]/I[g] + (V Ht[F] - It[F] h(V)) / (I[g] (It[F] - V)),        (needs It[F] > V)

which for p = 1/2 is H[F]/(I[F]-1) (O'Donnell-Tan, 6.278944 with a 6-variable g) and for F = NAND2 at p = Phi
with g = the lexicographic function l<Phi> is 6.413846 (Hod, Theorem 3.3). The base l<p> is the AND/OR chain whose
gate pattern is the binary expansion of p (digit 1 -> OR, digit 0 -> AND), measure exactly p (fei_chain.py).
Every value of R(F, g) is a rigorous lower bound on the FEI constant (it is the limit ratio of an explicit family).
"""
import sys, math, json, random, time, itertools
import numpy as np
from math import log2
sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
from fei_chain import chain_state

def h2(v):
    if v <= 0 or v >= 1:
        return 0.0
    return -v * log2(v) - (1 - v) * log2(1 - v)

def lex_pattern(p, digits=90):
    """binary expansion of p in (0,1): digit 1 -> 'O', digit 0 -> 'A' (x <_lex t has measure t)"""
    out = []
    x = p
    for _ in range(digits):
        x *= 2
        if x >= 1:
            out.append("O"); x -= 1
        else:
            out.append("A")
    return "".join(out)

def lex_HI(p):
    a, H, I = chain_state(lex_pattern(p))
    return H, I

def truth_from_int(tt, k):
    """values f(x) in {+1,-1}; index bit i = input x_i with bit 1 meaning TRUE (x_i = -1). f = -1 where tt bit is 1 (true)."""
    bits = (tt >> np.arange(1 << k)) & 1
    return 1 - 2 * bits

def biased_spectrum(f, k, p):
    """eta-biased Fourier coefficients of f (values +-1) with Pr[x_i = true] = p. Returns array over S (bitmask)."""
    eta = 1.0 - 2.0 * p
    sig = math.sqrt(max(1e-300, 1.0 - eta * eta))
    # input x_i: index bit 0 -> x_i = +1 (false, prob 1-p); bit 1 -> x_i = -1 (true, prob p)
    # chi~_S(x) = prod_{i in S} (x_i - eta)/sig ; f~(S) = E[f chi~_S]
    M = np.array([[1.0 - p, p], [(1.0 - p) * (1.0 - eta) / sig, p * (-1.0 - eta) / sig]])  # rows: i not in S, i in S; cols: bit 0, bit 1
    a = np.asarray(f, dtype=float).reshape([2] * k)  # axis j = variable j
    for j in range(k):
        a = np.tensordot(M, a, axes=([1], [j]))       # contract variable j -> new axis 0 indexed by (i in S)
        a = np.moveaxis(a, 0, j)
    return a.reshape(-1)  # index bit j = whether j in S

def HI_from_spectrum(coef, k):
    pS = coef * coef
    nz = pS > 1e-18
    H = float(-(pS[nz] * np.log2(pS[nz])).sum())
    I = float((POP[k] * pS).sum())
    return H, I

POP = {k: np.array([bin(s).count("1") for s in range(1 << k)]) for k in range(1, 13)}

def fixed_points(f, k):
    """all p in (0,1) with Pr_p[F = true] = p; Pr_p[F=true] = sum_{x: f(x)=-1} p^{#true bits}(1-p)^{k-#true}"""
    ntrue = POP[k]
    tru = (np.asarray(f) < 0)
    # polynomial in p: sum over true x of p^t (1-p)^(k-t) ; build coefficient array by counting t
    counts = np.bincount(ntrue[tru], minlength=k + 1)  # number of true inputs with t true bits
    poly = np.zeros(k + 1)
    for t in range(k + 1):
        if counts[t] == 0:
            continue
        # p^t (1-p)^(k-t) expanded: coefficients of (1-p)^(k-t)
        for j in range(k - t + 1):
            poly[t + j] += counts[t] * math.comb(k - t, j) * (-1) ** j
    poly[1] -= 1.0  # minus p
    roots = np.roots(poly[::-1]) if np.any(poly) else np.array([])
    out = []
    for r in roots:
        if abs(r.imag) < 1e-9 and 1e-6 < r.real < 1 - 1e-6:
            out.append(float(r.real))
    return sorted(set(round(x, 12) for x in out))

def objective(f, k, base="lex", return_detail=False):
    best = (-1.0, None)
    for p in fixed_points(f, k):
        V = 4 * p * (1 - p)
        coef = biased_spectrum(f, k, p)
        Ht, It = HI_from_spectrum(coef, k)
        if It - V <= 1e-9:
            continue
        if base == "lex":
            Hg, Ig = lex_HI(p)
        else:
            Hg, Ig = base(p)
        R = Hg / Ig + (V * Ht - It * h2(V)) / (Ig * (It - V))
        if R > best[0]:
            best = (R, dict(p=p, V=V, Ht=Ht, It=It, Hg=Hg, Ig=Ig))
    return best if return_detail else best[0]

def validate():
    ok = True
    # l<2/3>: I = 4/3, H = 2 log2 3 ; l<Phi>: I ~ 1.2976895, H ~ 2.4239395 (Hod)
    Phi = (math.sqrt(5) - 1) / 2
    H23, I23 = lex_HI(2 / 3); HPhi, IPhi = lex_HI(Phi)
    print("l<2/3>: H %.6f (2 log2 3 = %.6f) I %.6f (4/3)" % (H23, 2 * log2(3), I23))
    print("l<Phi>: H %.7f (Hod > 2.4239395) I %.7f (Hod < 1.2976895)" % (HPhi, IPhi))
    ok &= abs(H23 - 2 * log2(3)) < 1e-9 and abs(I23 - 4 / 3) < 1e-9 and abs(HPhi - 2.42394) < 1e-4 and abs(IPhi - 1.29769) < 1e-4
    # NAND2: f = -1 (true) unless both inputs true. index bits: 1 = true. true inputs: 00,01,10 -> tt has bits 0,1,2 set = 0b0111 = 7
    R, d = objective(truth_from_int(0b0111, 2), 2, return_detail=True)
    print("NAND2 at its fixed point p=%.6f: It %.5f (8 Phi^4 = %.5f) Ht %.5f (Hod 1.77611) -> R = %.6f (Hod 6.413846)" % (d["p"], d["It"], 8 * Phi ** 4, d["Ht"], R))
    ok &= abs(R - 6.413846) < 2e-6
    # O'Donnell-Tan g on 6 variables: g = (x1^x2^x3) v (x1^x2^x4) v (x1^x2^x5^x6) v (~x1^~x2^~x3) v (~x1^~x2^x4^x5)  [their listing shows
    # bars on the last two clauses' x1 x2 and x3 in the PDF text they are lost]; we test the balanced objective H/(I-1) on it below and print.
    def ot_g(x):  # x: tuple of booleans (True = true)
        x1, x2, x3, x4, x5, x6 = x
        return (x1 and x2 and x3) or (x1 and x2 and x4) or (x1 and x2 and x5 and x6) or ((not x1) and (not x2) and (not x3)) or ((not x1) and (not x2) and x4 and x5)
    vals = np.array([-1 if ot_g(tuple(bool((i >> j) & 1) for j in range(6))) else 1 for i in range(64)])
    bal = (vals < 0).sum()
    coef = biased_spectrum(vals, 6, 0.5); H, I = HI_from_spectrum(coef, 6)
    print("O'Donnell-Tan g (as read from the PDF): true on %d of 64, H %.5f I %.5f -> H/(I-1) = %.6f (paper: H>=3.92434, I=1.625, 6.278944)" % (bal, H, I, H / (I - 1) if I > 1 else float('nan')))
    R6 = objective(vals, 6)
    print("   objective with fixed points and lex base: %.6f" % R6)
    return ok

def anneal(k, iters, seed, T0=0.02, init=None, log=None):
    rng = random.Random(seed)
    n = 1 << k
    f = np.array(init, dtype=int) if init is not None else np.array([rng.choice((1, -1)) for _ in range(n)])
    cur = objective(f, k); best = (cur, f.copy())
    for it in range(iters):
        T = T0 * (1 - it / iters) + 1e-4
        j = rng.randrange(n); f[j] = -f[j]
        j2 = None
        if rng.random() < 0.3:
            j2 = rng.randrange(n); f[j2] = -f[j2]
        val = objective(f, k)
        if val >= cur or rng.random() < math.exp((val - cur) / T):
            cur = val
            if val > best[0]:
                best = (val, f.copy())
                if log is not None:
                    log(k, val, f)
        else:
            f[j] = -f[j]
            if j2 is not None:
                f[j2] = -f[j2]
    return best

def tt_int(f):
    bits = (np.asarray(f) < 0).astype(int)
    return int(sum(int(b) << i for i, b in enumerate(bits)))

if __name__ == "__main__":
    print("validation:", "OK" if validate() else "MISMATCH")
    print("exhaustive k=3 (all 256):")
    best3 = max(((objective(truth_from_int(t, 3), 3), t) for t in range(256)), key=lambda x: x[0])
    print("  best R %.6f tt=%d detail %s" % (best3[0], best3[1], objective(truth_from_int(best3[1], 3), 3, return_detail=True)[1]))
    t0 = time.time()
    print("exhaustive k=4 (all 65536):")
    best4 = (-1, 0)
    for t in range(1 << 16):
        v = objective(truth_from_int(t, 4), 4)
        if v > best4[0]:
            best4 = (v, t)
    print("  best R %.6f tt=%d detail %s  (%.0f s)" % (best4[0], best4[1], objective(truth_from_int(best4[1], 4), 4, return_detail=True)[1], time.time() - t0))
    for k in (5, 6, 7, 8):
        t0 = time.time()
        res = max((anneal(k, 6000 if k <= 6 else 4000, s) for s in range(3)), key=lambda b: b[0])
        R, d = objective(res[1], k, return_detail=True)
        print("anneal k=%d: best R %.6f  p=%.5f It=%.4f Ht=%.4f  tt=%d  (%.0f s)" % (k, R, d["p"], d["It"], d["Ht"], tt_int(res[1]), time.time() - t0))
