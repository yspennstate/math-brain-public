"""Finite Taylor-jet correction. Standard library; earlier folders read-only.

OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
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

sys.dont_write_bytecode = True
BASE = Path('~')
spec = importlib.util.spec_from_file_location(
    'r5_readonly', BASE/'codex_op_1114r5/briefs/T245/verify.py')
r5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r5)
q, raw = r5.q, r5.old
add, sc, mm, tr, mv, outer, err = q.add, q.sc, q.mm, q.tr, q.mv, q.outer, q.error
I, Z = (1, 0, 0, 1), (0, 0, 0, 0)


def sub(a, b):
    return add(a, sc(b, -1))


def comm(a, b):
    return sub(mm(a, b), mm(b, a))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def coefficients(kmat, v, g, t, degree):
    """R,N coefficients. Works exactly for rational input, including K=cI."""
    powers = [I]
    for j in range(1, degree+1):
        powers.append(sc(mm(kmat, powers[-1]), F(1, j)))
    rr = [Z]
    if degree:
        rr.append(sc(outer(v, g), -t))
    for j in range(2, degree+1):
        rr.append(sc(comm(kmat, rr[-1]), F(-1, j)))
    dd = [outer(g, g)]
    for j in range(1, degree+1):
        dd.append(sc(add(mm(kmat, dd[-1]), mm(dd[-1], kmat)), F(1, j)))
    aa = [dot(g, mv(power, g)) for power in powers]
    bb = [(-1)**j*dot(v, mv(power, v)) for j, power in enumerate(powers)]
    nn = []
    for j in range(degree+1):
        value = sc(outer(v, v), aa[j])
        for a in range(j+1):
            value = sub(value, sc(dd[j-a], bb[a]))
        nn.append(value)
    return rr, nn


def jet_derivative(jets, rr, nn, t):
    out = []
    for j in range(len(jets)):
        value = sc(nn[j], -t)
        for a in range(1, j+1):
            value = add(value, add(mm(tr(rr[a]), jets[j-a]), mm(jets[j-a], rr[a])))
        out.append(value)
    return out


def evaluate(jets, z):
    out = Z
    for j in reversed(jets):
        out = add(sc(out, z), j)
    return out


def log_gram(p, s):
    h = sc(mm(tr(p), p), 1/(s*s))
    k = Z
    for value, projector in q.eig(h):
        k = add(k, sc(projector, math.log(value)))
    return k


def rhs(y, t, s, data, degree, grid):
    p, bias, sensitivity, beta = y[:4], y[4], y[5:9], y[9]
    jets = [y[10+4*j:14+4*j] for j in range(degree+1)]
    h, g, _ = q.statistics(p, bias, data)
    f = q.closed(p, t, s, g)[0]
    rr, nn = coefficients(log_gram(p, s), p[:2], g, t, degree)
    jd = jet_derivative(jets, rr, nn, t)
    jf = [evaluate(jets, j/grid) for j in range(grid+1)]
    geo = r5.geometric(p, bias, jf, t, s, data)
    fun = lambda matrix, bb: q.endpoint_rhs((*matrix, bb), t, s, data)[:4]
    d_sensitivity = r5.directional(fun, p, bias, (*sensitivity, beta))
    d_flow = r5.directional(fun, p, bias, (*f, -h))
    ps = add(add(d_sensitivity, geo['F']), sub(geo['T'], sc(d_flow, .5)))
    bs = -r5.dh((*sensitivity, beta), data)+.5*r5.dh((*f, -h), data)
    return (*f, -h, *ps, bs, *(x for mat in jd for x in mat))


def run(t, s, data, degree, final=.4, dt=.002, grid=64):
    steps = round(final/dt)
    dt = final/steps
    state = (*sc(I, s), 0., *Z, 0., *(0. for _ in range(4*(degree+1))))
    fun = lambda y: rhs(y, t, s, data, degree, grid)
    for _ in range(steps):
        state = q.rk4(state, dt, fun)
    p, bias, sensitivity, beta = state[:4], state[4], state[5:9], state[9]
    jets = [state[10+4*j:14+4*j] for j in range(degree+1)]
    jf = [evaluate(jets, j/grid) for j in range(grid+1)]
    geo = r5.geometric(p, bias, jf, t, s, data)
    _, mat, bb = q.closed(p, t, s, (0., 0.))
    kernel = lambda matrix, bias: (*q.closed(matrix, t, s, (0., 0.))[1],
                                   q.closed(matrix, t, s, (0., 0.))[2])
    ds = r5.directional(kernel, p, bias, (*sensitivity, beta))
    return dict(P=p, b=bias, M=mat, B=bb, p=sensitivity, beta=beta,
                m=add(ds[:4], geo['M']), bcor=ds[4]+geo['B'],
                memory_M=geo['M'], memory_B=geo['B'], J=jf, jets=jets)


def exact_coefficient_checks():
    k = (F(2, 3), F(-1, 4), F(-1, 4), F(-3, 5))
    v, g, t, degree = (F(3, 5), F(-7, 4)), (F(-2, 3), F(4, 7)), F(2, 3), 8
    rr, nn = coefficients(k, v, g, t, degree)
    # Independent ordered power-series multiplication, no commutator formula.
    powers = [I]
    for j in range(1, degree+1):
        powers.append(sc(mm(powers[-1], k), F(1, j)))
    for j in range(degree):
        xx = Z
        for a in range(j+1):
            xx = sub(xx, sc(mm(mm(powers[a], outer(v, g)), powers[j-a]), (-1)**a))
        assert rr[j+1] == sc(xx, t/F(j+1))
    for j in range(degree+1):
        direct = sc(outer(v, v), dot(g, mv(powers[j], g)))
        for a in range(j+1):
            for b in range(j-a+1):
                c = j-a-b
                direct = sub(direct, sc(mm(mm(powers[b], outer(g, g)), powers[c]),
                                        (-1)**a*dot(v, mv(powers[a], v))))
        assert direct == nn[j]
    # A scalar K retains a nonzero source for nonparallel v,g.
    c = F(3, 7)
    r_scalar, n_scalar = coefficients(sc(I, c), v, g, t, degree)
    n0 = sub(sc(outer(v, v), dot(g, g)), sc(outer(g, g), dot(v, v)))
    assert n0 != Z
    for j in range(degree+1):
        assert n_scalar[j] == sc(n0, c**j/F(math.factorial(j)))
    assert all(r == Z for r in r_scalar[2:])
    # Prefix RHS unaffected by discarded coefficients.
    jets = [(F(j+1, 13), F(2-j, 11), F(2-j, 11), F(-j, 17))
            for j in range(degree+1)]
    all_rhs = jet_derivative(jets, rr, nn, t)
    for m in range(degree+1):
        assert jet_derivative(jets[:m+1], rr[:m+1], nn[:m+1], t) == all_rhs[:m+1]
    wrong_r2 = sc(comm(k, outer(v, g)), -t/2)
    wrong_error = float(err(rr[2], wrong_r2))
    assert wrong_error > .1
    # Mandatory benchmark and the two kernel constants from direct polynomial integration.
    r0, n0 = coefficients(Z, (F(1), F(0)), (F(0), F(-1, 2)), F(1), degree)
    jd = jet_derivative([Z]*(degree+1), r0, n0, F(1))
    assert jd[0] == (F(-1, 4), 0, 0, F(1, 4))
    assert all(mat == Z for mat in jd[1:])
    wb = F(1, 8)*(F(1, 2)-F(1, 3))
    assert -wb == F(-1, 48) and -2*wb == F(-1, 24)
    return dict(max_degree=degree, all_rational_identities_exact=True,
                scalar_repeated_eigenvalue_source_nonzero=True,
                truncation_rhs_prefix_exact=True,
                wrong_commutator_sign_error=wrong_error,
                initial_B_slope=str(-wb), initial_M22_slope=str(-2*wb))


def direct_sample_reference(t, s, data, final, grid=64, dt=.002):
    """Exact spectral R(z) evaluation, independent of prefix quadrature and jets."""
    indices = [0, 16, 37, 64]
    zs = [j/grid for j in indices]

    def fun(state):
        p, bias = state[:4], state[4]
        h, g, _ = q.statistics(p, bias, data)
        hmat = sc(mm(tr(p), p), 1/(s*s))
        spectral = [(math.log(val), proj) for val, proj in q.eig(hmat)]
        derivatives = []
        for i, z in enumerate(zs):
            rr = Z
            a, ai = Z, Z
            for ka, pa in spectral:
                a = add(a, sc(pa, math.exp(z*ka)))
                ai = add(ai, sc(pa, math.exp(-z*ka)))
                for kb, pb in spectral:
                    delta = kb-ka
                    phi = z if abs(delta) < 1e-14 else math.expm1(z*delta)/delta
                    rr = add(rr, sc(mm(mm(pa, outer(p[:2], g)), pb), -t*phi))
            nn = sub(sc(outer(p[:2], p[:2]), dot(g, mv(a, g))),
                     sc(mm(mm(a, outer(g, g)), a), dot(p[:2], mv(ai, p[:2]))))
            jj = state[5+4*i:9+4*i]
            derivatives.append(sub(add(mm(tr(rr), jj), mm(jj, rr)), sc(nn, t)))
        return (*q.closed(p, t, s, g)[0], -h, *(x for mat in derivatives for x in mat))

    y = (*sc(I, s), 0., *(0. for _ in range(4*len(zs))))
    steps = round(final/dt)
    for _ in range(steps):
        y = q.rk4(y, final/steps, fun)
    return indices, [y[5+4*i:9+4*i] for i in range(len(zs))]


def compression_checks():
    t, s, data, final = 2., 1.3, q.DATA, 1.2
    ref = r5.correction_run(t, s, data, final=final, grid=64, dt=.002)
    indices, direct = direct_sample_reference(t, s, data, final)
    source_error = max(err(ref['J'][i], j) for i, j in zip(indices, direct))
    assert source_error < 2e-8
    rows, previous, saved = [], None, {}
    for degree in (0, 1, 2, 4, 6, 8, 12):
        value = run(t, s, data, degree, final=final)
        field_error = max(err(a, b) for a, b in zip(value['J'], ref['J']))
        source_comparison = max(err(value['J'][i], j) for i, j in zip(indices, direct))
        memory_error = max(err(value['memory_M'], ref['memory_M']),
                           abs(value['memory_B']-ref['memory_B']))
        full_correction_error = max(err(value['p'], ref['p']),
                                    abs(value['beta']-ref['beta']),
                                    err(value['m'], ref['m']), abs(value['bcor']-ref['bcor']))
        row = dict(degree=degree, symmetric_memory_coordinates=3*(degree+1),
                   field_error=field_error, exact_R_sample_error=source_comparison,
                   memory_kernel_error=memory_error, full_correction_error=full_correction_error)
        if previous is not None:
            prefix_error = max(err(a, b) for a, b in zip(value['jets'], previous['jets']))
            row['earlier_jet_prefix_error'] = prefix_error
            assert prefix_error < 2e-13
        previous = value
        saved[degree] = value
        rows.append(row)
        print('compression_row: '+json.dumps(row, sort_keys=True), flush=True)
    assert rows[-1]['field_error'] < 2e-8
    assert rows[-1]['memory_kernel_error'] < 5e-8
    assert rows[4]['field_error'] < rows[2]['field_error']/50
    assert rows[-1]['full_correction_error'] < 5e-8
    # Refining depth evaluation and time integration does not change the dynamics' size.
    finer = run(t, s, data, 8, final=final, grid=128, dt=.001)
    refinement = max(err(finer['p'], saved[8]['p']), abs(finer['beta']-saved[8]['beta']),
                     err(finer['m'], saved[8]['m']), abs(finer['bcor']-saved[8]['bcor']))
    assert refinement < 2e-7
    return dict(t=t, S=s, final_time=final, rows=rows,
                direct_R_vs_previous_field_error=source_error,
                depth_time_refinement_error=refinement)


def discrete_checks():
    rows = []
    for t, s, data in ((.5, .7, q.DATA), (1., 1., q.TWO), (2., 1.3, q.DATA)):
        jet = run(t, s, data, 6)
        ref = r5.correction_run(t, s, data, grid=64, dt=.002)
        coefficient_error = max(err(jet['p'], ref['p']), abs(jet['beta']-ref['beta']),
                                err(jet['m'], ref['m']), abs(jet['bcor']-ref['bcor']))
        assert coefficient_error < 2e-7
        case = dict(t=t, S=s, degree=6, coefficient_error=coefficient_error, rows=[])
        previous = None
        for eta in (.04, .02, .01, .005):
            states, _ = raw.profile_run(t, s, eta, data, round(.4/eta), 128)
            actual = states[-1]
            observed = dict(P=sc(actual['Q'], s), b=actual['b'], M=actual['M'], B=actual['B'])
            predicted = dict(P=add(jet['P'], sc(jet['p'], eta)),
                             b=jet['b']+eta*jet['beta'],
                             M=add(jet['M'], sc(jet['m'], eta)),
                             B=jet['B']+eta*jet['bcor'])
            difference = q.state_error(observed, predicted)
            row = dict(eta=eta, full_state_error=difference, error_over_eta2=difference/eta**2)
            if previous is not None:
                row['previous_error_ratio'] = previous/difference
                assert previous/difference > 3.7
            previous = difference
            case['rows'].append(row)
        rows.append(case)
        print('discrete_case: '+json.dumps(case, sort_keys=True), flush=True)
    return rows


def edge_checks():
    out = []
    for t, s, data in ((1., 1., [((1., 0.), 1.), ((0., 1.), 0.)]),
                       (1., 1.3, [((0., 0.), 1.), ((0., 0.), 2.)]),
                       (.5, .7, [((1., 0.), -1.)])):
        result = run(t, s, data, 4, grid=32, dt=.004)
        size = max(abs(x) for mat in result['jets'] for x in mat)
        assert size < 1e-12
        out.append(dict(t=t, S=s, maximum_jet_entry=size))
    # The BVP stability constant 1/8 is attained by K=0 and constant scalar source.
    for grid in (16, 32, 64):
        field = [(1., 0., 0., 0.)]*(grid+1)
        ww = r5.gram_response(I, 1., field, 1.)
        assert abs(ww[grid//2][0]+1/8) < 1e-12
    return dict(commuting_stationary_and_zero_inputs=out,
                inverse_dirichlet_constant=1/8)


def main():
    started = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    result = {}
    for name, check in [('exact_coefficients', exact_coefficient_checks),
                        ('compression', compression_checks),
                        ('discrete', discrete_checks), ('edges', edge_checks)]:
        result[name] = check()
        print(name+': '+json.dumps(result[name], sort_keys=True), flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    result['resources'] = dict(seconds=time.monotonic()-started, peak_rss_bytes=rss,
                               priority=priority, OMP_NUM_THREADS='1')
    assert rss < 1_000_000_000 and result['resources']['seconds'] < 1200
    Path('verification_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print('resources: '+json.dumps(result['resources'], sort_keys=True), flush=True)
    print('All checks passed.', flush=True)


if __name__ == '__main__':
    main()
