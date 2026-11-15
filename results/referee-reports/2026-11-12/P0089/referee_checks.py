"""Exact finite-history checks and readable comparisons of independent outputs."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import signal
import time

signal.alarm(240)


def finite_histories(forced):
    n, m = 6, 2
    prescribed = {(2, 0): 0, (4, 1): 2}  # zero-based labels, valid older targets
    degrees = [0] * n
    total_mass = F(0)
    event_mass = [F(0), F(0)]
    weighted_mass = [F(0), F(0)]
    degree_second = F(0)
    leaves = 0

    def f(k):
        return F(1) + F(1, 2) * (-1) ** k

    def visit(v, slot, prob, likelihood, event):
        nonlocal total_mass, degree_second, leaves
        if v == n:
            leaves += 1
            total_mass += prob
            degree_second += prob * sum(k*k for k in degrees) / n
            tests = [True, degrees[0] == 3]
            for j, test in enumerate(tests):
                if event and test:
                    event_mass[j] += prob
                if test:
                    weighted_mass[j] += prob * likelihood
            assert sum(degrees) == m*(n-1)
            return
        ws = [f(degrees[i]) for i in range(v)]
        S = sum(ws)
        target = prescribed.get((v, slot))
        candidates = [target] if forced and target is not None else range(v)
        for i in candidates:
            orig_p = ws[i] / S
            p = F(1) if forced and target is not None else orig_p
            degrees[i] += 1
            next_v, next_slot = (v+1, 0) if slot+1 == m else (v, slot+1)
            visit(next_v, next_slot, prob*p,
                  likelihood * orig_p if target is not None else likelihood,
                  event and (target is None or target == i))
            degrees[i] -= 1

    visit(1, 0, F(1), F(1), True)
    return total_mass, event_mass, weighted_mass, degree_second, leaves


def law(name, m, c, count=10000):
    def f(k):
        if name == "sqrt": return math.sqrt(k+1)
        if name == "log": return math.log(k+2)
        if name == "osc": return math.sqrt(k+1) + (0.4 if k % 2 == 0 else -0.4)
        if name == "two": return 1 if k == 0 else 2
        return 1
    R, out = 1.0, []
    for k in range(count):
        out.append(R*c/(c+m*f(k)))
        R *= m*f(k)/(c+m*f(k))
    return out


def main():
    start = time.monotonic()
    ordinary, forced = finite_histories(False), finite_histories(True)
    assert ordinary[0] == forced[0] == 1
    assert ordinary[1] == forced[2]
    print("EXACT FORCED-SLOT IDENTITY")
    print(f"original histories={ordinary[4]}, forced histories={forced[4]}")
    print(f"total probabilities original={ordinary[0]} forced={forced[0]}")
    for label, x, y in zip(("1", "D_1(6)=3"), ordinary[1], forced[2]):
        print(f"Psi={label}: original={x}; forced-weighted={y}; difference={x-y}")
    print(f"finite E[D_U^2]={ordinary[3]} = {float(ordinary[3]):.12g} (bound 78)")
    print()

    th = {(d['name'], d['m']): d for d in json.loads(Path('referee_theory.json').read_text())}
    sims = json.loads(Path('referee_simulations.json').read_text())
    print("SCALAR ROOTS: c, p0..p3, mean, explicit tail bound")
    for key, d in th.items():
        print(f"{key}: c={d['c']}; p={d['p0_to_p10'][:4]}; mean={d['mean']}; tail<={d['series_tail_bound']}")
    print()
    print("SIMULATION COMPARISONS (signed errors and complete histogram L1)")
    for s in sims:
        t = th[s['name'], s['m']]
        p = law(s['name'], s['m'], float(t['c']))
        hist = s['histogram']
        l1 = sum(abs((hist[k]/s['n'] if k < len(hist) else 0)-pk) for k,pk in enumerate(p))
        diffs = [s['p0_to_p10'][k]-float(t['p0_to_p10'][k]) for k in range(4)]
        print(f"{s['name']} m={s['m']} s={s['seed']} S={s['S_over_n']:.9f} dS={s['S_over_n']-float(t['c']):+.7f} "
              f"p0..3={s['p0_to_p10'][:4]} dp={[round(v,8) for v in diffs]} L1={l1:.7f} max={s['max_degree']} "
              f"star={s['ball_star0']:.6f} H0={s['ball_H0']:.6f} dH0={s['ball_H0']-float(t['ball_H0']):+.8f} "
              f"H1={s['ball_H1']:.6f} dH1={s['ball_H1']-float(t['ball_H1']):+.8f} "
              f"rootp0..3={s['root_sample_p0_to_p10'][:4]} rootmean={s['root_sample_mean']:.5f}")
    print()
    print("AUTHOR DATA: numerical agreement and the iid-standard-deviation claim")
    worst = (0, None)
    for file in sorted(Path('data').glob('*.json')):
        s = json.loads(file.read_text())
        for source, name in [('two_level','two'), ('sqrt_rule','sqrt')]:
            t = th[name, 2]
            P = list(map(float, t['p0_to_p10']))
            for k, value in enumerate(s[source]['sim_degree_law'][:4]):
                z = abs(value-P[k])/math.sqrt(P[k]*(1-P[k])/s['n'])
                if z > worst[0]: worst = z, (str(file), name, k, value, P[k])
            own_theory = s[source]['theory']
            old_c = own_theory.get('c', own_theory.get('c_f'))
            print(f"{file} {name}: claimed c error={old_c-float(t['c']):+.3g}; "
                  f"max p0..3 absolute error={max(abs(x-y) for x,y in zip(s[source]['sim_degree_law'][:4], P)):.7g}")
        b = s['two_level']['sim_ball2_fraction_all_roots']
        target = float(th['two',2]['ball_H0'])
        z = abs(b-target)/math.sqrt(target*(1-target)/s['n'])
        print(f"  H0={b:.12f}, discrepancy={b-target:+.9f}, iid scale ratio={z:.6f}")
        if z > worst[0]: worst = z, (str(file),'two','H0',b,target)
    print(f"maximum iid scale ratio={worst[0]:.9f}; entry={worst[1]}")
    two = th['two',2]
    c = float(two['c']); lam = 2/c
    print(f"two-level parent age-ratio mean independently={ (1-1/(lam+2))/c:.15f}")
    print(f"elapsed_seconds={time.monotonic()-start:.3f}")


if __name__ == '__main__':
    main()
