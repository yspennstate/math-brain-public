#!/usr/bin/env python3
"""C058: exact frame/radius certificates and numerical full-Hessian examples.

Only the exact assertions are used as proof certificates. Entropy/Hessian
numbers are 90-digit corroboration of the analytic theorem in agents/C058.md.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
mp.mp.dps = 90
Q = sp.Rational


def signed_atoms(K):
    n = K.rows
    ans = []
    for bits in product((0, 1), repeat=n):
        absent = [1 - z for z in bits]
        N = K - sp.diag(*absent)
        p = sp.simplify((-1) ** sum(absent) * N.det())
        ans.append((bits, N, p))
    return ans


def fisher_features(K):
    n = K.rows
    ans = []
    for j in range(n):
        for history in product((0, 1), repeat=j):
            if j:
                absent = [1 - z for z in history]
                N = K[:j, :j] - sp.diag(*absent)
                pi = (-1) ** sum(absent) * N.det()
                w0 = -N.inv() * K[:j, j]
                q = K[j, j] - (K[j, :j] * N.inv() * K[:j, j])[0]
            else:
                pi, q, w0 = sp.Integer(1), K[0, 0], sp.zeros(0, 1)
            w = sp.zeros(n, 1)
            for k in range(j):
                w[k] = w0[k]
            w[j] = 1
            ans.append((history, w, sp.simplify(pi / (q * (1 - q)))))
    return ans


def smp(z):
    z = sp.expand_complex(z)
    return mp.mpc(str(sp.N(sp.re(z), 95)), str(sp.N(sp.im(z), 95)))


def mpmatrix(M):
    return mp.matrix([[smp(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def hermitian_basis(n):
    basis, kinds = [], []
    for i in range(n):
        E = sp.zeros(n)
        E[i, i] = 1
        basis.append(E)
        kinds.append('block')
    for i in range(n):
        for j in range(i + 1, n):
            for imag in (False, True):
                E = sp.zeros(n)
                E[i, j] = (sp.I if imag else 1) / sp.sqrt(2)
                E[j, i] = sp.conjugate(E[i, j])
                basis.append(E)
                kinds.append('link' if j == n - 1 else 'block')
    return basis, kinds


def trace(M):
    return sum(M[i, i] for i in range(M.rows))


def entropy_hessian(K):
    n = K.rows
    basis, kinds = hermitian_basis(n)
    Eb = list(map(mpmatrix, basis))
    H = mp.matrix(n*n)
    psum = mp.mpf(0)
    entropy = mp.mpf(0)
    for bits, Ns, ps in signed_atoms(K):
        assert ps > 0
        p = mp.re(smp(ps))
        psum += p
        entropy -= p * mp.log(p)
        R = mpmatrix(Ns.inv())
        RE = [R * E for E in Eb]
        score = [mp.re(trace(M)) for M in RE]
        for i in range(n*n):
            for j in range(n*n):
                second = score[i]*score[j] - mp.re(trace(RE[i] * RE[j]))
                H[i, j] -= p * score[i]*score[j] + p * second * mp.log(p)
    assert abs(psum - 1) < mp.mpf('1e-85')
    return entropy, H, kinds


def main():
    A = sp.Matrix([[Q(1, 2), Q(1, 10)], [Q(1, 10), Q(1, 2)]])
    features = fisher_features(A)
    ws = [w for _, w, _ in features]
    weights = [v for _, _, v in features]
    assert ws == [sp.Matrix([1, 0]), sp.Matrix([Q(1, 5), 1]), sp.Matrix([-Q(1, 5), 1])]
    assert weights == [4, Q(625, 312), Q(625, 312)]

    # A certified lower bound alpha for EVERY complementary partition.
    alpha = Q(2, 25)
    partition_results = []
    for mask in range(1 << len(ws)):
        grams = [sp.zeros(2), sp.zeros(2)]
        for j, w in enumerate(ws):
            grams[(mask >> j) & 1] += w * w.conjugate().T
        passes = []
        for G in grams:
            M = G - alpha * sp.eye(2)
            passes.append(bool(M[0, 0] >= 0 and M[1, 1] >= 0 and M.det() >= 0))
        assert any(passes)
        partition_results.append({'mask': mask, 'certified_sides': passes})
    # The partition {e1} versus the two conditional vectors attains alpha.
    Gpair = ws[1]*ws[1].T + ws[2]*ws[2].T
    assert Gpair == sp.diag(Q(2, 25), 2)

    # Exact quartic identity for arbitrary COMPLEX borders, with four free
    # real variables; this is not just a check on the real subspace.
    x, xi, y, yi = sp.symbols('x xi y yi', real=True)
    b = sp.Matrix([x + sp.I*xi, y + sp.I*yi])
    moment_quartic = sum(p * (b.conjugate().T * N.inv() * b)[0]**2
                         for _, N, p in signed_atoms(A))
    frame_quartic = sum(v * ((w.conjugate().T*b)[0]
                            * sp.conjugate((w.conjugate().T*b)[0]))**2
                        for _, w, v in features)
    assert sp.factor(moment_quartic - frame_quartic) == 0
    bdeg = sp.Matrix([Q(1, 20000), -Q(1, 100000)])
    assert (ws[1].T * bdeg)[0] == 0
    assert sp.simplify(moment_quartic.subs({x: bdeg[0], y: bdeg[1], xi: 0, yi: 0})) > 0

    # Reproduce the C028 input gap algebraically on all Hermitian directions.
    # The only transcendental bound is 1/13 <= log(13/12) <= 1/12,
    # obtained by bounding the integrand in integral_0^(1/12) 1/(1+s) ds.
    eigenbasis = [sp.eye(2)/sp.sqrt(2), sp.diag(1, -1)/sp.sqrt(2),
                  sp.Matrix([[0, 1], [1, 0]])/sp.sqrt(2),
                  sp.Matrix([[0, sp.I], [-sp.I, 0]])/sp.sqrt(2)]
    Hminus = sp.zeros(4)
    for _, Ns, p in signed_atoms(A):
        RE = [Ns.inv()*E for E in eigenbasis]
        scores = list(map(trace, RE))
        for i in range(4):
            for j in range(4):
                second = scores[i]*scores[j] - trace(RE[i]*RE[j])
                Hminus[i, j] += p*scores[i]*scores[j] + p*second*sp.log(p)
    ell = sp.Symbol('ell', real=True)
    eigenvalues = [Q(25, 6)-2*ell, Q(50, 13)+2*ell,
                   (Q(25, 6)+Q(50, 13))/25+2*ell, 2*ell]
    expected = sp.diag(*[v.subs(ell, sp.log(Q(13, 12))) for v in eigenvalues])
    assert all(sp.simplify(sp.expand_log(v, force=True)) == 0 for v in Hminus-expected)
    eigenvalue_lowers = [v.subs(ell, Q(1, 13) if v.coeff(ell) > 0 else Q(1, 12))
                        for v in eigenvalues]
    assert min(eigenvalue_lowers) == Q(2, 13)

    # Exact Green-kernel moments giving the finite-chord quartic modulus.
    s, t = sp.symbols('s t', real=True)
    moments = [sp.factor(sp.integrate((1-t)*s**(k+1), (s, 0, t))
                         + sp.integrate(t*(1-s)*s**k, (s, t, 1)))
               for k in range(3)]
    expected_moments = [t*(1-t)/2, t*(1-t)*(1+t)/6,
                        t*(1-t)*(1+t+t*t)/12]
    assert all(sp.expand(a-b) == 0 for a, b in zip(moments, expected_moments))
    green_variance = sp.factor((moments[2]-moments[1]**2/moments[0])/(t*(1-t)))
    assert sp.expand(green_variance-(1-t+t*t)/36) == 0
    assert sp.expand(green_variance-Q(1, 48)-(t-Q(1, 2))**2/36) == 0

    # All following constants are rational upper/lower bounds for the theorem.
    gamma = Q(2, 13)
    nu = Q(625, 312)
    frame_size, n, N = 3, 2, 3
    tau, kappa = Q(2, 5), sp.Integer(5)
    Lframe = sum((w.T*w)[0] for w in ws)
    delta, epsilon = Q(1, 100000), Q(1, 10000)
    # exp(3) > 1+3+3^2/2 > 25/3, so log(25/3)<3.
    assert 1+3+Q(9, 2) > Q(25, 3)
    sqrt2_upper = Q(3, 2)
    assert sqrt2_upper**2 > 2
    t1_upper, t2_exact = sqrt2_upper*kappa, 3*kappa**2
    t3_upper = (5*sqrt2_upper+2)*kappa**3
    Jupper = 3*t3_upper+3*t2_exact*t1_upper+t1_upper**3
    assert Jupper == Q(45375, 8)
    assert Jupper >= (3*6+3*2+1)*kappa**3  # singleton entropy bound
    assert delta <= tau/(8*n)
    assert delta <= gamma/(2*Jupper)
    assert delta <= alpha/(6*kappa*Lframe)
    block_checks = {
        'spectral_radius': tau/(8*n)-delta,
        'entropy_gap_radius': gamma/(2*Jupper)-delta,
        'frame_radius': alpha/(6*kappa*Lframe)-delta,
    }
    assert all(v > 0 for v in block_checks.values())
    coercivity = sp.simplify(nu * alpha**2 / (4*frame_size))
    assert coercivity == Q(1, 936)

    # Lupper=10 >= sqrt(3)*5; polynomial constants increase with L.
    Lupper, M = sp.Integer(10), sp.Integer(100)
    beta, r0 = kappa**2/2, 1/(4*kappa)
    P0 = (M/2 + 4*Lupper*kappa + 10*kappa**2)*beta**2
    P1 = (2*Lupper + 8*kappa)*beta**2
    R0 = (M/3 + 4*Lupper*kappa + 14*kappa**2)*beta**3
    R1 = (2*Lupper + 12*kappa)*beta**3
    R2 = 10*beta**3
    Ac, Bc, Cc = P0 + R0*r0**2, P1 + R1*r0**2, R2
    checks = {
        'epsilon_le_r0': r0 - epsilon,
        'block_remainder_budget': gamma/8 - Ac*epsilon**4,
        'link_remainder_budget': coercivity/4 - Cc*epsilon**2,
        'mixed_remainder_budget': coercivity/4 - (8*Bc**2/gamma)*epsilon**4,
    }
    assert all(v > 0 for v in checks.values())

    exact = {
        'frame_vectors': [list(map(str, w)) for w in ws],
        'frame_weights': list(map(str, weights)),
        'all_partition_certificates': partition_results,
        'alpha_exact': str(alpha), 'nu': str(nu), 'L_frame': str(Lframe),
        'gamma': str(gamma), 'delta': str(delta), 'epsilon': str(epsilon),
        'base_negative_Hessian_eigenvalues_in_ell': list(map(str, eigenvalues)),
        'ell_definition': 'log(13/12)', 'ell_interval': ['1/13', '1/12'],
        'base_negative_Hessian_eigenvalue_lower_bounds': list(map(str, eigenvalue_lowers)),
        'J_upper': str(Jupper),
        'positive_block_radius_slacks': {k: str(sp.factor(v)) for k, v in block_checks.items()},
        'c': str(coercivity), 'A_upper': str(Ac), 'B_upper': str(Bc), 'C': str(Cc),
        'positive_radius_slacks': {k: str(sp.factor(v)) for k, v in checks.items()},
        'quartic_identity_difference': '0',
        'quartic_identity_domain': 'b=(x+i*xi,y+i*yi), with x,xi,y,yi arbitrary real',
        'quartic_polynomial': str(sp.factor(sp.expand(frame_quartic))),
        'green_kernel_moments': list(map(str, moments)),
        'normalized_green_variance': str(green_variance),
        'exact_generic_feature_zero': str((ws[1].T*bdeg)[0]),
        'degenerate_border': list(map(str, bdeg)),
    }
    (HERE/'exact_certificate.json').write_text(json.dumps(exact, indent=2)+'\n')

    numerical = []
    borders = [
        ('first_feature_zero', sp.Matrix([0, Q(1, 20000)])),
        ('conditional_feature_zero', bdeg),
        ('complex_link', sp.Matrix([Q(1, 40000), sp.I*Q(1, 40000)])),
    ]
    for label, bv in borders:
        K = A.row_join(bv).col_join(bv.conjugate().T.row_join(sp.Matrix([[Q(1,2)]])))
        r2 = sp.simplify(2*(bv.conjugate().T*bv)[0])
        assert r2 <= epsilon**2
        ent, hess, kinds = entropy_hessian(K)
        bound = mp.diag([mp.re(smp(gamma/4 if kind == 'block' else coercivity*r2/2)) for kind in kinds])
        slack = -hess - bound
        eig_h = mp.eigsy(-hess, eigvals_only=True)
        eig_slack = mp.eigsy(slack, eigvals_only=True)
        assert eig_slack[0] > 0
        numerical.append({
            'label': label,
            'border': list(map(str, bv)),
            'link_Frobenius_squared': str(r2),
            'entropy': mp.nstr(ent, 45),
            'min_negative_Hessian_eigenvalue': mp.nstr(eig_h[0], 45),
            'min_coercivity_slack_eigenvalue': mp.nstr(eig_slack[0], 45),
            'precision_decimal_digits': mp.mp.dps,
        })

    # A finite chord crosses the independent apex and rotates through a
    # forbidden feature hyperplane; the new cylinder includes the whole chord.
    b0, b1 = bdeg, -bdeg
    K0 = A.row_join(b0).col_join(b0.T.row_join(sp.Matrix([[Q(1,2)]])))
    K1 = A.row_join(b1).col_join(b1.T.row_join(sp.Matrix([[Q(1,2)]])))
    def entropy_only(K):
        return -sum(mp.re(smp(p))*mp.log(mp.re(smp(p))) for _, _, p in signed_atoms(K))
    chord_gap = entropy_only((K0+K1)/2) - (entropy_only(K0)+entropy_only(K1))/2
    dZ2 = sp.simplify(2*((b1-b0).T*(b1-b0))[0])
    chord_bound = sp.simplify(Q(1,4)*coercivity/Q(96)*dZ2**2)
    assert chord_gap >= mp.re(smp(chord_bound))
    output = {
        'status': 'All exact assertions and numerical corroborations passed.',
        'full_Hessian_examples': numerical,
        'opposite_border_chord': {
            'midpoint_gap': mp.nstr(chord_gap, 45),
            'proved_uniform_bound_exact': str(chord_bound),
            'proved_uniform_bound_numeric': mp.nstr(mp.re(smp(chord_bound)), 45),
        },
    }
    (HERE/'results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'exact': exact, 'numerical': output}, indent=2))


if __name__ == '__main__':
    main()
