"""Independent checks of the logarithmic output-parity FEI derivation.

No author helper imports. Boolean/Fourier/edge counts and Gibbs reference
normalizations use integer or Fraction arithmetic. Entropies and relative
entropies are explicitly numerical supplements, not proof certificates.
"""
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import random

RNG = random.Random(2026100307)
C = dict(functions=0, parity_pairs=0, exact_isoperimetry=0,
         direct_nonempty_kl=0, reference_normalizations=0,
         abstract_gibbs_laws=0, gate_combinations=0, unate_gates=0,
         threshold_regime_cases=0)
MAX = dict(weak_target_ratio=0.0, logarithmic_target_ratio=0.0,
           maximum_kl_identity_error=0.0)


def entropy(p):
    return -sum(float(x) * math.log2(float(x)) for x in p if x)


def transform(f):
    out = list(f)
    width = 1
    while width < len(out):
        for start in range(0, len(out), 2 * width):
            for j in range(start, start + width):
                left, right = out[j], out[j + width]
                out[j], out[j + width] = left + right, left - right
        width *= 2
    return out


def edge_counts(f, n):
    return [sum(f[x] != f[x | (1 << i)] for x in range(len(f))
                if not x & (1 << i)) for i in range(n)]


def reference(n):
    raw = [Fraction(1, n ** s.bit_count()) for s in range(1, 1 << n)]
    z = sum(raw)
    assert z == (Fraction(n + 1, n) ** n - 1)
    assert 1 <= z < 2
    q = [x / z for x in raw]
    assert sum(q) == 1 and all(x > 0 for x in q)
    C['reference_normalizations'] += 1
    return z, q


def check(f, n, subsets, gate_count=None):
    size = 1 << n
    assert len(f) == size
    w = transform(f)
    assert sum(x * x for x in w) == size * size
    b = edge_counts(f, n)
    rho2 = Fraction(4 * sum(x * x for x in b), size * size)
    if gate_count is not None:
        assert rho2 <= gate_count * gate_count
    base_h = entropy([Fraction(x * x, size * size) for x in w])
    for mask in subsets:
        h = [f[x] * (-1 if (x & mask).bit_count() % 2 else 1)
             for x in range(size)]
        wh = transform(h)
        assert wh == [w[x ^ mask] for x in range(size)]
        bh = edge_counts(h, n)
        assert bh == [size // 2 - b[i] if mask & (1 << i) else b[i]
                      for i in range(n)]
        inf = Fraction(2 * sum(bh), size)
        energy = Fraction(sum(x * x * s.bit_count() for s, x in enumerate(wh)),
                          size * size)
        assert inf == energy
        a = min(h.count(-1), h.count(1))
        assert (1 << sum(bh)) * a ** a >= size ** a
        C['exact_isoperimetry'] += 1
        p = [Fraction(x * x, size * size) for x in wh]
        assert abs(entropy(p) - base_h) < 2e-12
        variance = 1 - p[0]
        assert variance <= inf
        if n:
            weak = (math.log2(n) + 3) * float(inf)
            assert base_h <= weak + 3e-11
            binary = entropy([variance, 1 - variance])
            assert binary <= 2 * float(inf) + 3e-11
            if inf:
                MAX['weak_target_ratio'] = max(MAX['weak_target_ratio'], base_h / weak)
            if variance:
                z, ref = REFERENCES[n]
                nonempty = [x / variance for x in p[1:]]
                assert sum(nonempty) == 1
                direct_kl = sum(float(x) * math.log2(float(x / y))
                                for x, y in zip(nonempty, ref) if x)
                rhs = (float(inf / variance) * math.log2(n)
                       + math.log2(float(z)) - entropy(nonempty))
                error = abs(direct_kl - rhs)
                MAX['maximum_kl_identity_error'] = max(MAX['maximum_kl_identity_error'], error)
                assert direct_kl >= -3e-11 and error < 3e-11
                assert abs(base_h - binary - float(variance) * entropy(nonempty)) < 3e-11
                C['direct_nonempty_kl'] += 1
        ell, q = mask.bit_count(), n - mask.bit_count()
        m = max(1.0, math.sqrt(float(rho2))) if gate_count is None else gate_count
        target = (math.log2(4 * m * m + 2 * q) + 3) * float(inf)
        assert base_h <= target + 3e-11
        assert float(inf) + 3e-12 >= ell - math.sqrt(float(rho2) * ell)
        if inf:
            MAX['logarithmic_target_ratio'] = max(MAX['logarithmic_target_ratio'], base_h / target)
        else:
            assert base_h == 0
        C['parity_pairs'] += 1
    C['functions'] += 1


REFERENCES = {n: reference(n) for n in range(1, 13)}


def main():
    for n in range(4):
        size = 1 << n
        for labels in product((-1, 1), repeat=size):
            check(labels, n, range(size))
    for n in range(4, 10):
        size = 1 << n
        cases = []
        for _ in range(45):
            cases.append([RNG.choice((-1, 1)) for _ in range(size)])
        for cut in (0, 1, n // 2, n - 1, n):
            cases.append([1 if x.bit_count() >= cut else -1 for x in range(size)])
        cases += [[1] * size, [-1] * size,
                  [-1 if x == 0 else 1 for x in range(size)],
                  [-1 if x.bit_count() % 2 else 1 for x in range(size)]]
        for f in cases:
            subsets = {0, size - 1, 1, size // 2, RNG.randrange(size), RNG.randrange(size)}
            check(f, n, sorted(subsets))
    for n in range(2, 10):
        size = 1 << n
        for m in range(1, 5):
            for _ in range(3):
                gates = []
                for j in range(m):
                    orient = RNG.randrange(size)
                    weights = [RNG.randint(1, 5) for _ in range(n)]
                    cut = RNG.randint(-n, n)
                    gate = [1 if sum(weights[i] * (1 if (x ^ orient) & (1 << i) else -1)
                                     for i in range(n)) >= cut else -1 for x in range(size)]
                    bg = edge_counts(gate, n)
                    wg = transform(gate)
                    assert all(abs(wg[1 << i]) == 2 * bg[i] for i in range(n))
                    assert 4 * sum(z * z for z in bg) <= size * size
                    gates.append(gate)
                table = [RNG.choice((-1, 1)) for _ in range(1 << m)]
                f = [table[sum((gates[j][x] == 1) << j for j in range(m))] for x in range(size)]
                bf = edge_counts(f, n)
                all_bg = [edge_counts(g, n) for g in gates]
                assert all(bf[i] <= sum(bg[i] for bg in all_bg) for i in range(n))
                check(f, n, sorted({0, size - 1, 1, RNG.randrange(size)}), m)
                C['gate_combinations'] += 1
                C['unate_gates'] += m
    # The off-law Gibbs inequality does not rely on Boolean constraints.
    for n in range(1, 13):
        z, q = REFERENCES[n]
        for _ in range(10):
            weights = [RNG.randrange(7) for _ in q]
            if not sum(weights):
                weights[0] = 1
            p = [Fraction(x, sum(weights)) for x in weights]
            degree = sum(float(x) * (s + 1).bit_count() for s, x in enumerate(p))
            kl = sum(float(x) * math.log2(float(x / y)) for x, y in zip(p, q) if x)
            rhs = degree * math.log2(n) + math.log2(float(z)) - entropy(p)
            assert kl >= -3e-11 and abs(kl - rhs) < 3e-11
            C['abstract_gibbs_laws'] += 1
    for m in [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(7, 3), Fraction(5), Fraction(10)]:
        for ell in range(0, 201):
            for q in range(0, 41):
                n = ell + q
                cap = 4 * m * m + 2 * q
                assert cap >= 4
                if ell >= max(4 * m * m, q):
                    assert ell >= 4 and n <= 2 * ell
                    assert ell - float(m) * math.sqrt(ell) >= ell / 2 - 3e-12
                else:
                    assert n < cap
                C['threshold_regime_cases'] += 1
    report = {'status': 'PASS independent finite checks; analytic audit separate',
              'counts': C, 'maxima': MAX,
              'exact': ['Walsh Parseval/physical energy/parity index permutation',
                        'physical influence complement', 'integer cube edge-isoperimetry',
                        'Fraction nonempty Gibbs reference normalization',
                        'unate Chow/Parseval/overlapping gate flip-union',
                        'Fraction dimension-regime cap inequalities'],
              'numerical': ['direct conditional KL identity and full spectral-law chain rule',
                            'weak logdim and logarithmic character targets',
                            'arbitrary nonempty spectral probability laws'],
              'scope': 'Evidence supplements a full analytic derivation; no novelty certificate or general FEI proof'}
    path = Path(__file__).with_name('output_parity_logarithmic_heat_checks.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
