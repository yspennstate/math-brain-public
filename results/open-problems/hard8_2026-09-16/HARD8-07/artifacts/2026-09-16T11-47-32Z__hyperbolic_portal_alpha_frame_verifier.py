from fractions import Fraction


def cf_value(ds):
    x = Fraction(ds[-1], 1)
    for a in reversed(ds[:-1]):
        x = Fraction(a, 1) + Fraction(1, x)
    return x


def convergents(ds):
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    out = []
    for a in ds:
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        out.append((p, q))
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q
    return out


def norm_frac(x):
    n = x.numerator
    d = x.denominator
    r = n % d
    return Fraction(min(r, d - r), d)


def absf(x):
    return x if x >= 0 else -x


# Deterministic finite continued fractions.  We use only indices for which
# the complete quotient required by the identity is defined.
alpha_families = [
    [0, 1, 2, 1, 3, 2, 1, 4, 2, 3, 1, 2],
    [1, 2, 2, 3, 1, 1, 4, 2, 2, 1, 3, 2],
    [0, 3, 1, 2, 4, 1, 3, 2, 1, 2, 3, 1],
    [2, 1, 3, 1, 2, 2, 1, 3, 4, 1, 2, 2],
    [0, 2, 4, 1, 1, 3, 2, 4, 1, 2, 2, 3],
    [1, 3, 2, 1, 4, 2, 3, 1, 1, 2, 4, 1],
]

beta_families = [
    [0, 2, 1, 3, 2, 2, 1, 4, 2, 1, 3, 2],
    [1, 1, 3, 2, 4, 1, 2, 3, 1, 2, 2, 4],
    [0, 4, 2, 1, 3, 1, 2, 2, 4, 1, 3, 1],
    [2, 2, 1, 4, 1, 3, 2, 1, 2, 4, 1, 3],
    [0, 3, 3, 1, 2, 4, 1, 2, 3, 1, 2, 2],
    [1, 2, 4, 2, 1, 3, 1, 4, 2, 1, 3, 2],
]

portal_checks = 0
weight_checks = 0
pointwise_checks = 0
adjacent_phase_checks = 0
future_drift_checks = 0
matched_constant_checks = 0

for bds in beta_families:
    beta = cf_value(bds)
    bc = convergents(bds)
    Abeta = max(bds[1:])

    for n in range(0, len(bds) - 2):
        C, D = bc[n]
        Cp, Dp = bc[n + 1]
        eta = cf_value(bds[n + 2 :])
        Delta = Dp * eta + D
        kappa = Fraction(Dp, 1) / Delta

        for z in range(-7, 8):
            for v in range(-7, 8):
                Q = z * D + v * Dp
                if Q == 0:
                    continue

                r = z * C + v * Cp
                delta = Fraction(v, 1) - z * eta
                signed_error = Fraction(Q, 1) * beta - r
                rhs = ((-1) ** (n + 1)) * delta / Delta
                assert signed_error == rhs

                a = absf(Fraction(z, 1) + kappa * delta)
                assert Fraction(abs(Q), 1) == Delta * a
                portal_checks += 1

                if 2 * absf(delta) < Delta:
                    q = abs(Q)
                    W = a * absf(delta)
                    assert Fraction(q, 1) * norm_frac(Fraction(q, 1) * beta) == W
                    weight_checks += 1

                    # Pointwise alpha-convergent bound and exact adjacent phase law.
                    for ads in alpha_families:
                        alpha = cf_value(ads)
                        ac = convergents(ads)

                        for j in range(0, len(ads) - 1):
                            A, B = ac[j]
                            Ap, Bp = ac[j + 1]

                            # For the penultimate convergent of a finite rational
                            # continued fraction equality can occur; infinite CFs
                            # have the usual strict bound.
                            err = absf(alpha - Fraction(A, B))
                            assert err <= Fraction(1, B * Bp)

                            rho = norm_frac(Fraction(q * A, B))
                            target = (
                                Fraction(q, 1)
                                * norm_frac(Fraction(q, 1) * alpha)
                                * norm_frac(Fraction(q, 1) * beta)
                            )
                            rhs_bound = W * rho + W * Fraction(q, B * Bp)
                            assert target <= rhs_bound
                            pointwise_checks += 1

                            det = Ap * B - A * Bp
                            assert abs(det) == 1
                            phase_diff = Fraction(q * Ap, Bp) - Fraction(q * A, B)
                            assert phase_diff == Fraction(q * det, B * Bp)
                            adjacent_phase_checks += 1

                        # Every future convergent phase is at least as close to
                        # the actual q*alpha lift as the starting convergent bound.
                        for j in range(0, len(ads) - 2):
                            A, B = ac[j]
                            Ap, Bp = ac[j + 1]
                            base_err_bound = Fraction(q, B * Bp)

                            for k in range(j, len(ads) - 1):
                                Ak, Bk = ac[k]
                                Bkp = ac[k + 1][1]
                                drift = absf(Fraction(q, 1) * alpha - Fraction(q * Ak, Bk))
                                assert drift <= Fraction(q, Bk * Bkp)
                                assert Fraction(q, Bk * Bkp) <= base_err_bound
                                future_drift_checks += 1

                    # Matched-scale bounded-type constant estimate.
                    for ads in alpha_families:
                        ac = convergents(ads)
                        Aalpha = max(ads[1:])

                        for j in range(0, len(ads) - 1):
                            A, B = ac[j]
                            Ap, Bp = ac[j + 1]
                            if B <= D < Bp:
                                actual_error_term = W * Fraction(q, B * Bp)
                                Kbeta = (Abeta + 1) ** 2 + 1
                                coarse = (
                                    Fraction(Kbeta * (Aalpha + 1), D)
                                    * a
                                    * a
                                    * absf(delta)
                                )
                                assert actual_error_term <= coarse
                                matched_constant_checks += 1

print("HARD8-07 hyperbolic portal / alpha-frame verifier: PASS")
print("portal_identity_checks", portal_checks)
print("exact_weight_checks", weight_checks)
print("pointwise_alpha_bound_checks", pointwise_checks)
print("adjacent_phase_checks", adjacent_phase_checks)
print("future_drift_checks", future_drift_checks)
print("matched_constant_checks", matched_constant_checks)
