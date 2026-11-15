"""Small, standard-library checks of the structured linear NTK limit.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
"""

import json
import math
import os
from pathlib import Path
import random
import resource
import time


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def mv(w, x):
    return [dot(row, x) for row in w]


def mtv(w, x):
    return [sum(w[i][j] * x[i] for i in range(len(w)))
            for j in range(len(w[0]))]


def dense_output_grad(ws, bias, x):
    """Backprop in dense W coordinates, then convert to Theta coordinates."""
    n = len(x)
    acts = [list(x)]
    for w in ws:
        acts.append(mv(w, acts[-1]))
    back = [1.0] + [0.0] * (n - 1)
    grads = [None] * len(ws)
    for l in range(len(ws) - 1, -1, -1):
        grads[l] = [[back[i] * acts[l][j] / math.sqrt(n)
                     for j in range(n)] for i in range(n)]
        back = mtv(ws[l], back)
    return bias + acts[-1][0], grads


def dense_kernel(ws, bias, x, xp):
    _, gx = dense_output_grad(ws, bias, x)
    _, gp = dense_output_grad(ws, bias, xp)
    return 1.0 + sum(dot(a, b) for ml, pl in zip(gx, gp)
                     for a, b in zip(ml, pl))


def coefficients(a, s, n):
    """Direct products, independent of the limiting integral formula."""
    prefix = [1.0]
    for z in s:
        prefix.append(prefix[-1] * z * z)
    suffix = [1.0] * (len(a) + 1)
    for l in range(len(a) - 1, -1, -1):
        suffix[l] = suffix[l + 1] * a[l] * a[l]
    p = math.prod(a)
    aa = sum((p / z) ** 2 for z in a) / n
    bb = sum(suffix[l + 1] * prefix[l] for l in range(len(a))) / n
    return p, aa, bb


def limit_coeff(s, c, t):
    p = s * math.exp(t * c)
    z = 2.0 * t * c
    h = math.expm1(z) / z if z else 1.0
    return p, t * p * p, t * s * s * h


def scalar_step(a, bias, y, eta, n):
    p = math.prod(a)
    r = bias + p - y
    return [z - eta * r * p / (n * z) for z in a], bias - eta * r


def dense_checks():
    n = 3
    s = [0.91, 1.06, 0.97, 1.03]
    a = list(s)
    ws = [[[s_l if i == j else 0.0 for j in range(n)]
           for i in range(n)] for s_l in s]
    bias = 0.0
    eta, y = 0.04, 0.2
    inputs = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.4, -0.3, 0.8]]
    kernel_error = matrix_orbit_error = finite_difference_error = 0.0
    for k in range(5):
        p, aa, bb = coefficients(a, s, n)
        for x in inputs:
            for xp in inputs:
                formula = 1.0 + aa * x[0] * xp[0] + bb * dot(x[1:], xp[1:])
                kernel_error = max(kernel_error,
                                   abs(formula - dense_kernel(ws, bias, x, xp)))
        # Numerical differentiation of every Theta entry, including off-diagonals.
        x = inputs[-1]
        _, grads = dense_output_grad(ws, bias, x)
        eps_theta = 1e-5
        for l in range(len(ws)):
            for i in range(n):
                for j in range(n):
                    old = ws[l][i][j]
                    ws[l][i][j] = old + eps_theta / math.sqrt(n)
                    plus = dense_output_grad(ws, bias, x)[0]
                    ws[l][i][j] = old - eps_theta / math.sqrt(n)
                    minus = dense_output_grad(ws, bias, x)[0]
                    ws[l][i][j] = old
                    fd = (plus - minus) / (2.0 * eps_theta)
                    finite_difference_error = max(finite_difference_error,
                                                  abs(fd - grads[l][i][j]))
        out, train_grads = dense_output_grad(ws, bias, inputs[0])
        residual = out - y
        ws = [[[w - eta * residual * g / math.sqrt(n)
                for w, g in zip(row, grow)] for row, grow in zip(wmat, gmat)]
              for wmat, gmat in zip(ws, train_grads)]
        a, new_bias = scalar_step(a, bias, y, eta, n)
        bias = bias - eta * residual
        matrix_orbit_error = max(matrix_orbit_error, abs(bias - new_bias))
        for l in range(len(ws)):
            for i in range(n):
                for j in range(n):
                    expected = a[l] if i == j == 0 else (s[l] if i == j else 0.0)
                    matrix_orbit_error = max(matrix_orbit_error,
                                             abs(ws[l][i][j] - expected))
    # A finite dense perturbation breaks the invariant orbit immediately.
    perturbed = [[[float(i == j) for j in range(n)] for i in range(n)]
                 for _ in range(3)]
    perturbed[1][0][1] = 0.1
    _, grad = dense_output_grad(perturbed, 0.0, inputs[0])
    nonaligned_gradient = abs(grad[0][1][0])
    assert kernel_error < 1e-12
    assert matrix_orbit_error < 1e-12
    assert finite_difference_error < 1e-8
    assert nonaligned_gradient > 0.01
    return dict(max_dense_kernel_error=kernel_error,
                max_dense_orbit_error=matrix_orbit_error,
                max_theta_finite_difference_error=finite_difference_error,
                nonaligned_off_diagonal_gradient=nonaligned_gradient,
                finite_difference_entries_checked=5 * 4 * n * n)


def derivative_checks():
    n = 9
    s = [0.92, 1.05, 0.98, 1.02, 1.01, 0.96]
    p, aa, _ = coefficients(s, s, n)
    r = p - 0.2
    q = sum(z ** -2 for z in s)
    rr = sum(z ** -4 for z in s)
    exact = -2.0 * r * p ** 3 * (q * q - rr) / n ** 2
    eps = 1e-6
    ap, _ = scalar_step(s, 0.0, 0.2, eps, n)
    am, _ = scalar_step(s, 0.0, 0.2, -eps, n)
    finite = (coefficients(ap, s, n)[1] - coefficients(am, s, n)[1]) / (2 * eps)
    t, ss = 0.7, 1.3
    rr0 = ss - 0.2
    p1, a1, b1 = limit_coeff(ss, -eps * ss * rr0, t)
    pm, am, bm = limit_coeff(ss, eps * ss * rr0, t)
    da = (a1 - am) / (2 * eps)
    db = (b1 - bm) / (2 * eps)
    da_exact = -2 * t * t * ss ** 3 * rr0
    db_exact = -t * t * ss ** 3 * rr0
    assert abs(finite - exact) < 1e-8
    assert abs(da - da_exact) < 1e-8
    assert abs(db - db_exact) < 1e-8
    return dict(finite_size_formula=exact, finite_size_difference=finite,
                finite_size_error=abs(finite - exact),
                limiting_parallel_derivative=da_exact,
                limiting_perpendicular_derivative=db_exact,
                limiting_derivative_error=max(abs(da - da_exact), abs(db - db_exact)))


def convergence_checks():
    rows = []
    eta, y, target_product = 0.05, 0.2, 1.3
    # The exceptional zero-residual case must stay exactly stationary.
    stationary = [0.91, 1.06, 0.97]
    target = math.prod(stationary)
    unchanged, unchanged_bias = scalar_step(stationary, 0.0, target, eta, 7)
    assert unchanged == stationary and unchanged_bias == 0.0
    for t in [0.5, 1.0, 2.0]:
        for n in [32, 128, 512, 2048, 8192]:
            ll = round(n * t)
            rng = random.Random(245000 + n + ll)
            noise = [rng.gauss(0, 1) / math.sqrt(n) for _ in range(ll)]
            average = sum(noise) / ll
            # This isolates the deterministic theorem at one fixed S.
            logs = [z - average + math.log(target_product) / ll for z in noise]
            s = [math.exp(z) for z in logs]
            a = list(s)
            bias = c = limit_bias = 0.0
            max_p = max_a = max_b = max_bias = 0.0
            for k in range(7):
                p, aa, bb = coefficients(a, s, n)
                lp, la, lb = limit_coeff(target_product, c, t)
                max_p = max(max_p, abs(p - lp))
                max_a = max(max_a, abs(aa - la))
                max_b = max(max_b, abs(bb - lb))
                max_bias = max(max_bias, abs(bias - limit_bias))
                if k < 6:
                    a, bias = scalar_step(a, bias, y, eta, n)
                    lr = limit_bias + lp - y
                    c -= eta * lp * lr
                    limit_bias -= eta * lr
            rows.append(dict(t=t, n=n, L=ll, max_gain_deviation=max(abs(z - 1) for z in s),
                             max_output_product_error=max_p, max_parallel_error=max_a,
                             max_perpendicular_error=max_b, max_bias_error=max_bias))
        assert rows[-1]['max_parallel_error'] < rows[-5]['max_parallel_error']
        assert rows[-1]['max_perpendicular_error'] < rows[-5]['max_perpendicular_error']
    # Continuity at c=0 and the sign of the two coefficient changes.
    for c in [-0.1, 0.0, 0.1]:
        _, aa, bb = limit_coeff(target_product, c, 1.0)
        if c < 0:
            assert aa < bb < target_product ** 2
        elif c > 0:
            assert aa > bb > target_product ** 2
        else:
            assert aa == bb == target_product ** 2
    return rows


def initialization_checks():
    # Check normal means/variances by direct iid layer sums. These are diagnostics,
    # not estimates of heavy-tailed unlogged kernel moments.
    n, ll, samples = 128, 64, 4000
    mu, sigma, t = -0.5, 1.0, ll / n
    rng = random.Random(245)
    vals = [sum(mu / n + sigma * rng.gauss(0, 1) / math.sqrt(n)
                for _ in range(ll)) for _ in range(samples)]
    avg = sum(vals) / samples
    variance = sum((z - avg) ** 2 for z in vals) / (samples - 1)
    # Independent exact moment calculation via a product of scalar lognormal moments.
    # E[s_l^(2r)] = exp((2r*mu + 2r^2*sigma^2)/n).
    moments_product = [t ** r * math.prod([math.exp((2*r*mu + 2*r*r*sigma*sigma) / n)] * ll)
                       for r in (1, 2)]
    moments_limit = [t ** r * math.exp((2*r*mu + 2*r*r*sigma*sigma) * t)
                     for r in (1, 2)]
    relative_variance = moments_product[1] / moments_product[0] ** 2 - 1
    relative_variance_formula = math.expm1(4 * sigma * sigma * t)
    assert abs(avg - mu * t) < 5 * math.sqrt(sigma * sigma * t / samples)
    assert abs(variance - sigma * sigma * t) < 0.05
    assert max(abs(a-b) for a, b in zip(moments_product, moments_limit)) < 1e-12
    assert abs(relative_variance - relative_variance_formula) < 1e-12
    return dict(n=n, L=ll, samples=samples, sample_log_product_mean=avg,
                exact_log_product_mean=mu*t, sample_log_product_variance=variance,
                exact_log_product_variance=sigma*sigma*t,
                limiting_A_moments_via_layer_products=moments_product,
                limiting_A_moments_via_normal_law=moments_limit,
                A_relative_variance_via_moments=relative_variance,
                A_relative_variance_formula=relative_variance_formula)


def flow_checks():
    """RK4 integrates (b,c); the independent invariant predicts its endpoint."""
    def rhs(b, c, t, s, y):
        p = s * math.exp(t * c)
        r = b + p - y
        return -r, -p * r

    max_invariant = max_endpoint = max_residual = 0.0
    cases = []
    for t in [0.5, 1.0, 2.0]:
        for s in [0.4, 1.3, 2.5]:
            for y in [-1.0, 0.2, 3.0]:
                b = c = 0.0
                dt = 0.004
                for _ in range(10000):
                    k1b, k1c = rhs(b, c, t, s, y)
                    k2b, k2c = rhs(b+dt*k1b/2, c+dt*k1c/2, t, s, y)
                    k3b, k3c = rhs(b+dt*k2b/2, c+dt*k2c/2, t, s, y)
                    k4b, k4c = rhs(b+dt*k3b, c+dt*k3c, t, s, y)
                    b += dt * (k1b+2*k2b+2*k3b+k4b)/6
                    c += dt * (k1c+2*k2c+2*k3c+k4c)/6
                    p = s * math.exp(t*c)
                    max_invariant = max(max_invariant, abs(1/p+t*b-1/s))
                q = 1/s-t*y
                predicted = 2/(math.sqrt(q*q+4*t)+q)
                endpoint_error = abs(p-predicted)
                residual = abs(b+p-y)
                max_endpoint = max(max_endpoint, endpoint_error)
                max_residual = max(max_residual, residual)
                cases.append(dict(t=t, S=s, y=y, RK4_P=p, predicted_P=predicted,
                                  final_residual=residual, endpoint_error=endpoint_error))
    assert max_invariant < 1e-6
    assert max_endpoint < 1e-6
    assert max_residual < 1e-10
    # Euler iterates of the closed discrete recursion converge to the ODE.
    t, s, y = 1.0, 1.3, 0.2
    endpoints = []
    for steps in [20, 40, 80, 160, 320, 640]:
        eta = 1.0/steps
        b = c = 0.0
        for _ in range(steps):
            db, dc = rhs(b, c, t, s, y)
            b, c = b+eta*db, c+eta*dc
        endpoints.append(dict(steps=steps, P=s*math.exp(t*c), b=b))
    assert abs(endpoints[-1]['P']-endpoints[-2]['P']) < abs(endpoints[1]['P']-endpoints[0]['P'])
    return dict(max_invariant_error=max_invariant, max_endpoint_error=max_endpoint,
                max_final_residual=max_residual, RK4_step=0.004, final_time=40,
                cases=cases, euler_endpoints_at_time_1=endpoints)


def main():
    start = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    # RLIMIT_AS is not portable on macOS; all allocations here are lists of at most
    # 16384 floats. Runtime and peak RSS are measured, not inferred from that count.
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    result = dict(dense=dense_checks(), derivatives=derivative_checks(),
                  convergence=convergence_checks(), initialization=initialization_checks(),
                  flow=flow_checks())
    result['resources'] = dict(priority=os.getpriority(os.PRIO_PROCESS, 0),
                               seconds=time.monotonic()-start,
                               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # On this Darwin machine ru_maxrss is in bytes.
    assert result['resources']['seconds'] < 1200
    assert result['resources']['peak_rss_bytes'] < 1_000_000_000
    Path('verification_data.json').write_text(json.dumps(result, indent=2) + '\n')
    lines = ['All checks passed.',
             'Dense matrix and finite differences: ' + json.dumps(result['dense'], sort_keys=True),
             'Independent derivative checks: ' + json.dumps(result['derivatives'], sort_keys=True),
             't      n       max |A_n-A|       max |B_n-B|       max |P_n-P|']
    for row in result['convergence']:
        lines.append(f"{row['t']:<4} {row['n']:>6}   {row['max_parallel_error']:.9g}   "
                     f"{row['max_perpendicular_error']:.9g}   {row['max_output_product_error']:.9g}")
    lines.append('Initialization: ' + json.dumps(result['initialization'], sort_keys=True))
    lines.append('Limiting flow: ' + json.dumps({k: v for k, v in result['flow'].items()
                                               if k not in ['cases', 'euler_endpoints_at_time_1']}, sort_keys=True))
    lines.append('Resources: ' + json.dumps(result['resources'], sort_keys=True))
    output = '\n'.join(lines) + '\n'
    Path('verification_output.txt').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
