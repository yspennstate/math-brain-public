"""Numerical checks for "The mode of classical and free Brownian motion at large time".

For a few initial laws (atomic, so every quantity is a finite sum) this script

1. finds the GLOBAL maximizer of the density of mu * N(0, t) by a grid scan
   over [m - 6 sqrt(t), m + 6 sqrt(t)] followed by Newton refinement,
2. finds the GLOBAL maximizer of the density of mu boxplus S(0, t) through
   Biane's parametrization: R(u) solves E[1 / (R + (u - X)^2)] = 1/t, the
   density at psi(u) = u + t E[(u - X) / (R + (u - X)^2)] equals sqrt(R)/(pi t);
   R(u) is scanned on a grid and the best point is refined by Newton,
3. compares both modes with the two-term expansions of Theorems 1.1 and 1.2
   (the scaled error t^3 (mode - expansion) should stay bounded; the script
   checks that it does not grow between t = 800 and t = 1600),
4. checks the explicit bounds |M_c - m| <= M_3 / t (Theorem 3.1) and
   |M_f - m| <= 64 (B^3 + M_3) / t, |u*| <= B (Theorem 2.1) at times above
   the stated thresholds, and that the free density has a single local
   maximum on the scan grid above the threshold 7A (below it two local
   maxima can occur, as for the "outlier" law at t = 50 and 100).

Writes checks.json next to this file. Needs mpmath.
"""
import json
import pathlib

import mpmath as mp

mp.mp.dps = 40
ROOT = pathlib.Path(__file__).resolve().parent

LAWS = {
    "skew_two_point": ([-1, 2], [mp.mpf(2) / 3, mp.mpf(1) / 3]),
    "three_point": ([-1, mp.mpf("0.5"), 3], [mp.mpf("0.5"), mp.mpf("0.35"), mp.mpf("0.15")]),
    "outlier": ([0, 1, 12], [mp.mpf("0.8"), mp.mpf("0.19"), mp.mpf("0.01")]),
    "symmetric": ([-2, 0, 2], [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.25")]),
}


def moments(x, p):
    m = sum(a * w for a, w in zip(x, p))
    y = [mp.mpf(a) - m for a in x]
    mu = {k: sum(w * b ** k for b, w in zip(y, p)) for k in range(2, 8)}
    M3 = sum(w * abs(b) ** 3 for b, w in zip(y, p))
    return m, y, mu, M3


def classical_mode(y, p, t):
    """Global maximizer of E exp(-(h - Y)^2 / (2t)) over h (Y centered)."""
    f = lambda h: sum(w * mp.exp(-(h - b) ** 2 / (2 * t)) for b, w in zip(y, p))
    g = lambda h: sum(w * (b - h) * mp.exp(-(h - b) ** 2 / (2 * t)) for b, w in zip(y, p))
    L = 6 * mp.sqrt(t)
    N = 2400
    grid = [-L + 2 * L * k / N for k in range(N + 1)]
    vals = [f(h) for h in grid]
    k = max(range(len(vals)), key=lambda i: vals[i])
    peaks = sum(1 for i in range(1, N) if vals[i] > vals[i - 1] and vals[i] >= vals[i + 1])
    return mp.findroot(g, grid[k]), peaks


def free_R(y, p, t, u):
    """Squared height R(u) >= 0 in Biane's parametrization (bisection)."""
    F = lambda R: sum(w / (R + (u - b) ** 2) for b, w in zip(y, p)) - 1 / t
    lo, hi = mp.mpf(10) ** -30, mp.mpf(t)
    if F(lo) <= 0:
        return mp.mpf(0)
    for _ in range(200):
        mid = (lo + hi) / 2
        if F(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def free_mode(y, p, t):
    """Global maximizer of the free density; returns (mode, u*, R*, peaks)."""
    B = 4 * mp.sqrt(t)
    N = 1600
    grid = [-B + 2 * B * k / N for k in range(N + 1)]
    old = mp.mp.dps
    mp.mp.dps = 20
    vals = [free_R(y, p, t, u) for u in grid]
    mp.mp.dps = old
    k = max(range(len(vals)), key=lambda i: vals[i])
    peaks = sum(1 for i in range(1, N) if vals[i] > vals[i - 1] and vals[i] >= vals[i + 1])
    eqs = lambda u, R: (
        sum(w / (R + (u - b) ** 2) for b, w in zip(y, p)) - 1 / t,
        sum(w * (u - b) / (R + (u - b) ** 2) ** 2 for b, w in zip(y, p)),
    )
    u, R = mp.findroot(eqs, (grid[k], vals[k]))
    mode = u + t * sum(w * (u - b) / (R + (u - b) ** 2) for b, w in zip(y, p))
    return mode, u, R, peaks


def expansions(mu, t):
    v, m3, m5 = mu[2], mu[3], mu[5]
    c = -m3 / (2 * t) + (m5 - 6 * v * m3) / (8 * t ** 2)
    f = -3 * m3 / t + (5 * m5 - 22 * v * m3) / t ** 2
    return c, f


def main():
    out = {"asymptotics": [], "bounds": [], "near_threshold": []}
    for name, (x, p) in LAWS.items():
        m, y, mu, M3 = moments(x, p)
        v = mu[2]
        A7 = 7 * (7 + 4 * mp.sqrt(2)) * v
        scaled = []
        for t in [100, 200, 400, 800, 1600]:
            t = mp.mpf(t)
            hc, pc = classical_mode(y, p, t)
            hf, u, R, pf = free_mode(y, p, t)
            ec, ef = expansions(mu, t)
            row = {
                "law": name, "t": int(t),
                "classical_mode_minus_mean": mp.nstr(hc, 15),
                "free_mode_minus_mean": mp.nstr(hf, 15),
                "classical_error_times_t3": mp.nstr((hc - ec) * t ** 3, 6),
                "free_error_times_t3": mp.nstr((hf - ef) * t ** 3, 6),
                "classical_local_maxima_on_grid": pc,
                "free_local_maxima_on_grid": pf,
            }
            out["asymptotics"].append(row)
            print("asym", row, flush=True)
            assert pc == 1
            if t > A7:
                assert pf == 1
            scaled.append(((hc - ec) * t ** 3, (hf - ef) * t ** 3))
            if name == "symmetric":
                assert abs(hc) < mp.mpf(10) ** -20 and abs(hf) < mp.mpf(10) ** -20

        (c1, f1), (c2, f2) = scaled[-2], scaled[-1]
        assert abs(c2) <= 1.25 * abs(c1) + 1e-6 and abs(f2) <= 1.25 * abs(f1) + 1e-6
        B = (mp.sqrt(2) + 2) * mp.sqrt(v)
        A = B ** 2 + v
        eps = mp.mpf("0.05")
        alpha_c = sum(w * mp.exp(eps / 2 * b ** 2) for b, w in zip(y, p))
        Tc = 36 * mp.log(2 * alpha_c) / (eps / 2)
        for t in [Tc, 2 * Tc, 7 * A * mp.mpf("1.001"), 20 * A]:
            hc, _ = classical_mode(y, p, t)
            hf, u, R, pf = free_mode(y, p, t)
            row = {"law": name, "t": mp.nstr(t, 8)}
            if t >= Tc:
                row["classical_bound_ok"] = bool(abs(hc) <= M3 / t)
                row["classical_ratio"] = mp.nstr(abs(hc) * t / M3, 6)
                assert row["classical_bound_ok"]
            if t > 7 * A:
                row["free_bound_ok"] = bool(abs(hf) <= 64 * (B ** 3 + M3) / t)
                row["free_ratio"] = mp.nstr(abs(hf) * t / (64 * (B ** 3 + M3)), 6)
                row["u_star_within_B"] = bool(abs(u) <= B)
                row["R_star_at_least_t_minus_v"] = bool(R >= t - v)
                assert row["free_bound_ok"] and row["u_star_within_B"] and row["R_star_at_least_t_minus_v"]
            out["bounds"].append(row)
            print("bound", row, flush=True)

        t = 7 * A * mp.mpf("1.0001")
        _, _, _, pf = free_mode(y, p, t)
        out["near_threshold"].append({"law": name, "t": mp.nstr(t, 8), "free_local_maxima_on_grid": pf})
        assert pf == 1
        print("threshold", name, "single free peak at t = 7A(1+1e-4)", flush=True)

    (ROOT / "checks.json").write_text(json.dumps(out, indent=2), encoding="utf8")
    print("all checks passed", flush=True)


if __name__ == "__main__":
    main()
