"""Standard-library checks of the matrix profile, independent of the old script.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
All writes are relative to this script's folder.
"""

import json
import math
import os
from pathlib import Path
import random
import resource
import sys
import time

I = (1.0, 0.0, 0.0, 1.0)
ZERO = (0.0, 0.0, 0.0, 0.0)
DATA = [((1.0, 0.0), 0.2), ((0.0, 1.0), -0.6), ((0.4, -0.7), 0.9)]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, v):
    return tuple(v * x for x in a)


def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def tr(a):
    return (a[0], a[2], a[1], a[3])


def mv(a, v):
    return (a[0]*v[0]+a[1]*v[1], a[2]*v[0]+a[3]*v[1])


def outer(a, b):
    return (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])


def inv(a):
    det = a[0]*a[3]-a[1]*a[2]
    assert abs(det) > 1e-10
    return (a[3]/det, -a[1]/det, -a[2]/det, a[0]/det)


def err(a, b):
    return max(abs(x-y) for x, y in zip(a, b))


def residuals(q, s, b, data):
    rr = [b+s*mv(q, x)[0]-y for x, y in data]
    h = sum(rr)/len(data)
    g = tuple(sum(r*x[j] for r, (x, _) in zip(rr, data))/len(data)
              for j in range(2))
    return h, g


def finite_state(cs, gains, n, b, data):
    ds = [add(I, scale(c, 1/n)) for c in cs]
    qs = [I]
    for d in ds:
        qs.append(mm(d, qs[-1]))
    rs = [I] * len(ds)
    acc = I
    for l in range(len(ds)-1, -1, -1):
        rs[l] = acc
        acc = mm(acc, ds[l])
    s = math.prod(gains)
    mat, beta = ZERO, 0.0
    for l, gain in enumerate(gains):
        back = rs[l][:2]  # R_l^T e1, a column represented as a pair.
        weight = s*s/(n*gain*gain)*(back[0]**2+back[1]**2)
        mat = add(mat, scale(mm(tr(qs[l]), qs[l]), weight))
        beta += weight
    h, g = residuals(qs[-1], s, b, data)
    return dict(M=mat, B=beta, Q=qs[-1], qs=qs, rs=rs, S=s, b=b, h=h, g=g)


def finite_step(cs, gains, n, b, data, eta):
    state = finite_state(cs, gains, n, b, data)
    new = []
    for l, (c, gain) in enumerate(zip(cs, gains)):
        grad = outer(state['rs'][l][:2], mv(state['qs'][l], state['g']))
        new.append(add(c, scale(grad, -eta*state['S']/(gain*gain))))
    return new, b-eta*state['h']


def profile_state(cs, t, s, b, data):
    """RK4 in depth with linear C interpolation; Simpson kernel quadrature."""
    count = len(cs)-1
    assert count % 2 == 0
    step = 1/count
    us = [I]
    for j in range(count):
        mid = scale(add(cs[j], cs[j+1]), 0.5)
        u = us[-1]
        k1 = scale(mm(cs[j], u), t)
        k2 = scale(mm(mid, add(u, scale(k1, step/2))), t)
        k3 = scale(mm(mid, add(u, scale(k2, step/2))), t)
        k4 = scale(mm(cs[j+1], add(u, scale(k3, step))), t)
        increment = add(add(k1, scale(k2, 2)), add(scale(k3, 2), k4))
        us.append(add(u, scale(increment, step/6)))
    vs = [mm(us[-1], inv(u)) for u in us]
    mat, beta = ZERO, 0.0
    for j, (u, v) in enumerate(zip(us, vs)):
        simpson = 1 if j in (0, count) else (4 if j % 2 else 2)
        weight = t*s*s*simpson/(3*count)*(v[0]**2+v[1]**2)
        mat = add(mat, scale(mm(tr(u), u), weight))
        beta += weight
    h, g = residuals(us[-1], s, b, data)
    return dict(M=mat, B=beta, Q=us[-1], us=us, vs=vs, S=s, b=b, h=h, g=g)


def profile_run(t, s, eta, data, steps, grid):
    cs, b, states, profiles = [ZERO]*(grid+1), 0.0, [], []
    for k in range(steps+1):
        state = profile_state(cs, t, s, b, data)
        states.append({key: state[key] for key in ('M', 'B', 'Q', 'S', 'b')})
        profiles.append(cs)
        if k < steps:
            new = []
            for c, u, v in zip(cs, state['us'], state['vs']):
                new.append(add(c, scale(outer(v[:2], mv(u, state['g'])), -eta*s)))
            cs, b = new, b-eta*state['h']
    return states, profiles


def state_error(a, b):
    return max(err(a['M'], b['M']), abs(a['B']-b['B']),
               err(scale(a['Q'], a['S']), scale(b['Q'], b['S'])),
               abs(a['b']-b['b']))


def dense_output(ws, bias, x):
    v = list(x)
    for w in ws:
        v = [sum(a*b for a, b in zip(row, v)) for row in w]
    return bias+v[0]


def numerical_theta_gradient(ws, bias, x):
    n, eps = len(x), 2e-5
    result = []
    for w in ws:
        grad = []
        for i in range(n):
            for j in range(n):
                original = w[i][j]
                w[i][j] = original+eps/math.sqrt(n)
                plus = dense_output(ws, bias, x)
                w[i][j] = original-eps/math.sqrt(n)
                minus = dense_output(ws, bias, x)
                w[i][j] = original
                grad.append((plus-minus)/(2*eps))
        result.append(grad)
    return result


def dense_from_blocks(cs, gains, n):
    ws = []
    for c, s in zip(cs, gains):
        a = scale(add(I, scale(c, 1/n)), s)
        w = [[float(i == j)*s for j in range(n)] for i in range(n)]
        w[0][0], w[0][1], w[1][0], w[1][1] = a
        ws.append(w)
    return ws


def dense_checks():
    n, gains, eta = 3, [0.91, 1.06, 0.97, 1.03], 0.08
    cs, b = [ZERO]*len(gains), 0.0
    xs = [(1., 0., 0.), (0., 1., 0.), (0.4, -0.3, 0.8)]
    max_kernel = max_update = 0.0
    count = 0
    for _ in range(4):
        state = finite_state(cs, gains, n, b, DATA)
        ws = dense_from_blocks(cs, gains, n)
        grads = [numerical_theta_gradient(ws, b, x) for x in xs]
        count += len(xs)*len(gains)*n*n
        for i, x in enumerate(xs):
            for j, xp in enumerate(xs):
                numeric = 1+sum(sum(a*c for a, c in zip(ga, gb))
                                for ga, gb in zip(grads[i], grads[j]))
                formula = 1+sum(a*c for a, c in zip(x[:2], mv(state['M'], xp[:2])))
                formula += state['B']*x[2]*xp[2]
                max_kernel = max(max_kernel, abs(numeric-formula))
        loss_grad = [[0.0]*(n*n) for _ in gains]
        for x, y in DATA:
            padded = (*x, 0.)
            r = dense_output(ws, b, padded)-y
            gg = numerical_theta_gradient(ws, b, padded)
            for l in range(len(gains)):
                for j in range(n*n):
                    loss_grad[l][j] += r*gg[l][j]/len(DATA)
        new_cs, new_b = finite_step(cs, gains, n, b, DATA, eta)
        expected = dense_from_blocks(new_cs, gains, n)
        for l, w in enumerate(ws):
            for i in range(n):
                for j in range(n):
                    updated = w[i][j]-eta*loss_grad[l][i*n+j]/math.sqrt(n)
                    max_update = max(max_update, abs(updated-expected[l][i][j]))
        cs, b = new_cs, new_b
    assert max_kernel < 1e-8 and max_update < 1e-8
    return dict(max_numerical_kernel_error=max_kernel,
                max_numerical_update_error=max_update,
                numerical_kernel_partials=count)


def scalar_recheck():
    n, gains, eta, y = 9, [0.92, 1.05, 0.98, 1.02, 1.01, 0.96], 0.05, 0.2
    cs, b, aa = [ZERO]*len(gains), 0.0, list(gains)
    max_error = 0.0
    for _ in range(6):
        state = finite_state(cs, gains, n, b, [((1., 0.), y)])
        p = math.prod(aa)
        parallel = sum(math.prod(aa[:l]+aa[l+1:])**2 for l in range(len(aa)))/n
        perp = sum(math.prod(aa[l+1:])**2*math.prod(gains[:l])**2
                   for l in range(len(aa)))/n
        max_error = max(max_error, err(state['M'], (parallel, 0., 0., perp)),
                        abs(state['B']-perp), abs(state['S']*state['Q'][0]-p))
        cs, new_b = finite_step(cs, gains, n, b, [((1., 0.), y)], eta)
        r = b+p-y
        aa = [a-eta*r*math.prod(aa[:l]+aa[l+1:])/n for l, a in enumerate(aa)]
        max_error = max(max_error, abs(new_b-(b-eta*r)))
        b = new_b
    # Direct normal-moment product is a separate check of the earlier random law.
    t, mu, sigma, n = 0.5, -0.5, 0.6, 128
    ll = round(t*n)
    product_moments = [t**r*math.prod([math.exp((2*r*mu+2*r*r*sigma*sigma)/n)]*ll)
                       for r in (1, 2)]
    normal_moments = [t**r*math.exp((2*r*mu+2*r*r*sigma*sigma)*t) for r in (1, 2)]
    moment_error = err(product_moments, normal_moments)
    assert max_error < 1e-12 and moment_error < 1e-12
    # A d=1-equivalent profile must reproduce the previous closed scalar recursion.
    states, _ = profile_run(1., 1.3, 0.05, [((1., 0.), y)], 5, 128)
    c = bias = 0.0
    limit_error = 0.0
    for state in states:
        p = 1.3*math.exp(c)
        perp = 1.3**2*(math.expm1(2*c)/(2*c) if c else 1.)
        limit_error = max(limit_error, err(state['M'], (p*p, 0., 0., perp)),
                          abs(state['B']-perp), abs(state['b']-bias))
        r = bias+p-y
        c, bias = c-0.05*p*r, bias-0.05*r
    assert limit_error < 1e-9
    return dict(exact_scalar_orbit_and_kernel_error=max_error,
                normal_moment_product_error=moment_error,
                scalar_limit_vs_matrix_profile_error=limit_error)


def rate_checks():
    n, gains = 9, [0.92, 1.05, 0.98, 1.02, 1.01, 0.96]
    cs, eps = [ZERO]*len(gains), 1e-6
    initial = finite_state(cs, gains, n, 0., DATA)
    s, g = initial['S'], initial['g']
    pairs = sum(a**-2*b**-2 for j, a in enumerate(gains) for b in gains[j+1:])
    pairs_second = (sum(a**-2 for a in gains)**2-sum(a**-4 for a in gains))/2
    e = (1., 0.)
    exact = scale(add(scale(I, 2*g[0]), add(outer(e, g), outer(g, e))), -s**3*pairs/n**2)
    exact_b = -2*s**3*pairs/n**2*g[0]
    cp, bp = finite_step(cs, gains, n, 0., DATA, eps)
    cm, bm = finite_step(cs, gains, n, 0., DATA, -eps)
    plus, minus = finite_state(cp, gains, n, bp, DATA), finite_state(cm, gains, n, bm, DATA)
    numeric = scale(add(plus['M'], scale(minus['M'], -1)), 1/(2*eps))
    numeric_b = (plus['B']-minus['B'])/(2*eps)
    error = max(err(numeric, exact), abs(numeric_b-exact_b))
    assert error < 1e-8 and abs(pairs-pairs_second) < 1e-12
    # One layer has an exactly constant full kernel for every weight state.
    single = [ZERO]
    one0 = finite_state(single, [1.2], 7, 0., DATA)
    single, bias = finite_step(single, [1.2], 7, 0., DATA, 0.2)
    one1 = finite_state(single, [1.2], 7, bias, DATA)
    assert err(one0['M'], one1['M']) == 0 and one0['B'] == one1['B']
    return dict(pair_sum=pairs, pair_sum_second_way=pairs_second,
                analytic_M_rate=exact, numerical_M_rate=numeric,
                max_rate_error=error, one_layer_constant_kernel=True)


def explicit_checks():
    eta, data, grid = 0.2, [((1., 0.), 1.), ((0., 1.), 1.)], 128
    states, profiles = profile_run(1., 1., eta, data, 2, grid)
    expected = (1+eta**2/12, eta/4+eta**3/96,
                eta/4+eta**3/96, 1+eta**2/6+eta**4/480)
    matrix_error = err(states[1]['M'], expected)
    beta_error = abs(states[1]['B']-(1+eta**2/12))
    c22_error = max(abs(c[3]-eta**2*(1-eta)*(1-j/grid)/4)
                    for j, c in enumerate(profiles[2]))
    commutator = add(mm(profiles[2][0], profiles[2][-1]),
                     scale(mm(profiles[2][-1], profiles[2][0]), -1))
    assert matrix_error < 1e-10 and beta_error < 1e-12 and c22_error < 1e-12
    assert max(abs(a) for a in commutator) > 1e-5
    commutator_entry_error = abs(commutator[2]-eta**6/32)
    assert commutator_entry_error < 1e-14
    # Initial off-diagonal rate by symmetric eta differences, independent of (22).
    eps = 1e-5
    plus, _ = profile_run(1., 1., eps, data, 1, 32)
    minus, _ = profile_run(1., 1., -eps, data, 1, 32)
    rate = scale(add(plus[1]['M'], scale(minus[1]['M'], -1)), 1/(2*eps))
    assert err(rate, (0., 0.25, 0.25, 0.)) < 1e-8
    return dict(eta=eta, M1_numerical=states[1]['M'], M1_polynomial=expected,
                B1=states[1]['B'], polynomial_error=matrix_error,
                B_polynomial_error=beta_error, C2_22_formula_error=c22_error,
                C2_22_at_depth_zero=profiles[2][0][3],
                C2_22_at_depth_one=profiles[2][-1][3],
                endpoint_commutator=commutator,
                commutator_entry_formula_error=commutator_entry_error,
                initial_M_rate=rate)


def convergence_checks():
    rows, refs, eta, steps, s = [], {}, 0.06, 4, 1.3
    grid_errors = []
    for t in (0.5, 1., 2.):
        coarse, _ = profile_run(t, s, eta, DATA, steps, 512)
        fine, _ = profile_run(t, s, eta, DATA, steps, 1024)
        reference, _ = profile_run(t, s, eta, DATA, steps, 2048)
        ec = max(state_error(a, b) for a, b in zip(coarse, reference))
        ef = max(state_error(a, b) for a, b in zip(fine, reference))
        assert ef < 1e-8 and ef <= ec+1e-13
        grid_errors.append(dict(t=t, grid512_vs_2048=ec, grid1024_vs_2048=ef))
        refs[t] = reference
        for n in (32, 128, 512, 2048, 8192):
            ll = round(t*n)
            rng = random.Random(2451000+n+ll)
            logs = [0.6*rng.gauss(0, 1)/math.sqrt(n) for _ in range(ll)]
            shift = (math.log(s)-sum(logs))/ll
            gains = [math.exp(z+shift) for z in logs]
            cs, b, maximum = [ZERO]*ll, 0., 0.
            for k in range(steps+1):
                state = finite_state(cs, gains, n, b, DATA)
                maximum = max(maximum, state_error(state, reference[k]))
                if k < steps:
                    cs, b = finite_step(cs, gains, n, b, DATA, eta)
            rows.append(dict(t=t, n=n, L=ll, max_state_error=maximum,
                             max_gain_deviation=max(abs(g-1) for g in gains)))
        assert rows[-1]['max_state_error'] < 0.005
        assert rows[-1]['max_state_error'] < rows[-5]['max_state_error']
    # Same gains, opposite order: this is not finite-size permutation invariance.
    order_rows = []
    for n in (128, 512, 2048):
        ll = n
        gains = [math.exp(math.log(s)/ll+0.6*math.sin(j*1.7)/math.sqrt(n)) for j in range(ll)]
        correction = math.exp((math.log(s)-sum(math.log(g) for g in gains))/ll)
        gains = [g*correction for g in gains]
        trajectories = []
        for ordered in (gains, gains[::-1]):
            cs, b, trajectory = [ZERO]*ll, 0., []
            for k in range(steps+1):
                trajectory.append(finite_state(cs, ordered, n, b, DATA))
                if k < steps:
                    cs, b = finite_step(cs, ordered, n, b, DATA, eta)
            trajectories.append(trajectory)
        order_rows.append(dict(n=n, max_order_difference=max(
            state_error(a, b) for a, b in zip(*trajectories))))
    assert order_rows[-1]['max_order_difference'] < order_rows[0]['max_order_difference']
    # Zero residuals and zero training inputs cover different degeneracies.
    stationary_data = [((1., 0.), 1.), ((0., 1.), 0.)]
    stationary, stationary_profiles = profile_run(1., 1., .2, stationary_data, 3, 32)
    assert all(c == ZERO for prof in stationary_profiles for c in prof)
    zero_data = [((0., 0.), 1.), ((0., 0.), 2.)]
    zero_states, zero_profiles = profile_run(1., 1.3, .2, zero_data, 3, 32)
    assert all(c == ZERO for prof in zero_profiles for c in prof)
    assert zero_states[-1]['b'] > 0
    return dict(profile_grid_errors=grid_errors, finite_size=rows,
                gain_order_checks=order_rows,
                zero_residual_stationary=True, zero_inputs_bias_only=True)


def main():
    started = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    result = dict(scalar_recheck=scalar_recheck(), dense=dense_checks(),
                  rates=rate_checks(), explicit=explicit_checks(),
                  convergence=convergence_checks())
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    result['resources'] = dict(seconds=time.monotonic()-started, peak_rss_bytes=rss,
                               priority=priority, OMP_NUM_THREADS='1')
    assert result['resources']['seconds'] < 1200 and rss < 1_000_000_000
    lines = ['All checks passed.']
    for key in ('scalar_recheck', 'dense', 'rates', 'explicit'):
        lines.append(key+': '+json.dumps(result[key], sort_keys=True))
    lines.append('t      n       max full-state error')
    for row in result['convergence']['finite_size']:
        lines.append(f"{row['t']:<4} {row['n']:>6}   {row['max_state_error']:.10g}")
    lines.append('Profile quadrature refinement: '+json.dumps(result['convergence']['profile_grid_errors']))
    lines.append('Gain-order checks: '+json.dumps(result['convergence']['gain_order_checks']))
    lines.append('Degenerate cases: stationary residuals and bias-only training passed.')
    lines.append('Resources: '+json.dumps(result['resources'], sort_keys=True))
    output = '\n'.join(lines)+'\n'
    Path('verification_data.json').write_text(json.dumps(result, indent=2)+'\n')
    Path('verification_output.txt').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
