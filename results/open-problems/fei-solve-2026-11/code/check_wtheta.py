"""Conjecture W_theta of FLOW.md 6(a):  W(f) = sum_S mu(S) c^-|S| up(S)^-theta  <=  K^I(f)  ?

Prints sup over the class of  log2(W)/I  (the smallest admissible log2 K), with the extremal function,
for several (theta, c) satisfying the tribes condition 1 + 2^theta/c <= 2^(1-theta), and two that violate it.
Also the tail form: sup over t of  [ log2 P_mu(up(S) < c^(-|S|/theta) 2^-t) + theta t ] / I.

Usage: python check_wtheta.py census4
       python check_wtheta.py census5s [count] [seed]     random 5-variable functions (default 200000)
       python check_wtheta.py fam [nmax]
       python check_wtheta.py tribesformula               closed form on tribes, widths up to 12
"""
import sys
import math
import numpy as np
from check_sec5 import wht, zeta_sup, TINY

PAIRS = [(0.5, 4.0), (0.5, 8.0), (0.25, 4.0), (0.75, 16.0), (0.9, 64.0), (0.5, 2.0), (1.0, 4.0)]


def ok_pair(th, c):
    return 1 + 2 ** th / c <= 2 ** (1 - th) + 1e-12


def wvals(f, n):
    N = 1 << n
    pop = np.array([bin(s).count("1") for s in range(N)], dtype=np.float64)
    fh = wht(f, n)
    mu = fh * fh
    up = zeta_sup(mu, n)
    pos = mu > 1e-15
    I = (mu * pop).sum(axis=1)
    out = {"I": I, "Var": 1.0 - mu[:, 0]}
    A = -(mu * np.where(pos, np.log2(np.maximum(up, TINY)), 0)).sum(axis=1)
    out["A"] = A
    for th, c in PAIRS:
        W = (np.where(pos, mu * np.maximum(up, TINY) ** (-th), 0.0) * c ** (-pop)).sum(axis=1)
        out[(th, c)] = np.log2(W)
    return out


def report(best):
    for th, c in PAIRS:
        v, tag, I, Var, A = best[(th, c)]
        print("  theta=%.2f c=%5.1f %s  sup log2(W)/I = %9.6f   at %s  I=%.4f Var=%.4f  A/I=%.4f  Jensen bound on A/I: %.4f"
              % (th, c, "ok  " if ok_pair(th, c) else "VIOL", v, tag, I, Var, A / I, (v + math.log2(c)) / th))


def upd(best, o, tags):
    ok = o["I"] > 1e-12
    for pr in PAIRS:
        v = np.where(ok, o[pr] / np.maximum(o["I"], TINY), -1e9)
        j = int(np.argmax(v))
        if pr not in best or v[j] > best[pr][0]:
            best[pr] = (float(v[j]), tags(j), float(o["I"][j]), float(o["Var"][j]), float(o["A"][j]))


def census4():
    n, N = 4, 16
    best = {}
    for start in range(0, 1 << N, 8192):
        idx = np.arange(start, start + 8192, dtype=np.uint64)
        f = 1.0 - 2.0 * ((idx[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)
        upd(best, wvals(f, n), lambda j: "tt=0x%04x" % int(idx[j]))
    print("n=4 census (65536 functions)")
    report(best)


def census5s(count, seed):
    n, N = 5, 32
    rng = np.random.default_rng(seed)
    best = {}
    done = 0
    while done < count:
        b = min(8192, count - done)
        # mix of densities so that low-influence functions are represented
        dens = rng.choice([0.5, 0.25, 0.1, 0.05], size=(b, 1))
        bits = (rng.random((b, N)) < dens)
        f = 1.0 - 2.0 * bits.astype(np.float64)
        codes = (bits.astype(np.uint64) << np.arange(N, dtype=np.uint64)[None, :]).sum(axis=1)
        upd(best, wvals(f, n), lambda j: "tt=0x%08x" % int(codes[j]))
        done += b
    print("n=5 sample (%d functions, seed %d, densities 0.5/0.25/0.1/0.05)" % (count, seed))
    report(best)


def families(nmax):
    def pts(n):
        return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)

    rows = []
    for n in range(2, nmax + 1):
        rows.append(("AND_%d" % n, n, np.where(pts(n).all(axis=1), -1.0, 1.0)))
    for n in range(3, nmax + 1, 2):
        rows.append(("MAJ_%d" % n, n, np.where(pts(n).sum(axis=1) * 2 > n, -1.0, 1.0)))
    for w in (2, 3, 4):
        for s in range(2, 9):
            if w * s <= nmax:
                b = pts(w * s).reshape(-1, s, w)
                rows.append(("TRIBES_%dx%d" % (w, s), w * s, np.where(b.all(axis=2).any(axis=1), -1.0, 1.0)))
    for k in (1, 2, 3):
        n = k + (1 << k)
        if n <= nmax:
            b = pts(n)
            addr = (b[:, :k] * (1 << np.arange(k))[None, :]).sum(axis=1)
            rows.append(("ADDR_%d" % k, n, 1.0 - 2.0 * b[np.arange(1 << n), k + addr]))
    print("%-12s %7s %6s %6s  " % ("f", "I", "Var", "A/I") + " ".join("th%.2f/c%g" % pr for pr in PAIRS) + "   (log2 W / I)")
    for name, n, f in rows:
        o = wvals(f[None, :].astype(np.float64), n)
        I = float(o["I"][0])
        print("%-12s %7.4f %6.4f %6.3f  " % (name, I, float(o["Var"][0]), float(o["A"][0]) / I)
              + " ".join("%10.4f" % (float(o[pr][0]) / I) for pr in PAIRS), flush=True)


def tribesformula():
    print("tribes closed form, s = round(2^w ln 2):  log2(W)/I for each pair")
    print("%3s %8s %8s  " % ("w", "s", "I") + " ".join("th%.2f/c%g" % pr for pr in PAIRS))
    for w in range(2, 13):
        d = 2.0 ** (-w)
        s = max(1, round(2 ** w * math.log(2)))
        q = (1 - d) ** s                       # P[no tribe true]
        mu0 = (1 - 2 * (1 - q)) ** 2 if False else (2 * q - 1) ** 2
        I = 2 * s * w * d * (1 - d) ** (s - 1)
        vals = []
        for th, c in PAIRS:
            base = (1 - d) ** (2 - th) + d ** (2 - th) * ((1 + 2 ** th / c) ** w - 1)
            logW_main = s * math.log(base)
            # W = mu0 + 4^(1-th) (base^s - (1-d)^((2-th)s)); use logs to avoid overflow
            if logW_main > 600:
                lw = (math.log(4) * (1 - th) + logW_main) / math.log(2)
            else:
                lw = math.log2(mu0 + 4 ** (1 - th) * (math.exp(logW_main) - (1 - d) ** ((2 - th) * s)))
            vals.append(lw / I)
        print("%3d %8d %8.4f  " % (w, s, I) + " ".join("%10.4f" % v for v in vals))


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "census4":
        census4()
    elif m == "census5s":
        census5s(int(sys.argv[2]) if len(sys.argv) > 2 else 200000, int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    elif m == "fam":
        families(int(sys.argv[2]) if len(sys.argv) > 2 else 14)
    else:
        tribesformula()
