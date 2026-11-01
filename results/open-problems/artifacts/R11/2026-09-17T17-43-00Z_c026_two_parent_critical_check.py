from fractions import Fraction
from itertools import product
from math import isqrt

checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def rising(a, k):
    r = Fraction(1)
    for j in range(k):
        r *= a + j
    return r

def falling(n, k):
    r = 1
    for j in range(k):
        r *= n - j
    return r

def sqrt_ceil(n):
    m = isqrt(n)
    return m if m*m == n else m + 1

def nu_config(N, alpha, x):
    s = sum(x)
    return rising(alpha, s) * rising(alpha, N-s) / rising(2*alpha, N)

def support_prob(N, x, i, j):
    s = sum(x)
    return Fraction(
        falling(s, i)*falling(N-s, j) + falling(s, j)*falling(N-s, i),
        falling(N, i+j)
    )

def split2_prob(N, x):
    return support_prob(N, x, 1, 1)

def ordinary_fixed_v_transition_prob(N, mu, v, x, y):
    # C023 comparison kernel: one victim v is fixed, and the locus parent
    # is uniform on all N population sites.
    if any(y[q] != x[q] for q in range(N) if q != v):
        return Fraction(0)
    ans = Fraction(0)
    for p in range(N):
        copied = x[p]
        ans += Fraction(1, N) * ((1-mu) if y[v] == copied else mu)
    return ans

def twoparent_fixed_v_marginal_prob(N, mu, v, x, y):
    # C026 one-locus marginal: choose A,B iid uniform on [N], then choose
    # one of the two parents with a fair independent locus coin.
    if any(y[q] != x[q] for q in range(N) if q != v):
        return Fraction(0)
    ans = Fraction(0)
    for A in range(N):
        for B in range(N):
            for coin in (0,1):
                p = A if coin == 0 else B
                copied = x[p]
                ans += Fraction(1, 2*N*N) * ((1-mu) if y[v] == copied else mu)
    return ans

# ----------------------------------------------------------------------
# 1. One-locus exact marginal identity, stationarity, heterozygosity.
# ----------------------------------------------------------------------
for N in range(2, 7):
    m = sqrt_ceil(N)
    alpha = Fraction(1, m)
    mu = alpha / (N + 2*alpha)
    states = list(product([0,1], repeat=N))
    nu = {x: nu_config(N, alpha, x) for x in states}
    ck(sum(nu.values()) == 1, f"nu normalization N={N}")

    # Full transition comparison is already plenty through N=5.
    if N <= 5:
        for v in range(N):
            out = {y: Fraction(0) for y in states}
            for x in states:
                row = Fraction(0)
                for y in states:
                    p0 = ordinary_fixed_v_transition_prob(N, mu, v, x, y)
                    p2 = twoparent_fixed_v_marginal_prob(N, mu, v, x, y)
                    ck(p0 == p2, f"one-locus marginal identity N={N},v={v},x={x},y={y}")
                    row += p2
                    if p2:
                        out[y] += nu[x]*p2
                ck(row == 1, f"two-parent marginal row sum N={N},v={v},x={x}")
            for y in states:
                ck(out[y] == nu[y], f"two-parent marginal invariance N={N},v={v},y={y}")

    # For two distinct uniformly sampled sites, stationary disagreement is
    # alpha/(2 alpha + 1).
    h = sum(
        pr * Fraction(2*sum(x)*(N-sum(x)), N*(N-1))
        for x, pr in nu.items()
    )
    ck(h == alpha/(2*alpha+1), f"heterozygosity N={N}")

# ----------------------------------------------------------------------
# 2. Exact N=4 finite tree-visible witness.
# ----------------------------------------------------------------------
N = 4
m = sqrt_ceil(N)
alpha = Fraction(1, m)
Delta = alpha
L = N*N
mu = alpha / (N + 2*alpha)
ck(alpha == Fraction(1,2), "N4 alpha")
ck(Delta == Fraction(1,2), "N4 Delta")
ck(L == 16, "N4 loci")
ck(mu == Fraction(1,10), "N4 mu")

states = list(product([0,1], repeat=N))
nu = {x: nu_config(N, alpha, x) for x in states}
p2 = sum(pr*split2_prob(N,x) for x,pr in nu.items())
eg2 = sum(pr*split2_prob(N,x)**2 for x,pr in nu.items())
ck(p2 == Fraction(1,4), "N4 one size-2 block split probability")
ck(eg2 == Fraction(9,64), "N4 same-locus two-query second moment")

# Two distinct loci after one shared two-parent update.
# A,B are common across the genome; each locus independently chooses A or B;
# mutation bits are independent. We average the two size-2 split indicators
# exactly, including the random victim.
joint_distinct = Fraction(0)
for x1, pr1 in nu.items():
    for x2, pr2 in nu.items():
        for v in range(N):
            for A in range(N):
                for B in range(N):
                    for c1 in (0,1):
                        r1 = A if c1 == 0 else B
                        for c2 in (0,1):
                            r2 = A if c2 == 0 else B
                            e1 = Fraction(0)
                            e2 = Fraction(0)
                            for flip, q in ((0,1-mu),(1,mu)):
                                y1 = list(x1)
                                y1[v] = x1[r1] ^ flip
                                e1 += q * split2_prob(N, tuple(y1))
                                y2 = list(x2)
                                y2[v] = x2[r2] ^ flip
                                e2 += q * split2_prob(N, tuple(y2))
                            joint_distinct += (
                                pr1*pr2
                                * Fraction(1, N**3)
                                * Fraction(1,4)
                                * e1*e2
                            )

ck(joint_distinct == Fraction(601,9600), "N4 distinct-locus joint split probability")
cov_distinct = joint_distinct - p2*p2
ck(cov_distinct == Fraction(1,9600), "N4 distinct-locus covariance")

# Two current size-2 tree blocks hash independently into L=16 loci.
# If they collide, both models use the same marginal locus, contributing E[g^2].
# If they choose distinct loci, C023 contributes p2^2 and C026 contributes
# joint_distinct. Thus this is a tree-visible transition-kernel witness.
joint_C023 = Fraction(1,L)*eg2 + Fraction(L-1,L)*p2*p2
joint_C026 = Fraction(1,L)*eg2 + Fraction(L-1,L)*joint_distinct
ck(joint_C023 == Fraction(69,1024), "N4 C023 two-block joint split probability")
ck(joint_C026 == Fraction(691,10240), "N4 C026 two-block joint split probability")
ck(joint_C026-joint_C023 == Fraction(1,10240), "N4 C026-C023 joint difference")

# The one-block root-shape ratio is 5/3, so the only retained binary collision
# is C023; the two-block statistic above separates that collision.
p13 = sum(pr*support_prob(N,x,1,3) for x,pr in nu.items())
p22 = sum(pr*support_prob(N,x,2,2) for x,pr in nu.items())
root_ratio = p13/p22
ck(p13 == Fraction(5,64), "N4 p13")
ck(p22 == Fraction(3,64), "N4 p22")
ck(root_ratio == Fraction(5,3), "N4 root ratio")

previous_binary = {
    "original_CTCS_finite": Fraction(2,1),
    "C001": Fraction(7,5),
    "C009": Fraction(2699,1365),
    "C010": Fraction(2273,1153),
    "C020": Fraction(61381,43765),
    "C021": Fraction(166094447739,85563797248),
    "C022": Fraction(33,17),
    "C023": Fraction(5,3),
    "C024": Fraction(597,359),
    "C025": Fraction(18,11),
}
for name, q in previous_binary.items():
    if name == "C023":
        ck(root_ratio == q, "intended C023 root collision")
    else:
        ck(root_ratio != q, f"root ratio collision with {name}")

# ----------------------------------------------------------------------
# 3. Parent-sharing invariant and critical scaling.
# ----------------------------------------------------------------------
for N in range(2, 201):
    # A,B iid uniform; each of two loci chooses A/B by independent fair coins.
    # Same chosen parent probability = 1 if A=B and 1/2 otherwise.
    psame = Fraction(1,N) + (1-Fraction(1,N))*Fraction(1,2)
    ck(psame == Fraction(N+1,2*N), f"two-parent parent-sharing N={N}")
    ck(psame - Fraction(1,N) == Fraction(N-1,2*N), f"parent excess N={N}")

# Exact perfect-square subsequence N=n^2.  C026 uses Delta=alpha=1/n and
# L=N^2=n^4.  The fresh-locus birthday scale L*Delta^2=n^2 -> infinity.
# The refined discrepancy theorem U010 uses eta <= alpha and yields
# path error <= k*eta*M(M+1)/(2N); at T=1,k=1,M=n this is O(1/n).
for n in range(2, 201):
    NN = n*n
    mm = sqrt_ceil(NN)
    D = Fraction(1,mm)
    LL = NN*NN
    eta = Fraction(NN-1,NN) * D/(2*D+1)
    M = n
    path_bound = eta * Fraction(M*(M+1), 2*NN)
    ck(mm == n, f"sqrt exact n={n}")
    ck(NN*D == n, f"NDelta=n n={n}")
    ck(LL*D*D == NN, f"LDelta2=N n={n}")
    ck(eta <= D, f"eta<=Delta n={n}")
    ck(path_bound <= Fraction(n+1,2*n*n), f"critical path bound n={n}")
    ck(path_bound <= Fraction(1,n), f"critical path bound <=1/n n={n}")

print("R11 C026 exact self-check")
print(f"checks={checks}")
print(f"N4 alpha={alpha} Delta={Delta} L={L} mu={mu}")
print(f"N4 root p13={p13} p22={p22} ratio={root_ratio}")
print(f"N4 distinct-locus size2 joint={joint_distinct} covariance={cov_distinct}")
print(f"N4 C023 two-block joint={joint_C023}")
print(f"N4 C026 two-block joint={joint_C026}")
print(f"N4 tree-visible C026-C023 difference={joint_C026-joint_C023}")
print("two-parent parent-sharing probability=(N+1)/(2N)")
print("U010 discrepancy source eta=((N-1)/N)*alpha/(2alpha+1) <= alpha")
print("critical scales: Delta=alpha=1/ceil(sqrt(N)), L=N^2")
print("on N=n^2: N*Delta=n and L*Delta^2=N")
print("ALL_EXACT_CHECKS_PASS")
