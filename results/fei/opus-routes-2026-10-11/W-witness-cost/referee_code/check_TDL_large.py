"""Large equal-mean term decision lists (dictator outputs, mu = 0): exact per-set witness quantities of Theorem 11.1's
proof, with Fourier sets sampled from the exact spectral law (Section 11 of NOTES, re-derived and checked on small
lists by check_TDL.py).

For a sampled set A (output j, S_k for k < j, S_j, B = {y_j}) everything below is EXACT for that set:
  root   = log(1/sum_owners pi)                                       (closed form)
  rank   = E_w[sum_{x in A} log+(r_t(x)/s)]  under the owner law w    (exact: independent t_u, convolution DP)
  Er(x)  = E_w[r_t(x)] for each rare element                          (exact)
and the proof's per-element bound Er <= W_R + 2^{w_v-M_v+3} Lambda_j, the per-set rare-rank bound, and the Jensen-form
code J(A) = log e + root + 1 + log(s(s+1)) + s log(2ea/(a-1)) + a*rank  (Lambda <= log e, Z <= (2ea/(a-1))^s, both as in
the proof) are compared; the Monte Carlo average of J over the spectral law (v = 1, h(v) = 0) must stay <= 26.71 I.
Usage: python check_TDL_large.py FAMILY SAMPLES SEED
"""
import sys, math, random, time
import numpy as np

a = 1.2
LOG2E = 1 / math.log(2)


def e_w(w):
    return w * 2 ** w / (2 * (2 ** w - 1))


def family(name):
    if name.startswith('TD1_'):            # m = 2^w terms of width w
        w = int(name[4:]); return [w] * (2 ** w)
    if name.startswith('NW_'):             # narrow top block (w0 = 2) then 4*2^W wide blocks of width W
        W = int(name[3:]); return [2] + [W] * (4 * 2 ** W)
    if name.startswith('WN_'):             # 2^W wide blocks then many narrow ones
        W = int(name[3:]); return [W] * (2 ** W) + [2] * 64
    if name.startswith('ALT_'):            # alternating widths 1 and W, 2^W pairs
        W = int(name[4:]); return [1, W] * (2 ** W)
    if name.startswith('RND_'):
        r = random.Random(int(name[4:])); m = r.randint(20, 300)
        return [r.randint(1, 10) for _ in range(m)]
    if name.startswith('GEO_'):            # widths 1,2,...,W each repeated 2^w times
        W = int(name[4:]); out = []
        for w in range(1, W + 1):
            out += [w] * (2 ** w)
        return out
    raise ValueError(name)


def tlaw(w, M):
    """owner law of t on [max(M,1), w], prob proportional to 2^-t: returns (values, probs)."""
    lo = max(M, 1)
    vals = np.arange(lo, w + 1)
    pr = 2.0 ** (-vals)
    return vals, pr / pr.sum()


def rare_rank_dp(widths, j, Sks, Mk, wj, s):
    """Exact E_w[sum log+(r/s)] over rare elements and E_w[r] per rare element (dict v -> arrays)."""
    laws = {k: tlaw(widths[k], int(Mk[k])) for k in range(j)}
    El_all = {}; Er_all = {}
    for v in sorted(Sks):
        wv = widths[v]
        vals_v, pr_v = laws[v]
        El = np.zeros(len(Sks[v])); Er = np.zeros(len(Sks[v]))
        for tv, ptv in zip(vals_v, pr_v):
            dv = wv - tv
            dist = np.zeros(1); dist[0] = 1.0
            for u in range(j):
                if u == v:
                    continue
                vals_u, pr_u = laws[u]
                du = widths[u] - vals_u
                before = (du < dv) | ((du == dv) & (u < v))
                if not before.any():
                    continue
                c = np.zeros(int(vals_u.max()) + 1)
                c[0] += pr_u[~before].sum()
                for tval, pp, bb in zip(vals_u, pr_u, before):
                    if bb:
                        c[int(tval)] += pp
                dist = np.convolve(dist, c)
            support = np.arange(len(dist))
            for ix, pos in enumerate(Sks[v]):
                r = wj + support + pos
                El[ix] += ptv * float(np.dot(dist, np.maximum(0.0, np.log2(r / s))))
                Er[ix] += ptv * float(np.dot(dist, r))
        El_all[v] = El; Er_all[v] = Er
    return El_all, Er_all


def rare_rank_brute(widths, j, Sks, Mk, wj, s):
    """Brute force over all owner gates t (weights 2^-sum t), deficit order with ties to earlier blocks."""
    import itertools
    ranges = [range(max(int(Mk[k]), 1), widths[k] + 1) for k in range(j)]
    totw = 0.0
    El = {v: np.zeros(len(Sks[v])) for v in Sks}; Er = {v: np.zeros(len(Sks[v])) for v in Sks}
    for t in itertools.product(*ranges):
        wt = 2.0 ** (-sum(t))
        totw += wt
        segs = sorted(range(j), key=lambda k: (widths[k] - t[k], k))
        start = {}; pos = wj
        for k in segs:
            start[k] = pos; pos += t[k]
        for v in Sks:
            for ix, p in enumerate(Sks[v]):
                r = start[v] + p
                El[v][ix] += wt * max(0.0, math.log2(r / s))
                Er[v][ix] += wt * r
    for v in Sks:
        El[v] /= totw; Er[v] /= totw
    return El, Er


def run(name, samples, seed):
    widths = family(name)
    m = len(widths)
    q = [2.0 ** -w for w in widths]
    # P(E_j): j = 0..m-1 terms, j = m default
    reach = [1.0]
    for k in range(m):
        reach.append(reach[-1] * (1 - q[k]))
    PE = np.array([reach[j] * q[j] for j in range(m)] + [reach[m]])
    PE = PE / PE.sum()
    I_true = sum(PE[j] * widths[j] / 2 for j in range(m))
    cum = np.concatenate([[0.0], np.cumsum([q[k] * e_w(widths[k]) for k in range(m)])])
    I_rare = sum(PE[j] * cum[j] for j in range(m + 1))
    I_Y = 1.0
    I = I_true + I_rare + I_Y
    Lam_pref = np.concatenate([[0.0], np.cumsum([q[k] * widths[k] for k in range(m)])])
    rng = np.random.default_rng(seed)
    tot = dict(J=0.0, root=0.0, rank=0.0, rare_rank=0.0, rare_bound=0.0)
    elem_viol = 0; set_viol = 0; worst_elem = -1e9
    js = rng.choice(m + 1, size=samples, p=PE)
    for j in js:
        j = int(j)
        wj = widths[j] if j < m else 0
        # sample S_k for k < j
        Mk = np.zeros(j, dtype=np.int64)
        Sks = {}
        nonempty = np.nonzero(rng.random(j) < np.array(q[:j]))[0]
        for k in nonempty:
            w = widths[k]
            while True:
                bits = rng.random(w) < 0.5
                if bits.any():
                    break
            pos = np.nonzero(bits)[0] + 1
            Sks[int(k)] = pos
            Mk[k] = pos.max()
        Sj = (np.nonzero(rng.random(wj) < 0.5)[0] + 1) if wj > 0 else np.array([], dtype=np.int64)
        s = len(Sj) + sum(len(p) for p in Sks.values()) + 1
        # root term (closed form)
        root = wj + 1.0  # log 1/q_j + log(1/P_j) with P_j = 1/2 (dictator)
        for k in range(j):
            if Mk[k] == 0:
                root += -math.log2(1 - q[k])
            else:
                root += -math.log2(2.0 ** (1 - Mk[k]) - q[k])
        # rank: true block + rare elements (data element has rank 1 -> 0)
        rank = sum(max(0.0, math.log2(p / s)) for p in Sj)
        rare_rank = 0.0; rare_bound = 0.0
        if Sks:
            Rset = sorted(Sks)
            W_R = wj + sum(widths[k] for k in Rset)
            Lam_j = Lam_pref[j]
            El_all, Er_all = rare_rank_dp(widths, j, Sks, Mk, wj, s)
            for v in Rset:
                wv = widths[v]
                El = El_all[v]; Er = Er_all[v]
                for ix in range(len(Sks[v])):
                    bnd = W_R + 2.0 ** (wv - Mk[v] + 3) * Lam_j
                    worst_elem = max(worst_elem, Er[ix] / bnd)
                    if Er[ix] > bnd + 1e-9:
                        elem_viol += 1
                rare_rank += El.sum()
                rare_bound += len(Sks[v]) * (math.log2(1 + W_R / s) + (wv - Mk[v] + 3) + math.log2(1 + Lam_j / s))
            if rare_rank > rare_bound + 1e-9:
                set_viol += 1
        rank += rare_rank
        J = LOG2E + root + 1 + math.log2(s * (s + 1)) + s * math.log2(2 * math.e * a / (a - 1)) + a * rank
        tot['J'] += J; tot['root'] += root; tot['rank'] += a * rank
        tot['rare_rank'] += a * rare_rank; tot['rare_bound'] += a * rare_bound
    for k in tot:
        tot[k] /= samples
    return dict(name=name, m=m, I=I, I_true=I_true, I_rare=I_rare, J_over_I=tot['J'] / I, root_over_I=tot['root'] / I,
                rank_over_I=tot['rank'] / I, rare_rank_over_I=tot['rare_rank'] / I, rare_bound_over_I=tot['rare_bound'] / I,
                root_bound_over_I=(2 * I_true + 2 * I_Y + (LOG2E + 2) * I_rare) / I,
                elem_viol=elem_viol, set_viol=set_viol, worst_elem_ratio=worst_elem)


if __name__ == '__main__':
    fams = sys.argv[1].split(','); samples = int(sys.argv[2]); seed = int(sys.argv[3])
    t0 = time.time()
    for fm in fams:
        r = run(fm, samples, seed)
        print('%-8s m=%4d I=%.3f (true %.3f rare %.3f) J/I=%.3f root/I=%.3f [bd %.3f] rank/I=%.3f rare/I=%.3f [per-set bd %.3f] '
              'elem_viol=%d set_viol=%d max Er/bound=%.3f  t=%.0fs'
              % (r['name'], r['m'], r['I'], r['I_true'], r['I_rare'], r['J_over_I'], r['root_over_I'], r['root_bound_over_I'],
                 r['rank_over_I'], r['rare_rank_over_I'], r['rare_bound_over_I'], r['elem_viol'], r['set_viol'],
                 r['worst_elem_ratio'], time.time() - t0), flush=True)
