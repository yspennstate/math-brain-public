from fractions import Fraction
from math import log

# Finite-support critical test law. This is only an algebra/indexing checker;
# it is not evidence for the infinite-variance target theorem.
PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
MAX_N = 40


def convolution_distribution(m):
    dist = {0: Fraction(1)}
    for _ in range(m):
        nxt = {}
        for s, p in dist.items():
            for x, px in PI.items():
                nxt[s + x] = nxt.get(s + x, Fraction(0)) + p * px
        dist = nxt
    return dist


SUM = [convolution_distribution(m) for m in range(MAX_N + 1)]


def p_sum(m, s):
    if m < 0:
        return Fraction(0)
    return SUM[m].get(s, Fraction(0))


def nu(m):
    # One-tree Dwass: P(|T|=m)=m^{-1}P(S_m=m-1).
    if m <= 0:
        return Fraction(0)
    return p_sum(m, m - 1) / m


def forest_total(m, b):
    # Forest Dwass for b ordinary GW trees.
    if b == 0:
        return Fraction(1) if m == 0 else Fraction(0)
    if m <= 0:
        return Fraction(0)
    return Fraction(b, m) * p_sum(m, m - b)


def ordinary_k2_prefix():
    # A=N_2=1+Z_1, B=Z_2.  Conditional on Z_1=d, B is S_d.
    out = {}
    for d, pd in PI.items():
        a = 1 + d
        for b, pb in SUM[d].items():
            out[(a, b)] = out.get((a, b), Fraction(0)) + pd * pb
    return out


P2 = ordinary_k2_prefix()
assert sum(P2.values(), Fraction(0)) == 1
# Criticality: E Z_2=1, so b*p_k is a probability law.
assert sum(Fraction(b) * p for (a, b), p in P2.items()) == 1


def check_n(n):
    a_n = p_sum(n, n - 1)
    nu_n = nu(n)
    assert a_n > 0 and nu_n > 0

    # Exact branching prefix law under |T|=n.
    q = {}
    for (a, b), p in P2.items():
        f = forest_total(n - a, b)
        if f:
            q[(a, b)] = p * f / nu_n
    assert sum(q.values(), Fraction(0)) == 1

    c = sum(prob for (a, b), prob in q.items() if b >= 1)
    assert c > 0

    # Exact Kesten-reference likelihood-ratio identity:
    # q(a,b)/(b p(a,b)) = n/(n-a) * P(S_{n-a}=n-a-b)/a_n.
    for (a, b), prob in q.items():
        if b < 1:
            continue
        p_hat = Fraction(b) * P2[(a, b)]
        lhs = prob / p_hat
        rhs = Fraction(n, n - a) * p_sum(n - a, n - a - b) / a_n
        assert lhs == rhs

    # Numerical check of the exact entropy/local-cost identity:
    # D(q~/p_hat)+E I_{n-A}(B)
    # = lambda_n-log c + E log(n/(n-A)).
    kl = 0.0
    e_local = 0.0
    e_shift = 0.0
    for (a, b), prob in q.items():
        if b < 1:
            continue
        tq = float(prob / c)
        p_hat = float(Fraction(b) * P2[(a, b)])
        kl += tq * log(tq / p_hat)
        local_atom = float(p_sum(n - a, n - a - b))
        assert local_atom > 0
        e_local += tq * (-log(local_atom))
        e_shift += tq * log(n / (n - a))

    rhs = -log(float(a_n)) - log(float(c)) + e_shift
    gap = (kl + e_local) - rhs
    assert abs(gap) < 1e-12

    # Weighted-density identity for r=1/2:
    # E_q B^r = E_{p_hat}[B^r R].
    r = 0.5
    e_cond = sum(float(prob) * (b ** r) for (a, b), prob in q.items())
    e_hat_r = 0.0
    l1 = 0.0
    for (a, b), p in P2.items():
        if b < 1:
            continue
        p_hat = float(Fraction(b) * p)
        q_prob = float(q.get((a, b), Fraction(0)))
        ratio = q_prob / p_hat
        e_hat_r += p_hat * (b ** r) * ratio
        l1 += p_hat * abs(ratio - 1.0)
    assert abs(e_cond - e_hat_r) < 1e-12

    return {
        "n": n,
        "a_n": float(a_n),
        "c_n2": float(c),
        "KL": kl,
        "E_local": e_local,
        "rhs": rhs,
        "identity_gap": gap,
        "E_conditioned_B^r": e_cond,
        "E_Kesten_B^r_R": e_hat_r,
        "unweighted_L1_density_gap": l1,
    }


if __name__ == "__main__":
    print("critical law PI={0:1/2,1:1/4,3:1/4}; k=2; r=1/2")
    for n in (8, 10, 12, 20, 30):
        row = check_n(n)
        print(
            "n={n} a_n={a_n:.15g} c={c_n2:.15g} "
            "KL={KL:.15g} E_local={E_local:.15g} rhs={rhs:.15g} "
            "gap={identity_gap:.3g} EBr={E_conditioned_B^r:.15g} "
            "KestenWeighted={E_Kesten_B^r_R:.15g} L1={unweighted_L1_density_gap:.15g}".format(**row)
        )
    print("ALL_ASSERTIONS_PASSED")
