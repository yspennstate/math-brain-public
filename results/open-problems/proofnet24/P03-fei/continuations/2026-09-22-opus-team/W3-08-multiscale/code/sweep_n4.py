"""Exhaustive multiscale survey over all 65,536 Boolean functions of four variables (covers n <= 3
through dummy coordinates, which leave every quantity below unchanged).

For every f and every mask J the exact E_x H(f_{J,x}) and H(S cap J) are computed (mslib.restr_profile).
Reported maxima over f:
  H/I;  kappa_delta = (H - E H(f_{J,x}))/((1-delta) I) on a grid of delta;  its mixing and location parts;
  rho0 = min_i Delta_i/Inf_i (existential coordinate step) and sum_i Delta_i / I (averaged coordinate step);
  existential block step with |J^c| = m: min_J (H - E_x H(f_{J,x})) / sum_{i not in J} Inf_i;
  candidate H <= alpha E H(f_{J,x}) + beta I at delta = 1/2: least beta and the implied constant beta/(1-alpha/2).
"""
import sys, os, json
import numpy as np
import numba as nb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mslib import polite, fwht, entropy_bits, influences, restr_profile

polite()
n = 4
N = 1 << n
NF = 1 << N


@nb.njit(cache=True)
def run_all():
    EHa = np.zeros((NF, N))
    HTa = np.zeros((NF, N))
    Ha = np.zeros(NF)
    INF = np.zeros((NF, n))
    tt = np.empty(N, dtype=np.int64)
    for code in range(NF):
        for x in range(N):
            tt[x] = -1 if (code >> x) & 1 else 1
        fh = fwht(tt)
        p = fh * fh
        Ha[code] = entropy_bits(p)
        INF[code] = influences(fh, n)
        EH, HT = restr_profile(tt, n, True)
        EHa[code] = EH
        HTa[code] = HT
    return EHa, HTa, Ha, INF


EHa, HTa, Ha, INF = run_all()
Ia = INF.sum(axis=1)
pc = np.array([bin(J).count("1") for J in range(N)])
nz = Ia > 1e-12
full = N - 1
res = {}


def argmax_report(vals, name):
    v = np.where(nz, vals, -np.inf)
    k = int(np.argmax(v))
    res[name] = {"max": float(v[k]), "argmax_code": k,
                 "truth_table": [(-1 if (k >> x) & 1 else 1) for x in range(N)],
                 "H": float(Ha[k]), "I": float(Ia[k])}
    return float(v[k])


print("max H/I", argmax_report(np.where(nz, Ha / np.where(nz, Ia, 1), 0), "H_over_I"))

deltas = [0.05, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 0.99]
table = []
for d in deltas:
    w = d ** pc * (1 - d) ** (n - pc)
    EHd = EHa @ w
    HTd = HTa @ w
    D = Ha - EHd
    den = (1 - d) * np.where(nz, Ia, 1)
    kap = D / den
    Mr = (HTd - EHd) / den
    Lr = (Ha - HTd) / den
    k1 = argmax_report(kap, f"kappa_{d}")
    k2 = argmax_report(Lr, f"L_{d}")
    k3 = argmax_report(Mr, f"M_{d}")
    ratio_ML = np.max(np.where(nz & (Lr > 1e-12), Mr / np.where(Lr > 1e-12, Lr, 1), 0))
    table.append((d, k1, k2, k3, float(ratio_ML)))
    print(f"delta={d:5.2f}  max kappa={k1:.6f}  max L/((1-d)I)={k2:.6f}  max M/((1-d)I)={k3:.6f}  max M/L={ratio_ML:.4f}")

# coordinate steps
drops = np.stack([Ha - EHa[:, full & ~(1 << i)] for i in range(n)], axis=1)
with np.errstate(divide="ignore", invalid="ignore"):
    rat = np.where(INF > 1e-12, drops / INF, np.inf)
rho0 = np.min(rat, axis=1)
rho0 = np.where(np.isfinite(rho0), rho0, 0.0)
print("max rho0 (existential coordinate)", argmax_report(rho0, "rho0"))
print("max sum_i Delta_i / I (averaged coordinate)", argmax_report(drops.sum(axis=1) / np.where(nz, Ia, 1), "avgcoord"))

# existential blocks of size m
for m in range(1, n + 1):
    best = np.full(NF, np.inf)
    for J in range(N):
        if n - pc[J] != m:
            continue
        infout = sum(INF[:, i] for i in range(n) if not (J >> i) & 1)
        with np.errstate(divide="ignore", invalid="ignore"):
            r = np.where(infout > 1e-12, (Ha - EHa[:, J]) / infout, np.inf)
        best = np.minimum(best, r)
    best = np.where(np.isfinite(best), best, 0.0)
    print(f"existential block |J^c|={m}: sup_f min_J ratio =", argmax_report(best, f"exist_block_{m}"))

# candidate H <= alpha E H + beta I at delta = 1/2
d = 0.5
w = d ** pc * (1 - d) ** (n - pc)
EHd = EHa @ w
for alpha in [1.0, 1.25, 1.5, 1.75, 1.9, 1.99]:
    beta = argmax_report((Ha - alpha * EHd) / np.where(nz, Ia, 1), f"beta_alpha_{alpha}")
    print(f"alpha={alpha:5.2f}: least beta = {beta:.6f}, implied constant beta/(1-alpha/2) = {beta / (1 - alpha * d):.6f}")

# monotonicity of kappa in delta, per function
dg = np.linspace(0.02, 0.98, 49)
K = np.stack([(Ha - EHa @ (x ** pc * (1 - x) ** (n - pc))) / ((1 - x) * np.where(nz, Ia, 1)) for x in dg], axis=1)
inc = np.all(np.diff(K[nz], axis=1) >= -1e-12, axis=1).sum()
dec = np.all(np.diff(K[nz], axis=1) <= 1e-12, axis=1).sum()
print(f"functions with kappa_delta nondecreasing in delta: {inc} of {nz.sum()}; nonincreasing: {dec}")
res["monotone_counts"] = {"nondecreasing": int(inc), "nonincreasing": int(dec), "total": int(nz.sum())}
res["table"] = table
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "sweep_n4.json"), "w") as fo:
    json.dump(res, fo, indent=1)
