from math import comb, exp

# Corroborative calculations for the random positive-density support corollary.
# For a fixed point x and a block I_t containing N_t shapes, independent
# Bernoulli(delta) deletion makes the diagonal activity D_t(x) exactly
# Binomial(N_t, delta).  This script computes exact lower-tail probabilities
# for moderate N and compares their scale to the coincidence-error exponent.


def binom_lower_tail(N, p, threshold):
    return sum(comb(N, k) * (p ** k) * ((1-p) ** (N-k))
               for k in range(threshold + 1))


def main():
    delta = 0.5
    for N in (40, 80, 160, 320):
        # Deficit below half the mean.
        threshold = int(delta * N / 2)
        tail = binom_lower_tail(N, delta, threshold)
        print("N", N, "P[D <= delta*N/2]", tail)

    # Source block choice q ~ n^(1/4): N_t ~ n^2/q and the coincidence
    # exceptional exponent is order (n/q)^(1/3).
    for n in (256, 1024, 4096, 16384):
        q = max(2, round(n ** 0.25))
        Nt = n * n / q
        activity_chernoff_exponent = delta * Nt / 8.0
        coincidence_exponent = (n / q) ** (1 / 3)
        print(
            "n", n,
            "q", q,
            "N_t_proxy", Nt,
            "activity_exp_proxy", activity_chernoff_exponent,
            "coincidence_exp_proxy", coincidence_exponent,
        )


if __name__ == "__main__":
    main()
