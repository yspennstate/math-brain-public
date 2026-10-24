#!/usr/bin/env python3
"""Self-checks for the codimension-2 terminal-retained relation-diagonal no-go.

The symbolic theorem is in REPORT.md. These calculations check exact finite
instances and the asymptotic lower-bound numerics. They are not a proof of FEI.
"""
from math import sin, cos, log, sqrt, pi


def xor_points(A):
    z = 0
    aa = A
    while aa:
        b = aa & -aa
        z ^= b.bit_length() - 1
        aa -= b
    return z


def event_relations(n):
    N = 1 << n
    # g=1 on the codimension-2 face x_1=x_2=0.
    gmask = sum(1 << x for x in range(N) if (x & 3) == 0)
    event = []
    for A in range(1 << N):
        q = A.bit_count()
        if q & 1:
            continue
        if xor_points(A) != 0:
            continue
        if (A & gmask).bit_count() & 1:
            event.append(A)
    return N, gmask, event


def finite_exactish_checks():
    total_relations = 0
    packet_checks = 0
    probability_checks = 0
    translated_frustration_checks = 0
    cauchy_checks = 0
    for n in (2, 3, 4):
        N, gmask, event = event_relations(n)
        total_relations += len(event)
        # RM(1,n)^perp has dimension N-n-1; the g-odd coset is half of it.
        assert len(event) == 1 << (N - n - 2)
        # Every retained relation is frustrated under all four translations
        # of the codimension-2 base face.
        for A in event:
            for t in range(4):
                parity = sum(
                    1 for x in range(N)
                    if ((A >> x) & 1) and ((x & 3) == t)
                ) & 1
                assert parity == 1
                translated_frustration_checks += 1
        for theta in (0.07, 0.11, 0.20):
            p = sin(theta) ** 2
            rho = 1 - 2*p
            a = rho ** (N/4)
            P_formula = (1-a) ** 4 / (4*N)
            Pprime = a * (1-a) ** 3 / (2*rho)
            Q_formula = N*p*P_formula + p*(1-p)*Pprime

            P_sum = 0.0
            Q_sum = 0.0
            Sinv_sum = 0.0
            signed_sum = 0.0
            for A in event:
                q = A.bit_count()
                w = p**q * (1-p)**(N-q)
                P_sum += w
                Q_sum += q*w
                Sinv_sum += w/q
                signed_sum += (
                    2 * ((-1) ** (q//2))
                    * sin(theta)**q * cos(theta)**(N-q)
                )
            s = N*theta
            G_formula = (cos(s) - 4*cos(s/2) + 3) / N

            assert abs(P_sum-P_formula) < 2e-13
            assert abs(Q_sum-Q_formula) < 2e-13
            assert abs(signed_sum-G_formula) < 2e-13
            assert Sinv_sum + 1e-15 >= P_sum*P_sum/Q_sum

            packet_checks += 1
            probability_checks += 2
            cauchy_checks += 1
    return {
        "event_relations_enumerated": total_relations,
        "packet_checks": packet_checks,
        "probability_moment_checks": probability_checks,
        "translated_frustration_checks": translated_frustration_checks,
        "cauchy_checks": cauchy_checks,
    }


def live_phase_row(n):
    N = 1 << n
    target = N / sqrt(2*n)
    k = round((target - pi) / (4*pi))
    s = pi + 4*pi*k
    theta = s/N
    # For large n this is inside the current half-band corridor:
    # 40 < s < N/sqrt(2(n-1)).
    assert s > 40
    assert s < N/sqrt(2*(n-1))

    p = sin(theta)**2
    rho = 1 - 2*p
    loga = (N/4)*log(rho)
    a = 0.0 if loga < -745 else pow(rho, N/4)

    P = (1-a)**4/(4*N)
    Pprime = 0.0 if a == 0.0 else a*(1-a)**3/(2*rho)
    Q = N*p*P + p*(1-p)*Pprime
    Dinv_lower = 4*P*P/Q

    # s == pi mod 4pi, so the exact coherent packet is G=2/N.
    G2 = 4/(N*N)
    ratio_lower = Dinv_lower/G2

    D0 = 4*P
    coherent_to_unweighted_diagonal = G2/D0
    return (
        n, p*n, a, ratio_lower,
        coherent_to_unweighted_diagonal,
        s-target,
    )


if __name__ == "__main__":
    checks = finite_exactish_checks()
    print("status=PASS")
    for k, v in checks.items():
        print(f"{k}={v}")
    print("asymptotic columns=n,n*p,a,Dinv/G2_lower,G2/D0,s-target")
    for n in (8, 12, 16, 24, 32, 48, 64, 96, 128):
        row = live_phase_row(n)
        print(
            f"{row[0]},{row[1]:.12e},{row[2]:.12e},"
            f"{row[3]:.12e},{row[4]:.12e},{row[5]:.12e}"
        )
