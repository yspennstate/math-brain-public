#!/usr/bin/env python3
"""Audit the exact three-bit calculation using only the standard library."""
import os
os.environ['OMP_NUM_THREADS'] = '1'
import csv
import itertools
import json
import math
from pathlib import Path
import random
import resource
import signal
import sys
import time
from decimal import Decimal, localcontext
from fractions import Fraction

signal.alarm(180)
START = time.monotonic()
LN2 = math.log(2)
WORDS = [''.join(x) for x in itertools.product('01', repeat=3)]
OUTS = [''] + [''.join(x) for n in range(1, 4)
                 for x in itertools.product('01', repeat=n)]
INDEX = {y: j for j, y in enumerate(OUTS)}
H0 = math.log2(3) - 2/3
COMMAND = 'OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py'


def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0)


def channel_masks(d):
    """All eight independent deletion masks; supports Fraction inputs."""
    s = 1-d
    W = []
    for x in WORDS:
        row = [0 for _ in OUTS]
        for mask in itertools.product((0, 1), repeat=3):
            y = ''.join(x[i] for i in range(3) if mask[i])
            m = sum(mask)
            row[INDEX[y]] += s**m * d**(3-m)
        W.append(row)
    return W


def channel_one_deletion_recurrence(d):
    """Different construction: append each transmitted bit recursively."""
    W = []
    for x in WORDS:
        row = {'': 1}
        for bit in x:
            nxt = {}
            for y, p in row.items():
                nxt[y] = nxt.get(y, 0) + d*p
                nxt[y+bit] = nxt.get(y+bit, 0) + (1-d)*p
            row = nxt
        W.append([row.get(y, 0) for y in OUTS])
    return W


def divergences(p, W):
    q = [sum(p[i]*W[i][j] for i in range(8)) for j in range(15)]
    D = [sum(w*math.log2(w/q[j]) for j, w in enumerate(row) if w > 0)
         for row in W]
    return sum(p[i]*D[i] for i in range(8)), D


def entropy_mi(p, W):
    q = [sum(p[i]*W[i][j] for i in range(8)) for j in range(15)]
    return entropy(q) - sum(p[i]*entropy(W[i]) for i in range(8))


def masses_to_p(a, b, c):
    return [a/2, b/4, c/2, b/4, b/4, c/2, b/4, a/2]


def log2sumexp(a, b):
    m = max(a, b)
    return m + math.log2(2**(a-m) + 2**(b-m))


def optimum(d):
    """Solve (1) in the log odds v=log2(a/(1-a))."""
    k = d/(1-d)
    logR = 1+2*k
    r = 1/(1+2**(-logR))
    L = log2sumexp(0, logR) - 3*k*math.log2(3)

    def G(v):
        # 2(1-a)/(1+2a)=2/(1+3*2^v).
        return -v + 2*k*(1-log2sumexp(0, math.log2(3)+v)) + 3*k*k*H0-L

    lo, hi = -4.0, max(4.0, 4*k*k+4)
    assert G(lo) > 0 and G(hi) < 0
    for _ in range(100):
        mid = (lo+hi)/2
        if G(mid) > 0:
            lo = mid
        else:
            hi = mid
    v = (lo+hi)/2
    rest = 1/(1+2**v)
    a = 1-rest
    b, c = rest*r, rest*(1-r)
    s = 1-d
    F = (3*d*d*s*(1-rest*H0)
         + 3*d*s*s*(1+entropy([(1+2*a)/3, 2*rest/3]))
         + s**3*(1+entropy([a, rest])+rest*L))
    return (a, b, c), F, G(v)


def blahut_arimoto(W, tolerance=2e-12):
    # Intentionally asymmetric initial law; no orbit reduction here.
    p = [x/36 for x in range(1, 9)]
    for iteration in range(100000):
        I, D = divergences(p, W)
        gap = max(D)-I
        if gap < tolerance:
            return I, gap, iteration, p
        p = [p[i]*2**D[i] for i in range(8)]
        z = sum(p)
        p = [x/z for x in p]
    raise AssertionError(('BA iteration cap', gap))


def direct_markov_score(k):
    """Independent scalar criterion from channel divergences, not formula B."""
    theta = 1/(1+2**(2*k))
    a, b, c = (1-theta)**2, 2*theta*(1-theta), theta**2
    p = masses_to_p(a, b, c)
    _, D = divergences(p, channel_masks(k/(1+k)))
    r = b/(b+c)
    return D[0] - r*D[1] - (1-r)*D[2]


def bisect(fun, lo, hi, steps):
    assert fun(lo) > 0 and fun(hi) < 0
    for _ in range(steps):
        mid = (lo+hi)/2
        if fun(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def decimal_root():
    with localcontext() as ctx:
        ctx.prec = 90
        one, two, three = Decimal(1), Decimal(2), Decimal(3)
        log2 = two.ln()
        h0 = three.ln()/log2-two/three

        def B(k):
            z = (two*k*log2).exp()
            ratio = two*(two*z+one)/(three*z*z+two*z+one)
            return -4+two*ratio.ln()/log2+three*k*h0+three*three.ln()/log2

        k = bisect(B, one, two, 280)
        d = k/(one+k)
        theta = one/(one+(two*k*log2).exp())
        return str(k), str(d), str(theta), str(B(k))


def poly_mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def run():
    checks = {}
    # Independent exact channel constructions and rational normalization.
    exact_rows = 0
    for d in (Fraction(1, 100), Fraction(1, 2), Fraction(13, 20), Fraction(9, 10)):
        A, B = channel_masks(d), channel_one_deletion_recurrence(d)
        assert A == B
        for row in A:
            assert sum(row) == 1
            exact_rows += 1
    checks['exact_rational_rows_compared_and_normalized'] = exact_rows

    # Independent polynomial multiplication audit of the concavity numerator.
    left = poly_mul([1, 6, 3], poly_mul([1, 2], [1, 2]))
    right = poly_mul([1, 2, 3], [1, 2, 3])
    difference = [a-b for a, b in zip(left, right)]
    assert difference == [0, 6, 21, 24, 3]
    checks['concavity_polynomial_coefficients_ascending'] = difference

    # Exact integer endpoint checks, generated from their rational ratios.
    ratio1 = Fraction(6, 19)**2 * 3**6 / 2**6
    ratio2 = Fraction(22, 267)**2 * 3**9 / 2**8
    assert ratio1 > 1 > ratio2
    assert ratio1 == Fraction(26244, 23104)
    assert ratio2 == Fraction(9526572, 18249984)
    checks['B1_log_argument_exact_reduced'] = str(ratio1)
    checks['B2_log_argument_exact_reduced'] = str(ratio2)

    k_text, d_text, theta_text, residual = decimal_root()
    k_direct = bisect(direct_markov_score, 1.0, 2.0, 55)
    assert abs(k_direct-float(k_text)) < 2e-12
    checks['root_k_decimal_90_digits'] = k_text
    checks['root_d_decimal_90_digits'] = d_text
    checks['root_theta_decimal_90_digits'] = theta_text
    checks['decimal_B_residual'] = residual
    checks['root_k_independent_channel_divergences_binary64'] = k_direct

    # Formula audit away from the optimum: random orbit laws vs raw channel entropy.
    rng = random.Random(117)
    max_random_error = 0.0
    for _ in range(100):
        d = rng.uniform(.005, .95)
        z = [rng.uniform(.01, 1) for _ in range(3)]
        a, b, c = [x/sum(z) for x in z]
        s = 1-d
        t = (1+2*a)/3
        formula = (3*d*d*s*(1-(1-a)*H0)
                   +3*d*s*s*(1+entropy([t, 1-t])-b*H0-c*math.log2(3))
                   +s**3*(1+entropy([a,b,c])+b))
        raw = entropy_mi(masses_to_p(a,b,c), channel_masks(d))
        max_random_error = max(max_random_error, abs(raw-formula))
    assert max_random_error < 1e-13
    checks['random_orbit_laws_checked'] = 100
    checks['max_formula_error_on_random_laws_bits'] = max_random_error

    rows = []
    for d in [.01, .05, .1, .25, .5, float(d_text), .6, .65, .75, .9]:
        masses, formula, g_residual = optimum(d)
        a, b, c = masses
        p, W = masses_to_p(*masses), channel_masks(d)
        raw, D = divergences(p, W)
        entropy_raw = entropy_mi(p, W)
        dual_gap = max(D)-raw
        spread = max(D)-min(D)
        assert abs(raw-formula) < 2e-13
        assert abs(raw-entropy_raw) < 2e-13
        assert spread < 2e-11
        # Both finite DMC lower (achieved I) and upper (max row divergence).
        row = dict(d=d, a=a, b=b, c=c, M3_bits=formula,
                   M3_per_input_bit=formula/3,
                   raw_mask_mutual_information_bits=raw,
                   raw_entropy_mutual_information_bits=entropy_raw,
                   numerical_dual_gap_bits=dual_gap,
                   row_divergence_spread_bits=spread,
                   scalar_derivative_residual=g_residual,
                   markov_constraint_b_squared_minus_4ac=b*b-4*a*c)
        if .05 <= d <= .65:
            ba_I, ba_gap, iters, ba_p = blahut_arimoto(W)
            assert abs(ba_I-formula) < 4e-12
            row.update(BA_I_bits=ba_I, BA_gap_bits=ba_gap, BA_iterations=iters,
                       BA_max_probability_difference=max(abs(x-y) for x,y in zip(p,ba_p)))
        rows.append(row)

    # Audit the extra half-deletion cubic by integer polynomial multiplication.
    constant_cube = [81*x for x in poly_mul(poly_mul([1,-1],[1,-1]),[1,-1])]
    rhs = [0]+poly_mul([1,2],[1,2])
    cubic = [y-x for x,y in zip(constant_cube,rhs)]
    assert cubic == [-81,244,-239,85]
    half = next(row for row in rows if row['d'] == .5)
    a = half['a']
    cubic_residual = 85*a**3-239*a*a+244*a-81
    divergence_formula = 3/8+3/8*math.log2(6/(1+2*a))+1/8*math.log2(2/a)
    assert abs(cubic_residual) < 1e-12
    assert abs(divergence_formula-half['M3_bits']) < 2e-14
    checks['half_deletion_cubic_coefficients_ascending'] = cubic
    checks['half_deletion_cubic_residual'] = cubic_residual
    checks['half_deletion_divergence_formula_bits'] = divergence_formula
    checks['half_deletion_optimal_a'] = a
    # Cubic root independently, avoiding logarithms and the G solver.
    cubic_root=bisect(lambda x: -(85*x**3-239*x*x+244*x-81),0.0,1.0,60)
    assert abs(cubic_root-a) < 3e-14
    checks['half_deletion_cubic_root_independent_binary64'] = cubic_root

    # The limiting d=0 formula is exactly uniform, and d=1 has zero MI.
    p_uniform = [1/8]*8
    assert abs(divergences(p_uniform, channel_masks(0.0))[0]-3) < 1e-14
    assert abs(divergences(p_uniform, channel_masks(1.0))[0]) < 1e-14
    checks['endpoint_mutual_information_uniform_input'] = {'d=0': 3, 'd=1': 0}

    # Independent numerical second derivatives versus (17), at varied k.
    second_derivative_errors = []
    def B_float(k):
        z = 2**(2*k)
        return -4 + 2*math.log2(2*(2*z+1)/(3*z*z+2*z+1)) + 3*k*H0 + 3*math.log2(3)
    for k in [0.0, .1, 1.0, 2.0, 4.0]:
        z=2**(2*k)
        f=3*z*z+2*z+1
        analytic=8*LN2*(2*z/(2*z+1)**2 - 2*z*(3*z*z+6*z+1)/(f*f))
        step=.001
        numerical=(B_float(k+step)-2*B_float(k)+B_float(k-step))/step**2
        assert analytic < 0
        assert abs(analytic-numerical) < 1e-6
        second_derivative_errors.append(abs(analytic-numerical))
    checks['max_second_derivative_finite_difference_error'] = max(second_derivative_errors)

    # Report resource use; macOS ru_maxrss is bytes, Linux is KiB.
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss*1024
    assert rss_bytes < 1024**3
    checks['peak_rss_bytes'] = rss_bytes
    checks['elapsed_seconds'] = time.monotonic()-START
    try:
        checks['observed_nice'] = os.getpriority(os.PRIO_PROCESS, 0)
    except (AttributeError, OSError) as exc:
        checks['observed_nice'] = 'unavailable: '+str(exc)
    result = {'status': 'all checks passed',
              'precision_notice': 'Decimal and binary64 checks are not directed interval certificates. The theorem and rational root bracket are proved in PROOF.md.',
              'checks': checks, 'rows': rows}
    Path('results.json').write_text(json.dumps(result, indent=2)+'\n')
    fields = ['d','a','b','c','M3_bits','M3_per_input_bit','numerical_dual_gap_bits',
              'markov_constraint_b_squared_minus_4ac']
    with Path('results.csv').open('w', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    output = [
        'All checks passed.',
        'Exact rational channel rows verified: '+str(exact_rows),
        'Random orbit-law formula checks: 100; maximum error %.3g bits' % max_random_error,
        'Concavity numerator coefficients (ascending): '+str(difference),
        'Exact B(1) log argument: '+str(ratio1)+' > 1',
        'Exact B(2) log argument: '+str(ratio2)+' < 1',
        'k_* (Decimal, 90-digit working precision): '+k_text,
        'd_* (Decimal, 90-digit working precision): '+d_text,
        'theta_* (Decimal, 90-digit working precision): '+theta_text,
        'k_* (independent raw-channel criterion): %.16g' % k_direct,
        'Maximum optimum row-divergence spread: %.3g bits' % max(row['row_divergence_spread_bits'] for row in rows),
        'Unconstrained asymmetric-start BA runs: '+str(sum('BA_I_bits' in row for row in rows)),
        'Half-deletion cubic coefficients (ascending): '+str(cubic),
        'Half-deletion optimal a: %.16g' % a,
        'Half-deletion M3 from independent divergence formula: %.16g bits' % divergence_formula,
        'Observed nice: '+str(checks['observed_nice']),
        'Peak RSS: %.2f MiB' % (rss_bytes/1024**2),
        'Elapsed: %.3f seconds' % checks['elapsed_seconds'],
        'Data: results.json, results.csv',
        'd          M3(d)/3         b^2-4ac',
    ]
    output += ['%.9f  %.12f  %+.9g' % (row['d'],row['M3_per_input_bit'],row['markov_constraint_b_squared_minus_4ac']) for row in rows]
    text='\n'.join(output)+'\n'
    Path('computation_output.txt').write_text(text)
    with Path('LOG.md').open('a') as f:
        f.write('\n## Step 4: numerical and independent algebra audit\n\nExact command:\n\n```sh\n'+COMMAND+'\n```\n\nOutput (the launch also reports `nice: setpriority: Operation not permitted`):\n\n```text\n'+text+'```\n\nThe decimal root values are numerical estimates, not outward-rounded enclosures. The exact root bracket (1/2,2/3) is established by rational inequalities in the proof. Every input law was checked directly against the channel, including the exceptional Markov candidate. Raw deletion-mask enumeration and a separate recursive construction agree exactly over rational probabilities. BA makes no symmetry assumption and begins asymmetrically.\n')
    print(text, end='')


if __name__ == '__main__':
    with Path('LOG.md').open('a') as f:
        f.write('\nStarting audit command: `'+COMMAND+'`. Wall alarm: 180 seconds.\n')
    try:
        run()
    except Exception:
        import traceback
        with Path('LOG.md').open('a') as f:
            f.write('\nAudit failed:\n\n```text\n'+traceback.format_exc()+'```\n')
        raise
