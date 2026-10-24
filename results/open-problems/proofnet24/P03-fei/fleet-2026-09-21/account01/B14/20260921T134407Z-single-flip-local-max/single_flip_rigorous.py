from __future__ import annotations

import json
import math
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

import numpy as np


N_BITS = 16
N_PAIRS = 8
LOG_TERMS = 36


def fwht_int(values: np.ndarray) -> np.ndarray:
    """Unnormalised Walsh-Hadamard transform, exact in int64 for this 16-bit test."""
    a = np.asarray(values, dtype=np.int64).copy()
    h = 1
    while h < a.size:
        blocks = a.reshape(-1, 2 * h)
        left = blocks[:, :h].copy()
        right = blocks[:, h:].copy()
        blocks[:, :h] = left + right
        blocks[:, h:] = left - right
        h *= 2
    return a


def width2_tribes_8() -> np.ndarray:
    """+1 iff none of the eight ordered pairs equals 11."""
    n = 1 << N_BITS
    x = np.arange(n, dtype=np.uint32)
    bad = np.zeros(n, dtype=bool)
    for j in range(N_PAIRS):
        bad |= ((x >> (2 * j)) & 3) == 3
    f = np.ones(n, dtype=np.int64)
    f[bad] = -1
    return f


def orbit_representative(a: int, b: int, c: int) -> int:
    """Canonical point with a 00-pairs, b 01-pairs and c 11-pairs."""
    assert a + b + c == N_PAIRS
    x = 0
    j = a
    for _ in range(b):
        x |= 1 << (2 * j)
        j += 1
    for _ in range(c):
        x |= 3 << (2 * j)
        j += 1
    return x


def entropy_float(p: np.ndarray) -> float:
    z = p[p > 0]
    return float(-np.dot(z, np.log2(z)))


def selector_float(tab: np.ndarray) -> dict:
    """Exploratory float evaluation used only to choose an explicit coordinate to certify."""
    n = N_BITS
    N = tab.size
    W = fwht_int(tab)
    p = (W.astype(np.float64) / N) ** 2
    H = entropy_float(p)
    idx = np.arange(N, dtype=np.int64)
    ratios = []
    alpha = []
    for i in range(n):
        low = idx[((idx >> i) & 1) == 0]
        u = W[low].astype(np.float64)
        v = W[low + (1 << i)].astype(np.float64)
        a_i = float(np.dot(v, v) / (N * N))
        hp = entropy_float(((u + v) / N) ** 2)
        hm = entropy_float(((u - v) / N) ** 2)
        dH = H - 0.5 * (hp + hm)
        ratios.append(dH / a_i)
        alpha.append(a_i)
    I = float(sum(alpha))
    return {
        "W": W,
        "rho0_float": float(min(ratios)),
        "argmin_float": int(min(range(n), key=lambda i: ratios[i])),
        "H_over_I_float": float(H / I),
        "I_float": I,
        "ratios_float": ratios,
    }


def ln_atanh_bounds(y: Fraction, terms: int = LOG_TERMS) -> tuple[Fraction, Fraction]:
    """Exact rational enclosure for ln(y), 1 <= y <= 2, via positive atanh series."""
    assert Fraction(1) <= y <= Fraction(2)
    if y == 1:
        return Fraction(0), Fraction(0)
    z = (y - 1) / (y + 1)
    z2 = z * z
    zpow = z
    s = Fraction(0)
    for k in range(terms):
        s += 2 * zpow / (2 * k + 1)
        zpow *= z2
    remainder = 2 * zpow / ((2 * terms + 1) * (1 - z2))
    return s, s + remainder


@lru_cache(maxsize=None)
def ln2_bounds(terms: int = LOG_TERMS) -> tuple[Fraction, Fraction]:
    # 2 = (1+1/3)/(1-1/3), so the same positive series applies.
    return ln_atanh_bounds(Fraction(2), terms)


@lru_cache(maxsize=None)
def log2_integer_bounds(m: int, terms: int = LOG_TERMS) -> tuple[Fraction, Fraction]:
    """Exact rational enclosure of log_2(m) for positive integer m."""
    assert m >= 1
    if m == 1:
        return Fraction(0), Fraction(0)
    e = m.bit_length() - 1
    y = Fraction(m, 1 << e)
    ly_lo, ly_hi = ln_atanh_bounds(y, terms)
    l2_lo, l2_hi = ln2_bounds(terms)
    return Fraction(e) + ly_lo / l2_hi, Fraction(e) + ly_hi / l2_lo


def linear_log_sum_bounds(weights: dict[int, Fraction]) -> tuple[Fraction, Fraction]:
    """Enclose sum_m weights[m] log_2(m) exactly from rational log bounds."""
    lo = Fraction(0)
    hi = Fraction(0)
    for m, w in weights.items():
        if not w:
            continue
        l, u = log2_integer_bounds(int(m))
        if w > 0:
            lo += w * l
            hi += w * u
        else:
            lo += w * u
            hi += w * l
    return lo, hi


def delta_over_influence_interval(W: np.ndarray, i: int) -> tuple[Fraction, Fraction]:
    """
    Exact rational enclosure for Delta_i H / Inf_i.

    If u=W_T and v=W_{T+i}, then constants cancel and
      N^2 Delta_i H =
        sum_T [((u+v)^2/2) log2 (u+v)^2
              +((u-v)^2/2) log2 (u-v)^2
              -u^2 log2 u^2-v^2 log2 v^2].
    Also N^2 Inf_i = sum_T v^2.
    """
    N = W.size
    idx = np.arange(N, dtype=np.int64)
    low = idx[((idx >> i) & 1) == 0]
    weights: dict[int, Fraction] = defaultdict(Fraction)
    influence_numerator = 0

    for t0 in low:
        u = int(W[t0])
        v = int(W[t0 + (1 << i)])
        influence_numerator += v * v
        ap = (u + v) * (u + v)
        am = (u - v) * (u - v)
        uu = u * u
        vv = v * v
        if ap:
            weights[ap] += Fraction(ap, 2)
        if am:
            weights[am] += Fraction(am, 2)
        if uu:
            weights[uu] -= uu
        if vv:
            weights[vv] -= vv

    assert influence_numerator > 0
    lo, hi = linear_log_sum_bounds(weights)
    d = Fraction(influence_numerator)
    return lo / d, hi / d


def h_over_i_interval(W: np.ndarray) -> tuple[Fraction, Fraction]:
    """Exact rational enclosure for H/I from an integer Walsh vector."""
    N = W.size
    n = N.bit_length() - 1
    log_weights: dict[int, Fraction] = defaultdict(Fraction)
    influence_num = 0
    for s, w0 in enumerate(W.tolist()):
        w = int(w0)
        m = w * w
        if not m:
            continue
        log_weights[m] += m
        influence_num += s.bit_count() * m
    assert influence_num > 0
    slog_lo, slog_hi = linear_log_sum_bounds(log_weights)
    # N^2 H = 2n N^2 - sum W_S^2 log2(W_S^2)
    constant = Fraction(2 * n * N * N)
    H_lo = constant - slog_hi
    H_hi = constant - slog_lo
    d = Fraction(influence_num)
    return H_lo / d, H_hi / d


def decimal_bound(x: Fraction, lower: bool, precision: int = 32) -> str:
    """Directed decimal rendering of an exact Fraction."""
    with localcontext() as ctx:
        ctx.prec = precision
        ctx.rounding = ROUND_FLOOR if lower else ROUND_CEILING
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def fraction_fingerprint(x: Fraction) -> str:
    """Compact identity for a huge exact rational without serialising thousands of digits."""
    import hashlib
    def b(i: int) -> bytes:
        n = max(1, (i.bit_length() + 7) // 8)
        return i.to_bytes(n, "big", signed=False)
    return hashlib.sha256(b(x.numerator) + b(x.denominator)).hexdigest()


def main() -> None:
    baseline = width2_tribes_8()
    base_float = selector_float(baseline)
    base_lo, base_hi = delta_over_influence_interval(base_float["W"], 0)
    # Coordinate transitivity of width-2 tribes makes this its exact rho_0 interval.
    base_h_lo, base_h_hi = h_over_i_interval(base_float["W"])

    rows = []
    for a in range(N_PAIRS + 1):
        for b in range(N_PAIRS + 1 - a):
            c = N_PAIRS - a - b
            x = orbit_representative(a, b, c)
            tab = baseline.copy()
            tab[x] *= -1
            fl = selector_float(tab)
            i = fl["argmin_float"]
            # The float step only selects a concrete coordinate.  The following
            # exact interval alone certifies rho_0(tab) <= this coordinate ratio.
            lo, hi = delta_over_influence_interval(fl["W"], i)
            rows.append({
                "orbit_abc": [a, b, c],
                "representative_index": x,
                "certified_coordinate": i,
                "coordinate_ratio_lower": decimal_bound(lo, True),
                "coordinate_ratio_upper": decimal_bound(hi, False),
                "coordinate_interval_fingerprint": fraction_fingerprint(lo) + ":" + fraction_fingerprint(hi),
                "rho0_float_search_only": fl["rho0_float"],
                "H_over_I_float_search_only": fl["H_over_I_float"],
            })

    best = max(
        rows,
        key=lambda r: Decimal(r["coordinate_ratio_upper"]),
    )
    # Recompute the exact upper endpoint for the selected representative/coordinate.
    ba, bb, bc = best["orbit_abc"]
    best_tab = baseline.copy()
    best_tab[orbit_representative(ba, bb, bc)] *= -1
    best_W = fwht_int(best_tab)
    _, best_upper = delta_over_influence_interval(best_W, int(best["certified_coordinate"]))
    gap_lower = base_lo - best_upper
    assert gap_lower > 0

    # The all-ones point is fixed by the full automorphism group, so this flip
    # remains coordinate-transitive.  Certify it and also certify that every
    # other single-point orbit lies strictly below it.
    top = baseline.copy()
    top[orbit_representative(0, 0, 8)] *= -1
    topW = fwht_int(top)
    top_rho_lo, top_rho_hi = delta_over_influence_interval(topW, 0)
    other_rows = [r for r in rows if r["orbit_abc"] != [0, 0, 8]]
    second = max(other_rows, key=lambda r: Decimal(r["coordinate_ratio_upper"]))
    sa, sb, sc = second["orbit_abc"]
    second_tab = baseline.copy()
    second_tab[orbit_representative(sa, sb, sc)] *= -1
    second_W = fwht_int(second_tab)
    _, second_upper = delta_over_influence_interval(
        second_W, int(second["certified_coordinate"])
    )
    top_vs_second_gap = top_rho_lo - second_upper
    assert top_vs_second_gap > 0

    # Also rigorously enclose H/I for the finite one-flip maximiser.
    top_h_lo, top_h_hi = h_over_i_interval(topW)

    out = {
        "status": "PASS",
        "claim_scope": "all 65536 single-truth-table-point flips of width-2 tribes with 8 pairs",
        "method": "45 orbits under pair permutations and within-pair swaps; one rigorously bounded coordinate per orbit",
        "baseline": {
            "rho0_lower": decimal_bound(base_lo, True),
            "rho0_upper": decimal_bound(base_hi, False),
            "rho0_interval_fingerprint": fraction_fingerprint(base_lo) + ":" + fraction_fingerprint(base_hi),
            "H_over_I_lower": decimal_bound(base_h_lo, True),
            "H_over_I_upper": decimal_bound(base_h_hi, False),
        },
        "best_single_flip_by_certified_upper_bound": best,
        "best_non_top_single_flip_by_certified_upper_bound": second,
        "top_flip_rho0": {
            "lower": decimal_bound(top_rho_lo, True),
            "upper": decimal_bound(top_rho_hi, False),
        },
        "top_vs_best_other_gap_lower": decimal_bound(top_vs_second_gap, True),
        "top_vs_best_other_gap_exact_positive": True,
        "strict_gap_lower": decimal_bound(gap_lower, True),
        "strict_gap_exact_positive": True,
        "strict_gap_fraction_fingerprint": fraction_fingerprint(gap_lower),
        "top_flip_H_over_I": {
            "lower": decimal_bound(top_h_lo, True),
            "upper": decimal_bound(top_h_hi, False),
        },
        "all_45_orbits": rows,
        "notes": [
            "Every strict comparison is between exact Fractions produced by positive-series remainder bounds.",
            "Float64 values only select a coordinate and are not used to prove the inequality.",
            "This finite local-maximality theorem does not prove a universal bound on rho0 and does not prove FEI.",
        ],
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
