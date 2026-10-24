"""Chain rule for U along spectral marginalisation (forgetting coordinates one at a time):
U(P) = sum_k [B - Gamma]_{i_k}(P_k), H(P) = sum_k B_{i_k}(P_k), H - U = sum_k Gamma_{i_k}(P_k),
P_k = law of S cap {i_k..i_n}.  Also the Jensen bound U <= I log2 e + sum_k Inf_k log2(Lambda_k/Inf_k)."""
import numpy as np, json
from feilib import *
from upward import Uprime, upper_sets

def merge(P, n, i):
    """law of S minus {i}: returns law on n-1 bits (bit i removed)."""
    idx = np.arange(1 << n); lo = idx[(idx >> i) & 1 == 0]
    m = P[lo] + P[lo | (1 << i)]
    comp = ((lo >> (i + 1)) << i) | (lo & ((1 << i) - 1))
    out = np.zeros(1 << (n - 1)); out[comp] = m; return out

def step_terms(P, n, i):
    idx = np.arange(1 << n); lo = idx[(idx >> i) & 1 == 0]; hi = lo | (1 << i)
    pi = upper_sets(P, n)
    u2, v2 = P[lo], P[hi]; m = u2 + v2
    with np.errstate(divide='ignore', invalid='ignore'):
        B = np.where(m > 0, m * binh(np.where(m > 0, v2 / np.where(m>0,m,1), 0)), 0).sum()
        Gam = np.where(v2 > 0, v2 * np.log2(pi[lo] / np.where(pi[hi] > 0, pi[hi], 1)), 0).sum()
        r = np.where(pi[lo] > 0, pi[hi] / np.where(pi[lo] > 0, pi[lo], 1), 0)
    Lam = float((m * r).sum()); Inf = float(v2.sum())
    return float(B), float(Gam), Lam, Inf

def chain(t, order):
    t = np.asarray(t); n = nbits(len(t)); P = spectrum(t); U0 = float(Uprime(P, n)); H0 = float(entropy(P))
    sB = sG = bound = 0.0; cur = P; labels = list(range(n))
    for i in order:
        j = labels.index(i); B, Gm, Lam, Inf = step_terms(cur, len(labels), j)
        sB += B; sG += Gm
        if Inf > 0: bound += Inf * np.log2(max(Lam / Inf, 1e-300))
        cur = merge(cur, len(labels), j); labels.pop(j)
    I = float(total_influence(P, n))
    return dict(U=U0, H=H0, sumB=sB, sumBminusG=sB - sG, I=I, LamBound=I * np.log2(np.e) + bound)

if __name__ == "__main__":
    from families import *
    from sweepG import compose
    g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
    maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
    cases = {'g5': g5, 'pd8': pointdefect(8), 'tribes3x3': tribes(3, 3), 'maj9': maj(9), 'addr2': addressing(2), 'x003_k4r4': x003(4, 4), 'bent6': bent(3), 'maj3 o g5': compose(maj3, 3, g5, 5)}
    for k, t in cases.items():
        t = np.asarray(t); n = nbits(len(t)); inf = influences(spectrum(t), n)
        res = {}
        for name, order in [('id', list(range(n))), ('incInf', list(np.argsort(inf))), ('decInf', list(np.argsort(-inf)))]:
            res[name] = chain(t, [int(o) for o in order])
        r0 = res['id']
        print(f"{k:10s} U={r0['U']:.4f} sum(B-G)={r0['sumBminusG']:.4f} H={r0['H']:.4f} sumB={r0['sumB']:.4f} | U/I={r0['U']/r0['I']:.3f} LamBound/I: id {res['id']['LamBound']/r0['I']:.3f} inc {res['incInf']['LamBound']/r0['I']:.3f} dec {res['decInf']['LamBound']/r0['I']:.3f}")
