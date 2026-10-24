from fractions import Fraction as F
from math import comb


def triangle_matrix(p):
    """Mean matrix for forward-fibre exploration in T_6 x C_3."""
    C = [[F(0) for _ in range(4)] for _ in range(4)]
    C[1][1] = (1-p)**2
    C[1][2] = 2*p*(1-p)**2
    C[1][3] = 3*p**2 - 2*p**3
    C[2][2] = (1-p)**2
    C[2][3] = 2*p - p**2
    C[3][3] = 1
    P = [[F(0) for _ in range(3)] for _ in range(3)]
    for k in (1, 2, 3):
        for ell in (1, 2, 3):
            P[k-1][ell-1] = sum(
                F(comb(k, j))*p**j*(1-p)**(k-j)*C[j][ell]
                for j in range(1, k+1)
            )
    return [[5*x for x in row] for row in P]


p0 = F(473, 3125)                  # 0.15136
v = [10_000_000, 19_495_060, 28_521_640]
M = triangle_matrix(p0)
diff = [sum(M[i][j]*v[j] for j in range(3)) - v[i] for i in range(3)]

# Rational upper bound for sqrt(5), used in the ambient degree-9
# nonbacktracking characteristic-root comparison.
sqrt5_upper = F(559017, 250000)    # 2.236068
pu_floor = F(16189, 100000)        # 0.16189
z0 = 1 / pu_floor
sqrt_margin = sqrt5_upper**2 - 5
nb_margin = z0 + F(8, 1)/z0 - (F(3, 1) + 2*sqrt5_upper)
gap = pu_floor - p0

print("p0 =", p0, "=", float(p0))
print("M =")
for row in M:
    print("  ", [str(x) for x in row])
print("v =", v)
for i, x in enumerate(diff, 1):
    print(f"(Mv-v)_{i} = {x} = {float(x):.15f}")
print("all_Mv_gt_v =", all(x > 0 for x in diff))
print("sqrt5_upper =", sqrt5_upper)
print("sqrt5_upper^2-5 =", sqrt_margin, "=", float(sqrt_margin))
print("pu_floor =", pu_floor, "=", float(pu_floor))
print("z0 =", z0, "=", float(z0))
print("z0^2-8 =", z0*z0-F(8, 1), "=", float(z0*z0-F(8, 1)))
print("NB margin z0+8/z0-(3+2 sqrt5_upper) =", nb_margin, "=", float(nb_margin))
print("gap floor =", gap, "=", float(gap))
print("n_threshold = 12*1+16 =", 12*1+16)

assert all(x > 0 for x in diff)
assert sqrt_margin > 0
assert z0*z0 > 8
assert nb_margin > 0
assert gap == F(1053, 100000)
assert 12*1 + 16 == 28
print("ALL_EXACT_CHECKS_PASS")
