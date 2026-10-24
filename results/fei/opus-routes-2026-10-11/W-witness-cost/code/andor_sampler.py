"""Structured (exact-law) Monte Carlo for the rank term R of Proposition 12.1 on read-once AND/OR formulas,
cells = 1-leaves of the short-circuit decision tree (left-to-right evaluation).
 - A ~ fhat^2 restricted to nonempty sets: exact recursive sampler from the product structure
   (1_f = 1_g 1_h for AND, 1 - 1_f = (1-1_g)(1-1_h) for OR).
 - owner law w_A (proportional to cell probability over 1-cells containing A) = law of x uniform conditioned on
   f(x) = 1 and A subset queried(x): exact recursive conditional sampler.
 - I(f) exact (Inf_u = prod over ancestors of P(sibling at the gate's identity value)).
Orders: 'path' (query order), 'mix' = best of path / reversed path plus (1/a)*1 bit (W-P123, gamma = 1/2).
EVIDENCE (Monte Carlo)."""
import math
import random
import sys

A_EXP = 6.0 / 5.0


class Node:
    __slots__ = ('kind', 'ch', 'var', 'vars', 'P', 'N', 'id')


def build_andor(depth, top='and', counter=None):
    if counter is None:
        counter = [0, 0]
    nd = Node()
    nd.id = counter[1]; counter[1] += 1
    if depth == 0:
        nd.kind = 'lit'; nd.var = counter[0]; counter[0] += 1
        nd.ch = (); nd.vars = frozenset([nd.var]); nd.P = 0.5
    else:
        sub = 'or' if top == 'and' else 'and'
        nd.kind = top
        nd.ch = (build_andor(depth - 1, sub, counter), build_andor(depth - 1, sub, counter))
        nd.vars = nd.ch[0].vars | nd.ch[1].vars
        p1, p2 = nd.ch[0].P, nd.ch[1].P
        nd.P = p1 * p2 if top == 'and' else 1 - (1 - p1) * (1 - p2)
    nd.N = nd.P * (1 - nd.P)
    return nd


def sample_nonempty(nd, rng):
    """Sample a nonempty set from the nonempty part of 1hat_node^2 (total mass N)."""
    if nd.kind == 'lit':
        return {nd.var}
    c1, c2 = nd.ch
    if nd.kind == 'and':
        e1, e2 = c1.P ** 2, c2.P ** 2
    else:
        e1, e2 = (1 - c1.P) ** 2, (1 - c2.P) ** 2
    w = [e1 * c2.N, c1.N * e2, c1.N * c2.N]
    r = rng.random() * sum(w)
    if r < w[0]:
        return sample_nonempty(c2, rng)
    if r < w[0] + w[1]:
        return sample_nonempty(c1, rng)
    return sample_nonempty(c1, rng) | sample_nonempty(c2, rng)


def influences(nd, acc=1.0, out=None):
    if out is None:
        out = {}
    if nd.kind == 'lit':
        out[nd.var] = acc
        return out
    c1, c2 = nd.ch
    if nd.kind == 'and':
        influences(c1, acc * c2.P, out); influences(c2, acc * c1.P, out)
    else:
        influences(c1, acc * (1 - c2.P), out); influences(c2, acc * (1 - c1.P), out)
    return out


def prob(nd, b, A, memo):
    """P(value(nd) = b and A subset queried(nd)), A = frozenset subset of nd.vars."""
    key = (nd.id, b, A)
    if key in memo:
        return memo[key]
    if nd.kind == 'lit':
        r = 0.5
    else:
        c1, c2 = nd.ch
        A1, A2 = A & c1.vars, A & c2.vars
        if nd.kind == 'and':
            if b:
                r = prob(c1, True, A1, memo) * prob(c2, True, A2, memo)
            else:
                r = (prob(c1, False, A1, memo) if not A2 else 0.0) + prob(c1, True, A1, memo) * prob(c2, False, A2, memo)
        else:
            if b:
                r = (prob(c1, True, A1, memo) if not A2 else 0.0) + prob(c1, False, A1, memo) * prob(c2, True, A2, memo)
            else:
                r = prob(c1, False, A1, memo) * prob(c2, False, A2, memo)
    memo[key] = r
    return r


def sample_free(nd, rng, seq):
    """Evaluate nd on fresh uniform bits, appending queried vars to seq; returns value."""
    if nd.kind == 'lit':
        seq.append(nd.var)
        return rng.random() < 0.5
    c1, c2 = nd.ch
    v1 = sample_free(c1, rng, seq)
    if nd.kind == 'and' and not v1:
        return False
    if nd.kind == 'or' and v1:
        return True
    return sample_free(c2, rng, seq)


def sample_cond(nd, b, A, rng, memo, seq):
    """Sample bits for nd conditioned on value b and A subset queried; append query order to seq."""
    if nd.kind == 'lit':
        seq.append(nd.var)
        return
    c1, c2 = nd.ch
    A1, A2 = A & c1.vars, A & c2.vars
    if nd.kind == 'and':
        if b:
            sample_cond(c1, True, A1, rng, memo, seq); sample_cond(c2, True, A2, rng, memo, seq); return
        w0 = prob(c1, False, A1, memo) if not A2 else 0.0
        w1 = prob(c1, True, A1, memo) * prob(c2, False, A2, memo)
        if rng.random() * (w0 + w1) < w0:
            sample_cond(c1, False, A1, rng, memo, seq)  # c2 not evaluated
        else:
            sample_cond(c1, True, A1, rng, memo, seq); sample_cond(c2, False, A2, rng, memo, seq)
    else:
        if not b:
            sample_cond(c1, False, A1, rng, memo, seq); sample_cond(c2, False, A2, rng, memo, seq); return
        w0 = prob(c1, True, A1, memo) if not A2 else 0.0
        w1 = prob(c1, False, A1, memo) * prob(c2, True, A2, memo)
        if rng.random() * (w0 + w1) < w0:
            sample_cond(c1, True, A1, rng, memo, seq)
        else:
            sample_cond(c1, False, A1, rng, memo, seq); sample_cond(c2, True, A2, rng, memo, seq)


def rank_costs(seq, A):
    s = len(A)
    pos = {u: i + 1 for i, u in enumerate(seq)}
    L = len(seq)
    c_path = sum(max(0.0, math.log2(pos[u] / s)) for u in A)
    c_rev = sum(max(0.0, math.log2((L - pos[u] + 1) / s)) for u in A)
    return c_path, min(c_path, c_rev) + 1.0 / A_EXP


def estimate(root, nsets, nown, rng, target=True):
    v = 4 * root.P * (1 - root.P)
    I = sum(influences(root).values())
    tot_p = 0.0
    tot_m = 0.0
    for _ in range(nsets):
        A = frozenset(sample_nonempty(root, rng))
        memo = {}
        pr = prob(root, target, A, memo)
        assert pr > 0
        cp = cm = 0.0
        for _ in range(nown):
            seq = []
            sample_cond(root, target, A, rng, memo, seq)
            a, b = rank_costs(seq, A)
            cp += a; cm += b
        tot_p += cp / nown
        tot_m += cm / nown
    return v * tot_p / nsets / I, v * tot_m / nsets / I, I, v


if __name__ == '__main__':
    dmax, nsets, nown, seed = map(int, sys.argv[1:5])
    rng = random.Random(seed)
    for d in range(1, dmax + 1):
        root = build_andor(d)
        rp, rm, I, v = estimate(root, nsets, nown, rng, True)
        rp0, rm0, _, _ = estimate(root, nsets, nown, rng, False)
        print(f"AND-OR depth {d} (n={2**d}): I={I:.4f} v={v:.4f}  R_path/I (b=1,-1) = {rp:.3f}, {rp0:.3f}   "
              f"R_mix(path,rev)/I = {rm:.3f}, {rm0:.3f}", flush=True)
