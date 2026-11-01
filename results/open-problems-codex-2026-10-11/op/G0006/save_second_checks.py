from pathlib import Path
from fractions import Fraction
import json, math
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8')
s=s.replace('because the stationary law is unique and the zero eigenvalue of a finite Markov generator with one recurrent class is simple.', 'as follows: for lambda>0 the connected finite chain is irreducible (recover to empty, infect successively from its boundary to fill the domain, then recover unwanted sites). Its stationary nullspace is one-dimensional. At lambda=0 the generator is triangular when ordered by occupancy count, with eigenvalues minus the counts and exactly one zero, again giving an invertible normalized system.')
s+='''

## Lemma 9: the certificate is nonvacuous below the branching threshold

If 0<lambda<1/k, put a=k*lambda<1. Then

    b_L(lambda) <= L^d * a^(2L+1)/(1-a).

In particular it passes Theorem 6 for all sufficiently large L. At d=2, lambda=1/8 and L=25, the bound is 625/4^25 < 1/3^25, so this is an explicit rigorously passing subcritical certificate. It is a sanity-check special case, not the target gap.

Proof. For a vertex x in D let r_x be its stationary occupied probability, and let e_x be its number of outside neighbors. Stationarity gives

    r_x = lambda*E[(1-eta_x)*(sum_{y in D,y~x}eta_y+e_x)]
        <= lambda*sum_{y in D,y~x} r_y + lambda*e_x.

Let A be the nonnegative internal adjacency matrix. Its maximum row sum is at most k. Iterating the componentwise inequality yields

    r <= sum_{j=0}^{n-1}(lambda*A)^j*lambda*e + (lambda*A)^n*r.

Since r<=1 and k*lambda<1, the last term is bounded by a^n and vanishes. Each term in the series counts walks that stay inside D until their final exit, weighted by lambda to the walk length. For x in C any exit walk has length at least 2L+1. There are at most k^n length-n walks, so r_x <= sum_{n>=2L+1} a^n = a^(2L+1)/(1-a). The crossing event requires at least one occupied vertex of C. Union over its L^d vertices proves the bound. Since a<1, polynomial L^d times a^(2L+1) tends to zero, establishing eventual passage. At lambda=0 the crossing probability is zero directly. QED.

This estimate ceases to give a finite bound when k*lambda>=1. It supplies no control at the actual survival critical rate and therefore does not complete Theorem 8's condition.

## Exact three-site result saved

At lambda=1/4 the eight stationary probabilities, ordered by binary occupancy states 0 through 7, are

    (394304/507375, 9824/56375, 8464/507375, 2252/101475,
     1696/507375, 76/56375, 1436/507375, 223/101475).

They are positive, sum to one, and satisfy all eight rational generator balance equations. States 6 and 7 have the last two sites occupied, with total probability 2551/507375. This is strictly greater than 1/847288609443 = 3^(-25). Graphical monotonicity extends the lower bound to every lambda>=1/4. Since lambda_c(Z^2)>=1/4, no L=1 buffered certificate can pass at or above lambda_c. This is a proof about L=1 only; it leaves every larger scale undecided.

SecondChecks.lean checks normalization, positivity, all eight generator balance equations, the exact joint probability and its strict threshold comparison, using decide +kernel. The generated equations are checked against the independently constructed Fraction generator in generate_second_lean.py. See second_lean_check.txt for the actual Lean result. This does not formalize the infinite-volume coupling, the sharpness theorem, or the block proof.
'''
p.write_text(s,encoding='utf8')
left=625*3**25;right=4**25
assert left<right
checks={'subcritical_certificate':{'d':2,'lambda':'1/8','L':25,'upper_bound':'625/4^25','threshold':'1/3^25','cross_mult_left':left,'cross_mult_right':right,'passes':True},'zero_hits_40_95_upper':1-.05**(1/40),'required_threshold':3.**(-25),'zero_hit_trials_for_95_threshold':math.ceil(math.log(.05)/math.log1p(-3.**(-25)))}
Path('second_exact_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8');print(json.dumps(checks))
