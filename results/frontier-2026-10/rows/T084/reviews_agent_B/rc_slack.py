"""How much does C022's injection route give away? Exact bridge-class polynomials on K_n.

For a marked pair e,f (adjacent or disjoint) on K_n, over edge sets A containing e,f with weight
q^k(A) lambda^(|A|-2), collect T, P_e, P_f, B (both bridges), J (joint bridges) as integer
coefficient tables in (k, m=|A|-2). Then on a (q, lambda) grid compare:
  R = s^2 P_e P_f + s T (J - s B)   (the true Rayleigh difference; R > 0 <=> Cov < 0)
  the route's sufficient condition J >= s B, and C022's threshold lambda >= s + sqrt(s).
"""
import itertools, json, sys
import numpy as np


def comps(n, edges):
    p = list(range(n))
    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    k = n
    for a, b in edges:
        ra, rb = f(a), f(b)
        if ra != rb:
            p[ra] = rb; k -= 1
    return k


def tables(n, pair):
    E = list(itertools.combinations(range(n), 2))
    e, f = pair
    rest = [x for x in E if x not in (e, f)]
    M = len(rest)
    shape = (n + 1, M + 1)
    T, Pe, Pf, B, J = (np.zeros(shape, dtype=object) for _ in range(5))
    for mask in range(1 << M):
        A = [rest[i] for i in range(M) if mask >> i & 1]
        m = len(A)
        k = comps(n, A + [e, f]); ke = comps(n, A + [f]); kf = comps(n, A + [e]); kef = comps(n, A)
        T[k, m] += 1
        be, bf = ke > k, kf > k
        if be: Pe[k, m] += 1
        if bf: Pf[k, m] += 1
        if be and bf: B[k, m] += 1
        if not be and not bf and kef > k: J[k, m] += 1
    return dict(T=T, Pe=Pe, Pf=Pf, B=B, J=J)


def ev(tab, q, lam):
    k = np.arange(tab.shape[0])[:, None].astype(float); m = np.arange(tab.shape[1])[None, :].astype(float)
    return float((tab.astype(float) * q ** k * lam ** m).sum())


if __name__ == "__main__":
    out = {}
    for n in [int(x) for x in sys.argv[1:]] or [5, 6]:
        for name, pair in (("adjacent", ((0, 1), (1, 2))), ("disjoint", ((0, 1), (2, 3)))):
            t = tables(n, pair)
            rows = []
            for q in (0.3, 0.5, 0.618, 0.7, 0.8, 0.9, 0.95):
                s = 1 - q
                lams = np.exp(np.linspace(np.log(1e-3), np.log(5), 400))
                Rv, Jv = [], []
                for lam in lams:
                    T_, Pe, Pf, B, J = (ev(t[x], q, lam) for x in ("T", "Pe", "Pf", "B", "J"))
                    Rv.append(s * s * Pe * Pf + s * T_ * (J - s * B)); Jv.append(J - s * B)
                Rv, Jv = np.array(Rv), np.array(Jv)
                minR = float((Rv / max(1e-300, abs(Rv).max())).min())
                thr = float(lams[np.nonzero(Jv < 0)[0].max() + 1]) if (Jv < 0).any() else 0.0
                rows.append({"q": q, "route_J>=sB_from_lambda": round(thr, 4),
                             "C022_threshold": round(s + s ** 0.5, 4), "R_positive_everywhere": bool((Rv > 0).all()),
                             "min_R_normalized": minR})
            out[f"K{n} {name}"] = rows
            print(f"K{n} {name}", json.dumps(rows), flush=True)
    json.dump(out, open("rc_slack.json", "w"), indent=1)
