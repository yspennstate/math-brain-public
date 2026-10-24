from fractions import Fraction
from itertools import product, permutations
from math import factorial

ASSERTIONS = 0

def chk(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def ff(x, r):
    v = 1
    for j in range(r):
        v *= x-j
    return v

def beta(i, j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def env_weights(N, signs):
    # One iid Rademacher sign for each reflected arc-length pair;
    # when N is even the central length N/2 gets its own sign.
    m = N//2
    chk(len(signs) == m, (N, signs))
    w = {}
    for s in range(1, N):
        r = min(s, N-s)
        w[s] = Fraction(1, 1) + Fraction(signs[r-1], 2)
        chk(w[s] in (Fraction(1,2), Fraction(3,2)))
        chk(w[s] > 0)
    for s in range(1, N):
        chk(w[s] == w[N-s])
    return w

def proposal_rate(N, s, w):
    return Fraction(N, 2*s*(N-s))*w[s]

def split_rate_formula(N, i, j, w):
    k = i+j
    chk(k <= N)
    out = Fraction(0, 1)
    for s in range(1, N):
        out += w[s]*ff(s-1, i-1)*ff(N-s-1, j-1)
    return Fraction(N, ff(N, k))*out

def split_prob_direct_type(N, k, i, s):
    A = set(range(i))
    Ac = set(range(k)) - A
    count = 0
    total = 0
    for inj in permutations(range(N), k):
        for start in range(N):
            arc = {(start+t) % N for t in range(s)}
            inside = {lab for lab, pos in enumerate(inj) if pos in arc}
            total += 1
            if inside == A or inside == Ac:
                count += 1
    chk(total == ff(N, k)*N)
    return Fraction(count, total)

def split_rate_direct(N, i, j, w):
    k = i+j
    total = Fraction(0,1)
    for s in range(1,N):
        p = split_prob_direct_type(N,k,i,s)
        total += proposal_rate(N,s,w)*p
    return total

def max_prefix(signs):
    z = 0
    m = 0
    for e in signs:
        z += e
        m = max(m, abs(z))
    return m

def weighted_cdf_discrepancy_grid(N, signs):
    w = env_weights(N, signs)
    # Supremum against x occurs at a grid point or immediately to its left.
    # Check the complete finite set exactly.
    best = Fraction(0,1)
    mass = Fraction(0,1)
    for r in range(0,N):
        if r > 0:
            mass += Fraction(w[r], N)
        x = Fraction(r,N)
        best = max(best, abs(mass-x))
        if r < N-1:
            xnext = Fraction(r+1,N)
            best = max(best, abs(mass-xnext))
    best = max(best, abs(mass-Fraction(1,1)))
    return best

# 1. Symmetry/positivity and exact direct-vs-closed-form rates.
# Exhaust all environments through N=7 and all fixed splits up to k=4.
for N in range(3, 8):
    for signs in product((-1,1), repeat=N//2):
        w = env_weights(N, signs)
        for k in range(2, min(4,N)+1):
            for i in range(1,k):
                j = k-i
                q1 = split_rate_formula(N,i,j,w)
                q2 = split_rate_direct(N,i,j,w)
                chk(q1 == q2, (N, signs, i, j, q1, q2))
                chk(q1 == split_rate_formula(N,j,i,w))

# 2. Annealed first-order generator is exactly CTCS at every finite N.
# This is a nontrivial feature of the quenched construction: E[Q_env]=Q_CTCS,
# while the annealed path law is not Markov at finite N.
for N in range(3, 11):
    envs = list(product((-1,1), repeat=N//2))
    for k in range(2, min(7,N)+1):
        for i in range(1,k):
            j = k-i
            avg = sum(split_rate_formula(N,i,j,env_weights(N,sg)) for sg in envs) / len(envs)
            chk(avg == beta(i,j), (N,i,j,avg,beta(i,j)))

# 3. Exact star-discrepancy deterministic domination used in the proof.
# D_N^* <= 1/N + (3/(2N)) max_prefix for the reflected sign sequence.
for N in range(3, 15):
    for signs in product((-1,1), repeat=N//2):
        D = weighted_cdf_discrepancy_grid(N, signs)
        M = max_prefix(signs)
        bound = Fraction(1,N) + Fraction(3*M,2*N)
        chk(D <= bound, (N, signs, D, bound))

# 4. Exact N=4 topology witness.
N = 4
root = []
for signs in product((-1,1), repeat=2):
    w = env_weights(N, signs)
    q13 = split_rate_formula(N,1,3,w)
    q22 = split_rate_formula(N,2,2,w)
    # Four unordered 1|3 partitions, three unordered 2|2 partitions.
    pbal = 3*q22/(4*q13+3*q22)
    root.append((signs, q13, q22, pbal))

expected = {
    (-1,-1): (Fraction(1,6), Fraction(1,12), Fraction(3,11)),
    (-1, 1): (Fraction(1,6), Fraction(1,4),  Fraction(9,17)),
    ( 1,-1): (Fraction(1,2), Fraction(1,12), Fraction(1,9)),
    ( 1, 1): (Fraction(1,2), Fraction(1,4),  Fraction(3,11)),
}
for signs, q13, q22, pbal in root:
    chk((q13,q22,pbal) == expected[signs], (signs,q13,q22,pbal))

annealed_bal = sum(x[3] for x in root)/4
source_bal = Fraction(3,11)
chk(annealed_bal == Fraction(499,1683), annealed_bal)
chk(annealed_bal - source_bal == Fraction(40,1683))
chk(annealed_bal != source_bal)

# 5. Demonstrate the hidden-environment effect algebraically:
# both same-sign environments are mere time rescalings of baseline at the root,
# but the opposite-sign environments change topology and the mixture is not baseline.
chk(root[0][3] == source_bal)
chk(root[3][3] == source_bal)
chk(root[1][3] == Fraction(9,17))
chk(root[2][3] == Fraction(1,9))

print(f"ASSERTIONS={ASSERTIONS}")
print("N4_CONDITIONAL_ROOT_BALANCED=" + ";".join(f"{sg}:{p}" for sg,_,_,p in root))
print(f"N4_ANNEALED_ROOT_BALANCED={annealed_bal}")
print(f"SOURCE_DTCS4_ROOT_BALANCED={source_bal}")
print(f"EXACT_GAP={annealed_bal-source_bal}")
print("ANNEALED_FIRST_ORDER_GENERATOR=EXACT_CTCS_FOR_TESTED_N")
print("ALL_EXACT_CHECKS_PASS")
