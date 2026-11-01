from fractions import Fraction


def mm(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def mpow(A, n, Ainv=None):
    if n < 0:
        if Ainv is None:
            raise ValueError("inverse required for negative power")
        return mpow(Ainv, -n, A)
    R = I
    X = A
    while n:
        if n & 1:
            R = mm(R, X)
        X = mm(X, X)
        n //= 2
    return R


def mod2(A):
    return tuple(tuple(x % 2 for x in row) for row in A)


def add(A, B, scale=1):
    return tuple(
        tuple(A[i][j] + scale * B[i][j] for j in range(3))
        for i in range(3)
    )


def comm(A, Ai, B, Bi):
    return mm(mm(mm(A, B), Ai), Bi)


E12 = ((0, 1, 0), (0, 0, 0), (0, 0, 0))
E21 = ((0, 0, 0), (1, 0, 0), (0, 0, 0))
E23 = ((0, 0, 0), (0, 0, 1), (0, 0, 0))
E31 = ((0, 0, 0), (0, 0, 0), (1, 0, 0))
E13 = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
E32 = ((0, 0, 0), (0, 0, 0), (0, 1, 0))

x = add(I, E12)
xi = add(I, E12, -1)
P = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
Pi = mm(P, P)

# Free subgroup seed in the upper-left SL_2(Z) block.
u = add(I, E12, 2)
ui = add(I, E12, -2)
v = add(I, E21, 2)
vi = add(I, E21, -2)

# Exact generation check for B={x,x^{-1},P,P^{-1}}.
e23 = mm(mm(P, x), Pi)
e31 = mm(mm(Pi, x), P)
e23i = add(I, E23, -1)
e31i = add(I, E31, -1)
e13 = comm(x, xi, e23, e23i)
e21 = comm(e23, e23i, e31, e31i)
e32 = comm(e31, e31i, x, xi)

assert mm(P, Pi) == I and mm(Pi, P) == I and mm(P, mm(P, P)) == I
assert e23 == add(I, E23)
assert e31 == add(I, E31)
assert e13 == add(I, E13)
assert e21 == add(I, E21)
assert e32 == add(I, E32)

# Five Schreier generators a_j=u^j v u^{-j}; code checks matrix-level
# distinctness and congruence separation from B. Freeness is proved in report
# by ping-pong for <u,v> and the standard Schreier basis of ker(F_2 -> Z).
ajs = []
for j in range(5):
    aj = mm(mm(mpow(u, j, ui), v), mpow(ui, j, u))
    aji = mm(mm(mpow(u, j, ui), vi), mpow(ui, j, u))
    ajs.extend([aj, aji])

assert len(set(ajs)) == 10
assert all(mod2(a) == I for a in ajs)
B = [x, xi, P, Pi]
assert len(set(B)) == 4
assert all(mod2(b) != I for b in B)
assert set(ajs).isdisjoint(B)

# Percolation/operator arithmetic for free rank 5 plus four complements.
q = 9                  # tree forward degree = 2m-1, m=5
r = 4
D = q + 1 + r          # full Cayley degree
adjacency_norm_bound = 10  # 2*sqrt(9)+4

# For z^2-a z+(D-1), the larger root beta is < q once q is to the
# right of both roots and P(q)>0.
Pq = q*q - adjacency_norm_bound*q + (D - 1)
assert Pq == 4
assert q*q > D - 1

# beta_14(10)=5+2*sqrt(3). The exact gap is
# 1/beta - 1/9 = (32-18*sqrt(3))/117.
# sqrt(3)<26/15 gives the rational certificate gap>4/585.
assert 3 * 15 * 15 < 26 * 26
rational_gap = Fraction(4, 585)

# General tradeoff condition specializes at q=9 to r<9/2.
assert Fraction(r, 1) < Fraction(9, 2)

# Minimality check for this coarse class theorem: q=7,r=4 fails
# r < q*(sqrt(q)-1)/(sqrt(q)+1). This is equivalent here to
# sqrt(7)>? 11/3 after rearrangement; the exact sign test below records
# that 7 < (11/3)^2, so the required opposite inequality fails.
assert 7 * 9 < 121

print("SL3_GENERATION_CONJUGATES_OK")
print("FREE_CORE_DIRECTED_GENERATORS_DISTINCT=10")
print("FREE_CORE_ALL_IDENTITY_MOD_2=True")
print("COMPLEMENT_SIZE=4")
print("COMPLEMENT_DISJOINT_BY_MOD_2=True")
print(f"q={q} r={r} D={D} adjacency_norm_bound={adjacency_norm_bound}")
print(f"characteristic_polynomial_at_q={Pq}>0")
print("beta_14(10)=5+2*sqrt(3)<9")
print("gap_exact=(32-18*sqrt(3))/117")
print(f"gap_rational_lower={rational_gap}={float(rational_gap):.15f}")
print("rank_complement_threshold_q9=9/2; r=4 passes")
print("rank4_r4_coarse_test_fails (useful minimality check)")
print("ALL_EXACT_CHECKS_PASS")
