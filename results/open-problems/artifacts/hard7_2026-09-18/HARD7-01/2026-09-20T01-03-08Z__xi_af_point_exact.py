from fractions import Fraction as Q

# Exact diagnostic for the Xi 2026 generalized-radii route on an aligned-box
# equality case. This does NOT test Xi's conjecture; it tests only the naive
# choice of the canonical Alexandrov-Fenchel point in B_3(K,L).
# Ratios b_i/a_i; product 1 gives equal volumes.
r = (Q(4), Q(2), Q(1, 8))
assert r[0] * r[1] * r[2] == 1
A = sum(r, Q(0))
B = sum((1 / x for x in r), Q(0))
t1 = Q(3, 1) / A
t2 = A / B
assert (A, B, t1, t2) == (Q(49, 8), Q(35, 4), Q(24, 49), Q(7, 10))

# For c_i=(sqrt(r_i)+1/sqrt(r_i))/2:
# c1=5/4, c2=3 sqrt(2)/4, c3=9 sqrt(2)/8.
# Hence S=sum c_i and C=prod c_i exactly.
S_rat = Q(5, 4)
S_sqrt2_coeff = Q(15, 8)
C = Q(135, 64)
assert S_rat == Q(5, 4)
assert S_sqrt2_coeff == Q(15, 8)
assert C == Q(135, 64)

# lambda(t)=(sqrt(t)+1/sqrt(t))/2 at the canonical point:
# lambda1=73 sqrt(6)/168, lambda2=17 sqrt(70)/140.
# These coefficients follow directly from t1=24/49 and t2=7/10.
lambda1_sqrt6_coeff = Q(73, 168)
lambda2_sqrt70_coeff = Q(17, 140)
assert lambda1_sqrt6_coeff == Q(1, 2) * (Q(2, 7) + Q(7, 12))
assert lambda2_sqrt70_coeff == Q(1, 2) * (Q(1, 10) + Q(1, 7))

# lambda1*lambda2=(1241/11760)*sqrt(105), so
# C/(lambda1*lambda2)=(945/4964)*sqrt(105).
recip_term_sqrt105_coeff = Q(945, 4964)
assert recip_term_sqrt105_coeff == C * Q(11760, 1241) / Q(105, 1)

# Therefore
# D := [lambda1+lambda2+C/(lambda1 lambda2)] - S
#    = -5/4 + (-1954575 sqrt2 + 126582 sqrt70
#              +452965 sqrt6 +198450 sqrt105)/1042440.
# Xi's lower inequality (3.4) on this equality-case box would require D<=0.
common_den = Q(1042440, 1)
assert -S_sqrt2_coeff == Q(-1954575, 1042440)
assert lambda2_sqrt70_coeff == Q(126582, 1042440)
assert lambda1_sqrt6_coeff == Q(452965, 1042440)
assert recip_term_sqrt105_coeff == Q(198450, 1042440)

# Prove D>0 using exact rational brackets for the radicals.
ub_sqrt2 = Q(141422, 100000)     # > sqrt(2)
lb_sqrt6 = Q(244948, 100000)     # < sqrt(6)
lb_sqrt70 = Q(836660, 100000)    # < sqrt(70)
lb_sqrt105 = Q(1024695, 100000)  # < sqrt(105)

assert ub_sqrt2 * ub_sqrt2 > 2
assert lb_sqrt6 * lb_sqrt6 < 6
assert lb_sqrt70 * lb_sqrt70 < 70
assert lb_sqrt105 * lb_sqrt105 < 105

D_lower = -Q(5, 4) + (
    -Q(1954575) * ub_sqrt2
    + Q(126582) * lb_sqrt70
    + Q(452965) * lb_sqrt6
    + Q(198450) * lb_sqrt105
) / common_den

assert D_lower == Q(48159943, 372300000)
assert D_lower > 0

print("r =", r)
print("A =", A, "B =", B)
print("canonical t1 =", t1, "t2 =", t2)
print("S = 5/4 + (15/8)*sqrt(2)")
print("C =", C)
print("lambda1 = (73/168)*sqrt(6)")
print("lambda2 = (17/140)*sqrt(70)")
print("D exact radical form = -5/4 + (-1954575*sqrt(2) + 126582*sqrt(70) + 452965*sqrt(6) + 198450*sqrt(105))/1042440")
print("Certified rational lower bound for D =", D_lower)
print("D_lower decimal = %.15f" % float(D_lower))
print("CONCLUSION: D > 0 exactly, so the canonical AF point fails Xi inequality (3.4) on this equality-case aligned-box pair.")
print("SCOPE: this is NOT a counterexample to Xi's conjecture, which permits a different point of B_3(K,L).")
print("ALL_EXACT_CHECKS_PASS = True")
