"""Exhaustive finite checks of the forcing and association proof ingredients."""
import cmath
import itertools
import json
import math
import os
import resource
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()


def e(j):
    return j*(j-1)//2


def audit(n):
    edges = list(itertools.combinations(range(n), 2))
    index = {edge: i for i, edge in enumerate(edges)}
    sizes = (2, 3, 4)
    masks = [[sum(1 << index[edge] for edge in itertools.combinations(A, 2))
              for A in itertools.combinations(range(n), j)] for j in sizes]
    graphs = 1 << len(edges)
    counts = [tuple(sum((g & mask) == 0 for mask in family) for family in masks)
              for g in range(graphs)]
    histograms = [Counter(row[i] for row in counts) for i in range(3)]
    means = [Fraction(math.comb(n, j), 2**e(j)) for j in sizes]
    variances = []
    epsilons = []
    forcing = []
    for i, j in enumerate(sizes):
        hist = histograms[i]
        mu = means[i]
        q = Fraction(1, 2**e(j))
        assert sum(x*c for x,c in hist.items()) == mu*graphs
        var = Fraction(sum(x*x*c for x,c in hist.items()), graphs)-mu**2
        epsilon = var/mu-1+2*q
        canonical_mask = masks[i][0]
        forced_hist = Counter()
        total_D = total_abs = zeros = 0
        for g, row in enumerate(counts):
            forced = counts[g & ~canonical_mask][i]
            D = forced-row[i]
            assert D >= 0
            assert (D == 0) == ((g & canonical_mask) == 0)
            forced_hist[forced] += 1
            total_D += D
            total_abs += abs(D-1)
            zeros += D == 0
        # Full distributional size bias, not just its first two moments.
        for x in set(hist) | set(forced_hist):
            assert forced_hist[x]*mu == x*hist[x]
        assert Fraction(zeros, graphs) == q
        assert Fraction(total_D, graphs) == var/mu
        assert Fraction(total_abs, graphs) == epsilon
        variances.append(var)
        epsilons.append(epsilon)
        max_marginal_slack = 0.0
        for z in (-3.0, -1.0, -.1, 0.0, .1, .5, 1.0, 2.0, 3.0):
            psi = sum(c*cmath.exp(1j*z*(x-float(mu))/math.sqrt(float(mu)))
                      for x,c in hist.items())/graphs
            lhs = abs(psi-math.exp(-z*z/2))
            bound = z*z*float(epsilon)/2+abs(z)**3/(6*math.sqrt(float(mu)))
            assert lhs <= bound+2e-13
            max_marginal_slack = max(max_marginal_slack, bound-lhs)
        forcing.append({'j': j, 'mean': str(mu), 'variance': str(var),
                        'P_D_zero': str(q), 'E_D': str(Fraction(total_D,graphs)),
                        'E_abs_D_minus_one': str(Fraction(total_abs,graphs)),
                        'size_bias_checked_for_entire_distribution': True,
                        'largest_marginal_CF_slack': max_marginal_slack})

    joint_checks = []
    for a,b in ((1,0),(2,1)):
        joint = Counter((row[a],row[b]) for row in counts)
        ma,mb = means[a],means[b]
        cov = Fraction(sum(x*y*c for (x,y),c in joint.items()),graphs)-ma*mb
        maxa,maxb = max(histograms[a]),max(histograms[b])
        kernel_sum = 0
        min_kernel = None
        for x in range(maxa):
            for y in range(maxb):
                pa = sum(c for v,c in histograms[a].items() if v>x)
                pb = sum(c for v,c in histograms[b].items() if v>y)
                pab = sum(c for (v,w),c in joint.items() if v>x and w>y)
                H_numerator = pab*graphs-pa*pb
                assert H_numerator >= 0
                kernel_sum += H_numerator
                min_kernel = H_numerator if min_kernel is None else min(min_kernel,H_numerator)
        assert Fraction(kernel_sum,graphs**2) == cov
        scalea,scaleb = math.sqrt(float(ma)),math.sqrt(float(mb))
        cn = float(cov)/(scalea*scaleb)
        tested = 0
        max_dependence_ratio = 0.0
        for s in (-3.0,-1.0,-.1,0.0,.1,.5,2.0):
            for t in (-3.0,-1.0,-.1,0.0,.1,.5,2.0):
                pa = sum(c*cmath.exp(1j*s*(x-float(ma))/scalea)
                         for x,c in histograms[a].items())/graphs
                pb = sum(c*cmath.exp(1j*t*(y-float(mb))/scaleb)
                         for y,c in histograms[b].items())/graphs
                phi = sum(c*cmath.exp(1j*(s*(x-float(ma))/scalea+t*(y-float(mb))/scaleb))
                          for (x,y),c in joint.items())/graphs
                dependence_bound = abs(s*t)*cn
                assert abs(phi-pa*pb) <= dependence_bound+2e-13
                if dependence_bound:
                    max_dependence_ratio = max(max_dependence_ratio,abs(phi-pa*pb)/dependence_bound)
                full_bound = (dependence_bound+(s*s*float(epsilons[a])+t*t*float(epsilons[b]))/2
                              +abs(s)**3/(6*scalea)+abs(t)**3/(6*scaleb))
                assert abs(phi-math.exp(-(s*s+t*t)/2)) <= full_bound+2e-13
                tested += 1
        joint_checks.append({'K':sizes[a], 'l':sizes[b], 'covariance':str(cov),
                             'kernel_integral':str(Fraction(kernel_sum,graphs**2)),
                             'minimum_kernel_numerator':min_kernel,
                             'CF_argument_pairs_checked':tested,
                             'largest_dependence_error_over_bound':max_dependence_ratio})
    return {'n':n,'graphs':graphs,'forcing_checks':forcing,'joint_checks':joint_checks}


rows = [audit(5), audit(6)]
result = {'status':'all forcing, kernel and CF checks passed',
          'nice':os.getpriority(os.PRIO_PROCESS,0), 'rows':rows,
          'elapsed_seconds':time.monotonic()-started,
          'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('joint_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
