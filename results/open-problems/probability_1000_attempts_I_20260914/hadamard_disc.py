"""Conjecture 13 of the Randomstrasse 2024 list: for odd k, disc(H_k) = sqrt(2)*sqrt(2^k), where
disc(A) = min over x in {+-1}^n of the sup-norm of Ax and H_k is the Sylvester Hadamard matrix.

H_k x is the Walsh-Hadamard transform of x, so with x the +-1 truth table of a Boolean function f on k
variables, disc(H_k) = min over f of max |W_f|, and since the nonlinearity of f is
NL(f) = 2^(k-1) - max|W_f|/2, the conjecture says exactly

    max nonlinearity on k variables = 2^(k-1) - 2^((k-1)/2)     (k odd),

the bent-concatenation bound.  This searches rotation-symmetric Boolean functions on 9 variables for a
function beating it: the conjecture predicts min max|W| = 32, so any f with max|W| <= 30 refutes it.
"""
import numpy as np, sys

K = 9
N = 1 << K

def orbits(k):
    n = 1 << k
    rep = -np.ones(n, dtype=int); reps = []
    for u in range(n):
        if rep[u] >= 0: continue
        idx = len(reps); reps.append(u)
        v = u
        for _ in range(k):
            rep[v] = idx
            v = ((v << 1) & (n - 1)) | (v >> (k - 1))     # cyclic rotation of the k bits
    return rep, reps

REP, REPS = orbits(K)
NORB = len(REPS)

def wht(x):
    a = x.astype(np.int32).copy()
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        u, v = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = u + v; a[:, 1, :] = u - v
        a = a.reshape(-1)
        h <<= 1
    return a

def spec(bits):
    return np.abs(wht(1 - 2 * bits[REP]))

def cost(w, T):
    over = np.maximum(0, w - T)
    return float((over * over).sum()), int(w.max())

def anneal(T=30, iters=400000, seed=0):
    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, NORB)
    c, mx = cost(spec(bits), T)
    best, bestbits = mx, bits.copy()
    temp0 = 40.0
    for it in range(iters):
        temp = temp0 * (1 - it / iters) + 0.05
        j = rng.integers(0, NORB)
        bits[j] ^= 1
        w = spec(bits); c2, mx2 = cost(w, T)
        if c2 <= c or rng.random() < np.exp(-(c2 - c) / temp):
            c = c2
            if mx2 < best:
                best, bestbits = mx2, bits.copy()
                if best <= T: return best, bestbits
        else:
            bits[j] ^= 1
    return best, bestbits

if __name__ == '__main__':
    seeds = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
    print(f"9 variables, {NORB} rotation orbits; the conjecture says the smallest possible max|W| is 32")
    overall, ob = 10 ** 9, None
    for s in range(seeds):
        b, bits = anneal(30, iters, seed=s)
        nl = (N // 2) - b // 2
        print(f"  seed {s}: best max|W| = {b}   nonlinearity = {nl}   (bound to beat: 240)")
        if b < overall: overall, ob = b, bits.copy()
        if overall <= 30: break
    print(f"\nbest found: max|W| = {overall}, nonlinearity = {N//2 - overall//2}")
    if overall <= 30:
        np.save('rsbf9_witness.npy', ob)
        print("orbit representatives set to 1:", [REPS[i] for i in np.where(ob == 1)[0]])
