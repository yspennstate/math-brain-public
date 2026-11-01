"""Certificate-first order inside each owner cell for read-once AND/OR formulas (short-circuit cells):
variables of the evaluation certificate (whose values propagate to the root value) first, in query order,
then the remaining queried variables in query order. Exact (enumeration) for small depth, and a structured
Monte Carlo (andor_sampler.sample_cond instrumented to return certificates) for large depth. EVIDENCE."""
import math, random, sys, itertools
from andor_sampler import build_andor, sample_nonempty, prob, influences, A_EXP
sys.setrecursionlimit(100000)

def eval_cert(nd, x, seq):
    """Evaluate with short-circuit on assignment dict x; append queried vars; return (value, certificate set)."""
    if nd.kind == 'lit':
        seq.append(nd.var); return x[nd.var], {nd.var}
    c1, c2 = nd.ch
    v1, s1 = eval_cert(c1, x, seq)
    if nd.kind == 'and':
        if not v1: return False, s1
        v2, s2 = eval_cert(c2, x, seq)
        return (True, s1 | s2) if v2 else (False, s2)
    else:
        if v1: return True, s1
        v2, s2 = eval_cert(c2, x, seq)
        return (True, s2) if v2 else (False, s1 | s2)

def sample_cond_cert(nd, b, A, rng, memo, seq):
    """Like andor_sampler.sample_cond but returns the certificate set of the sampled evaluation."""
    if nd.kind == 'lit':
        seq.append(nd.var); return {nd.var}
    c1, c2 = nd.ch
    A1, A2 = A & c1.vars, A & c2.vars
    if nd.kind == 'and':
        if b:
            s1 = sample_cond_cert(c1, True, A1, rng, memo, seq); s2 = sample_cond_cert(c2, True, A2, rng, memo, seq)
            return s1 | s2
        w0 = prob(c1, False, A1, memo) if not A2 else 0.0
        w1 = prob(c1, True, A1, memo) * prob(c2, False, A2, memo)
        if rng.random() * (w0 + w1) < w0:
            return sample_cond_cert(c1, False, A1, rng, memo, seq)
        sample_cond_cert(c1, True, A1, rng, memo, seq)
        return sample_cond_cert(c2, False, A2, rng, memo, seq)
    else:
        if not b:
            s1 = sample_cond_cert(c1, False, A1, rng, memo, seq); s2 = sample_cond_cert(c2, False, A2, rng, memo, seq)
            return s1 | s2
        w0 = prob(c1, True, A1, memo) if not A2 else 0.0
        w1 = prob(c1, False, A1, memo) * prob(c2, True, A2, memo)
        if rng.random() * (w0 + w1) < w0:
            return sample_cond_cert(c1, True, A1, rng, memo, seq)
        sample_cond_cert(c1, False, A1, rng, memo, seq)
        return sample_cond_cert(c2, True, A2, rng, memo, seq)

def cost_orders(seq, cert, A):
    s = len(A)
    pos_path = {u: i + 1 for i, u in enumerate(seq)}
    order = [u for u in seq if u in cert] + [u for u in seq if u not in cert]
    pos_cert = {u: i + 1 for i, u in enumerate(order)}
    cp = sum(max(0.0, math.log2(pos_path[u] / s)) for u in A)
    cc = sum(max(0.0, math.log2(pos_cert[u] / s)) for u in A)
    return cp, cc

if __name__ == '__main__':
    dmax, nsets, nown, seed = map(int, sys.argv[1:5])
    rng = random.Random(seed)
    for d in range(1, dmax + 1):
        root = build_andor(d)
        I = sum(influences(root).values()); v = 4 * root.P * (1 - root.P)
        Rp = Rc = 0.0
        for _ in range(nsets):
            A = frozenset(sample_nonempty(root, rng))
            memo = {}
            prob(root, True, A, memo)
            cp = cc = 0.0
            for _ in range(nown):
                seq = []
                cert = sample_cond_cert(root, True, A, rng, memo, seq)
                a, b = cost_orders(seq, cert, A); cp += a; cc += b
            Rp += cp / nown; Rc += cc / nown
        print(f"AND-OR depth {d} (n={2**d}): R_path/I={v*Rp/nsets/I:.3f}  R_certificate-first/I={v*Rc/nsets/I:.3f}", flush=True)
