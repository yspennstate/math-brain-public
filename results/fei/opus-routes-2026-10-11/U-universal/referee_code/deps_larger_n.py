"""Dependencies at larger n (random and structured functions, n = 5..8):
 (a) RM sec. 2.2 variance-local bound: Delta_i H <= Inf_i [log2(Var/Inf_i) + 6.078162672495945]   (used in C(vi))
 (b) BR channel bound: H(S_C) - E_X H(f_X) = I(X;D) <= (2/ln2) I_A   for random blocks A  (used in C(v),(viii),(ix), U-Han)
     and the identity E_X I(f_X) = I - I_A
 (c) U-Han for t in {0.25, 0.5, 0.75}, with the expectation over all (J, X) computed exactly.
"""
import itertools, json, math
import numpy as np
from rlib import Spec, restrict_tables, plogq

rng = np.random.default_rng(8)
C2 = 2 / math.log(2)
CV = 6.078162672495945


def restriction(f, n, fixed, X):
    """restrict coordinates in `fixed` to the 0/1 bits X (bit 1 = value -1); returns table on the live coords."""
    live = [i for i in range(n) if i not in fixed]
    base = sum(b << i for b, i in zip(X, fixed))
    keep = [base | sum((((y >> k) & 1) << i) for k, i in enumerate(live)) for y in range(1 << len(live))]
    return f[keep], live


def funcs():
    out = []
    for n in range(5, 9):
        for _ in range(3):
            out.append(('random', n, rng.choice([-1, 1], size=1 << n).astype(np.int64)))
        f = np.ones(1 << n, dtype=np.int64); f[rng.choice(1 << n, size=2, replace=False)] = -1
        out.append(('two-point', n, f))
        xs = np.arange(1 << n); m = n - (n % 2); q = np.zeros(1 << n, dtype=np.int64)
        for a in range(m // 2):
            q += ((xs >> (2 * a)) & 1) * ((xs >> (2 * a + 1)) & 1)
        b = (1 - 2 * (q & 1)).astype(np.int64); b[0] *= -1
        out.append(('bent+flip', n, b))
        w = rng.integers(1, 5, size=n); X = 1 - 2 * np.stack([(xs >> i) & 1 for i in range(n)], 1)
        out.append(('ltf', n, np.where(X @ w > 1, 1, -1).astype(np.int64)))
    return out


worst = dict(rm22=-1e9, channel=-1e9, EI=0.0, han=-1e9)
count = 0
for name, n, f in funcs():
    if abs(int(f.sum())) == f.size:
        continue
    count += 1
    sp = Spec.from_tables(f); H = float(sp.H()[0]); I = float(sp.I()[0]); inf = sp.infl()[0]; Var = float(sp.Var()[0])
    # (a)
    for i in range(n):
        if inf[i] <= 0:
            continue
        a = Spec.from_tables(restrict_tables(f, i, 1)); b = Spec.from_tables(restrict_tables(f, i, -1))
        dH = H - 0.5 * float(a.H()[0] + b.H()[0])
        worst['rm22'] = max(worst['rm22'], dH / (inf[i] * (math.log2(Var / inf[i]) + CV)))
    # (b) random blocks
    for _ in range(4):
        A = [i for i in range(n) if rng.random() < 0.4] or [0]
        C = [i for i in range(n) if i not in A]
        EH = 0.0; EI = 0.0
        for X in itertools.product([0, 1], repeat=len(A)):
            g, live = restriction(f, n, A, X)
            if len(live) and abs(int(g.sum())) != g.size:
                sg = Spec.from_tables(g); EH += float(sg.H()[0]); EI += float(sg.I()[0])
        EH /= 2 ** len(A); EI /= 2 ** len(A)
        # marginal of the spectral law on C
        idx = np.arange(1 << n); Cmask = sum(1 << i for i in C)
        q = np.zeros(1 << n); np.add.at(q, idx & Cmask, sp.p[0])
        HC = float(-plogq(q, q).sum())
        IA = float(sum(inf[i] for i in A))
        worst['channel'] = max(worst['channel'], (HC - EH) - C2 * IA)
        worst['EI'] = max(worst['EI'], abs(EI - (I - IA)))
        assert HC - EH >= -1e-12
    # (c) U-Han exact expectation
    for t in [0.25, 0.5, 0.75]:
        tot = 0.0
        for J in range(1 << n):
            live = [i for i in range(n) if (J >> i) & 1]; fixed = [i for i in range(n) if not (J >> i) & 1]
            w = t ** len(live) * (1 - t) ** len(fixed) / 2 ** len(fixed)
            for X in itertools.product([0, 1], repeat=len(fixed)):
                g, _ = restriction(f, n, fixed, X)
                if len(live) and abs(int(g.sum())) != g.size:
                    tot += w * float(Spec.from_tables(g).H()[0])
        worst['han'] = max(worst['han'], H - (tot / t + C2 * (1 - t) / t * I))
out = dict(functions=count, max_ratio_DeltaH_over_RM22_bound=worst['rm22'], max_channel_excess=worst['channel'],
           max_abs_err_EI=worst['EI'], max_Han_excess=worst['han'])
print(json.dumps(out, indent=1))
with open('deps_larger_n_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
