#!/usr/bin/env python3
"""Exact certificates for C036's multiphase diamond constructions.

Python standard library only.  The Gaussian rational arithmetic follows the
transparent implementation in C035; all composition, examples, covariances,
and obstruction checks here are independent C036 calculations.  No LP occurs.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def lift(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, x):
        x = G.lift(x)
        return G(self.re + x.re, self.im + x.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, x):
        return self + -G.lift(x)

    def __rsub__(self, x):
        return G.lift(x) + -self

    def __mul__(self, x):
        x = G.lift(x)
        return G(self.re*x.re - self.im*x.im,
                 self.re*x.im + self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = G.lift(x)
        z = self*x.conj()
        return G(z.re/x.norm(), z.im/x.norm())

    def conj(self):
        return G(self.re, -self.im)

    def norm(self):
        return self.re*self.re + self.im*self.im

    def __bool__(self):
        return bool(self.re or self.im)


def det(matrix):
    a = [[G.lift(x) for x in row] for row in matrix]
    out = G(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return G()
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            out = -out
        p = a[k][k]
        out *= p
        for i in range(k+1, len(a)):
            if not a[i][k]:
                continue
            scale = a[i][k]/p
            for j in range(k+1, len(a)):
                a[i][j] -= scale*a[k][j]
    return out


def minor(q, rows, cols):
    return det([[q[i][j] for j in cols] for i in rows])


def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), G())
             for j in range(len(b[0]))] for i in range(len(a))]


def phase_factor(z, omega):
    z = list(map(G.lift, z))
    omega = G.lift(omega)
    norm = sum(x.norm() for x in z)
    assert norm > 0 and omega.norm() == 1
    q = [[G(int(i == j))+(omega-1)*z[i]*z[j].conj()/norm
          for j in range(len(z))] for i in range(len(z))]
    return {"q": q, "s": [x.norm()/norm for x in z],
            "gamma": (omega-1).norm(), "omega": omega, "z": z}


def check_unitary(q):
    n = len(q)
    for i in range(n):
        for j in range(n):
            assert sum((q[k][i].conj()*q[k][j]
                        for k in range(n)), G()) == G(int(i == j))


def subset_levels(n):
    return [list(combinations(range(n), k)) for k in range(n+1)]


def swapped(s, i, j):
    return tuple(sorted(j if a == i else i if a == j else a for a in s))


def phase_channel(factor, t):
    s, gamma = factor["s"], factor["gamma"]
    mass = sum((s[i] for i in t), F(0))
    out = {t: 1-gamma*mass*(1-mass)}
    for i in t:
        for j in range(len(s)):
            if j not in t:
                out[swapped(t, i, j)] = gamma*s[i]*s[j]
    return {u: p for u, p in out.items() if p}


def composition_channel(factors, t):
    out = {t: F(1)}
    for factor in factors:
        nxt = {}
        for u, w in out.items():
            for v, p in phase_channel(factor, u).items():
                nxt[v] = nxt.get(v, F(0)) + w*p
        out = nxt
    return out


def verify_all_minors(q, factors):
    levels = subset_levels(len(q))
    table = {}
    count = 0
    for level in levels:
        for t in level:
            classical = composition_channel(factors, t)
            column = {}
            for s in level:
                value = minor(q, s, t).norm()
                assert value == classical.get(s, F(0)), (s, t, value)
                column[s] = value
                count += 1
            assert sum(column.values()) == 1
            table[t] = column
    return table, count


def add_weight(table, bottom, top, weight):
    key = (tuple(sorted(bottom)), tuple(sorted(top)))
    table[key] = table.get(key, F(0)) + weight


def local_diamonds(factor, bottom, top):
    """C035's formula, generalized here to an arbitrary coordinate diamond."""
    s, gamma = factor["s"], factor["gamma"]
    r = tuple(sorted(bottom))
    h = tuple(sorted(top))
    p = tuple(sorted(set(h)-set(r)))
    c = tuple(i for i in range(len(s)) if i not in h)
    assert set(r) < set(h) and len(p) == 2
    alpha = sum((s[i] for i in r), F(0))
    beta = sum((s[i] for i in p), F(0))
    chi = sum((s[i] for i in c), F(0))
    central = 1-gamma*(alpha*beta+alpha*chi+beta*chi)
    tau = max(F(0), -central)
    table = {(r, h): central}
    for left, right in ((r, p), (r, c), (p, c)):
        for a in left:
            for b in right:
                add_weight(table, swapped(r, a, b), swapped(h, a, b),
                           gamma*s[a]*s[b])
    if tau:
        assert alpha*beta*chi > 0
        assert tau <= gamma*min(alpha*beta, alpha*chi, beta*chi)
        for a in r:
            for k in p:
                for b in c:
                    w = tau*s[a]*s[k]*s[b]/(alpha*beta*chi)
                    add_weight(table, r, h, w)
                    add_weight(table, swapped(r, a, b), swapped(h, k, b), w)
                    add_weight(table, swapped(r, a, k), swapped(h, a, b), w)
                    add_weight(table, swapped(r, a, b), swapped(h, a, b), -w)
                    add_weight(table, swapped(r, a, k), h, -w)
                    add_weight(table, r, swapped(h, k, b), -w)
    assert all(w >= 0 for w in table.values())
    assert sum(table.values()) == 1
    return {d: w for d, w in table.items() if w}, tau


def compose_diamonds(factors, bottom, top):
    table = {(bottom, top): F(1)}
    stages = []
    for factor in factors:
        nxt = {}
        repaired = 0
        for (r, h), w in table.items():
            kernel, tau = local_diamonds(factor, r, h)
            repaired += int(bool(tau))
            for (a, b), p in kernel.items():
                add_weight(nxt, a, b, w*p)
        table = nxt
        assert sum(table.values()) == 1
        stages.append({"positive_atoms": len(table),
                       "input_diamonds_requiring_repair": repaired})
    return table, stages


def diamond_marginals(table, n, r):
    levels = subset_levels(n)
    bottom = dict.fromkeys(levels[r], F(0))
    top = dict.fromkeys(levels[r+2], F(0))
    middle = dict.fromkeys(levels[r+1], F(0))
    added = dict.fromkeys(levels[2], F(0))
    for (a, b), p in table.items():
        assert p > 0 and set(a) < set(b) and len(b)-len(a) == 2
        delta = tuple(sorted(set(b)-set(a)))
        bottom[a] += p
        top[b] += p
        added[delta] += p
        for i in delta:
            middle[tuple(sorted(a+(i,)))] += p
    return bottom, middle, top, added


def verify_diamonds(q, all_laws, factors, r, p):
    top = tuple(sorted(r+p))
    table, stages = compose_diamonds(factors, r, top)
    bottom, middle, upper, added = diamond_marginals(table, len(q), len(r))
    u, v = (tuple(sorted(r+(i,))) for i in p)
    assert bottom == all_laws[r]
    assert upper == all_laws[top]
    assert added == all_laws[tuple(sorted(p))]
    assert all(middle[x] == all_laws[u][x]+all_laws[v][x] for x in middle)
    return table, stages


def permutation_weights(factor):
    """C034's identity / transposition / oriented-three-cycle probabilities."""
    s, gamma = factor["s"], factor["gamma"]
    n = len(s)
    identity = tuple(range(n))
    table = {identity: 1-gamma*(1-sum(x**3 for x in s))/3}
    assert table[identity] >= 0
    for i, j in combinations(range(n), 2):
        pi = list(identity)
        pi[i], pi[j] = j, i
        table[tuple(pi)] = gamma*s[i]*s[j]*(s[i]+s[j])
    for i, j, k in combinations(range(n), 3):
        for a, b, c in ((i, j, k), (i, k, j)):
            pi = list(identity)
            pi[a], pi[b], pi[c] = b, c, a
            table[tuple(pi)] = gamma*s[i]*s[j]*s[k]
    assert all(w >= 0 for w in table.values())
    assert sum(table.values()) == 1
    return {pi: w for pi, w in table.items() if w}


def compose_permutations(factors):
    table = {tuple(range(len(factors[0]["s"]))): F(1)}
    for factor in factors:
        nxt = {}
        for pi, w in table.items():
            for sigma, p in permutation_weights(factor).items():
                product = tuple(sigma[pi[i]] for i in range(len(pi)))
                nxt[product] = nxt.get(product, F(0)) + w*p
        table = nxt
    assert sum(table.values()) == 1
    return table


def permute(pi, a):
    return tuple(sorted(pi[i] for i in a))


def verify_permutations(table, laws):
    for t, law in laws.items():
        result = dict.fromkeys(law, F(0))
        for pi, w in table.items():
            result[permute(pi, t)] += w
        assert result == law


def labeled_diamonds(permutations, r, p):
    table = {}
    for pi, w in permutations.items():
        key = (permute(pi, r), pi[p[0]], pi[p[1]])
        table[key] = table.get(key, F(0)) + w
    return table


def verify_labeled(table, laws, r, p):
    target = [r, tuple(sorted(r+(p[0],))), tuple(sorted(r+(p[1],))),
              tuple(sorted(r+p))]
    marg = [dict.fromkeys(laws[t], F(0)) for t in target]
    for (a, i, j), w in table.items():
        assert i != j and i not in a and j not in a
        vertices = [a, tuple(sorted(a+(i,))), tuple(sorted(a+(j,))),
                    tuple(sorted(a+(i, j)))]
        for b, v in zip(marg, vertices):
            b[v] += w
    assert all(m == laws[t] for m, t in zip(marg, target))


def projection(q, columns):
    return [[sum((q[i][a]*q[j][a].conj() for a in columns), G())
             for j in range(len(q))] for i in range(len(q))]


def matrix_rank(a):
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(r+1, len(a)):
            if not a[i][j]:
                continue
            scale = a[i][j]/a[r][j]
            for k in range(j, len(a[0])):
                a[i][k] -= scale*a[r][k]
        r += 1
        if r == len(a):
            break
    return r


def encode(x):
    if isinstance(x, G):
        return {"real": str(x.re), "imaginary": str(x.im)}
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def law_records(laws, selected):
    return [{"columns": list(t), "law": [
        {"set": list(a), "weight": str(w)} for a, w in laws[t].items()]}
        for t in selected]


def save_case(name, factors, r, p, triangle, with_permutations=False):
    q = factors[0]["q"]
    for factor in factors[1:]:
        q = matmul(factor["q"], q)
    for factor in factors:
        check_unitary(factor["q"])
    check_unitary(q)
    laws, count = verify_all_minors(q, factors)
    table, stages = verify_diamonds(q, laws, factors, r, p)
    kernel = projection(q, r)
    a, b, c = triangle
    invariant = kernel[a][b]*kernel[b][c]*kernel[c][a]
    assert invariant.im
    rank = matrix_rank([[q[i][j]-int(i == j) for j in range(len(q))]
                        for i in range(len(q))])
    assert rank == len(factors)
    records = {
        "name": name, "factors": factors, "Q": q,
        "rank_Q_minus_I": rank, "bottom_columns": r, "pivot_columns": p,
        "projection": kernel, "triangle": triangle, "triangle_product": invariant,
        "all_offdiagonal_projection_entries_nonzero": all(
            bool(kernel[i][j]) for i in range(len(q)) for j in range(i)),
        "unitary_minor_identities_checked": count, "stages": stages,
        "unlabeled_diamonds": [{"bottom": a, "top": b, "weight": w}
                                for (a, b), w in sorted(table.items())],
        "selected_laws": law_records(laws, [r, tuple(sorted(r+(p[0],))),
            tuple(sorted(r+(p[1],))), tuple(sorted(r+p)), tuple(sorted(p))]),
    }
    summary = {"name": name, "status": "PASS", "minor_identities": count,
               "unlabeled_atoms": len(table), "stages": stages,
               "rank_Q_minus_I": rank, "triangle_product": invariant}
    if with_permutations:
        perms = compose_permutations(factors)
        verify_permutations(perms, laws)
        labeled = labeled_diamonds(perms, r, p)
        verify_labeled(labeled, laws, r, p)
        records["permutations"] = [
            {"permutation": pi, "weight": w} for pi, w in sorted(perms.items())]
        records["labeled_diamonds"] = [
            {"bottom": a, "first_added": i, "second_added": j, "weight": w}
            for (a, i, j), w in sorted(labeled.items())]
        summary.update({"common_permutations": len(perms), "labeled_atoms": len(labeled)})
    (OUT/(name+"_certificate.json")).write_text(json.dumps(encode(records), indent=2)+"\n")
    return summary, q, laws


def obstruction_case(name, f1, f2, source, target):
    q = matmul(f2["q"], f1["q"])
    physical = minor(q, target, source).norm()
    paths = []
    for mid in combinations(range(len(q)), len(source)):
        value = minor(f2["q"], target, mid)*minor(f1["q"], mid, source)
        if value:
            paths.append({"intermediate": mid, "amplitude": value})
    coherent = sum((x["amplitude"] for x in paths), G()).norm()
    classical = sum(x["amplitude"].norm() for x in paths)
    assert coherent == physical and classical != physical
    return {"name": name, "source": source, "target": target,
            "factors": [f1, f2], "paths": paths, "physical_probability": physical,
            "classical_composition": classical, "difference": physical-classical}


OUT = Path(__file__).resolve().parent


def main():
    i = G(0, 1)
    f1 = phase_factor([1, 1, 1, 0, 0, 0], i)
    f2 = phase_factor([0, 0, 1, 1, 1, 1], G(F(3, 5), F(4, 5)))
    tree, q, laws = save_case("complex_six_tree", [f1, f2], (0, 3), (1, 4),
                              (0, 2, 3), True)
    delta = [[q[a][b]-int(a == b) for b in range(6)] for a in range(6)]
    assert minor(delta, (0, 3), (0, 3)) == G(F(-1, 30), F(-1, 10))
    assert tree["triangle_product"] == G(F(-101, 29160), F(-1, 405))
    print(json.dumps(encode(tree)), flush=True)

    # Independent coordinate phase changes and conjugation of either omega
    # preserve the complete occupation channel in the overlap-one family.
    v1 = phase_factor([1, i, -1, 0, 0, 0], -i)
    v2 = phase_factor([0, 0, i, 1, -i, -1], G(F(3, 5), F(-4, 5)))
    q_variant = matmul(v2["q"], v1["q"])
    variant_laws, covariance_count = verify_all_minors(q_variant, [f1, f2])
    assert variant_laws == laws

    g1 = phase_factor([1, 1, 1, 1, 1, 0, 0, 0], -1)
    g2 = phase_factor([0, 0, 0, 1, i, 1, 1, 1], -1)
    overlap, q_overlap, overlap_laws = save_case(
        "quadrature_eight_reflections", [g1, g2], (0, 3, 5), (1, 6), (0, 1, 3))
    assert overlap["triangle_product"] == G(F(-304, 390625), F(-48, 15625))
    assert overlap["stages"][0]["input_diamonds_requiring_repair"] == 1
    assert overlap["stages"][1]["input_diamonds_requiring_repair"] > 0
    print(json.dumps(encode(overlap)), flush=True)

    obstructions = [
        obstruction_case("overlap_two_real_vectors_nonreal_phases",
            phase_factor([1, 1, 1, 0], i), phase_factor([0, 1, 1, 1], i),
            (0,), (3,)),
        obstruction_case("quadrature_is_insufficient_for_nonreal_phases",
            phase_factor([1, 1, 1, 0], i), phase_factor([0, 1, i, 1], i),
            (0,), (1,)),
        obstruction_case("overlap_three_two_path_minor",
            phase_factor([1, 1, 1, 1, 0], -1),
            phase_factor([0, 1, 1, 1, 1], -1), (0, 3), (3, 4)),
    ]
    assert [(x["physical_probability"], x["classical_composition"])
            for x in obstructions] == [(F(16, 81), F(8, 81)),
                (F(26, 81), F(14, 81)), (F(1, 4), F(1, 8))]
    (OUT/"composition_obstructions.json").write_text(
        json.dumps(encode(obstructions), indent=2)+"\n")
    result = {"status": "PASS", "examples": [tree, overlap],
              "phase_covariance_minor_identities": covariance_count,
              "exact_obstructions": len(obstructions),
              "total_product_minor_identities": tree["minor_identities"]+
                  overlap["minor_identities"]+covariance_count}
    (OUT/"verified_output.json").write_text(json.dumps(encode(result), indent=2)+"\n")
    print(json.dumps(encode(result), indent=2), flush=True)


if __name__ == "__main__":
    main()
