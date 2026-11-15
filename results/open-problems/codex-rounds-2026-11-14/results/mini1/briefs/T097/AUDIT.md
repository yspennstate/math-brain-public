# Checks and attempted failures

## Gaussian shift sign and constant

PROOF.md sections 2 and 3 derive the comparison separately: differentiation
and first-moment rearrangement, then likelihood-ratio minimization. Both give
the displacement `-t sqrt(cap(K))` when the level increases by t. For a
single site with variance g(0,0), cap({0})=1/g(0,0); the formula becomes
the exact identity for a one-dimensional Gaussian tail. A reversed sign
would already fail this check. For t=0 both inequalities are equalities.

## Independent energy calculation

The first derivation uses sums of odd squares. Expanding instead gives

    sum_{k=R}^{2R-1} k = (3R^2-R)/2,
    sum_{k=R}^{2R-1} k^2 = (14R^3-9R^2+R)/6,
    sum_{k=R}^{2R-1} (4k^2+4k+1) = (28R^3-R)/3.

Dividing by R^2 reproduces `(28R-1/R)/3`. Direct small cases:

    R=1: 3^2 = 9; formula (28-1)/3 = 9.
    R=2: (5^2+7^2)/4 = 74/4 = 37/2;
         formula (56-1/2)/3 = 37/2.

These are exact hand calculations, not claimed computer outputs. A second
normalization check expands the unordered-edge energy: every vertex has
six incident edges, so `(1/6) sum_edges (f_x-f_y)^2` has coefficient one
on sum f_x^2 and coefficient -1/3 on sum_edges f_x f_y, agreeing with
`f^T(I-P)f`. Thus capacity has the simple-random-walk normalization used
by the covariance, not an unmentioned factor of six.

## Independent exponent check using Hölder rather than normal tails

Let P=N(0,G), Q=N(-t1,G), D be fixed, p=P(D), q=Q(D), and
s=t sqrt(1^T G^{-1}1). Under Q the likelihood L=dP/dQ satisfies

    E_Q L^r = exp(r(r-1)s^2/2), r>1.

This follows directly by writing the log likelihood as `sZ-s^2/2` under Q,
where Z is standard normal. Hölder then gives

    p <= q^{(r-1)/r} exp((r-1)s^2/2),
    q >= p^{r/(r-1)} exp(-r s^2/2).

Write A=log(1/p)>0 and choose r=1+sqrt(A). The result is

    -log q <= A + sqrt(A) + (s^2/2)(1+sqrt(A)).

For t=R^{-1/2}, s^2<=28/3, so a lower bound p>=c R^{-b} gives
`-log q <= b log R + O(sqrt(log R))`. This independently reproduces
both beta/2 in the conditional constraint and q/2 from the existing density
bound. In particular q>4, not q>=4, is the external theorem; letting
q decrease to 4 yields the limsup bound 2 but not `p_R >= c R^{-2}`.

## Checks on the crossover scale

Insert `R=c t^{-2}/log(1/t)` directly in (17). The three losses are

    Ct^2R/2 = Cc/(2 log(1/t)),
    t sqrt(CR) sqrt(6 log R) <= sqrt(12 Cc),
    2t sqrt(CR) = 2 sqrt(Cc/log(1/t)).

The first and third vanish, and the middle term can be made smaller than
log 2 by choosing c small. In contrast, setting R=c t^{-2} makes the
middle term grow as sqrt(log(1/t)); this method does not prove the stronger
constant-factor bound `L_rel >= c t^{-2}`. No numerical approximation to
log 2 or sqrt(12) is needed: with Cc=10^{-6}, the limiting middle term is
less than 4/1000, whereas log 2>1/2.

The set defining L_rel need not be an interval in R. The proof checks every
integer radius up to the claimed bound; it does not infer monotonicity of
the ratio from monotonicity of either numerator or denominator. Small R
are covered separately by continuity and positivity of finite-dimensional
Gaussian connection probabilities. The minimum is finite by the cited
subcritical theorem and the proved polynomial lower bound on the denominator.

## Cases deliberately not inferred

- Critical percolation is not ruled out. If theta(h_*)>0, a zero one-arm
  exponent remains compatible with every inequality here.
- The connection event is measurable on B_R; reaching the boundary uses a
  first-hit path, so no field outside that box is silently exposed.
- Half-space equality proves optimality among all increasing events on K,
  not optimality for the specific one-arm event. That distinction leaves
  room for better percolation-specific estimates.
- A relative one-arm radius is not identified with a two-point correlation
  length. Such an equivalence would need a separate argument.
- Cable clusters at height zero are not lattice clusters at h_*>0. No
  transfer of arm probabilities or exponents is used.
- The results are standard Gaussian consequences, possibly already recorded
  elsewhere. The limited literature check does not establish novelty.

No numerical experiment was needed or run. The sandbox denied `nice` priority
changes during read-only orientation, so no computation relying on a claimed
low scheduling priority was attempted.
