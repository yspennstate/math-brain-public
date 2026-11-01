from fractions import Fraction
from math import factorial

ASSERTIONS = 0

def ok(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def floor_log2(n):
    return n.bit_length() - 1

def bcrit(n):
    return 1 << floor_log2(n)

def b_c086(n):
    return 1 << max(1, floor_log2(n)//2)

def tau_exact(N, s, b):
    x = Fraction(s, N)
    odds = Fraction(s, N-s)
    if odds < 1 or odds >= 4:
        return x
    z = odds ** b
    q = 0
    while z >= 4:
        z /= 4
        q += 1
    ok(Fraction(1,1) <= z < Fraction(4,1), "reduced odds not in [1,4)")
    return z / (1 + z)

def biases(N, b):
    return [tau_exact(N,s,b) for s in range(1,N)]

def split_rate(N, ps, i, j):
    ans = Fraction(0)
    for s,p in enumerate(ps, start=1):
        lam = Fraction(N, 2*s*(N-s))
        ans += lam * (p**i * (1-p)**j + p**j * (1-p)**i)
    return ans

def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def harmonic(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

# 1. Critical branch-count sequence: exact dyadic linear scale.
for N in range(2, 5001):
    b = bcrit(N)
    ok(b <= N)
    ok(2*b > N)
    ok(b*b < N*N + 1)

# 2. Exact CTCS beta-rate combinatorics and total clade rate.
for m in range(2, 13):
    total = Fraction(0)
    for mask in range(0, 1 << (m-1)):
        A = {0}
        for t in range(1,m):
            if (mask >> (t-1)) & 1:
                A.add(t)
        if len(A)==m:
            continue
        i,j = len(A), m-len(A)
        total += beta_int(i,j)
    ok(total == harmonic(m-1), f"CTCS total-rate identity failed at m={m}")

# 3. Exact measure-preservation finite core for T_b(z)={bz}.
for b in [1,2,4,8,16,32,64,128]:
    for q in range(2, 31):
        for a in range(q):
            for c in range(a+1, q+1):
                target = Fraction(c-a, q)
                pre = sum((Fraction(c-a, b*q) for _ in range(b)), Fraction(0))
                ok(pre == target)

# 4. Exact rational harmonic-grid biases and positivity on small instances.
for N in range(2, 41):
    b = bcrit(N)
    ps = biases(N,b)
    ok(len(ps)==N-1)
    for p in ps:
        ok(Fraction(0) < p < Fraction(1))
    for i in range(1,5):
        for j in range(1,5):
            qij = split_rate(N,ps,i,j)
            qji = split_rate(N,ps,j,i)
            ok(qij == qji)
            ok(qij > 0)

# 5. Exact N=4 C087 witness.
N = 4
b = bcrit(N)
ps = biases(N,b)
ok(b == 4)
ok(ps == [Fraction(1,4), Fraction(1,2), Fraction(81,145)])
q11 = split_rate(N, ps, 1, 1)
q13 = split_rate(N, ps, 1, 3)
q22 = split_rate(N, ps, 2, 2)
root = 4*q13 + 3*q22
pbal = 3*q22/root
ratio = q13/q22
ok(q11 == Fraction(34849,42050))
ok(q13 == Fraction(6335613513,28291240000))
ok(q22 == Fraction(5387590087,28291240000))
ok(root == Fraction(41505224313,28291240000))
ok(pbal == Fraction(5387590087,13835074771))
ok(ratio == Fraction(6335613513,5387590087))
ok(pbal != Fraction(3,11))
ok(ratio != Fraction(2,1))
ok(pbal - Fraction(3,11) == Fraction(17758266644,152185822481))

# 6. Exact separation from C086 at the same N=4.
b86 = b_c086(N)
ps86 = biases(N,b86)
q13_86 = split_rate(N,ps86,1,3)
q22_86 = split_rate(N,ps86,2,2)
pbal86 = 3*q22_86/(4*q13_86+3*q22_86)
ok(b86 == 2)
ok(ps86 == [Fraction(1,4), Fraction(1,2), Fraction(9,13)])
ok(q13_86 == Fraction(406041,1827904))
ok(q22_86 == Fraction(310519,1827904))
ok(pbal86 == Fraction(310519,851907))
ok(pbal != pbal86)
ok(pbal - pbal86 == Fraction(5993308682240,240534633529353))

print("R11-I0054-U069/C087 exact self-check")
print(f"ASSERTIONS={ASSERTIONS}")
print(f"N4_bcrit={b}")
print("N4_biases=" + ",".join(str(x) for x in ps))
print(f"N4_q11={q11}")
print(f"N4_q13={q13}")
print(f"N4_q22={q22}")
print(f"N4_root_total={root}")
print(f"N4_balanced_root_probability={pbal}")
print(f"N4_source_CTCS_balanced_root_probability={Fraction(3,11)}")
print(f"N4_C086_balanced_root_probability={pbal86}")
print(f"N4_rate_ratio_q13_over_q22={ratio}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
