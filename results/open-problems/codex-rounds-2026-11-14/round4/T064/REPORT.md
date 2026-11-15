VERDICT: PROVED sharper crossing-stability bound with saddle-only interior counts and optimal corner coefficient

The preceding finite-scale bound holds. Its complete script was rerun,
and its Gaussian expectations and height integrals were independently
checked using different quadrature. No solution of the Cardy/SLE(6)
conjecture was found in the five-minute literature check.

New beyond round 3: classify the local types that can be a crossing
threshold, and count only those. Interior extrema are excluded. On
vertical edges only tangential maxima with positive inward derivative
are eligible; on horizontal edges only tangential minima with negative
inward derivative are eligible. Each corner has just one eligible
gradient quadrant. These necessary conditions give a strictly sharper
bound for every finite level interval.

For Q=[0,L]x[0,H], A=LH, P=2(L+H), and ordinary superlevel crossing
probability p_Q, the new result is

    0 <= p_Q(a)-p_Q(b) <= integral_a^b D_Q(t) dt,  a<b,

    D_Q(t) = A phi(t) exp(-t^2)/(4 pi)
             + P beta(t)/4
             + (H-L)t phi(t)/(4 sqrt(pi)) + phi(t),

where phi is the standard normal density and

    beta(t) = phi(t)exp(-t^2)/(2 pi)
              + t phi(t)erf(t)/(2 sqrt(pi)).

The edge term is nonnegative despite its signed representation.
The corner coefficient drops from 4 to 1, and 1 is optimal among
interval bounds of this form with fixed area and perimeter densities:
shrinking rectangles have thresholds converging to the field at a point.

For a square the small-|u| bound becomes

    |p_[0,R]^2(u)-1/2|
      <= phi(0)[R^2/(4 pi) + R/(2 pi) + 1]|u|
         + O((R^2+R+1)|u|^3).

The leading edge and corner terms are each divided by four. Removing
extrema saves order R^2|u|^5 near zero and does not change the leading
area term. Thus the sufficient level window remains o(R^(-2)).
PROOF.md contains the full interval bound, closed-form integrals,
local path arguments, orientation check and corner sharpness proof.
This is a derived lemma; no claim of literature priority is made.

Commands:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T064/check_level_stability.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_local_threshold.py
```

Both passed. The new audit used 13.19 MiB peak RSS and 0.178 seconds
on its first run, with actual niceness 20. It checked direct conditional
Gaussian integrals, 24 interval comparisons, 644 pointwise comparisons,
eight edge normal-form examples and four affine corner cases. Exact
commands and output are in LOG.md. Numerical checks audit the algebra
and signs; the proof does not depend on them.

The topological inputs are genericity and the strict threshold crossing
path in Lemma 2.9 and Lemma B.4 of Stephen Muirhead, Alejandro Rivera
and Hugo Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), which was opened.

What failed or remains uncertain: no attempt here supplies a conditional
macroscopic four-arm bound. Local eligibility overcounts globally
nonpivotal saddles; there is no new large-scale crossing theorem, RSW
bound or conformal limit. Literature priority was not established.
The shell's nice command reports a priority-change warning, but both
scripts independently verified inherited niceness 20. No numerical
check failed. Only this folder was changed; no git or external writes.

Next worker: insert global pivotality into the eligible-point Kac–Rice
count. Seek a quantitative bound on determinant-weighted four-arm
probabilities under the field conditioned on f(x)=t, grad f(x)=0,
uniformly for small t and points far from the boundary. The analogous
boundary estimates should start with the one-sided signs proved here.
An estimate that decays with the distance to the sides is needed to
reduce the area contribution and enlarge the level window.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 04:33 Asia/Tbilisi.
