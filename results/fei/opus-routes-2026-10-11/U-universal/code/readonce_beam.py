"""Beam search over read-once AND/OR formulas using the exact composition recursion; track H/I and U/I.
Checks Theorem G (H <= 2(I-Var)+2U) on near-extremal read-once formulas.  EVIDENCE (float logs)."""
import math, itertools, json
from compose_rec import compose_step, X, AND, OR
NB = 120
def bin_of(mu): return min(NB - 1, int((mu + 1) / 2 * NB))
pop = {bin_of(0.0): dict(X, H=0.0, U=0.0, I=1.0, Var=1.0, size=1, ratio=0.0)}
best_overall = []
for rnd in range(14):
    items = list(pop.values()); new = dict(pop)
    for a in items:
        for b in items:
            for gname, g in (('A', AND), ('O', OR)):
                if a['size'] + b['size'] > 4000: continue
                try: r = compose_step(g, [a, b])
                except ZeroDivisionError: continue
                if r['Var'] < 1e-6 or r['I'] <= 0: continue
                r['size'] = a['size'] + b['size']; r['ratio'] = r['H'] / r['I']
                k = bin_of(r['mu'])
                if k not in new or r['ratio'] > new[k]['ratio']: new[k] = r
    pop = new
    top = max(pop.values(), key=lambda d: d['ratio'])
    print('round', rnd, 'best H/I=%.4f U/I=%.4f size=%d Var=%.3g  G-check H/(2(I-V)+2U)=%.4f  max U/I in pop=%.4f' % (
        top['ratio'], top['U'] / top['I'], top['size'], top['Var'], top['H'] / (2 * (top['I'] - top['Var']) + 2 * top['U']),
        max(d['U'] / d['I'] for d in pop.values())), flush=True)
