"""Exact/rational certificate for a recursive FEI existential-restriction obstruction.

This independently reconstructs Numaro's published balanced monotone n=18 seed G
from the ten 512-bit slices already preserved in the project, verifies the published
truth-table SHA-256, and certifies the restriction-decrement ratios of the finite
recursive compositions

    F_1 = G,
    F_{r+1} = G(F_r^(1),...,F_r^(18))

on disjoint blocks, through r=5.

The new ingredient is the proved one-coordinate recursion used by the report beside
this file.  All Walsh transforms are integer.  Every logarithm entering a reported
strict inequality is enclosed by a rational atanh series; floating point is used
only for convenient non-authoritative display.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import argparse
import hashlib
import json

import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
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


def fwht(a: np.ndarray) -> np.ndarray:
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


def reconstruct_seed() -> tuple[np.ndarray, list[list[int]]]:
    if any(len(x) != 64 for row in SLICES for x in row):
        raise AssertionError("bad slice length")
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    if any(m & base for m in masks) or any(m.bit_count() != 2 for m in masks):
        raise AssertionError("bad auxiliary-host reconstruction")
    seen = base
    hosts: list[list[int]] = []
    for m in masks:
        if seen & m:
            raise AssertionError("overlapping auxiliary hosts")
        seen |= m
        hosts.append([x for x in range(512) if (m >> x) & 1])
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int8)
    table = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    if digest != EXPECTED_SHA:
        raise AssertionError((digest, EXPECTED_SHA))
    return table, hosts


def log2_fraction_interval(x: int, terms: int) -> tuple[Fraction, Fraction]:
    """Rigorous enclosure of log2(x) for a positive integer x."""
    if x <= 0:
        raise ValueError(x)
    e = x.bit_length() - 1
    den = 1 << e
    z = Fraction(x - den, x + den)

    def ln_atanh(z0: Fraction) -> tuple[Fraction, Fraction]:
        z2 = z0 * z0
        zp = z0
        s = Fraction(0)
        for k in range(terms):
            s += zp / (2 * k + 1)
            zp *= z2
        lo = 2 * s
        hi = lo + 2 * zp / ((2 * terms + 1) * (1 - z2))
        return lo, hi

    if z == 0:
        return Fraction(e), Fraction(e)
    nlo, nhi = ln_atanh(z)
    dlo, dhi = ln_atanh(Fraction(1, 3))
    return Fraction(e) + nlo / dhi, Fraction(e) + nhi / dlo


def entropy_interval(counter: Counter[int], common_den: int, terms: int) -> tuple[Fraction, Fraction]:
    if sum(k * v for k, v in counter.items()) != common_den:
        raise AssertionError("weights do not sum to one")
    if common_den & (common_den - 1):
        raise AssertionError("certificate expects dyadic common denominator")
    log_den = Fraction(common_den.bit_length() - 1)
    slo = Fraction(0)
    shi = Fraction(0)
    for num, mult in counter.items():
        if num <= 0:
            raise AssertionError("nonpositive mass")
        lo, hi = log2_fraction_interval(num, terms)
        weight = Fraction(num * mult, common_den)
        slo += weight * lo
        shi += weight * hi
    return log_den - shi, log_den - slo


def walsh_entropy_counter(values: np.ndarray) -> tuple[Counter[int], int, np.ndarray]:
    W = fwht(values)
    den = len(values) ** 2
    counter = Counter(int(x) * int(x) for x in W if x)
    if sum(k * v for k, v in counter.items()) != den:
        raise AssertionError("Parseval failed")
    return counter, den, W


def child(values: np.ndarray, n: int, i: int, bit: int) -> np.ndarray:
    idx = np.arange(1 << n)
    return values[((idx >> i) & 1) == bit]


def influence_exact(W: np.ndarray, n: int, i: int) -> Fraction:
    bit = 1 << i
    num = sum(int(W[s]) * int(W[s]) for s in range(1 << n) if s & bit)
    return Fraction(num, (1 << n) ** 2)


def singleton_exact(W: np.ndarray, n: int, i: int) -> Fraction:
    return Fraction(int(W[1 << i]), 1 << n)


def biased_entropy_counter(W: np.ndarray, n: int, i: int, q: Fraction, sign: int) -> tuple[Counter[int], int]:
    """Biased Fourier entropy of G when only logical coordinate i has mean sign*q."""
    Q, D = q.numerator, q.denominator
    if D & (D - 1):
        raise AssertionError("q must be dyadic")
    N = 1 << n
    bit = 1 << i
    vv = D * D - Q * Q
    masses: Counter[int] = Counter()
    for K in range(N):
        if K & bit:
            continue
        a = int(W[K])
        b = int(W[K | bit])
        z = a * D + sign * Q * b
        if z:
            masses[z * z] += 1
        if b and vv:
            masses[vv * b * b] += 1
    common_den = (N * D) ** 2
    if sum(k * v for k, v in masses.items()) != common_den:
        raise AssertionError("biased Parseval failed")
    return masses, common_den


def binary_entropy_q2(q: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    Q, D = q.numerator, q.denominator
    den = D * D
    masses: Counter[int] = Counter()
    if Q:
        masses[Q * Q] += 1
    if den != Q * Q:
        masses[den - Q * Q] += 1
    return entropy_interval(masses, den, terms)


def outward_decimal(x: Fraction, digits: int, upper: bool) -> str:
    scale = 10 ** digits
    y = x * scale
    if upper:
        q = -((-y.numerator) // y.denominator)
    else:
        q = y.numerator // y.denominator
    sign = "-" if q < 0 else ""
    q = abs(q)
    s = str(q).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}" if digits else f"{sign}{s}"


def main() -> dict:
    TERMS = 40
    table, hosts = reconstruct_seed()
    n = 18
    if int(table.sum()) != 0:
        raise AssertionError("seed not balanced")
    Hcounter, Hden, W = walsh_entropy_counter(table)
    Hseed = entropy_interval(Hcounter, Hden, TERMS)
    infs = [influence_exact(W, n, i) for i in range(n)]
    sings = [singleton_exact(W, n, i) for i in range(n)]
    core_a = Fraction(57, 256)
    aux_a = Fraction(1, 256)
    if infs[:9] != [core_a] * 9 or infs[9:] != [aux_a] * 9:
        raise AssertionError((infs[:9], infs[9:]))
    if sings[:9] != [core_a] * 9 or sings[9:] != [aux_a] * 9:
        raise AssertionError((sings[:9], sings[9:]))

    child_fingerprints = []
    base_ratio = {}
    for label, rep, a, members in [("C", 0, core_a, range(9)), ("A", 9, aux_a, range(9, 18))]:
        class_fps = []
        rep_entropies = None
        for i in members:
            fps = []
            eints = []
            for b in (0, 1):
                c, d, _ = walsh_entropy_counter(child(table, n, i, b))
                fp = hashlib.sha256(json.dumps({"den": d, "weights": sorted(c.items())}, separators=(",", ":")).encode()).hexdigest()
                fps.append(fp)
                eints.append(entropy_interval(c, d, TERMS))
            if fps[0] != fps[1]:
                raise AssertionError("+/- child spectra differ in class")
            class_fps.append(tuple(fps))
            if i == rep:
                rep_entropies = eints
        if len(set(class_fps)) != 1:
            raise AssertionError("coordinate class child spectra differ")
        child_fingerprints.append({"class": label, "members": len(list(members)), "fingerprint": class_fps[0][0]})
        assert rep_entropies is not None
        dlo = Hseed[0] - (rep_entropies[0][1] + rep_entropies[1][1]) / 2
        dhi = Hseed[1] - (rep_entropies[0][0] + rep_entropies[1][0]) / 2
        base_ratio[label] = (dlo / a, dhi / a)

    type_data = {
        "C": {"rep": 0, "a": core_a, "s": core_a},
        "A": {"rep": 9, "a": aux_a, "s": aux_a},
    }
    kcache: dict[tuple[str, Fraction], tuple[Fraction, Fraction]] = {}
    biased_class_checks = []

    def K_interval(label: str, q: Fraction) -> tuple[Fraction, Fraction]:
        key = (label, q)
        if key in kcache:
            return kcache[key]
        d = type_data[label]
        members = range(9) if label == "C" else range(9, 18)
        sign_fps = {1: set(), -1: set()}
        rep_h = {}
        for i in members:
            for sign in (1, -1):
                c, den = biased_entropy_counter(W, n, i, q, sign)
                fp = hashlib.sha256(json.dumps({"den": den, "weights": sorted(c.items())}, separators=(",", ":")).encode()).hexdigest()
                sign_fps[sign].add(fp)
                if i == d["rep"]:
                    rep_h[sign] = entropy_interval(c, den, TERMS)
        if len(sign_fps[1]) != 1 or len(sign_fps[-1]) != 1:
            raise AssertionError("biased entropy differs within coordinate class")
        hv = binary_entropy_q2(q, TERMS)
        a = d["a"]
        klo = Hseed[0] - (rep_h[1][1] + rep_h[-1][1]) / 2 + a * hv[0]
        khi = Hseed[1] - (rep_h[1][0] + rep_h[-1][0]) / 2 + a * hv[1]
        kcache[key] = (klo, khi)
        biased_class_checks.append({
            "class": label,
            "q": str(q),
            "plus_fingerprint": next(iter(sign_fps[1])),
            "minus_fingerprint": next(iter(sign_fps[-1])),
        })
        return klo, khi

    states = []
    for label, d in type_data.items():
        states.append({
            "path": label,
            "p": d["a"],
            "q": abs(d["s"]),
            "lo": base_ratio[label][0],
            "hi": base_ratio[label][1],
        })

    levels = []
    for r in range(1, 6):
        ordered = sorted(states, key=lambda s: s["lo"])
        levels.append({
            "r": r,
            "variables": 18 ** r,
            "min_path_outer_to_inner": ordered[0]["path"],
            "rho_lower": outward_decimal(ordered[0]["lo"], 30, False),
            "rho_upper": outward_decimal(ordered[0]["hi"], 30, True),
            "all_path_classes": [
                {
                    "path_outer_to_inner": s["path"],
                    "p_exact": str(s["p"]),
                    "q_exact": str(s["q"]),
                    "ratio_lower": outward_decimal(s["lo"], 30, False),
                    "ratio_upper": outward_decimal(s["hi"], 30, True),
                }
                for s in ordered
            ],
        })
        if r == 5:
            break
        new_states = []
        for s in states:
            for label, d in type_data.items():
                klo, khi = K_interval(label, s["q"])
                denom = d["a"] * s["p"]
                new_states.append({
                    "path": label + s["path"],
                    "p": d["a"] * s["p"],
                    "q": abs(d["s"]) * s["q"],
                    "lo": s["lo"] + klo / denom,
                    "hi": s["hi"] + khi / denom,
                })
        states = new_states

    Iseed = Fraction(261, 128)
    full_ratios = []
    for r in range(1, 6):
        factor = sum(Iseed ** j for j in range(r)) / (Iseed ** r)
        lo = Hseed[0] * factor
        hi = Hseed[1] * factor
        full_ratios.append({
            "r": r,
            "H_over_I_lower": outward_decimal(lo, 30, False),
            "H_over_I_upper": outward_decimal(hi, 30, True),
        })

    result = {
        "status": "PASS",
        "scope": "finite recursive existential-restriction certificate; not full FEI",
        "external_seed_provenance": "Numaro NUMARO-2026-016, 2026-07-22; recovered from project-preserved source slices",
        "seed_sha256": EXPECTED_SHA,
        "seed_variables": 18,
        "seed_balance_sum": int(table.sum()),
        "seed_I_exact": str(Iseed),
        "seed_H_lower": outward_decimal(Hseed[0], 30, False),
        "seed_H_upper": outward_decimal(Hseed[1], 30, True),
        "coordinate_classes": {
            "C": {"count": 9, "influence": str(core_a), "singleton": str(core_a)},
            "A": {"count": 9, "influence": str(aux_a), "singleton": str(aux_a)},
        },
        "child_spectrum_class_checks": child_fingerprints,
        "biased_spectrum_class_checks": biased_class_checks,
        "log_enclosure_terms": TERMS,
        "levels": levels,
        "full_H_over_I_separate": full_ratios,
        "headline": {
            "F5_variables": 18 ** 5,
            "rho0_lower": levels[4]["rho_lower"],
            "rho0_upper": levels[4]["rho_upper"],
            "min_path": levels[4]["min_path_outer_to_inner"],
            "strict_statement": "Every relevant coordinate of F5 has Delta_i H / Inf_i > 7.0960.",
        },
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="verification.json")
    args = parser.parse_args()
    report = main()
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(report["headline"], indent=2, sort_keys=True))
