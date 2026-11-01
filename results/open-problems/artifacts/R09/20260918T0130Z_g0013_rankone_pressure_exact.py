from fractions import Fraction as Q

# Exact rational self-check for the R09 / G0013 rank-one-pressure report.
# This certifies only the displayed rational consequences of the analytic
# inequalities proved in the accompanying immutable report. It is not an
# independent audit of the theorem-sized argument.

U = Q(1289727882057511, 11918000000000000)

def S_cap(k):
    return k / (3 * (2 + k))

threshold = Q(6, 7)
assert S_cap(threshold) == Q(1, 10)

# Formal complementary-level slope-product bounds inherited from the
# preceding R09 self-check.
Kmid = Q(82944, 130321)
Ktail = Q(180, 361)
assert Kmid < threshold and Ktail < threshold
assert S_cap(Kmid) == Q(13824, 171793)
assert S_cap(Ktail) == Q(30, 451)

# If a smooth Brenier candidate had S=U, the weighted average rank-one ratio
# required by the new inequality is alpha=2S/(1/3-S).  Any [0,1]-valued
# kappa with mean at least alpha has mass at least 7*alpha-6 above 6/7.
alpha = 2 * U / (Q(1, 3) - U)
mass = 7 * alpha - 6
assert alpha == Q(7738367292345066, 8048816353827467)
assert mass == Q(5875672923450660, 8048816353827467)
assert alpha > threshold and 0 < mass < 1

print('R09 G0013 RANK-ONE PRESSURE EXACT SELF-CHECK')
print('U_star =', U, '= %.17f' % float(U))
print('K_threshold =', threshold, 'S_cap(K_threshold) =', S_cap(threshold))
print('anti_pair_K_mid =', Kmid, '= %.15f' % float(Kmid))
print('S_cap(anti_pair_K_mid) =', S_cap(Kmid), '= %.15f' % float(S_cap(Kmid)))
print('anti_pair_K_tail =', Ktail, '= %.15f' % float(Ktail))
print('S_cap(anti_pair_K_tail) =', S_cap(Ktail), '= %.15f' % float(S_cap(Ktail)))
print('required_weighted_kappa_at_U =', alpha, '= %.15f' % float(alpha))
print('min_weight_above_6/7_at_U =', mass, '= %.15f' % float(mass))
print('SELF_CHECK_ONLY / PASS')
