"""First-order correction checks. Standard library, no writes outside this folder.

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


def readonly_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


q = readonly_module(BASE/'codex_op_1114r4/briefs/T245/verify.py', 'round4_readonly')
old = readonly_module(BASE/'codex_op_1114r3/briefs/T245/verify.py', 'round3_readonly')
I, Z = q.I, q.Z
add, sc, mm, tr, mv, outer, err = q.add, q.sc, q.mm, q.tr, q.mv, q.outer, q.error


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return add(a, sc(b, -1))


def comm(a, b):
    return sub(mm(a, b), mm(b, a))


def simpson(values):
    n = len(values)-1
    assert n % 2 == 0
    out = tuple(0. for _ in values[0])
    for j, value in enumerate(values):
        weight = (1 if j in (0, n) else 4 if j % 2 else 2)/(3*n)
        out = add(out, sc(value, weight))
    return out


def prefix_integrals(values):
    """Fourth-order cumulative quadrature, with an O(h^4) end interval."""
    n = len(values)-1
    hh = 1/n
    out = [tuple(0. for _ in values[0])]*(n+1)
    out[1] = sc(add(add(sc(values[0], 5), sc(values[1], 8)),
                    sc(values[2], -1)), hh/12)
    for j in range(2, n+1):
        if j % 2 == 0:
            out[j] = add(out[j-2], sc(add(add(values[j-2], sc(values[j-1], 4)),
                                           values[j]), hh/3))
        else:
            last = sc(add(add(sc(values[j-2], -1), sc(values[j-1], 8)),
                          sc(values[j], 5)), hh/12)
            out[j] = add(out[j-1], last)
    return out


def dirichlet(source, kappa):
    """Numerov's fourth-order discretization of y''-kappa^2 y=source."""
    n = len(source)-1
    invh2 = n*n
    low = invh2-kappa*kappa/12
    diag = -2*invh2-10*kappa*kappa/12
    c, d = [], []
    for j in range(1, n):
        rhs = (source[j-1]+10*source[j]+source[j+1])/12
        denom = diag-(low*c[-1] if c else 0.)
        c.append(low/denom)
        d.append((rhs-(low*d[-1] if d else 0.))/denom)
    y = [0.]*(n+1)
    for j in range(n-1, 0, -1):
        y[j] = d[j-1]-c[j-1]*y[j+1]
    return y


def gram_response(p, s, jfield, t):
    """Solve the forced boundary problem, in an eigenbasis of log(P^TP/S^2)."""
    n = len(jfield)-1
    h = sc(mm(tr(p), p), 1/(s*s))
    angle = .5*math.atan2(2*h[1], h[0]-h[3])
    c, sn = math.cos(angle), math.sin(angle)
    rot = (c, -sn, sn, c)
    diagonal = mm(mm(tr(rot), h), rot)
    logs = (math.log(diagonal[0]), math.log(diagonal[3]))
    sources = []
    for k, jj in enumerate(jfield):
        z = k/n
        half_inv = (math.exp(-z*logs[0]/2), 0., 0.,
                    math.exp(-z*logs[1]/2))
        jj = mm(mm(tr(rot), jj), rot)
        sources.append(sc(mm(mm(half_inv, jj), half_inv), t))
    components = []
    for entry in range(4):
        i, j = divmod(entry, 2)
        components.append(dirichlet([v[entry] for v in sources],
                                    abs(logs[i]-logs[j])/2))
    result = []
    for k in range(n+1):
        z = k/n
        half = (math.exp(z*logs[0]/2), 0., 0., math.exp(z*logs[1]/2))
        yy = tuple(component[k] for component in components)
        result.append(mm(mm(rot, mm(mm(half, yy), half)), tr(rot)))
    return result


def geometric(p, bias, jfield, t, s, data):
    n = len(jfield)-1
    _, g, _ = q.statistics(p, bias, data)
    v = p[:2]  # P^T e1
    h = sc(mm(tr(p), p), 1/(s*s))
    aa = [q.power(h, j/n) for j in range(n+1)]
    ai = [q.power(h, -j/n) for j in range(n+1)]
    xx = [sc(mm(mm(a, outer(v, g)), b), -1) for a, b in zip(ai, aa)]
    prefix = prefix_integrals(xx)
    rr = [sc(value, t) for value in prefix]
    source = []
    for a, inverse in zip(aa, ai):
        source.append(sub(sc(outer(v, v), dot(g, mv(a, g))),
                          sc(mm(mm(a, outer(g, g)), a), dot(v, mv(inverse, v)))))
    ww = gram_response(p, s, jfield, t)
    f_terms, m_terms, b_terms = [], [], []
    for a, inverse, w in zip(aa, ai, ww):
        iv = mv(inverse, v)
        scalar = dot(v, iv)
        variation = dot(iv, mv(w, iv))
        f_terms.append(sub(mm(inverse, mm(outer(v, g), w)),
                           mm(mm(mm(inverse, w), inverse), mm(outer(v, g), a))))
        m_terms.append(sub(sc(w, scalar), sc(a, variation)))
        b_terms.append((-variation,))
    df = sc(mm(p, simpson(f_terms)), -t)
    dm = sc(simpson(m_terms), t)
    db = t*simpson(b_terms)[0]
    ordered = [mm(x, integral) for x, integral in zip(xx, prefix)]
    time_hessian = sc(mm(p, simpson(ordered)), t*t)
    jdot = [sub(add(mm(tr(r), j), mm(j, r)), sc(src, t))
            for r, j, src in zip(rr, jfield, source)]
    return dict(F=df, M=dm, B=db, T=time_hessian, Jdot=jdot, W=ww,
                A=aa, X=xx)


def dh(direction, data):
    dp, db = direction[:4], direction[4]
    return db+sum(dot(dp[:2], x) for x, _ in data)/len(data)


def directional(function, p, bias, direction):
    eps = 2e-5/max(1., max(abs(x) for x in direction))
    yp = add((*p, bias), sc(direction, eps))
    ym = sub((*p, bias), sc(direction, eps))
    return sc(sub(function(yp[:4], yp[4]), function(ym[:4], ym[4])), 1/(2*eps))


def correction_rhs(y, t, s, data, grid):
    p, bias, sensitivity, beta = y[:4], y[4], y[5:9], y[9]
    jf = [y[10+4*k:14+4*k] for k in range(grid+1)]
    h, g, _ = q.statistics(p, bias, data)
    f = q.closed(p, t, s, g)[0]
    geo = geometric(p, bias, jf, t, s, data)
    fun = lambda matrix, bb: q.endpoint_rhs((*matrix, bb), t, s, data)[:4]
    df_sens = directional(fun, p, bias, (*sensitivity, beta))
    df_flow = directional(fun, p, bias, (*f, -h))
    ps = add(add(df_sens, geo['F']), sub(geo['T'], sc(df_flow, .5)))
    bs = -dh((*sensitivity, beta), data)+.5*dh((*f, -h), data)
    return (*f, -h, *ps, bs, *(x for mat in geo['Jdot'] for x in mat))


def correction_run(t, s, data, final=.4, grid=32, dt=.004):
    steps = round(final/dt)
    dt = final/steps
    y = (*sc(I, s), 0., *Z, 0., *(0. for _ in range(4*(grid+1))))
    rhs = lambda state: correction_rhs(state, t, s, data, grid)
    for _ in range(steps):
        y = q.rk4(y, dt, rhs)
    p, bias, sensitivity, beta = y[:4], y[4], y[5:9], y[9]
    jf = [y[10+4*k:14+4*k] for k in range(grid+1)]
    geo = geometric(p, bias, jf, t, s, data)
    _, mat, bb = q.closed(p, t, s, (0., 0.))
    kernel = lambda matrix, bias: (*q.closed(matrix, t, s, (0., 0.))[1],
                                  q.closed(matrix, t, s, (0., 0.))[2])
    ds = directional(kernel, p, bias, (*sensitivity, beta))
    return dict(P=p, b=bias, M=mat, B=bb, p=sensitivity, beta=beta,
                m=add(ds[:4], geo['M']), bcor=ds[4]+geo['B'],
                memory_M=geo['M'], memory_B=geo['B'], J=jf, W=geo['W'])


def exact_prior_recheck():
    """Fresh rational polynomial integrals, independent of the prior checker."""
    def integ(coeffs):
        return sum(x/F(k+1) for k, x in enumerate(coeffs))

    rows = []
    for eta in (F(1, 5), F(3, 7), F(7, 8)):
        a = eta/2
        # Expand norm(V^T e)^2 times the entries of U^T U by hand.
        m00 = integ([1+a*a, -2*a*a, a*a])
        m01 = integ([0, a+a**3, -2*a**3, a**3])
        m11 = integ([1+a*a, -2*a*a, 2*a*a+a**4, -2*a**4, a**4])
        mat = (m00, m01, m01, m11)
        assert mat == (1+eta**2/12, eta/4+eta**3/96,
                       eta/4+eta**3/96, 1+eta**2/6+eta**4/480)
        pp = (F(1), a, F(0), F(1))
        assert comm(mat, mm(tr(pp), pp))[1] == eta**3/48+eta**5/640
        ends = []
        for z in (F(0), F(2, 5), F(1)):
            u = (F(1), a*z, F(0), F(1))
            back = (F(1), a*(1-z))
            c2 = sub((0, a, 0, 0), sc(outer(back, mv(u, (eta/4, (eta-1)/2))), eta))
            assert c2[3] == eta**2*(1-eta)*(1-z)/4
            if z in (0, 1):
                ends.append(c2)
        assert comm(ends[0], ends[1])[2] == eta**6/32
        # Exact defect recurrence at an arbitrary nilpotent constant profile.
        for z in (F(0), F(1, 3), F(1)):
            c = (F(0), a, F(0), F(0))
            g = sc(outer((F(1), a*(1-z)), mv((1, a*z, 0, 1),
                                                           (eta/4, (eta-1)/2))), -1)
            gz = comm(g, tr(c))
            cp = add(c, sc(g, eta))
            new_def = sub(sc(add(gz, tr(gz)), eta), comm(cp, tr(cp)))
            expected = sub(sc(comm(c, tr(c)), -1), sc(comm(g, tr(g)), eta**2))
            assert new_def == expected
        rows.append(dict(eta=str(eta), M1=[str(x) for x in mat],
                         kernel_commutator=str(eta**3/48+eta**5/640)))
    # 1/24 and 1/48 from a separate polynomial boundary-value calculation.
    # w_11=z(1-z)/8, w_22=-w_11 at unit initial memory slope.
    integrated_w11 = integ([F(0), F(1, 8), F(-1, 8)])
    assert integrated_w11 == F(1, 48)
    assert -2*integrated_w11 == -F(1, 24)
    return dict(rational_checks=rows, initial_memory_B_slope=str(-integrated_w11),
                initial_memory_M22_slope=str(-2*integrated_w11))


def bvp_checks():
    """Known smooth solutions, repeated and separated eigenvalues."""
    rows = []
    for p in (I, (1.2, .0, .0, .7), (1.1, .4, -.2, 1.)):
        t, s = .7, 1.2
        h = sc(mm(tr(p), p), 1/(s*s))
        kval = Z
        for value, proj in q.eig(h):
            kval = add(kval, sc(proj, math.log(value)))
        a = (1., .3, .3, -.6)
        for grid in (16, 32, 64):
            jf, truth = [], []
            for j in range(grid+1):
                z = j/grid
                # W(z)=sin(pi z) a; source from the exact differential equation.
                w = sc(a, math.sin(math.pi*z))
                wz = sc(a, math.pi*math.cos(math.pi*z))
                wzz = sc(w, -math.pi**2)
                jj = sc(add(sub(sub(wzz, mm(wz, kval)), mm(kval, wz)),
                            mm(mm(kval, w), kval)), 1/t)
                jf.append(jj)
                truth.append(w)
            actual = gram_response(p, s, jf, t)
            difference = max(err(x, y) for x, y in zip(actual, truth))
            rows.append(dict(P=p, grid=grid, error=difference))
        assert rows[-1]['error'] < rows[-3]['error']/150
    return rows


def insertion_check():
    """Hessian insertion formula against actual profile perturbations."""
    grid, t, s, bias = 128, .8, 1.2, -.1
    cs = [(.10+.03*j/grid, -.08+.04*j/grid,
           .03*math.sin(j/grid), -.05) for j in range(grid+1)]
    state = old.profile_state(cs, t, s, bias, q.DATA)
    gs = [sc(outer(v[:2], mv(u, state['g'])), -s)
          for u, v in zip(state['us'], state['vs'])]
    xx = [mm(mm(old.inv(u), g), u) for u, g in zip(state['us'], gs)]
    prefix = prefix_integrals(xx)
    predicted = sc(mm(sc(state['Q'], s),
                      simpson([mm(x, integral) for x, integral in zip(xx, prefix)])), t*t)
    reversed_order = sc(mm(sc(state['Q'], s),
                      simpson([mm(integral, x) for x, integral in zip(xx, prefix)])), t*t)
    rows = []
    for eps in (.02, .01, .005):
        cp = [add(c, sc(g, eps)) for c, g in zip(cs, gs)]
        cm = [sub(c, sc(g, eps)) for c, g in zip(cs, gs)]
        plus = old.profile_state(cp, t, s, bias, q.DATA)['Q']
        minus = old.profile_state(cm, t, s, bias, q.DATA)['Q']
        measured = sc(sub(add(plus, minus), sc(state['Q'], 2)), s/(2*eps*eps))
        rows.append(dict(eps=eps, error=err(measured, predicted)))
    assert rows[-1]['error'] < 2e-7
    reversed_error = err(reversed_order, predicted)
    assert reversed_error > 20*rows[-1]['error']
    return dict(finite_differences=rows, reversed_order_error=reversed_error)


def trajectory_checks():
    rows, refinements = [], []
    for t, s, data in ((.5, .7, q.DATA), (1., 1., q.TWO), (2., 1.3, q.DATA)):
        coarse = correction_run(t, s, data, grid=32, dt=.004)
        ref = correction_run(t, s, data, grid=64, dt=.002)
        refinement = max(err(coarse['p'], ref['p']), abs(coarse['beta']-ref['beta']),
                         err(coarse['m'], ref['m']), abs(coarse['bcor']-ref['bcor']))
        refinements.append(dict(t=t, S=s, correction_refinement_error=refinement))
        assert refinement < 2e-6
        previous_error = None
        for eta in (.04, .02, .01, .005):
            steps = round(.4/eta)
            states, _ = old.profile_run(t, s, eta, data, steps, 128)
            raw = states[-1]
            actual = dict(P=sc(raw['Q'], s), b=raw['b'], M=raw['M'], B=raw['B'])
            predicted = dict(P=add(ref['P'], sc(ref['p'], eta)),
                             b=ref['b']+eta*ref['beta'],
                             M=add(ref['M'], sc(ref['m'], eta)),
                             B=ref['B']+eta*ref['bcor'])
            balanced_at_actual = q.closed(actual['P'], t, s, (0., 0.))
            recovered_m = sc(sub(actual['M'], balanced_at_actual[1]), 1/eta)
            recovered_b = (actual['B']-balanced_at_actual[2])/eta
            correction_error = q.state_error(actual, predicted)
            flow_error = q.state_error(actual, ref)
            row = dict(t=t, S=s, eta=eta, flow_error=flow_error,
                       corrected_error=correction_error,
                       corrected_error_over_eta2=correction_error/eta**2,
                       memory_M_error=err(recovered_m, ref['memory_M']),
                       memory_B_error=abs(recovered_b-ref['memory_B']))
            if eta == .005:
                row['limiting_memory_M'] = ref['memory_M']
                row['limiting_memory_B'] = ref['memory_B']
            rows.append(row)
            if previous_error is not None:
                assert correction_error < previous_error/2.8
            previous_error = correction_error
        assert rows[-1]['corrected_error'] < rows[-1]['flow_error']/30
        # Independent depth-grid refinement of the raw nonlinear GD recursion.
        finer, _ = old.profile_run(t, s, .005, data, 80, 256)
        grid_error = max(err(finer[-1]['M'], raw['M']),
                         err(finer[-1]['Q'], raw['Q']), abs(finer[-1]['B']-raw['B']))
        refinements[-1]['raw_profile_refinement_error'] = grid_error
        assert grid_error < 1e-7
    return dict(rows=rows, refinements=refinements)


def memory_source_check():
    """Compare J equation with direct accumulation in physical layer coordinates."""
    grid, t, s, data, dt, steps = 64, 1., 1., q.TWO, .002, 200
    cs, b, physical_e = [Z]*(grid+1), 0., [Z]*(grid+1)
    # Integrate the unclosed original profile flow and E_dot=-t[G,G^T].
    def rhs(y):
        cc = [y[4*j:4*j+4] for j in range(grid+1)]
        bias = y[4*(grid+1)]
        st = old.profile_state(cc, t, s, bias, data)
        gg = [sc(outer(v[:2], mv(u, st['g'])), -s)
              for u, v in zip(st['us'], st['vs'])]
        ee = [sc(comm(g, tr(g)), -t) for g in gg]
        naive_jdot = [mm(mm(tr(u), e), u) for u, e in zip(st['us'], ee)]
        return (*(x for g in gg for x in g), -st['h'],
                *(x for e in ee for x in e), *(x for j in naive_jdot for x in j))
    y = (*(x for c in cs for x in c), b, *(x for e in physical_e for x in e),
         *(0. for _ in range(4*(grid+1))))
    for _ in range(steps):
        y = q.rk4(y, dt, rhs)
    cs = [y[4*j:4*j+4] for j in range(grid+1)]
    b = y[4*(grid+1)]
    offset = 4*(grid+1)+1
    ee = [y[offset+4*j:offset+4*j+4] for j in range(grid+1)]
    naive_offset = offset+4*(grid+1)
    naive_j = [y[naive_offset+4*j:naive_offset+4*j+4] for j in range(grid+1)]
    st = old.profile_state(cs, t, s, b, data)
    actual_j = [mm(mm(tr(u), e), u) for u, e in zip(st['us'], ee)]
    closed = correction_run(t, s, data, grid=grid, dt=dt)
    difference = max(err(a, b) for a, b in zip(actual_j, closed['J']))
    assert difference < 1e-7
    missing_transport_error = max(err(a, b) for a, b in zip(actual_j, naive_j))
    assert missing_transport_error > 1000*difference
    # Direct scaled discrete defect via exact recurrence, not depth derivatives.
    eta = .005
    states, profiles = old.profile_run(t, s, eta, data, 80, grid)
    accumulated = [Z]*(grid+1)
    for k in range(80):
        current = old.profile_state(profiles[k], t, s, states[k]['b'], data)
        gg = [sc(outer(v[:2], mv(u, current['g'])), -s)
              for u, v in zip(current['us'], current['vs'])]
        accumulated = [sub(e, sc(comm(g, tr(g)), t*eta))
                       for e, g in zip(accumulated, gg)]
    actual = old.profile_state(profiles[-1], t, s, states[-1]['b'], data)
    discrete_j = [mm(mm(tr(u), e), u) for u, e in zip(actual['us'], accumulated)]
    derror = max(err(a, b) for a, b in zip(discrete_j, closed['J']))
    assert derror < .005
    return dict(closed_J_vs_direct_profile_error=difference,
                scaled_discrete_defect_error_at_eta005=derror,
                error_without_coordinate_transport=missing_transport_error)


def edge_checks():
    rows = []
    cases = [(1., 1., [((1., 0.), 1.), ((0., 1.), 0.)]),
             (1., 1.3, [((0., 0.), 1.), ((0., 0.), 2.)]),
             (.5, .7, [((1., 0.), -1.)]),
             (1., 1.3, [((1., 0.), .2)])]
    for t, s, data in cases:
        ref = correction_run(t, s, data, grid=32, dt=.004)
        memory_size = max(max(abs(x) for mat in ref['J'] for x in mat),
                          max(abs(x) for x in ref['memory_M']), abs(ref['memory_B']))
        assert memory_size < 1e-12  # stationary, zero input, or commuting scalar orbit
        eta = .01
        states, _ = old.profile_run(t, s, eta, data, 40, 64)
        actual = states[-1]
        predicted = dict(P=add(ref['P'], sc(ref['p'], eta)),
                         b=ref['b']+eta*ref['beta'],
                         M=add(ref['M'], sc(ref['m'], eta)),
                         B=ref['B']+eta*ref['bcor'])
        state = dict(P=sc(actual['Q'], s), b=actual['b'], M=actual['M'], B=actual['B'])
        difference = q.state_error(state, predicted)
        if all(x == (0., 0.) for x, _ in data):
            exact_beta = .4*1.5*math.exp(-.4)/2
            assert abs(ref['beta']-exact_beta) < 1e-11
        rows.append(dict(t=t, S=s, memory_size=memory_size, corrected_error=difference))
        assert difference < .0001
    return rows


def main():
    started = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    # All arrays have O(256) tiny matrices; no large allocations occur.
    result = {}
    checks = [('prior_independent', exact_prior_recheck), ('forced_gram', bvp_checks),
              ('ordered_hessian', insertion_check), ('trajectories', trajectory_checks),
              ('memory_source', memory_source_check), ('edge_cases', edge_checks)]
    for name, check in checks:
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
