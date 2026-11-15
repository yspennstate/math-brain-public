#!/usr/bin/env python3
"""Exact bounded-degree local-charge classification; Python standard library only.

All files are written next to this script. No integration or random sampling is used.
"""
import itertools
import json
import math
import os
import resource
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

DEGREE = 6
ROOT = Path(__file__).resolve().parent


def exponents(n, degree):
    """All exponent vectors of total degree at most degree, in fixed order."""
    return sorted(x for x in itertools.product(range(degree + 1), repeat=n)
                  if sum(x) <= degree)


def trim(e):
    """Infinite-chain monomial modulo translation; interleaved (r_i,p_i)."""
    pairs = [tuple(e[j:j + 2]) for j in range(0, len(e), 2)]
    while pairs and pairs[0] == (0, 0):
        pairs.pop(0)
    while pairs and pairs[-1] == (0, 0):
        pairs.pop()
    return tuple(a for pair in pairs for a in pair)


def local_column(alpha, cubic=1):
    """Differentiate one density at sites 0,1, then sum translation orbits.

    Working slots are sites -1,0,1,2. F(r)=r+cubic*r^3.
    """
    base = [0, 0] + list(alpha) + [0, 0]
    out = defaultdict(int)
    for j, power in enumerate(alpha):
        if not power:
            continue
        site, kind = divmod(j, 2)
        reduced = base.copy()
        reduced[2 + j] -= 1
        if kind == 0:
            # d r_site / dt = p_site - p_(site-1)
            terms = [(2 * (site + 1) + 1, 1, 1),
                     (2 * site + 1, 1, -1)]
        else:
            # d p_site / dt = F(r_(site+1)) - F(r_site)
            terms = [(2 * (site + 2), 1, 1),
                     (2 * (site + 1), 1, -1),
                     (2 * (site + 2), 3, cubic),
                     (2 * (site + 1), 3, -cubic)]
        for target, extra, sign in terms:
            if sign:
                term = reduced.copy()
                term[target] += extra
                out[trim(term)] += power * sign
    return {key: value for key, value in out.items() if value}


def rational_column_rank(columns):
    """Sparse Gaussian elimination over Q, processing columns."""
    pivots = {}
    for col in columns:
        v = {k: Fraction(a) for k, a in col.items()}
        while v:
            k = min(v)
            if k not in pivots:
                a = v[k]
                pivots[k] = {j: b / a for j, b in v.items()}
                break
            a = v[k]
            for j, b in pivots[k].items():
                v[j] = v.get(j, 0) - a * b
                if not v[j]:
                    del v[j]
    return len(pivots)


def modular_row_rank(rows, prime):
    """Dense row elimination over F_prime; records a nonsingular minor."""
    if not rows:
        return {"rank": 0, "pivot_rows": [], "pivot_columns": [], "determinant_mod_prime": 1}
    a = [[v % prime for v in row] for row in rows]
    original_rows = list(range(len(a)))
    pivot_rows, pivot_columns = [], []
    rank, determinant = 0, 1
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        if pivot != rank:
            a[rank], a[pivot] = a[pivot], a[rank]
            original_rows[rank], original_rows[pivot] = original_rows[pivot], original_rows[rank]
        pivot_rows.append(original_rows[rank])
        pivot_columns.append(col)
        lead = a[rank][col]
        determinant = determinant * lead % prime
        inverse = pow(lead, -1, prime)
        a[rank] = [(v * inverse) % prime for v in a[rank]]
        for i in range(rank + 1, len(a)):
            if a[i][col]:
                factor = a[i][col]
                a[i] = [(v - factor * w) % prime for v, w in zip(a[i], a[rank])]
        rank += 1
    # Selected rows are stored in elimination order, so row swaps are already
    # represented in their order: no parity factor belongs in this minor.
    return {"rank": rank, "pivot_rows": pivot_rows, "pivot_columns": pivot_columns,
            "determinant_mod_prime": determinant}


def determinant_mod(matrix, prime):
    """Independent square-matrix determinant, without row normalization."""
    a = [[x % prime for x in row] for row in matrix]
    result = 1
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            result = -result
        lead = a[col][col]
        result = result * lead % prime
        inverse = pow(lead, -1, prime)
        for i in range(col + 1, len(a)):
            factor = a[i][col] * inverse % prime
            for j in range(col + 1, len(a)):
                a[i][j] = (a[i][j] - factor * a[col][j]) % prime
            a[i][col] = 0
    return result % prime


def kernel_candidates(alphas):
    index = {alpha: j for j, alpha in enumerate(alphas)}

    def vector(terms):
        out = [0] * len(alphas)
        for alpha, coeff in terms:
            out[index[alpha]] += coeff
        return out

    basis = []
    labels = []
    for a, b in exponents(2, DEGREE):
        if a + b:
            labels.append(f"r0^{a}p0^{b}-r1^{a}p1^{b}")
            basis.append(vector([((a, b, 0, 0), 1), ((0, 0, a, b), -1)]))
    for label, terms in [
        ("constant", [((0, 0, 0, 0), 1)]),
        ("stretch", [((1, 0, 0, 0), 1)]),
        ("momentum", [((0, 1, 0, 0), 1)]),
        ("4*energy", [((0, 2, 0, 0), 2), ((2, 0, 0, 0), 2), ((4, 0, 0, 0), 1)]),
    ]:
        labels.append(label)
        basis.append(vector(terms))
    return labels, basis


def periodic_column(alpha, n, cubic=1):
    """Independent construction: first form Q on a ring, then differentiate Q.

    Full 2*n-variable monomials are retained, without orbit reduction during
    differentiation. Only afterward are their coefficients grouped by rotations.
    """
    q = defaultdict(int)
    for site in range(n):
        e = [0] * (2 * n)
        for j, power in enumerate(alpha):
            offset, kind = divmod(j, 2)
            e[2 * ((site + offset) % n) + kind] += power
        q[tuple(e)] += 1
    dq = defaultdict(int)
    for e, coeff in q.items():
        for variable, power in enumerate(e):
            if not power:
                continue
            site, kind = divmod(variable, 2)
            if kind == 0:
                velocity = [(2 * site + 1, 1, 1),
                            (2 * ((site - 1) % n) + 1, 1, -1)]
            else:
                velocity = [(2 * ((site + 1) % n), 1, 1),
                            (2 * site, 1, -1)]
                if cubic:
                    velocity += [(2 * ((site + 1) % n), 3, cubic),
                                 (2 * site, 3, -cubic)]
            for target, degree, sign in velocity:
                term = list(e)
                term[variable] -= 1
                term[target] += degree
                dq[tuple(term)] += coeff * power * sign
    out = defaultdict(int)
    for e, coeff in dq.items():
        if not coeff:
            continue
        # Every derivative term has support diameter <=2. Its cyclic orbit
        # has a unique shortest cut when n>=5. No infinite trim() is used.
        cuts = []
        for site in range(n):
            rotated = e[2 * site:] + e[:2 * site]
            occupied = [i for i in range(n) if rotated[2 * i] or rotated[2 * i + 1]]
            if occupied and occupied[0] == 0:
                cuts.append((occupied[-1], rotated[:2 * (occupied[-1] + 1)]))
        _, canonical = min(cuts)
        out[canonical] += coeff
    assert all(value % n == 0 for value in out.values())
    return {key: value // n for key, value in out.items() if value}


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def main():
    start = time.monotonic()
    # Limits apply to this process and are well below the author's ceilings.
    _, hard_cpu = resource.getrlimit(resource.RLIMIT_CPU)
    cpu_cap = 180 if hard_cpu == resource.RLIM_INFINITY else min(180, hard_cpu)
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_cap, cpu_cap))
    # macOS rejects lowering RLIMIT_RSS in this sandbox. The explicit matrices
    # are small; record actual peak RSS and check it against the author's cap.
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    alphas = exponents(4, DEGREE)
    assert len(alphas) == math.comb(DEGREE + 4, 4)
    columns = [local_column(alpha) for alpha in alphas]
    monomials = sorted(set().union(*(col.keys() for col in columns)))
    assert max(len(m) // 2 - 1 for m in monomials) == 2
    rows = [[col.get(key, 0) for col in columns] for key in monomials]
    print(f"degree={DEGREE}; density_variables=4; columns={len(alphas)}; rows={len(rows)}", flush=True)
    labels, kernel = kernel_candidates(alphas)
    for v in kernel:
        assert all(sum(x * y for x, y in zip(row, v)) == 0 for row in rows)
    kernel_rank = rational_column_rank([{i: v for i, v in enumerate(col) if v} for col in kernel])
    rank_q = rational_column_rank(columns)
    print(f"rational_rank={rank_q}; nullity={len(alphas)-rank_q}; exact_kernel_vectors={len(kernel)}; kernel_rank={kernel_rank}", flush=True)
    assert rank_q + kernel_rank == len(alphas)
    certificates = []
    for prime in (1000003, 1000033):
        assert is_prime(prime)
        cert = modular_row_rank(rows, prime)
        minor = [[rows[i][j] for j in cert["pivot_columns"]] for i in cert["pivot_rows"]]
        det = determinant_mod(minor, prime)
        assert det == cert["determinant_mod_prime"] != 0
        assert cert["rank"] == rank_q
        cert["prime"] = prime
        certificates.append(cert)
        print(f"prime={prime}; rank={cert['rank']}; certified_minor_determinant={det}", flush=True)
    periodic_checks = {}
    for n in (5, 6, 7, 8):
        independent = [periodic_column(alpha, n) for alpha in alphas]
        assert independent == columns
        periodic_checks[str(n)] = "all 210 columns identical, with exact integer coefficients"
        print(f"periodic_ring_N={n}: all {len(alphas)} independently constructed columns match", flush=True)
    # A negative control: the same ansatz must detect extra harmonic charges.
    harmonic = [local_column(alpha, cubic=0) for alpha in alphas]
    harmonic_rank = rational_column_rank(harmonic)
    harmonic_nullity = len(alphas) - harmonic_rank
    assert harmonic_nullity > len(kernel)
    print(f"harmonic_control: rank={harmonic_rank}; density_nullity={harmonic_nullity}; nonzero_additive_charges={harmonic_nullity-(math.comb(DEGREE+2,2)-1)}", flush=True)
    # One explicit harmonic charge that must fail for the quartic potential.
    ix = {a: i for i, a in enumerate(alphas)}
    current = [0] * len(alphas)
    current[ix[(1, 1, 0, 0)]] = 1
    current[ix[(0, 1, 1, 0)]] = 1
    def image(cols, v):
        out = defaultdict(int)
        for coeff, col in zip(v, cols):
            for key, value in col.items():
                out[key] += coeff * value
        return {key: value for key, value in out.items() if value}
    assert not image(harmonic, current)
    current_quartic = image(columns, current)
    assert current_quartic
    print(f"harmonic_current: conserved for harmonic force, NOT conserved for quartic force; residual_terms={len(current_quartic)}", flush=True)
    data = {
        "degree": DEGREE, "potential": "r^2/2+r^4/4",
        "density_variables": ["r0", "p0", "r1", "p1"],
        "column_exponents": alphas, "row_monomials_interleaved_r_p": monomials,
        "sparse_matrix_rows": [[[j, a] for j, a in enumerate(row) if a] for row in rows],
        "rational_rank": rank_q, "kernel_labels": labels, "kernel_vectors": kernel,
        "kernel_rank": kernel_rank, "modular_certificates": certificates,
        "periodic_checks": periodic_checks,
        "harmonic_rank": harmonic_rank, "harmonic_nullity": harmonic_nullity,
        "harmonic_current_quartic_residual": [[list(k), v] for k, v in sorted(current_quartic.items())],
    }
    (ROOT / "charge_data.json").write_text(json.dumps(data, indent=2) + "\n")
    elapsed = time.monotonic() - start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Darwin reports bytes; Linux reports KiB.
    import sys
    rss_mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
    assert rss_mib < 1024
    print(f"effective_nice={priority}; elapsed_seconds={elapsed:.3f}; peak_rss_MiB={rss_mib:.3f}", flush=True)
    print("PASS: exact classification and independent audits; data=charge_data.json", flush=True)


if __name__ == "__main__":
    main()
