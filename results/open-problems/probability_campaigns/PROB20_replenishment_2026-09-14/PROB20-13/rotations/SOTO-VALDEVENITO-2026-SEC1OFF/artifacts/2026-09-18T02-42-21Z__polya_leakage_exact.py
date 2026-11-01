from fractions import Fraction
from itertools import product
from math import comb, factorial


def polya_seq_prob(bits):
    """Exact probability of a left/right side sequence in Theorem 2.6's insertion law.

    bit=1 means the next worse rank is inserted on the left of the current block,
    bit=0 means it is inserted on the right.
    """
    left = right = 0
    prob = Fraction(1, 1)
    for t, bit in enumerate(bits, start=2):
        if bit:
            prob *= Fraction(left + 1, t)
            left += 1
        else:
            prob *= Fraction(right + 1, t)
            right += 1
    return prob


def beta_mix_prob(bits):
    """Integral_0^1 theta^L (1-theta)^R dtheta, exactly."""
    left = sum(bits)
    right = len(bits) - left
    return Fraction(factorial(left) * factorial(right), factorial(left + right + 1))


def r2_success_direct(N):
    """Exact Bayes-optimal success for r=2 after observing M lower-left arrivals.

    Under the uniform-Beta representation, M is uniform on {0,...,N}; posterior
    theta | M=m is Beta(m+1,N-m+1).  The two top candidates are ordered as
    (x2,x1) with posterior probability (m+1)/(N+2), otherwise as (x1,x2).
    """
    return sum(Fraction(max(m + 1, N - m + 1), N + 2) for m in range(N + 1)) / (N + 1)


def r2_success_closed(N):
    if N % 2 == 0:
        h = N // 2
        return Fraction(3 * h + 1, 2 * (2 * h + 1))
    h = (N - 1) // 2
    return Fraction(3 * h + 4, 2 * (2 * h + 3))


def asymptotic_ak(k):
    """Exact integral of the mode of Bin(k-1,theta), theta uniform on [0,1].

    The maximizing count j is constant on theta in [j/k,(j+1)/k].
    Polynomial expansion therefore gives an exact rational value.
    """
    n = k - 1
    total = Fraction(0, 1)
    for j in range(k):
        lo = Fraction(j, k)
        hi = Fraction(j + 1, k)
        r = n - j
        for ell in range(r + 1):
            coeff = comb(n, j) * comb(r, ell) * ((-1) ** ell)
            power = j + ell + 1
            total += Fraction(coeff, power) * (hi ** power - lo ** power)
    return total


def main():
    # Exact finite verification of the Pólya/Beta-mixture identity.
    for n in range(2, 11):
        for bits in product((0, 1), repeat=n - 1):
            assert polya_seq_prob(bits) == beta_mix_prob(bits)
    print("POLYA_BETA_EQUIVALENCE_PASS n<=10 all side strings")

    # Exact finite verification of the r=2 posterior closed form.
    for N in range(0, 51):
        assert r2_success_direct(N) == r2_success_closed(N)
    print("R2_POSTERIOR_CLOSED_FORM_PASS N<=50")

    # Exact asymptotic mode-integrals used in the report.
    for k in range(1, 11):
        print(f"a_{k}={asymptotic_ak(k)}")

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
