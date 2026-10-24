"""Finite stress checks for the parallel-slab candidate, independently coded.

This is numerical verification only; it cannot certify an asymptotic proof.
"""
import json
import math
from pathlib import Path

import numpy as np

rng = np.random.default_rng(20261012)
A0 = 20.5 * math.sqrt(2) / (1 - math.exp(-1))
LOGE = math.log2(math.e)
s = 2 ** -.5
Z = (1 + 2 ** -.25) / (1 - 2 ** -.25)
out = {
    "status": "passed",
    "scope": "finite numerical stress checks; no asymptotic or novelty certification",
    "slabs": 0, "narrow": 0, "wide": 0, "one_crossing": 0,
    "signed_stability_checks": 0, "low_degree_checks": 0,
    "pair_tail_checks": 0, "KL_checks": 0, "maxima": {},
}


def observe(name, value):
    out["maxima"][name] = max(float(value), out["maxima"].get(name, -math.inf))


def ft(y):
    a = np.array(y, dtype=float)
    step = 1
    while step < len(a):
        v = a.reshape(-1, 2 * step)
        l, r = v[:, :step].copy(), v[:, step:].copy()
        v[:, :step], v[:, step:] = l + r, l - r
        step *= 2
    # Only squared coefficients or products of two transforms are used.
    return a / len(a)


def ent(a):
    a = a[a > 0]
    return float(-a @ np.log2(a))


def kl(q, p):
    use = q > 0
    assert np.all(p[use] > 0)
    return float(q[use] @ np.log2(q[use] / p[use]))


def test(weights, lo, hi, scores, index):
    n = len(weights)
    exceptional = (scores > lo) & (scores < hi)
    f = 1 - 2 * exceptional.astype(float)
    if abs(f.mean()) == 1:
        return
    pivot = int(np.argmax(weights))
    w = weights[pivot]
    rest_index = index[((index >> pivot) & 1) == 0]
    minus, plus = f[rest_index], f[rest_index | (1 << pivot)]
    a, b = (plus + minus) / 2, (plus - minus) / 2
    alpha = float(np.mean(b ** 2))
    assert alpha > 0
    ah, bh = ft(a), ft(b)
    P, Q = ah ** 2 + bh ** 2, bh ** 2 / alpha
    k = np.array([int(v).bit_count() for v in range(len(P))])
    nz = P > 0
    C = ent(P) - ent(ah ** 2) - ent(bh ** 2)
    # The last equality is the conditional entropy of the split bit.
    C = -C
    delta = ent(ft(f) ** 2) - (ent(ft(plus) ** 2) + ent(ft(minus) ** 2)) / 2
    assert abs(P.sum() - 1) < 1e-12
    assert abs(Q.sum() - 1) < 1e-12
    assert Q[0] <= alpha + 1e-12
    assert delta <= 2 * C + 1e-11
    assert C >= -1e-11
    observe("largest_split_increment_over_alpha", delta / alpha)
    observe("conditional_entropy_over_alpha", C / alpha)
    observe("fine_KL_deficit", math.log2(1 / alpha) - kl(Q, P))
    out["slabs"] += 1
    if hi - lo < 2 * w:
        assert np.array_equal(a, 1 - abs(b))
        assert C <= 4 * alpha + 1e-11
        assert delta <= 8 * alpha + 1e-11
        out["narrow"] += 1
        observe("narrow_split_increment_over_alpha", delta / alpha)
        return
    out["wide"] += 1
    threshold_functions = []
    for endpoint in (lo, hi):
        h = np.where(scores > endpoint, 1., -1.)
        if abs(h.mean()) < 1:
            threshold_functions.append(h)
    m = len(threshold_functions)
    assert m in (1, 2)
    if m == 1:
        out["one_crossing"] += 1
    alpha_parts, p_parts = [], []
    boundary_b = []
    for h in threshold_functions:
        hm, hp = h[rest_index], h[rest_index | (1 << pivot)]
        bb = (hp - hm) / 2
        assert np.all((bb == 0) | (bb == 1))
        boundary_b.append(bb)
        aa = float(np.mean(bb))
        pp = min(float(np.mean(h == 1)), float(np.mean(h == -1)))
        assert aa <= 2 * pp + 1e-12
        alpha_parts.append(aa)
        p_parts.append(pp)
    assert abs(sum(alpha_parts) - alpha) < 1e-12
    assert np.all(sum(boundary_b) <= 1)
    R = max(0., (float(weights @ weights) - w * w) / (w * w))
    T = math.log(1 / alpha)
    M = max(1., R, T)
    noise_mass = sum(p * math.sqrt(math.log(1 / p)) for p in p_parts)
    kk_reciprocal = max(
        p * min(1., math.sqrt(math.log(1 / p) / (R + 1))) / aa
        for p, aa in zip(p_parts, alpha_parts)
    )
    # A measured coefficient here checks the algebraic conversion, not a
    # numerical assignment to the existential primary theorem constant.
    conversion = kk_reciprocal * (
        math.sqrt(R + 1) + math.sqrt(math.log(2 * m / alpha))
    )
    assert noise_mass <= alpha * conversion + 1e-12
    observe("summed_noise_scale_ratio", noise_mass / (alpha * math.sqrt(M)))
    for rho in [0, .1, .5, .8, .95, .99, .999]:
        stab = float((bh ** 2) @ rho ** k)
        if R:
            bound = alpha * min(1., 6 * m / math.sqrt((1 - rho) * R))
            assert stab <= bound + 1e-12
            observe("signed_slab_scaled_stability", stab / alpha * math.sqrt((1 - rho) * R))
        assert stab <= alpha + 1e-12
        out["signed_stability_checks"] += 1
    assert (bh ** 2) @ .5 ** k <= alpha ** (4 / 3) + 1e-12
    for u in np.unique(np.r_[np.arange(1, n + 1), [.01, .5, .999, M]]):
        low = Q[k <= u].sum()
        if u >= 1:
            assert low <= 18 * m * math.sqrt(u / M) + 1e-12
            assert low <= 2 ** u * alpha ** (1 / 3) + 1e-12
            if T:
                assert low <= 3 * math.sqrt(u / T) + 1e-12
            out["low_degree_checks"] += 1
        tail = P[k >= u].sum()
        assert tail <= A0 * noise_mass / math.sqrt(u) + 1e-12
        out["pair_tail_checks"] += 1
    gamma = max(1., A0 * noise_mass / (alpha * math.sqrt(M)))
    bins = {"zero": (float(Q[0]), float(P[0]))}
    for d, qp, pp in zip(k[1:], Q[1:], P[1:]):
        j = math.floor(math.log2(d / M))
        prevq, prevp = bins.get(j, (0., 0.))
        bins[j] = prevq + qp, prevp + pp
    qb, pb = np.array(list(bins.values())).T
    db = kl(qb, pb)
    assert db <= kl(Q, P) + 1e-10
    reference_lower = 0.
    negative_moment = 0.
    for j, (qj, pj) in bins.items():
        rr = .5 if j == "zero" else 2 ** (-abs(j) / 4) / (2 * Z)
        if qj:
            reference_lower += qj * math.log2(rr / pj)
        if j != "zero":
            assert pj <= gamma * alpha * 2 ** (-j / 2) + 1e-12
            if j < 0:
                assert qj <= 18 * m * math.sqrt(2) * 2 ** (j / 2) + 1e-12
                negative_moment += abs(j) * qj
    cminus = 18 * m * math.sqrt(2) * s / (1 - s) ** 2
    CD = math.log2(2 * Z * gamma) + .75 * cminus + 1 + LOGE / math.e
    assert db >= reference_lower - 1e-11
    assert negative_moment <= cminus + 1e-12
    assert db >= math.log2(1 / alpha) - CD - 1e-11
    assert C <= alpha * (CD + LOGE) + 1e-11
    observe("coarse_KL_deficit", math.log2(1 / alpha) - db)
    out["KL_checks"] += 1


for n in [1, 2, 3, 4, 5, 6, 8, 10, 12]:
    index = np.arange(1 << n)
    signs = 2 * ((index[:, None] >> np.arange(n)) & 1) - 1
    families = [np.ones(n), 2. ** np.arange(n),
                np.r_[4 * n, np.ones(n - 1)],
                np.r_[1., np.zeros(n - 1)],
                rng.integers(1, 6, n).astype(float),
                np.maximum(1., np.rint(100 * rng.lognormal(0, 3, n)))]
    for weights in families:
        scores = signs @ weights
        ds = np.unique(scores)
        gaps = np.r_[ds[0] - max(weights), (ds[:-1] + ds[1:]) / 2,
                     ds[-1] + max(weights)]
        pairs = set()
        if n <= 5:
            pairs.update((i, j) for i in range(len(gaps)) for j in range(i + 1, len(gaps)))
        else:
            # Single-score stripes, opposite tails, random widths, and
            # near-full intervals are all represented.
            for i in np.unique(np.linspace(0, len(gaps) - 2, 20).astype(int)):
                pairs.add((int(i), int(i + 1)))
                pairs.add((0, int(i + 1)))
                pairs.add((int(i), len(gaps) - 1))
            for _ in range(80):
                i, j = sorted(rng.choice(len(gaps), 2, replace=False))
                pairs.add((int(i), int(j)))
        for i, j in sorted(pairs):
            test(weights, gaps[i], gaps[j], scores, index)

Path(__file__).with_name("stripe_extension_parallel_slabs_verification.json").write_text(
    json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
