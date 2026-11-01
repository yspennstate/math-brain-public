#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

K = 2
L = 3
N = 3
RATES = [Fraction(1), Fraction(1), Fraction(1)]

states = [s for s in product(range(K + 1), repeat=L) if sum(s) == N]
index = {s: i for i, s in enumerate(states)}

Q = [[Fraction(0) for _ in states] for _ in states]
transitions = {}
for s in states:
    i = index[s]
    out = []
    out_rate = Fraction(0)
    for x in range(L):
        y = (x + 1) % L
        if s[x] > 0 and s[y] < K:
            t = list(s)
            t[x] -= 1
            t[y] += 1
            t = tuple(t)
            r = RATES[x]
            Q[i][index[t]] += r
            out_rate += r
            out.append(t)
    Q[i][i] -= out_rate
    transitions[s] = out

expected_states = [
    (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1),
    (1, 2, 0), (2, 0, 1), (2, 1, 0),
]
assert states == expected_states

# Exact stationary law in lexicographic state order.
pi = [
    Fraction(2, 11), Fraction(1, 11), Fraction(1, 11),
    Fraction(2, 11), Fraction(2, 11), Fraction(2, 11),
    Fraction(1, 11),
]
assert sum(pi) == 1

# Exact stationarity: pi Q = 0.
residual = [
    sum(pi[i] * Q[i][j] for i in range(len(states)))
    for j in range(len(states))
]
assert residual == [Fraction(0)] * len(states)

# Exact stationary current through each directed bond.
currents = []
for x in range(L):
    y = (x + 1) % L
    J = sum(
        pi[i] * RATES[x]
        for i, s in enumerate(states)
        if s[x] > 0 and s[y] < K
    )
    currents.append(J)
assert currents == [Fraction(6, 11)] * L

# Any iid product law on the ring, conditioned on total particle number 3,
# gives equal probability to arrangements with the same occupancy multiset.
# The actual stationary law distinguishes the two orientations below.
assert pi[index[(0, 1, 2)]] == Fraction(2, 11)
assert pi[index[(0, 2, 1)]] == Fraction(1, 11)
assert pi[index[(0, 1, 2)]] != pi[index[(0, 2, 1)]]

print('PASS exact K=2 homogeneous 3-cycle certificate')
print('states:', states)
print('stationary_pi:', [str(x) for x in pi])
print('piQ:', [str(x) for x in residual])
print('bond_currents:', [str(x) for x in currents])
print('product_conditioning_obstruction:',
      'P(0,1,2)=2/11 != P(0,2,1)=1/11')
print('transitions:')
for s in states:
    print(' ', s, '->', transitions[s])
