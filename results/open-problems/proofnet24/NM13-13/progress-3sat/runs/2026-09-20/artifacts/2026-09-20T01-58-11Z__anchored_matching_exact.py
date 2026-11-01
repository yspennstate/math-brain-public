from itertools import combinations, product
from fractions import Fraction
from math import comb


def lit_val(var, sign, assign):
    v = assign[var]
    return v if sign == 1 else 1-v


def sat(clause, assign):
    return any(lit_val(v, s, assign) for v, s in clause)


def clause_local_anchor_check(r=3, zcount=2):
    y = 'y'
    xs = [f'x{i}' for i in range(r)]
    zs = [f'z{i}' for i in range(zcount)]
    vars_ = [y] + xs + zs
    checked = 0
    blocker_checks = 0
    bad = []
    for zbits in product([0, 1], repeat=zcount):
        base = {y: 1, **{x: 0 for x in xs}, **dict(zip(zs, zbits))}
        flip = base.copy()
        flip[y] = 0
        for x in xs:
            flip[x] = 1

        # A selected child has negative degree one, and that unique negative
        # occurrence is reserved for its beta blocker, hence no other clause
        # can contain -x_i. A selected t_(1,1) root has one +y occurrence;
        # we restrict that occurrence to alpha_safe=(ps,ns2,pu), so a true
        # negative literal of an unflipped anchor remains after y flips.
        for trip in combinations(vars_, 3):
            for signs in product([-1, 1], repeat=3):
                cl = tuple(zip(trip, signs))
                if not sat(cl, base):
                    continue
                if any(v in xs and s == -1 for v, s in cl):
                    continue
                if (y, 1) in cl:
                    anchored = any(
                        v in zs and s == -1 and lit_val(v, s, base)
                        for v, s in cl
                    )
                    if not anchored:
                        continue
                checked += 1
                if not sat(cl, flip):
                    bad.append((base, cl, flip))

        # beta blocker=(ns1,pu,nu): (-x_i) OR (false pu filler) OR (-y).
        # It is uniquely satisfied by -x_i before, and rescued by -y after
        # the root flip.
        z = zs[0]
        false_sign = 1 if base[z] == 0 else -1
        for x in xs:
            cl = ((x, -1), (y, -1), (z, false_sign))
            truths = [lit_val(v, s, base) for v, s in cl]
            assert truths == [1, 0, 0]
            assert sat(cl, flip)
            blocker_checks += 1
    return checked, blocker_checks, bad


def hypergeom_prob(L, H, U, e):
    if e < 0 or e > H or e > U or U-e > L-H:
        return Fraction(0, 1)
    return Fraction(comb(H, e)*comb(L-H, U-e), comb(L, U))


def weighted_hypergeom(L, H, U):
    # E[2^{-E}] for E=overlap of a uniform U-subset with H special slots.
    return sum(
        hypergeom_prob(L, H, U, e)*Fraction(1, 2**e)
        for e in range(min(H, U)+1)
    )


def brute_weight(L, H, U):
    special = set(range(H))
    total = Fraction(0, 1)
    count = 0
    for S in combinations(range(L), U):
        e = len(special.intersection(S))
        total += Fraction(1, 2**e)
        count += 1
    return total/Fraction(count, 1)


checked, blocker_checks, bad = clause_local_anchor_check()
print('ANCHORED_DEGREE_ONE_CLAUSE_CHECK')
print('allowed_nonblocker_clause_cases_checked =', checked)
print('mandatory_beta_blockers_checked =', blocker_checks)
print('falsified_after_simultaneous_selected_pair_flips =', len(bad))
print('clause_check_pass =', len(bad) == 0)

mismatch = []
bound_fail = []
tests = 0
for L in range(1, 11):
    for H in range(L+1):
        for U in range(L+1):
            tests += 1
            exact = weighted_hypergeom(L, H, U)
            brute = brute_weight(L, H, U)
            if exact != brute:
                mismatch.append((L, H, U, exact, brute))
            # Maclaurin bound: e_U(w)/C(L,U) <= (e_1(w)/L)^U
            # for H weights 1/2 and L-H weights 1.
            rhs = Fraction(2*L-H, 2*L)**U
            if exact > rhs:
                bound_fail.append((L, H, U, exact, rhs))

print('\nHYPERGEOMETRIC_SCORE_PENALTY_CHECK')
print('triples_checked =', tests)
print('exact_formula_mismatches =', len(mismatch))
print('maclaurin_bound_failures =', len(bound_fail))
print('hypergeom_check_pass =', len(mismatch) == 0 and len(bound_fail) == 0)

print('\nPAIR_SCORE_FACTORS')
for e in range(0, 9):
    print(e, Fraction(1, 2**e))

# One exact nested toy refinement, only to check that the three-stage
# hypergeometric bookkeeping is wired correctly. It is NOT a source numeric.
P, T, A = 12, 4, 5
Q, F, B = 10, 3, 4
L = 9
R = Fraction(0, 1)
for u in range(max(0, T-(P-A)), min(T, A)+1):
    pu = Fraction(comb(A, u)*comb(P-A, T-u), comb(P, T))
    for hh in range(max(0, F-(Q-B)), min(F, B)+1):
        ph = Fraction(comb(B, hh)*comb(Q-B, F-hh), comb(Q, F))
        R += pu*ph*weighted_hypergeom(L, hh, u)
print('\nNESTED_REFINEMENT_TOY_EXACT')
print('parameters =', (P, T, A, Q, F, B, L))
print('weighted_ratio =', R)
print('weighted_ratio_float =', float(R))
print('strict_penalty =', R < 1)

PASS = (len(bad) == 0 and len(mismatch) == 0 and len(bound_fail) == 0 and R < 1)
print('\nALL_EXACT_CHECKS_PASS =', PASS)
