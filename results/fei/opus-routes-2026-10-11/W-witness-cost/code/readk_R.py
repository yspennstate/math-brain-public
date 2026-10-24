"""EVIDENCE: rank term R (Proposition 12.1) on random read-k decision trees (each variable labels at most k nodes).
Leaves random +-1 (adjacent leaves not merged). Reports, per k, the max over samples of H/I, the exact witness-sum
code length/I, R_path/I and R_adapt/I (best of b = +-1). Usage: python readk_R.py n depth samples seed"""
import random, math, sys
from fractions import Fraction
import fei_core as fc
from dt_code_exhaustive import code_from_leaves
from random_R import R_term


def random_readk_tree(rng, n, depth, k):
    budget = [k] * n
    leaves = []

    def rec(fixed, d):
        cand = [v for v in range(n) if v not in fixed and budget[v] > 0]
        if d == 0 or not cand or (d < depth and rng.random() < 0.15):
            leaves.append((dict(fixed), rng.choice([1, -1])))
            return
        v = rng.choice(cand)
        budget[v] -= 1
        for b in (0, 1):
            fixed[v] = b
            rec(fixed, d - 1)
            del fixed[v]

    rec({}, depth)
    return leaves


def table_from_leaves(leaves, n):
    T = [0] * (1 << n)
    for fixed, out in leaves:
        free = [v for v in range(n) if v not in fixed]
        base = 0
        for v, b in fixed.items():
            if b:
                base |= 1 << v
        for a in range(1 << len(free)):
            x = base
            for i, v in enumerate(free):
                if (a >> i) & 1:
                    x |= 1 << v
            T[x] = out
    assert all(t != 0 for t in T)
    return T


if __name__ == '__main__':
    n, depth, samples, seed = map(int, sys.argv[1:5])
    rng = random.Random(seed)
    for k in (1, 2, 3, 4, 6, 8):
        worst = {'H': 0, 'code': 0, 'Rp': 0, 'Ra': 0}
        done = 0
        while done < samples:
            leaves = random_readk_tree(rng, n, depth, k)
            T = table_from_leaves(leaves, n)
            H, I, v, masses = fc.entropy_influence_exact(T)
            if I == 0:
                continue
            fm = {S: float(m) for S, m in masses.items()}
            best = {}
            for b in (1, -1):
                cs, cm = code_from_leaves(fm, float(v), leaves, b, n)
                best['code'] = min(best.get('code', math.inf), cs)
                best['Rp'] = min(best.get('Rp', math.inf), R_term(masses, leaves, b, False))
                best['Ra'] = min(best.get('Ra', math.inf), R_term(masses, leaves, b, True))
            I = float(I)
            worst['H'] = max(worst['H'], H / I)
            for key in ('code', 'Rp', 'Ra'):
                worst[key] = max(worst[key], best[key] / I)
            done += 1
        print(f"k={k}: max H/I={worst['H']:.3f} code/I={worst['code']:.3f} R_path/I={worst['Rp']:.3f} R_adapt/I={worst['Ra']:.3f}", flush=True)
