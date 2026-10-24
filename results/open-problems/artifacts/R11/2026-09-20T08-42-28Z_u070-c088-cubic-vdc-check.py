#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial

checks = 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

# C088 exact near-cubic integer branch sequence:
# d_N = 1 + floor(log_2 N) = N.bit_length()
# b_N = floor(N^3 / d_N).
for N in range(2, 5001):
    d = N.bit_length()
    b = (N**3) // d
    ck(d == 1 + (N.bit_length()-1), f"d definition N={N}")
    ck(b >= 1, f"positive branch count N={N}")
    ck(Fraction(b, N**3) <= Fraction(1, d), f"near-cubic upper ratio N={N}")
    ck(Fraction(N**3, d) - 1 < b + 1, f"floor enclosure N={N}")
    if N >= 8:
        ck(b >= N*N, f"b_N already superquadratic at N={N}")

# N=4 exact active branch index.
# floor(21 log_4 3)=16 iff 4^16 <= 3^21 < 4^17.
N = 4
d4 = N.bit_length()
b4 = N**3 // d4
ck(d4 == 3, "d4")
ck(b4 == 21, "b4")
ck(4**16 <= 3**21 < 4**17, "exact log-floor certificate")
p3 = Fraction(3**21, 3**21 + 4**16)
ck(p3 == Fraction(10460353203, 14755320499), "p3 exact")

# Harmonic-grid rates at N=4.
ps = [Fraction(1,4), Fraction(1,2), p3]
lams = [Fraction(2,3), Fraction(1,2), Fraction(2,3)]

def q(i,j):
    return sum(
        (w * (x**i * (1-x)**j + x**j * (1-x)**i)
         for w,x in zip(lams, ps)),
        Fraction(0,1)
    )

q13 = q(1,3)
q22 = q(2,2)
D = 3033713490564534526429152960383315213952064
ck(q13 == Fraction(
    671719225794208878674503239067708227939609, D), "q13")
ck(q22 == Fraction(
    504051268651873282255855271645250407701495, D), "q22")
root = 4*q13 + 3*q22
ck(root == Fraction(
    4199030709132455361465578771206584134862921, D), "root rate")
pbal = 3*q22/root
ck(pbal == Fraction(
    504051268651873282255855271645250407701495,
    1399676903044151787155192923735528044954307), "balanced-root probability")

# Exact source CTCS(4) comparator from B(i,j).
def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

B13 = beta_int(1,3)
B22 = beta_int(2,2)
ck(B13 == Fraction(1,3), "B13")
ck(B22 == Fraction(1,6), "B22")
source_root = 4*B13 + 3*B22
source_pbal = 3*B22/source_root
ck(source_root == Fraction(11,6), "source root")
ck(source_pbal == Fraction(3,11), "source balanced")
diff_source = pbal-source_pbal
ck(diff_source == Fraction(
    1345533246038150743348829216891170349853524,
    15396445933485669658707122161090808494497377), "source difference")
ck(diff_source > 0, "source difference positive")
ck(q13/q22 != B13/B22, "scale-free split ratio differs")
ck(B13/B22 == 2, "source scale-free ratio")

# Distinguish from preceding C087 at the same N=4 invariant.
c087_pbal = Fraction(5387590087, 13835074771)
diff_087 = pbal-c087_pbal
ck(diff_087 == Fraction(
    -12070179098456533246249065760074943130593557184512,
    412013502316118244458837691081087896406601843052951), "C087 difference")
ck(diff_087 != 0, "C088 differs from C087")

# General exact finite sanity: beta split rates sum to H_{m-1}.
for m in range(2, 25):
    total = Fraction(0,1)
    # subsets containing label 1 index the unordered specified splits.
    for i in range(1,m):
        j=m-i
        total += comb(m-1,i-1)*beta_int(i,j)
    harmonic = sum((Fraction(1,r) for r in range(1,m)), Fraction(0,1))
    ck(total == harmonic, f"CTCS total rate m={m}")

# Exact color-probability normalization at the N=4 C088 proposal biases.
for x in ps:
    for m in range(2, 10):
        tot = sum((Fraction(comb(m,r),1) * x**r * (1-x)**(m-r)
                   for r in range(m+1)), Fraction(0,1))
        ck(tot == 1, f"binomial normalization p={x} m={m}")

print("R11 U070/C088 exact self-check")
print(f"ASSERTIONS={checks}")
print(f"b4={b4}")
print(f"p3={p3}")
print(f"q13={q13}")
print(f"q22={q22}")
print(f"root_rate={root}")
print(f"balanced_root={pbal}")
print(f"balanced_minus_CTCS={diff_source}")
print(f"balanced_minus_C087={diff_087}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
