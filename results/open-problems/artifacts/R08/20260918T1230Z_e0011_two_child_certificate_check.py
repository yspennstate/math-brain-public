#!/usr/bin/env python3
"""Exact finite checker for R08 / E0011 two-child catalyst certificate core.

This checker validates the finite local primitives used in the accompanying
immutable R08 report:

1. a boundary-uniform 2x2 -> 2x3 vacancy expander;
2. a boundary-uniform eraser for the canonical two-species 2x2 seed;
3. a three-mark planter for that seed inside an all-vacant 4x4 box;
4. macro mark counts and protected-clock geometry for child spacing L=10.

State values: 0=vacant, 1=CO, 2=O.  Instantaneous reactions are resolved by
one fixed legal tie outcome: E,W,N,S priority for the newly adsorbed particle;
for O2 the first endpoint is processed before the second.  The report accounts
separately for the positive probability of these tie outcomes.
"""

from fractions import Fraction
from itertools import product

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def patch_for(active):
    cells = set(active)
    for x, y in tuple(active):
        for dx, dy in DIRS:
            cells.add((x + dx, y + dy))
    cells = tuple(sorted(cells))
    idx = {c: i for i, c in enumerate(cells)}
    return cells, idx


def stable(s, cells, idx):
    for x, y in cells:
        a = s[idx[(x, y)]]
        for dx, dy in ((1, 0), (0, 1)):
            q = (x + dx, y + dy)
            if q in idx:
                b = s[idx[q]]
                if (a == 1 and b == 2) or (a == 2 and b == 1):
                    return False
    return True


def co_action(s, c, idx):
    s = list(s)
    i = idx[c]
    if s[i] != 0:
        return tuple(s)
    s[i] = 1
    x, y = c
    for dx, dy in DIRS:
        q = (x + dx, y + dy)
        if q in idx and s[idx[q]] == 2:
            s[i] = 0
            s[idx[q]] = 0
            break
    return tuple(s)


def o2_action(s, a, b, idx):
    s = list(s)
    ia, ib = idx[a], idx[b]
    if s[ia] != 0 or s[ib] != 0:
        return tuple(s)
    s[ia] = 2
    s[ib] = 2
    for c in (a, b):
        i = idx[c]
        if s[i] != 2:
            continue
        x, y = c
        for dx, dy in DIRS:
            q = (x + dx, y + dy)
            if q in idx and s[idx[q]] == 1:
                s[i] = 0
                s[idx[q]] = 0
                break
    return tuple(s)


def apply_word(s, word, idx):
    for kind, arg in word:
        if kind == "CO":
            s = co_action(s, arg, idx)
        elif kind == "O2":
            s = o2_action(s, *arg, idx)
        else:
            raise ValueError(kind)
    return s


# ---------------------------------------------------------------------------
# 1. Boundary-uniform 2x2 -> 2x3 vacancy expander.
# ---------------------------------------------------------------------------
EXP_ACTIVE = {(x, y) for x in (-1, 0, 1) for y in (0, 1)}
EXP_CELLS, EXP_IDX = patch_for(EXP_ACTIVE)
EXP_FIXED_VACANT = {(-1, 0), (-1, 1), (0, 0), (0, 1)}
EXP_VARIABLE = tuple(c for c in EXP_CELLS if c not in EXP_FIXED_VACANT)
EXP_WORD = (
    ("CO", (0, 0)),
    ("O2", ((-1, 1), (0, 1))),
    ("CO", (0, 0)),
    ("CO", (0, 1)),
    ("CO", (0, 0)),
    ("CO", (0, 1)),
    ("CO", (1, 0)),
    ("CO", (0, 1)),
    ("CO", (0, 0)),
    ("O2", ((-1, 0), (-1, 1))),
    ("O2", ((0, 0), (0, 1))),
    ("CO", (1, 0)),
    ("CO", (0, 0)),
    ("CO", (0, 1)),
    ("CO", (0, 1)),
    ("CO", (1, 0)),
    ("CO", (0, 0)),
    ("O2", ((-1, 0), (-1, 1))),
    ("CO", (1, 0)),
    ("O2", ((0, 0), (0, 1))),
    ("CO", (-1, 1)),
)


def check_expander():
    assert len(EXP_CELLS) == 16
    assert len(EXP_VARIABLE) == 12
    total = 0
    stable_count = 0
    for vals in product((0, 1, 2), repeat=len(EXP_VARIABLE)):
        total += 1
        s = [0] * len(EXP_CELLS)
        for c, v in zip(EXP_VARIABLE, vals):
            s[EXP_IDX[c]] = v
        s = tuple(s)
        if not stable(s, EXP_CELLS, EXP_IDX):
            continue
        stable_count += 1
        t = apply_word(s, EXP_WORD, EXP_IDX)
        assert stable(t, EXP_CELLS, EXP_IDX)
        assert all(t[EXP_IDX[c]] == 0 for c in EXP_ACTIVE)
    assert total == 3 ** 12 == 531441
    assert stable_count == 50785
    return stable_count


# ---------------------------------------------------------------------------
# 2. Boundary-uniform eraser for the canonical two-species seed.
# Canonical active 2x2 seed:
#   O 0
#   0 C
# in coordinates (-1,1)=O, (0,0)=CO.
# ---------------------------------------------------------------------------
ERASE_ACTIVE = {(x, y) for x in (-1, 0) for y in (0, 1)}
ERASE_CELLS, ERASE_IDX = patch_for(ERASE_ACTIVE)
ERASE_FIXED = {(-1, 1): 2, (0, 0): 1, (-1, 0): 0, (0, 1): 0}
ERASE_VARIABLE = tuple(c for c in ERASE_CELLS if c not in ERASE_FIXED)
ERASE_WORD = (
    ("CO", (0, 1)),
    ("O2", ((-1, 0), (-1, 1))),
    ("CO", (0, 1)),
    ("CO", (0, 0)),
    ("O2", ((-1, 0), (-1, 1))),
    ("CO", (0, 1)),
)


def check_eraser():
    assert len(ERASE_CELLS) == 12
    total = 0
    stable_count = 0
    for vals in product((0, 1, 2), repeat=len(ERASE_VARIABLE)):
        total += 1
        s = [0] * len(ERASE_CELLS)
        for c, v in ERASE_FIXED.items():
            s[ERASE_IDX[c]] = v
        for c, v in zip(ERASE_VARIABLE, vals):
            s[ERASE_IDX[c]] = v
        s = tuple(s)
        if not stable(s, ERASE_CELLS, ERASE_IDX):
            continue
        stable_count += 1
        t = apply_word(s, ERASE_WORD, ERASE_IDX)
        assert stable(t, ERASE_CELLS, ERASE_IDX)
        assert all(t[ERASE_IDX[c]] == 0 for c in ERASE_ACTIVE)
    assert stable_count == 625
    return stable_count


# ---------------------------------------------------------------------------
# 3. Three-mark planter in an all-vacant 4x4 box.
# ---------------------------------------------------------------------------
PLANT_BOX = {(x, y) for x in range(4) for y in range(4)}
PLANT_CELLS, PLANT_IDX = patch_for(PLANT_BOX)
PLANT_WORD = (
    ("O2", ((1, 1), (1, 2))),
    ("CO", (2, 1)),
    ("CO", (2, 1)),
)
PLANT_TARGET_O = (1, 2)
PLANT_TARGET_CO = (2, 1)


def check_planter():
    s = tuple(0 for _ in PLANT_CELLS)
    t = apply_word(s, PLANT_WORD, PLANT_IDX)
    assert stable(t, PLANT_CELLS, PLANT_IDX)
    assert t[PLANT_IDX[PLANT_TARGET_O]] == 2
    assert t[PLANT_IDX[PLANT_TARGET_CO]] == 1
    for c in PLANT_BOX - {PLANT_TARGET_O, PLANT_TARGET_CO}:
        assert t[PLANT_IDX[c]] == 0


# ---------------------------------------------------------------------------
# 4. Macro counts and protected-clock geometry for child spacing L=10.
# ---------------------------------------------------------------------------
L = 10
# Erase once, then for each of L newly opened columns apply the 21-mark
# expander independently on the two row-pairs, then plant both children.
MACRO_MARKS = len(ERASE_WORD) + 2 * L * len(EXP_WORD) + 2 * len(PLANT_WORD)
MACRO_CO = (
    sum(1 for k, _ in ERASE_WORD if k == "CO")
    + 2 * L * sum(1 for k, _ in EXP_WORD if k == "CO")
    + 2 * sum(1 for k, _ in PLANT_WORD if k == "CO")
)
MACRO_O2 = MACRO_MARKS - MACRO_CO

# Conservative protected box B_i=[10i-2,10i+15] x [-2,5], width 18, height 8.
PROTECTED_W = 18
PROTECTED_H = 8
PROTECTED_SITES = PROTECTED_W * PROTECTED_H
INTERNAL_EDGES = (PROTECTED_W - 1) * PROTECTED_H + PROTECTED_W * (PROTECTED_H - 1)
CROSSING_EDGES = 2 * PROTECTED_H + 2 * PROTECTED_W
PROTECTED_EDGES = INTERNAL_EDGES + CROSSING_EDGES
TOTAL_RATE = Fraction(PROTECTED_SITES, 2) + Fraction(PROTECTED_EDGES, 4)


def incident_edge_set(x0):
    sites = {(x, y) for x in range(x0 - 2, x0 + 16) for y in range(-2, 6)}
    edges = set()
    for x, y in sites:
        for dx, dy in DIRS:
            q = (x + dx, y + dy)
            e = tuple(sorted(((x, y), q)))
            edges.add(e)
    return sites, edges


def main():
    exp_count = check_expander()
    erase_count = check_eraser()
    check_planter()

    assert len(EXP_WORD) == 21
    assert sum(1 for k, _ in EXP_WORD if k == "CO") == 16
    assert sum(1 for k, _ in EXP_WORD if k == "O2") == 5
    assert len(ERASE_WORD) == 6
    assert sum(1 for k, _ in ERASE_WORD if k == "CO") == 4
    assert sum(1 for k, _ in ERASE_WORD if k == "O2") == 2
    assert len(PLANT_WORD) == 3
    assert sum(1 for k, _ in PLANT_WORD if k == "CO") == 2
    assert sum(1 for k, _ in PLANT_WORD if k == "O2") == 1

    assert MACRO_MARKS == 432
    assert MACRO_CO == 328
    assert MACRO_O2 == 104
    assert PROTECTED_SITES == 144
    assert PROTECTED_EDGES == 314
    assert TOTAL_RATE == Fraction(301, 2)

    s0, e0 = incident_edge_set(0)
    s2, e2 = incident_edge_set(2 * L)
    assert s0.isdisjoint(s2)
    assert e0.isdisjoint(e2)

    # A fully rational strict lower bound used in the report.  It is not
    # evaluated as a floating point number here; positivity is exact.
    denominator = (3 ** 432) * (1204 ** 328) * (19264 ** 104)
    assert denominator > 0

    print("PASS exact R08/E0011 two-child certificate core")
    print(f"expander_stable_environments={exp_count}")
    print(f"eraser_stable_environments={erase_count}")
    print(f"expander_word_length={len(EXP_WORD)}")
    print(f"eraser_word_length={len(ERASE_WORD)}")
    print(f"planter_word_length={len(PLANT_WORD)}")
    print(f"L={L}")
    print(f"macro_marks={MACRO_MARKS} CO={MACRO_CO} O2={MACRO_O2}")
    print(f"protected_sites={PROTECTED_SITES} protected_edges={PROTECTED_EDGES}")
    print(f"protected_total_rate={TOTAL_RATE}")
    print("blocks_i_and_i_plus_2_have_disjoint_protected_clock_sets=True")
    print("b0_exact=1/(3^432 * 1204^328 * 19264^104)")
    print("b0_positive=True")


if __name__ == "__main__":
    main()
