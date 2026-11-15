"""Numeric check of FLOW.md section 5 and first tables for WC, Phi(u), the sparse split, Conjectures T and W.

Notation: mu(S) = fhat(S)^2, up(S) = E (D_S f)^2 = sum_{U>=S} mu(U), p(S) = P[D_S f != 0], alpha(S) = E|D_S f|.
  H = sum mu log2(1/mu), A = sum mu log2(1/up), B = H - A, P = sum mu log2(1/p)
  w(S) = mu(S)/up(S), Z_U = sum_{S<=U} w(S);  Kraft: sum_U mu(U) Z_U = 1
  B = Hc - DZ with Hc = E_nu log2(Z_U/w(S)), DZ = sum_U mu(U) Z_U log2 Z_U
  Phi(u) = sum_S mu(S) log2(1/N_u(S)), N_u(S) = sum_{U>=S} mu(U) u^|U-S|; Phi(0)=H, Phi(1)=A,
           Gibbs: H <= Phi(u) + I log2(1/(1-u))
  WC = sum mu(S) up(S);  LWC = log2(1/WC)
  Sp_K = sum over S with p(S) < 2^(-K|S|) of mu(S) log2(1/p(S));  P <= K I + Sp_K
  T_t = E log2(1/p(R_t)), R_t = t-thinning of S ~ mu  (T_1 = P)
  W_c = sum_{S nonempty} mu(S) c^(-|S|)/up(S);  LW_c = log2(W_c/Var) / (I/Var)   (Conjecture W: bounded)
Usage: python check_sec5.py census4        all 65536 functions on 4 variables (sup of each ratio, identities)
       python check_sec5.py fam [nmax]     families: AND, majority, tribes, address, up to nmax variables (default 14)
"""
import sys
import numpy as np

TINY = 1e-300


def wht(a, n):
    N = 1 << n
    a = a.copy()
    h = 1
    while h < N:
        a = a.reshape(a.shape[0], N // (2 * h), 2, h)
        a = np.stack([a[:, :, 0, :] + a[:, :, 1, :], a[:, :, 0, :] - a[:, :, 1, :]], axis=2).reshape(-1, N)
        h *= 2
    return a / N


def zeta_sup(a, n):
    """b[S] = sum over U containing S of a[U], along the last axis."""
    N = 1 << n
    b = a.copy()
    for i in range(n):
        b = b.reshape(b.shape[0], N >> (i + 1), 2, 1 << i)
        b[:, :, 0, :] += b[:, :, 1, :]
        b = b.reshape(-1, N)
    return b


def zeta_sub(a, n):
    N = 1 << n
    b = a.copy()
    for i in range(n):
        b = b.reshape(b.shape[0], N >> (i + 1), 2, 1 << i)
        b[:, :, 1, :] += b[:, :, 0, :]
        b = b.reshape(-1, N)
    return b


def deriv_stats(f, n):
    """p(S), alpha(S), E g_S^2 for every S; f has shape (batch, 2^n). Work 3^n per function."""
    Bt = f.shape[0]
    N = 1 << n
    p = np.zeros((Bt, N))
    al = np.zeros((Bt, N))
    u2 = np.zeros((Bt, N))
    stack = [(f.reshape(Bt, 1, N), n, 0)]
    while stack:
        g, m, S = stack.pop()
        if m == 0:
            g = g[:, :, 0]
            p[:, S] = (np.abs(g) > 1e-12).mean(axis=1)
            al[:, S] = np.abs(g).mean(axis=1)
            u2[:, S] = (g * g).mean(axis=1)
            continue
        K = g.shape[1]
        h = g.reshape(Bt, K, 2, 1 << (m - 1))
        stack.append(((h[:, :, 0, :] - h[:, :, 1, :]) / 2.0, m - 1, S | (1 << (m - 1))))
        stack.append((h.reshape(Bt, 2 * K, 1 << (m - 1)), m - 1, S))
    return p, al, u2


def lg(x):
    return np.log2(np.maximum(x, TINY))


def analyse(f, n):
    N = 1 << n
    pop = np.array([bin(s).count("1") for s in range(N)], dtype=np.float64)
    fh = wht(f, n)
    mu = fh * fh
    up = zeta_sup(mu, n)
    p, al, u2 = deriv_stats(f, n)
    out = {}
    out["err_up"] = np.abs(up - u2).max(axis=1)
    pos = mu > 1e-15
    I = (mu * pop).sum(axis=1)
    Var = 1.0 - mu[:, 0]
    H = -(mu * np.where(pos, lg(mu), 0)).sum(axis=1)
    A = -(mu * np.where(pos, lg(up), 0)).sum(axis=1)
    P = -(mu * np.where(pos, lg(p), 0)).sum(axis=1)
    B = H - A
    w = np.where(pos, mu / np.maximum(up, TINY), 0.0)
    Z = zeta_sub(w, n)
    out["err_kraft"] = np.abs((mu * Z).sum(axis=1) - 1.0)
    # nu(S,U) = mu(U) w(S) for S <= U: E_nu log2 Z_U = sum_U mu(U) Z_U log2 Z_U; E_nu log2(1/w(S)) = sum_S w(S) up(S) log2(1/w) = B
    DZ = (mu * Z * np.where(pos, lg(Z), 0)).sum(axis=1)
    Bnu = -(w * up * np.where(pos, lg(w), 0)).sum(axis=1)
    out["err_B"] = np.abs(Bnu - B)
    Hc = DZ + Bnu
    out["Hc"], out["DZ"] = Hc, DZ
    out["I"], out["Var"], out["H"], out["A"], out["B"], out["P"] = I, Var, H, A, B, P
    # noise form
    for u in (0.25, 0.5, 0.75):
        Nu = zeta_sup(mu * u ** pop, n) / u ** pop
        Phi = -(mu * np.where(pos, lg(Nu), 0)).sum(axis=1)
        out["Phi%g" % u] = Phi
        out["gibbs_slack%g" % u] = Phi + I * np.log2(1.0 / (1.0 - u)) - H      # must be >= 0
        out["mono%g" % u] = np.minimum(H - Phi, Phi - A)                         # must be >= 0
    WC = (mu * up).sum(axis=1)
    out["LWC"] = -lg(WC)
    for K in (1, 2, 3, 4, 6):
        sparse = pos & (p < 2.0 ** (-K * pop) * (1 - 1e-12))
        out["Sp%d" % K] = -(mu * np.where(sparse, lg(p), 0)).sum(axis=1)
    cp = np.where(p > 0, -lg(p), 0.0)          # log2(1/p(R)); p(R) = 0 only where up(R) = 0, weight 0
    for t in (0.25, 0.5, 0.75):
        zs = zeta_sup(mu * (1 - t) ** pop, n) / (1 - t) ** pop
        out["T%g" % t] = (cp * t ** pop * zs).sum(axis=1)
    for c in (2.0, 4.0):
        Wc = (np.where(pos, mu / np.maximum(up, TINY), 0.0) * c ** (-pop))[:, 1:].sum(axis=1)
        with np.errstate(divide="ignore", invalid="ignore"):
            out["LW%g" % c] = np.where(Var > 1e-12, lg(Wc / np.maximum(Var, TINY)) / (I / np.maximum(Var, TINY)), 0.0)
    return out


RAT = ["H", "A", "B", "P", "Hc", "LWC", "Phi0.25", "Phi0.5", "Phi0.75", "Sp1", "Sp2", "Sp3", "Sp4", "Sp6",
       "T0.25", "T0.5", "T0.75"]


def census4():
    n, N = 4, 16
    best = {}
    errs = {"err_up": 0.0, "err_kraft": 0.0, "err_B": 0.0}
    mins = {}
    for start in range(0, 1 << N, 8192):
        idx = np.arange(start, start + 8192, dtype=np.uint64)
        f = 1.0 - 2.0 * ((idx[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)
        o = analyse(f, n)
        ok = o["I"] > 1e-12
        for k in errs:
            errs[k] = max(errs[k], float(o[k].max()))
        for k in o:
            if k.startswith("gibbs") or k.startswith("mono"):
                mins[k] = min(mins.get(k, 1e9), float(o[k].min()))
        for k in RAT + ["LW2", "LW4"]:
            v = o[k] if k.startswith("LW") and k != "LWC" else np.where(ok, o[k] / np.maximum(o["I"], TINY), -1)
            j = int(np.argmax(v))
            if k not in best or v[j] > best[k][0]:
                best[k] = (float(v[j]), int(idx[j]), float(o["I"][j]), float(o["Var"][j]))
        # balanced: ratio to I - 1 is not used here; LWC/(I) only
    print("n=4 census, 65536 functions")
    print("identity errors (max):", {k: "%.2e" % v for k, v in errs.items()})
    print("minima (must be >= 0 up to rounding):", {k: "%.3e" % v for k, v in mins.items()})
    print("sup of X/I (LW_c is its own ratio):")
    for k in RAT + ["LW2", "LW4"]:
        v, tt, I, Var = best[k]
        print("  %-8s %.6f   tt=0x%04x  I=%.4f Var=%.4f" % (k, v, tt, I, Var))


def families(nmax):
    def pts(n):
        return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)       # bits, 1 = "true"

    rows = []
    for n in range(2, nmax + 1):
        b = pts(n)
        rows.append(("AND_%d" % n, n, np.where(b.all(axis=1), -1.0, 1.0)))
    for n in range(3, nmax + 1, 2):
        b = pts(n)
        rows.append(("MAJ_%d" % n, n, np.where(b.sum(axis=1) * 2 > n, -1.0, 1.0)))
    for w in (2, 3, 4):
        for s in range(2, 9):
            n = w * s
            if n > nmax:
                continue
            b = pts(n).reshape(-1, s, w)
            rows.append(("TRIBES_%dx%d" % (w, s), n, np.where(b.all(axis=2).any(axis=1), -1.0, 1.0)))
    for k in (1, 2, 3):
        n = k + (1 << k)
        if n > nmax:
            continue
        b = pts(n)
        addr = (b[:, :k] * (1 << np.arange(k))[None, :]).sum(axis=1)
        rows.append(("ADDR_%d" % k, n, 1.0 - 2.0 * b[np.arange(1 << n), k + addr]))
    cols = ["I", "Var"] + RAT + ["LW2", "LW4"]
    print("%-12s %7s %6s " % ("f", "I", "Var") + " ".join("%7s" % c[:7] for c in RAT + ["LW2", "LW4"]))
    for name, n, f in rows:
        o = analyse(f[None, :].astype(np.float64), n)
        I = float(o["I"][0])
        vals = [float(o[k][0]) / I for k in RAT] + [float(o["LW2"][0]), float(o["LW4"][0])]
        bad = [k for k in o if (k.startswith("gibbs") or k.startswith("mono")) and o[k][0] < -1e-9]
        e = max(float(o["err_up"][0]), float(o["err_kraft"][0]), float(o["err_B"][0]))
        print("%-12s %7.4f %6.4f " % (name, I, float(o["Var"][0])) + " ".join("%7.3f" % v for v in vals)
              + ("  ERR %.1e" % e if e > 1e-9 else "") + ("  VIOL " + ",".join(bad) if bad else ""), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "census4":
        census4()
    else:
        families(int(sys.argv[2]) if len(sys.argv) > 2 else 14)
