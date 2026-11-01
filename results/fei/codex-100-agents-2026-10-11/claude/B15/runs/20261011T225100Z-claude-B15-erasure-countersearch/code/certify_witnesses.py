"""Exact certification and description of the witnesses found by search.py.
For each witness: support A = {x : f(x) = -1}, integer Walsh spectrum, and for every coordinate the exact
sign of B_i - K* Inf_i (prime-exponent linear form, interval-decided), plus float B_i, Inf_i, ratios, H, I, Delta_i."""
import sys, json, numpy as np
sys.path.insert(0, sys.argv[1])
from b15_engine import KSTAR, hadamard, pair_index, quantities
from exact_prime import sign_pairs_vs_kstar, linear_form, sign_form

S = json.load(open(sys.argv[2], encoding='utf-8'))
OUT = sys.argv[3]


def pm_from_int(table, n):
    return np.array([[1 - 2 * ((table >> x) & 1) for x in range(1 << n)]], dtype=np.int64)


def describe(table, n, label):
    F = pm_from_int(table, n)
    Hm = hadamard(n)
    W = (F @ Hm)[0]
    Q = quantities(F, n, want_delta=True)
    rows = []
    for i in range(n):
        i0, i1 = pair_index(n, i)
        L = int(sum(int(W[t]) ** 2 for t in i1))
        if L == 0:
            rows.append(dict(i=i, relevant=False))
            continue
        pairs = [(int(W[a]) ** 2, int(W[b]) ** 2, 1) for a, b in zip(i0, i1)]
        sg, e = sign_pairs_vs_kstar(pairs)
        rows.append(dict(i=i, relevant=True, Inf_times_4n=L, Inf=float(Q['Inf'][0, i]), B=float(Q['B'][0, i]),
                         ratio=float(Q['B'][0, i] / Q['Inf'][0, i]), Delta=float(Q['Delta'][0, i]),
                         Delta_ratio=float(Q['Delta'][0, i] / Q['Inf'][0, i]), exact_sign_B_minus_Kstar_Inf=sg,
                         prime_form={str(p): k for p, k in sorted(e.items())}))
    rel = [r for r in rows if r['relevant']]
    support = [x for x in range(1 << n) if (table >> x) & 1]
    return dict(label=label, n=n, table=str(table), support_points=support,
                support_bits=[format(x, '0%db' % n)[::-1] for x in support],
                walsh=[int(v) for v in W], H=float(Q['H'][0]), I=float(Q['I'][0]), H_over_I=float(Q['H'][0] / Q['I'][0]),
                E=min(r['ratio'] for r in rel), G=min(r['Delta_ratio'] for r in rel), coords=rows,
                exact_violation=all(r['exact_sign_B_minus_Kstar_Inf'] > 0 for r in rel))


out = []
for d in S['C_ils']:
    seen = set()
    for key, val in d['top'][:6]:
        if val > KSTAR + 1e-12:
            out.append(describe(int(key), d['n'], 'ILS n=%d E=%.9f' % (d['n'], val)))
for d in S['B_cyclic']:
    if d['best_E'] > KSTAR + 1e-12:
        n = d['n']
        # rebuild the truth table integer from the orbit code
        D = 1 << n
        orb = [-1] * D
        k = 0
        for x in range(D):
            if orb[x] >= 0:
                continue
            y = x
            while orb[y] < 0:
                orb[y] = k
                y = ((y << 1) | (y >> (n - 1))) & (D - 1)
            k += 1
        code = d['best_code']
        table = sum(((code >> orb[x]) & 1) << x for x in range(D))
        out.append(describe(table, n, 'cyclic n=%d best' % n))
json.dump(out, open(OUT, 'w', encoding='utf-8'), indent=1)
for o in out:
    print(o['label'], 'support', o['support_bits'], 'E=%.9f G=%.6f H/I=%.6f' % (o['E'], o['G'], o['H_over_I']),
          'exact_violation', o['exact_violation'],
          [(r['i'], round(r['ratio'], 6), r['exact_sign_B_minus_Kstar_Inf']) for r in o['coords'] if r['relevant']])
