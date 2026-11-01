"""Second path for Lemma B (NOTES section 5e), sharing no code with selector_block.py.

F(x, y) = s(x) chi_{tau(x)}(y), x in {0,1}^m (address, low bits), y in {0,1}^N (data, high bits). Checks, with its own
Hadamard-matrix transform and its own entropy and B routines:
    sum_{t in Y} B_t  <=  H(S_Y)  =  H(tau(X))  <=  2 I_X.
(1) exhaustive: every Boolean function of 4 bits with each coordinate as Y (|Y| = 1; every function is in the class);
    every (tau, s) with m = 2, N = 2;
(2) random: tau and s drawn under four schemes (uniform tau, few cells, subcube cells, one-hot), m = 3..7, N = 1..6.
Prints the largest ratios sum_Y B_t / H(S_Y) and H(S_Y) / (2 I_X) and any violation beyond 1e-12.
Usage: python -B audit_selector_block.py
"""
import itertools, math
import numpy as np


def hadamard(n):
    H = np.array([[1.0]])
    for _ in range(n):
        H = np.block([[H, H], [H, -H]])
    return H


HAD = {}


def spectrum(F, n):
    if n not in HAD:
        HAD[n] = hadamard(n)
    c = HAD[n] @ F.astype(float) / (1 << n)
    return c * c


def xlogx_sum(w):
    w = w[w > 1e-300]
    return float(-(w * np.log2(w)).sum())


def cond_one(p, i, n):
    """H(S_i | S - i) for a law p on subsets of n coordinates"""
    idx = np.arange(1 << n)
    lo = idx[((idx >> i) & 1) == 0]
    a, d = p[lo], p[lo + (1 << i)]
    tot = a + d
    out = 0.0
    for aa, dd, tt in zip(a, d, tot):
        if aa > 0 and dd > 0:
            out += -aa * math.log2(aa / tt) - dd * math.log2(dd / tt)
    return out


def check(tau, s, m, N):
    """tau: array over x of subsets of Y (as N-bit ints); s: array of +-1. Returns (BY, HSY, Htau, IX)."""
    n = m + N
    idx = np.arange(1 << n)
    x, y = idx & ((1 << m) - 1), idx >> m
    par = np.zeros(1 << n, dtype=np.int64)
    for k in range(N):
        par ^= ((tau[x] >> k) & 1) & ((y >> k) & 1)
    F = s[x] * (1 - 2 * par)
    p = spectrum(F, n)
    BY = sum(cond_one(p, m + k, n) for k in range(N))
    RY = np.zeros(1 << N)
    np.add.at(RY, idx >> m, p)
    HSY = xlogx_sum(RY)
    Rt = np.bincount(tau, minlength=1 << N) / len(tau)
    Htau = xlogx_sum(Rt)
    IX = float(sum(((idx >> j) & 1) @ p for j in range(m)))
    return BY, HSY, Htau, IX


def update(st, BY, HSY, Htau, IX):
    st["n"] += 1
    st["viol"] += int(BY > HSY + 1e-12) + int(abs(HSY - Htau) > 1e-9) + int(HSY > 2 * IX + 1e-12)
    if HSY > 1e-12:
        st["r1"] = max(st["r1"], BY / HSY)
    if IX > 1e-12:
        st["r2"] = max(st["r2"], HSY / (2 * IX))
    st["dH"] = max(st["dH"], abs(HSY - Htau))


def new():
    return dict(n=0, viol=0, r1=0.0, r2=0.0, dH=0.0)


def show(name, st):
    print(f"  {name:34s} cases={st['n']:7d} violations={st['viol']}  max B_Y/H(S_Y)={st['r1']:.6f}  "
          f"max H(S_Y)/(2 I_X)={st['r2']:.6f}  max|H(S_Y)-H(tau)|={st['dH']:.1e}", flush=True)


def exhaustive():
    print("(1) exhaustive")
    st = new()
    for code in range(1 << 16):
        T = np.array([1 - 2 * ((code >> v) & 1) for v in range(16)], dtype=np.int64)
        for t in range(4):
            # move coordinate t to the top: x = the other three bits, y = bit t
            perm = [b for b in range(4) if b != t] + [t]
            idx = np.arange(16)
            newidx = np.zeros(16, dtype=np.int64)
            for k, b in enumerate(perm):
                newidx |= ((idx >> b) & 1) << k
            F2 = np.empty(16, dtype=np.int64)
            F2[newidx] = T
            # read tau and s off the fibers: F2[x + 8 y]
            f0, f1 = F2[:8], F2[8:]
            tau = (f0 != f1).astype(np.int64)
            s = f0
            r = check(tau, s, 3, 1)
            update(st, *r)
    show("all 4-bit functions, |Y| = 1", st)
    st = new()
    for taus in itertools.product(range(4), repeat=4):
        tau = np.array(taus, dtype=np.int64)
        for sg in range(16):
            s = np.array([1 - 2 * ((sg >> v) & 1) for v in range(4)], dtype=np.int64)
            update(st, *check(tau, s, 2, 2))
    show("all (tau, s), m = 2, N = 2", st)


def random_cases(seed=20261012, per=150):
    print("(2) random")
    rng = np.random.default_rng(seed)
    for scheme in ("uniform", "few cells", "subcube cells", "one-hot"):
        st = new()
        for m in range(3, 8):
            for N in range(1, 7):
                if m + N > 11:
                    continue
                for _ in range(per):
                    M = 1 << m
                    if scheme == "uniform":
                        tau = rng.integers(0, 1 << N, M)
                    elif scheme == "few cells":
                        vals = rng.integers(0, 1 << N, rng.integers(1, 4))
                        tau = vals[rng.integers(0, len(vals), M)]
                    elif scheme == "subcube cells":
                        c = int(rng.integers(0, m + 1))
                        cells = np.arange(M) & ((1 << c) - 1)
                        vals = rng.integers(0, 1 << N, 1 << c)
                        tau = vals[cells]
                    else:
                        tau = np.zeros(M, dtype=np.int64)
                        hit = rng.integers(0, N, M)
                        on = rng.random(M) < 0.5
                        tau[on] = 1 << hit[on]
                    s = rng.choice([-1, 1], M)
                    if rng.random() < 0.3:
                        s = np.ones(M, dtype=np.int64)
                    update(st, *check(tau.astype(np.int64), s.astype(np.int64), m, N))
        show(scheme, st)


if __name__ == "__main__":
    exhaustive()
    random_cases()
    print("done")
