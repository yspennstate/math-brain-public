"""Exhaustive census of all 65536 Boolean functions on 4 uniform variables (covers every function on <=4 variables)."""
import sys, json, time, math, numpy as np
sys.path.insert(0, sys.argv[1])
from b15_engine import *
OUT = sys.argv[2]
n = 4; t0 = time.time()
tabs = np.arange(1 << 16, dtype=np.int64)
F = tables_to_pm(tabs, n)
Q = quantities(F, n)
nonconst = Q['I'] > 1e-12
res = {}
# identity checks (float): Delta_i = B_i + JS_i (C005); JS_i <= (2/ln2) min(Inf_i,1-Inf_i); sum B_i <= H; I = Inf_i + avg I(f_pm) is structural
res['max_abs_Delta_minus_B_minus_JS'] = float(np.abs(Q['Delta'] - Q['B'] - Q['JS']).max())
jsb = TWO_OVER_LN2*np.minimum(Q['Inf'], 1 - Q['Inf'])
res['max_JS_minus_bound'] = float((Q['JS'] - jsb).max())
res['min_H_minus_sumB'] = float((Q['H'] - Q['B'].sum(axis=1))[nonconst].min())
E, Ei = min_ratio(Q['B'], Q['Inf']); G, Gi = min_ratio(Q['Delta'], Q['Inf'])
R = np.where(nonconst, Q['H']/np.where(nonconst, Q['I'], 1), -np.inf)
BI = np.where(nonconst, Q['B'].sum(axis=1)/np.where(nonconst, Q['I'], 1), -np.inf)
E = np.where(nonconst, E, -np.inf); G = np.where(nonconst, G, -np.inf)
def top(arr, k=6):
    o = np.argsort(-arr)[:k]
    return [dict(table=int(t), value=float(arr[t]), I=float(Q['I'][t]), H=float(Q['H'][t])) for t in o]
res['max_E_minB_over_Inf'] = top(E); res['max_G_minDelta_over_Inf'] = top(G)
res['max_H_over_I'] = top(R); res['max_B_over_I'] = top(BI)
res['KSTAR'] = KSTAR
# exact certificate: every nonconstant table has a relevant coordinate with B_i <= K* Inf_i
eq = 0; strict = 0; fail = []; eqtabs = []
Wint = spectra(F, n)
for t in np.nonzero(nonconst)[0]:
    i = int(Ei[t]); s = exact_sign_Bi_minus_Kstar(Wint[t], n, i)
    if s > 0:
        # try every relevant coordinate exactly before declaring failure
        ok = False
        for j in range(n):
            if Q['Inf'][t, j] > 1e-12 and exact_sign_Bi_minus_Kstar(Wint[t], n, j) <= 0:
                ok = True; break
        if not ok: fail.append(int(t))
        else: strict += 1
    elif s == 0: eq += 1; eqtabs.append(int(t))
    else: strict += 1
res['exact_cert'] = dict(nonconstant=int(nonconst.sum()), strict=strict, equal=eq, fail=fail[:20], n_fail=len(fail), equality_tables=eqtabs[:40])
# for equality tables, check that EVERY relevant coordinate is exactly K* (sharpness)
sharp = []
for t in eqtabs:
    sg = [exact_sign_Bi_minus_Kstar(Wint[t], n, j) for j in range(n) if Q['Inf'][t, j] > 1e-12]
    sharp.append(dict(table=t, relevant=len(sg), signs=sg))
res['equality_detail'] = sharp
res['seconds'] = time.time() - t0
json.dump(res, open(OUT, 'w'), indent=1)
print(json.dumps({k: res[k] for k in ['max_abs_Delta_minus_B_minus_JS','max_JS_minus_bound','min_H_minus_sumB','KSTAR','seconds']}, indent=1))
print('exact', json.dumps(res['exact_cert']))
for k in ['max_E_minB_over_Inf','max_G_minDelta_over_Inf','max_H_over_I','max_B_over_I']:
    print(k, [(d['table'], round(d['value'], 9)) for d in res[k]])
print('equality detail', res['equality_detail'][:16])
