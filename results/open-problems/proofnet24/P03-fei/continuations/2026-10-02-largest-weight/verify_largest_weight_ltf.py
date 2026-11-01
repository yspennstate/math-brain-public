"""Independent finite stress checks for the candidate largest-weight LTF proof.

This script checks identities and inequalities, not research novelty or an
asymptotic theorem. It does not import any earlier checker.
"""

import json
import math
from pathlib import Path

import numpy as np


SEED = 20261004
rng = np.random.default_rng(SEED)
A0 = 20.5 * math.sqrt(2) / (1 - math.exp(-1))
rbin = 2 ** (-.25)
ZBIN = (1 + rbin) / (1 - rbin)
rnegative = 2 ** (-.5)
CMINUS = 18 * math.sqrt(2) * rnegative / (1 - rnegative) ** 2
LOGE = math.log2(math.e)
report = {
    "status": "all assertions passed",
    "scope": "finite stress checks only; no novelty or asymptotic certification",
    "seed": SEED,
    "ltfs": 0,
    "slab_noise_checks": 0,
    "low_degree_checks": 0,
    "pair_tail_checks": 0,
    "bin_KL_checks": 0,
    "maxima": {},
    "regimes": {},
    "constants": {"A0": A0, "Cminus": CMINUS},
}


def record(name, value):
    report["maxima"][name] = max(float(value), report["maxima"].get(name, -math.inf))


def fourier(values):
    """Product-of-sign convention, where input bit one represents +1."""
    a = np.array(values, dtype=float)
    d = np.array([int(s).bit_count() for s in range(len(a))])
    step = 1
    while step < len(a):
        view = a.reshape(-1, 2 * step)
        left, right = view[:, :step].copy(), view[:, step:].copy()
        view[:, :step], view[:, step:] = left + right, left - right
        step *= 2
    return a * np.where(d % 2, -1, 1) / len(a), d


def entropy(prob):
    positive = prob[prob > 0]
    return float(-np.dot(positive, np.log2(positive)))


def relative_entropy(q, p):
    use = q > 0
    assert np.all(p[use] > 0)
    return float(np.dot(q[use], np.log2(q[use] / p[use])))


def check(weights, theta, family):
    n = len(weights)
    index = np.arange(1 << n)
    x = 2 * ((index[:, None] >> np.arange(n)) & 1) - 1
    f = np.where(x @ weights > theta, 1., -1.)
    if abs(np.mean(f)) == 1:
        return
    if np.mean(f) > 0:
        # Output and all coordinates flipped: weights stay nonnegative and
        # the rare output is +1. The exact truth table handles original ties.
        f = -f[::-1]
    p = np.mean(f == 1)
    L = math.log(1 / p)
    pivot = int(np.argmax(weights))
    alpha = float(np.mean(f != f[index ^ (1 << pivot)]))
    assert alpha > 0
    assert alpha <= 2 * p + 1e-14
    # Arrays with the pivot fixed, in the remaining-coordinate product order.
    minus_index = index[((index >> pivot) & 1) == 0]
    minus, plus = f[minus_index], f[minus_index | (1 << pivot)]
    A, B = (plus + minus) / 2, (plus - minus) / 2
    assert np.all((B == 0) | (B == 1))
    assert abs(np.mean(B) - alpha) < 1e-14
    ahat, deg = fourier(A)
    bhat, _ = fourier(B)
    P = ahat ** 2 + bhat ** 2
    Q = bhat ** 2 / alpha
    R = (float(np.dot(weights, weights)) - weights[pivot] ** 2) / weights[pivot] ** 2
    R = max(0., R)
    M = max(1., R, L)
    assert abs(np.sum(P) - 1) < 1e-12
    assert abs(np.sum(Q) - 1) < 1e-12
    assert abs(Q[0] - alpha) < 1e-12
    for i in range(n):
        influence = np.mean(f != f[index ^ (1 << i)])
        assert alpha >= influence - 1e-14, (n, family, weights.tolist(), theta, p, pivot, i, alpha, influence)
    cf, full_degree = fourier(f)
    cp, _ = fourier(plus)
    cm, _ = fourier(minus)
    delta = entropy(cf ** 2) - (entropy(cp ** 2) + entropy(cm ** 2)) / 2
    positive_P = P > 0
    q = bhat[positive_P] ** 2 / P[positive_P]
    binary = np.zeros(len(q))
    use = (q > 0) & (q < 1)
    binary[use] = -q[use] * np.log2(q[use]) - (1 - q[use]) * np.log2(1 - q[use])
    conditional = float(np.dot(P[positive_P], binary))
    conditional_direct = alpha * (math.log2(1 / alpha) - relative_entropy(Q, P))
    other = ahat ** 2
    use_other = other > 0
    conditional_direct += float(np.dot(other[use_other], np.log2(P[use_other] / other[use_other])))
    assert abs(conditional - conditional_direct) < 1e-10
    r = (ahat[positive_P] + bhat[positive_P]) ** 2 / (2 * P[positive_P])
    r = np.clip(r, 0, 1)
    rbinary = np.zeros(len(r))
    use = (r > 0) & (r < 1)
    rbinary[use] = -r[use] * np.log2(r[use]) - (1 - r[use]) * np.log2(1 - r[use])
    delta_identity = float(np.dot(P[positive_P], 1 + binary - rbinary))
    assert abs(delta - delta_identity) < 1e-10
    assert delta <= 2 * conditional + 1e-10
    record("split_identity_error", abs(delta - delta_identity))
    record("split_increment_over_alpha", delta / alpha)
    record("conditional_bit_entropy_over_alpha", conditional / alpha)
    record("fine_KL_deficit", math.log2(1 / alpha) - relative_entropy(Q, P))
    record("scale_conversion_factor", p * math.sqrt(L) / (alpha * math.sqrt(M)))
    record("minimum_KK_coefficient_reciprocal", p * min(1., math.sqrt(L / (R + 1))) / alpha)
    for rho in [0, .1, .5, .8, .95, .99, .999, 1 - 2 ** -20]:
        stability = float(np.dot(bhat ** 2, rho ** deg))
        bound = alpha * min(1., 6 / math.sqrt((1 - rho) * R)) if R else alpha
        assert stability <= bound + 1e-12
        if R:
            record("slab_scaled_stability", stability / alpha * math.sqrt((1 - rho) * R))
        report["slab_noise_checks"] += 1
    assert np.dot(bhat ** 2, .5 ** deg) <= alpha ** (4 / 3) + 1e-12
    for k in np.unique(np.r_[np.arange(1, n + 1), [1., 1.001, max(1., L / (12 * math.log(2))), max(1., M / 8), max(1., M / 2)]]):
        low = float(np.sum(Q[deg <= k]))
        assert low <= 18 * math.sqrt(k / M) + 1e-12
        assert low <= 3 * math.sqrt(k / L) + 1e-12
        assert low <= 2 ** k * alpha ** (1 / 3) + 1e-12
        if R:
            assert low <= 18 * math.sqrt(k / R) + 1e-12
        record("low_degree_scaled_mass", low * math.sqrt(M / k))
        report["low_degree_checks"] += 1
    gamma = max(1., A0 * p * math.sqrt(L) / (alpha * math.sqrt(M)))
    for u in np.unique(np.r_[np.arange(1, n + 1), [.01, .5, .999, 1.001, M]]):
        tail = float(np.sum(P[deg >= u]))
        assert tail <= A0 * p * math.sqrt(L / u) + 1e-12
        assert tail <= gamma * alpha * math.sqrt(M / u) + 1e-12
        record("pair_tail_scaled_mass", tail / (p * math.sqrt(L / u)))
        report["pair_tail_checks"] += 1
    bins = {"star": (float(Q[0]), float(P[0]))}
    for j in range(len(deg)):
        if deg[j] == 0:
            continue
        b = math.floor(math.log2(deg[j] / M))
        previous_q, previous_p = bins.get(b, (0., 0.))
        bins[b] = previous_q + Q[j], previous_p + P[j]
    qbin = np.array([prob[0] for prob in bins.values()])
    pbin = np.array([prob[1] for prob in bins.values()])
    dbin = relative_entropy(qbin, pbin)
    assert dbin <= relative_entropy(Q, P) + 1e-11
    reference_test = 0.
    negative_moment = 0.
    for b, (qb, pb) in bins.items():
        reference = .5 if b == "star" else 2 ** (-abs(b) / 4) / (2 * ZBIN)
        if qb:
            reference_test += qb * math.log2(reference / pb)
        if b != "star":
            assert pb <= gamma * alpha * 2 ** (-b / 2) + 1e-12
            if b < 0:
                assert qb <= 18 * math.sqrt(2) * 2 ** (b / 2) + 1e-12
                negative_moment += qb * abs(b)
    assert dbin >= reference_test - 1e-11
    assert negative_moment <= CMINUS + 1e-12
    CD = math.log2(2 * ZBIN * gamma) + .75 * CMINUS + 1 + LOGE / math.e
    assert dbin >= math.log2(1 / alpha) - CD - 1e-11
    assert conditional <= alpha * (CD + LOGE) + 1e-11
    record("coarse_KL_deficit", math.log2(1 / alpha) - dbin)
    record("negative_bin_first_moment", negative_moment)
    record("R", R)
    record("L", L)
    report["regimes"][family] = report["regimes"].get(family, 0) + 1
    report["bin_KL_checks"] += 1
    report["ltfs"] += 1


for n in [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16]:
    families = {
        "equal_weights": np.ones(n),
        "binary_geometric": 2. ** np.arange(n),
        "almost_dictator": np.r_[4 * n, np.ones(n - 1)],
        "zero_remaining": np.r_[1., np.zeros(n - 1)],
        "two_scale": np.r_[100 * np.ones((n + 1) // 2), np.ones(n // 2)],
        "integer_atoms": rng.integers(1, 5, n).astype(float),
        "normal_weights": np.maximum(1., np.rint(1000 * abs(rng.normal(size=n)))),
        "lognormal_weights": np.maximum(1., np.rint(100000 * rng.lognormal(0, 4, n))),
    }
    index = np.arange(1 << n)
    x = 2 * ((index[:, None] >> np.arange(n)) & 1) - 1
    for family, weights in families.items():
        score = x @ weights
        distinct = np.unique(score)
        # Ties and the smallest/largest two gaps are included. The latter
        # include minority densities 2^-n and 2^(1-n) where available.
        selected = np.unique(np.r_[0, 1, len(distinct) - 3, len(distinct) - 2,
                                   np.linspace(0, len(distinct) - 2, 13).astype(int)])
        for j in selected:
            if not 0 <= j < len(distinct) - 1:
                continue
            for theta in [distinct[j], (distinct[j] + distinct[j + 1]) / 2]:
                check(weights, theta, family)

Path(__file__).with_name("largest_weight_ltf_verification.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
