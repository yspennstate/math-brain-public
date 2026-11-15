#!/usr/bin/env python3
"""Bounded numerical checks of PROOF.md; these checks are not the proof."""
import os

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import warnings

warnings.simplefilter("error", RuntimeWarning)

signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()

import mpmath as mp
import numpy as np

mp.mp.dps = 60


def kernel(z, gamma):
    if gamma == math.pi / 2:
        return np.zeros_like(z)
    return math.sin(2 * gamma) / (2 * math.pi *
                                       (np.cosh(z) - math.cos(2 * gamma)))


def kernel_prime(z, gamma):
    if gamma == math.pi / 2:
        return np.zeros_like(z)
    return (-math.sin(2 * gamma) * np.sinh(z) /
            (2 * math.pi * (np.cosh(z) - math.cos(2 * gamma)) ** 2))


def quadrature(B, gamma, intervals):
    assert 4 <= intervals <= 192 and intervals % 2 == 0
    r = np.linspace(-1.0, 1.0, intervals + 1)
    w = np.ones(intervals + 1)
    w[1:-1:2] = 4
    w[2:-1:2] = 2
    w *= 2 / (3 * intervals)
    d = r[:, None] - r[None, :]
    kval = kernel(B * d, gamma)
    mat = np.eye(len(r)) - B * kval * w[None, :]
    rho = np.linalg.solve(mat, np.ones(len(r)))
    derivative = (kval + B * d * kernel_prime(B * d, gamma)) * w[None, :]
    rho_B = np.linalg.solve(mat, np.sum(derivative * rho[None, :], axis=1))
    return r, w, mat, rho, rho_B


def A_pair(z, gamma):
    den_A = np.cosh(z) + math.cos(gamma)
    A = math.sin(gamma) / (2 * math.pi * den_A)
    Ap = -math.sin(gamma) * np.sinh(z) / (2 * math.pi * den_A ** 2)
    return A, Ap


def L_pair(z, gamma, u):
    delta = math.pi - gamma
    T = delta - u
    h = math.pi / delta
    den_L = np.cosh(z) - math.cos(T)
    den_h = np.cosh(h * z) - math.cos(h * T)
    alpha = math.sin(T) / (2 * math.pi)
    beta = math.sin(h * T) / (2 * delta)
    L = alpha / den_L - beta / den_h
    Lp = -alpha * np.sinh(z) / den_L ** 2 + beta * h * np.sinh(h*z) / den_h ** 2
    return L, Lp


def scalar_determinant(matrix):
    """Partial-pivot scalar elimination, separate from numpy's linear solver."""
    rows = [[complex(v) for v in row] for row in matrix]
    result = 1 + 0j
    for j in range(len(rows)):
        pivot = max(range(j,len(rows)), key=lambda k: abs(rows[k][j]))
        if pivot != j:
            rows[j],rows[pivot] = rows[pivot],rows[j]
            result = -result
        v = rows[j][j]
        assert abs(v) > 1e-15
        result *= v
        for k in range(j+1,len(rows)):
            factor = rows[k][j]/v
            for ell in range(j+1,len(rows)):
                rows[k][ell] -= factor*rows[j][ell]
    return result


def coefficients(B, gamma, u, theta, intervals=64):
    r, w, mat, rho, rho_B = quadrature(B, gamma, intervals)
    zp = B*r + 1j*(theta-u)
    zq = B*r + 1j*(theta+u)
    zl = B*r + 1j*theta
    p, pp = A_pair(zp, gamma)
    q, qp = A_pair(zq, gamma)
    ell, ellp = L_pair(zl, gamma, u)
    vals = []
    for f, fp in ((p, pp), (q, qp), (ell, ellp)):
        value = B * np.sum(w*rho*f)
        db = np.sum(w*((rho+B*rho_B)*f+B*rho*r*fp))
        dt = B * np.sum(w*rho*1j*fp)
        assert max(abs(value.imag), abs(db.imag), abs(dt.imag)) < 1e-9
        vals.append((value.real, db.real, dt.real))
    return np.array(vals)


def critical_pair(B, gamma, u, theta, intervals=64):
    vals = coefficients(B, gamma, u, theta, intervals)
    matrix = vals[:2, 1:].T
    return np.linalg.solve(matrix, vals[2, 1:])


def envelope(gamma, u, theta):
    g, v, t = map(mp.mpf, (gamma, u, theta))
    delta = mp.pi-g
    T = delta-v
    def A(t):
        return mp.sin(g)/(2*mp.pi*(mp.cos(t)+mp.cos(g)))
    def ell(t):
        return (mp.sin(T)/(2*mp.pi*(mp.cos(t)-mp.cos(T))) -
                mp.sin(mp.pi*T/delta)/
                (2*delta*(mp.cos(mp.pi*t/delta)-mp.cos(mp.pi*T/delta))))
    av = [mp.diff(lambda s: A(s-v), t, j) for j in range(4)]
    bv = [mp.diff(lambda s: A(s+v), t, j) for j in range(4)]
    ev = [mp.diff(ell, t, j) for j in range(4)]
    W = av[0]*bv[1]-av[1]*bv[0]
    assert W > 0
    x = (ev[0]*bv[1]-ev[1]*bv[0])/W
    y = (av[0]*ev[1]-av[1]*ev[0])/W
    C = x*av[2]+y*bv[2]-ev[2]
    D = x*av[3]+y*bv[3]-ev[3]
    x2 = (3*C*bv[1]-D*bv[0])/(6*W)
    y2 = (av[0]*D-3*av[1]*C)/(6*W)
    # Independent moment equations (16), solved without Cramer's formula.
    independent = mp.lu_solve(mp.matrix([[av[0],bv[0]],[av[1],bv[1]]]),
                              mp.matrix([C/2,D/6]))
    assert abs(x2-independent[0])+abs(y2-independent[1]) < mp.mpf("1e-45")
    return np.array([float(x), float(y)]), np.array([float(x2), float(y2)]), float(W)


results = {"mass_checks": [], "determinant_checks": [], "branch_checks": [],
           "exact_free_fermion_checks": []}
for gstr in ("0.02", "0.4", str(math.pi/3), "2.4", str(math.pi-0.02)):
    g = mp.mpf(gstr)
    kfun = lambda z: mp.sin(2*g)/(2*mp.pi*(mp.cosh(z)-mp.cos(2*g)))
    mass = mp.quad(kfun, [-mp.inf, 0, mp.inf])
    # A second numerical integration after tanh substitution.
    mass_t = mp.quad(lambda t: mp.sin(2*g)/(2*mp.pi*(
        mp.sin(g)**2+mp.cos(g)**2*t*t)), [-1,0,1])
    target = 1-2*g/mp.pi
    assert abs(mass-target) < mp.mpf("1e-45")
    assert abs(mass_t-target) < mp.mpf("1e-45")
    results["mass_checks"].append({"gamma": float(g), "signed_mass": float(mass),
                                     "absolute_error": float(abs(mass-target))})

for gamma in (0.4, math.pi/2, 2.4):
    B = 0.7
    r, w, mat, rho, _ = quadrature(B, gamma, 64)
    s = B*r
    f = 1+0.3j*s+0.2*s*s+0.07*s**4
    direct = B*np.sum(w*rho*f)
    U = np.broadcast_to(B*w*f, mat.shape)
    quotient = scalar_determinant(mat+U)/scalar_determinant(mat)-1
    error = abs(direct-quotient)
    assert error < 1e-10
    assert abs(direct.imag) < 1e-12
    if gamma < math.pi/2:
        assert min(rho) >= 1 and max(rho) <= math.pi/(2*gamma)
    results["determinant_checks"].append({"gamma": gamma, "B": B,
        "D": float(direct.real), "determinant_vs_resolvent_error": float(error)})

cases = [(0.02,0.35,0.4),(0.4,0.3,-0.4),(0.4,0.5,0.0),
         (0.4,0.75,0.3),(math.pi/3,0.4,0.2),(math.pi/2,0.5,0.0),
         (2.4,0.3,-0.2),(math.pi-0.02,0.7,0.25)]
epsilons = [0.04,0.02,0.01,0.005]
for gamma, fraction_u, fraction_theta in cases:
    delta = math.pi-gamma
    u = fraction_u*delta
    T = delta-u
    theta = fraction_theta*T
    scale = min(gamma, delta, T-abs(theta),
                delta-abs(theta-u), delta-abs(theta+u))
    base, predicted, W = envelope(gamma,u,theta)
    target = scale**2*predicted
    values = []
    for eps in epsilons:
        B = scale*eps
        pair = critical_pair(B,gamma,u,theta)
        values.append((pair-base)/eps**2)
    extrapolated = 2*values[-1]-values[-2]
    error = float(max(abs(extrapolated-target)))
    assert error < 3e-5*max(1,float(max(abs(target))))
    B = scale*epsilons[0]
    p64 = critical_pair(B,gamma,u,theta,64)
    p128 = critical_pair(B,gamma,u,theta,128)
    refinement = float(max(abs(p64-p128)))
    assert refinement < 1e-8
    # Check analytic B and theta derivatives with independent finite differences.
    vals = coefficients(B,gamma,u,theta)
    weights = np.array([p64[0],p64[1],-1])
    h = B*1e-4
    db_fd = ((coefficients(B+h,gamma,u,theta)[:,0] -
              coefficients(B-h,gamma,u,theta)[:,0]) @ weights)/(2*h)
    htheta = scale*1e-5
    dt_fd = ((coefficients(B,gamma,u,theta+htheta)[:,0] -
              coefficients(B,gamma,u,theta-htheta)[:,0]) @ weights)/(2*htheta)
    db_error = abs(db_fd-vals[:,1]@weights)
    dt_error = abs(dt_fd-vals[:,2]@weights)
    assert db_error < 2e-6 and dt_error < 2e-6
    row = {"gamma":gamma,"u_over_delta":fraction_u,"theta_over_T":fraction_theta,
           "W":W,"scale":scale,"predicted_scaled_B2":target.tolist(),
           "observed_scaled_B2": [v.tolist() for v in values],
           "extrapolation_error":error,"quadrature_refinement_error":refinement,
           "B_derivative_fd_error":float(db_error),
           "theta_derivative_fd_error":float(dt_error)}
    results["branch_checks"].append(row)
    print("branch gamma=%.8g u/delta=%.2f theta/T=%+.2f B2_error=%.3g refinement=%.3g" %
          (gamma,fraction_u,fraction_theta,error,refinement))

base, quadratic, _ = envelope(math.pi/2,math.pi/4,0.0)
assert max(abs(base-(0.5-1/(2*math.sqrt(2))))) < 1e-14
assert max(abs(quadratic-1/(4*math.sqrt(2)))) < 1e-14
for B in (0.01,0.2,0.7):
    pair = critical_pair(B,math.pi/2,math.pi/4,0.0,128)
    exact = 0.5-1/(2*math.sqrt(2)*math.cosh(B))
    error = float(max(abs(pair-exact)))
    assert error < 2e-9
    results["exact_free_fermion_checks"].append({"B":B,"exact":exact,
                                                "absolute_error":error})

usage = resource.getrusage(resource.RUSAGE_SELF)
rss_bytes = usage.ru_maxrss if sys.platform == "darwin" else usage.ru_maxrss*1024
assert rss_bytes < 1024**3
results["resources"] = {"elapsed_seconds":time.monotonic()-started,
    "peak_rss_MiB":rss_bytes/1024**2,"nice":os.getpriority(os.PRIO_PROCESS,0),
    "maximum_matrix_dimension":129,"thread_environment":{
        key:os.environ[key] for key in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS",
                                       "VECLIB_MAXIMUM_THREADS")}}
Path(__file__).with_name("verification.json").write_text(json.dumps(results,indent=2)+"\n")
print("mass checks: 5; determinant/resolvent checks: 3; local branch checks: 8")
print("exact free-fermion checks: 3; max error %.3g" %
      max(row["absolute_error"] for row in results["exact_free_fermion_checks"]))
print("PASS " + json.dumps(results["resources"],sort_keys=True))
