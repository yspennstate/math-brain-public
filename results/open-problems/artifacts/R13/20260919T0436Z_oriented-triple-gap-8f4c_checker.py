from itertools import combinations, product
from collections import Counter, defaultdict

N = 6
# Projective Boolean sign classes, quotienting epsilon ~ -epsilon by fixing bit 0 = 0.
classes = [x for x in range(1 << N) if (x & 1) == 0]
triples = list(combinations(range(N), 3))

# An oriented equal-triple atom is a support T plus one of four relative sign patterns.
# We fix the first support-coordinate pattern bit to 0; the remaining two bits choose
# the pattern modulo simultaneous sign reversal. The bad class condition is that
# epsilon_j xor pattern_j is constant on T.
atoms = []
for T in triples:
    for b1, b2 in product((0,1), repeat=2):
        pat = {T[0]:0, T[1]:b1, T[2]:b2}
        bad = set()
        for x in classes:
            vals = [((x >> j) & 1) ^ pat[j] for j in T]
            if vals[0] == vals[1] == vals[2]:
                bad.add(x)
        atoms.append((T, (b1,b2), frozenset(bad)))

assert len(classes) == 32
assert len(triples) == 20
assert len(atoms) == 80
assert all(len(B) == 8 for _,_,B in atoms)

# A family of strict normalized equal-triple rows r_i=a_i sigma_i 1_{T_i}, a_i>1/3,
# under any per-coordinate squared-load cap alpha<1/3 has support degree at most 2:
# three occurrences in one coordinate would cost >3*(1/3)^2 = 1/3.
# Hence there are at most 4 rows (3q support incidences <= 6*2=12).
# For q<=3, union <= 3*8=24. The only nontrivial finite case is q=4.

count_q4 = 0
union_dist = Counter()
support_multiset_count = set()
max_union = -1
max_examples = []
for inds in combinations(range(len(atoms)), 4):
    Ts = [atoms[i][0] for i in inds]
    deg = [sum(j in T for T in Ts) for j in range(N)]
    if max(deg) > 2:
        continue
    count_q4 += 1
    # 12 incidences and six coordinates with cap 2 force degree exactly 2.
    assert deg == [2] * N
    support_multiset_count.add(tuple(sorted(Ts)))
    U = set().union(*(atoms[i][2] for i in inds))
    u = len(U)
    union_dist[u] += 1
    if u > max_union:
        max_union = u
        max_examples = [inds]
    elif u == max_union:
        max_examples.append(inds)

assert count_q4 == 19560
assert len(support_multiset_count) == 85
assert max_union == 24
assert 32 - max_union == 8
# Full exact distribution is retained as a fingerprint of the enumeration.
expected = Counter({19:1440, 20:2400, 22:11520, 23:960, 24:3240})
assert union_dist == expected

# Also isolate the simple-support balanced case (four distinct triples), which has
# a sharper 23-class maximum. This is useful for diagnosing the fractional extremizer.
simple_count = 0
simple_dist = Counter()
for Fs in combinations(triples, 4):
    deg = [sum(j in T for T in Fs) for j in range(N)]
    if max(deg) <= 2:
        assert deg == [2] * N
        simple_count += 1
        # Maximize over all 4^4 orientations on these supports.
        idx_lists = []
        for T in Fs:
            idx_lists.append([i for i,(S,_,_) in enumerate(atoms) if S == T])
        best = 0
        for choice in product(*idx_lists):
            U = set().union(*(atoms[i][2] for i in choice))
            best = max(best, len(U))
        simple_dist[best] += 1
assert simple_count == 75
assert simple_dist == Counter({24:45, 23:30})

ex = max_examples[0]
formatted_ex = [(atoms[i][0], atoms[i][1]) for i in ex]

print('R13_ORIENTED_TRIPLE_GAP_EXACT_PASS')
print('projective_classes =', len(classes))
print('support_triples =', len(triples))
print('oriented_triple_atoms =', len(atoms))
print('classes_per_atom =', 8)
print('q4_degree_le_2_oriented_families =', count_q4)
print('q4_support_multisets =', len(support_multiset_count))
print('q4_union_distribution =', dict(sorted(union_dist.items())))
print('q4_max_union =', max_union)
print('q4_min_uncovered =', 32-max_union)
print('q4_max_example =', formatted_ex)
print('simple_support_systems =', simple_count)
print('simple_support_best_union_distribution =', dict(sorted(simple_dist.items())))
print('restricted_equal_triple_cover_impossible_for_alpha_lt_1_over_3 = True')
