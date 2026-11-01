"""PROB20-17 corroborative checker for the 2026-09-16 even-m four-run theorem.

Checks (numerical only; analytic proof is in the paired report):
  * exact orbit counts for the two equal-split four-run families;
  * endpoint symmetrization inequality;
  * spectral lower bound for every selected four-run orbit;
  * selected-orbit lower envelope for m=4,6;
  * full C_{4,4} >= 30 ||AB||^4 by direct enumeration.

Seed: 20260916024632.
"""
import itertools
import numpy as np

SEED = 20260916024632
rng = np.random.default_rng(SEED)


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rho(M):
    return float(np.max(np.abs(np.linalg.eigvals(M))))


def psd_power(A, s):
    vals, vecs = np.linalg.eigh(A)
    vals = np.maximum(vals, 0.0)
    return (vecs * (vals ** s)) @ vecs.conj().T


def rand_psd(d, spread=7.0):
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    Q, _ = np.linalg.qr(X)
    vals = np.exp(rng.uniform(-spread, 0.0, size=d))
    return Q @ np.diag(vals) @ Q.conj().T


def word_matrix(A, B, word):
    M = np.eye(A.shape[0], dtype=complex)
    for bit in word:
        M = M @ (A if bit == 0 else B)
    return M


def rotations(word):
    word = list(word)
    n = len(word)
    return {tuple(word[k:] + word[:k]) for k in range(n)}


def four_run_families(m):
    assert m >= 4 and m % 2 == 0
    q = m // 2
    F_B = set()
    for a in range(1, q + 1):
        F_B |= rotations([0] * a + [1] * q + [0] * (m - a) + [1] * q)
    F_A = set()
    for b in range(1, q + 1):
        F_A |= rotations([0] * q + [1] * b + [0] * q + [1] * (m - b))
    return F_B, F_A, F_B | F_A


def all_balanced_words(m):
    n = 2 * m
    for apos in itertools.combinations(range(n), m):
        w = [1] * n
        for k in apos:
            w[k] = 0
        yield tuple(w)


for m in (4, 6, 8, 10):
    F_B, F_A, U = four_run_families(m)
    assert len(F_B) == m * (m - 1)
    assert len(F_A) == m * (m - 1)
    assert len(F_B & F_A) == m
    assert len(U) == m * (2 * m - 3)

min_sym = float("inf")
min_orbit = float("inf")
min_selected = float("inf")
min_full44 = float("inf")

for m in (4, 6):
    q = m // 2
    F_B, F_A, U = four_run_families(m)
    block = rotations([0] * m + [1] * m)
    alt = {tuple([0, 1] * m), tuple([1, 0] * m)}
    selected = block | U | alt
    expected_selected = 2 * m + m * (2 * m - 3) + 2
    assert len(selected) == expected_selected

    for d in (2, 3, 5):
        trials = 24 if m == 4 else 12
        for _ in range(trials):
            A = rand_psd(d)
            B = rand_psd(d)
            p = opnorm(A @ B)
            r = rho(A @ B)
            if p < 1e-13:
                continue
            t = r / p

            for a in range(1, q + 1):
                X = psd_power(A, (m - a) / 2) @ psd_power(B, q) @ psd_power(A, a / 2)
                X0 = psd_power(A, m / 4) @ psd_power(B, q) @ psd_power(A, m / 4)
                ratio = opnorm(X) / opnorm(X0)
                min_sym = min(min_sym, ratio)
                assert ratio >= 1.0 - 2e-9

            denom = p ** m * t ** (-(m - 4))
            for w in U:
                ratio = rho(word_matrix(A, B, w)) / denom
                min_orbit = min(min_orbit, ratio)
                assert ratio >= 1.0 - 2e-8

            selected_sum = sum(opnorm(word_matrix(A, B, w)) for w in selected)
            lower = p ** m * (
                2 * m * t ** (-(m - 2))
                + m * (2 * m - 3) * t ** (-(m - 4))
                + 2 * t ** m
            )
            ratio = selected_sum / lower
            min_selected = min(min_selected, ratio)
            assert ratio >= 1.0 - 2e-8

            if m == 4:
                full = sum(opnorm(word_matrix(A, B, w)) for w in all_balanced_words(4))
                ratio = full / (30.0 * p ** 4)
                min_full44 = min(min_full44, ratio)
                assert ratio >= 1.0 - 2e-8

print("seed", SEED)
print("min endpoint-symmetrization ratio", min_sym)
print("min selected-four-run spectral ratio", min_orbit)
print("min selected-sum / analytic envelope", min_selected)
print("min full C44 / (30 ||AB||^4)", min_full44)
print("PASS")
