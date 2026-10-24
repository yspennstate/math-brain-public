from fractions import Fraction

# Exact specialization m=2, delta=1 for the one-unit cap-layer theorem.
m = 2
delta = Fraction(1, 1)
A = Fraction(2 * m, 1) + delta
C0 = 2 * A
K = int(4 * m + delta) + 1  # 4m+delta=9 is integral here
theta = Fraction(K, 1) - (Fraction(4 * m, 1) + delta)

p = {}
p[m] = A / (A + m * (Fraction(m, 1) + delta))
for k in range(m + 1, K + 1):
    p[k] = (
        Fraction(m, 1)
        * (Fraction(k - 1, 1) + delta)
        * p[k - 1]
        / (A + Fraction(m, 1) * (Fraction(k, 1) + delta))
    )

# d(w)=min(1,(w-C0)_+). Here theta=1 at k=10, so
# Dcap=sum_{k>=10}(k+1)p_k. Compactify the tail with the exact
# mean-attractiveness identity sum_k (k+delta)p_k=A.
Dcap = (
    A
    - sum((Fraction(k, 1) + delta) * p[k] for k in range(m, K))
    - (1 - theta) * (Fraction(K, 1) + delta) * p[K]
)
expected = Fraction(98304, 96577)

print(f"A={A}")
print(f"C0={C0}")
print(f"K={K}")
print(f"theta={theta}")
for k in range(m, K + 1):
    print(f"p_{k}={p[k]}")
print(f"Dcap={Dcap}")
print(f"Dcap_float={float(Dcap):.18f}")
print(f"expected={expected}")
print(f"Dcap_matches_expected={Dcap == expected}")
print(f"Dcap_positive={Dcap > 0}")
assert theta == 1
assert Dcap == expected
assert Dcap > 0
print("ALL_EXACT_CHECKS_PASS")
