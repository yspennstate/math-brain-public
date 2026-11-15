"""Independent permutation check of every gate presentation for m=1,2."""
import csv
import itertools
from fractions import Fraction

with open('certificates.csv') as stream:
    rows = {}
    for row in csv.DictReader(stream):
        m = int(row['m'])
        if m > 2:
            break
        rows[(m, *(int(row[k]) for k in 'abcdef'))] = row

presentations = nonchains = cyclic = chains = 0
for m in (1, 2):
    n = 3*m
    permutations = list(itertools.permutations(range(n)))
    rail_relations = [(r*m+j, r*m+j+1) for r in range(3) for j in range(m-1)]
    for gate in itertools.product(range(1, m+1), repeat=6):
        a, b, c, d, e, f = gate
        edges = rail_relations + [(a-1, m+b-1), (m+c-1, 2*m+d-1), (2*m+e-1, f-1)]
        count = 0
        before = [[0]*n for _ in range(n)]
        for permutation in permutations:
            positions = [0]*n
            for i, x in enumerate(permutation):
                positions[x] = i
            if any(positions[x] >= positions[y] for x, y in edges):
                continue
            count += 1
            for x in range(n):
                for y in range(n):
                    before[x][y] += positions[x] < positions[y]
        presentations += 1
        key = (m, *gate)
        if count == 0:
            cyclic += 1
            assert key not in rows
        elif count == 1:
            chains += 1
            assert key not in rows
        else:
            nonchains += 1
            row = rows.pop(key)
            best = max(min(before[x][y], count-before[x][y]) for x in range(n) for y in range(x+1, n))
            assert int(row['extensions']) == count
            assert int(row['best_numerator']) == best
            assert before[int(row['x'])][int(row['y'])] == int(row['x_before_y'])
assert not rows
print(f'BRUTE VERIFIED presentations={presentations} cyclic={cyclic} chains={chains} nonchains={nonchains}; every pair checked')

# The tight three-element example, outside the cyclic family, is a sanity test.
extensions = [p for p in itertools.permutations(range(3)) if p.index(0) < p.index(1)]
balances = [Fraction(min(sum(p.index(x)<p.index(y) for p in extensions), sum(p.index(y)<p.index(x) for p in extensions)), len(extensions))
            for x, y in ((0, 2), (1, 2))]
assert len(extensions) == 3 and balances == [Fraction(1, 3)]*2
print('TIGHT EXAMPLE VERIFIED extensions=3; both incomparable-pair balances=1/3')

# Independently enumerate all 9!/(3!)^3 shuffles for the width-three minimizer.
# Choosing positions, rather than generating extensions recursively, avoids
# either recurrence used by the C++ programs.
n = 9
shuffles = count = 0
before = [[0]*n for _ in range(n)]
for places_a in itertools.combinations(range(n), 3):
    left = [j for j in range(n) if j not in places_a]
    for places_b in itertools.combinations(left, 3):
        places_c = [j for j in left if j not in places_b]
        positions = [*places_a, *places_b, *places_c]
        shuffles += 1
        if not (positions[0] < positions[3] and positions[5] < positions[8] and positions[6] < positions[2]):
            continue
        count += 1
        for x in range(n):
            for y in range(n):
                before[x][y] += positions[x] < positions[y]
assert shuffles == 1680 and count == 344
best = max(min(before[x][y], count-before[x][y]) for x in range(n) for y in range(x+1, n))
assert best == before[2][5] == 137
print('WIDTH-THREE MINIMIZER VERIFIED shuffles=1680; extensions=344; A3_before_B3=137; maximum_balance=137/344; every pair checked')
