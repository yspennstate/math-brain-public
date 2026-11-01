"""Exact check of Theorem 11.1 on small equal-mean term decision lists:
truth table -> integer Walsh spectrum -> exact queue-law witness sums over ALL single-root witnesses,
with the deficit order inside each unfolded-path gate (true block first, then false prefixes by
increasing deficit, ties to earlier blocks). Reports H/I, witness-sum code length / I, and the bound 27.
Also reports the natural path order for comparison. Floating-point logs (EVIDENCE)."""
import itertools
import math
import random
import fei_core as fc
from rodt import and_table, or_table
from queue_cost import elem_sym, h2

A_EXP = 6.0 / 5.0


def leaf_tables(kind, u):
    if kind == 'dict':
        return [1, -1], 1
    if kind == 'and':
        return and_table(u), u
    if kind == 'or':
        return or_table(u), u
    raise ValueError


def build(widths, outs):
    m = len(widths)
    var = 0
    blocks = []
    for w in widths:
        blocks.append(list(range(var, var + w)))
        var += w
    oblocks = []
    otabs = []
    for kind, u in outs:
        T, size = leaf_tables(kind, u)
        oblocks.append(list(range(var, var + size)))
        otabs.append(T)
        var += size
    n = var

    def f(x):
        for k in range(m):
            if all(((x >> v) & 1) == 0 for v in blocks[k]):
                j = k
                break
        else:
            j = m
        loc = 0
        for i, v in enumerate(oblocks[j]):
            if (x >> v) & 1:
                loc |= 1 << i
        return otabs[j][loc]

    T = [f(x) for x in range(1 << n)]
    # gates
    gates = []
    for j in range(m + 1):
        for t in itertools.product(*[range(1, widths[k] + 1) for k in range(j)]):
            segs = []
            for k in range(j):
                segs.append(('pre', k, t[k], widths[k] - t[k]))
            gates.append((j, t, segs))
    return T, n, blocks, oblocks, otabs, gates, widths


def gate_info(j, t, segs, blocks, oblocks, otabs, widths, m, order):
    # cell probability and P(g_j = 1)
    q = [2.0 ** (-w) for w in widths]
    p = 1.0
    for k in range(j):
        p *= 2.0 ** (-t[k])
    if j < m:
        p *= q[j]
    P = sum(1 for v in otabs[j] if v == 1) / len(otabs[j])
    pi = min(p * P, 0.5)
    # ordering of control variables
    if order == 'deficit':
        pre = sorted(segs, key=lambda g: (g[3], g[1]))
    else:
        pre = segs
    seq = []
    if order == 'deficit' and j < m:
        seq += blocks[j]
    for _, k, tk, _ in pre:
        seq += blocks[k][:tk]
    if order != 'deficit' and j < m:
        seq += blocks[j]
    ranks = {v: i + 1 for i, v in enumerate(seq)}
    # output ranks (desirability order of the leaf)
    ok, sign, ordr = fc.is_unate_regular(otabs[j])
    assert ok
    oranks = {oblocks[j][kl]: i + 1 for i, kl in enumerate(ordr)}
    R = 0
    for v in list(ranks) + list(oranks):
        R |= 1 << v
    return pi, ranks, oranks, R


def code_length(T, n, blocks, oblocks, otabs, gates, widths, order):
    m = len(widths)
    H, I, v, masses = fc.entropy_influence_exact(T)
    infos = [gate_info(j, t, segs, blocks, oblocks, otabs, widths, m, order) for j, t, segs in gates]
    infos = [g for g in infos if g[0] > 0]
    Lam = sum(math.log1p(g[0]) for g in infos) / math.log(2)
    total = h2(v) + float(v) * Lam
    Zcache = {}
    for S, mass in masses.items():
        if S == 0:
            continue
        s = fc.popcount(S)
        acc = 0.0
        for gi, (pi, ranks, oranks, R) in enumerate(infos):
            if S & ~R:
                continue
            key = (gi, s)
            if key not in Zcache:
                th = [min(1.0, (s / r) ** A_EXP) for r in ranks.values()] + [min(1.0, (s / r) ** A_EXP) for r in oranks.values()]
                Zcache[key] = elem_sym(th, s)[s]
            lp = math.log2(pi) - math.log2(s * (s + 1)) - 1 - math.log2(Zcache[key])
            x = S
            k = 0
            while x:
                if x & 1:
                    r = ranks.get(k, oranks.get(k))
                    lp += math.log2(min(1.0, (s / r) ** A_EXP))
                x >>= 1
                k += 1
            acc += 2.0 ** lp
        assert acc > 0
        total += float(mass) * (-math.log2(acc))
    return H, float(I), total


if __name__ == '__main__':
    rng = random.Random(8)
    worst = {'deficit': 0, 'natural': 0}
    cnt = 0
    for trial in range(60):
        m = rng.randint(1, 3)
        widths = [rng.randint(1, 3) for _ in range(m)]
        kind = rng.choice(['dict', 'and', 'or'])
        u = rng.randint(1, 2) if kind != 'dict' else 1
        outs = [(kind, u)] * (m + 1)
        nv = sum(widths) + (m + 1) * (1 if kind == 'dict' else u)
        if nv > 15:
            continue
        T, n, blocks, oblocks, otabs, gates, widths = build(widths, outs)
        res = {}
        for order in ('deficit', 'natural'):
            H, I, tot = code_length(T, n, blocks, oblocks, otabs, gates, widths, order)
            assert tot >= H - 1e-9, "Gibbs violated?"
            res[order] = tot / I
            worst[order] = max(worst[order], tot / I)
        cnt += 1
    print("instances:", cnt, "worst exact code/I:", {k: round(v, 3) for k, v in worst.items()}, "(Theorem 11.1 bound: 27)")
