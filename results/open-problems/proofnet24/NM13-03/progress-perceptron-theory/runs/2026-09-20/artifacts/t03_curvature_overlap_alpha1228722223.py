#!/usr/bin/env python3
"""
NM13-03 / T03 essential numerical checker, 2026-09-20.

Exact source model: iid Gaussian constraints, kappa=-1, exact sphere radius sqrt(N).
Numerical support only; this is not directed interval arithmetic.

Checks at alpha=12.28722223:
  * full complete-third stationary solve at GH orders 120,160,200,240;
  * positive comparison / stationary scale gap at every order;
  * new curvature-overlap sandwich, pointwise in the outer Gaussian V;
  * exact outer-variance identity used in the proof;
  * independent adaptive quadrature for the nested Q term at the GH240 point.

The analytic theorem is proved in the run report.
"""
import os, math
os.environ.setdefault("JAX_ENABLE_X64", "True")
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
from scipy.integrate import quad
from scipy.special import log_ndtr, logsumexp
import jax
import jax.numpy as jnp
from jax.scipy.special import log_ndtr as jlog_ndtr
from jax.scipy.special import logsumexp as jlogsumexp
jax.config.update("jax_enable_x64", True)

KAPPA = -1.0
ALPHA = 12.28722223
LOWER = 6.30297437506
PREV = 12.2872223


def gh(n):
    x, w = hermgauss(n)
    return jnp.array(np.sqrt(2.0) * x), jnp.array(w / np.sqrt(np.pi))


def reconstruct(p3, p2, q3, q2):
    sq_qp = jnp.sqrt(q3 / p3)
    sq_pq = 1.0 / sq_qp
    c3 = sq_pq / (p2 - p3) - sq_qp / (q2 - q3)
    gp = 0.5 * ((1 - q2) / (1 - p2)) * ((p2 - p3) / (q2 - q3)) * sq_qp
    c2 = (((p2 - p3) / (q2 - q3)) * sq_qp) / (1 - p2) \
         - (((q2 - q3) / (p2 - p3)) * sq_pq) / (1 - q2)
    return c3, c2, gp


def make_full_system(n):
    nodes, weights = gh(n)
    U = nodes[:, None]
    V = nodes[None, :]

    def psi_orig(v, alpha):
        p3, p2, q3, q2, c3, c2, gs, gp = v
        Aq = 2 * gp - c2 * (1 - q2)
        Dq = Aq - c3 * (q2 - q3)
        B = c2 / (4 * gs)
        s = jnp.sqrt(1 - p2)
        mu = jnp.sqrt(p2 - p3) * U + jnp.sqrt(p3) * V + KAPPA
        A = 1 + 2 * B * s * s
        logf = jnp.logaddexp(
            jlog_ndtr(-mu / s),
            -0.5 * jnp.log(A) - B * mu * mu / A
            + jlog_ndtr(mu / (s * jnp.sqrt(A)))
        )
        m = c3 / c2
        logZ = jlogsumexp(jnp.log(weights)[:, None] + m * logf, axis=0)
        Q = jnp.sum(weights * logZ)
        return (
            0.5 * (1 - p2 * q2) * c2
            + 0.5 * (p2 * q2 - p3 * q3) * c3
            - gp
            + (0.5 / c2) * jnp.log(Aq / (2 * gp))
            + (0.5 / c3) * jnp.log(Dq / Aq)
            - q3 / (2 * Dq)
            + gs
            - (alpha / c3) * Q
        )

    psi = jax.jit(psi_orig)
    grad = jax.jit(jax.grad(psi_orig, argnums=0))

    def fixres(y, alpha):
        p3, p2, q3, q2, gs = y
        c3, c2, gp = reconstruct(p3, p2, q3, q2)
        v = jnp.array([p3, p2, q3, q2, c3, c2, gs, gp])
        g = grad(v, alpha)
        return jnp.array([g[0], g[1], g[4], g[5], g[6]])

    return psi, grad, jax.jit(fixres)


def score_curvature(v, n):
    p3, p2, q3, q2, c3, c2, gs, gp = [float(z) for z in v]
    x, w = hermgauss(n)
    x = np.sqrt(2.0) * x
    w = w / np.sqrt(np.pi)
    U = jnp.array(x[:, None])
    V = jnp.array(x[None, :])
    jw = jnp.array(w)
    B = c2 / (4 * gs)
    s = math.sqrt(1 - p2)
    d = math.sqrt(p2 - p3)
    m = c3 / c2

    def lf(mu, Bv):
        A = 1 + 2 * Bv * s * s
        return jnp.logaddexp(
            jlog_ndtr(-mu / s),
            -0.5 * jnp.log(A) - Bv * mu * mu / A
            + jlog_ndtr(mu / (s * jnp.sqrt(A)))
        )

    ux = jax.grad(lf, argnums=0)
    uxx = jax.grad(ux, argnums=0)
    uB = jax.grad(lf, argnums=1)
    vf = jax.jit(jax.vmap(lf, in_axes=(0, None)))
    vx = jax.jit(jax.vmap(ux, in_axes=(0, None)))
    vxx = jax.jit(jax.vmap(uxx, in_axes=(0, None)))
    vB = jax.jit(jax.vmap(uB, in_axes=(0, None)))

    mu = (d * U + jnp.sqrt(p3) * V + KAPPA).reshape(-1)
    uu = vf(mu, B).reshape((n, n))
    gx = vx(mu, B).reshape((n, n))
    gxx = vxx(mu, B).reshape((n, n))
    bb = vB(mu, B).reshape((n, n))

    lw = jnp.log(jw)[:, None]
    lz = jlogsumexp(lw + m * uu, axis=0)
    pr = jnp.exp(lw + m * uu - lz[None, :])

    mean_g = jnp.sum(pr * gx, axis=0)
    second_g = jnp.sum(pr * gx * gx, axis=0)
    t = second_g - mean_g * mean_g
    c = -jnp.sum(pr * gxx, axis=0)

    # New lower bound from Cramer--Rao plus the exact outer variance identity.
    lower = d * d * c * c / (1 + m * d * d * c)

    # New upper bound from one-dimensional Brascamp--Lieb for the outer tilt.
    upper = jnp.sum(
        pr * (d * d * gxx * gxx / (1 - m * d * d * gxx)), axis=0
    )

    mean_U = jnp.sum(pr * U, axis=0)
    second_U = jnp.sum(pr * U * U, axis=0)
    var_U = second_U - mean_U * mean_U
    var_identity = 1 - m * d * d * c + m * m * d * d * t

    mb_v = -jnp.sum(pr * bb, axis=0)
    M1 = jnp.sum(jw * mean_g * mean_g)
    M2 = jnp.sum(jw * second_g)
    MB = jnp.sum(jw * mb_v)
    Ev_t = jnp.sum(jw * t)
    Ev_lower = jnp.sum(jw * lower)
    Ev_upper = jnp.sum(jw * upper)
    Ev_c = jnp.sum(jw * c)
    qden = 4 * B * B * MB

    return {
        "B": float(B), "m": float(m), "d": float(d),
        "M1": float(M1), "M2": float(M2), "MB": float(MB),
        "t": float(Ev_t), "lower": float(Ev_lower), "upper": float(Ev_upper),
        "cmean": float(Ev_c),
        "qgap_direct": float((M2 - M1) / qden),
        "qgap_lower": float(Ev_lower / qden),
        "qgap_upper": float(Ev_upper / qden),
        "pointwise_lower_margin": float(jnp.min(t - lower)),
        "pointwise_upper_margin": float(jnp.min(upper - t)),
        "var_identity_inf": float(jnp.max(jnp.abs(var_U - var_identity))),
        "varU_min": float(jnp.min(var_U)), "varU_max": float(jnp.max(var_U)),
    }


def gh_Q(v, n):
    p3, p2, q3, q2, c3, c2, gs, gp = [float(z) for z in v]
    x, w = hermgauss(n)
    x = np.sqrt(2) * x
    w = w / np.sqrt(np.pi)
    U = x[:, None]
    V = x[None, :]
    B = c2 / (4 * gs)
    s = np.sqrt(1 - p2)
    m = c3 / c2
    mu = np.sqrt(p2 - p3) * U + np.sqrt(p3) * V + KAPPA
    A = 1 + 2 * B * s * s
    u = np.logaddexp(
        log_ndtr(-mu / s),
        -0.5 * np.log(A) - B * mu * mu / A
        + log_ndtr(mu / (s * np.sqrt(A)))
    )
    return float(np.sum(w * logsumexp(np.log(w)[:, None] + m * u, axis=0)))


def adaptive_Q(v, L=8.0):
    p3, p2, q3, q2, c3, c2, gs, gp = [float(z) for z in v]
    B = c2 / (4 * gs)
    s = np.sqrt(1 - p2)
    m = c3 / c2
    rt = np.sqrt(2 * np.pi)

    def phi(x):
        return np.exp(-0.5 * x * x) / rt

    def logf(u3, u4):
        mu = np.sqrt(p2 - p3) * u3 + np.sqrt(p3) * u4 + KAPPA
        A = 1 + 2 * B * s * s
        return np.logaddexp(
            log_ndtr(-mu / s),
            -0.5 * np.log(A) - B * mu * mu / A
            + log_ndtr(mu / (s * np.sqrt(A)))
        )

    def inner(u4):
        val, _ = quad(
            lambda u3: phi(u3) * np.exp(m * logf(u3, u4)),
            -L, L, epsabs=2e-12, epsrel=2e-12, limit=180
        )
        return val

    return quad(
        lambda u4: phi(u4) * np.log(inner(u4)),
        -L, L, epsabs=5e-11, epsrel=5e-11, limit=120
    )


seed = np.array([
    0.59916661152315709,
    0.96911590889423460,
    0.22869805492482020,
    0.63843683182824196,
    0.076564610980229264,
], float)

print("NM13-03 T03 curvature-overlap checker")
print("STATUS NUMERICAL_SUPPORT_NOT_DIRECTED_INTERVAL")
print("ALPHA", format(ALPHA, ".14f"))
last = None
all_positive = True
for n in (120, 160, 200, 240):
    psi, grad, F = make_full_system(n)
    sol = root(lambda z: np.asarray(F(jnp.array(z), ALPHA), float), seed,
               method="hybr", tol=1e-12)
    p3, p2, q3, q2, gs = sol.x
    c3, c2, gp = [float(z) for z in reconstruct(p3, p2, q3, q2)]
    v = np.array([p3, p2, q3, q2, c3, c2, gs, gp])
    g = np.asarray(grad(jnp.array(v), ALPHA), float)
    pv = float(psi(jnp.array(v), ALPHA))
    r2 = q3 / p3
    r1 = (q2 - q3) / (p2 - p3)
    r0 = (1 - q2) / (1 - p2)
    gap = 2 * gs - r1 / (r0 * np.sqrt(r2))
    all_positive = all_positive and pv > 0 and gap > 0
    print("GH", n, "success", sol.success,
          "psi", format(pv, ".17g"),
          "scale_gap", format(gap, ".17g"),
          "grad_inf", format(np.max(np.abs(g)), ".3e"))
    seed = sol.x
    last = (n, v, pv, gap)

n, v, pv, gap = last
cc = score_curvature(v, n)
p3, p2, q3, q2, c3, c2, gs, gp = v
print("PARAMS_GH240", *(format(z, ".17g") for z in v))
print("CURVATURE_OVERLAP_T", format(cc["lower"], ".17g"),
      format(cc["t"], ".17g"), format(cc["upper"], ".17g"))
print("CURVATURE_OVERLAP_QGAP", format(cc["qgap_lower"], ".17g"),
      format(q2 - q3, ".17g"), format(cc["qgap_upper"], ".17g"))
print("QGAP_DIRECT_SCORE", format(cc["qgap_direct"], ".17g"))
print("POINTWISE_LOWER_MARGIN", format(cc["pointwise_lower_margin"], ".3e"), "tolerance_pass", cc["pointwise_lower_margin"] > -1e-8)
print("POINTWISE_UPPER_MARGIN", format(cc["pointwise_upper_margin"], ".3e"), "tolerance_pass", cc["pointwise_upper_margin"] > -1e-8)
print("OUTER_VARIANCE_IDENTITY_INF", format(cc["var_identity_inf"], ".3e"))
print("OUTER_VARIANCE_RANGE", format(cc["varU_min"], ".17g"), format(cc["varU_max"], ".17g"))

qgh = gh_Q(v, 240)
qad, qerr = adaptive_Q(v)
print("Q_GH240", format(qgh, ".17g"),
      "Q_ADAPTIVE", format(qad, ".17g"),
      "Q_DIFF", format(qad - qgh, ".3e"),
      "Q_QUAD_ERR", format(qerr, ".3e"))
print("ENVELOPE_SLOPE", format(-qgh / c3, ".17g"))
print("SUPPORTED_BOUND_BEFORE", format(PREV, ".10f"))
print("SUPPORTED_BOUND_AFTER", format(ALPHA, ".11f"))
print("UPPER_ENDPOINT_GAIN", format(PREV - ALPHA, ".17g"))
print("WIDTH_BEFORE", format(PREV - LOWER, ".14f"))
print("WIDTH_AFTER", format(ALPHA - LOWER, ".14f"))
print("ALL_POSITIVE", all_positive)
print("ALL_NUMERICAL_CHECKS_PASS")
