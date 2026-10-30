from math import comb


def burst_block_stats(n, L, j, a, t, s, parity):
    """Evaluate one symmetry type for nu_{n,L}.

    J has size j, T has size t, a=|J intersect T|, and parity is 0/1.
    Returns (cell_mass, unnormalized_laplace, rhs, ratio).
    Floating arithmetic is used only for this diagnostic; this is not a proof.
    """
    sizes = (a, j - a, t - a, n - j - t + a)
    if min(sizes) < 0:
        return None

    empty_mass = 1.0 - 1.0 / L
    r = empty_mass if parity == 0 else 0.0
    lhs = empty_mass * (s ** t) if parity == 0 else 0.0
    denominator = comb(n, L)

    for x0 in range(max(0, L - sum(sizes[1:])), min(sizes[0], L) + 1):
        for x1 in range(max(0, L - x0 - sizes[2] - sizes[3]), min(sizes[1], L - x0) + 1):
            for x2 in range(max(0, L - x0 - x1 - sizes[3]), min(sizes[2], L - x0 - x1) + 1):
                x3 = L - x0 - x1 - x2
                if not (0 <= x3 <= sizes[3]):
                    continue
                count = (
                    comb(sizes[0], x0)
                    * comb(sizes[1], x1)
                    * comb(sizes[2], x2)
                    * comb(sizes[3], x3)
                )
                if count == 0 or ((x0 + x1) & 1) != parity:
                    continue
                mass = count / (L * denominator)
                distance = (t - x0 - x2) + x1 + x3
                r += mass
                lhs += mass * (s ** distance)

    rhs = r ** (2.0 / (1.0 + s)) if r > 0 else 0.0
    ratio = lhs / rhs if rhs > 0 else None
    return r, lhs, rhs, ratio


def exhaustive_max_ratio(n, L, s_values):
    best = (-1.0, None)
    for j in range(n + 1):
        for t in range(n + 1):
            lo = max(0, j + t - n)
            hi = min(j, t)
            for a in range(lo, hi + 1):
                for parity in (0, 1):
                    for s in s_values:
                        out = burst_block_stats(n, L, j, a, t, s, parity)
                        if out is None or out[0] <= 0 or out[2] <= 0:
                            continue
                        if out[3] > best[0]:
                            best = (out[3], (j, t, a, parity, s, out[:3]))
    return best


if __name__ == "__main__":
    coarse = [k / 100.0 for k in range(101)]
    for n, L in ((12, 4), (16, 4), (18, 6), (24, 6)):
        print((n, L), exhaustive_max_ratio(n, L, coarse))

    # Explicit product-profile diagnostic from the integrated theorem.
    n = 64
    variance = 1.0 - (1.0 - 1.0 / n) ** n
    profile_rhs = 2.0 / __import__("math").log(n)
    print("product_n64", variance, profile_rhs, variance - profile_rhs)
