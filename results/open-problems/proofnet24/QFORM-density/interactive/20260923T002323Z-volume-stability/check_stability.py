"""Deterministic finite checks for REPORT.md, not a proof of the conjecture.

Requires Python 3.10+ and NumPy. Writes check_results.json beside this file.
No network access, remote workflows, installation or large Monte Carlo run.
"""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path
import numpy as np


def elementary(x: np.ndarray, degree: int) -> float:
    c = np.zeros(degree + 1, dtype=float)
    c[0] = 1.0
    for value in x:
        for k in range(degree, 0, -1):
            c[k] += float(value) * c[k-1]
    return float(c[degree])


def volume_data(M: np.ndarray) -> tuple[float, np.ndarray, np.ndarray, np.ndarray]:
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    lam = s*s
    Z = elementary(lam, 3)
    if not np.isfinite(Z) or Z <= 0:
        raise ValueError("Matrix must have positive third volume")
    p = np.array([x*elementary(np.delete(lam, j), 2)/Z for j, x in enumerate(lam)])
    W = (U*p) @ U.T
    return Z, np.diag(W).copy(), W, s


def op(M: np.ndarray) -> float:
    return float(np.linalg.norm(M, 2))


def hadamard(n: int) -> np.ndarray:
    if n < 1 or n & (n-1):
        raise ValueError("n must be a positive power of two")
    H = np.ones((1, 1))
    while len(H) < n:
        H = np.block([[H, H], [H, -H]])
    return H


def main() -> None:
    rng = np.random.default_rng(230923)
    out = {"status": "PASS", "scope": "Finite deterministic algebra and matrix checks only; not a universal proof or independent analytic review", "full_conjecture_verified": False}

    errors = []
    for _ in range(12):
        M = rng.normal(size=(5, 6))
        Z, alpha, W, s = volume_data(M)
        total = 0.0
        row = np.zeros(5)
        for S in itertools.combinations(range(5), 3):
            for T in itertools.combinations(range(6), 3):
                mass = float(np.linalg.det(M[np.ix_(S, T)])**2)
                total += mass
                row[list(S)] += mass
        error = max(abs(Z-total)/Z, float(np.max(abs(alpha-row/total))))
        errors.append(error)
        assert error < 1e-11
        assert abs(float(np.trace(W))-3) < 1e-11
        assert np.linalg.eigvalsh(W).min() > -1e-11
        assert np.linalg.eigvalsh(np.eye(5)-W).min() > -1e-11
        assert np.linalg.eigvalsh(3*M@M.T/s[2]**2-W).min() > -1e-9
    out["volume_marginals"] = {"enumerated_matrices": 12, "maximum_relative_or_marginal_error": max(errors)}

    cases = []
    general_worst = 0.0
    gaussian_ratios = []
    q = 4.0/3.0
    for m, d, r in [(12, 9, 3), (16, 11, 4), (24, 13, 5), (32, 17, 5)]:
        for scale in [1e-2, 1e-6]:
            Uhalf, _ = np.linalg.qr(rng.normal(size=(m//2, r)))
            U = np.vstack([Uhalf, Uhalf])/math.sqrt(2)
            V, _ = np.linalg.qr(rng.normal(size=(d, r)))
            sigma = np.r_[2.0, 1.4, 1.0, np.full(r-3, scale)]
            M0 = (U*sigma)@V.T
            P = U@U.T
            leverage = np.diag(P)
            assert leverage.max() <= .5+1e-12
            for eps in [0.0, 0.01, 1.0/16]:
                E = rng.normal(size=(m, d))
                E *= eps/op(E)
                M = M0+E
                Z, alpha, W, s = volume_data(M)
                kappa = float(s[2])
                residual = op((np.eye(m)-P)@M)
                rhs = np.sqrt(np.maximum(0, leverage)) + math.sqrt(3)*residual/kappa*np.sqrt(np.maximum(0, 1-leverage))
                violation = float(np.max(np.sqrt(np.maximum(0,alpha))-rhs))
                general_worst = max(general_worst, violation)
                assert violation < 1e-10
                assert kappa >= 1-eps-1e-11
                assert alpha.max() < 2.0/3.0
                cases.append({"shape": [m, d], "baseline_rank": r, "small_singular_scale": scale, "noise_op_norm": op(E), "s3": kappa, "max_alpha": float(alpha.max())})
                # One explicit smooth cap-one product law, for a full quadratic
                # form with arbitrary self blocks. Not all laws or matrices.
                F = rng.normal(size=(m, m)); F=(F+F.T)/2
                G = rng.normal(size=(d, d)); G=(G+G.T)/2
                A = np.block([[F, M], [M.T, G]])
                eig = np.linalg.eigvalsh(A)
                b = 3/(2*q)
                logK = (3-1.5*math.log(q)+3*math.log(math.pi)-.5*math.log(Z))/(2*q)
                for t in np.geomspace(.01, 100, 25):
                    logexact = -.25*float(np.log1p((t*eig/math.pi)**2).sum())
                    logbound = min(0.0, logK-b*math.log(t))
                    assert logexact <= logbound + 1e-10
                    gaussian_ratios.append(math.exp(logexact-logbound))
    out["perturbation_cases"] = {"count": len(cases), "maximum_positive_stability_violation": general_worst, "cases": cases}
    out["gaussian_full_form_checks"] = {"count": len(gaussian_ratios), "maximum_modulus_over_envelope": max(gaussian_ratios), "law": "Each coordinate has density exp(-pi*x*x); affine term zero in this finite check"}

    # Non-special projections test the intrinsic version, independent of the
    # near-range hypothesis in the theorem's application.
    max_violation = 0.0
    for k in range(20):
        M = rng.normal(size=(9, 7))
        V, _ = np.linalg.qr(rng.normal(size=(9, 3)))
        P = V@V.T
        Z, alpha, W, s = volume_data(M)
        l = np.clip(np.diag(P), 0, 1)
        rhs = np.sqrt(l) + math.sqrt(3)*op((np.eye(9)-P)@M)/s[2]*np.sqrt(1-l)
        violation = float(np.max(np.sqrt(alpha)-rhs))
        assert violation < 1e-11
        max_violation = max(max_violation, violation)
    out["general_projection_checks"] = {"count": 20, "maximum_positive_violation": max_violation}

    n, m = 256, 128
    H = hadamard(n)
    U = hadamard(m)[:, :3]/math.sqrt(m)
    R = np.vstack([U,U])/math.sqrt(2)
    J = np.diag([1.,1.,-1.])
    A0 = 2*R@J@R.T
    eta = 1.0/16
    A = A0 + eta*H/math.sqrt(n)
    eig = np.linalg.eigvalsh(A)
    abs_eig = np.sort(abs(eig))[::-1]
    diag = np.diag(A)
    pairdet = diag[:,None]*diag[None,:]-A*A
    upper = pairdet[np.triu_indices(n,1)]
    M0=U@J@U.T
    E=(A-A0)[:m,m:]
    Z, alpha, _, s = volume_data(A[:m,m:])
    assert abs_eig[2] >= 31/16-1e-11
    assert abs_eig[3] <= 1/16+1e-11
    assert abs_eig[-1] > 1e-8
    assert max(abs(diag)) < 1/64
    assert max(abs(upper)) < 1/64
    assert op(E) <= eta+1e-12
    assert max(alpha) < 2/3
    out["no_pivot_family"] = {"n":n, "tau":1/64, "eta":eta, "minimum_absolute_eigenvalue":float(abs_eig[-1]), "third_absolute_eigenvalue":float(abs_eig[2]), "fourth_absolute_eigenvalue":float(abs_eig[3]), "max_absolute_diagonal":float(max(abs(diag))), "max_absolute_pair_determinant":float(max(abs(upper))), "cross_noise_op_norm":op(E), "cross_s3":float(s[2]), "max_cross_volume_marginal":float(max(alpha)), "full_rank_at_tested_eta":True}
    alpha_gate=(1+math.sqrt(3)/15)**2/2
    prefactor=24*math.sqrt(3)*math.e/5
    assert alpha_gate < 2/3
    assert prefactor < 23
    out["constants"]={"proved_upper_marginal":alpha_gate,"allowed_marginal":2/3,"density_prefactor":prefactor}
    text=json.dumps(out,indent=2)+"\n"
    Path(__file__).with_name("check_results.json").write_text(text,encoding="utf-8")
    print(json.dumps({"status":out["status"], "volume_marginals":out["volume_marginals"], "perturbation_cases":len(cases), "no_pivot_family":out["no_pivot_family"], "constants":out["constants"]},indent=2))

if __name__ == "__main__":
    main()
