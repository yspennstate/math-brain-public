from fractions import Fraction


def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x + y, x - y
        h *= 2
    return a


def product_spectral_marginals(W, n):
    N = 1 << n
    den = N * N
    p = [Fraction(w*w, den) for w in W]
    theta = [sum(p[s] for s in range(N) if (s >> i) & 1)
             for i in range(n)]
    for s in range(N):
        q = Fraction(1, 1)
        for i, t in enumerate(theta):
            q *= t if ((s >> i) & 1) else (1 - t)
        if q != p[s]:
            return None
    return theta


def main():
    all_good = True
    for n in range(1, 5):
        N = 1 << n
        count = 0
        profiles = {}
        active_fixed_counts = {}
        for mask in range(1 << (N - 1)):
            # Quotient by global output sign by fixing f(0)=+1.
            vals = [1] + [-1 if (mask >> j) & 1 else 1
                          for j in range(N - 1)]
            W = fwht_int(vals)
            theta = product_spectral_marginals(W, n)
            if theta is None:
                continue
            count += 1
            profile = tuple(theta)
            profiles[profile] = profiles.get(profile, 0) + 1
            active = [t for t in theta if t not in (0, 1)]
            if any(t != Fraction(1, 2) for t in active) or len(active) % 2:
                all_good = False
                raise AssertionError((n, mask, theta))
            key = (sum(t == Fraction(1, 2) for t in theta),
                   sum(t == 1 for t in theta))
            active_fixed_counts[key] = active_fixed_counts.get(key, 0) + 1
        print(f"n={n}: product-spectrum functions modulo global sign={count}; "
              f"distinct marginal profiles={len(profiles)}")
        print("  (number fair-active, number fixed-one) -> count:",
              sorted(active_fixed_counts.items()))
    print("PASS: through n=4, every independent spectral coordinate is "
          "deterministic or fair, and the number of fair coordinates is even.")
    print("The exhaustive check is only a sanity check; the report gives a "
          "dimension-free arithmetic proof.")
    assert all_good


if __name__ == "__main__":
    main()
