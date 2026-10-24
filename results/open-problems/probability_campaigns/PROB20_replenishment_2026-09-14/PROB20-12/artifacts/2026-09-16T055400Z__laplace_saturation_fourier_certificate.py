import itertools
import collections
import sympy as sp

# Exact certificate for the 6-site Fourier example in
# runs/2026-09-16/2026-09-16T055400Z__report.md

V = tuple(range(6))
I = sp.I
SQ3 = sp.sqrt(3)
ZETA = sp.Rational(1,2) + I*SQ3/2
SQ6 = sp.sqrt(6)

F = sp.Matrix([[sp.simplify(ZETA**(j*k)/SQ6) for k in V] for j in V])
assert sp.simplify(F.conjugate().T*F) == sp.eye(6)
DET_F = sp.simplify(F.det())
assert sp.simplify(DET_F*sp.conjugate(DET_F)) == 1


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for t in range(1, len(items)):
        b = items[t]
        rem = items[1:t] + items[t+1:]
        for rest in perfect_matchings(rem):
            yield ((a,b),) + rest


def circular_gap(e):
    a,b = e
    d = (b-a) % 6
    return min(d, 6-d)


def row_states():
    out = []
    for e0 in itertools.combinations(V,2):
        rem = [x for x in V if x not in e0]
        for e1 in itertools.combinations(rem,2):
            e2 = tuple(x for x in rem if x not in e1)
            out.append((tuple(sorted(e0)), tuple(sorted(e1)), tuple(sorted(e2))))
    return out

ROW_STATES = row_states()
assert len(ROW_STATES) == 90


def abs_minor_from_gaps(freq_gap, row_gap):
    # |1-zeta^(freq_gap*row_gap)|/6, simplified by circular gap type.
    if freq_gap == 1:
        return {1:sp.Rational(1,6), 2:SQ3/6, 3:sp.Rational(1,3)}[row_gap]
    if freq_gap == 2:
        return {1:SQ3/6, 2:SQ3/6, 3:sp.Integer(0)}[row_gap]
    if freq_gap == 3:
        return {1:sp.Rational(1,3), 2:sp.Integer(0), 3:sp.Rational(1,3)}[row_gap]
    raise ValueError(freq_gap)


def lambda_for_frequency_matching(matching):
    gaps = tuple(circular_gap(e) for e in matching)
    total = sp.Integer(0)
    nonzero = []
    for state in ROW_STATES:
        term = sp.Integer(1)
        for g,e in zip(gaps,state):
            term *= abs_minor_from_gaps(g,circular_gap(e))
        term = sp.simplify(term)
        if term != 0:
            nonzero.append(term)
            total += term
    return sp.simplify(total), tuple(nonzero), tuple(sorted(gaps))

# Complete classification of the 15 unlabelled pairings of Fourier frequencies.
FREQ_MATCHINGS = list(perfect_matchings(V))
assert len(FREQ_MATCHINGS) == 15

classes = collections.Counter()
examples = {}
for M in FREQ_MATCHINGS:
    lam, nz, gaps = lambda_for_frequency_matching(M)
    key = (gaps, sp.simplify(lam), len(nz))
    classes[key] += 1
    examples.setdefault(key,M)

expected = {
    ((1,1,1), sp.Rational(13,9), 90): 2,
    ((1,2,2), sp.Rational(2,3)+SQ3/3, 60): 6,
    ((1,1,3), sp.Rational(10,9), 54): 3,
    ((2,2,3), sp.Integer(1), 36): 3,
    ((3,3,3), sp.Rational(4,3), 36): 1,
}
assert classes == expected

# Representative saturation example.
BLOCKS = ((0,2),(1,4),(3,5))
lam, nz, gaps = lambda_for_frequency_matching(BLOCKS)
assert gaps == (2,2,3)
assert lam == 1
assert len(nz) == 36
assert set(nz) == {sp.Rational(1,36)}

# Verify the actual canonical complex Laplace weights exactly: 36 weights 1/36, 54 zeros.
def shuffle_sign(state):
    seq = [x for edge in state for x in edge]
    inv = sum(seq[a] > seq[b] for a in range(6) for b in range(a+1,6))
    return -1 if inv % 2 else 1

canonical = []
for state in ROW_STATES:
    prod = sp.Integer(1)
    for edge,cols in zip(state,BLOCKS):
        prod *= sp.simplify(F.extract(list(edge),list(cols)).det())
    z = sp.simplify(sp.conjugate(DET_F)*shuffle_sign(state)*prod)
    canonical.append(z)

cc = collections.Counter(canonical)
assert cc == collections.Counter({sp.Rational(1,36):36, sp.Integer(0):54})
assert sp.simplify(sum(canonical)) == 1

# Verify every one-color marginal from the canonical coupling against squared minors.
for color,cols in enumerate(BLOCKS):
    for edge in itertools.combinations(V,2):
        lhs = sp.Integer(0)
        for state,z in zip(ROW_STATES,canonical):
            if state[color] == tuple(edge):
                lhs += z
        minor = sp.simplify(F.extract(list(edge),list(cols)).det())
        rhs = sp.simplify(minor*sp.conjugate(minor))
        assert sp.simplify(lhs-rhs) == 0

print('det_F',DET_F)
print('classification')
for key,count in sorted(classes.items(), key=lambda kv: kv[0][0]):
    print(key,'count',count,'example',examples[key])
print('representative_nonzero_weights',cc)
print('ALL EXACT CHECKS PASSED')
