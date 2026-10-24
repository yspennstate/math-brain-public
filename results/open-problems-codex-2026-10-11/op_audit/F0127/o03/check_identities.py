from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

records = []
for name, n, steps in [('cycle', 7, [(1, .5), (-1, .5)]),
                        ('weighted_cycle', 9, [(1, .35), (-1, .35), (2, .15), (-2, .15)]),
                        ('complete', 8, [(j, 1/7) for j in range(1, 8)])]:
    Q = np.zeros((n, n))
    for i in range(n):
        for step, weight in steps:
            Q[i, (i+step) % n] += weight / 2
    Q -= np.eye(n)/2
    eigenvalues = np.linalg.eigvalsh(-Q)[1:]
    K = sum(1/eigenvalues)
    keep = np.arange(1, n)
    hitting = np.linalg.solve(-Q[np.ix_(keep, keep)], np.ones(n-1)).sum()/n
    pair_Q = np.kron(Q, np.eye(n)) + np.kron(np.eye(n), Q)
    off = [i*n+j for i in range(n) for j in range(n) if i != j]
    meeting = np.linalg.solve(-pair_Q[np.ix_(off, off)], np.ones(len(off))).sum()/n**2
    assert np.isclose(hitting, K, rtol=1e-11)
    assert np.isclose(meeting, K/2, rtol=1e-11)
    for s in [.03, .4, 2.0]:
        # Direct killed-generator Laplace transform, including diagonal start mass.
        A = pair_Q[np.ix_(off, off)]
        absorption = -A @ np.ones(len(off))
        direct = (n + np.linalg.solve(s*np.eye(len(off))-A, absorption).sum())/n**2
        renewal = 1/(1+s*sum(1/(s+2*eigenvalues)))
        assert np.isclose(direct, renewal, rtol=1e-11)
    uniform_mix = brentq(lambda t: n*expm(t*Q)[0,0]-1.5, 0, 1000)
    relaxation = 1/eigenvalues[0]
    bound = relaxation*max(1, np.log(4*meeting/relaxation))
    assert uniform_mix <= bound + 1e-10
    records.append(f'{name}: n={n}, stationary hitting={hitting:.12g}, meeting={meeting:.12g}, K={K:.12g}; uniform mixing={uniform_mix:.12g} <= Hermon bound={bound:.12g}; three Laplace-transform checks passed')

for n in range(2, 51):
    meeting = Fraction(n-1, n)*Fraction(n-1)
    coal = sum((Fraction(2*(n-1), k*(k-1)) for k in range(2,n+1)), Fraction(0))
    assert coal == 2*meeting
records.append('Complete graphs n=2,...,50: exact Fraction computations give E C = 2 tau_meet, including coincident stationary starts.')
out = '\n'.join(records)+'\n'
Path('independent_checks.txt').write_text(out, encoding='utf-8')
print(out)
