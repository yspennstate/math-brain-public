#!/usr/bin/env python
"""Exact certificate: every two-address conditional-product Boolean F on N=n+2<=5 variables satisfies
H <= c* I with c* = 16/3 - (3/2) log2 3 (the three-variable one-point defect), with equality classified.

H <= c* I  <=>  Ztot^(6 Ztot) * 3^(9K) <= 2^(32K) * prod_atoms C^(6C),   K = sum |S| C, Ztot = sum C = 4^(n+1),
because H*Ztot = sum C log2(Ztot/C) and I*Ztot = K.  All integers; no floating point enters the decision.
Usage: python -X utf8 certify_max.py OUTDIR
"""
import sys, os, json, time
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1]
sys.argv = [sys.argv[0], OUT, 'P0']
import b07_lead_checks as B

res_all = {}
t0 = time.time()
for n in (2, 3):
    res, D = B.census(n, want_exact_all=False, internal=True)
    combos, Ck, Zl, gk = D['combos'], D['Ck'], D['Zl'], D['gk']
    P = 1 << n
    Ztot = 4 ** (n + 1)
    wJ = [0, 1, 1, 2]
    # per-slice exact data
    nslices = len(Zl)
    P6 = []
    K2 = []
    atomsC = []
    for j in range(nslices):
        prod = 1
        k2 = 0
        at = []
        for T in range(P):
            c = int(Ck[j, T])
            if c:
                prod *= c ** (6 * c)
                k2 += B.popc(T) * c
                at.append(c)
        P6.append(prod)
        K2.append(k2)
        atomsC.append(at)
    LHS0 = Ztot ** (6 * Ztot)
    pow3 = {}
    viol = 0
    equal = []
    for idx, js in enumerate(combos):
        K = sum(wJ[J] * Zl[j] + K2[j] for J, j in enumerate(js))
        if K == 0:
            continue  # constant function, H = I = 0
        if K not in pow3:
            pow3[K] = 3 ** (9 * K)
        lhs = LHS0 * pow3[K]
        rhs = (P6[js[0]] * P6[js[1]] * P6[js[2]] * P6[js[3]]) << (32 * K)
        if lhs > rhs:
            viol += 1
        elif lhs == rhs:
            equal.append(idx)
    # classify equality cases: joint law must be one atom 9/16 and seven atoms 1/16
    def law(js):
        cs = []
        for j in js:
            cs.extend(atomsC[j])
        return sorted((Fraction(c, Ztot) for c in cs), reverse=True)
    pd = [Fraction(9, 16)] + [Fraction(1, 16)] * 7
    eq_pd = sum(1 for idx in equal if law(combos[idx]) == pd)
    res_all['n%d' % n] = {'N_total': n + 2, 'valid_functions': len(combos), 'violations_of_H_le_cstar_I': viol,
                          'equality_cases': len(equal), 'equality_cases_with_point_defect_law': eq_pd,
                          'float_argmax_count': res['argmax_count'], 'seconds_cumulative': round(time.time() - t0, 1)}
    print(n, res_all['n%d' % n], flush=True)
    with open(os.path.join(OUT, 'P4_certificate_cstar.json'), 'w', encoding='utf-8') as fh:
        json.dump({'c_star': '16/3 - (3/2) log2 3', 'c_star_float': 16 / 3 - 1.5 * 1.584962500721156, 'results': res_all,
                   'method': __doc__}, fh, indent=1)
