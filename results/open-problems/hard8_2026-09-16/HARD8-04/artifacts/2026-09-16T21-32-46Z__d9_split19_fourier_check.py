from collections import Counter

P = 523
Q = 19
N = 9

# ---------- elementary modular arithmetic ----------
def order_mod(a, p):
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == 1:
            return k
    raise AssertionError('no order')

assert order_mod(19, P) == 9
assert order_mod(3, P) == 58
assert pow(3, 29, P) == P - 1

K = []
x = 1
for _ in range(9):
    K.append(x)
    x = x * 19 % P
assert x == 1 and len(set(K)) == 9
K = sorted(K)

# 58 multiplicative cosets C_j = 3^j K.
cosets = []
seen = set()
for j in range(58):
    C = sorted({pow(3, j, P) * k % P for k in K})
    assert len(C) == 9
    assert not (set(C) & seen)
    seen.update(C)
    cosets.append(C)
assert seen == set(range(1, P))
for j in range(58):
    assert {(-x) % P for x in cosets[j]} == set(cosets[(j + 29) % 58])

# ---------- polynomial arithmetic over F_19 ----------
# f(x)=x^9+17x^8+3x^7+3x^6+2x^5+12x^4+4x^3+10x+6
MOD = [6, 10, 0, 4, 12, 2, 3, 3, 17, 1]  # low -> high
assert len(MOD) == 10 and MOD[-1] == 1

def trim(a):
    a = [x % Q for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def padd(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % Q
    return trim(out)

def psub(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % Q
    return trim(out)

def pmul_raw(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % Q
    return trim(out)

def pdivmod(a, b):
    a = trim(a[:])
    b = trim(b[:])
    assert b != [0]
    if len(a) < len(b):
        return [0], a
    inv = pow(b[-1], -1, Q)
    q = [0] * (len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] * inv % Q
        q[d] = c
        for i, bi in enumerate(b):
            a[i + d] = (a[i + d] - c * bi) % Q
        a = trim(a)
    return trim(q), a

def pmod(a, m=MOD):
    return pdivmod(a, m)[1]

def pmul(a, b):
    return pmod(pmul_raw(a, b))

def ppow(a, e):
    r = [1]
    b = pmod(a)
    while e:
        if e & 1:
            r = pmul(r, b)
        b = pmul(b, b)
        e //= 2
    return r

def pgcd(a, b):
    a = trim(a)
    b = trim(b)
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    inv = pow(a[-1], -1, Q)
    return trim([(inv * x) % Q for x in a])

# Rabin irreducibility check for degree 9. The only prime divisor of 9 is 3.
X = [0, 1]
assert ppow(X, Q ** N) == X
assert pgcd(psub(ppow(X, Q ** 3), X), MOD) == [1]

# ---------- F_(19^9) arithmetic ----------
ZERO = (0,) * N
ONE = (1,) + (0,) * (N - 1)
ALPHA = (0, 1) + (0,) * (N - 2)

def fadd(a, b):
    return tuple((a[i] + b[i]) % Q for i in range(N))

def fmul(a, b):
    conv = [0] * (2 * N - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            conv[i + j] = (conv[i + j] + x * y) % Q
    for d in range(2 * N - 2, N - 1, -1):
        c = conv[d] % Q
        if c:
            # x^9 = -(f_0+...+f_8 x^8)
            for k in range(N):
                conv[d - N + k] = (conv[d - N + k] - c * MOD[k]) % Q
    return tuple(x % Q for x in conv[:N])

def fpow(a, e):
    r = ONE
    b = a
    while e:
        if e & 1:
            r = fmul(r, b)
        b = fmul(b, b)
        e //= 2
    return r

zeta = fpow(ALPHA, (Q ** N - 1) // P)
assert zeta != ONE and fpow(zeta, P) == ONE
# P is prime, so a nontrivial P-th root has exact order P.

# Gauss periods eta_j = sum_{x in C_j} zeta^x. Frobenius-19 fixes each.
etas = []
for C in cosets:
    s = ZERO
    for a in C:
        s = fadd(s, fpow(zeta, a))
    assert fpow(s, Q) == s
    assert all(v == 0 for v in s[1:])
    etas.append(s[0])
assert sum(etas) % Q == Q - 1  # sum over all nonzero p-th roots is -1

# Full rank of the period convolution map on the K-invariant subspace.
M = [[etas[(i + j) % 58] for j in range(58)] for i in range(58)]

def rank_mod(A, p):
    A = [row[:] for row in A]
    r = 0
    n = len(A)
    m = len(A[0])
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] % p), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c] % p, -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] % p:
                f = A[i][c] % p
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(m)]
        r += 1
        if r == n:
            break
    return r

assert rank_mod(M, Q) == 58

# ---------- current product-T candidate from the previous exact report ----------
H4 = ((1, 1, 1, 1), (1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1))
labels = [7,3,2,7,6,3,1,6,1,7,3,6,2,5,4,3,7,0,6,6,6,7,2,7,6,1,7,2,6,7,0,6,6,6,7,4,3,7,6,6,0,6,5,5,4,7,6,7,7,0,2,7,0,2,6,7,4,7]
assert len(labels) == 58
q = [0] * P
for j, C in enumerate(cosets):
    for x in C:
        q[x] = labels[j]
# q(0)=+e0 by default.

# Four transformed sign sequences and their negative sets.
neg = []
rows = []
for r in range(4):
    bits = []
    s = 0
    for x in range(P):
        lab = q[x]
        comp = lab // 2
        sg = 1 if lab % 2 == 0 else -1
        val = sg * H4[r][comp]
        s += val
        bits.append(1 if val < 0 else 0)
    neg.append(bits)
    rows.append(s)
assert tuple(rows) == (37, 19, 19, 1)  # H4 transform of T row sums (19,9,9,0)
assert tuple(sum(b) for b in neg) == (243, 252, 252, 261)
assert all(neg[r][0] == 0 for r in range(4))
assert all(neg[3][x] == (neg[0][x] ^ neg[1][x] ^ neg[2][x]) for x in range(P))

orb_bits = []
for r in range(4):
    b = []
    for C in cosets:
        vals = {neg[r][x] for x in C}
        assert len(vals) == 1
        b.append(next(iter(vals)))
    orb_bits.append(b)
assert tuple(sum(b) for b in orb_bits) == (27, 28, 28, 29)

def fhat_bits(bits, c, zero_bit=0):
    return (zero_bit + sum(bits[j] * etas[(c + j) % 58] for j in range(58))) % Q

def t_corr(s):
    total = 0
    for x in range(P):
        a = q[x]
        b = q[(x + s) % P]
        if a // 2 == b // 2:
            total += 1 if (a % 2) == (b % 2) else -1
    return total

C_orb = [t_corr(C[0]) for C in cosets]
assert all(t_corr(s) == C_orb[j] for j, C in enumerate(cosets) for s in C)
assert all(C_orb[j] == C_orb[(j + 29) % 58] for j in range(58))

# Split-prime Fourier identity. For every frequency coset c,
# sum_i Xhat_i(t)Xhat_i(-t) = p + sum_{s!=0} C_T(s) zeta^(ts), modulo 19.
# A true periodic-T witness therefore satisfies 29 paired equations LHS == p == 10 mod 19.
L = []
for c in range(58):
    lhs = 0
    for r in range(4):
        a = fhat_bits(orb_bits[r], c)
        b = fhat_bits(orb_bits[r], (c + 29) % 58)
        lhs = (lhs + a * b) % Q
    rhs = (P % Q + sum(C_orb[j] * etas[(c + j) % 58] for j in range(58))) % Q
    assert lhs == rhs
    L.append(lhs)
assert all(L[c] == L[(c + 29) % 58] for c in range(29))
assert any(v != P % Q for v in L[:29])  # retained candidate is not a solution

# ---------- B21: second surviving d=9 GS row-sum profile ----------
# Positive row sums (17,17,17,35) force zero to be negative in this K-invariant normalization.
row2 = (17, 17, 17, 35)
k2 = tuple((P - r) // 2 for r in row2)
assert k2 == (253, 253, 253, 244)
assert tuple((k - 1) // 9 for k in k2) == (28, 28, 28, 27)
lambda2 = sum(k2) - P
assert lambda2 == 480
# Equivalent global sign flips make zero positive and row sums negative.
row2_flip = tuple(-r for r in row2)
k2_flip = tuple((P - r) // 2 for r in row2_flip)
assert k2_flip == (270, 270, 270, 279)
assert tuple(k // 9 for k in k2_flip) == (30, 30, 30, 31)
assert sum(k2_flip) - P == 566

print('P', P)
print('ord_523(19)', order_mod(19, P), 'ord_523(3)', order_mod(3, P), '3^29_mod_523', pow(3, 29, P))
print('K_generator_19', K)
print('coset_count', len(cosets), 'negation_shift', 29)
print('field_modulus_low_to_high', MOD)
print('zeta_order', P)
print('periods_F19', etas)
print('period_transform_rank', rank_mod(M, Q))
print('product_profile_rowsums', tuple(rows), 'orbit_weights', tuple(sum(b) for b in orb_bits))
print('product_candidate_split19_blocks', L[:29])
print('product_candidate_split19_target', P % Q, 'is_solution_mod19', all(v == P % Q for v in L[:29]))
print('second_GS_profile_rowsums', row2, 'negative_sizes', k2, 'orbit_counts_after_fixed_zero', tuple((k - 1) // 9 for k in k2), 'lambda', lambda2)
print('second_GS_profile_zero_positive_equiv_rowsums', row2_flip, 'negative_sizes', k2_flip, 'orbit_counts', tuple(k // 9 for k in k2_flip), 'lambda', sum(k2_flip) - P)
print('THEOREM_CHECK: K=<19> has order 9 and all K-invariant Fourier values at 523rd roots lie in F19')
print('THEOREM_CHECK: 29 exact split-prime Fourier blocks are necessary for d=9 GS/product-T witnesses')
print('ALL_EXACT_SPLIT19_FOURIER_CHECKS_PASSED')
