"""Structured / adversarial LTF families at n = 14..22: every lemma, exactly.

usage: python attack_structured.py N [pointwise_every]
"""
import math, sys, json, time
import numpy as np
import ltf_ref as L

L.be_polite()
n = int(sys.argv[1])
pw_every = int(sys.argv[2]) if len(sys.argv) > 2 else 0   # 0: no pointwise
rng = np.random.default_rng(12345 + n)


def thetas_from_quantiles(w, alphas):
    v = np.sort(L.linear_values(w).astype(np.float64))
    out = []
    for a in alphas:
        k = min(len(v) - 1, max(0, int(round(a * len(v)))))
        t = v[k]
        out.append(float(t))                        # theta equal to an attained value (sgn(0) bites)
        nxt = v[min(len(v) - 1, k + 1)]
        if nxt > t:
            out.append(float((t + nxt) / 2))        # theta strictly between values
    return sorted(set(out))


ALPHAS = [0.5, 0.25, 0.75, 1 / 16, 15 / 16, 2 ** -8, 1 - 2 ** -8, 2 ** -12, 1 - 2 ** -12,
          2 ** -(n - 2), 1 - 2 ** -(n - 2), 3 / 2 ** n, 1 - 3 / 2 ** n]

families = []
# 1. majority / symmetric thresholds (integer, all ties)
w = [1] * n
for t in range(-n, n + 1):
    families.append(("sym", w, t))
# 2. geometric weights (float)
for q in [0.5, 0.55, 0.62, 0.7, 0.8, 0.9, 0.95, 0.99]:
    w = [q ** j for j in range(n)]
    for t in thetas_from_quantiles(w, ALPHAS):
        families.append((f"geom{q}", w, t))
# 3. integer near-ties: M + j, and M*(1+small)
for M in [10 ** 6, 3 * n, n]:
    w = [M + j for j in range(n)]
    for t in thetas_from_quantiles(w, ALPHAS):
        families.append((f"neartie{M}", w, int(round(t))))
# 4. one huge weight on top of ones
for Hh in sorted(set([2, 3, n // 4, n // 2, n - 3, n - 2, n - 1, n, n + 1])):
    w = [Hh] + [1] * (n - 1)
    for t in range(-(Hh + n - 1), Hh + n, 1):
        families.append((f"huge{Hh}", w, t))
# 5. heavy block + many tiny distinct weights (ties in the heavy block broken by tiny ones)
for m in [2, 4, 6, n // 2]:
    w = [10 ** 6] * m + [j + 1 for j in range(n - m)]
    for t in thetas_from_quantiles(w, ALPHAS) + [0, 1, -1]:
        families.append((f"heavytiny{m}", w, int(round(t))))
# 6. fibonacci, powers of 2 and 3
fib = [1, 2]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
for name, w in [("fib", fib[::-1][:n]), ("pow2", [2 ** (n - 1 - j) for j in range(n)]),
                ("pow3", [3 ** (n - 1 - j) for j in range(n)] if n <= 30 else None)]:
    if w is None:
        continue
    for t in thetas_from_quantiles(w, ALPHAS):
        families.append((name, w, int(round(t))))
# 7. random weights
for dist in ["gauss", "exp", "cauchy", "logunif", "powlaw1", "powlaw2"]:
    for rep in range(3):
        if dist == "gauss":
            w = list(rng.normal(size=n))
        elif dist == "exp":
            w = list(rng.exponential(size=n))
        elif dist == "cauchy":
            w = list(rng.standard_cauchy(size=n))
        elif dist == "logunif":
            w = list(np.exp(rng.uniform(-8, 0, size=n)))
        elif dist == "powlaw1":
            w = [j ** -1.0 for j in range(1, n + 1)]
        else:
            w = [j ** -0.5 for j in range(1, n + 1)]
        for t in thetas_from_quantiles(w, ALPHAS):
            families.append((f"{dist}{rep}", w, t))

stride = int(sys.argv[3]) if len(sys.argv) > 3 else 1
if stride > 1:   # keep every stride-th function of each family group, plus both ends
    families = [f for idx_f, f in enumerate(families) if idx_f % stride == 0 or f[0] == "sym"]
print(f"n={n}: {len(families)} functions (stride {stride})", flush=True)
worst = {}
keys = ["L2avg", "L3", "L3tail", "L3tail_mid", "L4", "L5", "L6", "T1", "HI"]
pkeys = ["pw_a", "pw_b", "pw_c"]

def dump(tag):
    print(f"--- {tag}: distinct functions so far {count}, time {time.time() - t0:.1f}s", flush=True)
    for kk in keys + pkeys:
        if kk in worst:
            v, fam, tt, arg = worst[kk]
            print(f"  worst {kk:10s} = {v:.9f}   family={fam} theta={tt} arg={arg}", flush=True)

t0 = time.time()
seen = set()
count = 0
for fi, (name, w, t) in enumerate(families):
    tab = L.ltf_table(w, t)
    hsh = hash(tab.tobytes())
    if hsh in seen:
        continue
    seen.add(hsh)
    count += 1
    sp = L.Spec(tab)
    if sp.I < 1e-15:
        continue
    absw = [abs(x) for x in w]
    out = L.lemma_checks(sp, absw)
    fam = name
    for k in keys:
        v = float(out.get(k, 0.0))
        if k not in worst or v > worst[k][0]:
            worst[k] = (v, fam, t, str(out.get(k + "_arg")))
    if count % 25 == 0:
        dump('progress')
    if pw_every and (count % pw_every == 0):
        r, U, N = L.ranks_and_U(absw)
        inf = sp.influences()
        for i in range(n):
            if inf[i] < 1e-15 or N[i] < 2:
                continue
            cs = sorted(set([c for c in [0.5, 1.0, 2.0, 3.0, 4.0, N[i] / 4, N[i] / 2, 0.75 * N[i], N[i]] if 0 < c <= N[i]]))
            for (c, maxP, ra, rb, rc) in L.lemma2_pointwise(tab, absw, i, U[i], N[i], cs):
                for kk, vv in zip(pkeys, (ra, rb, rc)):
                    if kk not in worst or vv > worst[kk][0]:
                        worst[kk] = (vv, fam, t, f"i={i} N={N[i]} c={c:.3g} maxP={maxP:.4f}")
print(f"distinct functions: {count}, time {time.time() - t0:.1f}s")
for k in keys + pkeys:
    if k in worst:
        v, fam, t, arg = worst[k]
        print(f"  worst {k:10s} = {v:.6f}   family={fam} theta={t} arg={arg}")
with open(f"../logs/structured_n{n}.json", "w", encoding="utf-8") as fh:
    json.dump({k: list(map(str, v)) for k, v in worst.items()}, fh, indent=1)
