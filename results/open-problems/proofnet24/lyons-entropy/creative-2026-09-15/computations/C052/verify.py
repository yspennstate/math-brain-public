#!/usr/bin/env python3
"""C052: exact rational certificate plus labeled high-precision diagnostics.

The analytic family theorem is proved in agents/C052.md. No floating-point
sign is used in the rational certificate. The optional mpmath part checks the
complete seven-feature identity and the full nine-coordinate Hessian at one
non-particle-hole, nonzero-triple example.
"""
from fractions import Fraction as F
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


def fs(x):
    return str(x)


def log_interval(x, terms=64):
    """Positive atanh series and a rational geometric tail; x >= 1."""
    assert x >= 1
    z = (x - 1) / (x + 1)
    lo = sum((2 * z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    tail = 2 * z ** (2*terms+1) / ((2*terms+1) * (1-z*z))
    return lo, lo + tail


def exact_certificate():
    delta = F(1, 7)
    u = F(1, 32768)
    zeta = F(9, 8)
    fields = [F(1, 2), F(1), F(3, 2)]
    epsilon = F(9, 4) * u
    b_lower = F(15625, 8192) - F(8, 127)
    d_margin = F(32, 3) - F(33, 4) - F(4, 127)
    assert b_lower > F(3, 2)
    assert d_margin > 0
    assert epsilon < delta / 64
    assert epsilon * 1870 < delta
    assert 16 * F(85, 8)**2 + 6 * F(85, 8) == 1870

    l2lo, l2hi = log_interval(F(2))
    lzlo, lzhi = log_interval(zeta)
    assert l2lo > F(2, 3)
    assert l2hi < F(7, 10)
    assert lzhi < F(1, 8)
    clo, chi = 15*l2lo, 15*l2hi
    assert clo > 10
    assert chi + lzhi < F(85, 8)
    assert clo - lzhi > F(3, 4)
    barlo = clo - lzhi/2
    assert barlo > F(159, 16)

    radicand = 3-4*(1+zeta)*u+6*zeta*u*u-zeta*zeta*u**4
    numerator = 2-3*u+zeta*u**3
    assert radicand > 0
    # These verify |R_23|^2=1-u and det(R)=zeta*u^3 exactly.
    assert numerator**2 + u*u*radicand == 4*(1-u)**3
    assert numerator-2+3*u == zeta*u**3

    weights = []
    for mask in range(8):
        value = F(1)
        for i in range(3):
            if mask >> i & 1:
                value *= fields[i] / u
        for i in range(3):
            for j in range(i):
                if mask >> i & 1 and mask >> j & 1:
                    value *= u
        if mask == 7:
            value *= zeta
        weights.append(value)
    normalizer = sum(weights)
    atoms = [w/normalizer for w in weights]
    assert sum(atoms) == 1
    assert atoms[7]/atoms[0] == F(27, 32)  # Not particle-hole symmetric.
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        assert atoms[0]*atoms[(1 << i) | (1 << j)]/(atoms[1 << i]*atoms[1 << j]) == u
    assert (atoms[0]*atoms[3]*atoms[5]*atoms[6]/
            (atoms[1]*atoms[2]*atoms[4]*atoms[7])) == 1/zeta

    mean = sum((atoms[s]*s.bit_count() for s in range(8)), F(0))
    variance = sum((atoms[s]*(F(s.bit_count())-mean)**2 for s in range(8)), F(0))
    assert variance > F(1, 5)
    pairs = []
    projected_sum = F(0)
    for pair in [3, 5, 6]:
        configurations = [0] + [1 << i for i in range(3) if pair >> i & 1] + [pair]
        marginals = [sum((atoms[s] for s in range(8) if s & pair == h), F(0))
                     for h in configurations]
        conditional_numerators = [sum((atoms[s]*s.bit_count() for s in range(8)
                                      if s & pair == h), F(0)) for h in configurations]
        projection = sum((a*a/b for a, b in zip(conditional_numerators, marginals)), F(0)) - mean*mean
        t_squared = (marginals[1]+marginals[2])**2/(4*marginals[0]*marginals[3])
        assert t_squared < 9
        assert projection > 0
        projected_sum += projection
        pairs.append({"pair_mask": pair, "marginals": list(map(fs, marginals)),
                      "T_squared": fs(t_squared), "count_projection_variance": fs(projection)})
    assert projected_sum > variance
    # C045's B_t is affine in t here. Both endpoint count Rayleigh quotients
    # exceed one, so every shared-coefficient matrix budget fails.
    rayleigh_zero_lower = barlo * projected_sum/(8*variance)
    rayleigh_end_lower = barlo * variance
    assert rayleigh_zero_lower > F(159, 128) > 1
    assert rayleigh_end_lower > F(159, 80) > 1

    e1 = sum(fields)/u
    e2 = sum((fields[i]*fields[j] for i in range(3) for j in range(i)), F(0))/u
    e3 = zeta*fields[0]*fields[1]*fields[2]
    assert 3*e3/e2 <= epsilon
    assert 3/e1 <= 2*u
    assert e2/(3*e1) >= F(1, 6)
    assert 3*e2/e1 <= 6

    result = {
        "status": "PASS: exact rational certificate",
        "parameters": {"u": fs(u), "zeta": fs(zeta), "fields": list(map(fs, fields))},
        "delta": fs(delta), "epsilon": fs(epsilon),
        "frame_middle_lower": fs(b_lower), "frame_edge_margin": fs(d_margin),
        "uniform_smallness_upper": fs(epsilon*1870),
        "phase_radicand": fs(radicand),
        "L_characteristic_invariants": list(map(fs, [e1, e2, e3])),
        "atoms_mask_order": list(map(fs, atoms)),
        "count_mean": fs(mean), "count_variance": fs(variance),
        "pairs": pairs, "sum_count_projection_variances": fs(projected_sum),
        "C045_rayleigh_t_zero_lower": fs(rayleigh_zero_lower),
        "C045_rayleigh_t_max_lower": fs(rayleigh_end_lower),
        "log_intervals": {"log_2": list(map(fs, [l2lo, l2hi])),
                          "log_9_over_8": list(map(fs, [lzlo, lzhi]))},
    }
    return result, (u, zeta, fields, atoms, delta, epsilon)


def diagnostics(data):
    import mpmath as mp
    mp.mp.dps = 90
    u0, zeta0, fields0, atoms0, delta0, epsilon0 = data
    cv = lambda x: mp.mpf(x.numerator)/x.denominator
    u, zeta = cv(u0), cv(zeta0)
    fields, atoms = list(map(cv, fields0)), list(map(cv, atoms0))
    delta, epsilon = cv(delta0), cv(epsilon0)
    ident = mp.eye(3)
    rho = mp.sqrt(1-u)
    numerator = 2-3*u+zeta*u**3
    radicand = 3-4*(1+zeta)*u+6*zeta*u*u-zeta*zeta*u**4
    edge = (numerator + 1j*u*mp.sqrt(radicand))/(2*(1-u))
    normalized = mp.matrix([[1, rho, rho], [rho, 1, edge], [rho, mp.conj(edge), 1]])
    L = mp.matrix([[mp.sqrt(fields[i]*fields[j])/u*normalized[i, j]
                    for j in range(3)] for i in range(3)])
    K = L*(ident+L)**-1
    eigenvalues, unitary = mp.eigh(K)
    c, tau = -mp.log(u), -mp.log(zeta)
    M = c*ident+tau*K
    basis = []
    for i in range(3):
        b = mp.zeros(3); b[i, i] = 1; basis.append(b)
    for i in range(3):
        for j in range(i+1, 3):
            b = mp.zeros(3); b[i, j] = b[j, i] = 1/mp.sqrt(2); basis.append(b)
            b = mp.zeros(3); b[i, j] = 1j/mp.sqrt(2); b[j, i] = -1j/mp.sqrt(2); basis.append(b)
    trace = lambda a: sum(a[i, i] for i in range(a.rows))
    outer = lambda v: mp.matrix([[a*b for b in v] for a in v])
    maxnorm = lambda a: max(abs(x) for x in a)
    atom_fisher = mp.zeros(9)
    atom_second_log = mp.zeros(9)
    atom_derivatives = []
    atom_error = mp.mpf(0)
    for mask in range(8):
        Q = K-mp.diag([0 if mask >> i & 1 else 1 for i in range(3)])
        qi = Q**-1
        atom_error = max(atom_error, abs((-1)**(3-mask.bit_count())*mp.det(Q)-atoms[mask]))
        resolvents = [qi*b for b in basis]
        scores = [mp.re(trace(r)) for r in resolvents]
        atom_derivatives.append([atoms[mask]*s for s in scores])
        atom_fisher += atoms[mask]*outer(scores)
        for i in range(9):
            for j in range(9):
                acceleration = atoms[mask]*(scores[i]*scores[j]-mp.re(trace(resolvents[i]*resolvents[j])))
                atom_second_log[i, j] += acceleration*mp.log(atoms[mask])

    conditional_fisher = mp.zeros(9)
    feature_records = []
    for i in range(3):
        for history in range(1 << i):
            prefix = (1 << i)-1
            probability = sum(atoms[s] for s in range(8) if s & prefix == history)
            w = mp.zeros(3, 1); w[i] = 1
            if i:
                Q = mp.matrix([[K[a, b]-(1 if a == b and not(history >> a & 1) else 0)
                                for b in range(i)] for a in range(i)])
                kfi = mp.matrix([K[a, i] for a in range(i)])
                correction = Q**-1*kfi
                for a in range(i):
                    w[a] = -correction[a]
                q = mp.re(K[i, i]-(kfi.H*correction)[0])
            else:
                q = mp.re(K[i, i])
            weight = probability/(q*(1-q))
            feature = [mp.re((w.H*b*w)[0]) for b in basis]
            conditional_fisher += weight*outer(feature)
            feature_records.append({"stage": i+1, "history_mask": history,
                                    "conditional_probability": mp.nstr(q, 24),
                                    "weight": mp.nstr(weight, 24)})
    assert len(feature_records) == 7

    count_fisher = mp.zeros(9)
    for count in range(4):
        pc = sum(atoms[s] for s in range(8) if s.bit_count() == count)
        derivative = [sum(atom_derivatives[s][i] for s in range(8) if s.bit_count() == count)
                      for i in range(9)]
        count_fisher += outer(derivative)/pc
    transformed_basis = [unitary.H*b*unitary for b in basis]
    diagonal_features = [[mp.re(b[k, k]) for b in transformed_basis] for k in range(3)]
    frame = mp.mpf(3)/2*outer(diagonal_features[1])
    frame += delta/(3*epsilon)*(outer(diagonal_features[0])+outer(diagonal_features[2]))

    def adj(a):
        out = mp.zeros(3)
        for i in range(3):
            for j in range(3):
                rows = [k for k in range(3) if k != j]
                cols = [k for k in range(3) if k != i]
                out[i, j] = (-1)**(i+j)*(a[rows[0], cols[0]]*a[rows[1], cols[1]]
                                            -a[rows[0], cols[1]]*a[rows[1], cols[0]])
        return out

    curvature_value = lambda a: 2*mp.re(trace(M*adj(a)))
    values = [curvature_value(b) for b in basis]
    curvature = mp.matrix([[(curvature_value(basis[i]+basis[j])-values[i]-values[j])/2
                             for j in range(9)] for i in range(9)])
    penalty = mp.zeros(9)
    for i in range(3):
        for j in range(i+1, 3):
            k = 3-i-j
            coefficient = c+tau*eigenvalues[k]
            z = [b[i, j] for b in transformed_basis]
            for a in range(9):
                for b in range(9):
                    penalty[a, b] += 2*coefficient*mp.re(mp.conj(z[a])*z[b])
    negative_hessian = atom_fisher+atom_second_log
    min_eig = lambda a: min(mp.eigsy((a+a.T)/2, eigvals_only=True))
    fisher_error = maxnorm(conditional_fisher-atom_fisher)
    frozen_error = maxnorm(atom_second_log+curvature)
    assert atom_error < mp.mpf('1e-65')
    assert fisher_error < mp.mpf('1e-65')
    assert frozen_error < mp.mpf('1e-65')
    assert min_eig(count_fisher-frame) > -mp.mpf('1e-60')
    assert min_eig(conditional_fisher-count_fisher) > -mp.mpf('1e-60')
    surplus_matrix = negative_hessian-atom_fisher/2-penalty
    surplus_spectrum = list(mp.eigsy((surplus_matrix+surplus_matrix.T)/2, eigvals_only=True))
    surplus = min(surplus_spectrum)
    # Phase-gauge directions have zero Fisher information and zero surplus.
    assert surplus > -mp.mpf('1e-60')
    return {
        "status": "PASS: 90-digit consistency diagnostics; not a proof of signs",
        "kernel_eigenvalues": [mp.nstr(x, 28) for x in eigenvalues],
        "seven_features": feature_records,
        "atom_probability_max_error": mp.nstr(atom_error, 8),
        "complete_fisher_identity_max_error": mp.nstr(fisher_error, 8),
        "frozen_hessian_identity_max_error": mp.nstr(frozen_error, 8),
        "count_frame_minimum_eigenvalue": mp.nstr(min_eig(count_fisher-frame), 12),
        "count_projection_remainder_minimum_eigenvalue": mp.nstr(min_eig(conditional_fisher-count_fisher), 12),
        "negative_hessian_minimum_eigenvalue": mp.nstr(min_eig(negative_hessian), 24),
        "strong_certificate_surplus_minimum_eigenvalue": mp.nstr(surplus, 24),
        "strong_certificate_surplus_spectrum": [mp.nstr(x, 20) for x in surplus_spectrum],
    }


if __name__ == '__main__':
    result, data = exact_certificate()
    result['diagnostics'] = diagnostics(data)
    (OUT/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])
    print(result['diagnostics']['status'])
    print('Complete conditional Fisher discrepancy:', result['diagnostics']['complete_fisher_identity_max_error'])
    print('Full-Hermitian certificate surplus:', result['diagnostics']['strong_certificate_surplus_minimum_eigenvalue'])
