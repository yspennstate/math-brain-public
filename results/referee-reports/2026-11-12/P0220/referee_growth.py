"""Independent Young-lattice propagation at 50 digits, no skew determinants.

The unnormalized vector is g(lambda)=exp(t)*|lambda|!*P(lambda)/f(lambda).
Its evolution is exp(Delta*B), where B adds one box with coefficient one.
Hook dimensions enter only when converting g back to probabilities.
"""
import math
import time
from fractions import Fraction
import mpmath as mp
from referee_numeric import determinant, hook_dimension, partitions_at_most, num

mp.mp.dps = 50
START = time.monotonic()


def growth(obs, cutoff=40):
    d = obs[-1][1]-1
    if d == 0:
        return mp.exp(-num(obs[-1][0]))
    factorials = [math.factorial(n) for n in range(cutoff+d+1)]
    states = [p for n in range(cutoff+1) for p in partitions_at_most(n, d)]
    lookup = {p: j for j, p in enumerate(states)}
    edges = []
    for j, p in enumerate(states):
        if sum(p) == cutoff:
            continue
        for row in range(d):
            if row and p[row] == p[row-1]:
                continue
            child = list(p)
            child[row] += 1
            edges.append((j, lookup[tuple(child)]))
    zero = mp.mpf(0)
    mass = [zero]*len(states)
    mass[0] = mp.mpf(1)
    prev = Fraction(0)
    for t, k in obs:
        delta = num(t-prev)
        answer = mass.copy()
        term = mass
        for h in range(1, cutoff+1):
            following = [zero]*len(states)
            scale = delta/h
            for src, dst in edges:
                if term[src]:
                    following[dst] += term[src]*scale
            for j, value in enumerate(following):
                if value:
                    answer[j] += value
            term = following
        for j, part in enumerate(states):
            if sum(x > 0 for x in part) >= k:
                answer[j] = zero
        mass = answer
        prev = t
    total = mp.fsum(value*hook_dimension(part, factorials)/factorials[sum(part)]
                    for part, value in zip(states, mass) if value)
    return mp.exp(-num(obs[-1][0]))*total


def main():
    lines = ['Young-lattice propagation; 50 digits; total size cutoff 40.']
    cases = [
        [('0.2',1),('1',2)],
        [('0.4',2),('1',2)],
        [('0.2',1),('1',4)],
        [('0.4',2),('1',4)],
        [('0.2',1),('0.6',2),('1',3)],
        [('0.2',1),('0.6',3),('1',4)],
        [('0.2',2),('0.6',2),('1',4)],
        [('0.2',1),('0.6',1),('1',4)],
        [('0.2',2),('0.6',4),('1',4)],
        [('0.2',1),('0.6',1),('1',1)],
    ]
    tail = mp.exp(-1)/mp.factorial(41)/(1-mp.mpf(1)/42)
    lines.append('Rigorous omitted probability <= '+mp.nstr(tail,15)+'.')
    for case in cases:
        obs = [(Fraction(t), k) for t, k in case]
        result = growth(obs)
        expected, size = determinant(obs)
        diff = expected-result
        assert -mp.mpf('1e-47') < diff < tail+mp.mpf('1e-47')
        line = (f'{case}; size={size}; growth={mp.nstr(result,42)}; '
                f'determinant-minus-growth={mp.nstr(diff,8)}; PASS')
        print(line, flush=True)
        lines.append(line)
    lines.append(f'Elapsed seconds: {time.monotonic()-START:.3f}')
    with open('referee_growth.txt', 'w') as output:
        output.write('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
