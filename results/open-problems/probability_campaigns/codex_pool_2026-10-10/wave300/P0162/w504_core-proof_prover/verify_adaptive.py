"""Independent truth-table verification of w504's adaptive-coordinate lemma.

Uses only integer Walsh transforms and stdlib floating entropy. Numerical checks
do not prove the universal conjecture. All writes stay in this worker folder.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CPU0 = time.process_time()
WALL0 = time.monotonic()
MAX_ERR = 0.0
SIGNED_CHECKS = 0


def gate_check():
    if time.process_time() - CPU0 > 20:
        raise RuntimeError("fresh CPU gate exhausted")
    if time.monotonic() - WALL0 > 60:
        raise RuntimeError("fresh wall-time gate exhausted")


def check_close(actual, expected, tol=2e-10):
    global MAX_ERR
    err = abs(actual - expected)
    MAX_ERR = max(MAX_ERR, err)
    if err > tol:
        raise AssertionError((actual, expected, err))


def walsh(values):
    result = list(values)
    step = 1
    while step < len(result):
        for start in range(0, len(result), 2 * step):
            for j in range(start, start + step):
                u, v = result[j], result[j + step]
                result[j], result[j + step] = u + v, u - v
        step *= 2
    return result


def entropy(nums):
    denom = len(nums) ** 2
    return math.fsum(
        -(num * num / denom) * math.log2(num * num / denom)
        for num in nums if num
    )


def influences(nums):
    n = len(nums).bit_length() - 1
    denom = len(nums) ** 2
    return [sum(v * v for s, v in enumerate(nums) if s & (1 << j)) / denom
            for j in range(n)]


def restrict(values, coordinate, bit):
    low_mask = (1 << coordinate) - 1
    return [values[(x & low_mask) | ((x >> coordinate) << (coordinate + 1))
                   | (bit << coordinate)] for x in range(len(values) // 2)]


def h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def defect_formula(plus_nums, minus_nums):
    denom = len(plus_nums) ** 2
    total = 0.0
    infl = 0.0
    for u, v in zip(plus_nums, minus_nums):
        norm = u * u + v * v
        if not norm:
            continue
        w = norm / (2 * denom)
        p = u * u / norm
        q = (u - v) ** 2 / (2 * norm)
        total += w * (1 + h2(q) - h2(p))
        infl += w * q
    return total, infl


def L(a, c, d):
    terms = []
    for eps in [-1, 1]:
        r = (1 - c * eps * a) ** 2
        terms.append(0.0 if not r else (1 + eps * d) * r * math.log2(r) / 2)
    return math.fsum(terms)


def family(m):
    assert m % 2 == 0 and 2 <= m <= 12
    def core(b):
        exponent = sum(((b >> j) & 1) * ((b >> (j + 1)) & 1)
                       for j in range(0, m, 2))
        return 1 if exponent % 2 == 0 else -1
    base = [core(b) for b in range(1 << m)]
    # z is the most significant bit; the exceptional flip is in z=1.
    return base + [-1 if b == 0 else value for b, value in enumerate(base)]


def verify_family(m):
    global SIGNED_CHECKS
    values = family(m)
    nums = walsh(values)
    H = entropy(nums)
    inf = influences(nums)
    t, a = 2.0 ** (-m), 2.0 ** (-m / 2)
    check_close(H, m * (1 + t) - L(a, 1, a))
    check_close(inf[m], t)
    check_close(sum(inf), m / 2 + (m + 1) * t)
    coord_rows = []
    for j in range(m):
        gate_check()
        n0 = walsh(restrict(values, j, 0))
        n1 = walsh(restrict(values, j, 1))
        # The exceptional point has partner bit 0 and selector z=1. The
        # three nonzero control blocks consequently have numerator -2
        # when z is absent and +2 when z is present (denominator 2^m).
        partner = j ^ 1
        partner_after_restriction = partner if partner < j else partner - 1
        selector_mask = 1 << (m - 1)
        control_mask = selector_mask | (1 << partner_after_restriction)
        for s, numerator in enumerate(n0):
            if s & control_mask:
                assert numerator == (2 if s & selector_mask else -2)
                SIGNED_CHECKS += 1
        H0, H1 = entropy(n0), entropy(n1)
        check_close(H1, m - 2)
        check_close(H0, m - 2 + 3 * m * t - L(a, 1, 2 * a))
        delta = H - (H0 + H1) / 2
        expected = 2 - m * t / 2 - L(a, 1, a) + L(a, 1, 2 * a) / 2
        check_close(delta, expected)
        check_close(inf[j], 0.5 + t)
        identity, identity_inf = defect_formula(n0, n1)
        check_close(identity, delta)
        check_close(identity_inf, inf[j])
        check_close(sum(inf), (sum(influences(n0)) + sum(influences(n1))) / 2 + inf[j])
        assert delta <= 2 - m * t / 2 + 2e-10
        assert delta <= 4 * inf[j] + 2e-10
        # Independently inspect the edge definition of influence.
        exact_edge_count = sum(values[x] != values[x ^ (1 << j)]
                               for x in range(len(values)))
        assert exact_edge_count * (1 << m) == (len(values) * ((1 << (m - 1)) + 1))
        coord_rows.append({"coordinate":j,"H0":H0,"H1":H1,"delta":delta,
                           "influence":inf[j],"delta_over_influence":delta/inf[j]})
    assert H <= 2 * sum(inf) + 2e-10
    # Selector comparison is obtained from the same table, solely as a control
    # for the new coordinate-selection claim, not as a separate obstruction run.
    z0, z1 = walsh(restrict(values, m, 0)), walsh(restrict(values, m, 1))
    zdelta = H - (entropy(z0) + entropy(z1)) / 2
    return {"m":m,"dimension":m+1,"truth_table_entries":len(values),"H":H,
            "I":sum(inf),"H_over_I":H/sum(inf),
            "selector_delta_over_influence":zdelta/inf[m],"base_coordinates":coord_rows}


def verify_identity_cases():
    rng = random.Random(504)
    cases = [[1]*16, [-1]*16, [(-1)**x.bit_count() for x in range(16)],
             [-1 if x == 0 else 1 for x in range(16)]]
    cases.extend([[rng.choice([-1, 1]) for _ in range(16)] for _ in range(12)])
    count = 0
    for values in cases:
        nums = walsh(values)
        H, inf = entropy(nums), influences(nums)
        for j in range(4):
            n0, n1 = walsh(restrict(values,j,0)), walsh(restrict(values,j,1))
            delta = H - (entropy(n0)+entropy(n1))/2
            predicted, predicted_inf = defect_formula(n0,n1)
            check_close(delta,predicted)
            check_close(inf[j],predicted_inf)
            check_close(sum(inf),(sum(influences(n0))+sum(influences(n1)))/2+inf[j])
            count += 1
        gate_check()
    return {"functions":len(cases),"coordinate_checks":count,"seed":504,
            "dimensions":[4],"edge_cases":["constant +/-1","parity","one-point flip"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate",required=True)
    args = parser.parse_args()
    gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    assert args.gate == gate['gate_id'] and args.gate in ['adaptive-n13-cpu20','adaptive-n13-cpu20-signed']
    assert gate['worker'] == 'w504' and gate['cpu_only'] and gate['no_background']
    results = {"gate":args.gate,"command":gate['command'],"status":"RUNNING",
               "formal_proof":False,"independent_review":"C001-C004 KEEP by w506; auxiliary signed coefficients checked by worker",
               "families":[],"identity_checks":None}
    for m in [2,6,10,12]:
        row = verify_family(m)
        results['families'].append(row)
        # Checkpoint each completed row; an interruption cannot erase earlier rows.
        (ROOT/'measurements.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    results['identity_checks']=verify_identity_cases()
    results['max_absolute_identity_residual']=MAX_ERR
    results['signed_auxiliary_coefficient_checks']=SIGNED_CHECKS
    results['cpu_seconds']=time.process_time()-CPU0
    results['wall_seconds']=time.monotonic()-WALL0
    gate_check()
    results['status']='PASS'
    (ROOT/'measurements.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({"status":results['status'],"families":len(results['families']),
                      "base_coordinate_checks":sum(len(r['base_coordinates']) for r in results['families']),
                      "identity_coordinate_checks":results['identity_checks']['coordinate_checks'],
                      "signed_auxiliary_coefficient_checks":SIGNED_CHECKS,
                      "max_residual":MAX_ERR,"cpu_seconds":results['cpu_seconds'],
                      "wall_seconds":results['wall_seconds'],
                      "largest_family":{"m":12,"selector_ratio":results['families'][-1]['selector_delta_over_influence'],
                                        "base_ratio":results['families'][-1]['base_coordinates'][0]['delta_over_influence']}}))


if __name__=='__main__':
    main()
