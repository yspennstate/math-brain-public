#!/usr/bin/env python3
"""Self-check the selector lemma and logarithmic NAND formulas.

Theorems are proved in the accompanying notes. Transform coefficients and
influences are exact; logarithmic expressions use rigorous rational intervals.
Overlap of two intervals is only a consistency check on a proved identity.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random
from certify_nand80 import (wht, IV, h, edge, LN2_LO, LN2_HI,
                           rational_interval)


def overlap(a, b):
    assert max(a.lo, b.lo) <= min(a.hi, b.hi)


def kedge(r, s):
    r, s = max(r, s), min(r, s)
    if s == 0 or r == s:
        return IV(0)
    return h(s)-h(r)*(s/r)


def indicator_metrics(a):
    N = len(a)
    n = N.bit_length()-1
    c = [F(v, N) for v in wht(a)]
    p = [v*v for v in c]
    K = sum((kedge(p[S], p[S | (1 << i)])
             for i in range(n) for S in range(N) if not S & (1 << i)), IV(0))
    Q = sum((p[1 << i] for i in range(n)), F(0))
    influence = 4*sum((S.bit_count()*p[S] for S in range(N)), F(0))
    alpha = c[0]
    U = K+h(alpha)*(2*Q/alpha) if alpha else IV(0)
    return alpha, K, Q, influence, U


def log2(x):
    return h(x)*(-1/x)


def identical_checks():
    records = []
    for n in range(1, 5):
        for size in range(1, 1 << n):
            a = [int(x < size) for x in range(1 << n)]
            alpha, K, Q, I, U = indicator_metrics(a)
            for k in [2, 3, 4]:
                if n*k > 9:
                    continue
                product = [1]
                for _ in range(k):
                    product = [u*v for u in product for v in a]
                ap, Kp, Qp, Ip, Up = indicator_metrics([1-v for v in product])
                w = alpha**(k-1)
                assert ap == 1-alpha**k and Ip == k*w*I and Qp == k*w*w*Q
                predicted = K*(k*w)+log2(ap/(1-ap))*(2*Qp)
                overlap(Kp, predicted)
                z, zp = Q/I, Qp/Ip
                P = K*(1/I)+IV(4*z/LN2_HI, 4*z/LN2_LO)
                Pp = Kp*(1/Ip)+IV(4*zp/LN2_HI, 4*zp/LN2_LO)
                assert Pp.hi < P.lo
                records.append([n, size, k])
    return records


def unequal_checks():
    seeds = [[1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1]*7+[0]]
    results = []
    for i, a in enumerate(seeds):
        aa, Ka, Qa, Ia, Ua = indicator_metrics(a)
        for j, b in enumerate(seeds):
            ab, Kb, Qb, Ib, Ub = indicator_metrics(b)
            product = [x*y for x in a for y in b]
            outa, K, Q, I, U = indicator_metrics([1-x for x in product])
            p = aa*ab
            assert outa == 1-p
            assert Q == ab*ab*Qa+aa*aa*Qb and I == ab*Ia+aa*Ib
            overlap(K, Ka*ab+Kb*aa+log2((1-p)/p)*(2*Q))
            correction = ((log2(aa)*(1-ab)-log2(ab)*ab)*(2*ab*Qa)
                          +(log2(ab)*(1-aa)-log2(aa)*aa)*(2*aa*Qb))
            overlap(U, Ua*ab+Ub*aa+correction)
            _, Kc, Qc, Ic, Uc = indicator_metrics(product)
            assert Q == Qc and I == Ic
            overlap(U, Uc)
            results.append([i, j])
    a = [1, 0, 0, 0]
    _, K, Q, I, U = indicator_metrics(a)
    _, Kc, Qc, Ic, Uc = indicator_metrics([1-v for v in a])
    assert Q == Qc and I == Ic and Kc.lo > K.hi
    return results, rational_interval(Kc-K)


def selector_checks():
    rng = random.Random(202609180015)
    selectors, data = 3, 3
    counts = []
    for trial in range(64):
        labels = [rng.randrange(data+1) for _ in range(1 << selectors)]
        signs = [rng.choice([-1, 1]) for _ in labels]
        values = []
        for index in range(1 << (selectors+data)):
            x = index & ((1 << selectors)-1)
            j = labels[x]
            values.append(signs[x] if j == 0
                          else signs[x]*(1-2*((index >> (selectors+j-1)) & 1)))
        size = len(values)
        p = [F(v, size)**2 for v in wht(values)]
        By = sum((edge(p[S], p[S | (1 << i)])
                  for i in range(selectors, selectors+data)
                  for S in range(size) if not S & (1 << i)), IV(0))
        Ix = sum((p[S]*(S & ((1 << selectors)-1)).bit_count()
                  for S in range(size)), F(0))
        law = [F(labels.count(j), len(labels)) for j in range(data+1)]
        HJ = sum((h(v) for v in law), IV(0))
        # Here every finite claim below has disjoint certified bounds or an
        # exactly represented equality; no floating tolerance is accepted.
        assert By.hi <= HJ.lo
        assert HJ.hi <= 2*Ix
        spectral_law = [sum((p[S] for S in range(size)
                            if S >> selectors == (0 if j == 0 else 1 << (j-1))), F(0))
                        for j in range(data+1)]
        assert spectral_law == law
        counts.append({'trial': trial, 'label_counts': [labels.count(j) for j in range(data+1)],
                       'B_y': rational_interval(By), 'H_J': rational_interval(HJ),
                       'I_x': str(Ix)})
    return counts


def main():
    identical = identical_checks()
    unequal, complement_gap = unequal_checks()
    selector = selector_checks()
    out = {'status': 'PASS',
           'identical_nand_parameters': identical,
           'identical_nand_count': len(identical),
           'unequal_nand_seed_pairs': unequal,
           'complement_counterexample_K_increase': complement_gap,
           'selector_seed': 202609180015,
           'selector_checks': selector,
           'scope': 'Exact finite self-checks and rigorous rational log enclosures. Identity interval overlap is consistency evidence, not a substitute for the written algebraic proofs. No independent audit.'}
    Path('logarithmic_structures_certificate.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'status': out['status'], 'identical_nand_count': len(identical),
                      'unequal_nand_count': len(unequal), 'selector_count': len(selector),
                      'complement_gap': complement_gap}, indent=2))


if __name__ == '__main__':
    main()
