from math import sin, cos, tan, log
from decimal import Decimal, getcontext
getcontext().prec = 90


def dot(a, b):
    return (a & b).bit_count() & 1


def rm1_words(D):
    N = 1 << D
    out = []
    for a in range(1 << D):
        for c in (0, 1):
            out.append([dot(a, x) ^ c for x in range(N)])
    return out


def active_coeff(P, D, Q, h, R, t):
    N = 1 << D
    R = set(R)
    total = 0.0
    sn, cs = sin(t), cos(t)
    for rb in P:
        y = [h[x] * (-1 if rb[x] else 1) for x in range(N)]
        W = sum(y[x] for x in range(N) if x not in Q)
        Z = 1
        for x in R:
            Z *= y[x]
        phase = (1j * sn) ** len(R) * (cs ** (4 - len(R))) * Z
        total += 2 * N * (complex(cos(t * W), sin(t * W)) * phase).real
    return total / len(P)


def hodge_check():
    D = 4
    N = 1 << D
    Q = [0, 1, 2, 3]
    P = rm1_words(D)
    # Deterministic nonlinear fixed phase; not an RM(1,D) character.
    h = [
        -1 if ((((x >> 0) & 1) * ((x >> 2) & 1)) ^ ((x >> 3) & 1)) else 1
        for x in range(N)
    ]
    sigma = 1
    for x in Q:
        sigma *= h[x]
    max_err = 0.0
    for t in (0.07, 0.13, 0.21):
        for i in Q:
            T = [x for x in Q if x != i]
            b1 = active_coeff(P, D, Q, h, [i], t)
            b3 = active_coeff(P, D, Q, h, T, t)
            max_err = max(max_err, abs(b3 + sigma * (tan(t) ** 2) * b1))
    return max_err


def r16_closed_form_float(D, R=400):
    N = 2.0 ** D
    delta = 16 / N - 64 / N**2
    p0 = 1 - delta
    p1 = 64 / N**2
    m = N / 4 - 1
    partial = 0.0
    for r in range(2, R + 1):
        C = 1 - p0**r - m * p1**r
        partial += ((-1) ** r) * C / ((r - 1) * 2 ** (r - 1))
    closed = log(1.5) - p0 * log(1 + p0 / 2) - m * p1 * log(1 + p1 / 2)
    return abs(partial - closed), closed


def r16_D128():
    D = 128
    N = Decimal(2) ** D
    n = Decimal(D - 1)
    delta = Decimal(16) / N - Decimal(64) / (N * N)
    p0 = Decimal(1) - delta
    p1 = Decimal(64) / (N * N)
    A = (Decimal(3) / Decimal(2)).ln()
    Delta_inf = A - p0 * (Decimal(1) + p0 / Decimal(2)).ln() - delta * (Decimal(1) + p1 / Decimal(2)).ln()
    kappa = Decimal(2) / Decimal(3) + Decimal(3).ln() / Decimal(2)
    J = Decimal(8) * n / N
    B = kappa * J - Delta_inf
    floor = Decimal(11) / (Decimal(864) * n**3)
    return {
        "J": str(J),
        "Delta_infty": str(Delta_inf),
        "B_fullspent_proxy": str(B),
        "central_compensation_floor": str(floor),
        "B_over_floor": str(B / floor),
    }


if __name__ == "__main__":
    import json

    out = {
        "hodge_rm1_max_abs_error": hodge_check(),
        "r16_D8_partial_vs_closed": r16_closed_form_float(8),
        "r16_D12_partial_vs_closed": r16_closed_form_float(12),
        "D128": r16_D128(),
        "notes": [
            "finite checks are falsification checks only; REPORT.md contains analytic proofs",
            "B_fullspent_proxy differs from half-band B_d only by the terminal-saturation tail bounded analytically in REPORT.md",
        ],
    }
    print(json.dumps(out, indent=2))
