#!/usr/bin/env python3
"""Exact certificates for C037's universal bilinear Pluecker-SOS obstruction.

Only the Python standard library is used. All frames and Pluecker values are
rational. A phase projection is a finite Fourier average over coordinate
phases in {1,i,-1,-i}; its coefficient vector is computed symbolically.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent
E = tuple(range(6))
PAIRS = tuple(combinations(E, 2))
FEATURES = tuple(product(PAIRS, repeat=2))
INDEX = {cd: k for k, cd in enumerate(FEATURES)}
A = (0, 1)
B = (2, 3)
C, S = F(3, 5), F(4, 5)


def vec(*terms):
    out = [F(0)] * 6
    for i, value in terms:
        out[i] += value
    return out


def unit(i):
    return vec((i, F(1)))


def validate(w, z):
    cols = w + z
    for i in range(4):
        for j in range(4):
            assert sum(x * y for x, y in zip(cols[i], cols[j])) == int(i == j)


def pluecker(w):
    return {ij: w[0][ij[0]] * w[1][ij[1]] - w[0][ij[1]] * w[1][ij[0]]
            for ij in PAIRS}


def weight(cd, mode):
    c, d = cd
    return tuple(int(i in c) + (1 if mode == "holomorphic" else -1) * int(i in d)
                 for i in E)


def phase_vector(w, z, tag, mode):
    p, q = pluecker(w), pluecker(z)
    # All base frames are real; conjugation changes the phase tag only.
    return {k: p[c] * q[d] for k, (c, d) in enumerate(FEATURES)
            if weight((c, d), mode) == tag and p[c] * q[d]}


def serial_vector(v):
    return [[k, str(value)] for k, value in sorted(v.items())]


def frame_record(w, z, tag, mode, base):
    validate(w, z)
    assert pluecker(w)[base] == 0
    v = phase_vector(w, z, tag, mode)
    assert v
    return {
        "zero_bottom": list(base), "mode": mode, "phase_tag": list(tag),
        "W_columns": [[str(x) for x in col] for col in w],
        "Z_columns": [[str(x) for x in col] for col in z],
        "projected_evaluation": serial_vector(v),
    }, v


def holomorphic_isolators(base):
    records = []
    for c, d in FEATURES:
        if c == base:
            continue
        overlap = set(c) & set(d)
        if not overlap:
            w, z = [unit(i) for i in c], [unit(i) for i in d]
        elif len(overlap) == 1:
            i = next(iter(overlap))
            j = next(iter(set(c) - {i}))
            k = next(iter(set(d) - {i}))
            ell = next(v for v in E if v not in set(base) | set(c) | set(d))
            w = [vec((i, C), (ell, S)), unit(j)]
            z = [vec((i, S), (ell, -C)), unit(k)]
        else:
            i, j = c
            k, ell = [v for v in E if v not in set(base) | set(c)][:2]
            w = [vec((i, C), (k, S)), vec((j, C), (ell, S))]
            z = [vec((i, S), (k, -C)), vec((j, S), (ell, -C))]
        tag = weight((c, d), "holomorphic")
        rec, v = frame_record(w, z, tag, "holomorphic", base)
        assert set(v) == {INDEX[(c, d)]}
        rec["isolated_feature"] = [list(c), list(d)]
        records.append(rec)
    assert len(records) == 210
    return records


def sesquilinear_samples(base):
    records, vectors = [], []

    def add(w, z, tag, kind):
        rec, v = frame_record(w, z, tag, "sesquilinear", base)
        rec["kind"] = kind
        records.append(rec)
        vectors.append(v)

    # Unique phase sectors with disjoint endpoint pairs.
    for c, d in FEATURES:
        if c != base and not set(c) & set(d):
            add([unit(i) for i in c], [unit(i) for i in d],
                weight((c, d), "sesquilinear"), "disjoint")

    # Two-coordinate differences in each off-diagonal contraction sector.
    for i in E:
        for j in E:
            if i == j:
                continue
            allowed = [k for k in E if k not in (i, j) and tuple(sorted((i, k))) != base]
            for k, ell in combinations(allowed, 2):
                w = [unit(i), vec((k, C), (ell, S))]
                z = [unit(j), vec((k, S), (ell, -C))]
                tag = tuple(int(v == i) - int(v == j) for v in E)
                add(w, z, tag, "off_diagonal")

    # Alternating rectangles in the diagonal phase sector.
    for sites in combinations(E, 4):
        i, j, k, ell = sites
        for first, second in (((i, j), (k, ell)), ((i, k), (j, ell)), ((i, ell), (j, k))):
            x, y = first
            z0, t = second
            w = [vec((x, C), (y, S)), vec((z0, C), (t, S))]
            z = [vec((x, S), (y, -C)), vec((z0, S), (t, -C))]
            if pluecker(w)[base] == 0:
                add(w, z, (0,) * 6, "diagonal_rectangle")
    return records, vectors


def rank(rows):
    pivots = {}
    for original in rows:
        row = dict(original)
        while row:
            k = min(row)
            if k not in pivots:
                a = row[k]
                pivots[k] = {j: value / a for j, value in row.items()}
                break
            a = row[k]
            for j, value in pivots[k].items():
                row[j] = row.get(j, F(0)) - a * value
                if not row[j]:
                    del row[j]
    return len(pivots), pivots


def sector_ranks(rows):
    groups = defaultdict(list)
    for row in rows:
        tags = {weight(FEATURES[k], "sesquilinear") for k in row}
        assert len(tags) == 1
        groups[next(iter(tags))].append(row)
    ranks = {tag: rank(rs)[0] for tag, rs in groups.items()}
    return sum(ranks.values()), [
        {"phase_tag": list(tag), "rank": r}
        for tag, r in sorted(ranks.items())
    ]


def oriented_pair(i, j):
    assert i != j
    return (tuple(sorted((i, j))), 1 if i < j else -1)


def contractions():
    rows = []
    for i in E:
        for j in E:
            row = {}
            for k in E:
                if k == i or k == j:
                    continue
                c, cs = oriented_pair(i, k)
                d, ds = oriented_pair(j, k)
                row[INDEX[(c, d)]] = F(cs * ds)
            rows.append(row)
    return rows


def dot(a, b):
    return sum(value * b.get(k, F(0)) for k, value in a.items())


def swap_features(v):
    return {INDEX[(d, c)]: value for k, value in v.items() for c, d in [FEATURES[k]]}


def determinant(a):
    if not a:
        return F(1)
    a = [row[:] for row in a]
    result = F(1)
    for j in range(len(a)):
        pivot = next((k for k in range(j, len(a)) if a[k][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        t = a[j][j]
        result *= t
        for k in range(j + 1, len(a)):
            ratio = a[k][j] / t
            for ell in range(j + 1, len(a)):
                a[k][ell] -= ratio * a[j][ell]
    return result


def law(cols):
    r = len(cols)
    return {sites: determinant([[col[i] for col in cols] for i in sites]) ** 2
            for sites in combinations(E, r)}


def counterexample():
    w = [vec((0, C), (2, S)), unit(1)]
    z = [vec((0, S), (2, -C)), unit(3)]
    u, v = unit(4), unit(5)
    validate(w, z)
    frame = w + [u, v] + z
    for i, x in enumerate(frame):
        for j, y in enumerate(frame):
            assert sum(a * b for a, b in zip(x, y)) == int(i == j)
    a, c = law(w), law(z)
    m1, m2, top = law(w + [u]), law(w + [v]), law(w + [u, v])
    g = {m: m1[m] + m2[m] for m in m1}
    atoms = {(A, B): F(9, 25), ((1, 2), (0, 3)): F(16, 25)}
    for pair in PAIRS:
        assert sum(x for (aa, bb), x in atoms.items() if aa == pair) == a[pair]
        assert sum(x for (aa, bb), x in atoms.items() if bb == pair) == c[pair]
        assert c[pair] == top[tuple(i for i in E if i not in pair)]
    for middle in combinations(E, 3):
        total = sum(x for (aa, bb), x in atoms.items()
                    if set(aa) <= set(middle) and not set(bb) & set(middle))
        assert total == g[middle]
    product_atoms = {(aa, bb): a[aa] * c[bb] for aa, bb in FEATURES if not set(aa) & set(bb)}
    forced_row = sum(x for (aa, bb), x in product_atoms.items() if aa == A)
    assert forced_row == F(81, 625) != a[A] == F(9, 25)
    assert a[A] - forced_row == F(144, 625)
    assert sum(product_atoms.values()) == F(337, 625)
    return {
        "Q_columns": [[str(x) for x in col] for col in frame],
        "bottom": {"".join(map(str, k)): str(v) for k, v in a.items() if v},
        "complement_top": {"".join(map(str, k)): str(v) for k, v in c.items() if v},
        "aggregate_middle": {"".join(map(str, k)): str(v) for k, v in g.items() if v},
        "valid_diamond_weights": [[list(aa), list(bb), str(x)] for (aa, bb), x in atoms.items()],
        "forced_product_row": str(forced_row), "required_row": str(a[A]),
        "exact_row_deficit": str(a[A] - forced_row),
        "forced_product_total_mass": str(sum(product_atoms.values())),
    }


def main():
    hol = holomorphic_isolators(A)
    row_records, row_samples = sesquilinear_samples(A)
    col_records, col_pre = sesquilinear_samples(B)
    col_samples = [swap_features(v) for v in col_pre]
    rels = contractions()
    assert rank(rels)[0] == 36
    row_null = rels + [{INDEX[(A, d)]: F(1)} for d in PAIRS]
    assert rank(row_null)[0] == 51
    for sample in row_samples:
        assert all(dot(sample, r) == 0 for r in row_null)
    row_rank, row_sectors = sector_ranks(row_samples)
    assert row_rank == 174
    joint_null = rels + [{INDEX[(A, B)]: F(1)}]
    assert rank(joint_null)[0] == 37
    for sample in row_samples + col_samples:
        assert all(dot(sample, r) == 0 for r in joint_null)
    joint_rank, joint_sectors = sector_ranks(row_samples + col_samples)
    assert joint_rank == 188
    global_rank, _ = sector_ranks(row_samples + col_samples + [{INDEX[(A, B)]: F(1)}])
    assert global_rank == 189
    # Every contraction is the displayed exact expansion of W*Z = 0.
    for record in row_records + col_records:
        w = [[F(x) for x in col] for col in record["W_columns"]]
        z = [[F(x) for x in col] for col in record["Z_columns"]]
        p, q = pluecker(w), pluecker(z)
        full = {k: p[c] * q[d] for k, (c, d) in enumerate(FEATURES) if p[c] * q[d]}
        assert all(dot(full, r) == 0 for r in rels)
    bad = counterexample()
    certificate = {
        "feature_order": [[list(c), list(d)] for c, d in FEATURES],
        "rotation": {"c": str(C), "s": str(S)},
        "holomorphic_row_isolators": hol,
        "sesquilinear_row_zero_samples": row_records,
        "sesquilinear_column_zero_samples_before_swapping_W_Z": col_records,
        "contraction_relations": [serial_vector(r) for r in rels],
        "row_sector_ranks": row_sectors, "joint_sector_ranks": joint_sectors,
        "counterexample_to_forced_product_weights": bad,
    }
    out = {
        "status": "all exact checks passed",
        "arithmetic": "fractions; no numerical LP or SDP",
        "holomorphic_individually_isolated_nonrow_features": len(hol),
        "sesquilinear_row_zero_samples": len(row_samples),
        "sesquilinear_column_zero_samples": len(col_samples),
        "global_contraction_relation_rank": 36,
        "global_sesquilinear_feature_span_rank": global_rank,
        "row_zero_evaluation_rank": row_rank,
        "row_zero_annihilator_dimension": 225 - row_rank,
        "row_plus_column_zero_evaluation_rank": joint_rank,
        "row_plus_column_zero_annihilator_dimension": 225 - joint_rank,
        "allowed_atom_amplitude_dimension_modulo_global_relations": 1,
        "required_counterexample_row": bad["required_row"],
        "forced_counterexample_row": bad["forced_product_row"],
        "row_deficit": bad["exact_row_deficit"],
        "counterexample_has_an_exact_two_atom_full_diamond_coupling": True,
    }
    (ROOT / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    (ROOT / "verified_output.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
