"""Independent finite-ring enumeration for the 1D cumulant sanity check.

At beta=(log 2)/2, q=e^(-2 beta)=1/2. Each periodic spin
configuration has relative weight 2^(-number_of_domain_walls).
"""

from fractions import Fraction


def ring_cumulant_per_site(n: int) -> Fraction:
    mask_all = (1 << n) - 1
    z = m2 = m4 = 0
    for mask in range(1 << n):
        rot = ((mask << 1) & mask_all) | (mask >> (n - 1))
        walls = (mask ^ rot).bit_count()
        weight = 1 << (n - walls)
        spin_sum = 2 * mask.bit_count() - n
        z += weight
        m2 += weight * spin_sum**2
        m4 += weight * spin_sum**4
    variance = Fraction(m2, z)
    fourth = Fraction(m4, z) - 3 * variance**2
    return fourth / n


if __name__ == "__main__":
    predicted = Fraction(1, Fraction(1, 2)) - 3 / Fraction(1, 2) ** 3
    print(f"infinite_volume_prediction={predicted}")
    for n in (8, 12, 16):
        observed = ring_cumulant_per_site(n)
        print(f"N={n} kappa4_per_site={float(observed):.12f} error={float(observed-predicted):.12f}")
