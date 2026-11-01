import itertools
import math
from collections import defaultdict

# Finite bookkeeping checker only. This does not verify the universal theorem.

PI = {0: 0.35, 1: 0.30, 2: 0.20, 3: 0.10, 4: 0.05}
NU = sum(k * p for k, p in PI.items())
QBAR = {k: k * p / NU for k, p in PI.items() if k > 0}


def conv_prob(n, m):
    dp = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for s, ps in dp.items():
            for k, pk in PI.items():
                nxt[s + k] += ps * pk
        dp = nxt
    return dp.get(m, 0.0)


def check_cloud_palm_identity(N=4, M=6, L=1):
    p_nm = conv_prob(N, M)
    assert p_nm > 0

    K = {}
    for k, pk in PI.items():
        if k <= 0 or M - k < 0:
            continue
        p_prev = conv_prob(N - 1, M - k)
        if p_prev > 0:
            K[k] = N * k * pk * p_prev / (M * p_nm)

    assert abs(sum(K.values()) - 1.0) < 1e-12

    alpha = sum(v for k, v in K.items() if k > L)
    QL = sum(v for k, v in QBAR.items() if k > L)
    assert alpha > 0 and QL > 0

    Kc = {k: v / alpha for k, v in K.items() if k > L}
    qc = {k: v / QL for k, v in QBAR.items() if k > L}

    lhs = sum(Kc[k] * math.log(Kc[k] / qc[k]) for k in Kc)
    b_cur = -math.log(p_nm)
    e_b_next = sum(
        Kc[k] * (-math.log(conv_prob(N - 1, M - k))) for k in Kc
    )
    rhs = (
        b_cur
        - e_b_next
        - math.log((M / N) / NU)
        + math.log(QL / alpha)
    )

    err = abs(lhs - rhs)
    assert err < 1e-12
    return {
        "N": N,
        "M": M,
        "L": L,
        "alpha": alpha,
        "Q_L": QL,
        "KL_lhs": lhs,
        "identity_rhs": rhs,
        "abs_error": err,
    }


def stopped_event_probability(q, L, U, x, marked_threshold, nmax):
    supp = sorted(q)
    total = 0.0
    for seq in itertools.product(supp, repeat=nmax):
        p = 1.0
        for z in seq:
            p *= q[z]
        S = 0
        C = 0
        hit = False
        for z in seq:
            if z > U:
                break
            S += z
            if z > L:
                C += z
            if S >= x:
                hit = C >= marked_threshold
                break
        if hit:
            total += p
    return total


def transform(q, L, U, t, u):
    return sum(
        pk * math.exp((t if k > L else 0.0) * k - u * k)
        for k, pk in q.items()
        if k <= U
    )


def check_bivariate_bound():
    # Small exact model; all sequences are enumerated.
    L = 1
    U = 3
    x = 3
    marked_threshold = 2
    nmax = 4
    t = 0.10
    u = 0.0

    mf = transform(QBAR, L, U, t, u)
    assert mf <= 1.0 + 1e-12

    exact = stopped_event_probability(
        QBAR, L, U, x, marked_threshold, nmax
    )
    bound = math.exp(-t * marked_threshold + u * (x + U))
    assert exact <= bound + 1e-12

    return {
        "L": L,
        "U": U,
        "x": x,
        "marked_threshold": marked_threshold,
        "nmax": nmax,
        "t": t,
        "u": u,
        "M_LU": mf,
        "exact_event_probability": exact,
        "martingale_bound": bound,
        "slack": bound - exact,
    }


if __name__ == "__main__":
    print("CLOUD_PALM_IDENTITY")
    for k, v in check_cloud_palm_identity().items():
        print(f"{k}={v}")

    print("BIVARIATE_STOPPED_MARTINGALE")
    for k, v in check_bivariate_bound().items():
        print(f"{k}={v}")

    print("ALL_CHECKS_PASSED")
