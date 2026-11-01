#!/usr/bin/env python3
"""Exact certificates for the nonreplacement reversible DPP flow in C027."""

from itertools import product
import json
from pathlib import Path

import sympy as sp


def require(statement, label):
    if not statement:
        raise AssertionError(label)


def rational_matrix(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def main():
    eta = sp.symbols("eta", real=True)
    c, d, a, b = map(sp.Rational, ["1/20", "1/16", "1/10", "1/40"])
    alpha, beta, gamma, delta = 4*c*c, 4*d*d, 4*a*a, 4*b*b
    kernel = sp.Matrix([
        [sp.Rational(1, 2), c, eta*a, 0],
        [c, sp.Rational(1, 2), 0, sp.I*eta*b],
        [eta*a, 0, sp.Rational(1, 2), d],
        [0, -sp.I*eta*b, d, sp.Rational(1, 2)],
    ])
    direction = kernel.diff(eta)
    require(direction.rank() == 4, "direction rank")
    require(direction[:2, :].rank() == 2, "first block row rank")
    require(direction[2:, :].rank() == 2, "second block row rank")

    spins = list(product([-1, 1], repeat=4))
    mu_values, h_values, g_values, atoms = [], [], [], []
    for y in spins:
        z, w, s = y[0]*y[1], y[2]*y[3], y[0]*y[2]
        denominator = (1-alpha*z)*(1-beta*w)
        mu = denominator/16
        h = -s*(gamma+delta*z*w)/denominator
        g = gamma*delta*z*w/denominator
        atom = sp.expand(mu*(1+eta**2*h+eta**4*g))
        absent = [int(x == 1) for x in y]
        determinant_atom = (-1)**sum(absent) * (kernel-sp.diag(*absent)).det()
        require(sp.expand(atom-determinant_atom) == 0, "signed determinant atom")
        mu_values.append(mu)
        h_values.append(h)
        g_values.append(g)
        atoms.append(atom)

    mu, h, g, p = map(sp.Matrix, [mu_values, h_values, g_values, atoms])
    W = sp.diag(*mu_values)
    one = sp.ones(16, 1)
    require((one.T*mu)[0] == 1, "normalization")
    require((mu.T*h)[0] == 0 and (mu.T*g)[0] == 0, "centered modes")
    require((h.T*W*g)[0] == 0, "mode orthogonality")
    variance = (h.T*W*h)[0]
    expected_variance = (gamma**2+delta**2+2*alpha*beta*gamma*delta)/(
        (1-alpha**2)*(1-beta**2)
    )
    require(variance == expected_variance, "variance formula")
    maximum = max(abs(x) for x in h)
    require(maximum == (gamma+delta)/((1-alpha)*(1-beta)), "mode maximum")
    theta = maximum**2/variance
    require(theta < sp.Rational(6, 5), "curvature criterion")

    # The orthogonal mode projection is not assumed to be a Markov map.
    R = one*mu.T
    P = h*h.T*W/variance
    L = 4*(R-sp.eye(16))+2*P
    B = L*L+L
    M = -B
    require(L*one == sp.zeros(16, 1), "L row sums")
    require(M*one == sp.zeros(16, 1), "M row sums")
    require(W*L == L.T*W and W*M == M.T*W, "reversibility")
    require(L*h == -2*h and L*g == -4*g, "exact DPP eigenmodes")
    require(B == 12*(sp.eye(16)-R)-10*P, "curvature generator formula")
    require(all(L[i,j] > 0 for i in range(16) for j in range(16) if i != j),
            "positive transition rates")
    require(all(M[i,j] > 0 for i in range(16) for j in range(16) if i != j),
            "positive curvature-generator rates")
    f = one+eta**2*h+eta**4*g
    require(sp.simplify(L*f+eta*f.diff(eta)) == sp.zeros(16, 1),
            "full affine-line forward equation")
    require(sp.simplify(W*B*f-eta**2*p.diff(eta, 2)) == sp.zeros(16, 1),
            "exact acceleration identity")

    # Fixed block marginals make cross entropy against mu constant.
    for block in [(0, 1), (2, 3)]:
        for value in product([-1, 1], repeat=2):
            indices = [i for i, y in enumerate(spins)
                       if tuple(y[j] for j in block) == value]
            require(sp.expand(sum(p[i]-mu[i] for i in indices)) == 0,
                    "fixed coherent-block marginal")

    # A real cycle phase supplies the exact obstruction to reversible embedding.
    real_kernel = kernel.subs({sp.I*eta*b: eta*b, -sp.I*eta*b: eta*b})
    # Explicit construction avoids expression-order ambiguity in substitutions.
    real_kernel[1, 3] = real_kernel[3, 1] = eta*b
    zeta = -32*c*d*a*b
    h_real = []
    for i, y in enumerate(spins):
        z, w = y[0]*y[1], y[2]*y[3]
        denominator = (1-alpha*z)*(1-beta*w)
        altered_h = h[i]+zeta*z*w/denominator
        h_real.append(altered_h)
        absent = [int(x == 1) for x in y]
        actual = (-1)**sum(absent)*(real_kernel-sp.diag(*absent)).det()
        predicted = mu[i]*(1+eta**2*altered_h+eta**4*g[i])
        require(sp.expand(actual-predicted) == 0, "real-phase atom formula")
    obstruction = (sp.Matrix(h_real).T*W*g)[0]
    require(obstruction == zeta*gamma*delta/((1-alpha**2)*(1-beta**2)),
            "phase obstruction formula")
    require(obstruction != 0, "nonreversible real-phase obstruction")

    samples = []
    for parameter in map(sp.Rational, ["1/4", "1/2", "1"]):
        density = f.subs(eta, parameter)
        probabilities = p.subs(eta, parameter)
        Lf = L*density
        Mf = M*density
        fisher = sum(mu[i]*Lf[i]**2/density[i] for i in range(16))
        dissipation = -sum(mu[i]*Mf[i]*sp.log(density[i]) for i in range(16))
        curvature = -(fisher+dissipation)/parameter**2
        p1, p2 = p.diff(eta).subs(eta, parameter), p.diff(eta, 2).subs(eta, parameter)
        direct = -sum(p1[i]**2/probabilities[i]+p2[i]*sp.log(probabilities[i])
                      for i in range(16))
        error = abs(float(sp.N(curvature-direct, 60)))
        require(error < 1e-50, "direct entropy Hessian identity")
        entropy = -sum(x*sp.log(x) for x in probabilities)
        samples.append({
            "eta": str(parameter), "entropy": str(sp.N(entropy, 25)),
            "H_second": str(sp.N(curvature, 25)),
            "fisher_term": str(sp.N(fisher, 25)),
            "curvature_generator_dissipation": str(sp.N(dissipation, 25)),
            "identity_error": error,
        })

    output = {
        "status": "PASS",
        "parameters": {"c": str(c), "d": str(d), "a": str(a), "b": str(b)},
        "direction_rank": 4,
        "coherent_block_row_ranks": [2, 2],
        "all_eta_Gershgorin_interval": ["27/80", "53/80"],
        "variance": str(variance), "maximum_absolute_mode": str(maximum),
        "theta": str(theta), "theta_decimal": float(theta),
        "gap_to_six_fifths": str(sp.Rational(6, 5)-theta),
        "real_phase_mode_inner_product": str(obstruction),
        "minimum_L_off_diagonal": str(min(L[i,j] for i in range(16)
                                            for j in range(16) if i != j)),
        "minimum_M_off_diagonal": str(min(M[i,j] for i in range(16)
                                            for j in range(16) if i != j)),
        "samples": samples,
    }
    folder = Path(__file__).resolve().parent
    (folder/"results.json").write_text(json.dumps(output, indent=2)+"\n")
    (folder/"exact_generator.json").write_text(json.dumps({
        "spin_order": spins, "mu": list(map(str, mu)),
        "h": list(map(str, h)), "g": list(map(str, g)),
        "L": rational_matrix(L), "M": rational_matrix(M),
    }, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
