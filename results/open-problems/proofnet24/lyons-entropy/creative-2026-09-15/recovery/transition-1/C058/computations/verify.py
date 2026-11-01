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

    # Quartic Fisher identity and zero generic feature at a permitted border.
    x, y = sp.symbols('x y', real=True)
    b = sp.Matrix([x, y])
    moment_quartic = sum(p * (b.T * N.inv() * b)[0]**2 for _, N, p in signed_atoms(A))
    frame_quartic = sum(v * (w.T*b)[0]**4 for _, w, v in features)
    assert sp.factor(moment_quartic - frame_quartic) == 0
    bdeg = sp.Matrix([Q(1, 20000), -Q(1, 100000)])
    assert (ws[1].T * bdeg)[0] == 0
    assert sp.simplify(moment_quartic.subs({x: bdeg[0], y: bdeg[1]})) > 0

    # All following constants are rational upper/lower bounds for the theorem.
    gamma = Q(2, 13)
    nu = Q(625, 312)
    frame_size, n, N = 3, 2, 3
    tau, kappa = Q(2, 5), sp.Integer(5)
    Lframe = sum((w.T*w)[0] for w in ws)
    delta, epsilon = Q(1, 100000), Q(1, 10000)
    Jupper = Q(45375, 8)  # log(25/3)<3 and sqrt(2)<3/2.
    assert delta <= tau/(8*n)
    assert delta <= gamma/(2*Jupper)
    assert delta <= alpha/(6*kappa*Lframe)
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
        'c': str(coercivity), 'A_upper': str(Ac), 'B_upper': str(Bc), 'C': str(Cc),
        'positive_radius_slacks': {k: str(sp.factor(v)) for k, v in checks.items()},
        'quartic_identity_difference': '0',
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
