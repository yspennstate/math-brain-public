"""Exact identities and bounded diagnostics for the endpoint theorem.

Standard library, one process, no workers. Direct GD uses row-based gradients;
the claimed Gram and Krylov recurrences are used only as independent checks.
"""

import json
import math
import os
import random
import resource
import signal
import sys
import time
from fractions import Fraction as F
from pathlib import Path

started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
signal.alarm(90)
cpu_soft, cpu_hard = resource.getrlimit(resource.RLIMIT_CPU)
cpu_cap = 60 if cpu_hard == resource.RLIM_INFINITY else min(60, cpu_hard)
resource.setrlimit(resource.RLIMIT_CPU, (cpu_cap, cpu_hard))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    bt = tr(b)
    return [[dot(row, col) for col in bt] for row in a]


def mv(a, v):
    return [dot(row, v) for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def determinant(a):
    a = [row[:] for row in a]
    result = F(1)
    for k in range(len(a)):
        pivot = next((j for j in range(k, len(a)) if a[j][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        scale = a[k][k]
        result *= scale
        for j in range(k+1, len(a)):
            factor = a[j][k]/scale
            for ell in range(k+1, len(a)):
                a[j][ell] -= factor*a[k][ell]
            a[j][k] = 0
    return result


def inverse(a):
    n = len(a)
    a = [row[:] + erow for row, erow in zip(a, eye(n))]
    for k in range(n):
        p = next(j for j in range(k, n) if a[j][k])
        a[p], a[k] = a[k], a[p]
        pivot = a[k][k]
        a[k] = [x/pivot for x in a[k]]
        for j in range(n):
            if j != k:
                factor = a[j][k]
                a[j] = [x-factor*y for x, y in zip(a[j], a[k])]
    return [row[n:] for row in a]


def gram(z):
    return mm(tr(z), z)


def quantities(a, u):
    c = gram(u)
    v = mv(tr(u), a)
    q = dot(a, a)
    hh = [[x+(q if i == j else 0) for j, x in enumerate(row)]
          for i, row in enumerate(c)]
    return q, c, v, dot(v, v), hh


def step(a, u, target=None):
    residual = mv(tr(u), a)
    if target is not None:
        residual = [x-y for x, y in zip(residual, target)]
    # Both gradients use the old parameters.
    return ([x-dot(row, residual) for x, row in zip(a, u)],
            [[x-ai*rj for x, rj in zip(row, residual)]
             for ai, row in zip(a, u)])


def augmented(a, u):
    return [[ai]+row for ai, row in zip(a, u)]


def krylov(c, v):
    cols = []
    x = v[:]
    for _ in v:
        cols.append(x)
        x = mv(c, x)
    return tr(cols)


def kblock(v):
    n = len(v)+1
    return [[(v[j-1] if i == 0 and j else
              v[i-1] if j == 0 and i else F(0))
             for j in range(n)] for i in range(n)]


def eigensystem(a):
    """Jacobi rotations with eigenvectors; descending eigenvalues."""
    a = [list(map(float, row)) for row in a]
    n = len(a)
    vectors = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(100*n*n):
        pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
        if not pairs:
            break
        i, j = max(pairs, key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 2e-15:
            break
        angle = .5*math.atan2(2*a[i][j], a[j][j]-a[i][i])
        cs, sn = math.cos(angle), math.sin(angle)
        ai, aj, off = a[i][i], a[j][j], a[i][j]
        for k in range(n):
            if k != i and k != j:
                x, y = a[k][i], a[k][j]
                a[k][i] = a[i][k] = cs*x-sn*y
                a[k][j] = a[j][k] = sn*x+cs*y
            x, y = vectors[k][i], vectors[k][j]
            vectors[k][i], vectors[k][j] = cs*x-sn*y, sn*x+cs*y
        a[i][i] = cs*cs*ai-2*cs*sn*off+sn*sn*aj
        a[j][j] = sn*sn*ai+2*cs*sn*off+cs*cs*aj
        a[i][j] = a[j][i] = 0.
    else:
        raise AssertionError("Jacobi iteration cap")
    order = sorted(range(n), key=lambda i: -a[i][i])
    return [a[i][i] for i in order], [[row[i] for i in order] for row in vectors]


def projector_weight(c, v, k):
    vals, vecs = eigensystem(c)
    weights = mv(tr(vecs), v)
    return sum(x*x for x in weights[:k]), vals, weights


rng = random.Random(226202611150846)
exact_cases = 0
correction_cases = 0
for d in (1, 2, 3, 4):
    m = d+2
    for case in range(8):
        a = [F(rng.randrange(-5, 6), 9) for _ in range(m)]
        u = [[F(rng.randrange(-5, 6), 13) for _ in range(d)] for _ in range(m)]
        q, c, v, h, hh = quantities(a, u)
        an, un = step(a, u)
        qn, cn, vn, hn, hhn = quantities(an, un)
        assert qn == q-2*h+dot(v, mv(c, v))
        assert cn == [[x-(2-q)*v[i]*v[j] for j, x in enumerate(row)]
                      for i, row in enumerate(c)]
        assert vn == [vi-dot(row, v)+h*vi for vi, row in zip(v, hh)]
        zz, zzn = augmented(a, u), augmented(an, un)
        assert determinant(gram(zzn)) == determinant(gram(zz))*(1-h)**2
        theta = (1-q)*(1-h)
        filt = [[(theta if i == j else 0)-x for j, x in enumerate(row)]
                for i, row in enumerate(cn)]
        assert vn == mv(filt, v)
        assert determinant(krylov(cn, v)) == determinant(krylov(c, v))
        assert krylov(cn, vn) == mm(filt, krylov(cn, v))
        assert determinant(krylov(cn, vn)) == (
            determinant(filt)*determinant(krylov(c, v)))
        exact_cases += 1
        if determinant(hh) and determinant(hhn):
            # Independent audit of the round-4 corrected parameter argument.
            hi, hni = inverse(hh), inverse(hhn)
            w, wn = mv(hi, v), mv(hni, vn)
            err = [x-y+vi for x, y, vi in zip(wn, w, v)]
            r1 = mv(add(hni, hi, -1), v)
            r2 = mv(mm(hni, add(hhn, hh, -1)), v)
            r3 = mv(hni, v)
            assert err == [x+y+h*z for x, y, z in zip(r1, r2, r3)]
            corrected = mm(zz, add(eye(d+1), kblock(w), -1))
            correctedn = mm(zzn, add(eye(d+1), kblock(wn), -1))
            rhs = add(mm(mm(zz, kblock(v)), kblock(wn)), mm(zz, kblock(err)), -1)
            assert add(correctedn, corrected, -1) == rhs
            correction_cases += 1

# Vandermonde witnesses: check by elimination, not by a determinant expansion.
witnesses = []
for d in range(1, 7):
    c = [[F((i+1)**2 if i == j else 0) for j in range(d)] for i in range(d)]
    v = [F(j+1) for j in range(d)]
    direct = determinant(krylov(c, v))
    formula = math.prod(range(1, d+1))*math.prod(
        (j*j-i*i) for i in range(1, d+1) for j in range(i+1, d+1))
    assert direct == formula and direct != 0
    witnesses.append(str(direct))

# Old exact active-supercritical landing, from direct row updates.
m, d = 16, 8
a = [F(4, 3), F(1, 3)]+[F(0)]*(m-2)
u = [[F(0)]*d for _ in range(m)]
u[0][0], u[1][0] = F(52, 51), F(47, 51)
for j in range(1, d):
    u[j+1][j] = F(1, 2)
q0, c0, v0, h0, _ = quantities(a, u)
an, un = step(a, u)
qn, cn, vn, hn, _ = quantities(an, un)
assert q0 == c0[0][0] == F(17, 9)
assert h0 == F(25, 9)
assert qn == cn[0][0] == F(128, 81)
assert vn == [0]*d
assert qn+cn[0][0] == F(256, 81)
assert determinant(gram(augmented(a, u))) > 0
assert determinant(gram(augmented(an, un))) > 0
assert determinant(krylov(cn, vn)) == 0
# Lift a nonzero eigenvector of the output Gram to the full parameter Hessian.
alpha = tr(un)[0]
pert = [[ai if j == 0 else F(0) for j in range(d)] for ai in an]
jpert = [x+y for x, y in zip(mv(tr(un), alpha), mv(tr(pert), an))]
ha = mv(un, jpert)
hu = [[ai*rj for rj in jpert] for ai in an]
assert ha == [F(256, 81)*x for x in alpha]
assert hu == [[F(256, 81)*x for x in row] for row in pert]

# Independent rank-collapse check inside the rectangle, now in a scalar model.
aa = [F(1), F(1, 2), F(1, 2)]
uu = [[F(1)], [F(-1, 2)], [F(1, 2)]]
assert quantities(aa, uu)[3] == 1
assert determinant(gram(augmented(aa, uu))) > 0
ap, up = step(aa, uu)
assert determinant(gram(augmented(ap, up))) == 0

# New spectator example; no finite landing after step 1 by the positive factor.
a = [F(1)]+[F(0)]*(m-1)
u = [[F(0)]*d for _ in range(m)]
u[0][0], u[1][0], u[2][1] = F(1, 4), F(1, 4), F(6, 5)
for j in range(2, d):
    u[j+1][j] = F(1, 10)
assert determinant(gram(augmented(a, u))) > 0
q0, c0, v0, h0, _ = quantities(a, u)
assert q0 == 1 and c0[1][1] == F(36, 25) < 2 and h0 == F(1, 16)
assert determinant(krylov(c0, v0)) == 0
an, un = step(a, u)
q1, c1, v1, h1, _ = quantities(an, un)
assert q1 == F(113, 128) and c1[0][0] == F(1, 16)
assert v1[0] == F(-1, 64) and h1 == F(1, 4096)
assert q1+c1[0][0] == F(121, 128) < 1
assert tr(u)[1:] == tr(un)[1:]
active_tail_bound = c1[0][0]/(2-q1)
qlower = q1-2*active_tail_bound
assert active_tail_bound == F(8, 143)
assert qlower == F(14111, 18304)
spectator_lower_bound = qlower+F(36, 25)
assert spectator_lower_bound > 2
# A second derivation uses explicit one-step coordinates and the scalar C law.
assert an[:2] == [F(15, 16), F(-1, 16)]
assert [row[0] for row in un[:2]] == [F(0), F(1, 4)]
assert sum(x*x for x in an[:2]) == q1
assert F(1, 16) * F(128, 143) == active_tail_bound
spectator_float = (list(map(float, a)), [list(map(float, row)) for row in u])

# Critical stationary endpoint and whole-space top multiplicity are not excluded
# deterministically: they lie in the null set D0=0.
a = [F(1)]+[F(0)]*(m-1)
u = [[F(0)]*d for _ in range(m)]
for j in range(d):
    u[j+1][j] = F(1)
assert step(a, u) == (a, u)
q, c, v, h, _ = quantities(a, u)
assert q+c[0][0] == 2 and v == [0]*d

# Projector diagnostic 1: Jacobi's full eigensystem must reconstruct B.
max_eigen_residual = 0.
for case in range(10):
    n = 5
    b = [[rng.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    b = [[(b[i][j]+b[j][i])/2 for j in range(n)] for i in range(n)]
    vals, vecs = eigensystem(b)
    for val, vec in zip(vals, tr(vecs)):
        max_eigen_residual = max(max_eigen_residual,
            max(abs(x-val*y) for x, y in zip(mv(b, vec), vec)))
    assert max_eigen_residual < 1e-12
    assert max(abs(x-float(i == j)) for i, row in enumerate(mm(tr(vecs), vecs))
               for j, x in enumerate(row)) < 1e-12


def closed_weight_2x2(b, v):
    """P_top=(B-lambda_min I)/(lambda_max-lambda_min), independent formula."""
    trace = b[0][0]+b[1][1]
    gap = math.hypot(b[0][0]-b[1][1], 2*b[0][1])
    low = (trace-gap)/2
    return (dot(v, mv(b, v))-low*dot(v, v))/gap


max_closed_error = 0.
max_derivative_error = 0.
projector_cases = 0
for case in range(32):
    b = [[2.8+rng.random(), rng.uniform(-.2, .2)], [0., .6+rng.random()*.2]]
    b[1][0] = b[0][1]
    v = [rng.uniform(-.4, .4), rng.uniform(-.4, .4)]
    alpha = rng.uniform(.1, 1.9)
    h = dot(v, v)

    def segment(s):
        return [[x-s*alpha*v[i]*v[j] for j, x in enumerate(row)]
                for i, row in enumerate(b)]

    w0, vals0, _ = projector_weight(b, v, 1)
    w1, vals1, _ = projector_weight(segment(1), v, 1)
    # Weyl gives a certified lower gap over the whole segment.
    delta = vals0[0]-vals0[1]-alpha*h
    assert delta > 1
    assert w1+1e-14 >= math.exp(-2*alpha*h/delta)*w0
    for s in (0., .25, .5, .75, 1.):
        bb = segment(s)
        w, vals, weights = projector_weight(bb, v, 1)
        independent_w = closed_weight_2x2(bb, v)
        max_closed_error = max(max_closed_error, abs(w-independent_w))
        assert abs(w-independent_w) < 1e-13
        if s == .5:
            eps = 1e-5
            fd = (closed_weight_2x2(segment(s+eps), v)
                  - closed_weight_2x2(segment(s-eps), v))/(2*eps)
            deriv = -2*alpha*weights[0]**2*weights[1]**2/(vals[0]-vals[1])
            max_derivative_error = max(max_derivative_error, abs(fd-deriv))
            assert abs(fd-deriv) < 1e-9
            assert deriv >= -2*alpha*h/delta*w-1e-13
    projector_cases += 1

# Projector diagnostic 2: repeated eigenvalues inside a nontrivial top cluster.
for diagonal, k in (([3., 3., 1., 0.], 2), ([4., 4., 4., 1., 1.], 3)):
    n = len(diagonal)
    b = [[diagonal[i] if i == j else 0. for j in range(n)] for i in range(n)]
    v = [(.15 if i % 2 else -.1) for i in range(n)]
    alpha = 1.6
    h = dot(v, v)
    bn = [[x-alpha*v[i]*v[j] for j, x in enumerate(row)] for i, row in enumerate(b)]
    delta = diagonal[k-1]-diagonal[k]-alpha*h
    w0, _, _ = projector_weight(b, v, k)
    w1, _, _ = projector_weight(bn, v, k)
    assert w1 >= math.exp(-2*alpha*h/delta)*w0-1e-13
    # A 2D invariant reduction requires both diagonal blocks to be scalar.
    if len(set(diagonal[k:])) == 1:
        topnorm = math.sqrt(sum(x*x for x in v[:k]))
        botnorm = math.sqrt(sum(x*x for x in v[k:]))
        reduced = [[diagonal[0]-alpha*topnorm**2, -alpha*topnorm*botnorm],
                   [-alpha*topnorm*botnorm, diagonal[k]-alpha*botnorm**2]]
        closed = closed_weight_2x2(reduced, [topnorm, botnorm])
        assert abs(w1-closed) < 1e-13
    # Check the derivative for either bottom spectrum, including at s=0
    # where the internal top eigenvalue is repeated.
    def cluster_weight(s):
        bs = [[x-s*alpha*v[i]*v[j] for j, x in enumerate(row)]
              for i, row in enumerate(b)]
        return projector_weight(bs, v, k)[0]
    eps = 1e-5
    fd = (cluster_weight(eps)-cluster_weight(-eps))/(2*eps)
    deriv = -2*alpha*sum(v[i]**2*v[j]**2/(diagonal[i]-diagonal[j])
                         for i in range(k) for j in range(k, n))
    assert abs(fd-deriv) < 1e-9
    projector_cases += 1

# Bounded finite trajectories: Gaussian draws conditioned on the rectangle,
# and normalized dense starts close to the upper sides of the rectangle.
starts = []
draws = 0
while len(starts) < 24 and draws < 400:
    draws += 1
    m, d = (16, 8) if len(starts) < 16 else (6, 3)
    sd = .2 if m == 16 else .36
    a = [rng.gauss(0, sd) for _ in range(m)]
    u = [[rng.gauss(0, sd) for _ in range(d)] for _ in range(m)]
    q, c, v, h, _ = quantities(a, u)
    cmax = eigensystem(c)[0][0]
    if q < 2 and cmax < 2:
        starts.append(("conditioned_gaussian", a, u))
assert len(starts) == 24
for case in range(16):
    m, d = (16, 8) if case < 8 else (6, 3)
    a = [rng.gauss(0, 1) for _ in range(m)]
    u = [[rng.gauss(0, 1) for _ in range(d)] for _ in range(m)]
    q, c, v, h, _ = quantities(a, u)
    qwant = (1.5, 1.9, 1.999, 1.9999)[case % 4]
    cwant = (1.8, 1.5, 1.999, 1.9999)[case % 4]
    sa = math.sqrt(qwant/q)
    su = math.sqrt(cwant/eigensystem(c)[0][0])
    starts.append(("normalized_dense", [x*sa for x in a],
                   [[x*su for x in row] for row in u]))

records = []
for case, (kind, a, u) in enumerate(starts):
    q0, c0, v0, h0, _ = quantities(a, u)
    cmax0 = eigensystem(c0)[0][0]
    assert q0 < 2 and cmax0 < 2
    sumh, loss_increases, first_subcritical, small_supercritical = 0., 0, None, 0
    updates = 0
    maxh = h0
    for iteration in range(6000):
        q, c, v, h, _ = quantities(a, u)
        vals = eigensystem(c)[0] if iteration % 5 == 0 or h < 1e-24 else None
        s = q+vals[0] if vals is not None else math.inf
        if s < 2 and first_subcritical is None:
            first_subcritical = iteration
        if h < 1e-24 and s >= 2:
            small_supercritical += 1
        if h < 1e-26 and s < 2:
            break
        sumh += h
        maxh = max(maxh, h)
        an, un = step(a, u)
        qn, cn, vn, hn, _ = quantities(an, un)
        assert qn <= q+1e-12
        # Trace decreases independently of an eigenvalue computation.
        assert sum(cn[j][j] for j in range(len(v))) <= sum(c[j][j] for j in range(len(v)))+1e-12
        assert sumh <= q0/(2-cmax0)+1e-8
        if hn > h*(1+1e-9):
            loss_increases += 1
        a, u = an, un
        updates += 1
    qf, cf, vf, hf, _ = quantities(a, u)
    cfvals = eigensystem(cf)[0]
    sf = qf+cfvals[0]
    records.append({"case": case, "kind": kind, "m": len(a), "d": len(vf),
                    "initial_q": q0, "initial_cmax": cmax0,
                    "initial_h": h0, "peak_h": maxh,
                    "outside_old_sum_basin": q0+cmax0 >= 2,
                    "updates": updates, "first_observed_output_sharpness_below_2": first_subcritical,
                    "loss_increasing_steps": loss_increases,
                    "tiny_residual_with_output_sharpness_ge_2_steps": small_supercritical,
                    "final_residual_norm": math.sqrt(hf),
                    "final_output_sharpness": sf,
                    "final_output_smallest_eigenvalue": qf+cfvals[-1],
                    "reached_tolerance_with_output_sharpness_below_2": hf < 1e-26 and sf < 2})

# Numerical spectator trajectory: expected supercritical, all parameters trainable.
a, u = spectator_float
for _ in range(200):
    a, u = step(a, u)
qf, cf, vf, hf, _ = quantities(a, u)
spectator_final = qf+eigensystem(cf)[0][0]
assert spectator_final >= float(spectator_lower_bound)-1e-12
assert spectator_final > 2

# Earlier numerical constant, re-evaluated by two formulas.
old_chernoff = math.exp(-72*(3-math.log(4)))
assert abs(old_chernoff/((4**72)*math.exp(-216))-1) < 2e-14

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != "darwin":
    peak *= 1024
assert peak < 1024**3
summary = {
    "status": "PASS", "seed": 226202611150846,
    "effective_nice": priority, "cpu_cap_seconds": cpu_cap,
    "wall_alarm_seconds": 90, "peak_rss_bytes": peak,
    "elapsed_seconds": time.monotonic()-started,
    "exact_cases": exact_cases, "round4_correction_identity_cases": correction_cases,
    "vandermonde_witnesses_d1_through_d6": witnesses,
    "projector_cases_including_internal_multiplicities": projector_cases,
    "maximum_eigenvector_residual": max_eigen_residual,
    "maximum_projector_closed_formula_error": max_closed_error,
    "maximum_projector_derivative_error": max_derivative_error,
    "one_step_supercritical_endpoint": "256/81",
    "spectator_exact_q_lower_bound": str(qlower),
    "spectator_exact_sharpness_lower_bound": str(spectator_lower_bound),
    "spectator_numerical_final_output_sharpness": spectator_final,
    "gaussian_draws_for_24_accepted_starts": draws,
    "finite_trajectory_cases": len(records),
    "finite_cases_outside_old_sum_basin": sum(r["outside_old_sum_basin"] for r in records),
    "finite_cases_with_loss_increases": sum(r["loss_increasing_steps"] > 0 for r in records),
    "finite_cases_with_h_above_one": sum(r["peak_h"] > 1 for r in records),
    "finite_cases_reaching_tolerance_and_output_sharpness_below_2": sum(
        r["reached_tolerance_with_output_sharpness_below_2"] for r in records),
    "largest_finite_update_count": max(r["updates"] for r in records),
    "maximum_final_residual_norm": max(r["final_residual_norm"] for r in records),
    "largest_final_output_sharpness_generic_probes": max(r["final_output_sharpness"] for r in records),
    "earlier_chernoff_bound": old_chernoff,
}
Path("verification.json").write_text(json.dumps({"summary": summary, "trajectories": records}, indent=2)+"\n")
print(json.dumps(summary, indent=2))
