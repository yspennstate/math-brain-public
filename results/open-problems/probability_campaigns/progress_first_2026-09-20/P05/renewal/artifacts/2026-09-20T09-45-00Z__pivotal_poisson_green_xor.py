from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial

N = 7

@lru_cache(None)
def lcs(x, y):
    # exact LCS length for tuples x,y
    m, n = len(x), len(y)
    dp = [0] * (n + 1)
    for i in range(m):
        prev = 0
        for j in range(1, n + 1):
            old = dp[j]
            if x[i] == y[j-1]:
                dp[j] = prev + 1
            elif dp[j-1] > dp[j]:
                dp[j] = dp[j-1]
            prev = old
    return dp[n]

STR = {n: list(product((0,1), repeat=n)) for n in range(N+1)}

F = {}
Q = {}

for m in range(N+1):
    for n in range(N+1):
        total = 0
        for x in STR[m]:
            for y in STR[n]:
                total += lcs(x,y)
        F[m,n] = Fraction(total, 2**(m+n))

        if m and n:
            piv = 0
            mismatch_pairs = 0
            for x in STR[m]:
                for y in STR[n]:
                    if x[0] != y[0]:
                        A = lcs(x[1:], y)
                        B = lcs(x, y[1:])
                        assert abs(A-B) in (0,1)
                        piv += abs(A-B)
                        mismatch_pairs += 1
            q_direct = Fraction(piv, mismatch_pairs)

            # Exact source-averaged Poisson recurrence.
            q_from_F = (
                4*F[m,n] - 2 - 2*F[m-1,n-1] - F[m-1,n] - F[m,n-1]
            )
            assert q_direct == q_from_F
            assert 0 <= q_direct <= 1
            Q[m,n] = q_direct

            # Common-core insertion-gain XOR representation.
            xor_sum = 0
            core_count = 0
            for u in STR[m-1]:
                for v in STR[n-1]:
                    C = lcs(u,v)

                    # mismatch orientation 0/1
                    alpha = lcs(u, (1,)+v) - C
                    beta  = lcs((0,)+u, v) - C
                    assert alpha in (0,1) and beta in (0,1)
                    xor_sum += abs(alpha-beta)
                    core_count += 1

                    # mismatch orientation 1/0
                    alpha = lcs(u, (0,)+v) - C
                    beta  = lcs((1,)+u, v) - C
                    assert alpha in (0,1) and beta in (0,1)
                    xor_sum += abs(alpha-beta)
                    core_count += 1

            assert Fraction(xor_sum, core_count) == q_direct

def green(start_m, start_n, a, b):
    """
    Probability that the killed reverse walk started at (start_m,start_n)
    ever visits (a,b), with steps
       (-1,-1) prob 1/2, (-1,0) prob 1/4, (0,-1) prob 1/4.
    For a,b>=1, monotonicity means no path reaching (a,b) can hit the
    boundary first.
    """
    dm = start_m - a
    dn = start_n - b
    if dm < 0 or dn < 0:
        return Fraction(0)
    ans = Fraction(0)
    for d in range(min(dm,dn)+1):
        h = dm - d
        v = dn - d
        t = d + h + v
        mult = factorial(t) // (factorial(d)*factorial(h)*factorial(v))
        ans += Fraction(mult) * Fraction(1,2)**d * Fraction(1,4)**(h+v)
    return ans

for n in range(1, N+1):
    green_value = Fraction(0)
    green_mass = Fraction(0)
    green_q_mass = Fraction(0)
    for a in range(1,n+1):
        for b in range(1,n+1):
            g = green(n,n,a,b)
            green_mass += g
            green_q_mass += g * Q[a,b]
            green_value += g * (Fraction(1,2) + Q[a,b]/4)
    assert green_value == F[n,n]

    # The occupation-weighted pivotal density is exactly a deterministic
    # Green average of q_{a,b}.
    p_green = green_q_mass / green_mass
    assert 0 <= p_green <= 1

print("N =", N)
print("diagonal F_n/n:")
for n in range(1,N+1):
    print(n, F[n,n] / n, float(F[n,n] / n))

print("diagonal q_{n,n}:")
for n in range(1,N+1):
    print(n, Q[n,n], float(Q[n,n]))

print("extreme q_{m,1} check:")
for m in range(1,N+1):
    claimed = Fraction(0) if m == 1 else 1 - Fraction(1, 2**(m-1))
    assert Q[m,1] == claimed
    print(m, Q[m,1])

print("EXACT_PIVOTAL_POISSON_GREEN_XOR_PASS")
