from fractions import Fraction
from itertools import product, combinations

N = 3
Q = Fraction(2, N)


def flip(x, i):
    return x ^ (1 << i)


def rates(weights):
    c = [[Fraction(0) for _ in range(N)] for _ in range(1 << N)]
    for x in range(1 << N):
        for i in range(N):
            y = flip(x, i)
            c[x][i] = Q * Fraction(weights[y], weights[x] + weights[y])
    return c


def deltas(c):
    ds = [[Fraction(0) for _ in range(N)] for _ in range(1 << N)]
    for x in range(1 << N):
        for i in range(N):
            val = c[x][i]
            for j in range(N):
                if i == j:
                    continue
                inc = c[flip(x, i)][j] - c[x][j]
                if inc > 0:
                    val -= inc
            ds[x][i] = val
    return ds


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def psd3(M):
    for i in range(3):
        if M[i][i] < 0:
            return False
    for i, j in combinations(range(3), 2):
        if M[i][i] * M[j][j] - M[i][j] * M[j][i] < 0:
            return False
    return det3(M) >= 0


def schur_after_hessian_minimization(c, x, delta):
    # Exact Schur complement of Gamma_2(f)(x)-2*delta*Gamma(f)(x)
    # in g_i = D_i f(x), after minimizing independently over
    # h_ij = D_i D_j f(x).  The derivation is written in the run report.
    M = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a = c[x][i]
        M[i][i] += a * (3 * Q - 2 * a) / 4
    for i, j in combinations(range(N), 2):
        a, b = c[x][i], c[x][j]
        A = c[flip(x, j)][i]
        B = c[flip(x, i)][j]
        X = b * (A - a)
        Y = a * (B - b)
        S = b * A + a * B
        K = (X - Y) * (X - Y) / S
        M[i][i] += (X - K) / 4
        M[j][j] += (Y - K) / 4
        off = (K - X - Y) / 4
        M[i][j] += off
        M[j][i] += off
    for i in range(N):
        M[i][i] -= delta * c[x][i]
    return M


def L_value(f, c, x):
    return sum(c[x][i] * (f[flip(x, i)] - f[x]) for i in range(N))


def gamma_value(f, c, x):
    return Fraction(1, 2) * sum(
        c[x][i] * (f[flip(x, i)] - f[x]) ** 2 for i in range(N)
    )


def gamma2_value(f, c, x):
    gam = [gamma_value(f, c, y) for y in range(1 << N)]
    Lgam = sum(c[x][i] * (gam[flip(x, i)] - gam[x]) for i in range(N))
    Lf = [L_value(f, c, y) for y in range(1 << N)]
    mixed = Fraction(1, 2) * sum(
        c[x][i]
        * (f[flip(x, i)] - f[x])
        * (Lf[flip(x, i)] - Lf[x])
        for i in range(N)
    )
    return Fraction(1, 2) * Lgam - mixed


tested = 0
eligible = 0
candidate_bad = None
for weights in product(range(1, 5), repeat=8):
    tested += 1
    c = rates(weights)
    ds = deltas(c)
    delta_star = min(min(row) for row in ds)
    if delta_star < 0:
        continue
    eligible += 1
    for x in range(8):
        if not psd3(schur_after_hessian_minimization(c, x, delta_star)):
            candidate_bad = (weights, delta_star, x)
            break
    if candidate_bad is not None:
        break

print(f"tested_total={tested}")
print(f"eligible_delta_nonnegative={eligible}")
print(f"candidate_counterexamples={0 if candidate_bad is None else 1}")
if candidate_bad is not None:
    print(f"FIRST_CANDIDATE_COUNTEREXAMPLE={candidate_bad}")
    raise SystemExit(1)

# Exact witness killing the tempting local-coordinate strengthening
# Gamma_2 >= sum_i c_i(x) delta_i(x) (D_i f(x))^2.
weights = (1, 1, 1, 1, 1, 1, 2, 2)
c = rates(weights)
ds = deltas(c)
delta_star = min(min(row) for row in ds)
x = 2
f = [
    Fraction(1), Fraction(1), Fraction(0), Fraction(0),
    Fraction(18, 17), Fraction(0), Fraction(0), Fraction(0)
]
g2 = gamma2_value(f, c, x)
local_rhs = sum(
    c[x][i] * ds[x][i] * (f[flip(x, i)] - f[x]) ** 2 for i in range(N)
)
global_rhs = delta_star * sum(
    c[x][i] * (f[flip(x, i)] - f[x]) ** 2 for i in range(N)
)
print(f"local_witness_weights={weights}")
print(f"local_witness_delta_star={delta_star}")
print(f"local_witness_state={x}")
print("local_witness_delta_at_state=" + ",".join(str(v) for v in ds[x]))
print("local_witness_f=" + ",".join(str(v) for v in f))
print(f"local_witness_Gamma2={g2}")
print(f"local_witness_local_rhs={local_rhs}")
print(f"local_witness_difference={g2-local_rhs}")
print(f"local_witness_global_rhs={global_rhs}")
print(f"local_witness_global_difference={g2-global_rhs}")
assert delta_star == Fraction(1, 9)
assert g2 - local_rhs == Fraction(-23, 1836)
assert g2 - global_rhs == Fraction(113, 1836)

print("PASS: exact n=3 box search found no failure of Gamma2 >= 2 delta_* Gamma")
print("PASS: exact witness refutes the stronger local-coordinate delta_i(x) replacement")
