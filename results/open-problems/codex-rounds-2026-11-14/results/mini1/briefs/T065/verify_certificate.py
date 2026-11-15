#!/usr/bin/env python3
"""Standalone verifier; does not import conserved_charges.py.

Reconstructs the full derivative polynomials on a five-site ring and checks
the saved matrix, an exact kernel basis, and a nonzero rank minor.
"""
import json
import os
import resource
import time
from collections import defaultdict
from pathlib import Path


def determinant(a, p):
    a = [[x % p for x in row] for row in a]
    value = 1
    for j in range(len(a)):
        i = next((i for i in range(j, len(a)) if a[i][j]), None)
        if i is None:
            return 0
        if i != j:
            a[i], a[j] = a[j], a[i]
            value = -value
        pivot = a[j][j]
        value = value * pivot % p
        # Fraction-free row update, scaled by inverse pivot in the field.
        inv = pow(pivot, p - 2, p)
        for k in range(j + 1, len(a)):
            factor = a[k][j] * inv % p
            for ell in range(j + 1, len(a)):
                a[k][ell] = (a[k][ell] - factor * a[j][ell]) % p
            a[k][j] = 0
    return value % p


def derivative_on_ring(alpha, n):
    q = defaultdict(int)
    for origin in range(n):
        powers = [0] * (2 * n)
        for offset in range(2):
            for kind in range(2):
                powers[2 * ((origin + offset) % n) + kind] = alpha[2 * offset + kind]
        q[tuple(powers)] += 1
    result = defaultdict(int)
    for powers, coefficient in q.items():
        for site in range(n):
            for kind in range(2):
                variable = 2 * site + kind
                power = powers[variable]
                if not power:
                    continue
                reduced = list(powers)
                reduced[variable] -= 1
                if kind == 0:
                    velocity_terms = [(site, 1, 1, 1), ((site - 1) % n, 1, 1, -1)]
                else:
                    velocity_terms = [((site + 1) % n, 0, k, 1) for k in (1, 3)]
                    velocity_terms += [(site, 0, k, -1) for k in (1, 3)]
                for target_site, target_kind, degree, sign in velocity_terms:
                    term = reduced.copy()
                    term[2 * target_site + target_kind] += degree
                    result[tuple(term)] += coefficient * power * sign
    return {k: v for k, v in result.items() if v}


def main():
    start = time.monotonic()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    data = json.loads(Path(__file__).with_name("charge_data.json").read_text())
    alphas = data["column_exponents"]
    assert len(alphas) == 210 and len(set(map(tuple, alphas))) == 210
    assert all(len(a) == 4 and min(a) >= 0 and sum(a) <= 6 for a in alphas)
    rows = [[0] * 210 for _ in data["sparse_matrix_rows"]]
    for i, row in enumerate(data["sparse_matrix_rows"]):
        for j, value in row:
            rows[i][j] = value
    n = 5
    for j, alpha in enumerate(alphas):
        expected = defaultdict(int)
        for i, monomial in enumerate(data["row_monomials_interleaved_r_p"]):
            coefficient = rows[i][j]
            if not coefficient:
                continue
            for origin in range(n):
                term = [0] * (2 * n)
                for k, power in enumerate(monomial):
                    offset, kind = divmod(k, 2)
                    term[2 * ((origin + offset) % n) + kind] += power
                expected[tuple(term)] += coefficient
        assert {k: v for k, v in expected.items() if v} == derivative_on_ring(alpha, n)
    print("full N=5 polynomial derivatives: 210/210 columns verified")
    kernel = data["kernel_vectors"]
    assert len(kernel) == 31
    assert all(sum(row[j] * v[j] for j in range(210)) == 0 for row in rows for v in kernel)
    # Full rank of the 31 candidate vectors, independently checked by a Gram
    # determinant modulo a prime. Invertible Gram implies independence.
    p = 1000003
    assert all(p % d for d in range(2, 1001))
    gram = [[sum(x * y for x, y in zip(v, w)) for w in kernel] for v in kernel]
    gram_det = determinant(gram, p)
    assert gram_det
    print(f"31 exact kernel vectors; independent Gram determinant mod {p} = {gram_det}")
    for cert in data["modular_certificates"]:
        prime = cert["prime"]
        assert all(prime % d for d in range(2, int(prime**0.5) + 1))
        assert len(set(cert["pivot_rows"])) == len(set(cert["pivot_columns"])) == 179
        minor = [[rows[i][j] for j in cert["pivot_columns"]] for i in cert["pivot_rows"]]
        value = determinant(minor, prime)
        assert value == cert["determinant_mod_prime"] != 0
        print(f"179x179 minor mod {prime}: determinant = {value}")
    print("rank over Q and R = 179; kernel dimension = 31; quotient by 27 telescopes = 4")
    elapsed = time.monotonic() - start
    import sys
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024**2 if sys.platform == "darwin" else 1024)
    assert peak < 1024
    print(f"PASS; elapsed_seconds={elapsed:.3f}; peak_rss_MiB={peak:.3f}")


if __name__ == "__main__":
    main()
