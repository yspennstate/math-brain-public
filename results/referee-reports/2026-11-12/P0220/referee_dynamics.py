"""Direct exact jump-process simulation, independently coded.

Samples on a fixed time grid; a single exponential hazard budget is consumed
across sample times, rather than redrawing an event after each observation.
Separate iid uniform sequences give a second Monte Carlo method via O(n^2) LIS.
No subprocesses or workers; arrays total less than 20 MB.
"""
import bisect
import math
import random
import time
from fractions import Fraction
import numpy as np
from referee_numeric import determinant

SAMPLES = 180000
SPACING = 2.0
BURN = 50.0
BATCHES = 90
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def estimate(values):
    blocks = np.asarray(values).reshape(BATCHES, -1).mean(axis=1)
    return float(blocks.mean()), float(blocks.std(ddof=1)/math.sqrt(BATCHES))


def direct(k, seed):
    rng = random.Random(seed)
    start_scale = {2: 1e-5, 3: 100.0, 4: 1.0}[k]
    positions = [start_scale*(i+1) for i in range(k)]
    sample_time = BURN
    now = 0.0
    hazard = rng.expovariate(1.0)
    samples = np.empty((SAMPLES, k))
    count, events = 0, 0
    while count < SAMPLES:
        dt_event = math.log1p(hazard/positions[-1])
        if now+dt_event <= sample_time:
            multiplier = 1+hazard/positions[-1]
            positions = [x*multiplier for x in positions]
            now += dt_event
            point = rng.random()*positions[-1]
            positions[bisect.bisect_right(positions, point)] = point
            events += 1
            hazard = rng.expovariate(1.0)
        else:
            dt = sample_time-now
            hazard -= positions[-1]*math.expm1(dt)
            multiplier = math.exp(dt)
            positions = [x*multiplier for x in positions]
            now = sample_time
            samples[count] = positions
            count += 1
            sample_time = BURN+count*SPACING
    return samples, events, start_scale


def lis_sample(seed):
    rng = random.Random(seed)
    result = np.empty((SAMPLES, 4))
    for run in range(SAMPLES):
        values, ending = [], []
        longest, clock = 0, 0.0
        while longest < 4:
            u = rng.random()
            length = 1+max((v for x, v in zip(values, ending) if x < u), default=0)
            values.append(u)
            ending.append(length)
            clock += rng.expovariate(1.0)
            if length > longest:
                longest = length
                result[run, longest-1] = clock
    return result


def summarize(samples, label, cases):
    for i in range(1, samples.shape[1]+1):
        mean, se = estimate(samples[:,i-1])
        target = [1, math.e, 5.0906787293171656, 8.086508584743576][i-1]
        say(f'{label} EX_{i}: mean={mean:.9f}; batch_SE={se:.7f}; theory={target:.12f}; z={(mean-target)/se:+.3f}')
    for case in cases:
        hits = np.ones(SAMPLES, dtype=bool)
        for s, k in case:
            hits &= samples[:,k-1] > float(s)
        value, se = estimate(hits)
        theory = float(determinant([(Fraction(s), k) for s, k in case])[0])
        say(f'{label} {case}: empirical={value:.8f}; batch_SE={se:.7f}; determinant={theory:.12f}; z={(value-theory)/se:+.3f}')


def main():
    start = time.monotonic()
    cases = [[('2',2)], [('0.5',1),('2',2)], [('3',3)],
             [('0.2',1),('0.6',2),('1',3)], [('1',2),('3',3)],
             [('1',2),('3',4)], [('0.5',1),('1.5',2),('3',3),('5',4)]]
    say(f'Exact dynamics: samples={SAMPLES}, spacing={SPACING}, burn={BURN}, batches={BATCHES}.')
    for k in [2,3,4]:
        samples, events, scale = direct(k, 891170+k)
        say(f'k={k}; initial X_i={scale}*i; seed={891170+k}; events={events}; observed time={SPACING*(SAMPLES-1):.0f}')
        summarize(samples, f'dynamics k={k}', [c for c in cases if max(j for t,j in c) <= k])
    samples = lis_sample(309917)
    say('IID LIS/Gamma samples; seed=309917; quadratic subsequence DP; independent of dynamics.')
    summarize(samples, 'LIS/Gamma', cases)
    say(f'Elapsed seconds: {time.monotonic()-start:.3f}')
    with open('referee_dynamics.txt', 'w') as output:
        output.write('\n'.join(LOG)+'\n')


if __name__ == '__main__':
    main()
