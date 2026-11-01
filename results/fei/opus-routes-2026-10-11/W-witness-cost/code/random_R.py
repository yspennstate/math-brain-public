"""Random functions on n = 5, 6 (EVIDENCE): greedy reduced decision tree (query the most influential variable
of the current subfunction), both level sets b = +-1, path order and adapted order; report R/I and the exact
witness-sum code length/I (queue law, lambda = 1). Also biased random functions (P(f=1) = rho)."""
import random, math, sys
from fractions import Fraction
import fei_core as fc
from dt_code_exhaustive import code_from_leaves

def greedy_leaves(T, n):
    leaves = []
    def sub_table(fixed):
        free = [v for v in range(n) if v not in fixed]
        vals = []
        for a in range(1 << len(free)):
            x = 0
            for v, b in fixed.items():
                if b: x |= 1 << v
            for k, v in enumerate(free):
                if (a >> k) & 1: x |= 1 << v
            vals.append((x, T[x]))
        return free, vals
    def rec(fixed):
        free, vals = sub_table(fixed)
        outs = set(t for _, t in vals)
        if len(outs) == 1:
            leaves.append((dict(fixed), outs.pop())); return
        best, bv = None, -1
        for v in free:
            cnt = sum(1 for x, t in vals if T[x ^ (1 << v)] != t)
            if cnt > bv: best, bv = v, cnt
        for b in (0, 1):
            fixed[best] = b; rec(fixed); del fixed[best]
    rec({})
    return leaves

def R_term(masses, leaves, target, adaptive):
    gates = [(list(fx.keys()), Fraction(1, 1 << len(fx))) for fx, out in leaves if out == target]
    owners = {}
    for S, m in masses.items():
        if S == 0: continue
        owners[S] = [g for g, (pv, p) in enumerate(gates) if all(((S >> u) & 1) == 0 or u in pv for u in range(S.bit_length()))]
    orders = []
    for g, (pv, p) in enumerate(gates):
        if not adaptive:
            orders.append({v: i + 1 for i, v in enumerate(pv)}); continue
        w = {v: 0.0 for v in pv}
        for S, own in owners.items():
            if g in own:
                tot = sum(gates[h][1] for h in own)
                s = fc.popcount(S)
                for v in pv:
                    if (S >> v) & 1: w[v] += float(masses[S]) * float(p / tot) / s
        orders.append({v: i + 1 for i, v in enumerate(sorted(pv, key=lambda v: -w[v]))})
    R = 0.0
    for S, own in owners.items():
        s = fc.popcount(S); tot = sum(gates[h][1] for h in own)
        R += float(masses[S]) * sum(float(gates[h][1] / tot) * sum(max(0.0, math.log2(orders[h][u] / s)) for u in range(S.bit_length()) if (S >> u) & 1) for h in own)
    return R

if __name__ == '__main__':
    n, cnt, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    worst = {'Rpath': (0,), 'Radapt': (0,), 'code': (0,), 'H': (0,)}
    for t in range(cnt):
        rho = rng.choice([0.5, 0.5, 0.25, 0.1, 0.03])
        T = [1 if rng.random() < rho else -1 for _ in range(1 << n)]
        H, I, v, masses = fc.entropy_influence_exact(T)
        if I == 0: continue
        lv = greedy_leaves(T, n)
        fm = {S: float(m) for S, m in masses.items()}
        best = {}
        for b in (1, -1):
            cs, cm = code_from_leaves(fm, float(v), lv, b, n)
            rp = R_term(masses, lv, b, False); ra = R_term(masses, lv, b, True)
            for k, val in (('code', cs), ('Rpath', rp), ('Radapt', ra)):
                best[k] = min(best.get(k, math.inf), val)
        I = float(I)
        for k in ('Rpath', 'Radapt', 'code'):
            if best[k] / I > worst[k][0]: worst[k] = (best[k] / I, rho)
        if H / I > worst['H'][0]: worst['H'] = (H / I, rho)
    print(f"n={n} samples={cnt}: max H/I={worst['H'][0]:.3f}; max code/I={worst['code'][0]:.3f} (rho={worst['code'][1]}); "
          f"max R_path/I={worst['Rpath'][0]:.3f}; max R_adapt/I={worst['Radapt'][0]:.3f} (rho={worst['Radapt'][1]})")
