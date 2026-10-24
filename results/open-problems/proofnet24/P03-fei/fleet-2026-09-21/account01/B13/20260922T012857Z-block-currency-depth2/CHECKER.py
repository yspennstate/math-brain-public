"""Exact/rigorous B13 check for the Numaro n=18 FEI seed.

Reconstructs the published truth table from the ten source slices already
recorded in the FEI repository, verifies its source digest, proves the exact
Poincare block-currency identities numerically from integer Walsh data, and
uses rational log enclosures to certify the one- and two-step entropy ratios.

This is a checker for a structured obstruction, not a proof of full FEI.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
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
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
PIVOTS = [0, 3, 8, 4, 1, 7, 5, 2, 6]
TERMS = 80


def fwht(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        v = a.reshape(-1, 2 * h)
        x = v[:, :h].copy()
        y = v[:, h:].copy()
        v[:, :h] = x + y
        v[:, h:] = x - y
        h *= 2
    return a


def reconstruct() -> tuple[np.ndarray, list[list[int]]]:
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    if any((m & base) or m.bit_count() != 2 for m in masks):
        raise AssertionError("source-slice host reconstruction failed")
    hosts = [[x for x in range(512) if (m >> x) & 1] for m in masks]
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int8)
    table = np.tile(core, (1 << 9, 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << 9) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    return table.ravel(), hosts


def restrict(table: np.ndarray, conditions: tuple[tuple[int, int], ...]) -> np.ndarray:
    idx = np.arange(len(table), dtype=np.int64)
    keep = np.ones(len(table), dtype=bool)
    for coord, bit in conditions:
        keep &= ((idx >> coord) & 1) == bit
    return table[keep]


def influence(table: np.ndarray, coord: int) -> F:
    idx = np.arange(len(table), dtype=np.int64)
    lo = idx[((idx >> coord) & 1) == 0]
    changes = int(np.count_nonzero(table[lo] != table[lo | (1 << coord)]))
    return F(changes, len(lo))


def p_currency(table: np.ndarray) -> F:
    W = fwht(table)
    norm = len(table) ** 2
    I_num = sum(int(W[s]) ** 2 * s.bit_count() for s in range(len(W)))
    I = F(I_num, norm)
    minus = int(np.count_nonzero(table == -1))
    p = F(minus, len(table))
    return I / 4 - p * (1 - p)


def log_unit_interval(x: F, terms: int = TERMS) -> tuple[F, F]:
    if not (1 <= x <= 2):
        raise ValueError("range reduction failure")
    if x == 1:
        return F(0), F(0)
    z = (x - 1) / (x + 1)
    z2 = z * z
    power = z
    s = F(0)
    for k in range(terms):
        s += power / (2 * k + 1)
        power *= z2
    lower = 2 * s
    rem = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lower, lower + rem


@lru_cache(maxsize=None)
def log2_interval(x: F, terms: int = TERMS) -> tuple[F, F]:
    if x <= 0:
        raise ValueError("log input must be positive")
    if x < 1:
        lo, hi = log2_interval(1 / x, terms)
        return -hi, -lo
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2) ** e:
        e -= 1
    m = x / (F(2) ** e)
    a, b = log_unit_interval(m, terms)
    c, d = log_unit_interval(F(2), terms)
    return F(e) + a / d, F(e) + b / c


def entropy_interval(table: np.ndarray) -> tuple[F, F]:
    W = fwht(table)
    norm = len(table) ** 2
    lo = F(0)
    hi = F(0)
    for square, multiplicity in Counter(int(x) ** 2 for x in W).items():
        if square == 0:
            continue
        l, u = log2_interval(F(norm, square))
        mass = F(multiplicity * square, norm)
        lo += mass * l
        hi += mass * u
    return lo, hi


def decimal_out(x: F, digits: int = 18, upper: bool = False) -> str:
    scale = 10 ** digits
    a = x.numerator * scale
    b = x.denominator
    q = -((-a) // b) if upper else a // b
    sign = "-" if q < 0 else ""
    q = abs(q)
    return f"{sign}{q // scale}.{q % scale:0{digits}d}"


def main() -> None:
    table, hosts = reconstruct()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert int(table.sum()) == 0

    W = fwht(table)
    norm = len(table) ** 2
    I = F(sum(int(W[s]) ** 2 * s.bit_count() for s in range(len(W))), norm)
    assert I == F(261, 128)
    P = p_currency(table)
    assert P == F(133, 512)

    expected_hosts = [[78,79], [113,121], [228,484], [170,186], [149,151],
                      [338,466], [284,316], [291,295], [393,457]]
    assert hosts == expected_hosts
    pair_walsh = []
    for j, pivot in enumerate(PIVOTS):
        aux = 9 + j
        coeff = int(W[(1 << aux) | (1 << pivot)])
        pair_walsh.append(coeff)
        assert coeff == 0

    Hlo, Hhi = entropy_interval(table)
    first = {}
    for i in range(18):
        child_H = [entropy_interval(restrict(table, ((i, b),))) for b in (0, 1)]
        child_P = [p_currency(restrict(table, ((i, b),))) for b in (0, 1)]
        Llo = Hlo - sum(x[1] for x in child_H) / 2
        Lhi = Hhi - sum(x[0] for x in child_H) / 2
        Q = P - sum(child_P) / 2
        inf = influence(table, i)
        assert Q == inf * (1 - inf) / 4
        first[i] = (inf, Llo, Lhi, Q)

    core = first[0]
    aux = first[9]
    assert all(first[i][0] == F(57, 256) and first[i][3] == F(11343, 262144)
               for i in range(9))
    assert all(first[i][0] == F(1, 256) and first[i][3] == F(255, 262144)
               for i in range(9, 18))

    core_rho = (core[1] / (4 * core[3]), core[2] / (4 * core[3]))
    aux_rho = (aux[1] / (4 * aux[3]), aux[2] / (4 * aux[3]))

    pairs = []
    for j, pivot in enumerate(PIVOTS):
        auxcoord = 9 + j
        child_H = []
        child_P = []
        for ba in (0, 1):
            for bp in (0, 1):
                t = restrict(table, ((auxcoord, ba), (pivot, bp)))
                child_H.append(entropy_interval(t))
                child_P.append(p_currency(t))
        Llo = Hlo - sum(x[1] for x in child_H) / 4
        Lhi = Hhi - sum(x[0] for x in child_H) / 4
        Qblock = P - sum(child_P) / 4
        assert Qblock == F(5799, 131072)
        assert Qblock == first[auxcoord][3] + first[pivot][3]
        rho = (Llo / (4 * Qblock), Lhi / (4 * Qblock))
        assert rho[1] < F(2959, 500)
        pairs.append({
            "aux": auxcoord,
            "pivot": pivot,
            "Q_exact": str(Qblock),
            "rho_lower": decimal_out(rho[0]),
            "rho_upper": decimal_out(rho[1], upper=True),
        })

    out = {
        "status": "PASS",
        "source_table_sha256": digest,
        "I_exact": str(I),
        "P_exact": str(P),
        "pair_walsh_coefficients_all_zero": pair_walsh,
        "core_first_step": {
            "influence": str(core[0]), "Q_exact": str(core[3]),
            "rho_lower": decimal_out(core_rho[0]),
            "rho_upper": decimal_out(core_rho[1], upper=True),
        },
        "aux_first_step": {
            "influence": str(aux[0]), "Q_exact": str(aux[3]),
            "rho_lower": decimal_out(aux_rho[0]),
            "rho_upper": decimal_out(aux_rho[1], upper=True),
        },
        "host_pivot_blocks": pairs,
        "certified_common_host_pivot_upper": "5.918",
        "log_series_terms": TERMS,
        "meaning": (
            "For this balanced monotone n=18 source, every expensive auxiliary "
            "coordinate has a natural host-pivot two-coordinate block whose "
            "zero-reference FEI-unit block ratio is rigorously below 5.918. "
            "This is not a universal FEI proof and does not test the certified "
            "read-once reference potential."
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
