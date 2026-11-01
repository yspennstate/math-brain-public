#!/usr/bin/env python3
"""Exact certificates for C068's Doob recovery construction.

Run with Python 3 and SymPy from any working directory. No floating-point
arithmetic or numerical sign decisions are used. The all-dimensional proof
is in agents/C068.md; this verifies its symbolic scalar-reservoir realization,
the rational three-site example, and the scalar generating identities.
"""

from itertools import product
import json
from pathlib import Path

import sympy as sp


CHECKS = []


def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def zero(name, expr):
    check(name, sp.cancel(sp.expand(expr)) == 0)


def logq(value):
    """Formal prime-log linear form for the logarithm of a positive rational."""
    value = sp.Rational(value)
    if value <= 0:
        raise ValueError("logq requires a positive rational")
    terms = []
    for sign, integer in ((1, value.p), (-1, value.q)):
        for prime, multiplicity in sp.factorint(integer).items():
            terms.append(sign * multiplicity * sp.Symbol(f"log_{prime}"))
    return sp.Add(*terms)


def log_data(expr):
    expr = sp.expand(expr)
    symbols = sorted(expr.free_symbols, key=lambda s: int(str(s)[4:]))
    coeffs = {str(s)[4:]: str(expr.coeff(s)) for s in symbols}
    zero("prime-log form has no unrecorded remainder",
         expr - sum(expr.coeff(s) * s for s in symbols))
    return {"expression": str(expr), "prime_log_coefficients": coeffs}


def kl(left, right):
    return sp.expand(sum(x * logq(x / y) for x, y in zip(left, right)))


def atom_probability(kernel, bits):
    absent = [1 - bit for bit in bits]
    return sp.factor((-1) ** sum(absent)
                     * (kernel - sp.diag(*absent)).det())


def bitname(bits):
    return "".join(map(str, bits)) or "empty"


def conditional_means(values, probabilities, depth):
    result = {}
    for history in product((0, 1), repeat=depth):
        atoms = [atom for atom in probabilities if atom[:depth] == history]
        mass = sum(probabilities[atom] for atom in atoms)
        result[history] = sp.expand(sum(probabilities[atom] * values[atom]
                                       for atom in atoms) / mass)
    return result


def main():
    t, rho, w = sp.symbols("t rho w", real=True)
    half, quarter = sp.Rational(1, 2), sp.Rational(1, 4)
    kernel = sp.Matrix([[half, sp.I * t, w],
                        [-sp.I * t, half, w],
                        [w, w, rho]])
    a, b = quarter - t**2, quarter + t**2
    p, d = [1 - rho, rho], [-4 * w**2, 4 * w**2]
    atoms = tuple(product((0, 1), repeat=3))
    probabilities = {}
    for atom in atoms:
        x, y = atom[:2], atom[2]
        actual = atom_probability(kernel, atom)
        if x == (0, 0):
            expected = a * p[y] + d[y] / 4
        elif x == (1, 1):
            expected = a * p[y] - d[y] / 4
        else:
            expected = b * p[y]
        zero(f"symbolic atom {bitname(atom)}", actual - expected)
        zero(f"zero first derivative {bitname(atom)}",
             sp.diff(actual, t).subs(t, 0))
        sign = -1 if x[0] == x[1] else 1
        zero(f"second derivative {bitname(atom)}",
             sp.diff(actual, t, 2) - 2 * sign * p[y])
        probabilities[atom] = actual
    zero("symbolic atom normalization", sum(probabilities.values()) - 1)
    zero("signed reservoir perturbation has zero sum", sum(d))

    for x in product((0, 1), repeat=2):
        q = sum(probabilities[x + (y,)] for y in (0, 1))
        expected_q = a if x[0] == x[1] else b
        zero(f"leaf marginal {bitname(x)}", q - expected_q)
        conditional = probabilities[x + (1,)] / q
        expected_conditional = rho
        if x == (0, 0):
            expected_conditional += w**2 / a
        elif x == (1, 1):
            expected_conditional -= w**2 / a
        zero(f"conditional reservoir law {bitname(x)}",
             conditional - expected_conditional)

        signs = [2 * bit - 1 for bit in x]
        leaf_signed = sp.Matrix([[signs[0] / sp.Integer(2), sp.I * t],
                                 [-sp.I * t, signs[1] / sp.Integer(2)]])
        ones = sp.Matrix([1, 1])
        coefficient = (ones.T * leaf_signed.inv() * ones)[0]
        expected_coefficient = sum(signs) / (2 * leaf_signed.det())
        zero(f"signed Schur coefficient {bitname(x)}",
             coefficient - expected_coefficient)

    for site in (0, 1):
        for occupation in (0, 1):
            marginal = sum(value for atom, value in probabilities.items()
                           if atom[site] == occupation)
            zero(f"constant leaf {site + 1} marginal {occupation}",
                 marginal - half)

    # Rational example; principal minors certify physicality on t^2 < 1/8.
    example_subs = {rho: half, w: quarter}
    example_kernel = kernel.subs(example_subs)
    example_probs = {atom: sp.expand(value.subs(example_subs))
                     for atom, value in probabilities.items()}
    expected_classes = {
        "small": sp.Rational(1, 16) - t**2 / 2,
        "large": sp.Rational(3, 16) - t**2 / 2,
        "middle": sp.Rational(1, 8) + t**2 / 2,
    }
    for atom, value in example_probs.items():
        if atom in ((0, 0, 0), (1, 1, 1)):
            expected = expected_classes["small"]
        elif atom in ((0, 0, 1), (1, 1, 0)):
            expected = expected_classes["large"]
        else:
            expected = expected_classes["middle"]
        zero(f"rational atom {bitname(atom)}", value - expected)

    lam = sp.Symbol("lambda")
    characteristic = example_kernel.charpoly(lam).as_expr()
    expected_characteristic = ((lam - half)
                               * ((lam - half)**2 - t**2 - sp.Rational(1, 8)))
    zero("characteristic polynomial", characteristic - expected_characteristic)
    expected_minors = [half, a, sp.Rational(1, 16) - t**2 / 2]
    minor_data = {}
    for label, matrix in (("K", example_kernel),
                          ("I_minus_K", sp.eye(3) - example_kernel)):
        minors = [sp.factor(matrix[:size, :size].det()) for size in (1, 2, 3)]
        for size, (minor, expected) in enumerate(zip(minors, expected_minors), 1):
            zero(f"{label} leading principal minor {size}", minor - expected)
        minor_data[label] = [str(value) for value in minors]

    r0 = {atom: value.subs(t, 0) for atom, value in example_probs.items()}
    r1 = {atom: sp.diff(value, t).subs(t, 0)
          for atom, value in example_probs.items()}
    r2 = {atom: sp.diff(value, t, 2).subs(t, 0)
          for atom, value in example_probs.items()}
    check("all base probabilities positive", all(value > 0 for value in r0.values()))
    check("all base first scores vanish", all(value == 0 for value in r1.values()))
    zero("second derivatives sum to zero", sum(r2.values()))
    score2 = {atom: r2[atom] / r0[atom] for atom in atoms}
    frozen = {atom: -logq(r0[atom]) for atom in atoms}
    means_f = [conditional_means(frozen, r0, depth) for depth in range(4)]
    means_u = [conditional_means(score2, r0, depth) for depth in range(4)]
    curvatures = []
    for depth in range(1, 4):
        stage = sum(r2[atom]
                    * (means_f[depth][atom[:depth]]
                       - means_f[depth - 1][atom[:depth - 1]]) for atom in atoms)
        covariance = sum(r0[atom]
                         * (means_u[depth][atom[:depth]]
                            - means_u[depth - 1][atom[:depth - 1]])
                         * (means_f[depth][atom[:depth]]
                            - means_f[depth - 1][atom[:depth - 1]]) for atom in atoms)
        zero(f"Doob covariance identity stage {depth}", stage - covariance)
        curvatures.append(sp.expand(stage))
    zero("first reveal curvature", curvatures[0])
    zero("leaf-pair curvature", curvatures[1] - logq(sp.Rational(27, 16)))
    zero("reservoir curvature", curvatures[2] + logq(3))
    total_frozen = sp.expand(sum(r2[atom] * frozen[atom] for atom in atoms))
    zero("Doob telescoping", sum(curvatures) - total_frozen)
    zero("full entropy curvature", total_frozen + 2 * logq(sp.Rational(4, 3)))

    p0 = [half, half]
    d0 = [-quarter, quarter]
    plus, minus = [x + y for x, y in zip(p0, d0)], [x - y for x, y in zip(p0, d0)]
    j = kl(plus, p0) + kl(minus, p0)
    ell = kl(p0, plus) + kl(p0, minus)
    zero("J exact value", j - (sp.Rational(3, 2) * logq(3) - 2 * logq(2)))
    zero("L exact value", ell - (2 * logq(2) - logq(3)))
    zero("early is twice J", curvatures[1] - 2 * j)
    zero("late is minus twice J plus L", curvatures[2] + 2 * (j + ell))
    zero("total is minus twice L", total_frozen + 2 * ell)
    direct_residual = -2 * sum(delta * logq(vp / vm)
                               for delta, vp, vm in zip(d0, plus, minus))
    zero("late direct residual", curvatures[2] - direct_residual)
    zero("late is negative symmetric relative entropy",
         curvatures[2] + kl(plus, minus) + kl(minus, plus))
    for atom in atoms:
        x, y = atom[:2], atom[2]
        actual = score2[atom] - means_u[2][x]
        if x == (0, 0):
            expected = 8 * d0[y] / plus[y]
        elif x == (1, 1):
            expected = -8 * d0[y] / minus[y]
        else:
            expected = 0
        zero(f"second-score residual {bitname(atom)}", actual - expected)
    check("early sign via rational logarithm argument", sp.Rational(27, 16) > 1)
    check("late sign via rational logarithm argument", sp.Integer(3) > 1)
    check("total sign via rational logarithm argument", sp.Rational(4, 3) > 1)
    zero("strict recovery gap exact logarithm",
         ell - j - logq(sp.Rational(256, 243)) / 2)

    # Nonzero-Fisher obstruction, entirely as a rational identity and limit.
    fisher = sp.factor(sum(sp.diff(value, t)**2 / value
                           for value in example_probs.values()))
    fisher_expected = 32 * t**2 * (1 / (1 - 8 * t**2)
                                  + 1 / (3 - 8 * t**2)
                                  + 1 / (1 + 4 * t**2))
    zero("entire Fisher rational function", fisher - fisher_expected)
    fisher_quadratic = sp.limit(fisher / t**2, t, 0)
    zero("Fisher quadratic limit", fisher_quadratic - sp.Rational(224, 3))

    # Check the moving-base early formula as an identity of formal atom logs.
    small, large, middle = (expected_classes[key]
                            for key in ("small", "large", "middle"))
    ls, ll, la, lb, l2 = sp.symbols("L_small L_large L_a L_b L_two")
    m_equal = -(small * ls + large * ll) / a
    m_mixed = -(lb - l2)  # middle = b/2
    early_direct = 4 * (m_mixed - m_equal)
    moving_j = 2 * (small / a * (ls - la + l2)
                    + large / a * (ll - la + l2))
    early_formula = 4 * (la - lb) + 2 * moving_j
    zero("moving-base early curvature formula", early_direct - early_formula)
    early_at_zero = sp.expand(early_direct.subs({
        t: 0, ls: logq(sp.Rational(1, 16)), ll: logq(sp.Rational(3, 16)),
        lb: logq(quarter), l2: logq(2),
    }))
    zero("moving-base early positive limit", early_at_zero - logq(sp.Rational(27, 16)))
    inverse_fisher_limit = sp.limit(t**2 / fisher, t, 0)
    zero("scaled obstruction limit prefactor", inverse_fisher_limit - sp.Rational(3, 224))

    # Exact scalar generating identities determine every power-series term.
    z = sp.Symbol("z", real=True)
    k = sp.Symbol("k", integer=True, positive=True)
    jgen = (1 + z) * sp.log(1 + z) + (1 - z) * sp.log(1 - z)
    lgen = -sp.log(1 - z**2)
    zero("J generator second derivative", sp.diff(jgen, z, 2) - 2 / (1 - z**2))
    zero("J generator value at zero", jgen.subs(z, 0))
    zero("J generator derivative at zero", sp.diff(jgen, z).subs(z, 0))
    zero("L generator derivative", sp.diff(lgen, z) - 2 * z / (1 - z**2))
    zero("L generator value at zero", lgen.subs(z, 0))
    cj, cl = 1 / (k * (2 * k - 1)), 1 / k
    gap_coefficient = 2 * (k - 1) / (k * (2 * k - 1))
    zero("all-index coefficient difference", cl - cj - gap_coefficient)
    zero("quartic gap coefficient", gap_coefficient.subs(k, 2) - sp.Rational(1, 3))
    zero("J quadratic coefficient", sp.limit(jgen / z**2, z, 0) - 1)
    zero("L quadratic coefficient", sp.limit(lgen / z**2, z, 0) - 1)
    zero("sharp quartic coefficient", sp.limit((lgen - jgen) / z**4, z, 0) - sp.Rational(1, 3))
    zero("sharp recovery factor", sp.limit(1 + lgen / jgen, z, 0) - 2)

    certificate = {
        "status": "PASS",
        "arithmetic": "Exact SymPy rational, polynomial, rational-function, and formal prime-log arithmetic",
        "sympy_version": sp.__version__,
        "scope": "DPP Doob recovery cancellation and Fisher-only method obstruction; no new entropy family",
        "symbolic_scalar_reservoir": {
            "kernel": [[str(value) for value in row] for row in kernel.tolist()],
            "probabilities": {bitname(atom): str(sp.expand(value))
                              for atom, value in probabilities.items()},
            "conditional_reservoir_kernels": {
                "00": "rho + w**2/(1/4 - t**2)", "01": "rho",
                "10": "rho", "11": "rho - w**2/(1/4 - t**2)",
            },
        },
        "rational_example": {
            "strict_contraction_domain": "t**2 < 1/8",
            "characteristic_polynomial": str(sp.factor(expected_characteristic)),
            "leading_principal_minors": minor_data,
            "probabilities": {bitname(atom): str(value) for atom, value in example_probs.items()},
            "base_probabilities": {bitname(atom): str(value) for atom, value in r0.items()},
            "base_first_derivatives": {bitname(atom): str(value) for atom, value in r1.items()},
            "base_second_derivatives": {bitname(atom): str(value) for atom, value in r2.items()},
            "J": log_data(j), "L": log_data(ell),
            "frozen_curvature_by_reveal": [log_data(value) for value in curvatures],
            "total_entropy_curvature": log_data(total_frozen),
            "Doob_frozen_surprisal_means": {
                str(depth): {bitname(history): log_data(value)
                             for history, value in means_f[depth].items()}
                for depth in range(4)
            },
            "Doob_second_score_means": {
                str(depth): {bitname(history): str(value)
                             for history, value in means_u[depth].items()}
                for depth in range(4)
            },
            "strict_recovery_gap_L_minus_J": log_data(ell - j),
        },
        "nonzero_fisher_obstruction": {
            "complete_fisher": str(fisher_expected),
            "limit_Fisher_over_t_squared": str(fisher_quadratic),
            "limit_early_curvature": log_data(early_at_zero),
            "limit_t_squared_times_early_over_Fisher": log_data(inverse_fisher_limit * early_at_zero),
            "early_over_Fisher_limit": "+infinity, since numerator tends to log(27/16)>0 and Fisher is positive and tends to zero",
        },
        "scalar_series": {
            "domain": "abs(z)<1",
            "J_generator_second_derivative": "2/(1-z**2), with J(0)=J_prime(0)=0",
            "L_generator_derivative": "2*z/(1-z**2), with L(0)=0",
            "J_coefficient_of_z_to_2k": str(cj),
            "L_coefficient_of_z_to_2k": str(cl),
            "gap_coefficient_of_z_to_2k": str(gap_coefficient),
            "gap_first_nonzero_coefficient": "1/3 at k=2; every coefficient is positive for k>=2",
            "sharp_recovery_factor": "2",
        },
    }
    certificate["checks_passed"] = len(CHECKS)
    certificate["checks"] = CHECKS
    output = Path(__file__).resolve().with_name("exact_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: {len(CHECKS)} exact checks")
    print(f"Certificate: {output}")


if __name__ == "__main__":
    main()
