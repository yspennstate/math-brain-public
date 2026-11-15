"""Numeric check of FLOW.md section 7: the restriction step, the erasure form, the good-coordinate form.

For Boolean f (+-1), mu = fhat^2, U ~ mu. For a coordinate i and T not containing i: a = fhat(T), b = fhat(T+i).
  E_i = H(1[i in U] | U - i) = sum_T (a^2+b^2) h(b^2/(a^2+b^2))
  J_i = JSD(spectrum f(i->+1), spectrum f(i->-1)) = sum_T (a^2+b^2) (1 - h((1+t)/2)), t = 2ab/(a^2+b^2)
  D_i = H(f) - H(f(i->+1))/2 - H(f(i->-1))/2          claim: D_i = E_i + J_i
  Hm = sum_i E_i (claim Hm <= H);  Psi = sum_i D_i;  G = E_U sum_{i in U} log2(1 + mu(U-i)/mu(U))
  claims: J_i <= (2/ln 2) Inf_i;  G <= Hm <= G + I/ln 2
  best coordinate: rD = min over i with Inf_i > 0 of D_i/Inf_i,  rE likewise with E_i;
  rmaxD, rmaxE = the same ratios at the coordinate of largest influence (ties: the best of the tied ones)

Usage: python check_erasure.py census4
       python check_erasure.py file PATH n        one hex truth table per line (bit x set when f(x) = -1)
       python check_erasure.py sample n count seed
       python check_erasure.py fam [nmax]
"""
import sys
import math
import numpy as np
from check_sec5 import wht

LN2 = math.log(2.0)


def eta(x):
    return np.where(x > 1e-300, -x * np.log2(np.maximum(x, 1e-300)), 0.0)


def h2(x):
    return eta(x) + eta(1.0 - x)


def stats(f, n, direct=False):
    """f: (B, 2^n) of +-1. Returns dict of per-function arrays."""
    Bt = f.shape[0]
    N = 1 << n
    fh = wht(f, n)
    mu = fh * fh
    pop = np.array([bin(s).count("1") for s in range(N)], dtype=np.float64)
    H = eta(mu).sum(axis=1)
    I = (mu * pop).sum(axis=1)
    E = np.zeros((Bt, n))
    J = np.zeros((Bt, n))
    D = np.zeros((Bt, n))
    Gi = np.zeros((Bt, n))
    Inf = np.zeros((Bt, n))
    res_direct = 0.0
    for i in range(n):
        v = fh.reshape(Bt, N >> (i + 1), 2, 1 << i)
        a = v[:, :, 0, :].reshape(Bt, -1)
        b = v[:, :, 1, :].reshape(Bt, -1)
        a2, b2 = a * a, b * b
        m = a2 + b2
        ok = m > 1e-300
        ms = np.where(ok, m, 1.0)
        E[:, i] = (m * h2(np.where(ok, b2 / ms, 0.0))).sum(axis=1)
        t = np.where(ok, 2 * a * b / ms, 0.0)
        J[:, i] = (m * (1.0 - h2((1.0 + t) / 2.0))).sum(axis=1)
        Hp = eta((a + b) ** 2).sum(axis=1)
        Hn = eta((a - b) ** 2).sum(axis=1)
        D[:, i] = H - 0.5 * Hp - 0.5 * Hn
        Inf[:, i] = b2.sum(axis=1)
        okb = b2 > 1e-300
        Gi[:, i] = (b2 * np.log2(1.0 + np.where(okb, a2 / np.where(okb, b2, 1.0), 0.0))).sum(axis=1)
        if direct:
            # restrict the truth table itself and transform on n-1 variables
            g = f.reshape(Bt, N >> (i + 1), 2, 1 << i)
            gp = g[:, :, 0, :].reshape(Bt, -1)      # x_i bit 0  <->  x_i = +1
            gn = g[:, :, 1, :].reshape(Bt, -1)
            hp = eta(wht(gp, n - 1) ** 2).sum(axis=1)
            hn = eta(wht(gn, n - 1) ** 2).sum(axis=1)
            res_direct = max(res_direct, float(np.abs(H - 0.5 * hp - 0.5 * hn - D[:, i]).max()))
    live = Inf > 1e-12
    big = 1e18
    rD = np.where(live, D / np.where(live, Inf, 1.0), big)
    rE = np.where(live, E / np.where(live, Inf, 1.0), big)
    rJ = np.where(live, J / np.where(live, Inf, 1.0), 0.0)
    top = Inf >= Inf.max(axis=1, keepdims=True) - 1e-12
    out = {
        "H": H, "I": I, "Hm": E.sum(axis=1), "J": J.sum(axis=1), "Psi": D.sum(axis=1), "G": Gi.sum(axis=1),
        "rD": rD.min(axis=1), "rE": rE.min(axis=1),
        "rmaxD": np.where(top, rD, big).min(axis=1), "rmaxE": np.where(top, rE, big).min(axis=1),
        "rJmax": rJ.max(axis=1), "rDmax": np.where(live, rD, 0.0).max(axis=1),
        "maxInf": Inf.max(axis=1),
        "res_split": float(np.abs(D - E - J).max()),
        "res_direct": res_direct,
    }
    return out


KEYS = [("H/I", lambda o: o["H"] / o["I"]),
        ("Hm/I", lambda o: o["Hm"] / o["I"]),
        ("Psi/I", lambda o: o["Psi"] / o["I"]),
        ("G/I", lambda o: o["G"] / o["I"]),
        ("J/I", lambda o: o["J"] / o["I"]),
        ("best coord D_i/Inf_i", lambda o: o["rD"]),
        ("best coord E_i/Inf_i", lambda o: o["rE"]),
        ("max-inf coord D_i/Inf_i", lambda o: o["rmaxD"]),
        ("max-inf coord E_i/Inf_i", lambda o: o["rmaxE"]),
        ("worst coord D_i/Inf_i", lambda o: o["rDmax"]),
        ("worst coord J_i/Inf_i", lambda o: o["rJmax"])]


class Acc:
    def __init__(self):
        self.best = {}
        self.viol = {"Hm<=H": 0.0, "G<=Hm": 0.0, "Hm<=G+I/ln2": 0.0, "J_i<=(2/ln2)Inf_i": 0.0,
                     "split": 0.0, "direct": 0.0}
        self.count = 0

    def add(self, o, tag):
        nz = o["I"] > 1e-12
        self.count += int(nz.sum())
        I = np.where(nz, o["I"], 1.0)
        o = dict(o)
        o["I"] = I
        for name, fn in KEYS:
            v = np.where(nz, fn(o), -1.0)
            j = int(np.argmax(v))
            if name not in self.best or v[j] > self.best[name][0]:
                self.best[name] = (float(v[j]), tag(j), float(o["I"][j]), float(o["H"][j]), float(o["maxInf"][j]))
        self.viol["Hm<=H"] = max(self.viol["Hm<=H"], float((o["Hm"] - o["H"]).max()))
        self.viol["G<=Hm"] = max(self.viol["G<=Hm"], float((o["G"] - o["Hm"]).max()))
        self.viol["Hm<=G+I/ln2"] = max(self.viol["Hm<=G+I/ln2"], float(np.where(nz, o["Hm"] - o["G"] - I / LN2, -1).max()))
        self.viol["J_i<=(2/ln2)Inf_i"] = max(self.viol["J_i<=(2/ln2)Inf_i"], float(o["rJmax"].max() - 2 / LN2))
        self.viol["split"] = max(self.viol["split"], o["res_split"])
        self.viol["direct"] = max(self.viol["direct"], o["res_direct"])

    def report(self, title):
        print(title + "   (%d nonconstant functions)" % self.count)
        for name, _ in KEYS:
            v, tag, I, H, mi = self.best[name]
            print("  sup %-26s = %10.6f   at %s  I=%.5f H=%.5f maxInf=%.5f" % (name, v, tag, I, H, mi))
        print("  identity residuals: D=E+J %.2e ; D by actual restriction %.2e" % (self.viol["split"], self.viol["direct"]))
        print("  largest value of (lhs - rhs), must be <= 0 up to rounding:")
        for k in ("Hm<=H", "G<=Hm", "Hm<=G+I/ln2", "J_i<=(2/ln2)Inf_i"):
            print("     %-20s %+.3e" % (k, self.viol[k]))
        sys.stdout.flush()


def from_codes(codes, n):
    N = 1 << n
    c = np.asarray(codes, dtype=np.uint64)
    return 1.0 - 2.0 * ((c[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)


def census4():
    acc = Acc()
    for start in range(0, 1 << 16, 8192):
        idx = np.arange(start, start + 8192, dtype=np.uint64)
        acc.add(stats(from_codes(idx, 4), 4, direct=True), lambda j: "tt=0x%04x" % int(idx[j]))
    acc.report("n=4 census, all 65536 truth tables")


def fromfile(path, n):
    acc = Acc()
    codes = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                codes.append(int(line, 16))
    codes = np.array(codes, dtype=np.uint64)
    for start in range(0, len(codes), 8192):
        c = codes[start:start + 8192]
        acc.add(stats(from_codes(c, n), n, direct=(start == 0)), lambda j: "tt=0x%0*x" % (1 << (n - 2), int(c[j])))
    acc.report("file %s, n=%d, %d truth tables" % (path, n, len(codes)))


def sample(n, count, seed):
    N = 1 << n
    rng = np.random.default_rng(seed)
    acc = Acc()
    done = 0
    bs = max(16, min(8192, (1 << 21) // N))
    while done < count:
        b = min(bs, count - done)
        dens = rng.choice([0.5, 0.3, 0.15, 0.05], size=(b, 1))
        bits = rng.random((b, N)) < dens
        keep = bits.copy()
        acc.add(stats(1.0 - 2.0 * bits.astype(np.float64), n, direct=(done == 0)),
                lambda j: "bits=" + ("".join("1" if x else "0" for x in keep[j]) if N <= 64 else "(n=%d)" % n))
        done += b
    acc.report("n=%d sample of %d (seed %d, densities 0.5/0.3/0.15/0.05)" % (n, count, seed))


def fam(nmax):
    def pts(n):
        return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)

    rows = []
    for n in range(2, nmax + 1, 2):
        rows.append(("AND_%d" % n, n, np.where(pts(n).all(axis=1), -1.0, 1.0)))
    for n in range(3, nmax + 1, 2):
        rows.append(("MAJ_%d" % n, n, np.where(pts(n).sum(axis=1) * 2 > n, -1.0, 1.0)))
    for n in range(4, nmax + 1, 2):
        b = pts(n)
        for t in (1, 2, n // 2 - 1):
            if 1 <= t < n // 2 + 1:
                rows.append(("BALL_%d_%d" % (n, t), n, np.where(b.sum(axis=1) >= n - t, -1.0, 1.0)))
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
    for k in range(2, nmax, 2):
        # bent inner product on k variables, one point replaced by a fresh dictator (FLOW 7(h))
        if k + 1 <= nmax:
            b = pts(k + 1)
            ip = (b[:, 0:k:2] * b[:, 1:k:2]).sum(axis=1) % 2
            f = 1.0 - 2.0 * ip
            star = (b[:, :k] == 0).all(axis=1)
            f = np.where(star, 1.0 - 2.0 * b[:, k], f)
            rows.append(("BENTPT_%d" % k, k + 1, f))
    for k in range(2, nmax + 1, 2):
        b = pts(k)
        ip = (b[:, 0:k:2] * b[:, 1:k:2]).sum(axis=1) % 2
        rows.append(("BENT_%d" % k, k, 1.0 - 2.0 * ip))
    print("%-13s %7s %7s %7s %7s %7s %7s | %8s %8s %8s %8s" % ("f", "I", "H/I", "Hm/I", "Psi/I", "G/I", "J/I",
          "bestD", "maxinfD", "worstD", "maxInf"))
    for name, n, f in rows:
        o = stats(f[None, :].astype(np.float64), n)
        I = float(o["I"][0])
        print("%-13s %7.4f %7.4f %7.4f %7.4f %7.4f %7.4f | %8.4f %8.4f %8.4f %8.5f" % (
            name, I, o["H"][0] / I, o["Hm"][0] / I, o["Psi"][0] / I, o["G"][0] / I, o["J"][0] / I,
            o["rD"][0], o["rmaxD"][0], o["rDmax"][0], o["maxInf"][0]), flush=True)


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "census4":
        census4()
    elif m == "file":
        fromfile(sys.argv[2], int(sys.argv[3]))
    elif m == "sample":
        sample(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        fam(int(sys.argv[2]) if len(sys.argv) > 2 else 14)
