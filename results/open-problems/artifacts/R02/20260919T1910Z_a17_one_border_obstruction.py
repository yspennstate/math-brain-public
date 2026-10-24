from itertools import combinations

A = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,1],
[1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1],
[-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1],
[1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1],
[1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1],
[-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1],
[1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1],
[-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,1],
[1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1],
[-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1],
[-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1],
[-1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Exact finite core for the following handoff lemma.
# If D is any 18x18 sign matrix having this A as its upper-left 17x17
# principal block, then disc(D) <= 6.
#
# Projectivize 17-sign vectors by fixing coordinate 17 to +1.
def vec(mask):
    return [(-1 if (mask >> j) & 1 else 1) for j in range(16)] + [1]

def rowsums(mask):
    y = vec(mask)
    return [sum(a*b for a,b in zip(row,y)) for row in A]

best = 99
minimizers = []
for mask in range(1 << 16):
    s = rowsums(mask)
    m = max(abs(z) for z in s)
    if m < best:
        best = m
        minimizers = [(mask,s)]
    elif m == best:
        minimizers.append((mask,s))

singletons = []
active_hist = {}
for mask,s in minimizers:
    active = [i for i,z in enumerate(s) if abs(z) == best]
    active_hist[len(active)] = active_hist.get(len(active),0) + 1
    if len(active) == 1:
        i = active[0]
        singletons.append((mask,i,1 if s[i] > 0 else -1))

# For projective r with r_17=+1, r.y = 1 iff the first-16 masks differ
# in exactly 8 coordinates. Mark all r hit by a singleton minimizer y.
layer8 = []
for C in combinations(range(16), 8):
    d = 0
    for j in C:
        d |= 1 << j
    layer8.append(d)

covered = bytearray(1 << 16)
for smask,_,_ in singletons:
    for d in layer8:
        covered[smask ^ d] = 1

uncovered = [m for m,v in enumerate(covered) if not v]

assert best == 7
assert len(minimizers) == 21952
assert active_hist == {1:3780, 2:14364, 3:3264, 4:480, 5:64}
assert len(singletons) == 3780
assert len(layer8) == 12870
assert not uncovered

print('R02 A17 one-border exact obstruction checker')
print('projective_signings_checked =', 1 << 16)
print('A17_discrepancy =', best)
print('A17_minimizers =', len(minimizers))
print('active_set_histogram =', dict(sorted(active_hist.items())))
print('singleton_minimizers =', len(singletons))
print('distance8_masks =', len(layer8))
print('projective_border_rows_covered_at_dot_1 =', sum(covered))
print('uncovered_border_rows =', len(uncovered))
print('THEOREM_CORE: for every r in {+-1}^17 (mod global sign),')
print('there is a singleton A17 minimizer y with r.y = 1.')
print('COROLLARY: every 18x18 sign matrix having this A17 as a principal')
print('top-left block has discrepancy <= 6, for every added column/row/corner.')
print('PASS')
