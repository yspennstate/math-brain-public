"""Scalar normalization checks for the Brownian signed resolvent note.

No spatial discretization or numerical operator-convergence claim is made.
All output files are written beside this script.
"""

import ctypes
import json
import os
from pathlib import Path
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))

THREAD_KEYS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
)
assert all(os.environ.get(k) == "1" for k in THREAD_KEYS)

import mpmath as mp

mp.mp.dps = 45
started = time.monotonic()
c = 1 / (4 * mp.pi)
tol = mp.mpf("1e-34")


def number(x):
    if isinstance(x, (mp.mpc, complex)):
        return {"real": mp.nstr(x.real, 32), "imag": mp.nstr(x.imag, 32)}
    return mp.nstr(x, 32)


def close(x, y):
    error = abs(x - y)
    assert error < tol, (number(x), number(y), number(error))
    return number(error)


# Recheck the previous result via a finite-interval integral, rather than
# the old script's semi-infinite heat-overlap quadrature.
# For independent Gaussians of variances s,t, W=|X-Y|^2/(2(s+t))
# is exponential. Substitute W=-log y to integrate on y in (0,1).
def gaussian_g(s):
    return c * mp.quad(
        lambda y: mp.log(4) - mp.euler - mp.log(2 * s * (-mp.log(y))),
        [0, mp.mpf("0.5"), 1],
    )


old_integral = 4 * gaussian_g(2) - 4 * gaussian_g(3) + gaussian_g(4)
old_closed = c * mp.log(mp.mpf(81) / 32)
old_check = {
    "I_finite_interval_gaussian_quadrature": number(old_integral),
    "I_closed": number(old_closed),
    "absolute_error": close(old_integral, old_closed),
    "4pi_I": number(old_closed / c),
}


# The gamma shift: direct, convergent time-cutoff difference, including
# genuinely complex parameters. expm1 avoids loss of digits at s=0.
def cutoff_difference(z):
    return mp.quad(lambda s: mp.expm1(-z * s) / s, [0, 1]) + mp.quad(
        lambda s: mp.exp(-z * s) / s, [1, mp.inf]
    )


gamma_rows = []
for z in [mp.mpf("0.5"), mp.mpf(1), mp.mpf(3),
          mp.mpc("0.6", "0.8"), mp.mpc(2, 1)]:
    direct = cutoff_difference(z)
    target = -mp.euler - mp.log(z)
    gamma_rows.append({"z": number(z), "direct": number(direct),
                       "target": number(target),
                       "absolute_error": close(direct, target)})


# Heat-kernel normalization: numerical time integral vs the Bessel formula.
bessel_rows = []
for r, n, z in [(mp.mpf("0.7"), 13, mp.mpf(2)),
                (mp.mpf(2), 1000, mp.mpf("0.5")),
                (mp.mpf("1.3"), 100, mp.mpc(2, 1))]:
    direct = c * mp.quad(
        lambda t: mp.exp(-z * t / n - r*r / (4*t)) / t,
        [0, 1, n, mp.inf],
    )
    bessel = 2 * c * mp.besselk(0, r * mp.sqrt(z / n))
    bessel_rows.append({"r": number(r), "N": n, "z": number(z),
                        "direct": number(direct),
                        "bessel": number(bessel),
                        "absolute_error": close(direct, bessel)})


# Finite-N exponential Gaussian overlap: two exact routes, plus the
# asymptotic finite part from the proof. The direct integral uses
# t=N*s to sample the macroscopic damping scale.
terms = [(mp.mpf(1), 4), (mp.mpf("1.5"), -4), (mp.mpf(2), 1)]


def scaled_overlap(s, n):
    return sum(weight / (s + b/n) for b, weight in terms)


overlap_rows = []
for z in [mp.mpf("0.5"), mp.mpf(2), mp.mpc(2, 1)]:
    previous_error = None
    for n_int in [100, 10000, 1000000]:
        n = mp.mpf(n_int)
        direct = mp.quad(lambda s: mp.exp(-z*s) * scaled_overlap(s, n),
                         [0, 1/n, 1, mp.inf])
        exact = sum(weight * mp.exp(z*b/n) * mp.e1(z*b/n)
                    for b, weight in terms)
        limit = mp.log(mp.mpf(81)/32) - mp.euler - mp.log(z)
        finite_part = exact - mp.log(n)
        error = abs(finite_part - limit)
        if previous_error is not None:
            assert error < previous_error
        previous_error = error
        overlap_rows.append({
            "z": number(z), "N": n_int,
            "direct_vs_exact_error": close(direct, exact),
            "finite_part_4pi": number(finite_part),
            "limiting_finite_part_4pi": number(limit),
            "asymptotic_absolute_error": number(error),
        })


# Test the spatial error bound in (17) with an explicit valid constant.
# On s<=1, |w_z(s)|<=|z|s; on s>1, use exp(-Re(z)s).
# The tail integral is <= exp(-Re(z))/Re(z), so this C is conservative.
remainder_rows = []
for z in [mp.mpf("0.5"), mp.mpc(2, 1)]:
    constant = c * (2*abs(z) + mp.exp(-z.real)/z.real)
    for r in [mp.mpf("0.01"), mp.mpf(2), mp.mpf(50)]:
        n = mp.mpf(1000)
        q = r*r/(4*n)
        transformed = 2*c*mp.besselk(0, r*mp.sqrt(z/n))
        sharp = c*mp.e1(q)
        error = abs(transformed-sharp-c*(-mp.euler-mp.log(z)))
        bound = constant*mp.sqrt(q)
        assert error <= bound
        remainder_rows.append({"z": number(z), "r": number(r),
                                "N": int(n), "error": number(error),
                                "bound": number(bound)})

libc = ctypes.CDLL(None, use_errno=True)
libc.getpriority.argtypes = [ctypes.c_int, ctypes.c_uint]
libc.getpriority.restype = ctypes.c_int
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
priority_errno = ctypes.get_errno()
assert priority_errno == 0 and priority >= 15, (priority, priority_errno)

rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss_raw if sys.platform == "darwin" else rss_raw * 1024
assert rss_bytes < 1_000_000_000

output = {
    "precision_digits": mp.mp.dps,
    "assertion_tolerance": str(tol),
    "earlier_result_check": old_check,
    "gamma_shift_checks": gamma_rows,
    "heat_kernel_bessel_checks": bessel_rows,
    "exponential_overlap_checks": overlap_rows,
    "spatial_remainder_checks": remainder_rows,
    "getpriority": priority,
    "getpriority_errno": priority_errno,
    "thread_environment": {k: os.environ.get(k) for k in THREAD_KEYS},
    "max_rss_bytes": rss_bytes,
    "wall_seconds": round(time.monotonic()-started, 3),
    "scope": "Scalar constant and remainder checks; not an operator discretization.",
}
serialized = json.dumps(output, indent=2) + "\n"
Path(__file__).with_name("verification.json").write_text(serialized)
print(serialized, end="")
