#!/usr/bin/env python3
"""Exact certificate for a RESTRICTED Sidorenko theorem, not the full conjecture.

H = K_{5,5} minus C_10; hosts are symmetric nonnegative 3x3 matrices
with row sums 3, with UNIFORM vertex weights. Standard library only.
No floating-point decisions, random tests, network access, or input certificates.
Run: python3 verify.py --output results.json
The full polynomial and all 12,288 control coefficients are regenerated.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, prod
from pathlib import Path
import json

Exponent = tuple[int, int, int]
Poly = dict[Exponent, int]
ZERO: Exponent = (0, 0, 0)
DEGREES = (11, 15, 15)
SHAPE = tuple(d + 1 for d in DEGREES)
INDICES = tuple(product(*(range(n) for n in SHAPE)))
DENOM = prod(factorial(d) for d in DEGREES)
GAP_DENOM = DENOM * 2**30 * 3**10


def require(condition: bool, message: str) -> None:
    """Checks remain active even under python -O."""
    if not condition:
        raise ArithmeticError(message)


def plus(*polys: Poly) -> Poly:
    result: Poly = {}
    for p in polys:
        for e, c in p.items():
            result[e] = result.get(e, 0) + c
    return {e: c for e, c in result.items() if c}


def scale(p: Poly, c: int) -> Poly:
    return {e: c * v for e, v in p.items() if c * v}


def times(p: Poly, q: Poly) -> Poly:
    result: Poly = {}
    for (a, b, c), x in p.items():
        for (i, j, k), y in q.items():
            e = (a + i, b + j, c + k)
            result[e] = result.get(e, 0) + x * y
    return {e: c for e, c in result.items() if c}


def evaluate(p: Poly, point: tuple[int, int, int]) -> int:
    return sum(c * prod(x**i for x, i in zip(point, e)) for e, c in p.items())


def digest(data: object) -> str:
    return sha256(json.dumps(data, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def construct_gap() -> tuple[Poly, int]:
    one = {ZERO: 1}
    a = {(1, 0, 0): 1}
    b = {(0, 1, 0): 1}
    c = {(0, 0, 1): 1}
    A = [[plus(one, scale(a, -1), scale(b, -1)), plus(one, a), plus(one, b)],
         [plus(one, a), plus(one, scale(a, -1), scale(c, -1)), plus(one, c)],
         [plus(one, b), plus(one, c), plus(one, scale(b, -1), scale(c, -1))]]
    for row in A:
        require(plus(*row) == {ZERO: 3}, "symbolic row sum")
    triples = sorted({tuple(sorted(x)) for x in product(range(3), repeat=3)})
    D = {tri: plus(*(times(times(A[w][tri[0]], A[w][tri[1]]), A[w][tri[2]])
                        for w in range(3))) for tri in triples}
    patterns: Counter = Counter()
    for colors in product(range(3), repeat=5):
        pat = tuple(sorted(tuple(sorted(colors[(i + j) % 5] for j in range(3)))
                           for i in range(5)))
        patterns[pat] += 1
    result: Poly = {}
    for pat, multiplicity in sorted(patterns.items()):
        term = one
        for tri in pat:
            term = times(term, D[tri])
        result = plus(result, scale(term, multiplicity))
    require(sum(patterns.values()) == 3**5, "coloring coverage")
    require(result.get(ZERO) == 3**10, "density normalization at J")
    return plus(result, {ZERO: -(3**10)}), len(patterns)


def numeric_matrix(a: int, b: int, c: int) -> list[list[int]]:
    return [[1-a-b, 1+a, 1+b], [1+a, 1-a-c, 1+c], [1+b, 1+c, 1-b-c]]


def direct_hom(A: list[list[int]]) -> int:
    # Independent sum over ALL 59,049 complete colorings, without contraction.
    edges = [(i, 5+j) for j in range(5) for i in range(5) if (i-j) % 5 in (0, 1, 2)]
    total = 0
    for colors in product(range(3), repeat=10):
        weight = 1
        for u, v in edges:
            weight *= A[colors[u]][colors[v]]
            if weight == 0:
                break
        total += weight
    return total


def geometry_checks() -> None:
    # Verify missing edges form ONE C_10, not a different cubic bipartite graph.
    missing = [(i, 5+j) for j in range(5) for i in range(5) if (i-j) % 5 not in (0, 1, 2)]
    neighbors = {i: set() for i in range(10)}
    for a, b in missing:
        neighbors[a].add(b)
        neighbors[b].add(a)
    require(len(missing) == 10 and all(len(v) == 2 for v in neighbors.values()), "missing degree")
    seen, stack = set(), [0]
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack.extend(neighbors[x] - seen)
    require(len(seen) == 10, "missing cycle connectivity")

    # Polytope inequalities n dot x <= 1. Enumerate every intersection of 3 planes.
    normals = [(-1,0,0), (0,-1,0), (0,0,-1), (1,1,0), (1,0,1), (0,1,1)]
    def det(m):
        return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
                -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    vertices = set()
    for rows in combinations(normals, 3):
        d = det(rows)
        if not d:
            continue
        point = tuple(Fraction(det([[1 if j == k else row[j] for j in range(3)]
                                    for row in rows]), d) for k in range(3))
        if all(sum(n[i]*point[i] for i in range(3)) <= 1 for n in normals):
            vertices.add(point)
    expected = {(-1,-1,-1), (2,-1,-1), (-1,2,-1), (-1,-1,2),
                (Fraction(1,2),)*3}
    require(vertices == expected, "all polytope vertices")
    require(all(sum(sum(n[i]*v[i] for i in range(3)) == 1 for v in vertices) == 3
                for n in normals), "six triangular faces")


def face_square(F: Poly, name: str) -> Poly:
    # Variables here are (r,u,v). Divide out r^4 symbolically, then clear 2^15.
    def linear(c0: int, cu: int, cv: int) -> Poly:
        return {e: c for e, c in [(ZERO,c0), ((0,1,0),cu), ((0,0,1),cv)] if c}
    if name == "lower":
        face, den = [linear(-1,3,0), linear(-1,0,3), linear(-1,0,0)], 1
    elif name == "upper":
        face, den = [linear(1,3,-3), linear(1,-3,3), linear(1,-3,-3)], 2
    else:
        raise ValueError(name)
    powers = [[{ZERO: 1}] for _ in range(3)]
    for i in range(3):
        for _ in range(15):
            powers[i].append(times(powers[i][-1], face[i]))
    poly: Poly = {}
    for (i,j,k), c in F.items():
        d = i+j+k
        require(4 <= d <= 15 and 2**15 % den**d == 0, "radial quotient")
        term = scale(times(times(powers[0][i], powers[1][j]), powers[2][k]), c*(2**15//den**d))
        poly = plus(poly, {(a+d-4,b,c): v for (a,b,c),v in term.items()})
    # u=s, v=(1-s)t, an onto map of the unit square onto the face triangle.
    result: Poly = {}
    for (i,j,k), c in poly.items():
        result = plus(result, {(i,j+h,k): c*comb(k,h)*(-1)**h for h in range(k+1)})
    require(all(all(e[i] <= DEGREES[i] for i in range(3)) for e in result), "multidegrees")
    return result


def tensor_map(tensor: list[int], axis: int, matrix: list[list[int]]) -> list[int]:
    stride = prod(SHAPE[axis+1:])
    width = SHAPE[axis]
    result = [0]*len(INDICES)
    for index, e in enumerate(INDICES):
        base = index - e[axis]*stride
        result[index] = sum(matrix[e[axis]][k]*tensor[base+k*stride] for k in range(width))
    return result


def bernstein(poly: Poly) -> list[int]:
    # Returns D times the tensor Bernstein coefficients; all entries are integers.
    tensor = [poly.get(e, 0) for e in INDICES]
    for axis, d in enumerate(DEGREES):
        matrix = [[comb(i,k)*factorial(k)*factorial(d-k) if k <= i else 0
                   for k in range(d+1)] for i in range(d+1)]
        tensor = tensor_map(tensor, axis, matrix)
    return tensor


def midpoint_coefficients(parent: list[int], half: int) -> list[int]:
    # Split only s, degree 15. Extra scale 2^15 on both children.
    d = DEGREES[1]
    if half == 0:
        matrix = [[comb(i,j)*2**(d-i) if j <= i else 0 for j in range(d+1)] for i in range(d+1)]
    else:
        matrix = [[comb(d-i,j-i)*2**i if j >= i else 0 for j in range(d+1)] for i in range(d+1)]
    return tensor_map(parent, 1, matrix)


def direct_half_polynomial(poly: Poly, half: int) -> Poly:
    # Independent power substitution 2^15 Q(r,(z+half)/2,t).
    result: Poly = {}
    for (i,j,k), c in poly.items():
        if half == 0:
            result = plus(result, {(i,j,k): c*2**(15-j)})
        else:
            result = plus(result, {(i,h,k): c*comb(j,h)*2**(15-j) for h in range(j+1)})
    return result


def run() -> dict:
    geometry_checks()
    F, pattern_count = construct_gap()
    require(len(F) == 664 and pattern_count == 39, "expected polynomial size")
    require(min(map(sum, F)) == 4 and all(sum(e) != 5 for e in F), "first homogeneous degrees")
    for sigma in permutations(range(3)):
        require({tuple(e[i] for i in sigma): c for e,c in F.items()} == F, "block relabeling invariance")
    points = [(0,0,0), (-1,-1,-1), (2,-1,-1), (1,0,0), (1,-1,-1), (2,-3,4)]
    for point in points:
        require(direct_hom(numeric_matrix(*point)) - 3**10 == evaluate(F, point),
                f"complete-coloring regression {point}")

    # Scalar/unit-monomial control checks catch tensor ordering and normalization mistakes.
    require(all(c == DENOM for c in bernstein({ZERO:1})), "constant Bernstein")
    for axis,d in enumerate(DEGREES):
        e = tuple(int(i == axis) for i in range(3))
        coeff = bernstein({e:1})
        require(all(coeff[k]*d == DENOM*index[axis] for k,index in enumerate(INDICES)),
                "linear Bernstein")
    expected_minima = {
        ("lower",0): Fraction(17929,38220), ("lower",1): Fraction(43,84),
        ("upper",0): Fraction(725117,3179904), ("upper",1): Fraction(5055,11648)}
    certificates = []
    for name in ("lower", "upper"):
        poly = face_square(F, name)
        parent = bernstein(poly)
        for half in (0,1):
            coeff = midpoint_coefficients(parent, half)
            # Checks all 3,072 coefficients via a different exact derivation.
            require(coeff == bernstein(direct_half_polynomial(poly, half)), "midpoint identity")
            require(all(5*x > GAP_DENOM for x in coeff), "strict 1/5 lower certificate")
            value = Fraction(min(coeff), GAP_DENOM)
            require(value == expected_minima[name,half], "reproducible exact minimum")
            certificates.append({
                "face": name, "s_half": half, "coefficient_count": len(coeff),
                "negative_count": sum(x < 0 for x in coeff),
                "minimum_scaled_integer": str(min(coeff)),
                "normalized_minimum": str(value),
                "coefficient_sha256": digest(coeff),
                "independent_power_substitution_match": True})
    return {
        "status": "ALL_EXACT_CHECKS_PASS",
        "claim_id": "C30-EQUAL-THREE-BLOCK-STABILITY-20260917",
        "scope": "Symmetric nonnegative 3x3 matrices with row sums 3; uniform block weights only",
        "full_Sidorenko_conjecture_solved": False,
        "arithmetic": "Python integers and exact rational numbers; no floating-point decisions",
        "polynomial_monomials": len(F), "triple_patterns": pattern_count,
        "polynomial_sha256": digest([[list(e), c] for e,c in sorted(F.items())]),
        "homogeneous_monomial_counts": dict(sorted(Counter(map(sum,F)).items())),
        "all_block_permutations_checked": 6,
        "direct_full_coloring_checks": len(points),
        "colorings_per_direct_check": 3**10,
        "geometry_vertex_and_face_checks": "PASS",
        "tensor_degrees": list(DEGREES),
        "normalized_gap_common_denominator": str(GAP_DENOM),
        "total_certified_coefficients": sum(c["coefficient_count"] for c in certificates),
        "global_radial_constant": str(min(Fraction(c["normalized_minimum"]) for c in certificates)),
        "simplified_radial_constant": "1/5", "L2_fourth_power_constant": "1/20",
        "certificates": certificates,
        "external_independent_audits": "Not performed; internal cross-checks are not independent track audits"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write deterministic JSON result to this path")
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
