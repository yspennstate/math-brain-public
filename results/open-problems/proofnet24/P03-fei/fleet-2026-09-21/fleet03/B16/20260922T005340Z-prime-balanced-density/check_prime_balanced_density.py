"""Sanity/certificate calculations for the B16 prime-balanced density theorem.

This does NOT prove FEI. The theorem in REPORT.md is analytic. The exact
integer checks below verify the numerical threshold N>=64 used in its
probabilistic construction, and the floating-point rows only illustrate the
explicit continuity/error bounds.
"""
from math import log, log2, sqrt

N0 = 64

# ln 2 < 7/10, so 16 ln(2) N^8 < (56/5) N^8. The first exact inequality
# proves the case-2 union bound at N0; the second exact difference makes
# 2^N/N^8 increase from N0 onward.
assert 5 * (1 << N0) > 56 * N0**8
assert 2 * N0**8 > (N0 + 1)**8

# To make the total probability of any nontrivial decomposition smaller than
# the exact-balance event it suffices that 2^N > 20 N^5. Again the second
# exact check makes 2^N/N^5 increase from N0 onward.
assert (1 << N0) > 20 * N0**5
assert 2 * N0**5 > (N0 + 1)**5


def h2(x):
    if x == 0 or x == 1:
        return 0.0
    return -x * log2(x) - (1-x) * log2(1-x)


print("PASS")
print("N0", N0)
print("threshold_case2_gap_exact", 5*(1 << N0) - 56*N0**8)
print("threshold_balance_gap_exact", (1 << N0) - 20*N0**5)
print("monotone_N8_gap_exact", 2*N0**8 - (N0+1)**8)
print("monotone_N5_gap_exact", 2*N0**5 - (N0+1)**5)

for N in (64, 80, 100, 128):
    delta = N**-4
    eta = delta * (1 + 2**(1-N))
    tau = 2*sqrt(eta)
    entropy_err = h2(tau) + tau*N
    influence_err = 2*N*eta

    # From REPORT.md:
    # P(non-prime) < 2^(3N) exp(-2^N/(4N^4)).
    log2_prime_failure = 3*N - (2**N/(4*N**4))/log(2)
    # P(the selected exact-balance event) > 2^(-2N).
    log2_balance_lower = -2*N
    assert log2_prime_failure < log2_balance_lower

    print(
        "row",
        N,
        "delta", format(delta, ".17g"),
        "eta_upper", format(eta, ".17g"),
        "tv_upper", format(tau, ".17g"),
        "entropy_error_upper_bits", format(entropy_err, ".17g"),
        "influence_error_upper", format(influence_err, ".17g"),
        "log2_prime_failure_upper", format(log2_prime_failure, ".17g"),
        "log2_balance_event_lower", log2_balance_lower,
    )
