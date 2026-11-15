"""Finite Toeplitz angle checks for D0037 (one BLAS thread, small memory).

Run: python3 code/checks.py
Writes data/finite_angles.csv, data/checks.json, data/conjugate_profile.csv,
and data/periodic_limits.csv.
Finite matrix correlations are lower bounds on rho-star, never upper bounds.
"""
import os

for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

import csv
import json
import math
from pathlib import Path
import resource
import time

import numpy as np
from scipy import linalg, special

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def angle(cov, s, t):
    """Whiten with Cholesky, then check against a generalized eigenvalue."""
    s, t = np.asarray(s), np.asarray(t)
    aa = cov(s[:, None] - s[None, :])
    bb = cov(t[:, None] - t[None, :])
    cc = cov(s[:, None] - t[None, :])
    la = linalg.cholesky(aa, lower=True)
    lb = linalg.cholesky(bb, lower=True)
    white = linalg.solve_triangular(la, cc, lower=True)
    white = linalg.solve_triangular(lb, white.T, lower=True).T
    sv = float(linalg.svdvals(white)[0])
    solved = linalg.cho_solve((lb, True), cc.T)
    assert np.all(np.isfinite(solved))
    # Explicit summation also avoids spurious floating-status warnings from
    # this host's NumPy matmul/Accelerate combination on small finite inputs.
    product = np.einsum("ik,kj->ij", cc, solved, optimize=False)
    eig = float(linalg.eigh(product, aa, eigvals_only=True, subset_by_index=[len(s)-1, len(s)-1])[0])
    ge = math.sqrt(max(eig, 0))
    if not np.isclose(sv, ge, atol=2e-10, rtol=2e-9):
        raise AssertionError((sv, ge))
    return sv, ge, float(np.linalg.eigvalsh(aa)[0]), float(np.linalg.eigvalsh(bb)[0])


def white_cov(k):
    return (np.asarray(k) == 0).astype(float)


def difference_cov(k):
    k = np.asarray(k)
    return 2.0*(k == 0) - (np.abs(k) == 1)


def step_cov(k, a=0.6):
    k = np.asarray(k)
    result = np.zeros_like(k, dtype=float)
    result[k == 0] = 1
    nz = k != 0
    # Integer parity avoids loss from sin(pi*k/2) at high integer arguments.
    odd = nz & (k % 2 != 0)
    result[odd] = (2*a/math.pi) * np.where(k[odd] % 4 == 1, 1., -1.) / k[odd]
    return result


def ar_cov(k, r=0.7):
    return r**np.abs(np.asarray(k))


def fractional_cov(k, alpha=0.5):
    """Exact Fourier coefficients of |1-exp(it)|**alpha, via recurrence.

    gamma_0=Gamma(alpha+1)/Gamma(alpha/2+1)^2;
    gamma_k/gamma_{k-1}=(k-1-alpha/2)/(k+alpha/2).
    """
    k = np.abs(np.asarray(k, dtype=int))
    tab = np.empty(int(k.max())+1)
    tab[0] = special.gamma(alpha+1)/special.gamma(alpha/2+1)**2
    for j in range(1, len(tab)):
        tab[j] = tab[j-1]*(j-1-alpha/2)/(j+alpha/2)
    return tab[k]


def sampled_covariance(f, count=65536):
    # Midpoint nodes avoid assigning an arbitrary finite value at t=0.
    ts = (np.arange(count)+0.5)*2*np.pi/count
    vals = f(ts)
    co = np.fft.fft(vals)/count
    phase = np.exp(-1j*np.pi*np.arange(count)/count)
    co = (co*phase).real
    return lambda k: co[np.abs(np.asarray(k, dtype=int))]


def slow_zero(ts, a=4.):
    ts = np.asarray(ts)
    result = np.zeros_like(ts, dtype=float)
    nz = ts != 0
    ll = np.log(a/(-np.expm1(1j*ts[nz])))
    result[nz] = math.log(a)/np.abs(ll)
    return result


def periodic_limit(f, width, gap):
    """Exact N->infinity Fejer limit for two shifted periodic block masks.

    S has width consecutive residues, followed by gap omitted residues;
    T is S shifted by p/2. For continuous f the formula is rigorous.
    """
    p = 2*(width+gap)
    mask = np.zeros(p)
    mask[:width] = 1
    df = np.fft.fft(mask)
    ts = 2*np.pi*np.arange(p)/p
    weights = f(ts)*np.abs(df)**2/p
    var = float(np.sum(weights))
    covariance = float(np.sum(weights*np.where(np.arange(p) % 2, -1, 1)))
    return var, covariance, abs(covariance)/var, 2*(var+covariance)


def run():
    start = time.time()
    rows = []
    models = {
        "white": white_cov,
        "difference": difference_cov,
        "positive_continuous_AR": ar_cov,
        "positive_step_a_0.6": step_cov,
        "fractional_zero_alpha_0.5": fractional_cov,
        "slow_zero_midpoint_65536": sampled_covariance(slow_zero),
    }
    for model, cov in models.items():
        for n in [1, 2, 4, 8, 16, 32]:
            for size in [16, 64, 128]:
                for geometry in ["past_future", "even_odd_halflines", "alternating_blocks"]:
                    if geometry == "past_future":
                        s = -np.arange(size)
                        t = n+np.arange(size)
                    elif geometry == "even_odd_halflines":
                        d = n//2
                        s = -2*np.arange(size)
                        t = 2*np.arange(size)+2*d+1
                    else:
                        width = max(1, size//4)
                        s = np.concatenate([2*j*(width+n-1)+np.arange(width) for j in range(4)])
                        t = np.concatenate([(2*j+1)*(width+n-1)+np.arange(width) for j in range(4)])
                    distance = int(np.min(np.abs(s[:, None]-t[None, :])))
                    assert distance >= n
                    value, ge, mina, minb = angle(cov, s, t)
                    rows.append(dict(model=model, n=n, size=len(s), geometry=geometry,
                                     distance=distance, rho_finite=value, rho_generalized=ge,
                                     min_eigen_A=mina, min_eigen_B=minb))
    with (DATA / "finite_angles.csv").open("w") as out:
        w = csv.DictWriter(out, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    periodic_rows=[]
    for model, f in {
        "difference": lambda t: 4*np.sin(t/2)**2,
        "fractional_zero_alpha_0.5": lambda t: (2*np.abs(np.sin(t/2)))**.5,
        "slow_zero": slow_zero,
    }.items():
        for n in [1,2,4,8,16,32]:
            for width in [16,64,256,1024,4096,16384]:
                var, covariance, rho, combined = periodic_limit(f,width,n-1)
                if model == "difference" and n >= 2:
                    assert rho < 1e-12
                periodic_rows.append(dict(model=model,n=n,width=width,period=2*(width+n-1),
                                          variance_per_period=var,covariance_per_period=covariance,
                                          rho_period_limit=rho,combined_variance_per_period=combined))
    with (DATA / "periodic_limits.csv").open("w") as out:
        w=csv.DictWriter(out,fieldnames=list(periodic_rows[0]))
        w.writeheader()
        w.writerows(periodic_rows)

    white_error = max(r["rho_finite"] for r in rows if r["model"] == "white")
    diff_gap_error = max(r["rho_finite"] for r in rows if r["model"] == "difference" and r["n"] >= 2)
    # For the difference model, use *interlaced* even and odd contiguous indices
    # for the exact lag-one formula, rather than the separated halflines above.
    explicit_diff = []
    for size in [16, 64, 128]:
        value, _, _, _ = angle(difference_cov, 2*np.arange(size), 2*np.arange(size)+1)
        exact = math.cos(math.pi/(2*size+1))
        assert abs(value-exact) < 1e-12
        explicit_diff.append(dict(size=size, rho_finite=value, exact=exact))
    # Two independent ways to verify Fourier sign/normalization for a smooth model.
    midpoint_ar = sampled_covariance(lambda t: (1-.7**2)/(1-1.4*np.cos(t)+.7**2))
    covariance_error = float(np.max(np.abs(midpoint_ar(np.arange(100))-ar_cov(np.arange(100)))))
    # The slow-zero quadrature is not a proof. Save its discretization discrepancy.
    slow_coarse = sampled_covariance(slow_zero, 32768)
    slow_fine = sampled_covariance(slow_zero, 65536)
    slow_difference = float(np.max(np.abs(slow_coarse(np.arange(5000))-slow_fine(np.arange(5000)))))
    assert white_error < 1e-14 and diff_gap_error < 1e-14 and covariance_error < 1e-12
    assert max(r["rho_finite"] for r in rows if r["model"] == "positive_step_a_0.6") < .6+1e-12
    checks = dict(nice=os.getpriority(os.PRIO_PROCESS, 0), blas_threads=1,
                  white_error=white_error, difference_lag_ge_2_error=diff_gap_error,
                  exact_difference_interlaced=explicit_diff,
                  largest_svd_eigen_discrepancy=max(abs(r["rho_finite"]-r["rho_generalized"]) for r in rows),
                  AR_midpoint_covariance_error=covariance_error,
                  slow_zero_covariance_grid_discrepancy=slow_difference,
                  matrix_rows=len(rows), elapsed_seconds=time.time()-start,
                  periodic_rows=len(periodic_rows),
                  maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  maxrss_unit="bytes on macOS; kilobytes on Linux",
                  note="Finite correlations are lower bounds; slow-zero FFT values are exploratory.")
    (DATA / "checks.json").write_text(json.dumps(checks, indent=2)+"\n")
    with (DATA / "conjugate_profile.csv").open("w") as out:
        w=csv.writer(out)
        w.writerow(["minus_log_t", "real_log_log", "continuous_v", "H_v", "f_slow_zero", "reciprocal"])
        for minus_log_t in [1,2,4,8,16,32,64,128,256,512]:
            t=math.exp(-minus_log_t)
            ll=np.log(4/(-np.expm1(1j*t)))
            ff=np.log(ll)
            hv=math.log(math.log(4))-ff.real
            w.writerow([minus_log_t, ff.real, ff.imag, hv, math.exp(hv), math.exp(-hv)])
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    run()
