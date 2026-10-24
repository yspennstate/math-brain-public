"""E_S |union of V_t over dense terms t| / I  for read-k DNFs (beta = 2, 3), next to the
proof's sum-over-dense-terms cost.  Dense: |S cap V_t| >= |V_t|/beta.  Also the sparse mass
E_S #{i in S not in any dense term}/I."""
import numpy as np, numba as nb
from feicore import spectrum, popcounts, polite
from mincover import random_readk, tt_dnf
polite()

@nb.njit(cache=True)
def dense_union(masks, sizes, pc, beta, n):
    N = 1 << n
    un = np.zeros(N, dtype=np.int64); sm = np.zeros(N, dtype=np.int64); sp = np.zeros(N, dtype=np.int64)
    for A in range(N):
        U = 0; s = 0
        for t in range(masks.size):
            if beta * pc[A & masks[t]] >= sizes[t]:
                U |= masks[t]; s += sizes[t]
        un[A] = pc[U]; sm[A] = s; sp[A] = pc[A & ~U]
    return un, sm, sp

rng = np.random.default_rng(13)
for n in (14, 16):
    pc = popcounts(n)
    for k in (2, 3, 4, 6, 8, 10):
        for rep in range(3):
            terms = random_readk(n, k, rng)
            if not terms: continue
            masks = np.array([sum(1 << int(v) for v in V) for V, _ in terms], dtype=np.int64)
            sizes = np.array([len(V) for V, _ in terms], dtype=np.int64)
            P = spectrum(tt_dnf(n, terms)); I = float((P * pc).sum())
            if I <= 0: continue
            out = []
            for beta in (2, 3):
                un, sm, sp = dense_union(masks, sizes, pc, beta, n)
                out.append(f"b={beta}: union/I={(P*un).sum()/I:5.2f} sum/I={(P*sm).sum()/I:6.2f} sparse/I={(P*sp).sum()/I:5.3f}")
            print(f"n={n} k={k:2d} " + " | ".join(out), flush=True)
