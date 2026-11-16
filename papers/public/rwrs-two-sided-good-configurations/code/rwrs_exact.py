"""Exact finite-window RWRS calculations; standard library, one thread.

A record is chronological, with a single None marking the unobserved time.
The walk starts at the first time, by translation invariance of iid scenery.
DP states keep the coloured visited interval and the current site within it.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import os
import time


def full_record_count(record, p, max_states=200_000):
    """Return integer numerator over b**N * 2**(N+1), and peak states.

    Here p=a/b and N=len(record)-1. A new site has scenery factor 1/2;
    revisiting a matching site has factor 1. Integer weights therefore
    multiply by 1 at a new site and by 2 at a matching revisit.
    """
    p = Fraction(p)
    a, b = p.numerator, p.denominator
    states = {(0, 1, record[0]): 1}  # (relative position, range, colour bits)
    peak = 1
    for colour in record[1:]:
        nxt = defaultdict(int)
        for (x, size, bits), weight in states.items():
            for step, step_weight in ((1, a), (-1, b-a)):
                if not step_weight:
                    continue
                xx = x + step
                if xx == -1:
                    key = (0, size+1, (bits << 1) | colour)
                    factor = 1
                elif xx == size:
                    key = (xx, size+1, bits | (colour << size))
                    factor = 1
                elif ((bits >> xx) & 1) == colour:
                    key = (xx, size, bits)
                    factor = 2
                else:
                    continue
                nxt[key] += weight * step_weight * factor
        states = nxt
        peak = max(peak, len(states))
        if peak > max_states:
            raise RuntimeError(f'state cap {max_states} exceeded')
    return sum(states.values()), peak


def conditional(record, p):
    zero = record.index(None)
    counts, peaks = [], []
    for colour in (0, 1):
        filled = list(record)
        filled[zero] = colour
        count, peak = full_record_count(filled, p)
        counts.append(count)
        peaks.append(peak)
    if not sum(counts):
        raise ValueError('conditioning cylinder has zero probability')
    return Fraction(counts[1], sum(counts)), max(peaks)


def brute_probability(record, p):
    """Independent enumeration of step words, integrating scenery by sites."""
    p = Fraction(p)
    ans = Fraction(0)
    for steps in product((-1, 1), repeat=len(record)-1):
        x, colours, weight = 0, {}, Fraction(1)
        positions = [0]
        for step in steps:
            x += step
            positions.append(x)
            weight *= p if step == 1 else 1-p
        for x, colour in zip(positions, record):
            if colour is None:
                continue
            if x in colours and colours[x] != colour:
                break
            colours[x] = colour
        else:
            ans += weight / 2**len(colours)
    return ans


def cut_edges(positions):
    return [k for k in range(len(positions)-1)
            if max(positions[:k+1]) <= positions[k]
            and min(positions[k+1:]) > positions[k]]


def polymer_probability(record, p):
    """Independent interval-block partition function, for proof audits only.

    Enumerates words inside each interval; intended for <=9 observations.
    """
    p = Fraction(p)
    if not 0 < p < 1:
        raise ValueError('polymer audit uses 0<p<1')
    size = len(record)
    activity = {}
    for u in range(size):
        for v in range(u, size):
            length = v-u
            total = Fraction(0)
            for word in product((-1, 1), repeat=length):
                positions = [0]
                for step in word:
                    positions.append(positions[-1]+step)
                if cut_edges(positions):
                    continue
                if u > 0 and min(positions) != positions[0]:
                    continue
                if v < size-1 and max(positions) != positions[-1]:
                    continue
                colours = {}
                for x, colour in zip(positions, record[u:v+1]):
                    if colour is None:
                        continue
                    if x in colours and colours[x] != colour:
                        break
                    colours[x] = colour
                else:
                    h = sum(c is not None for c in record[u:v+1])
                    left = word.count(-1)
                    assert length <= 3*left or not length
                    total += ((1-p)/p)**left * 2**(h-len(colours))
            activity[u,v] = total
    z = [Fraction(0)]*(size+1)
    z[size] = 1
    for u in range(size-1, -1, -1):
        z[u] = sum(activity[u,v]*z[v+1] for v in range(u,size))
    return p**(size-1) * Fraction(1, 2**sum(c is not None for c in record)) * z[0]


def self_check():
    checks = 0
    for p in (Fraction(1,2), Fraction(4,5), Fraction(199,200)):
        for record in product((0,1), repeat=7):
            count, _ = full_record_count(record, p)
            prob = Fraction(count, p.denominator**6 * 2**7)
            assert prob == brute_probability(record, p)
            checks += 1
        for record in ((1,1,1,None,1,1,1), (0,0,1,None,0,1,1),
                       (1,0,1,0,0,1,0), (0,None,1,0,1)):
            prob = brute_probability(record, p)
            assert prob == polymer_probability(record, p)
            checks += 1
            if None in record:
                value, _ = conditional(record, p)
                other, _ = conditional([None if c is None else 1-c for c in record], p)
                reverse_p, _ = conditional(record, 1-p)
                assert value + other == 1
                assert value == reverse_p
                checks += 2
    for record in ((1,None,0), (1,0,None,1,1), (0,1,0,None,1,0,1)):
        assert conditional(record, Fraction(1))[0] == Fraction(1,2)
        checks += 1
    return checks


if __name__ == '__main__':
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    start = time.monotonic()
    checks = self_check()
    print(f'{checks} exact checks passed in {time.monotonic()-start:.3f}s; nice={os.getpriority(os.PRIO_PROCESS,0)}')
