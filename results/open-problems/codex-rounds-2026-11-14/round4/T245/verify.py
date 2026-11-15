"""Independent small checks for the T245 gradient-flow closure.

Run from this folder: OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
Standard library only. All writes are confined to this folder.
"""

import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction as F

I = (1., 0., 0., 1.)
Z = (0., 0., 0., 0.)
DATA = [((1., 0.), .2), ((0., 1.), -.6), ((.4, -.7), .9)]
TWO = [((1., 0.), 1.), ((0., 1.), 1.)]


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sc(a, s):
    return tuple(s*x for x in a)


def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def tr(a):
    return a[0], a[2], a[1], a[3]


def mv(a, x):
    return a[0]*x[0]+a[1]*x[1], a[2]*x[0]+a[3]*x[1]


def outer(x, y):
    return x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1]


def error(a, b):
    return max(abs(x-y) for x, y in zip(a, b))


def p_add(a, b):
    return [sum(v[i] if i < len(v) else F(0) for v in (a, b))
            for i in range(max(len(a), len(b)))]


def p_mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def integ(a):
    return sum(x/F(i+1) for i, x in enumerate(a))


def exact_earlier_checks():
    rows = []
    for eta in (F(1, 5), F(2, 5), F(7, 8)):
        a = eta/2
        weight = [1+a*a, -2*a*a, a*a]
        actual = (integ(weight), integ(p_mul(weight, [0, a])),
                  integ(p_mul(weight, [0, a])),
                  integ(p_mul(weight, [1, 0, a*a])))
        expected = (1+eta**2/12, eta/4+eta**3/96,
                    eta/4+eta**3/96, 1+eta**2/6+eta**4/480)
        assert actual == expected
        assert integ(weight) == 1+eta**2/12
        pp = (F(1), a, F(0), F(1))
        hh = mm(tr(pp), pp)
        comm = add(mm(actual, hh), sc(mm(hh, actual), -1))
        assert comm[1] == eta**3/48+eta**5/640
        c1 = (F(0), a, F(0), F(0))
        defect = sc(add(mm(c1, tr(c1)), sc(mm(tr(c1), c1), -1)), -1)
        assert defect == (-eta**2/4, 0, 0, eta**2/4)
        ends = []
        for z in (F(0), F(1, 3), F(1)):
            uu = (F(1), a*z, F(0), F(1))
            back = (F(1), a*(1-z))
            g1 = (eta/4, (eta-1)/2)
            c2 = add(c1, sc(outer(back, mv(uu, g1)), -eta))
            assert c2[3] == eta**2*(1-eta)*(1-z)/4
            if z in (0, 1):
                ends.append(c2)
        comm2 = add(mm(ends[0], ends[1]), sc(mm(ends[1], ends[0]), -1))
        assert comm2[2] == eta**6/32
        rows.append(dict(eta=str(eta), M1=[str(x) for x in actual],
                         first_step_kernel_commutator_12=str(comm[1]),
                         second_step_profile_commutator_21=str(comm2[2])))
    return dict(exact_rational_cases=rows, all_identities_exact=True)


def exact_finite_defect():
    """Raw finite-layer GD: linear terms cancel, leaving the quadratic defect."""
    ws = [(F(1), F(1, 5), F(-1, 7), F(4, 5)),
          (F(6, 5), F(-1, 9), F(1, 8), F(1))]
    eta, n = F(1, 6), 7
    gg = (F(2, 3), F(-1, 4))
    # grad_l = suffix^T e (prefix g)^T; no matrix-power formula.
    grad0 = outer(ws[1][:2], gg)
    grad1 = outer((F(1), F(0)), mv(ws[0], gg))
    new = [add(w, sc(grad, -eta/n)) for w, grad in zip(ws, (grad0, grad1))]
    old_balance = add(mm(ws[0], tr(ws[0])), sc(mm(tr(ws[1]), ws[1]), -1))
    new_balance = add(mm(new[0], tr(new[0])), sc(mm(tr(new[1]), new[1]), -1))
    expected_change = sc(add(mm(grad0, tr(grad0)),
                             sc(mm(tr(grad1), grad1), -1)), eta**2/n**2)
    assert add(new_balance, sc(old_balance, -1)) == expected_change
    return dict(exact=True, balance_change=[str(x) for x in expected_change])


def eig(a):
    """Eigenvalues and rank-one projectors of a symmetric positive 2x2 matrix."""
    mid = (a[0]+a[3])/2
    rad = math.hypot((a[0]-a[3])/2, a[1])
    hi = mid+rad
    lo = (a[0]*a[3]-a[1]*a[2])/hi
    assert lo > 0, (a, lo)
    if rad < 1e-14*mid:
        return [(mid, (1., 0., 0., 0.)), (mid, (0., 0., 0., 1.))]
    ph = sc(add(a, sc(I, -lo)), 1/(hi-lo))
    return [(hi, ph), (lo, add(I, sc(ph, -1)))]


def power(a, z):
    out = Z
    for val, proj in eig(a):
        out = add(out, sc(proj, val**z))
    return out


def logmean(a, b):
    delta = math.log(b/a)
    return a if abs(delta) < 1e-15 else a*math.expm1(delta)/delta


def statistics(p, bias, data):
    rr = [bias+mv(p, x)[0]-y for x, y in data]
    h = sum(rr)/len(rr)
    g = tuple(sum(r*x[j] for r, (x, _) in zip(rr, data))/len(rr) for j in (0, 1))
    loss = sum(r*r for r in rr)/(2*len(rr))
    return h, g, loss


def closed(p, t, s, g):
    """Spectral projector/logarithmic mean evaluation, no depth integration."""
    left, right = eig(mm(p, tr(p))), eig(mm(tr(p), p))
    gg = (g[0], g[1], 0., 0.)
    op, mat, beta = Z, Z, 0.
    for a, lp in left:
        beta += t*lp[0]*logmean(a, s*s)
        for b, rp in right:
            weight = t*logmean(a, b)
            op = add(op, sc(mm(mm(lp, gg), rp), weight))
            mat = add(mat, sc(rp, weight*lp[0]))
    return sc(op, -1), mat, beta


def endpoint_rhs(y, t, s, data):
    p, bias = y[:4], y[4]
    h, g, _ = statistics(p, bias, data)
    dp, _, _ = closed(p, t, s, g)
    return (*dp, -h)


def rk4(y, dt, rhs):
    k1 = rhs(y)
    k2 = rhs(add(y, sc(k1, dt/2)))
    k3 = rhs(add(y, sc(k2, dt/2)))
    k4 = rhs(add(y, sc(k3, dt)))
    return add(y, sc(add(add(k1, sc(k2, 2)), add(sc(k3, 2), k4)), dt/6))


def endpoint_run(t, s, data, final=.4, dt=.002):
    count = round(final/dt)
    dt = final/count
    y = (*sc(I, s), 0.)
    rhs = lambda state: endpoint_rhs(state, t, s, data)
    initial_loss = statistics(y[:4], y[4], data)[2]
    previous_loss = initial_loss
    max_bound_excess = 0.
    for k in range(count):
        y = rk4(y, dt, rhs)
        loss = statistics(y[:4], y[4], data)[2]
        assert loss <= previous_loss+1e-12
        previous_loss = loss
        elapsed = (k+1)*dt
        vals = [x[0] for x in eig(mm(tr(y[:4]), y[:4]))]
        for val in vals:
            excess = abs(math.log(math.sqrt(val)/s))-math.sqrt(t*elapsed*initial_loss)
            max_bound_excess = max(max_bound_excess, excess)
        assert abs(y[4]) <= math.sqrt(elapsed*initial_loss)+1e-10
    assert max_bound_excess < 1e-10
    _, mat, beta = closed(y[:4], t, s, (0., 0.))
    return dict(P=y[:4], b=y[4], M=mat, B=beta, loss=previous_loss,
                singular_value_bound_excess=max_bound_excess)


def state_error(a, b):
    return max(error(a['P'], b['P']), abs(a['b']-b['b']),
               error(a['M'], b['M']), abs(a['B']-b['B']))


def spectral_checks():
    maximum = 0.
    count = 128
    for p in (I, sc(I, 1.3), (1., .6, -.3, 1.2), (.8, -.7, .5, 1.1)):
        t, s, g = .7, 1.2, (.3, -.6)
        dp, mat, beta = closed(p, t, s, g)
        qop, qm, qb = Z, Z, 0.
        for j in range(count+1):
            z = j/count
            weight = (1 if j in (0, count) else (4 if j % 2 else 2))/(3*count)
            aa, bb = power(mm(p, tr(p)), 1-z), power(mm(tr(p), p), z)
            qop = add(qop, sc(mm(mm(aa, (g[0], g[1], 0., 0.)), bb), -t*weight))
            qm = add(qm, sc(bb, t*weight*aa[0]))
            qb += t*weight*s**(2*z)*aa[0]
        maximum = max(maximum, error(dp, qop), error(mat, qm), abs(beta-qb))
    assert maximum < 1e-8
    # Independent central differences of the kernel yield the earlier initial rate.
    t, s, eps = .7, 1.3, 1e-6
    _, g, _ = statistics(sc(I, s), 0., DATA)
    dp = ( -t*s*s*g[0], -t*s*s*g[1], 0., 0.)
    plus, minus = add(sc(I, s), sc(dp, eps)), add(sc(I, s), sc(dp, -eps))
    _, mp, bp = closed(plus, t, s, g)
    _, mm0, bm = closed(minus, t, s, g)
    numeric = sc(add(mp, sc(mm0, -1)), 1/(2*eps))
    expected = sc((2*g[0], g[1]/2, g[1]/2, g[0]), -t*t*s**3)
    rate_error = max(error(numeric, expected), abs((bp-bm)/(2*eps)+t*t*s**3*g[0]))
    assert rate_error < 2e-8
    # Misusing the balanced formula after one discrete step has the predicted error.
    rows = []
    for eta in (.04, .02, .01, .005):
        p = (1., eta/2, 0., 1.)
        _, m, b = closed(p, 1., 1., (0., 0.))
        actual22, actualb = 1+eta*eta/6+eta**4/480, 1+eta*eta/12
        rows.append(dict(eta=eta, M22_difference_over_eta2=(m[3]-actual22)/eta**2,
                         B_difference_over_eta2=(b-actualb)/eta**2))
    assert abs(rows[-1]['M22_difference_over_eta2']-1/24) < 1e-6
    assert abs(rows[-1]['B_difference_over_eta2']-1/48) < 1e-6
    return dict(spectral_vs_depth_quadrature_max_error=maximum,
                initial_rate_error=rate_error, wrong_discrete_formula=rows)


def finite_layer_rhs(y, ll, n, data):
    ws = [y[4*j:4*j+4] for j in range(ll)]
    prefixes = [I]
    for w in ws:
        prefixes.append(mm(w, prefixes[-1]))
    h, g, _ = statistics(prefixes[-1], y[-1], data)
    derivatives, suffix = [None]*ll, I
    for j in range(ll-1, -1, -1):
        derivatives[j] = sc(outer(suffix[:2], mv(prefixes[j], g)), -1/n)
        suffix = mm(suffix, ws[j])
    return tuple(x for mat in derivatives for x in mat)+(-h,)


def finite_layer_state(y, gains, n):
    ll = len(gains)
    ws = [y[4*j:4*j+4] for j in range(ll)]
    prefixes, perp = [I], [1.]
    for w, gain in zip(ws, gains):
        prefixes.append(mm(w, prefixes[-1]))
        perp.append(perp[-1]*gain*gain)
    mat, beta, suffix = Z, 0., I
    for j in range(ll-1, -1, -1):
        weight = (suffix[0]**2+suffix[1]**2)/n
        mat = add(mat, sc(mm(tr(prefixes[j]), prefixes[j]), weight))
        beta += weight*perp[j]
        suffix = mm(suffix, ws[j])
    imbalance = max((error(mm(ws[j], tr(ws[j])), mm(tr(ws[j+1]), ws[j+1]))
                     for j in range(ll-1)), default=0.)
    return dict(P=prefixes[-1], b=y[-1], M=mat, B=beta, imbalance=imbalance)


def finite_layer_checks():
    rows = []
    max_power_sum_error = 0.
    for t, s, data in ((.5, .7, DATA), (1., 1., TWO), (2., 1.3, DATA)):
        reference = endpoint_run(t, s, data)
        refined = endpoint_run(t, s, data, dt=.001)
        assert state_error(reference, refined) < 1e-9
        for n in (16, 64, 256):
            ll = round(t*n)
            gains = [s**(1/ll)]*ll
            y = tuple(x for gain in gains for x in sc(I, gain))+(0.,)
            rhs = lambda state: finite_layer_rhs(state, ll, n, data)
            for _ in range(40):
                y = rk4(y, .01, rhs)
            state = finite_layer_state(y, gains, n)
            assert state['imbalance'] < 1e-9
            # Exact finite-depth balanced sum has exponents summing to 1-1/L.
            p = state['P']
            aa, hh = mm(p, tr(p)), mm(tr(p), p)
            predicted_m, predicted_b = Z, 0.
            for j in range(ll):
                suffix_gram = power(aa, (ll-j-1)/ll)
                prefix_gram = power(hh, j/ll)
                predicted_m = add(predicted_m, sc(prefix_gram, suffix_gram[0]/n))
                predicted_b += suffix_gram[0]*s**(2*j/ll)/n
            max_power_sum_error = max(max_power_sum_error, error(predicted_m, state['M']),
                                      abs(predicted_b-state['B']))
            rows.append(dict(t=t, S=s, n=n, L=ll,
                             max_full_state_error=state_error(state, reference),
                             balance_error=state['imbalance']))
        assert rows[-1]['max_full_state_error'] < rows[-3]['max_full_state_error']/5
    # Unequal gains do not obey exact balancedness, but approach the same limit.
    unequal = []
    t, s = 1., 1.3
    reference = endpoint_run(t, s, DATA)
    for n in (32, 128, 512):
        logs = [.35*math.sin(1.7*j)/math.sqrt(n) for j in range(n)]
        shift = (math.log(s)-sum(logs))/n
        gains = [math.exp(x+shift) for x in logs]
        endpoints = []
        for ordered in (gains, gains[::-1]):
            y = tuple(x for gain in ordered for x in sc(I, gain))+(0.,)
            rhs = lambda state: finite_layer_rhs(state, n, n, DATA)
            for _ in range(40):
                y = rk4(y, .01, rhs)
            endpoints.append(finite_layer_state(y, ordered, n))
        unequal.append(dict(n=n, gain_order_difference=state_error(*endpoints),
                            max_error=max(state_error(v, reference) for v in endpoints)))
    assert unequal[-1]['max_error'] < unequal[0]['max_error']/4
    assert max_power_sum_error < 1e-9
    return dict(balanced_layers=rows, unequal_gains=unequal,
                exact_finite_depth_power_sum_error=max_power_sum_error)


def earlier_profile_checks():
    # Import does not run main. Disable bytecode so the old folder is never written.
    sys.dont_write_bytecode = True
    path = Path('~/codex_op_1114r3/briefs/T245/verify.py')
    spec = importlib.util.spec_from_file_location('previous_t245_readonly', path)
    previous = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    ref = endpoint_run(1., 1., TWO)
    rows = []
    for steps in (10, 20, 40, 80):
        eta = .4/steps
        states, profiles = previous.profile_run(1., 1., eta, TWO, steps, 64)
        last = states[-1]
        actual = dict(P=previous.scale(last['Q'], last['S']), b=last['b'], M=last['M'], B=last['B'])
        rows.append(dict(eta=eta, steps=steps, error_to_endpoint_flow=state_error(actual, ref)))
    assert rows[-1]['error_to_endpoint_flow'] < rows[0]['error_to_endpoint_flow']/5
    # Two depth grids distinguish depth error from the leading Euler error.
    fine, _ = previous.profile_run(1., 1., .005, TWO, 80, 128)
    depth_error = max(error(fine[-1]['M'], states[-1]['M']),
                      error(fine[-1]['Q'], states[-1]['Q']),
                      abs(fine[-1]['B']-states[-1]['B']))
    assert depth_error < 1e-7
    return dict(discrete_profile_to_flow=rows, depth_grid_refinement_error=depth_error)


def edge_checks():
    results = []
    for t, s, data in ((.5, .4, [((1., 0.), -1.)]),
                       (2., 2.5, [((1., 0.), 3.)]),
                       (1., 1., [((1., 0.), 1.), ((0., 1.), 0.)]),
                       (1., 1.3, [((0., 0.), 1.), ((0., 0.), 2.)])):
        state = endpoint_run(t, s, data)
        results.append(dict(t=t, S=s, loss=state['loss'], P=state['P'], b=state['b']))
        if all(x == (0., 0.) for x, _ in data):
            assert error(state['P'], sc(I, s)) < 1e-13
            assert abs(state['b']-1.5*(1-math.exp(-.4))) < 1e-10
        if len(data) == 1:
            assert abs(1/state['P'][0]+t*state['b']-1/s) < 1e-8
            p = state['P'][0]
            z = 2*math.log(p/s)
            expected_b = t*s*s*(math.expm1(z)/z if z else 1.)
            assert abs(state['M'][0]-t*p*p) < 1e-10
            assert abs(state['B']-expected_b) < 1e-10
    # Verify dissipation against a numerical derivative of the actual squared loss.
    p, bias, t, s = (1.2, .3, -.2, .9), -.1, .7, 1.1
    h, g, _ = statistics(p, bias, DATA)
    dy = endpoint_rhs((*p, bias), t, s, DATA)
    eps = 1e-6
    yp, ym = add((*p, bias), sc(dy, eps)), add((*p, bias), sc(dy, -eps))
    fd = (statistics(yp[:4], yp[4], DATA)[2]-statistics(ym[:4], ym[4], DATA)[2])/(2*eps)
    _, mat, _ = closed(p, t, s, g)
    exact = -h*h-sum(x*y for x, y in zip(g, mv(mat, g)))
    assert abs(fd-exact) < 1e-8
    return dict(cases=results, loss_dissipation_difference=abs(fd-exact))


def main():
    started = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    out = {}
    for name, check in [('earlier_exact', exact_earlier_checks),
                        ('finite_defect_exact', exact_finite_defect), ('spectral', spectral_checks),
                        ('finite_layer', finite_layer_checks), ('profile', earlier_profile_checks),
                        ('edges', edge_checks)]:
        out[name] = check()
        print(name+': '+json.dumps(out[name], sort_keys=True), flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    out['resources'] = dict(seconds=time.monotonic()-started, peak_rss_bytes=rss,
                            priority=priority, OMP_NUM_THREADS='1')
    assert rss < 1_000_000_000 and out['resources']['seconds'] < 1200
    print('resources: '+json.dumps(out['resources'], sort_keys=True), flush=True)
    print('All checks passed.', flush=True)
    Path('verification_data.json').write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
