"""Independent constant checks for PROOF.md; no simulation or spectral claim."""

import ctypes
import json
import os
from pathlib import Path
import resource
import time

# This workload uses scalar quadrature only; report actual RSS below.
# macOS rejected a 900 MB RLIMIT_AS setting, so do not claim that limit.
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))

import mpmath as mp

mp.mp.dps = 45
started = time.monotonic()
c = 1 / (4 * mp.pi)


def serial(value):
    return mp.nstr(value, 38)


def check_close(left, right, tol=mp.mpf("1e-36")):
    err = abs(left - right)
    if err >= tol:
        raise AssertionError((serial(left), serial(right), serial(err)))
    return serial(err)


# This route uses a logarithmic Gaussian moment, not the heat overlap.
def log_moment(variance):
    # With W=|Z|^2/(2 variance), W has density exp(-w).
    return mp.quad(
        lambda w: mp.exp(-w) * mp.log(2 * variance * w) / 2,
        [0, 1, mp.inf],
    )


terms = [(mp.mpf(1), mp.mpf(2)), (mp.mpf(2), mp.mpf(-1))]
i_moment = mp.mpf(0)
for s, a_s in terms:
    for t, a_t in terms:
        i_moment += a_s * a_t * c * (
            mp.log(4) - mp.euler - 2 * log_moment(s + t)
        )

i_closed = c * mp.log(mp.mpf(81) / 32)


def heat_overlap(t):
    return c * (4 / (t + 1) - 4 / (t + mp.mpf("1.5")) + 1 / (t + 2))


def renormalized_tail(t):
    # Algebraic simplification of H(t)-c/t avoids subtracting near equals.
    # The numerator of 4/(t+1)-4/(t+3/2)+1/(t+2)-1/t is -t-3.
    return c * (-t - 3) / (t * (t + 1) * (t + mp.mpf("1.5")) * (t + 2))


for t in [mp.mpf("0.25"), mp.mpf(1), mp.mpf(7)]:
    check_close(renormalized_tail(t), heat_overlap(t) - c / t)

i_heat = mp.quad(heat_overlap, [0, 1]) + mp.quad(
    renormalized_tail, [1, mp.inf]
)
checks = {
    "moment_vs_closed_abs_error": check_close(i_moment, i_closed),
    "heat_vs_closed_abs_error": check_close(i_heat, i_closed),
}

# Independently integrate the time kernel, then compare with E_1.
kernel_rows = []
for r, n in [(mp.mpf("0.7"), mp.mpf(13)), (mp.mpf(2), mp.mpf(1000))]:
    q = r**2 / 4
    direct = c * mp.quad(lambda t: mp.exp(-q / t) / t, [0, 1, n])
    exponential_integral = c * mp.e1(q / n)
    g = c * (mp.log(4) - mp.euler - 2 * mp.log(r))
    rem = direct - c * mp.log(n) - g
    upper = r**2 / (16 * mp.pi * n)
    if not 0 <= rem <= upper:
        raise AssertionError("Heat remainder bound failed")
    kernel_rows.append({
        "r": serial(r), "N": serial(n),
        "direct_vs_E1_error": check_close(direct, exponential_integral),
        "remainder": serial(rem), "upper_bound": serial(upper),
    })

finite_rows = []
for n in [10, 100, 1000, 10000]:
    n_mp = mp.mpf(n)
    exact = c * (4 * mp.log1p(n_mp) - 4 * mp.log1p(2 * n_mp / 3)
                 + mp.log1p(n_mp / 2))
    numeric = mp.quad(heat_overlap, [0, 1, n_mp])
    check_close(exact, numeric)
    finite_rows.append({
        "N": n,
        "renormalized_heat_overlap": serial(exact - c * mp.log(n_mp)),
        "error_from_I": serial(exact - c * mp.log(n_mp) - i_closed),
    })

libc = ctypes.CDLL(None, use_errno=True)
libc.getpriority.argtypes = [ctypes.c_int, ctypes.c_uint]
libc.getpriority.restype = ctypes.c_int
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
priority_errno = ctypes.get_errno()
result = {
    "precision_digits": mp.mp.dps,
    "I_closed": serial(i_closed),
    "I_log_moment_quadrature": serial(i_moment),
    "I_heat_overlap_quadrature": serial(i_heat),
    "tuning_shift_4piI": serial(4 * mp.pi * i_closed),
    "checks": checks,
    "heat_kernel_checks": kernel_rows,
    "finite_N_overlap_checks": finite_rows,
    "getpriority": priority,
    "getpriority_errno": priority_errno,
    "thread_environment": {key: os.environ.get(key) for key in [
        "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS"]},
    "wall_seconds": round(time.monotonic() - started, 3),
    "max_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "scope": "Constant checks only; no numerical proof of an operator limit.",
}
Path(__file__).with_name("verification.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result, indent=2))
