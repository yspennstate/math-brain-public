"""Stress test of the CONJECTURE GU (sum_i Delta_i U <= K I) on deep read-once compositions (EVIDENCE only).
Uses the validated engine rec.py."""
import json, sys
import numpy as np
from rec import var, table, gate, root_stats, AND2, OR2, MAJ3, andk, ork, majk
from gu_values import g5

rows = []


def rep(name, node):
    st = root_stats(node)
    row = dict(name=name, H_over_I=round(st['H_over_I'], 4), U_over_I=round(st['U_over_I'], 4), G_over_I=round(st['G_over_I'], 4),
               min_loc=round(st['min_local_U'], 4), max_loc=round(st['max_local_U'], 4), Var=round(st['Var'], 4),
               thmG_full=round(st['thmG_ratio_full'], 6))
    rows.append(row); print(json.dumps(row), flush=True)


G5 = table(g5)
# iterated majority over g5
cur = G5
for d in range(0, 7):
    rep(f'maj3^{d} o g5', cur)
    cur = gate(MAJ3, [cur, cur, cur], symmetric=True)
# iterated g5 over itself
cur = G5
for d in range(1, 4):
    cur = gate(g5, [cur] * 5)
    rep(f'g5^{d+1}', cur)
# other symmetric outers
for k in [5, 7, 9]:
    rep(f'maj{k} o g5', gate(majk(k), [G5] * k, symmetric=True))
for k in [2, 3, 4, 6]:
    rep(f'and{k} o g5', gate(andk(k), [G5] * k, symmetric=True))
    rep(f'or{k} o g5', gate(ork(k), [G5] * k, symmetric=True))
# alternating and/or towers over g5
for pat in ['A', 'O', 'AO', 'OA', 'AAO', 'MA', 'AM', 'MO']:
    cur = G5
    for d in range(4):
        c = pat[d % len(pat)]
        g = {'A': AND2, 'O': OR2, 'M': MAJ3}[c]
        k = 3 if c == 'M' else 2
        cur = gate(g, [cur] * k, symmetric=True)
    rep(f'tower {pat} depth4 o g5', cur)
with open('explore_gu_results.json', 'w', encoding='utf-8') as fh:
    json.dump(rows, fh, indent=1)
