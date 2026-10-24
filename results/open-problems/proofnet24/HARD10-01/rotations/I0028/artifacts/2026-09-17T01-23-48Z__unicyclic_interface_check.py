from fractions import Fraction


def gauss(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c])
        M[c], M[p] = M[p], M[c]
        q = M[c][c]
        M[c] = [x / q for x in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                q = M[r][c]
                M[r] = [M[r][j] - q * M[c][j] for j in range(n + 1)]
    return [M[i][-1] for i in range(n)]


# Diagnostic 1: triangle a-b-c-a. Root a, with a-b treated as the
# would-be tree parent edge for the component {b,c}. Compute the probability
# that {b,c} is covered before the first directed traversal a->b.
# q_a = (1/2)*0 + (1/2)*q_c
# q_c = (1/2)*1 + (1/2)*q_a
A = [
    [Fraction(1), Fraction(-1, 2)],
    [Fraction(-1, 2), Fraction(1)],
]
b = [Fraction(0), Fraction(1, 2)]
q_a, q_c = gauss(A, b)
assert q_a == Fraction(1, 3)


# Diagnostic 2: two-terminal segment L-u-v-R with a pendant leaf y at v.
# Start an internal episode by L->u and stop at the first hit of {L,R}.
# Track whether y was seen. This tests whether entrance count alone can
# summarize the cover state: it cannot, because the exit terminal changes
# the conditional probability that y was covered.
neighbors = {'u': ['L', 'v'], 'v': ['u', 'R', 'y'], 'y': ['v']}
states = [('u', 0), ('v', 0), ('y', 1), ('u', 1), ('v', 1)]
idx = {s: i for i, s in enumerate(states)}
outcomes = [('L', 0), ('R', 0), ('L', 1), ('R', 1)]


def absorption_probability(target):
    n = len(states)
    A = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    for i, (x, seen) in enumerate(states):
        A[i][i] = 1
        for nb in neighbors[x]:
            p = Fraction(1, len(neighbors[x]))
            if nb in ('L', 'R'):
                if (nb, seen) == target:
                    b[i] += p
            else:
                ns = (nb, int(seen or nb == 'y'))
                A[i][idx[ns]] -= p
    sol = gauss(A, b)
    return sol[idx[('u', 0)]]


p = {o: absorption_probability(o) for o in outcomes}
assert p == {
    ('L', 0): Fraction(3, 5),
    ('R', 0): Fraction(1, 5),
    ('L', 1): Fraction(1, 15),
    ('R', 1): Fraction(2, 15),
}
assert sum(p.values(), Fraction(0)) == 1
py_given_L = p[('L', 1)] / (p[('L', 0)] + p[('L', 1)])
py_given_R = p[('R', 1)] / (p[('R', 0)] + p[('R', 1)])
assert py_given_L == Fraction(1, 10)
assert py_given_R == Fraction(2, 5)
assert py_given_L != py_given_R

print('TRIANGLE_BYPASS_PROB', q_a)
for o in outcomes:
    print('EPISODE_OUTCOME', o, p[o])
print('P_Y_SEEN_GIVEN_EXIT_L', py_given_L)
print('P_Y_SEEN_GIVEN_EXIT_R', py_given_R)
print('EXIT_TYPE_MATTERS', py_given_L != py_given_R)
print('EXACT_CHECK_PASS')
