"""Read-once AND/OR formulas with arbitrary fan-in: exact recursive samplers for the spectral law and the owner law
(cells = 1-leaves of the left-to-right short-circuit tree), exact influences, exact coefficients. Generalizes
andor_sampler.py (fan-in 2). Usage: python andor_k.py SPEC DEPTHMAX NSETS SEED, SPEC like 'and2,or3' (alternating)."""
import math
import random
import sys

A_EXP = 6.0 / 5.0
sys.setrecursionlimit(100000)


class Node:
    __slots__ = ('kind', 'ch', 'var', 'vars', 'P', 'N', 'id')


def build(spec, depth, counter=None, level=0):
    if counter is None:
        counter = [0, 0]
    nd = Node(); nd.id = counter[1]; counter[1] += 1
    if level == depth:
        nd.kind = 'lit'; nd.var = counter[0]; counter[0] += 1
        nd.ch = (); nd.vars = frozenset([nd.var]); nd.P = 0.5
    else:
        kind, k = spec[level % len(spec)]
        nd.kind = kind
        nd.ch = tuple(build(spec, depth, counter, level + 1) for _ in range(k))
        nd.vars = frozenset().union(*[c.vars for c in nd.ch])
        if kind == 'and':
            nd.P = math.prod(c.P for c in nd.ch)
        else:
            nd.P = 1 - math.prod(1 - c.P for c in nd.ch)
    nd.N = nd.P * (1 - nd.P)
    return nd


def sample_nonempty(nd, rng):
    if nd.kind == 'lit':
        return {nd.var}
    # product of child laws (indicator for AND, complement for OR); empty masses e_i, nonempty N_i
    while True:
        out = set()
        for c in nd.ch:
            e = c.P ** 2 if nd.kind == 'and' else (1 - c.P) ** 2
            if rng.random() * (e + c.N) >= e:
                out |= sample_nonempty(c, rng)
        if out:
            return out


def influences(nd, acc=1.0, out=None):
    if out is None:
        out = {}
    if nd.kind == 'lit':
        out[nd.var] = acc; return out
    for i, c in enumerate(nd.ch):
        f = 1.0
        for j, o in enumerate(nd.ch):
            if j != i:
                f *= o.P if nd.kind == 'and' else (1 - o.P)
        influences(c, acc * f, out)
    return out


def coef(nd, A):
    if nd.kind == 'lit':
        return 0.5 if not A else (0.5 if nd.var in A else 0.0)
    if nd.kind == 'and':
        return math.prod(coef(c, A & c.vars) for c in nd.ch)
    comp = 1.0
    for c in nd.ch:
        B = A & c.vars
        comp *= (1 - c.P) if not B else -coef(c, B)
    return (1 - comp) if not A else -comp


def prob(nd, b, A, memo):
    key = (nd.id, b, A)
    if key in memo:
        return memo[key]
    if nd.kind == 'lit':
        r = 0.5
    else:
        dom = (nd.kind == 'or')  # dominating child value: OR stops at True, AND stops at False
        parts = [A & c.vars for c in nd.ch]
        k = len(nd.ch)
        cont = not dom  # value that lets evaluation continue
        if b == cont:
            # all children evaluated and all equal cont
            r = math.prod(prob(c, cont, parts[i], memo) for i, c in enumerate(nd.ch))
        else:
            r = 0.0
            pre = 1.0
            for j, c in enumerate(nd.ch):
                if any(parts[i] for i in range(j + 1, k)):
                    pre *= prob(c, cont, parts[j], memo)
                    continue
                r += pre * prob(c, dom, parts[j], memo)
                pre *= prob(c, cont, parts[j], memo)
    memo[key] = r
    return r


def sample_cond(nd, b, A, rng, memo, seq):
    if nd.kind == 'lit':
        seq.append(nd.var); return
    dom = (nd.kind == 'or')
    cont = not dom
    parts = [A & c.vars for c in nd.ch]
    k = len(nd.ch)
    if b == cont:
        for i, c in enumerate(nd.ch):
            sample_cond(c, cont, parts[i], rng, memo, seq)
        return
    # choose the stopping child j
    w = []
    pre = 1.0
    for j, c in enumerate(nd.ch):
        if any(parts[i] for i in range(j + 1, k)):
            w.append(0.0)
        else:
            w.append(pre * prob(c, dom, parts[j], memo))
        pre *= prob(c, cont, parts[j], memo)
    r = rng.random() * sum(w)
    for j in range(k):
        r -= w[j]
        if r <= 0:
            break
    for i in range(j):
        sample_cond(nd.ch[i], cont, parts[i], rng, memo, seq)
    sample_cond(nd.ch[j], dom, parts[j], rng, memo, seq)


def run(spec, dmin, dmax, nsets, seed, nown=4):
    rng = random.Random(seed)
    for d in range(dmin, dmax + 1):
        root = build(spec, d)
        I = sum(influences(root).values()); v = 4 * root.P * (1 - root.P)
        Hn = Rj = Rm = 0.0
        for _ in range(nsets):
            A = frozenset(sample_nonempty(root, rng))
            Hn += math.log2(1 / (4 * coef(root, A) ** 2))
            memo = {}
            cj = cm = 0.0
            for _ in range(nown):
                seq = []; sample_cond(root, True, A, rng, memo, seq)
                pos = {u: i + 1 for i, u in enumerate(seq)}; s = len(A); L = len(seq)
                cp = sum(max(0.0, math.log2(pos[u] / s)) for u in A)
                cr = sum(max(0.0, math.log2((L - pos[u] + 1) / s)) for u in A)
                cj += cp; cm += min(cp, cr) + 1 / A_EXP
            Rj += cj / nown; Rm += cm / nown
        p0 = 1 - v
        H = (p0 * math.log2(1 / p0) if 0 < p0 < 1 else 0) + v * Hn / nsets
        print(f"{spec} depth {d} (n={len(root.vars)}): P(f=1)={root.P:.3f} I={I:.4f} H/I={H/I:.3f} "
              f"R_path/I={v*Rj/nsets/I:.3f} R_mix/I={v*Rm/nsets/I:.3f}", flush=True)


if __name__ == '__main__':
    spec = [(s[:-1] if s[-1].isdigit() else s, int(s[-1])) for s in sys.argv[1].split(',')]
    spec = [(k.rstrip('0123456789'), n) for k, n in spec]
    run(spec, 1, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
