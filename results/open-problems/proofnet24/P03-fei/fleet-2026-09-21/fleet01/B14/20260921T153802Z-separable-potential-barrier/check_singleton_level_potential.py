"""Finite diagnostics for the B14 singleton-level FEI potential.

This is not a proof of FEI.  The universal statements in the companion report are
algebraic.  This script only (i) exhausts Boolean truth tables through four variables
(up to global sign), (ii) checks the exact level-one restriction-flux identity on
that atlas, and (iii) reconstructs the preserved Numaro 18-variable seed to measure
how the level-one credit propagates along its all-core recursive path.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
import numpy as np

LAMBDA = 4.0
EXPECTED_SEED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
RAW_NUMARO_ALLCORE = [
    4.552314588405312149574520855739,
    6.329015279480452454420605168315,
    6.890112313700557073165093644989,
    7.051852835007350697107979721615,
    7.096060618744925556394954995917,
]


def hadamard(n: int) -> np.ndarray:
    h = np.array([[1]], dtype=np.int16)
    while h.shape[0] < n:
        h = np.block([[h, h], [h, -h]])
    return h


def entropy_rows(p: np.ndarray) -> np.ndarray:
    z = np.zeros_like(p, dtype=float)
    mask = p > 0
    z[mask] = -p[mask] * np.log2(p[mask])
    return z.sum(axis=1)


def atlas_n4() -> dict:
    n = 4
    N = 1 << n
    # Global sign does not change squared Fourier data, restrictions, or influences.
    m = 1 << (N - 1)
    ids = np.arange(m, dtype=np.uint32)[:, None]
    bits = ((ids >> np.arange(N - 1, dtype=np.uint32)) & 1).astype(np.int8)
    vals = np.ones((m, N), dtype=np.int8)
    vals[:, 1:] = 1 - 2 * bits

    HN = hadamard(N)
    W = (vals.astype(np.int16) @ HN.T) / N
    P = W * W
    sizes = np.array([s.bit_count() for s in range(N)])
    H = entropy_rows(P)
    W1 = P[:, sizes == 1].sum(axis=1)

    dH = np.zeros((m, n), dtype=float)
    dW1 = np.zeros((m, n), dtype=float)
    inf = np.zeros((m, n), dtype=float)
    idx = np.arange(N)
    Hc = hadamard(N // 2)
    csizes = np.array([s.bit_count() for s in range(N // 2)])

    for i in range(n):
        child_H = []
        child_W1 = []
        for b in (0, 1):
            cols = idx[((idx >> i) & 1) == b]
            CW = (vals[:, cols].astype(np.int16) @ Hc.T) / (N // 2)
            CP = CW * CW
            child_H.append(entropy_rows(CP))
            child_W1.append(CP[:, csizes == 1].sum(axis=1))
        dH[:, i] = H - (child_H[0] + child_H[1]) / 2
        dW1[:, i] = W1 - (child_W1[0] + child_W1[1]) / 2
        base = idx[((idx >> i) & 1) == 0]
        inf[:, i] = (vals[:, base] != vals[:, base | (1 << i)]).mean(axis=1)

    # Independent exact-formula check: Delta_i W1 = fhat(i)^2 - sum_{j!=i} fhat(i,j)^2.
    flux = np.zeros_like(dW1)
    for i in range(n):
        ei = P[:, 1 << i]
        qi = np.zeros(m, dtype=float)
        for j in range(n):
            if i != j:
                qi += P[:, (1 << i) | (1 << j)]
        flux[:, i] = ei - qi
    max_flux_error = float(np.max(np.abs(dW1 - flux)))
    if max_flux_error != 0.0:
        raise AssertionError(max_flux_error)

    relevant = inf > 0
    has_relevant = relevant.any(axis=1)

    def worst(lam: float) -> tuple[float, int]:
        ratio = np.full_like(inf, np.inf, dtype=float)
        np.divide(dH + lam * dW1, inf, out=ratio, where=relevant)
        selector = ratio.min(axis=1)
        selector = np.where(has_relevant, selector, -np.inf)
        arg = int(np.argmax(selector))
        return float(selector[arg]), arg

    raw, raw_arg = worst(0.0)
    phi4, phi4_arg = worst(LAMBDA)

    # A fine one-dimensional diagnostic for lambda; not a theorem/optimization certificate.
    grid = np.linspace(0.0, 6.0, 1201)
    best = (float("inf"), None, None)
    for lam in grid:
        val, arg = worst(float(lam))
        if val < best[0]:
            best = (val, float(lam), arg)

    return {
        "truth_tables_checked_up_to_global_sign": int(m),
        "level_one_flux_identity_max_abs_error": max_flux_error,
        "raw_entropy_selector_worst_n4": raw,
        "raw_witness_index": raw_arg,
        "phi_lambda": LAMBDA,
        "phi_selector_worst_n4": phi4,
        "phi_witness_index": phi4_arg,
        "grid_best_lambda_step_0p005": best[1],
        "grid_best_worst_selector": best[0],
        "grid_best_witness_index": best[2],
    }


def fwht_int(a: np.ndarray) -> np.ndarray:
    out = np.array(a, dtype=np.int64, copy=True)
    h = 1
    while h < len(out):
        view = out.reshape(-1, 2 * h)
        left = view[:, :h].copy()
        right = view[:, h:].copy()
        view[:, :h] = left + right
        view[:, h:] = left - right
        h *= 2
    return out


def reconstruct_numaro() -> np.ndarray:
    TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
    BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
    slices = [
        (TOP, BOT),
        (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
        (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
        ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
        (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
        (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
        ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
        ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
        ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
        ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
    ]
    base = int("".join(slices[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in slices[1:]]
    hosts = [[x for x in range(512) if (mask >> x) & 1] for mask in masks]
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int8)
    table = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    if digest != EXPECTED_SEED_SHA:
        raise AssertionError((digest, EXPECTED_SEED_SHA))
    return table


def numaro_allcore() -> dict:
    table = reconstruct_numaro()
    W = fwht_int(table)
    N = len(table)
    den = N * N

    def mass(mask: int) -> Fraction:
        return Fraction(int(W[mask]) ** 2, den)

    core_i = 0
    s_core = Fraction(abs(int(W[1 << core_i])), N)
    # The seed verifier independently proves influence = singleton magnitude = 57/256
    # for the core class. Re-use that exact certified class value here.
    a_core = Fraction(57, 256)
    if s_core != a_core:
        raise AssertionError((s_core, a_core))

    W1 = sum((mass(1 << i) for i in range(18)), Fraction(0))
    Q_core = sum((mass((1 << core_i) | (1 << j)) for j in range(18) if j != core_i), Fraction(0))
    e = mass(1 << core_i)
    p_inf = a_core
    qstar = Q_core
    inner_W1 = W1

    rows = []
    for depth, raw in enumerate(RAW_NUMARO_ALLCORE, start=1):
        dW = e - qstar
        correction = dW / p_inf
        rows.append({
            "depth": depth,
            "p_influence_exact": str(p_inf),
            "singleton_mass_exact": str(e),
            "pair_star_mass_exact": str(qstar),
            "delta_W1_over_influence": float(correction),
            "inherited_raw_allcore_ratio": raw,
            "phi4_allcore_ratio": raw + LAMBDA * float(correction),
        })
        if depth < len(RAW_NUMARO_ALLCORE):
            # For balanced identical-inner composition F=G(g^1,...,g^m):
            # e' = s_j^2 e,
            # Q' = s_j^2 Q + e W1(g) Q_j(G).
            qstar = s_core * s_core * qstar + e * inner_W1 * Q_core
            e = s_core * s_core * e
            p_inf = a_core * p_inf
            inner_W1 = W1 * inner_W1

    return {
        "seed_sha256": EXPECTED_SEED_SHA,
        "seed_W1_exact": str(W1),
        "seed_core_singleton_amplitude_exact": str(s_core),
        "seed_core_pair_star_mass_exact": str(Q_core),
        "allcore_rows": rows,
    }


def one_point_phi4() -> list[dict]:
    rows = []
    for n in range(2, 13):
        N = 1 << n
        vals = np.ones(N, dtype=np.int8)
        vals[0] = -1
        W = fwht_int(vals) / N
        p = W * W
        sizes = np.array([s.bit_count() for s in range(N)])
        mask = p > 0
        H = float(-(p[mask] * np.log2(p[mask])).sum())
        W1 = float(p[sizes == 1].sum())
        i = 0
        idx = np.arange(N)
        child_vals = [vals[((idx >> i) & 1) == b] for b in (0, 1)]
        child_phi = []
        for cv in child_vals:
            CW = fwht_int(cv) / (N // 2)
            cp = CW * CW
            cs = np.array([s.bit_count() for s in range(N // 2)])
            cm = cp > 0
            cH = float(-(cp[cm] * np.log2(cp[cm])).sum())
            cW1 = float(cp[cs == 1].sum())
            child_phi.append(cH + LAMBDA * cW1)
        phi = H + LAMBDA * W1
        base = idx[((idx >> i) & 1) == 0]
        influence = float(np.mean(vals[base] != vals[base | (1 << i)]))
        ratio = (phi - sum(child_phi) / 2) / influence
        rows.append({"n": n, "phi4_selector_ratio": ratio})
    return rows


def main() -> None:
    result = {
        "status": "PASS",
        "warning": "finite diagnostics only; full FEI remains open",
        "atlas_n4": atlas_n4(),
        "one_point_phi4": one_point_phi4(),
        "numaro": numaro_allcore(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
