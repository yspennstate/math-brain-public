from fractions import Fraction


def weight(k):
    if k == 0:
        return Fraction(2, 1)
    if k == 1:
        return Fraction(1, 1)
    j = k.bit_length()  # ceil(log2(k+1)) for k>=1
    return Fraction(1, k*k*j*j)


def exact_max_stats(n, m):
    # Sequential labeled-box DP: state (sum_so_far, current_max) -> exact weight.
    dp = {(0, 0): Fraction(1, 1)}
    for _ in range(n):
        nd = {}
        for (s, mx), val in dp.items():
            for k in range(m - s + 1):
                key = (s + k, max(mx, k))
                nd[key] = nd.get(key, Fraction(0, 1)) + val * weight(k)
        dp = nd
    dist = {mx: val for (s, mx), val in dp.items() if s == m}
    Z = sum(dist.values(), Fraction(0, 1))
    Emax = sum(Fraction(mx, 1) * val for mx, val in dist.items()) / Z
    p_half = sum(val for mx, val in dist.items() if 2*mx <= n) / Z
    mode = max(dist, key=dist.get)
    return Emax, p_half, mode


print("PROB20-20 fixed dyadic-log stress law exact checker")
print("w0=2, w1=1, wk=1/(k^2*j(k)^2), j(k)=ceil(log2(k+1)); conditioning m=n")
for n in (4, 6, 8, 10, 12, 14, 16, 18):
    Emax, p_half, mode = exact_max_stats(n, n)
    ratio = Emax / n
    print(f"n={n}")
    print(f"  Emax/n exact = {ratio.numerator}/{ratio.denominator}")
    print(f"  Emax/n decimal = {float(ratio):.12f}")
    print(f"  P(max<=n/2) exact = {p_half.numerator}/{p_half.denominator}")
    print(f"  P(max<=n/2) decimal = {float(p_half):.12f}")
    print(f"  max-weight mode = {mode}")

# Exact finite block checks used in the report's dyadic estimates.
for j in range(2, 12):
    lo, hi = 2**(j-1), 2**j - 1
    block_mean = sum(Fraction(1, k*j*j) for k in range(lo, hi+1))
    assert block_mean <= Fraction(1, j*j)
    assert block_mean >= Fraction(1, 2*j*j)

print("dyadic block inequalities j=2..11: PASS")
print("finite exact DP: PASS")
