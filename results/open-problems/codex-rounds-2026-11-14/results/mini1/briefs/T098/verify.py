"""Small independent checks of the barrier-chain theorem in PROOF.md.

No sampling claim about generic MBL is made. Matrices have dimension <=128.
Writes verification.json and tail_checks.csv in this script's directory.
"""

import os

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

import csv
import ctypes
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15, (priority, ctypes.get_errno())

import numpy as np

np.seterr(all="raise")

ROOT = Path(__file__).resolve().parent
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOL = 1e-10


def mm(a, b):
    # Explicit contraction avoids the BLAS matmul path used in the first run.
    assert np.all(np.isfinite(a)) and np.all(np.isfinite(b))
    result = np.einsum("ij,jk->ik", a, b, optimize=False)
    assert np.all(np.isfinite(result))
    return result


def kron_all(factors):
    ans = np.ones((1, 1), dtype=complex)
    for factor in factors:
        ans = np.kron(ans, factor)
    return ans


def local(pauli, i, n):
    return kron_all([pauli if j == i else I for j in range(n)])


def spins(k, n):
    return [1 - 2 * ((k >> (n - 1 - i)) & 1) for i in range(n)]


def active_blocks(mask):
    blocks = []
    i = 0
    while i < len(mask):
        if not mask[i]:
            i += 1
            continue
        a = i
        while i + 1 < len(mask) and mask[i + 1]:
            i += 1
        blocks.append((a, i))
        i += 1
    return blocks


def envelope_from_blocks(mask, i):
    ans = {i}
    n = len(mask)
    for a, b in active_blocks(mask):
        padded = set(range(max(0, a - 1), min(n, b + 2)))
        if i in padded:
            ans |= padded
    return ans


def envelope_by_stopping(mask, i):
    # An independent nearest-frozen-site construction of (12).
    left = i
    if mask[i] or (i > 0 and mask[i - 1]):
        left = i - 1
        while left >= 0 and mask[left]:
            left -= 1
        left = max(0, left)
    right = i
    if mask[i] or (i + 1 < len(mask) and mask[i + 1]):
        right = i + 1
        while right < len(mask) and mask[right]:
            right += 1
        right = min(len(mask) - 1, right)
    return set(range(left, right + 1))


def hamiltonian_kron(h, gamma, bonds):
    n = len(h)
    zs = [local(Z, i, n) for i in range(n)]
    ans = sum(h[i] * zs[i] + gamma[i] * local(X, i, n) for i in range(n))
    for i, j in enumerate(bonds):
        ans += j * mm(zs[i], zs[i + 1])
    return ans


def hamiltonian_bits(h, gamma, bonds):
    # Uses basis energies and bit flips, independently of Kronecker assembly.
    n = len(h)
    ans = np.zeros((2**n, 2**n), dtype=complex)
    for k in range(2**n):
        s = spins(k, n)
        ans[k, k] = sum(a * b for a, b in zip(h, s))
        ans[k, k] += sum(bonds[i] * s[i] * s[i + 1] for i in range(n - 1))
        for i in range(n):
            ans[k ^ (1 << (n - 1 - i)), k] += gamma[i]
    return ans


def gates_and_predicted_diagonal(h, gamma, bonds, mask):
    n = len(mask)
    gates = []
    frozen = [i for i in range(n) if not mask[i]]
    predicted = np.zeros(2**n)
    for k in range(2**n):
        s = spins(k, n)
        predicted[k] = sum(h[i] * s[i] for i in frozen)
        predicted[k] += sum(bonds[i] * s[i] * s[i + 1]
                            for i in range(n - 1) if not mask[i] and not mask[i + 1])
    for a, b in active_blocks(mask):
        boundary = ([a - 1] if a > 0 else []) + ([b + 1] if b + 1 < n else [])
        eigensystems = {}
        for signs in product((1, -1), repeat=len(boundary)):
            hh = np.array(h[a:b + 1], copy=True)
            control = dict(zip(boundary, signs))
            if a > 0:
                hh[0] += bonds[a - 1] * control[a - 1]
            if b + 1 < n:
                hh[-1] += bonds[b] * control[b + 1]
            block = hamiltonian_bits(hh, gamma[a:b + 1], bonds[a:b])
            eigensystems[signs] = np.linalg.eigh(block)
        gate = np.zeros((2**n, 2**n), dtype=complex)
        block_mask = ((1 << (b - a + 1)) - 1) << (n - 1 - b)
        for col in range(2**n):
            s = spins(col, n)
            signs = tuple(s[i] for i in boundary)
            values, vectors = eigensystems[signs]
            target_col = (col & block_mask) >> (n - 1 - b)
            predicted[col] += values[target_col]
            for target_row in range(2**(b - a + 1)):
                row = (col & ~block_mask) | (target_row << (n - 1 - b))
                gate[row, col] = vectors[target_row, target_col]
        gates.append(gate)
    return gates, predicted


def expectation_onto(matrix, support, n):
    kept = sorted(support)
    removed = [i for i in range(n) if i not in support]
    order = kept + removed + [n + i for i in kept] + [n + i for i in removed]
    dk, dr = 2**len(kept), 2**len(removed)
    tensor = matrix.reshape([2] * (2 * n)).transpose(order).reshape(dk, dr, dk, dr)
    reduced = np.einsum("abcb->ac", tensor) / dr
    rebuilt = np.kron(reduced, np.eye(dr)).reshape([2] * (2 * n))
    return rebuilt.transpose(np.argsort(order)).reshape(2**n, 2**n)


def matrix_checks():
    rng = np.random.default_rng(9802026)
    cases = []
    for n in range(1, 6):
        for mask in product((0, 1), repeat=n):
            cases.append(("exhaustive_masks", mask, rng.uniform(-4, 4, n),
                          rng.uniform(-0.7, 0.7, n), rng.uniform(-1, 1, n - 1)))
    for mask in ((1, 1, 0, 1, 1, 0, 1), (0, 1, 1, 1, 1, 1, 0),
                 (1, 0, 1, 0, 1, 0, 1), (1,) * 7, (0,) * 7):
        n = len(mask)
        cases.append(("seven_site_edges", mask, rng.uniform(-3, 3, n),
                      rng.uniform(-0.5, 0.5, n), rng.uniform(-1, 1, n - 1)))
    cases.append(("all_zero_degeneracy", (1, 0, 1, 1, 0),
                  np.zeros(5), np.zeros(5), np.zeros(4)))
    cases.append(("degenerate_interacting", (1, 0, 1, 0, 1),
                  np.zeros(5), np.ones(5), np.ones(4)))
    maxima = {}
    rows = []

    def check(name, value, scale=1.0):
        assert np.isfinite(value) and np.isfinite(scale), (name, value, scale)
        normalized = float(value / max(1.0, scale))
        maxima[name] = max(maxima.get(name, 0.0), normalized)
        assert normalized < TOL, (name, normalized)

    for label, mask, h, amplitudes, bonds in cases:
        n, dim = len(mask), 2**len(mask)
        gamma = np.array(mask) * amplitudes
        H = hamiltonian_kron(h, gamma, bonds)
        Hbits = hamiltonian_bits(h, gamma, bonds)
        scale = max(1, np.linalg.norm(H, "fro"))
        check("independent_H_assembly", np.linalg.norm(H - Hbits, "fro"), scale)
        gates, predicted = gates_and_predicted_diagonal(h, gamma, bonds, mask)
        U = np.eye(dim, dtype=complex)
        for gate in gates:
            U = mm(U, gate)
        for j, gate in enumerate(gates):
            for other in gates[:j]:
                check("gate_commutator", np.linalg.norm(mm(gate, other) - mm(other, gate), "fro"), dim**0.5)
        check("unitarity", np.linalg.norm(mm(U.conj().T, U) - np.eye(dim), "fro"), dim**0.5)
        D = mm(mm(U.conj().T, H), U)
        check("off_diagonal", np.linalg.norm(D - np.diag(np.diag(D)), "fro"), scale)
        check("sector_energy_formula", np.linalg.norm(np.diag(D) - predicted), scale)
        eig_error = np.max(np.abs(np.linalg.eigvalsh(H) - np.sort(predicted)))
        check("full_spectrum", eig_error, scale)
        taus = [mm(mm(U, local(Z, i, n)), U.conj().T) for i in range(n)]
        for i, tau in enumerate(taus):
            check("lbit_H_commutator", np.linalg.norm(mm(H, tau) - mm(tau, H), "fro"), scale)
            check("lbit_involution", np.linalg.norm(mm(tau, tau) - np.eye(dim), "fro"), dim**0.5)
            for other in taus[:i]:
                check("lbit_pair_commutator", np.linalg.norm(mm(tau, other) - mm(other, tau), "fro"), dim**0.5)
            if not mask[i]:
                check("frozen_lbit", np.linalg.norm(tau - local(Z, i, n), "fro"), dim**0.5)
            support = envelope_from_blocks(mask, i)
            assert support == envelope_by_stopping(mask, i)
            for pauli in (X, Y, Z):
                op = local(pauli, i, n)
                for forward in (True, False):
                    rotated = mm(mm(U, op), U.conj().T) if forward else mm(mm(U.conj().T, op), U)
                    check("support_envelope", np.linalg.norm(rotated - expectation_onto(rotated, support, n), "fro"), dim**0.5)
        # Binary-weighted l-bits have 2^n distinct joint-label eigenvalues.
        label_op = sum(2**i * tau for i, tau in enumerate(taus))
        exact_labels = sorted(sum(2**i * s for i, s in enumerate(spins(k, n))) for k in range(dim))
        check("joint_label_completeness", np.max(np.abs(np.linalg.eigvalsh(label_op) - exact_labels)), dim)
        rows.append({"kind": label, "mask": "".join(map(str, mask)), "n": n,
                     "dimension": dim, "full_spectrum_absolute_error": float(eig_error)})
    return {"case_count": len(cases), "normalized_residual_maxima": maxima,
            "cases": rows}


def exact_tail_checks():
    probabilities = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))
    row_count = 0
    masks_checked = 0
    sample = []
    with (ROOT / "tail_checks.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["L", "site_1based", "r", "p", "enumerated_probability",
                         "boundary_corrected_formula", "uniform_upper_bound"])
        for n in range(1, 10):
            counts = {(i, r): [0] * (n + 1) for i in range(n) for r in range(1, n + 1)}
            for mask in product((0, 1), repeat=n):
                masks_checked += 1
                k = sum(mask)
                for i in range(n):
                    env = envelope_from_blocks(mask, i)
                    assert env == envelope_by_stopping(mask, i)
                    radius = max(abs(j - i) for j in env)
                    for r in range(1, n + 1):
                        if radius > r:
                            counts[(i, r)][k] += 1
            for p in probabilities:
                weights = [p**k * (1 - p)**(n - k) for k in range(n + 1)]
                for (i, r), histogram in counts.items():
                    actual = sum(c * w for c, w in zip(histogram, weights))
                    sides = int(i - r > 0) + int(i + r < n - 1)
                    expected = 1 - (1 - p**r)**sides
                    bound = 2 * p**r - p**(2 * r)
                    assert actual == expected and actual <= bound, (n, i, r, p, actual, expected)
                    writer.writerow([n, i + 1, r, str(p), str(actual), str(expected), str(bound)])
                    row_count += 1
                    if n == 9 and i == 4 and r in (1, 2, 3, 4) and p == Fraction(1, 2):
                        sample.append({"L": n, "site": i + 1, "r": r,
                                       "p": str(p), "probability": str(actual), "bound": str(bound)})
    return {"masks_checked": masks_checked, "rational_probability_checks": row_count,
            "maximum_exact_error": "0", "selected_bulk_and_boundary_rows": sample}


def failure_and_gap_checks():
    mask = (1, 1, 0, 1, 1)
    h = np.array([1.3, -0.6, 0.2, 1.7, -2.1])
    amplitudes = np.array([0.2, -0.3, 0, 0.4, 0.1])
    bonds = np.array([0.5, -0.7, 0.8, -0.2])
    H = hamiltonian_kron(h, amplitudes, bonds)
    gates, _ = gates_and_predicted_diagonal(h, amplitudes, bonds, mask)
    U = np.eye(32, dtype=complex)
    for gate in gates:
        U = mm(U, gate)
    eps = 0.03125
    Hpert = H + eps * local(X, 2, 5)
    zbar = local(Z, 2, 5)
    comm = mm(Hpert, zbar) - mm(zbar, Hpert)
    comm_norm = float(np.linalg.norm(comm, 2))
    Dpert = mm(mm(U.conj().T, Hpert), U)
    residual = float(np.linalg.norm(Dpert - np.diag(np.diag(Dpert)), 2))
    assert abs(comm_norm - 2 * eps) < TOL
    assert abs(residual - eps) < TOL
    # H=0: an arbitrary energy eigenvector need not have definite l-bit labels.
    ghz = np.zeros(32)
    ghz[0] = ghz[-1] = 1 / np.sqrt(2)
    zghz = np.einsum("ij,j->i", zbar, ghz, optimize=False)
    zzghz = np.einsum("ij,j->i", zbar, zghz, optimize=False)
    variance = float(np.vdot(ghz, zzghz).real - np.vdot(ghz, zghz).real**2)
    assert abs(variance - 1) < TOL
    gaps = []
    for n in range(1, 9):
        energies = sorted(sum((3**i) * s for i, s in enumerate(spins(k, n))) for k in range(2**n))
        gap = min(b - a for a, b in zip(energies, energies[1:]))
        assert gap == 2
        gaps.append({"L": n, "exact_minimum_field_only_gap_at_t_1": gap})
    return {"epsilon": eps, "barrier_commutator_norm": comm_norm,
            "predicted_commutator_norm": 2 * eps,
            "old_diagonalizer_off_diagonal_norm": residual,
            "predicted_off_diagonal_norm": eps,
            "zero_H_GHZ_lbit_variance": variance, "base_three_gap_checks": gaps}


def main():
    started = time.monotonic()
    result = {"numpy_version": np.__version__, "seed": 9802026,
              "nice_value_from_libc": priority, "thread_environment": {
                  key: os.environ[key] for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                      "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")},
              "matrix_checks": matrix_checks(), "exact_tail_checks": exact_tail_checks(),
              "failure_and_gap_checks": failure_and_gap_checks()}
    peak_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak_raw if sys.platform == "darwin" else peak_raw * 1024
    result["peak_rss_bytes"] = peak_bytes
    result["elapsed_seconds"] = time.monotonic() - started
    assert peak_bytes < 1_000_000_000, peak_bytes
    result["status"] = "PASS"
    (ROOT / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    summary = {k: result[k] for k in ("status", "nice_value_from_libc", "peak_rss_bytes", "elapsed_seconds")}
    summary["matrix_cases"] = result["matrix_checks"]["case_count"]
    summary["largest_normalized_matrix_residual"] = max(result["matrix_checks"]["normalized_residual_maxima"].values())
    summary["exact_probability_checks"] = result["exact_tail_checks"]["rational_probability_checks"]
    summary["exact_probability_error"] = result["exact_tail_checks"]["maximum_exact_error"]
    summary["barrier_perturbation"] = result["failure_and_gap_checks"]
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
