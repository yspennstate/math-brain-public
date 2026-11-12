# Identification attacks on the limiting laws (2026-08-24 session)

All computations exact rational arithmetic; moments from Theorem 11.1 plus
the new m_16(gamma_H) = 9179819/840 computed this session (reduced-core
route; independent direct sweep in progress).

## Refutations (each a small theorem)

1. gamma_T is NOT a scale mixture of Gaussians. If X = sqrt(V) Z then
   m_4 = 3 E[V^2] >= 3 (E V)^2 = 3 m_2^2 = 3; but m_4 = 8/3 < 3. The same
   one-line argument kills gamma_H (m_4 = 2 < 3). Both laws are strictly
   sub-Gaussian at fourth order; no symbol-averaging / conditional-variance
   heuristic representation can be exact.

2. gamma_H is NOT a scale mixture of semicircle laws. s_k = m_2k/Cat_k
   would be the mixing moments; s_1 = s_2 = 1 forces V degenerate at 1
   (Cauchy-Schwarz equality), i.e. gamma_H = semicircle, contradicted at
   m_6 (11/2 vs 5). Formally the Hankel minor D_2 = -1/100 < 0. Consistent
   with the known non-unimodality of gamma_H (a scale mixture of
   semicircles is unimodal).

3. Neither law is a q-Gaussian (Bozejko-Speicher). m_4 = 2 + q pins
   q_T = 2/3, but then m_6 would be 287/27 != 11; m_4(gamma_H) = 2 pins
   q_H = 0 (free/semicircle), but m_6 = 11/2 != 5.

## The surviving conjecture

gamma_T IS consistent, through all fourteen available moment orders, with
being a scale mixture of semicircle laws:

    gamma_T = law of sqrt(V) * S,  S standard semicircle, V >= 0,
    E[V^k] = m_2k(gamma_T)/Cat_k
           = 1, 4/3, 11/5, 454/105, 415/42, 5960/231, 108573/1430, ...

Stieltjes moment test (both Hankel matrices) passes with strictly positive
minors:

    H0: 1, 1/3, 461/4725, 12041459/254677500
    H1: 1, 19/45, 64489/330750, 274935633677/1529593065000

Strict positivity means the evidence is nondegenerate at every available
order (a finite atomic mixing law would zero a minor). Negative controls:
the identical test refutes gamma_H at the second minor and the Gaussian
variants at the first, so the test has teeth on sequences of this shape.

Equivalent generating-function form, via Theorem 6.4 of the paper: the
moment series satisfies M_T(z) = E[C(Vz)] with C the Catalan generating
function, so the paper's inverse transform

    K_T(u) = ((1-u)/(1+u)) [ E[C(V u/(1+u)^2)] - (1+u) ]

turns the primitive-mass sequence kappa_r^T into an exact functional of the
mixing law. Identifying V identifies gamma_T.

Consequences if true: gamma_T is unimodal (open question, believed true
from plots); the density is a superposition of semicircle edges, explaining
smoothness; and the free-probability structure of gamma_T reduces to the
classical moment problem for V. The mixing moments grow like a Gamma-type
law: Gamma(shape 3, scale 1/3) matches E[V] and E[V^2] exactly and misses
E[V^3] by 1 percent (20/9 vs 11/5) - V is Gamma-like but not Gamma.

Order-22 update (extension moment tables, verified this session): the
conjecture SURVIVES through order 22 - all six H0 minors and all six H1
minors strictly positive with s_8..s_11 = 56067533/225225,
3065263961/3403400, 17293570111/4849845, 298983373961/19492200. Twelve
moment orders of evidence, none degenerate.

## Jacobi (three-term recurrence) data, exact

gamma_T: b_k^2 = 1, 5/3, 7/3, 529/175, 14958/4025, 252766/57339,
295624148135/57973398696, and with the extension moments the sequence
continues through b_11^2 = 7.85799. The first three are exactly (2k+1)/3;
the increments peak at 0.69342 (k=4) and then decrease MONOTONICALLY:
0.69200, 0.69103, 0.69046, 0.68979, 0.68939, 0.68905 - descending straight
toward the squared Sen-Virag operator-norm constant 0.68707.

Conjecture (with mechanism): b_k^2 ~ c k with c = rho_SV^2. The increment
limit c is the Gaussian-tail variance of gamma_T (for laws with
exp(-x^2/2c) tails, the Jacobi coefficients satisfy b_k^2 ~ ck), and the
extreme eigenvalues of the n-sample then grow like sqrt(2c log n) - which
is exactly the Sen-Virag norm asymptotic rho sqrt(2n log n) after the
n^{-1/2} normalization, forcing sqrt(c) = rho. So the conjecture is
equivalent to: the limiting law's Gaussian tail variance equals the
squared norm constant - possibly provable from the known tail estimates
for gamma_T plus standard orthogonal-polynomial asymptotics.

gamma_H: b_k^2 = 1, 1, 3/2, 149/90, 14452/6705, 2526641/1076674,
621050847457/219090094392, 1789840863641094203/589756120262400728. The
increments alternate (~0.5, ~0.16-0.20 repeating): the structural variable
is the x^2-pushforward. Its own Jacobi parameters (computed from the new
m_16) fit no classical family: a_k = 1, 5/2, 3407/894, ...; b_k^2 = 1,
149/60, 5053282/999045, ... - linear-ish a_k at slope ~1.35, quadratic-ish
b_k^2 at ~0.54 k^2 (exponential law would need slope 2 and k^2 exactly).

## Holonomy / algebraicity: excluded at small size

Guess-and-verify with a held-out moment: every small algebraic ansatz
P(z, M) = 0 (bidegrees through (4,4) with at most 16 coefficients) and
every small holonomic ansatz (order <= 3, polynomial degree <= 4) that is
uniquely determined by the moments through order 14 PREDICTS the next
moment; for gamma_H the two uniquely-determined ansatzes predict 10894.88
and 10866.32 against the true 10928.356 - both wrong. So neither
generating function satisfies a small algebraic or differential equation.
This matches, independently, the extension audit's finding that the
volume-weighted moment and primitive series are nonalgebraic (their
route: a D-finite fit that failed a Wick check at order 24).

## The unified decay conjecture (three constants are one)

Write c_k = m_2k/(2k-1)!! = E_pi[p_T(pi)] for the mean pairing-polytope
volume (equivalently: the corridor-survival probability of the matched
walk over a uniformly random pairing). Exact data through order 22:

  c_k: 1, .8889, .7333, .5765, .4392, .3276, .2410, .1756, .1271, .0915, .0656
  ratios c_{k+1}/c_k: .8889, .8250, .7861, .7617, .7460, .7357, .7286,
                      .7236, .7198, .7169   (monotone decreasing)
  Richardson (L + a/k): hovers 0.683-0.691 around rho_SV^2 = 0.68707

Conjecture (unified): the three limits coincide -

  lim c_{k+1}/c_k  =  lim (b_{k+1}^2 - b_k^2)  =  rho_SV^2,

i.e. the geometric decay rate of the mean polytope volume, the Jacobi
increment of gamma_T, and the squared Sen-Virag operator-norm constant are
the same number. The first equality is classical orthogonal-polynomial
folklore for Gaussian-tailed laws (both express the tail variance); the
content is the second. Proof route: E_pi[p(pi)] is a single analytic
object - the survival probability of an exchangeable matched walk in the
corridor - and the dihedral reflection series converts each p(pi) into an
alternating sum of free-space box-spline values whose pairing-sums have
Gaussian (Isserlis) structure; matching the resulting rate against the
Sen-Virag variational formula for rho is the concrete remaining step.
Localized refinement (CORRECTED AND COMPLETE): section profiles are NOT
dihedral invariant at fixed x (rotations move the basepoint: abcbca has
constant profile 2/3, its rotation ababcc has the parabola), so the
first per-x computations, done over orbit representatives, were wrong
from k = 3 on; global volumes are rotation invariant so nothing else was
affected. The per-word recomputation (localized_perword.py, complete
through k = 5) gives:

  x = 0:   t_k = 1, 1, 5/4, 19/10, 1157/336, 36901/5040
  x = 1/4: t_k = 1, 1, 43/32, 179/80, 190639/43008, 6575123/645120
  x = 1/2: t_k = 1, 1, 11/8, 47/20, 12823/2688, 451883/40320

and ALL Stieltjes minors (H0 and H1) are strictly positive at all three
x - the localized mixture conjecture survives its own correction at
every tested point. The floor-section integers k! F_k(0) = 1, 5, 57,
1157, 36901 (per-word, exact; no consecutive OEIS match found) are a
combinatorial statistic refining the matching count: e(pi) = k! f_pi(0)
with e = 1 on cube cycles times k!/r, multiplicative over concatenation,
and equal to k! p(inner) on single-pair nestings.

## The primitive-mass asymptotics (open problem 2): a sharp conjectural answer

The binomial transform c_k = sum_r C(2k,k-r) kappa_r / (2k-1)!! is
boundary-local: with kappa_r ~ r! gamma^r the term ratio
[(k-r)/(k+r+1)](r+1)gamma peaks at fixed distance ~2/gamma from r = k
(the exact shares confirm this: the r = k term carries a stable ~21
percent and the top two ~52 percent at k = 8).  Boundary-local dominance
gives c_{k+1}/c_k -> gamma/2, so the mean-volume decay conjecture
(ratio -> rho_SV^2) is EQUIVALENT to

    kappa_{r+1} / ((r+1) kappa_r)  ->  2 rho_SV^2  =  1.37414.

The exact data: 1.4833, 1.4213, 1.4002, 1.3899, 1.3844 (through the new
kappa_8 = 687080/9), with geometrically halving decrements extrapolating
to 1.3734 - agreement with 2 rho^2 to under 1e-3.  So the conjectural
answer to the paper's primitive-volume asymptotics problem is

    kappa_r^T  ~  r! (2 rho_SV^2)^r  x subexponential factors,

one constant, tied to the operator norm.  The same analysis on the Hankel
side (ratios/(r+1): 0.992, 0.760, 0.764, 0.746 at r = 7) predicts a
Hankel analogue of the Sen-Virag constant near sqrt(0.746/2) ~ 0.61 - a
new falsifiable prediction, since no exact Hankel norm constant is in the
literature to our knowledge.

## The cluster equation and the Borel form of the unified conjecture

Every linear double-occurrence word factors uniquely into indecomposables;
indecomposables are nested (profile flattens to a moment, by the profile
calculus) or crossing-type. This gives the exact system

    F(z;x) = 1 / (1 - z M(z) - J(z;x)),      M(z) = int_0^1 F(z;x) dx,

with J the crossing-indecomposable profile series - verified exactly
through k = 4 at x = 1/2 (J_k by series inversion equals the direct
enumeration: 0, 3/4, 55/12, 6139/192). With J = 0 this is the Catalan
equation, so J is precisely the crossing correction to the semicircle
law. J itself expands over gap-irreducible atoms with gaps refilled by
F at the gap positions (the paper's ear inflation generalized to a full
renormalized expansion; the gap-marginal lemma is the first moment of
this structure). The localized mixture conjecture is equivalent to
F(z;x) = E_{mu_x}[C(Vz)] termwise.

Since m_2k ~ (2k-1)!! rho^{2k}, the moment series is factorially
divergent and the honest analytic object is the Borel transform. The
unified conjecture takes its cleanest form there:

    sum_k m_2k(gamma_T) zeta^k / k!   has radius  1/(2 rho_SV^2),
    equivalently sum_r kappa_r^T zeta^r / r! has radius 1/(2 rho_SV^2),

one statement packaging the mean-volume decay, the Jacobi increment, and
the kappa growth. The resurgence/Borel singularity structure of the
cluster equation is the natural machinery for attacking it.

## Density test against simulated matrices (independent data path)

The mixture conjecture predicts the whole density of gamma_T as a
superposition of semicircles, f(t) = E[sqrt(4V - t^2)_+ / (2 pi V)].
density_falsification.py builds V by Gauss quadrature from the exact
s_k, predicts f, and compares against eigenvalues of REAL simulated
random symmetric Toeplitz matrices (6 x 700, no moments or polytopes in
that path). Result on the bulk t in [0, 1.5]:

    t      predicted   simulated
    0.00   0.3672      0.3857
    0.50   0.3453      0.3369
    1.00   0.2581      0.2591
    1.50   0.1552      0.1397

- agreement within about 10 percent, which is the size of the finite-n
error at n = 700 (the simulated m_4 is 2.724 against the exact 2.667).
The conjecture SURVIVES this independent test where the test is valid.

The first run flagged a 50 percent deviation at t = 2.0 as a possible
refutation. That flag was MY artifact, not the law: the quadrature
prediction itself moves 23 to 280 percent between 5 and 6 nodes for
t >= 1.75, because a finite atomic approximant has spurious edges at
2 sqrt(V_i). The test is therefore uninformative in the tail and the
flag is withdrawn. Discriminating in the tail needs either a genuine
Abel/Stieltjes inversion of the simulated density or far larger n.

## Portrait of the mixing law mu_V (what we are hunting)

Gauss quadrature from the eleven exact mixing moments: unimodal, mode near
0.85, mean exactly 1, variance exactly 1/3, positive support reaching ~6
at the sixth node with weights collapsing super-geometrically.  The
s-ratio data s_{k+1}/((k+1) s_k) = 0.410, 0.402, 0.396, 0.391 descends
toward rho^2/2 = 0.34353, i.e. E[V^k] ~ k! (rho^2/2)^k: V has an
EXPONENTIAL right tail with rate exactly 2/rho^2 = 2.9110, which chains
back to m_2k ~ (2k-1)!! rho^{2k} - the same unified constant a third way.
Sharp non-Gamma fingerprint: a Gamma law with mean 1 has variance equal
to its tail scale; here Var(V) = 1/3 exactly (from kappa_2 = 2/3) while
the tail scale is rho^2/2 = 0.34353.  The 3 percent gap is structural:
mu_V is a genuinely new law, Gamma-like at the level of two moments and
provably not Gamma at the third.  Localized version at x = 1/2: the
two-point quadrature of mu_{1/2} is {0.63 (weight 0.73), 2.01 (0.27)}.

## Why V resists identification: it is a boundary-layer object

Write the mixing moments through the Catalan transform:

  s_k = 1 + sum_{r>=2} [C(2k,k-r)/Cat_k] kappa_r,
  C(2k,k-r)/Cat_k = (k+1) * Gamma(k+1)/Gamma(k+r+1) * Gamma(k+1)/Gamma(k-r+1).

The first Gamma ratio is a Beta moment,
Gamma(k+1)/Gamma(k+r+1) = (1/Gamma(r)) int_0^1 x^k (1-x)^{r-1} dx, so each
FIXED-r term carries a representation as a moment against a measure on
[0,1] (after integrating the falling factorial by parts). A mixing law
built from fixed-r terms alone would therefore be supported in [0,1] and
have bounded moments. But s_k grows like k!(rho^2/2)^k, so V has
unbounded support with an exponential tail - the growth cannot come from
the bulk.

Measured: the share of s_k contributed by r > k/2 is

  k=4: 0.460   k=5: 0.706   k=6: 0.735   k=7: 0.884   k=8: 0.896

and the empty-core (semicircle) share collapses from 0.231 to 0.004.
So V is essentially a BOUNDARY-LAYER object: its law is determined by the
cores whose size is comparable to k, not by any fixed-size structure.
That is the concrete reason the identification is hard - every
finite-order expansion sees the wrong part of the transform - and it is
why the analysis has to be done on the Borel/exponential scale, where
the boundary layer becomes the singularity nearest the origin.

Necessary conditions all pass: log-convexity s_k s_{k+2} >= s_{k+1}^2
holds at every available k, with the ratio decreasing monotonically
1.3333, 1.2375, 1.1911, ..., 1.0865 toward 1 as a genuine moment
sequence should.

CONSEQUENCE - the two open problems are one. Push the boundary-layer
analysis to leading order. Writing r = k - j and using kappa_r ~ r!
gamma^r, the ratio of consecutive boundary terms is

  term_{j+1}/term_j  ~  2 / (gamma (j+1)),

so the boundary sum is Poisson-like with parameter 2/gamma and

  s_k  ~  (kappa_k / Cat_k) * exp(2/gamma) = (kappa_k/Cat_k) * exp(1/rho^2),

using gamma = 2 rho^2. So the mixing law's moments ARE the primitive
masses, up to the Catalan normalization and one explicit constant.
Identifying V is therefore the same problem as the paper's second open
problem (primitive-volume asymptotics), not a different one.

Measured check: s_k Cat_k / kappa_k for k = 2..8 is 4.0000, 5.5000,
5.1011, 4.9209, 4.8068, 4.7252, 4.6630 - decreasing monotonically, with
first-order Richardson extrapolation landing at 4.20, 4.236, 4.235,
4.228 against the predicted exp(1/rho^2) = 4.2864. Agreement to about
1.4 percent. CAVEAT, stated plainly: that is an extrapolation from
k <= 8 assuming a 1/k correction, so it is a consistency check and not a
measurement of the limit; the honest content is that an independently
derived constant lands inside the extrapolation's own spread.

## Status of the famous identification problem

Not solved here. The refutations close off the natural mixture and
q-deformation routes for gamma_H entirely; for gamma_T everything now
points at the mixing law V, which is a strictly harder-to-fake target than
the raw moments. The two conjectures above (semicircle mixture; Sen-Virag
slope) are, as far as we know, new.
