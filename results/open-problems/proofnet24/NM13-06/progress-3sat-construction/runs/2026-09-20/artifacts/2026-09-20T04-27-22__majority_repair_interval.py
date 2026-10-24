#!/usr/bin/env python3
"""
Validated local-weak-limit check for the majority-start nonbacktracking
repair process in iid random 3-SAT.

For alpha, let P,N ~ Pois(mu), mu=3 alpha/2, independently.
A uniformly sampled false literal under the majority assignment size-biases
(P,N) by Z=min(P,N). Put M=max(P,N) and
    q = E Z / (2 mu).
Conditionally on (P,N), the number B of critical clauses broken by flipping
that variable converges to Bin(M,q^2).
For non-root repair clauses there are two fresh candidate variables, so the
tree-level offspring is Y=min(B1,B2), and
    r2 = E Y = sum_{t>=1} P(B>=t)^2.

We truncate P,N at K. mpmath.iv provides outward-rounded interval arithmetic.
The omitted size-biased mass obeys
  delta_Z <= 2 mu P(Pois(mu)>=K),
and the omitted contribution to sum_{t>K} P(B>=t)^2 is at most
  delta_PM/EZ0, delta_PM <= 2 mu^2 P(Pois(mu)>=K),
because Z*M=P*N and x^2<=x.
The Poisson tail is bounded by the standard Chernoff bound
  P(Pois(mu)>=K) <= exp(-mu) (e mu/K)^K, K>mu.
"""
import mpmath as mp

mp.iv.dps = 50
iv = mp.iv


def certify(alpha_string, K=50):
    alpha = iv.mpf(alpha_string)
    mu = iv.mpf("1.5") * alpha

    pois = [iv.exp(-mu)]
    for k in range(K):
        pois.append(pois[-1] * mu / (k + 1))

    ez0 = iv.mpf("0")
    pairs = []
    for p in range(K + 1):
        for n in range(K + 1):
            z = min(p, n)
            if not z:
                continue
            m = max(p, n)
            wz = pois[p] * pois[n] * z
            ez0 += wz
            pairs.append((wz, m))

    ch = iv.exp(-mu) * (iv.exp(iv.mpf("1")) * mu / K) ** K
    delta_z = 2 * mu * ch

    ez_lo, ez_hi = ez0.a, ez0.b
    mu_lo, mu_hi = mu.a, mu.b
    q_lo = ez_lo / (2 * mu_hi)
    q_hi = (ez_hi + delta_z.b) / (2 * mu_lo)
    q = iv.mpf([q_lo, q_hi])
    r = q * q

    tails_by_m = {}
    for m in range(K + 1):
        tails = [iv.mpf("0")] * (K + 1)
        if m:
            pmf = [iv.mpf("0")] * (m + 1)
            pmf[0] = (1 - r) ** m
            ratio = r / (1 - r)
            for k in range(m):
                pmf[k + 1] = pmf[k] * (m - k) / (k + 1) * ratio
            s = iv.mpf("0")
            for k in range(m, 0, -1):
                s += pmf[k]
                tails[k] = s
        tails_by_m[m] = tails

    r2_upper = iv.mpf("0")
    for t in range(1, K + 1):
        num = iv.mpf("0")
        for wz, m in pairs:
            if m >= t:
                num += wz * tails_by_m[m][t]
        tail_upper = (num.b + delta_z.b) / ez_lo
        r2_upper += tail_upper * tail_upper

    delta_pm = 2 * mu_hi * mu_hi * ch.b
    r2_upper += delta_pm / ez_lo

    r1 = mu * q / 2
    unsat_density = alpha * q * q * q

    q_mid = (float(q_lo.mid) + float(q_hi.mid)) / 2.0

    print(f"alpha={alpha_string}")
    print(f"K={K}")
    print(f"q_false_literal in [{float(q_lo.mid):.15f}, {float(q_hi.mid):.15f}]")
    print(f"r1_random_candidate in [{float(r1.a.mid):.15f}, {float(r1.b.mid):.15f}]")
    print(f"r2_nonbacktracking <= {float(r2_upper.b.mid):.15f}")
    print(f"majority_unsat_density in [{float(unsat_density.a.mid):.15f}, {float(unsat_density.b.mid):.15f}]")
    print(f"q_mid_readability={q_mid:.15f}")
    print(f"poisson_chernoff_tail <= {float(ch.b.mid):.3e}")
    print(f"omitted_size_biased_mass <= {float(delta_z.b.mid):.3e}")
    print(f"omitted_r2_tail_numerator <= {float(delta_pm.mid):.3e}")
    print(f"subcritical_certificate={bool(r2_upper.b < iv.mpf('1'))}")
    print()


if __name__ == "__main__":
    for a in ("3.52", "4.0", "4.4898"):
        certify(a)
