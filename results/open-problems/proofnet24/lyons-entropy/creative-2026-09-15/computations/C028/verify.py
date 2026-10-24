"""Reproduce C028's quantitative block corridor and exact degree-five cancellation.

Dependencies: Python 3, mpmath, sympy.  Run from any directory.
All-dimensional claims are proved in agents/C028.md; numerical Hessian checks
below are supporting examples, not the proof or a universal sign certificate.
"""

from itertools import product
from math import comb
from pathlib import Path
import json
import mpmath as mp
import sympy as sp

mp.mp.dps = 80


def frob(a):
    return mp.sqrt(sum(abs(z) ** 2 for z in a))


def hinner(a, b):
    return mp.re(sum(mp.conj(x) * y for x, y in zip(a, b)))


def trace(a):
    return sum(a[i, i] for i in range(a.rows))


def block_matrix(a, b, c):
    out = mp.matrix(a.rows + b.rows)
    for i in range(a.rows):
        for j in range(a.rows):
            out[i, j] = a[i, j]
    for i in range(b.rows):
        for j in range(b.rows):
            out[a.rows + i, a.rows + j] = b[i, j]
    for i in range(a.rows):
        for j in range(b.rows):
            out[i, a.rows + j] = c[i, j]
            out[a.rows + j, i] = mp.conj(c[i, j])
    return out


def constants(n, kappa):
    """The finite sums in the theorem, evaluated without coarse simplification."""
    r0 = 1 / (4 * n * kappa)
    L = mp.sqrt(n) * kappa
    M = (n + 1) * kappa**2
    beta = {k: mp.mpf(comb(n, k)) * kappa**k for k in range(2, n + 1)}
    a0 = sum(beta[k] * r0 ** (k - 2) for k in beta)
    a1 = sum(k * beta[k] * r0 ** (k - 2) for k in beta)
    a2 = sum(k * (k - 1) * beta[k] * r0 ** (k - 2) for k in beta)
    b0 = kappa * a1
    b1 = kappa * sum(k*k * beta[k] * r0 ** (k - 2) for k in beta)
    b2 = kappa**2 * sum(k*(k+1) * beta[k] * r0 ** (k - 2) for k in beta)
    d0 = d1 = d2 = mp.mpf(0)
    for d in range(6, 2*n + 1):
        cd = sum(beta[k] * beta.get(d-k, 0) for k in beta)
        tail = cd * r0**(d - 6) / 2
        d0 += (M + 2*L*d*kappa + d*(d+1)*kappa**2) * tail
        d1 += d*(L + d*kappa) * tail
        d2 += d*(d-1) * tail
    R2 = d2 + 2*a0*a1*a1 + a0*a0*a2
    R1 = d1 + L*a0*a0*a1 + 2*a0*b0*a1 + a0*a0*b1
    R0 = d0 + M*a0**3/3 + 2*L*a0*a0*b0 + 2*a0*b0*b0 + a0*a0*b2
    phi0 = (M/2 + 4*L*kappa + 10*kappa**2) * beta[2]**2
    phi1 = (2*L + 8*kappa) * beta[2]**2
    return dict(r0=r0, R0=R0, R1=R1, R2=R2,
                A=phi0 + R0*r0*r0, B=phi1 + R1*r0*r0, C=R2)


def exact_cancellation_check():
    """Three coherent 2-site blocks and three full-rank complex links."""
    rat = sp.Rational
    I = sp.I
    ds = [sp.Matrix([[rat(1,2), rat(1,10)], [rat(1,10), rat(1,2)]]),
          sp.Matrix([[rat(2,5), rat(1,12)+I*rat(1,20)],
                     [rat(1,12)-I*rat(1,20), rat(3,5)]]),
          sp.Matrix([[rat(3,7), -rat(1,9)], [-rat(1,9), rat(4,7)]])]
    cs = {(0,1): sp.Matrix([[1, 2+I], [3-I, 5]])/20,
          (0,2): sp.Matrix([[2+I, -1], [1, 3-I]])/25,
          (1,2): sp.Matrix([[1-I, 2], [-2+I, 1+I]])/30}
    c = sp.zeros(6)
    for (a,b), cab in cs.items():
        c[2*a:2*a+2, 2*b:2*b+2] = cab
        c[2*b:2*b+2, 2*a:2*a+2] = cab.conjugate().T
    block_atoms = []
    all_features = []
    for d in ds:
        atoms = []
        for x in product((0,1), repeat=2):
            ns = d - sp.diag(*[1-v for v in x])
            p = sp.simplify((-1)**(2-sum(x)) * ns.det())
            atoms.append((p, ns.inv()))
        block_atoms.append(atoms)
        feats = [(1/(d[0,0]*(1-d[0,0])), sp.Matrix([1, 0]))]
        for x in (0,1):
            nr = d[0,0] - (1-x)
            q = sp.simplify(d[1,1] - d[1,0]*d[0,1]/nr)
            pi = d[0,0] if x else 1-d[0,0]
            w = sp.Matrix([-d[0,1]/nr, 1])
            feats.append((sp.simplify(pi/(q*(1-q))), w))
        all_features.append(feats)
    e23 = e22 = e33 = sp.S.Zero
    for atoms in product(*block_atoms):
        prob = sp.prod(a[0] for a in atoms)
        r = sp.diag(*[a[1] for a in atoms])
        rc = r*c
        q2 = sp.simplify(-sp.trace(rc**2)/2)
        q3 = sp.simplify(sp.trace(rc**3)/3)
        e23 += prob*q2*q3
        e22 += prob*q2*q2
        e33 += prob*q3*q3
    e23, e22, e33 = map(sp.simplify, (e23, e22, e33))
    quartic = sp.S.Zero
    for (a,b), cab in cs.items():
        for wa, va in all_features[a]:
            for wb, vb in all_features[b]:
                z = (va.conjugate().T * cab * vb)[0]
                quartic += wa*wb*(z*sp.conjugate(z))**2
    quartic = sp.simplify(quartic)
    assert e23 == 0
    assert e22 == quartic
    assert e33 > 0
    assert all(v.det() != 0 for v in cs.values())
    return {"E_q2_q3": str(e23), "Q_identity_difference": str(e22-quartic),
            "E_q3_squared": str(e33), "all_three_links_rank_two": True}


def hermitian_basis(n):
    out, within = [], []
    for i in range(n):
        a = mp.matrix(n)
        a[i,i] = 1
        out.append(a)
        within.append(True)
    for i in range(n):
        for j in range(i+1, n):
            for z in (mp.mpf(1), mp.j):
                a = mp.matrix(n)
                a[i,j] = z/mp.sqrt(2)
                a[j,i] = mp.conj(z)/mp.sqrt(2)
                out.append(a)
                within.append(i//2 == j//2)
    return out, within


def entropy_hessian(k):
    n = k.rows
    basis, within = hermitian_basis(n)
    result = mp.matrix(n*n)
    atom_min = mp.inf
    for x in product((0,1), repeat=n):
        ns = k - mp.diag([1-v for v in x])
        p = mp.re((-1)**(n-sum(x))*mp.det(ns))
        atom_min = min(atom_min, p)
        assert p > 0
        inv = ns**-1
        ra = [inv*a for a in basis]
        tr = [trace(a) for a in ra]
        for i in range(n*n):
            for j in range(i, n*n):
                tr2 = sum(ra[i][u,v]*ra[j][v,u]
                          for u in range(n) for v in range(n))
                val = -p*(tr[i]*tr[j] + (tr[i]*tr[j]-tr2)*mp.log(p))
                result[i,j] += mp.re(val)
    for i in range(n*n):
        for j in range(i):
            result[i,j] = result[j,i]
    return result, within, atom_min


def corridor_example():
    d = mp.matrix([[mp.mpf(1)/2, mp.mpf(1)/10],
                   [mp.mpf(1)/10, mp.mpf(1)/2]])
    zero = mp.matrix(2)
    base = block_matrix(d, d, zero)
    link = mp.matrix([[1,1], [1,2]])/mp.sqrt(14)
    v0 = block_matrix(zero, zero, link)
    assert abs(frob(v0)-1) < mp.mpf('1e-70')
    features = [mp.matrix([1,0]), mp.matrix([mp.mpf(1)/5,1])]
    weights = [mp.mpf(4), mp.mpf(625)/312]
    wf = mp.matrix([[1, mp.mpf(1)/5], [0,1]])
    s = mp.sqrt(min(mp.eigsy(wf.T*wf, eigvals_only=True)))
    fnorm = frob(wf)
    feat = []
    for i in range(2):
        for j in range(2):
            value = abs((features[i].T*link*features[j])[0])
            lip = frob(features[i])*frob(features[j])/mp.sqrt(2)
            feat.append(dict(value=value, lip=lip, weight=weights[i]*weights[j]))
    eta = min(f['value']/f['lip'] for f in feat)/2
    for f in feat:
        f['a'] = (f['value']-eta*f['lip'])/(1+eta)
    n, dmax = 4, 2
    pstar, tau, gamma = mp.mpf(6)/25, mp.mpf(2)/5, mp.mpf(2)/13
    kappa = 2/tau
    t1 = mp.sqrt(dmax)*kappa
    t2 = (dmax+1)*kappa**2
    t3 = (mp.mpf(dmax)**mp.mpf('1.5')+3*mp.sqrt(dmax)+2)*kappa**3
    H3 = mp.log(2/pstar)*t3 + 3*t2*t1+t1**3
    delta_candidates = [tau/(8*dmax), gamma/(2*H3), s/(2*kappa*fnorm),
                        min(f['a']/(6*kappa*f['lip']) for f in feat)]
    delta = min(delta_candidates)
    zeta = (1-delta/tau)**(3*dmax)/(1+delta/tau)**(2*dmax)
    sdelta = s-kappa*delta*fnorm
    c = zeta*zeta*sdelta**4 * min(
        f['weight']*(f['a']-kappa*delta*(2+kappa*delta)*f['lip'])**2
        for f in feat)
    cc = constants(n, kappa)
    eps_candidates = [cc['r0'], (gamma/(8*cc['A']))**mp.mpf('.25'),
                      mp.sqrt(c/(4*cc['C'])),
                      (c*gamma/(32*cc['B']**2))**mp.mpf('.25')]
    eps = min(eps_candidates)
    assert c > 0 and delta > 0 and eps > 0
    e = block_matrix(zero, zero, mp.matrix([[1, mp.j], [2-mp.j, -1]]))
    e -= hinner(e, v0)*v0
    e /= frob(e)
    t = block_matrix(mp.matrix([[1,mp.j],[-mp.j,-1]]),
                     mp.matrix([[2,1],[1,-1]]), zero)
    t /= frob(t)
    checks = []
    for name, ufrac, shape, scale in [
            ('center', 0, 0, mp.mpf('.5')),
            ('mixed_complex', mp.mpf('.7'), mp.mpf('.6'), mp.mpf('.8')),
            ('near_apex', -mp.mpf('.5'), -mp.mpf('.7'), mp.mpf('.1'))]:
        ss = scale*eps/(1+eta)
        cmat = ss*v0 + shape*eta*ss*e
        k = base + ufrac*delta*t + cmat
        hess, within, pmin = entropy_hessian(k)
        rr = frob(cmat)
        penalty = mp.diag([gamma/4 if internal else c*rr*rr/2
                           for internal in within])
        slack_min = min(mp.eigsy(-hess-penalty, eigvals_only=True))
        max_hess = max(mp.eigsy(hess, eigvals_only=True))
        assert slack_min > 0
        checks.append(dict(name=name, link_norm=rr, max_hessian_eigenvalue=max_hess,
                           minimum_bound_slack_eigenvalue=slack_min,
                           smallest_atom=pmin))
    return dict(block_atom_minimum=pstar, block_spectral_margin=tau,
                certified_block_hessian_gap=gamma, selected_feature_sigma_min=s,
                angular_radius=eta, block_radius=delta, coupling_radius=eps,
                quartic_coercivity=c, third_derivative_bound=H3,
                delta_candidates=delta_candidates, coupling_radius_candidates=eps_candidates,
                constants=cc, center_rectangular_link_determinant=mp.det(link),
                hessian_checks=checks, precision_decimal_digits=mp.mp.dps)


def stringify(x):
    if isinstance(x, dict):
        return {k: stringify(v) for k,v in x.items()}
    if isinstance(x, list):
        return [stringify(v) for v in x]
    if isinstance(x, (mp.mpf, mp.mpc)):
        return mp.nstr(x, 40)
    return x


if __name__ == '__main__':
    result = {"exact_three_block_check": exact_cancellation_check(),
              "quantitative_two_block_example": corridor_example()}
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(stringify(result), indent=2) + '\n')
    ex = result['quantitative_two_block_example']
    print('PASS: exact degree-five cancellation, exact Fisher quartic identity, '
          'three 80-digit full-Hessian corridor checks.')
    for key in ('block_radius', 'coupling_radius', 'quartic_coercivity'):
        print(key + ': ' + mp.nstr(ex[key], 15))
