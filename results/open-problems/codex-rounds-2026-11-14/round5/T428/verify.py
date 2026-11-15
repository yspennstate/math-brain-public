"""Scalar checks for PROOF.md; no discretized operator-convergence claim.

All outputs are saved beside this script. Only scalar mpmath arithmetic is
used, without arrays, subprocesses, workers, GPUs or numerical libraries.
"""

import ctypes
import json
import os
from pathlib import Path
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
THREAD_KEYS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
)
assert all(os.environ.get(key) == "1" for key in THREAD_KEYS)
libc = ctypes.CDLL(None, use_errno=True)
libc.getpriority.argtypes = [ctypes.c_int, ctypes.c_uint]
libc.getpriority.restype = ctypes.c_int
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
priority_errno = ctypes.get_errno()
assert priority_errno == 0 and priority >= 15, (priority, priority_errno)

import mpmath as mp

mp.mp.dps = 45
started = time.monotonic()
TOL = mp.mpf("1e-32")


def number(value):
    return mp.nstr(value, 36)


def close(left, right):
    error = abs(left - right)
    assert error < TOL, (number(left), number(right), number(error))
    return number(error)


# Uniform envelope moments, with the specific Gaussian-family envelope.
C = (4*mp.exp(mp.mpf("0.5")) + mp.mpf("1.5")*mp.e)/(2*mp.pi)
a = mp.mpf(1)
moment_rows = []
for k in [0, 1, 2, 4]:
    direct = 2*mp.pi*C*mp.quad(
        lambda r: r**(k+1)*mp.exp(-a*r), [0, 1, mp.inf])
    formula = 2*mp.pi*C*mp.factorial(k+1)/a**(k+2)
    moment_rows.append({"k": k, "formula": number(formula),
                        "absolute_error": close(direct, formula)})


# Independent logarithmic Gaussian moment, integrated in radial coordinate.
# If Z has covariance v Id, |Z|^2/(2v) has density exp(-w).
def gaussian_log_constant(v):
    return mp.quad(
        lambda w: mp.exp(-w)*(mp.log(4)-mp.euler-mp.log(2*v*w)),
        [0, 1, mp.inf])


g2, g3, g4 = [gaussian_log_constant(mp.mpf(v)) for v in [2, 3, 4]]
family_rows = []
overlap_rows = []
projection_rows = []

for b_text in ["0", "0.25", "1", "3"]:
    b = mp.mpf(b_text)
    weights = [(mp.mpf(1), (1+b)**2),
               (mp.mpf("1.5"), -2*b*(1+b)),
               (mp.mpf(2), b*b)]
    closed = 2*b*(1+b)*mp.log(mp.mpf("1.5"))-b*b*mp.log(2)
    log_route = (1+b)**2*g2-2*b*(1+b)*g3+b*b*g4

    def heat(t):
        return sum(weight/(t+shift) for shift, weight in weights)

    # Since the weights sum to 1, this is H(t)-1/t without subtracting
    # two quantities of order 1/t at infinity.
    def tail(t):
        return -sum(weight*shift/(t*(t+shift))
                    for shift, weight in weights)

    heat_route = mp.quad(heat, [0, 1]) + mp.quad(tail, [1, mp.inf])
    family_rows.append({"b": b_text, "4pi_I": number(closed),
                        "log_moment_error": close(log_route, closed),
                        "heat_integral_error": close(heat_route, closed)})

    # Exact projection norm: mass=1, and the negative tail has mass
    # b^2/[4(1+b)]. Verify by radial absolute-value integration.
    def radial_density(r):
        return r*((1+b)*mp.exp(-r*r/2)-b*mp.exp(-r*r/4)/2)

    if b:
        crossing = mp.sqrt(4*mp.log(2*(1+b)/b))
        absolute_mass = mp.quad(radial_density, [0, crossing]) - mp.quad(
            radial_density, [crossing, mp.inf])
    else:
        crossing = None
        absolute_mass = mp.quad(radial_density, [0, 1, mp.inf])
    norm_formula = 1+b*b/(2*(1+b))
    projection_rows.append({"b": b_text, "projection_norm": number(norm_formula),
                            "radial_error": close(absolute_mass, norm_formula)})

    for n_int in [100, 10000, 1000000]:
        n = mp.mpf(n_int)
        sharp = sum(weight*mp.log1p(n/shift) for shift, weight in weights)
        sharp_direct = mp.quad(heat, [0, 1, n])
        sharp_error = abs(sharp-mp.log(n)-closed)
        sharp_bound = sum(abs(weight)*shift for shift, weight in weights)/n
        assert sharp_error <= sharp_bound <= 70/n
        z = mp.mpf(2)
        damped = sum(weight*mp.exp(z*shift/n)*mp.e1(z*shift/n)
                     for shift, weight in weights)
        damped_direct = mp.quad(
            lambda s: mp.exp(-z*s)*sum(weight/(s+shift/n)
                                     for shift, weight in weights),
            [0, 1/n, 1, mp.inf])
        target = closed-mp.euler-mp.log(z)
        overlap_rows.append({
            "b": b_text, "N": n_int,
            "sharp_direct_error": close(sharp_direct, sharp),
            "sharp_finite_part_error": number(sharp_error),
            "uniform_sharp_bound_70_over_N": number(70/n),
            "damped_direct_error": close(damped_direct, damped),
            "damped_finite_part_error": number(abs(damped-mp.log(n)-target)),
        })

assert close(mp.mpf(family_rows[2]["4pi_I"]), mp.log(mp.mpf(81)/32))


# Check the lower-mass obstruction exactly and by radial integration.
mass_rows = []
for delta_text in ["1", "0.1", "0.01", "0.001"]:
    delta = mp.mpf(delta_text)
    coeff = 1+delta
    crossing = mp.sqrt(4*mp.log(2*coeff))

    def radial(r):
        return r*(coeff*mp.exp(-r*r/2)-mp.exp(-r*r/4)/2)

    absolute_mass = mp.quad(radial, [0, crossing])-mp.quad(
        radial, [crossing, mp.inf])
    exact_mass = delta+1/(2*(1+delta))
    mass_rows.append({"delta": delta_text,
                      "absolute_mass": number(absolute_mass),
                      "projection_norm": number(exact_mass/delta),
                      "absolute_error": close(absolute_mass, exact_mass)})


# Recheck the previous time-density normalization in two independent
# variables. This does not test the operator theorem numerically.
def gamma_density(t, zstar):
    def integrand(s):
        if not s:
            return mp.mpf(0)
        return mp.exp(s*mp.log(zstar*t)-mp.loggamma(s))/t
    return mp.quad(integrand, [0, 1, 4, 16, mp.inf])


def branch_density(t, zstar):
    def integrand(r):
        if not r:
            return mp.mpf(0)
        return mp.exp(-r*t)/(mp.log(r/zstar)**2+mp.pi**2)
    return zstar*mp.exp(zstar*t)+mp.quad(
        integrand, [0, zstar, max(2*zstar, 1/t), mp.inf])


density_rows = []
for theta_text, t_text in [("0", "0.05"), ("0", "1"),
                           ("0.7", "0.05"), ("0.7", "1")]:
    zstar = mp.exp(mp.mpf(theta_text)-mp.euler)
    t = mp.mpf(t_text)
    left = gamma_density(t, zstar)
    right = branch_density(t, zstar)
    density_rows.append({"theta": theta_text, "t": t_text,
                         "gamma_density": number(left),
                         "absolute_error": close(left, right)})

# A discontinuous choice of profiles still belongs to one bounded class.
moving_sequence = [{"N": n, "b": b, "mass": "1"}
                   for n, b in [(100, "0.25"), (10000, "3"),
                                (1000000, "0.25"), (100000000, "3")]]

rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss_raw if sys.platform == "darwin" else rss_raw*1024
assert rss_bytes < 1_000_000_000
output = {
    "precision_digits": mp.mp.dps,
    "assertion_tolerance": str(TOL),
    "gaussian_family_envelope": {"C": number(C), "a": "1", "m_0": "1"},
    "moment_checks": moment_rows,
    "signed_family_constant_checks": family_rows,
    "projection_norm_checks": projection_rows,
    "finite_N_overlap_checks": overlap_rows,
    "lower_mass_obstruction_checks": mass_rows,
    "previous_time_density_checks": density_rows,
    "example_nonconvergent_profile_choices": moving_sequence,
    "getpriority": priority,
    "getpriority_errno": priority_errno,
    "thread_environment": {key: os.environ[key] for key in THREAD_KEYS},
    "max_rss_bytes": rss_bytes,
    "wall_seconds": round(time.monotonic()-started, 3),
    "scope": "Scalar checks only; no numerical proof of a uniform operator limit.",
}
serialized = json.dumps(output, indent=2)+"\n"
Path(__file__).with_name("verification.json").write_text(serialized)
print(serialized, end="")
