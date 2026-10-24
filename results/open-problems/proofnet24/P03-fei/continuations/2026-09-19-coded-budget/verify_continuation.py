"""Exact checks for the 19 September 2026 FEI continuation.

All accepted inequalities use integer/Fraction arithmetic and outward rational
logarithm intervals. The large example is checked from proved formulas, not by
enumerating its 2**2040 truth table. These are self-checks, not Lean or an
independent audit. No full FEI proof is claimed.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json
import math
import time

@dataclass(frozen=True)
class IV:
    lo: F
    hi: F
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('Reversed interval')
    @staticmethod
    def point(x):
        return IV(F(x), F(x))
    def __add__(self, other):
        b = asiv(other)
        return IV(self.lo + b.lo, self.hi + b.hi)
    __radd__ = __add__
    def __neg__(self):
        return IV(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-asiv(other))
    def __rsub__(self, other):
        return asiv(other) + (-self)
    def __mul__(self, other):
        b = asiv(other)
        values = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return IV(min(values), max(values))
    __rmul__ = __mul__
    def __truediv__(self, other):
        b = asiv(other)
        if b.lo <= 0 <= b.hi:
            raise ZeroDivisionError('Interval contains zero')
        return self * IV(1/b.hi, 1/b.lo)
    def __rtruediv__(self, other):
        return asiv(other) / self

def asiv(x):
    return x if isinstance(x, IV) else IV.point(x)

@lru_cache(None)
def small_log(q: F) -> IV:
    if not 1 <= q <= 2:
        raise ValueError('Range reduction failed')
    z = (q-1)/(q+1)
    power, total = z, F(0)
    for j in range(64):
        total += 2*power/(2*j+1)
        power *= z*z
    tail = 2*power/(129*(1-z*z))
    return IV(total, total+tail)

LN2 = small_log(F(2))

@lru_cache(None)
def log2_iv(q: F) -> IV:
    q = F(q)
    if q <= 0:
        raise ValueError('Logarithm requires a positive argument')
    power = 0
    while q < 1:
        q *= 2
        power -= 1
    while q >= 2:
        q /= 2
        power += 1
    # Integer powers of two are exact: do not divide a repeated LN2 interval.
    return IV.point(power) + small_log(q)/LN2

def hbit(t: F) -> IV:
    if t in (0, 1):
        return IV.point(0)
    return -t*log2_iv(t) - (1-t)*log2_iv(1-t)

def decimal_endpoint(x: F, digits: int, lower: bool) -> str:
    scaled = x * 10**digits
    integer = scaled.numerator // scaled.denominator
    if not lower and scaled.denominator != 1:
        integer += 1
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    whole, fractional = divmod(integer, 10**digits)
    return f'{sign}{whole}.{fractional:0{digits}d}'

def show(v, digits=12):
    v = asiv(v)
    return {'decimal_lower': decimal_endpoint(v.lo, digits, True),
            'decimal_upper': decimal_endpoint(v.hi, digits, False)}

def fwht(values):
    a = list(values)
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2*width):
            for j in range(start, start+width):
                x, y = a[j], a[j+width]
                a[j], a[j+width] = x+y, x-y
        width *= 2
    return a

def canonical(f):
    return tuple(x*f[0] for x in f)

def derivative(f, z):
    return canonical(tuple(f[x]*f[x^z] for x in range(len(f))))

def entropy(p):
    return sum((-v*log2_iv(v) for v in p if v), IV.point(0))

@lru_cache(None)
def metrics(f):
    N = len(f)
    n = N.bit_length()-1
    assert N == 1 << n and set(f) <= {-1, 1}
    w = fwht(f)
    p = tuple(F(v*v, N*N) for v in w)
    assert sum(p) == 1
    influences = tuple(F(sum(f[x] != f[x^(1<<i)] for x in range(N)), N)
                       for i in range(n))
    assert all(influences[i] == sum(p[s] for s in range(N) if s & (1<<i))
               for i in range(n))
    j = tuple(min(v, 1-v) for v in influences)
    t = [[F(0) for _ in range(n)] for _ in range(n)]
    phases = []
    C = F(0)
    for i in range(n):
        u = tuple(f[x]*f[x^(1<<i)] for x in range(N))
        phases.append(u)
        coeff = fwht(u)
        C += sum((F(coeff[s]**2, N*N*(1+s.bit_count()))
                  for s in range(1, N)), F(0))
        for l in range(i):
            t[i][l] = t[l][i] = F(sum(u[x] != u[x^(1<<l)] for x in range(N)), 4*N)
    t = tuple(tuple(row) for row in t)
    R = sum((v*v/(v+sum(row)) for v, row in zip(j, t) if v), F(0))
    Q = sum((v*v*log2_iv(1/v) for v in j if v), IV.point(0))
    return {'H': entropy(p), 'p': p, 'I': sum(influences), 'J': sum(j),
            'j': j, 't': t, 'R': R, 'Q': Q, 'C': C}

@lru_cache(None)
def discounted(f):
    data = metrics(f)
    if data['J'] == 0:
        # Characters have zero R,C,Q; their derivatives are constant.
        return F(0), F(0), IV.point(0)
    children = [discounted(derivative(f, z)) for z in range(len(f))]
    return (data['R'] + sum(v[0] for v in children)/(2*len(f)),
            data['C'] + sum(v[1] for v in children)/(2*len(f)),
            data['Q'] + sum((v[2] for v in children), IV.point(0))/(2*len(f)))

def small_hierarchy_checks():
    counts, transitions = {}, 0
    maxR = maxC = F(0)
    maxQ = IV.point(0)
    for n in range(4):
        N = 1 << n
        counts[str(n)] = 1 << N
        for bits in range(1 << N):
            f = canonical(tuple(-1 if bits & (1<<x) else 1 for x in range(N)))
            data = metrics(f)
            r, c, q = discounted(f)
            assert r <= 5*data['J']
            assert c <= 16*data['J']
            assert q.hi <= F(5, 2)*data['J']
            assert data['R'] <= data['C']
            if data['J']:
                maxR = max(maxR, r/data['J'])
                maxC = max(maxC, c/data['J'])
                ratio = q/data['J']
                if ratio.lo > maxQ.lo:
                    maxQ = ratio
            children = [metrics(derivative(f, z)) for z in range(N)]
            for child in children:
                assert all(child['j'][i] <= 2*data['j'][i] for i in range(n))
                assert all(child['t'][i][l] <= 2*data['t'][i][l]
                           for i in range(n) for l in range(n))
            for i in range(n):
                for l in range(i):
                    s = data['t'][i][l]
                    assert sum(x['t'][i][l] for x in children)/N == 2*s-8*s*s
                    transitions += 1
    return {'status': 'PASS', 'truth_tables_by_dimension': counts,
            'total_truth_tables': sum(counts.values()),
            'face_expectation_identities': transitions,
            'largest_observed_discounted_R_over_J': str(maxR),
            'largest_observed_discounted_C_over_J': str(maxC),
            'largest_observed_discounted_Q_over_J': show(maxQ),
            'scope': 'Exact finite self-checks; universal bounds are proved in REPORT.md'}

def rank(columns):
    pivots = {}
    for x in columns:
        while x:
            bit = x.bit_length()-1
            if bit not in pivots:
                pivots[bit] = x
                break
            x ^= pivots[bit]
    return len(pivots)

def syndrome_table(columns):
    values = [0] * (1 << len(columns))
    for x in range(1, len(values)):
        bit = x & -x
        values[x] = values[x^bit] ^ columns[bit.bit_length()-1]
    return values

def small_coded_checks():
    rows = []
    for m, r, n in [(2, 3, 6), (3, 4, 12), (4, 4, 12), (2, 4, 14)]:
        assert n % m == 0
        columns = list(range(1, n+1))
        assert len(set(columns)) == n and rank(columns) == r
        assert all(rank(columns[:b]+columns[b+m:]) == r for b in range(0, n, m))
        syndrome = syndrome_table(columns)
        base = tuple((-1)**sum(((x >> b) & ((1<<m)-1)) == 0
                              for b in range(0, n, m)) for x in range(1<<n))
        perturbation = tuple(-1 if s == 0 else 1 for s in syndrome)
        f = tuple(x*y for x, y in zip(base, perturbation))
        data = metrics(f)
        a, epsilon = F(1, 2**(m-1)), F(1, 2**r)
        predicted_Ii = a+2*epsilon-4*a*epsilon
        assert data['I'] == n*predicted_Ii
        assert data['j'] == (min(predicted_Ii, 1-predicted_Ii),)*n
        assert sum(s == 0 for s in syndrome) == 2**(n-r)
        for i in range(n):
            for j in range(i):
                expected = epsilon if i//m != j//m else a/2+epsilon-4*a*epsilon
                assert data['t'][i][j] == expected
        # Fourier support of h is exactly in the row code.
        code = {sum((((u&col).bit_count() & 1) << i) for i, col in enumerate(columns))
                for u in range(1<<r)}
        wh = fwht(perturbation)
        assert {s for s, v in enumerate(wh) if v} <= code
        rows.append({'block_size': m, 'syndrome_bits': r, 'variables': n,
                     'truth_table_entries_checked': 1<<n, 'I': str(data['I']),
                     'j_i': str(data['j'][0]), 'R': str(data['R']), 'C': str(data['C'])})
    return {'status': 'PASS', 'examples': rows,
            'scope': 'Actual full truth tables and every coordinate/face for these four small examples'}

def packet_checks():
    n, r = 12, 4
    N = 1 << n
    columns = list(range(1, n+1))
    syndrome = syndrome_table(columns)
    h = tuple(-1 if x == 0 else 1 for x in syndrome)
    wh = fwht(h)
    ph = tuple(F(x*x, N*N) for x in wh)
    Hh = entropy(ph)
    Ih = tuple(sum(ph[s] for s in range(N) if s & (1 << i)) for i in range(n))
    code = {sum((((u&col).bit_count() & 1) << i) for i, col in enumerate(columns))
            for u in range(1 << r)}
    d = min(x.bit_count() for x in code if x)
    assert d == 5
    checked = 0
    for mask in range(16):
        g = tuple(-1 if mask & (1 << (x & 3)) else 1 for x in range(N))
        wg = fwht(g)
        pg = tuple(F(x*x, N*N) for x in wg)
        product = tuple(x*y for x, y in zip(g, h))
        wp = fwht(product)
        pp = tuple(F(x*x, N*N) for x in wp)
        # The nonzero product masses factor exactly, including multiplicity.
        expected = sorted(a*b for a in pg if a for b in ph if b)
        assert sorted(a for a in pp if a) == expected
        Ig = tuple(sum(pg[s] for s in range(N) if s & (1 << i)) for i in range(n))
        Iproduct = sum(s.bit_count()*pp[s] for s in range(N))
        assert Iproduct == sum(Ig)+sum(Ih)-2*sum(a*b for a, b in zip(Ig, Ih))
        checked += 1
    # One rare point-flip creates a small nonzero tail outside the ball.
    g = tuple((-1 if x & 1 else 1)*(-1 if x == 0 else 1) for x in range(N))
    wg = fwht(g)
    pg = tuple(F(x*x, N*N) for x in wg)
    pp = tuple(F(x*x, N*N) for x in fwht(tuple(a*b for a,b in zip(g,h))))
    tail = sum(pg[s] for s in range(N) if s.bit_count() > 2)
    eta, root_eta = F(1, 1024), F(1, 32)
    assert tail <= eta and eta <= F(1, 16) and root_eta**2 == eta
    E = n*(eta+root_eta)+hbit(eta)+hbit(root_eta)
    deficit = entropy(pp)-entropy(pg)-Hh
    assert deficit.lo >= -E.lo and deficit.hi <= E.lo
    Ig = tuple(sum(pg[s] for s in range(N) if s & (1 << i)) for i in range(n))
    Iproduct = sum(s.bit_count()*pp[s] for s in range(N))
    energy_discrepancy = Iproduct-(sum(Ig)+sum(Ih)-2*sum(a*b for a,b in zip(Ig,Ih)))
    assert abs(energy_discrepancy) <= n*(eta+root_eta)
    return {'status': 'PASS', 'variables': n, 'code_distance': d,
            'exact_product_spectrum_examples': checked,
            'nonzero_tail_example': {'tail_mass': str(tail),
                                    'entropy_additivity_error': show(deficit),
                                    'certified_allowed_error': show(E),
                                    'energy_discrepancy': str(energy_discrepancy)}}

def clause_H(s):
    if s <= 1:
        return IV.point(0)
    a = F(1, 2**(s-1))
    return -2*(1-a)**2*log2_iv(1-a) + (4*a-2*a*a)*(s-1)

def clause_D(s):
    return 2*clause_H(s) - (1-F(1, 2**s))*clause_H(s-1)

def large_family_certificate():
    m, h = 8, 3
    r, k = m+h, 2**m-1
    M = 1 << r
    n = m*k
    assert n == M-m
    columns = list(range(1, n+1))
    assert rank(columns) == r
    complement_ranks = [rank(columns[:b]+columns[b+m:]) for b in range(0, n, m)]
    assert complement_ranks == [r]*k
    row_masks = [sum(((col >> bit)&1) << i for i, col in enumerate(columns))
                 for bit in range(r)]
    words = [0]*M
    for x in range(1, M):
        bit = x & -x
        words[x] = words[x^bit] ^ row_masks[bit.bit_length()-1]
    distances = [w.bit_count() for w in words[1:]]
    d = M//2-m+1
    assert min(distances) >= d
    b = (d-1)//2
    s = b//m+1
    assert s == 2**(m-2)
    a, epsilon = F(1, 2**(m-1)), F(1, M)
    p = 4*a
    union_tail_bound = 2**k*p**s
    assert union_tail_bound == F(1, 2**65)
    eta, root_eta = F(1, 2**64), F(1, 2**32)
    assert union_tail_bound <= eta and root_eta*root_eta == eta
    entropy_error = n*(eta+root_eta)+hbit(eta)+hbit(root_eta)
    D_error = 3*entropy_error
    j = a+2*epsilon-4*a*epsilon
    t = (m-1)*a/2+(n-1)*epsilon-4*(m-1)*a*epsilon
    assert j == F(575, 65536) and j < F(1, 2)
    R = n*j*j/(j+t)
    Q = n*j*j*log2_iv(1/j)
    ideal_D = k*clause_D(m)+clause_D(r)
    actual_D = IV(ideal_D.lo-D_error.hi, ideal_D.hi+D_error.hi)
    ratio = actual_D/(R+Q)
    assert ratio.lo > F(13716, 1000) # stronger than >13.7 and hence >8
    actual_H = IV((k*clause_H(m)+clause_H(r)).lo-entropy_error.hi,
                  (k*clause_H(m)+clause_H(r)).hi+entropy_error.hi)
    I = n*j
    C_base = k*4*a*a*(2**m-1-m)
    C_lo = (1-4*epsilon)**2*C_base
    C_hi = C_lo+32*epsilon
    # Loose all-m inequalities used in the analytical asymptotic proof.
    assert R+Q.hi <= F(6*m*m, 2**m)
    assert actual_D.lo > 3
    return {'status': 'PASS', 'block_size': m, 'blocks': k, 'syndrome_bits': r,
            'variables': n, 'nonzero_codewords_enumerated': M-1,
            'actual_minimum_code_distance': min(distances),
            'proved_distance_lower_bound': d,
            'all_block_complement_ranks_checked': len(complement_ranks),
            'spectral_ball_radius': b, 'active_block_threshold': s,
            'exact_union_tail_bound': str(union_tail_bound),
            'tail_bound_used_in_entropy_continuity': str(eta),
            'j_i': str(j), 't_i': str(t), 'R': show(R), 'Qlog': show(Q),
            'D_ideal': show(ideal_D), 'absolute_D_error_upper_bound': show(D_error),
            'D_actual_enclosure': show(actual_D),
            'D_over_R_plus_Q_enclosure': show(ratio),
            'strict_rational_comparison': 'D/(R+Qlog) > 3429/250 = 13.716',
            'H_over_I_enclosure': show(actual_H/I),
            'resolvent_C_enclosure': show(IV(C_lo, C_hi)),
            'scope': 'No 2**2040 truth-table or shift enumeration; proof-derived formulas plus exact code geometry and rational entropy intervals'}

def one_point_budget_ratio(d):
    A = F(2**(d+1)-1, d+1)-1
    probability = F(1)
    total = F(0)
    for k in range(d):
        total += probability*F(2**d-2**k, 2**d-1)
        probability *= 1-F(2**k, 2**d)
    return F(4, 2**d)*A*total

def benchmark_checks():
    dimension_parameters = []
    previous_n = None
    for m in range(8, 65):
        r = m+(m-1).bit_length()
        M = 1 << r
        k = (M-1)//m
        n = m*k
        omitted = M-n
        b = M//4-(omitted+1)//2
        active = b//m+1
        assert 1 <= omitted <= m and n-m > M//2-1
        assert F(active) > F(k, 4)-1
        assert k+(3-m)*active <= -6*m
        assert 2**m-1 <= k and M < 2*m*2**m
        if previous_n is not None:
            assert previous_n < n < 5*previous_n
        previous_n = n
        dimension_parameters.append(m)
    direct = []
    for n in range(2, 6):
        f = canonical(tuple(-1 if x == 0 else 1 for x in range(1<<n)))
        actual = discounted(f)[1]/metrics(f)['J']
        predicted = one_point_budget_ratio(n-1)
        assert actual == predicted
        direct.append({'variables': n, 'exact_ratio': str(actual)})
    rows = []
    for d in range(1, 65):
        value = one_point_budget_ratio(d)
        assert 0 < value < 8
        if d in (8, 16, 32, 64):
            rows.append({'point_phase_dimension': d,
                         'global_function_dimension': d+1,
                         'discounted_C_over_J': show(value)})
    return {'status': 'PASS', 'direct_hierarchy_comparisons': direct,
            'closed_formula_dimensions_checked': 64, 'selected_values': rows,
            'uniform_dimension_construction_parameters_checked': dimension_parameters,
            'scope': 'The formula is proved in Section 7.6; its limiting value is eight'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', choices=['hierarchy', 'coded', 'packets', 'large', 'benchmark', 'all'], default='all')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    data = {'full_FEI_proved': False, 'independent_audit': False, 'lean_used': False,
            'acceptance_arithmetic': 'Integers and Fraction intervals; 64-term atanh series',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    jobs = {'hierarchy': small_hierarchy_checks, 'coded': small_coded_checks,
            'packets': packet_checks, 'large': large_family_certificate, 'benchmark': benchmark_checks}
    for name, fun in jobs.items():
        if args.part in (name, 'all'):
            data[name] = fun()
    data['elapsed_seconds'] = round(time.monotonic()-start, 3)
    data['status'] = 'ALL_REQUESTED_CHECKS_PASS'
    text = json.dumps(data, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text)

if __name__ == '__main__':
    main()
