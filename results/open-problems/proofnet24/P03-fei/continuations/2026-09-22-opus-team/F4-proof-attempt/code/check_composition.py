"""Brute-force check of the erasure composition lemma for balanced disjoint composition.

f = F(g_1,...,g_k), g_j balanced on disjoint blocks, some outer inputs left as fresh variables.
Claim: for w in block j,  B_w(f) = Inf_j(F) B_w(g_j) + sum_{T not ni j} E(Fhat(T)^2, ghat_j({w})^2 Fhat(T+j)^2),
       Inf_w(f) = Inf_j(F) Inf_w(g_j);   for a fresh outer input z:  B_z(f) = B_z(F), Inf_z(f) = Inf_z(F).
E(r,s) = phi(r)+phi(s)-phi(r+s)."""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *

def E(r, s):
    return phi(np.array(r)) + phi(np.array(s)) - phi(np.array(r) + np.array(s))

def compose(Ftt, kF, blocks):
    """blocks[j] = (tt_j, n_j) or None (fresh variable). Returns tt of f and the variable layout."""
    sizes = [b[1] if b is not None else 1 for b in blocks]
    n = sum(sizes); offs = np.cumsum([0] + sizes[:-1])
    N = 1 << n; tt = np.empty(N, dtype=np.int8)
    for x in range(N):
        yidx = 0
        for j, b in enumerate(blocks):
            sub = (x >> offs[j]) & ((1 << sizes[j]) - 1)
            val = b[0][sub] if b is not None else (1 - 2 * sub)
            bit = 1 if val == -1 else 0   # -1 -> bit 1
            yidx |= bit << j
        tt[x] = Ftt[yidx]
    return tt, n, offs, sizes

rng = np.random.default_rng(1)
maxerr = 0.0
cases = 0
for trial in range(40):
    kF = int(rng.integers(2, 5))
    Ftt = (1 - 2 * rng.integers(0, 2, 1 << kF)).astype(np.int8)
    blocks = []
    for j in range(kF):
        if rng.random() < 0.3:
            blocks.append(None); continue
        nj = int(rng.integers(2, 4))
        while True:  # balanced random g
            gt = np.array([1] * (1 << (nj - 1)) + [-1] * (1 << (nj - 1)), dtype=np.int8); rng.shuffle(gt)
            break
        blocks.append((gt, nj))
    tt, n, offs, sizes = compose(Ftt, kF, blocks)
    if n > 14: continue
    fh = wht(tt[None, :].astype(float)); cq = coord_quantities(fh, n)
    FH = wht(Ftt[None, :].astype(float))[0]; cF = coord_quantities(FH[None, :], kF)
    for j, b in enumerate(blocks):
        if b is None:
            z = offs[j]
            maxerr = max(maxerr, abs(cq["B"][0, z] - cF["B"][0, j]), abs(cq["Inf"][0, z] - cF["Inf"][0, j]))
            cases += 1; continue
        gt, nj = b
        gh = wht(gt[None, :].astype(float))[0]; cg = coord_quantities(gh[None, :], nj)
        for wl in range(nj):
            w = offs[j] + wl
            c2 = gh[1 << wl] ** 2
            S = np.arange(1 << kF)
            low = S[((S >> j) & 1) == 0]
            second = E(FH[low] ** 2, c2 * FH[low | (1 << j)] ** 2).sum()
            pred_B = cF["Inf"][0, j] * cg["B"][0, wl] + second
            pred_I = cF["Inf"][0, j] * cg["Inf"][0, wl]
            maxerr = max(maxerr, abs(cq["B"][0, w] - pred_B), abs(cq["Inf"][0, w] - pred_I))
            cases += 1
print("composition lemma: cases", cases, "max abs error", maxerr)
