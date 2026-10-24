from fractions import Fraction

# Exact self-check for the finite-depth branching-process-in-varying-environment
# comparator used in the R16/I0043 STUCK_RECOVERY_2 report.
#
# At level k, retain each of two children independently with
#   p_k = (N+k)/(2(N+k-1)).
# Then m_k = 2 p_k and the expected generation-size multiplier is
#   M_n = prod_{k=1}^n m_k = (N+n)/N.
# If u_k is the probability that one particle at level k reaches level n,
#   u_n = 1,
#   u_{k-1} = 1 - (1-p_k u_k)^2.
# The report proves
#   1/u_0 >= 1/M_n + (1/4) sum_{j=0}^{n-1} 1/M_j.
# Everything below uses exact Fraction arithmetic.


def finite_bpve_check(N: int, nmax: int):
    M = Fraction(1, 1)
    final_row = None
    for n in range(1, nmax + 1):
        p = Fraction(N + n, 2 * (N + n - 1))
        m = 2 * p
        M *= m
        assert M == Fraction(N + n, N)

        u = Fraction(1, 1)
        for k in range(n, 0, -1):
            pk = Fraction(N + k, 2 * (N + k - 1))
            u = 1 - (1 - pk * u) ** 2

        reciprocal_sum = sum(
            (Fraction(N, N + j) for j in range(n)), Fraction(0, 1)
        )
        upper_bound = 1 / (
            Fraction(N, N + n) + Fraction(1, 4) * reciprocal_sum
        )
        assert u <= upper_bound
        final_row = (n, u, upper_bound)
    return final_row


for N in (3, 5, 10):
    n, survival, upper = finite_bpve_check(N, 15)
    print(
        f"N={N}: n={n} survival={float(survival):.12f}, "
        f"upper_bound={float(upper):.12f}"
    )

print("ALL_EXACT_FINITE_BPVE_CHECKS_PASS")
