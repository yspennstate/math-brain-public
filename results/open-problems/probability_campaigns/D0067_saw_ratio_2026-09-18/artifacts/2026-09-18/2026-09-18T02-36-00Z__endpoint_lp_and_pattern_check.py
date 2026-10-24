from itertools import product

P = [(0,0),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]
NN = {(1,0),(-1,0),(0,1),(0,-1)}

def md(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

assert len(P) == len(set(P))
assert all(md(a,b) == 1 for a,b in zip(P,P[1:]))
assert NN.issubset(set(P))
print('P_SELF_AVOIDING=PASS')
print('P_NEAREST_NEIGHBOR_STEPS=PASS')
print('P_VISITS_ALL_ORIGIN_NEIGHBORS=PASS')

# Exact pointwise endpoint-degree slack identity on {0,1,2,3}^2.
eq_pairs = []
for x,y in product(range(4), repeat=2):
    slack = (3-x)*(3-y)
    assert x*y == 3*x + 3*y - 9 + slack
    assert slack >= 0
    if slack == 0:
        eq_pairs.append((x,y))
expected = {(x,y) for x,y in product(range(4), repeat=2) if x == 3 or y == 3}
assert set(eq_pairs) == expected
print('POINTWISE_SLACK_IDENTITY=PASS')
print('ZERO_SLACK_SET=PASS', eq_pairs)

# Explicit simultaneous two-end-pattern family.  For every M>=3 the formula
# in the report gives an (M+16)-step SAW beginning with P and whose final
# seven edges, read backwards from the endpoint, are a translate of P.
def both_end_walk(M):
    start = P[:]
    connector = [(0,-2)] + [(x,-2) for x in range(1,M+1)] + [(M,-1)]
    terminal_forward = [
        (M-1,-1),(M-1,0),(M-1,1),(M,1),(M+1,1),(M+1,0),(M,0)
    ]
    return start + connector + terminal_forward

for M in range(3,101):
    W = both_end_walk(M)
    assert len(W) == M + 17
    assert len(W) == len(set(W))
    assert all(md(a,b) == 1 for a,b in zip(W,W[1:]))
    assert W[:8] == P
    z = W[-1]
    reversed_terminal = [(v[0]-z[0],v[1]-z[1]) for v in W[-8:][::-1]]
    assert reversed_terminal == P
    start_neighbours = {(W[0][0]+dx,W[0][1]+dy) for dx,dy in NN}
    end_neighbours = {(z[0]+dx,z[1]+dy) for dx,dy in NN}
    assert start_neighbours.issubset(set(W))
    assert end_neighbours.issubset(set(W))
print('SIMULTANEOUS_BOTH_END_PATTERN_FAMILY_M_3_TO_100=PASS')
print('FAMILY_LENGTH_FORMULA_n=M+16=PASS')
