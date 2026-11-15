"""Scalar checks for the signed Brownian time-limit theorem.

This checks normalizations, not the infinite-dimensional operator theorem.
Only this directory receives output; no arrays or workers are used.
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

mp.mp.dps = 40
started = time.monotonic()
TOL = mp.mpf("1e-28")


def serial(x):
    return mp.nstr(x, 32)


def close(x, y):
    error = abs(x-y)
    assert error < TOL, (serial(x), serial(y), serial(error))
    return serial(error)


# Independent check of the previous finite-part constant: integrate the
# rational overlap after the substitution t=x/(1-x), rather than the
# old scripts' logarithmic Gaussian quadrature.
c = 1/(4*mp.pi)


def overlap(t):
    return 4/(t+1)-4/(t+mp.mpf("1.5"))+1/(t+2)


def transformed_tail(x):
    # H(t)-1/t=(-t-3)/(t(t+1)(t+3/2)(t+2)); transform exactly.
    return -(3-2*x)*(1-x)/(x*(mp.mpf("1.5")-x/2)*(2-x))


old_constant = mp.quad(overlap, [0, 1]) + mp.quad(
    transformed_tail, [mp.mpf("0.5"), 1]
)
old_closed = mp.log(mp.mpf(81)/32)
old_result = {"4pi_I_quadrature": serial(old_constant),
              "4pi_I_closed": serial(old_closed),
              "absolute_error": close(old_constant, old_closed)}


# Gamma shift, independently through the same compactification t=x/(1-x).
gamma_rows = []
for z in [mp.mpf("0.6"), mp.mpf(1), mp.mpf("2.5")]:
    first = mp.quad(lambda s: mp.expm1(-z*s)/s, [0, 1])
    tail = mp.quad(lambda x: mp.exp(-z*x/(1-x))/(x*(1-x)),
                   [mp.mpf("0.5"), 1])
    target = -mp.euler-mp.log(z)
    gamma_rows.append({"z": serial(z), "quadrature": serial(first+tail),
                       "target": serial(target),
                       "absolute_error": close(first+tail, target)})


def density_gamma(t, zstar):
    logscale = mp.log(zstar*t)

    def integrand(s):
        if not s:
            return mp.mpf(0)
        return mp.exp(s*logscale-mp.loggamma(s))/t

    return mp.quad(integrand, [0, 1, 4, 16, mp.inf])


def density_branch(t, zstar):
    def integrand(r):
        if not r:
            return mp.mpf(0)
        return mp.exp(-r*t)/(mp.log(r/zstar)**2+mp.pi**2)

    cutoff = max(zstar*2, 1/t)
    return zstar*mp.exp(zstar*t) + mp.quad(
        integrand, [0, zstar, cutoff, mp.inf]
    )


# The two densities use different integration variables and derivations.
density_rows = []
monotonicity_rows = []
for theta_text in ["-1", "0", "0.7"]:
    theta = mp.mpf(theta_text)
    zstar = mp.exp(theta-mp.euler)
    b = 2*zstar
    previous = None
    for t_text in ["0.01", "0.2", "1", "3"]:
        t = mp.mpf(t_text)
        gamma_value = density_gamma(t, zstar)
        branch_value = density_branch(t, zstar)
        density_rows.append({
            "theta": theta_text, "t": t_text, "z_star": serial(zstar),
            "gamma_integral": serial(gamma_value),
            "pole_plus_branch": serial(branch_value),
            "absolute_error": close(gamma_value, branch_value),
        })
        damped = mp.exp(-b*t)*gamma_value
        if previous is not None:
            assert damped < previous
        previous = damped
        monotonicity_rows.append({"theta": theta_text, "t": t_text,
                                  "damped_density": serial(damped)})


# Check the keyhole transform without nesting quadrature. Under
# r=zstar exp(x), the branch transform has a logistic factor times
# 1/(x^2+pi^2); this captures the long logarithmic tail explicitly.
transform_rows = []
for ratio_text in ["1.2", "2", "5"]:
    ratio = mp.mpf(ratio_text)

    def transformed_branch(x):
        if x >= 0:
            factor = 1/(1+ratio*mp.exp(-x))
        else:
            expx = mp.exp(x)
            factor = expx/(ratio+expx)
        return factor/(x*x+mp.pi**2)

    branch = mp.quad(transformed_branch, [-mp.inf, -10, 0, 10, mp.inf])
    pole = 1/(ratio-1)
    target = 1/mp.log(ratio)
    transform_rows.append({
        "z_over_z_star": ratio_text,
        "pole_transform": serial(pole), "branch_transform": serial(branch),
        "sum": serial(pole+branch), "target": serial(target),
        "absolute_error": close(pole+branch, target),
    })


# Scaling independently removes the theta-dependent z_star.
scaling_rows = []
for zstar, t in [(mp.mpf("0.3"), mp.mpf("0.7")),
                 (mp.mpf("1.7"), mp.mpf("0.2"))]:
    left = density_gamma(t, zstar)
    right = zstar*density_branch(zstar*t, mp.mpf(1))
    scaling_rows.append({"z_star": serial(zstar), "t": serial(t),
                         "absolute_error": close(left, right)})

libc = ctypes.CDLL(None, use_errno=True)
libc.getpriority.argtypes = [ctypes.c_int, ctypes.c_uint]
libc.getpriority.restype = ctypes.c_int
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
priority_errno = ctypes.get_errno()
assert priority_errno == 0 and priority >= 15, (priority, priority_errno)
rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss_raw if sys.platform == "darwin" else rss_raw*1024
assert rss_bytes < 1_000_000_000

result = {
    "precision_digits": mp.mp.dps,
    "assertion_tolerance": str(TOL),
    "earlier_constant_check": old_result,
    "gamma_shift_checks": gamma_rows,
    "density_checks": density_rows,
    "damped_monotonicity_checks": monotonicity_rows,
    "branch_transform_checks": transform_rows,
    "scaling_checks": scaling_rows,
    "getpriority": priority,
    "getpriority_errno": priority_errno,
    "thread_environment": {k: os.environ[k] for k in THREAD_KEYS},
    "max_rss_bytes": rss_bytes,
    "wall_seconds": round(time.monotonic()-started, 3),
    "scope": "Scalar normalization checks, not a numerical operator proof.",
}
serialized = json.dumps(result, indent=2)+"\n"
Path(__file__).with_name("verification.json").write_text(serialized)
print(serialized, end="")
