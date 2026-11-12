# Notes on the margin extension

Working notes for extending the zero-margin capacity result of
ising-perceptron-capacity to constraints `<g_a, x>/sqrt(N) >= kappa`.
Status labels are load-bearing here: **certified** means ball arithmetic
over the full stated parameter rectangle; **high-precision** means mpmath
continuation (dps 20-30), nonrigorous; **float** means vectorized float64
scans.

## 1. The system at general kappa

Ding-Sun sections 7-9 treat kappa = 0; Huang's Theorem "Main result,
general kappa" (his Section 3) upper-bounds the capacity by
alpha_*(kappa) for every kappa, conditional on four numerical conditions.
With M(x) = phi(x)/Psi(x) the inverse Mills ratio and

    u(z; q, kappa) = (kappa - sqrt(q) z) / sqrt(1 - q),

the RS system is

    P(psi)          = E tanh^2(sqrt(psi) Z)
    R(q, alpha)     = (alpha/(1-q)) E[ M(u(Z))^2 ]
    G(alpha, q, psi) = -psi(1-q)/2 + E log(2 cosh(sqrt(psi) Z))
                       + alpha E log Psi(u(Z))

with fixed point q = P(R(q)), psi = R(q), and alpha_*(kappa) the root of
G_*(alpha) = G(alpha, q_*(alpha), psi_*(alpha)).  At kappa = 0 this is
exactly the certified Block-1 system (u = -gamma z in law).  Huang's
displayed RS free energy has a sign typo on the alpha term (minus where
the fixed point requires plus); the certified kappa = 0 rectangle
reproduces only with the plus sign.

## 2. Stationarity at general kappa (lemma)

R is the q-stationarity condition of G at every kappa, not only at 0.
Two Gaussian integration-by-parts identities give, for any q, psi, kappa:

    d/dpsi G = (q - P(psi))/2,
    d/dq   G = (psi - R(q, alpha))/2.

The second is the nontrivial one.  Differentiating u in q,

    u_q = [ -z/sqrt(q) + u/sqrt(1-q) ] / (2 sqrt(1-q))
        = [ -z/sqrt(q) + (kappa - sqrt(q) z)/(1-q) ] / (2 sqrt(1-q)),

so d/dq E log Psi(u) = -E[ M(u) u_q ].  Stein's lemma on the z-part
(E[z M(u)] = -sqrt(q/(1-q)) E[M'(u)]) and the Mills identity
M' + u M = M^2 collapse the two pieces:

    E[ M(u) u_q ] = ( E[M'(u)] + E[u M(u)] ) / (2(1-q))
                  = E[ M(u)^2 ] / (2(1-q)) = R / (2 alpha).

Hence d/dq G = psi/2 - alpha (R/(2 alpha)) = (psi - R)/2.  Verified
numerically along the whole continuation (the `dG_dq` column stays at
the finite-difference noise floor, ~1e-19 at dps 30).

Consequence (envelope): along the fixed-point branch,

    d/dalpha G_*(alpha) = E log Psi(u) < 0   strictly, for every kappa,

so G_* is strictly decreasing and its root alpha_*(kappa) is unique on
the branch.  This is the kappa-general form of the monotonicity clause
in Huang's Condition km-well-defd.

## 3. Anchors at kappa = 0 (all reproduced independently)

- alpha = 0.83307859973957923, q = 0.56394908008456164,
  psi = 2.57635131907567457: inside the certified rectangle
  (Block 1 / Ding-Sun Proposition 1.3).
- Huang Condition amp-works LHS: 0.544360 against his certified bound
  0.5446.
- Huang Condition local-concavity: minimizer z0 = -0.6693157 against
  his witness -0.669316; lambda_0 = -0.19100 against his bound -0.1906.
- S_*(1, 0) = 2e-14 with optimal tilt s = 0.66034153 = sqrt(1-q_0) to
  eight digits (his lemma).
- Global S_* landscape at kappa = 0: off-center maximum -0.0016 (the
  thin Region-I margins), all rays negative, Hessian at (1,0) negative
  definite with eigenvalues (-0.224, -0.0045).

## 4. The continuation and the condition map (high-precision)

`scan_kappa.py` walks alpha_*(kappa) outward from 0 (warm-started; cold
solves above the fold escape to the frozen branch q -> 1, which is what
a naive solve at kappa = 0.5 does).  Per point it records the
contraction (P o R)'(q_*), Huang's amp-works product, lambda_0, the
stationarity residuals, and two external anchors (annealed bound
log 2 / (-log Psi(kappa)); Gardner spherical capacity).  Results in
`results/kappa_pos.csv`, `results/kappa_neg.csv`.

Measured over kappa in [-2.0, 1.5] (71 points; exact values in the
CSVs), all three per-point conditions hold everywhere:

- contraction (P o R_alpha)'(q_*): monotone increasing in kappa, 0.39
  at -2.0, 0.744 at 0, 0.903 at +1.5 - always below 1, and the only
  condition trending toward failure at large positive margin;
- amp-works: humped, maximum 0.607 near kappa = -1, decreasing on both
  flanks (0.381 at +1.5, 0.438 at -2.0);
- local-concavity lambda_0: humped, closest approach to zero -0.094
  near kappa = -1.3, then strengthening again to -0.147 at -2.0.  An
  early extrapolation from [-0.55, 0] suggested a crossing near -1.5;
  the measurement refutes it - the decay reverses.

The optimal tilt at the distinguished point matches sqrt(1 - q_0) to
eight digits at every kappa checked (0, +-0.05, +-0.25), extending
Huang's kappa = 0 lemma along the curve.  On the positive branch
alpha_*(kappa) stays below Nakajima's saddle-existence bound at all 31
points (worst ratio 0.874 at kappa = 1.5), so his uniqueness theorem
covers the whole computed positive branch.  As kappa -> -2 the
candidate approaches the annealed bound from below, as it should where
constraints trivialize.

Saddle uniqueness for kappa >= 0 below alpha_c(kappa) =
2/(pi E[(kappa - Z)_+^2]) is Nakajima's analytic theorem
(arXiv 2512.23195; formula checked against the abstract verbatim);
along the computed branch alpha_*(kappa) stays far below alpha_c(kappa),
so the uniqueness clause has an analytic proof on the positive side and
the certificates only need contraction and the crossing.

## 5. Certified slabs (ball arithmetic)

`certify_km_slab.py` proves Condition km-well-defd on kappa sub-slabs.
The first design (uniform interval evaluation of the map over the whole
alpha interval) cannot work: the fixed point itself sweeps
dq_*/dalpha ~ 0.92 across the alpha pad, and the crude contraction
bound (sup P' times sup |dR/dq| ~ 0.93, against a true 0.74) amplifies
every width by 1/(1-c).  The design that closes the budget:

  - contraction bound once over the full rectangle (0.93 < 1 suffices);
  - endpoint-inward checks of q -> P(R(q)) on alpha sub-intervals
    (existence for every alpha by the intermediate value theorem,
    uniqueness from the contraction);
  - at the two thin alpha endpoints, a certified Picard shrink locates
    the fixed point to the kappa-width floor, and the G signs resolve
    through a mean-value form whose coefficients are the near-zero
    saddle derivatives (q - P(psi))/2 and (psi - R(q))/2 - evaluating
    G naively over a (q, psi) box loses exactly that cancellation and
    inflates the enclosure by two orders of magnitude;
  - tails adapted to the shifted Mills arguments, no monotonicity
    input (Ding-Sun's Lemma 7.3; its displays carry kappa but the
    proof's reflection step is kappa = 0 only - see DS_KAPPA_AUDIT.md).

Slab seeds come from `gen_slabs.py`; the q pad must cover the
dq_*/dalpha sweep of the alpha pad (0.0035 for a 0.0015 alpha pad at
slab width 5e-4).  Precision is 80 bits deliberately: margins are
>= 1e-4, ball radii ~1e-16, and the batch must be tractable.

Numerical architecture, learned the hard way: adaptive complex
quadrature cannot resolve integrand width that comes from parameter
balls (subdividing z does not shrink it) and burns any budget to NaN;
and arb's erfc on a wide real ball in the steep region returns an
enclosure spanning zero, so phi/Psi NaNs by division.  Every
wide-parameter integral therefore goes through real-cell Riemann sums
with monotone-endpoint evaluations (M, log Psi, log 2cosh, and the
psi-monotone expectations are all monotone in the right variable, so
cell hulls come from two thin evaluations).  Thin-parameter integrals
(the inward sweep, the Picard locate) keep the adaptive path, which
passes with certified hair-thin margins.

Two mathematical byproducts of the rework.  First, integrating the
dR/dq cross term by parts collapses it entirely:

    dR/dq = alpha E[ M'(u)^2 + 2 M(u)^2 M'(u) ] / (1-q)^2,

verified against a finite difference to 1e-15; the integrand is
positive, so R is increasing in q at every kappa - the general-kappa
form of Ding-Sun's Lemma 7.3 for free.  Second, the contraction
product bound sup P' * sup |dR/dq| is scale-sensitive: over the whole
batch hull it fails (the kappa width 0.05 poisons the dR/dq enclosure
and the product-of-sups loses a factor ~2 against the true sup of the
product), but on a single slab's rectangle (kappa width 5e-4) the
identity-based dR/dq enclosure is tight enough that the product clears
1 with a few percent to spare.  The contraction is therefore certified
per slab - which is Huang's condition verbatim, since his sup runs
over the same q interval - and uniqueness needs no external input.
(An audit of every use of Condition km-well-defd in his source shows
the contraction is consumed only qualitatively, in the eps-perturbation
proposition: any value strictly below 1 suffices.  Nakajima's theorem
remains an independent cross-check on the positive side.)

## 6. Certified results

Certified span: 1680 contiguous slabs covering kappa in [-0.65, 0.19],
zero failures (results/certified_intervals.csv holds the contraction
lane's 1500 on [-0.65, 0.10] with forty global records ok;
results/certified_intervals_nak.csv holds the Nakajima lane's 180 on
[0.10, 0.19] - eight worker records, uniqueness from the certified
premise alpha_ub < alpha_c(kappa) per slab; all worker evidence under
results/box/).  Worst certified margins per batch, read from the
worker evidence (contr = 1 - contraction product, amp = 1 - amp-works,
lambda = -sup lambda(z_hat); the lambda column for batches before
neg5 is the old separated-form enclosure, so those entries are
conservative - the neg4 value 0.0081 is the old form nearly dying at
-0.35 before it did die at -0.3505; and the pos2 row's contr is the
LOCATED-interval product of the Nakajima lane, not the box product,
which is past 1 there by construction):

    batch     range               n    contr     amp   lambda
    pos3      [+0.160, +0.190]   60   0.1635  0.3958   0.1420
    pos2      [+0.100, +0.160]  120   0.1704  0.3915   0.1351
    neg7      [-0.650, -0.550]  200   0.1981  0.3494   0.0400
    neg6      [-0.550, -0.450]  200   0.1652  0.3533   0.0536
    neg5      [-0.450, -0.350]  200   0.1299  0.3579   0.0669
    neg4      [-0.350, -0.250]  200   0.0921  0.2896   0.0081
    neg3b     [-0.250, -0.150]  200   0.0515  0.2982   0.0249
    neg2ext   [-0.150, -0.100]  100   0.0879  0.3612   0.0821
    negext    [-0.100, -0.050]  100   0.0690  0.3653   0.0892
    neg       [-0.050, +0.000]  100   0.0494  0.3694   0.0961
    pos       [+0.000, +0.050]  100   0.0292  0.3733   0.1027
    posext    [+0.050, +0.100]  100   0.0083  0.3776   0.1093  The positive extension [0.05, 0.1] passed 100/100 with
the contraction margin thinning to 0.0083 at the edge; the negative
extensions [-0.1, -0.05] and [-0.15, -0.1] passed 100/100 each with
margins growing (0.106 at kappa = -0.15) - the negative direction
extends mechanically as far as batch time allows, while the positive
wall stays projected near 0.12.  The [-0.45, -0.35], [-0.55, -0.45]
and [-0.65, -0.55] batches passed 200/200 each on the corrected
lambda certificate (below), the last two launched 2-wide by the
adaptive batch runner.  The lambda
margin thins to 0.0400 at -0.65; per-slab margins for the whole strip
are in results/lambda_margin_by_kappa.csv (1580 slabs), and on the
corrected-form support ([-0.65, -0.35] and [0.10, 0.16], 680 slabs) a
linear fit reads 0.1228 + 0.1254 kappa, crossing zero near -0.98 -
a projection past the measured edge, not a finding, and doubly so
because the float lambda_0(kappa) is humped near -1.3 (the true value
strengthens again), so the enclosure-driven linear decay cannot hold
to the crossing.  Deeper extension is a measurement, not an
extrapolation.  results/lambda_margins.png plots all 1580 margins:
the correlated form is a clean line on the fit, while the separated
form shows per-batch sawteeth (each batch's hull psi-range resets the
enclosure) with the neg3b near-death at 0.008 plainly visible - the
figure is the failure post-mortem in one image.  The contraction
margin grows the other way (0.198 at -0.65).

One failed extension attempt, kept as evidence
(results/box/failed_neg3_width1e3/): [-0.25, -0.15] at DOUBLE slab
width (1e-3, a launch mistake) failed 74/100 on the inward checks with
the fixed point escaping both interval ends - at deep negative kappa
the fixed-point drift dq_*/dkappa grows (q falls ~3.4e-3 per 1e-3 of
kappa near -0.2), consuming the whole q pad.  The pad rule
generalizes: pad_q must cover the alpha-pad sweep PLUS the within-slab
kappa drift, and the latter dominates once |dq_*/dkappa| ~ 3.  The
drift is humped, not monotone: from the continuation CSV it peaks
around -0.2 and falls to ~0.2 by kappa = -0.5 (q_* flattens while the
curve steepens in alpha instead, dalpha/dkappa reaching -2.65 at
-0.55), so the drift hazard is a mid-negative phenomenon and the deep
slabs' q boxes are pad-dominated.
Standard width with pad_q = 5e-3 passes: the corrected [-0.25, -0.15] batch certified 200/200, margins still growing (the pad rule holds).

A second failed extension, kept the same way
(results/box/failed_neg5_lambda_width/): the first [-0.45, -0.35]
batch failed all 200 slabs on exactly one check, lambda(z_hat), with
every other check passing.  Not a pad problem and not the truth
failing - an enclosure-width problem with two causes.  First, the
certificate evaluated lambda's two E-terms (the hf/(1+m hf) integral
and d0) as separate Riemann sums; they nearly cancel, so the q-box
width entered twice with no correlation, and by alpha ~ 1.35 the hull
([-0.270, +0.009] around a true value near -0.14) crossed zero.
Second, the condition checks received the batch-hull psi range (0.90
wide for a deep batch) when the slab's own derived range R_slab (0.09
wide) is the sound domain - psi_* = R(q_*, alpha_*) lies in it by
construction.  The cure is the same correlated-integrand move that
fixed P and R: with t = M', A = 1-q, b = m-A,

    lambda(z_hat) = z_hat + alpha E[g],   g = b t^2 / (A (A + b t)),

where g is monotone in t for fixed (m, A) (dg/dt has the sign of b),
regular on the whole closed t in [0,1] with g(1) = b/(Am) (the old
form blew up at t -> 1 and needed a cap branch), and |g| <= |b|/(Am)
bounds the tails.  All three claims are verified symbolically (sympy,
07-14): the identity's difference simplifies to zero, g(1) - b/(Am)
to zero, and dg/dt factors to t (m-A) (2A+bt) over a positive square,
so the sign statement is exact; the closed form behind alpha_c_ball
((1+k^2) Phi + k phi) likewise reproduces sympy's own integral with
difference zero.  Boundary slab: [-0.196, -0.080]; deepest slab at
-0.45: [-0.179, -0.067]; a float evaluation of the original formula
lands inside both, and on a passing earlier slab the new midpoint lies
inside the old enclosure.  The margin decays only ~0.013 per 0.1 of
kappa, so the form has headroom well past -0.45.  Slab checks also run
~4x faster (7 s locally) with the double integral and cap branch gone.

Details of the first positive batch:

Positive strip: all 100 slabs covering kappa in [0, 0.05] PASS every
check (contiguous coverage verified by the collector; four global
records ok).  Per slab this certifies, in ball arithmetic: the
contraction sup (P o R_alpha)' < 1 on the slab rectangle, existence of
the fixed point for every alpha in the interval, the G crossing, and
Huang's amp-works and local-concavity conditions - i.e. three of his
four conditions hold verbatim on the strip, with alpha_*(kappa) pinned
to intervals of width ~3.5e-3 (results/certified_intervals_pos.csv).
The slab containing kappa = 0 contains the certified Ding-Sun value;
an independent mid-slab continuation solve lands inside its interval.
Replay: `python certify_km_slab.py <slabs_file>` for any of the ten
slab files (slabs_pos, slabs_neg, slabs_pos_ext, slabs_neg_ext,
slabs_neg2_ext, slabs_neg3b, slabs_neg4, slabs_neg5, slabs_neg6,
slabs_neg7 - all .json in the repo root; point
ISING_CAPACITY_VERIFICATION at the capacity repo's verification/
directory if it is not a sibling checkout), then
`python collect_slabs.py "results/box/result_*.json" -o out.csv` to
re-gate contiguity.  Enclosure digits vary with the FLINT build, the
PASS/FAIL verdicts do not.  Consumer-tested cold on 07-14, twice: a fresh
shallow clone plus the env var replays past_wall_0p13.py to the same
verdicts in 15 s, and the full lane certifier passes 51/51 checks on
a slab from the clone (selfcheck.py green there too).  Note the pre-fix worker outputs under
results/box/failed_*/ are excluded by the collector globs above and
kept only as evidence.

Point-tightening: `locate_alpha.py` bisects alpha_*(kappa) at a fixed
kappa on the certified G sign.  At kappa = 0.05 it gives alpha_* in
[0.780449305, 0.781324282] (width 8.7e-4, the current G-enclosure
floor; the continuation value 0.7810743 lies inside); at
kappa = -0.05, alpha_* in [0.889115939, 0.890012455] (continuation
0.8894090 inside) - a certified point on the side where uniqueness has
no analytic backup and rests on the slab contraction alone; and at
kappa = 0.0995 (the strip's thin-margin edge), alpha_* in
[0.732844501, 0.733710140] (continuation 0.733017 inside), later
deepened at the raised floors to [0.733478514, 0.733480204], width
1.69e-6 (eleven bisections, clean final sign).  The deep-negative
strip edge got the same treatment: alpha_*(-0.45) in
[1.557652103, 1.557654133], width 2.03e-6, eleven bisections
(continuation 1.557652375 inside) - the deepest certified point
interval, at alpha nearly twice the zero-margin value.

Deep pass: upgrading the wide evaluators to mean-value Riemann (the
floor decomposition put the plain-hull h-term of P_of_wide at ~1e-3,
dominating the Picard floor) drops the G enclosure at thin kappa from
~1e-4 to a few 1e-6, and the bisection reaches its tolerance instead
of straddling: alpha_*(0.05) in [0.781064523, 0.781078194], width
1.4e-5 (continuation 0.7810743 inside) - the box width the Hessian
certificate needs.

The bisection floor is measured, not guessed: a second run at tol
2.5e-6 stalls at the same width 1.37e-5 (straddle at level nine) - the
G0 quadrature at n = 4000 binds.  Raising the floors (G0 at n = 32000,
locate at n = 16000) breaks through exactly as budgeted:
alpha_*(0.05) in [0.781073068, 0.781074776], width 1.7e-6, eleven
bisections with a clean final sign (continuation 0.7810743 inside).
The Hessian certificate at this interval then RESOLVES: on located
boxes of width 3.6e-6 (q) and 5.2e-5 (psi), M11 < 0 and det M > 0
both certify - the fixed-tilt local maximality at the distinguished
point, the center piece of the two-variable condition, holds in ball
arithmetic at kappa = 0.05 (results/cert_hessian_0p05.log; and at
kappa = 0 on the DS rectangle, where it independently re-verifies
Huang's certified claim).  The same chain run at kappa = -0.05
(deep interval [0.889408032, 0.889409783], width 1.75e-6) also
certifies (results/cert_hessian_n0p05.log), and so does the strip's
thin-margin edge kappa = 0.0995 (deep interval
[0.733478514, 0.733480204], width 1.69e-6, n_loc = 32000;
results/cert_hessian_0p0995.log), and the deep-negative edge
kappa = -0.45 (deep interval [1.557652103, 1.557654133]; boxes
2.1e-6 in q, 1.7e-5 in psi; M11 = -0.065 +- 5e-4 < 0, det M > 0;
results/cert_hessian_n0p45.log) - five margins now carry the center
certificate: kappa = 0 on the DS rectangle, both signs at 0.05, and
both strip edges, two of them on the side with no analytic uniqueness
backup.  The -0.45 constants sit far from their zero-margin values
(C1 = -0.855 vs -0.718, C3 = 0.883 vs 1.144), so the certificate is
exercising genuinely shifted territory, not a perturbation of the
kappa = 0 point.

cert_hessian.py then certifies the fixed-tilt local maximality in ball
arithmetic.  At kappa = 0, on the Ding-Sun rectangle itself: M11 < 0
and det M > 0 both resolve, with C enclosures ([-0.7178 +- 1.8e-5],
[5.0501 +- 5.8e-5], [1.144 +- 2.5e-4]) landing inside Huang's
certified intervals - an independent arb re-verification of his
Claim on the M-matrix, through the general-kappa formulas.  The
near-cancellations that defeated the first attempt ((1 - 4q + 3p4)
and q - p4 as differences of independent balls) are evaluated as
single correlated integrands, and the five constraint-side integrals
run mean-value Riemann with elementary Mills-family derivatives.  Tightening to
the ~1e-5 the Hessian certificate needs means shrinking the G
enclosure: finer Riemann grids and deeper located boxes at thin kappa.
Negative strip: all 100 slabs covering [-0.05, 0] PASS the same checks
(contiguous, four global records ok;
results/certified_intervals_neg.csv), so the certified statement holds
on the full strip kappa in [-0.05, 0.05].  On the negative side
uniqueness rests on our own contraction certificates alone (Nakajima's
theorem is kappa >= 0); the margins there GROW as kappa decreases.
The per-slab contraction margins (1 - c: 0.049 at kappa = 0, 0.029 at
0.05) put the product bound's saturation near kappa ~ 0.12 - the
positive-side wall of this certificate design, well before the true
contraction approaches 1.

Past the positive wall, a design (built the same night, below): the
0.12 wall belongs to the rectangle product bound sup P' x sup dR/dq,
not to the condition - the pointwise contraction (P o R)'(q_*) stays
below 1 everywhere scanned (0.903 even at kappa = 1.5).  Measured
sharper on 07-14: the wall is not a fixed kappa but a function of the
box geometry.  On the 3.5e-3 q pads of the positive batches the
product reads 0.9917 at the [0.0995, 0.10] slab (crossing projected
near 0.12); on the 5e-3 pads the deep slabs need, it reads 1.064
already at 0.10 (1.079 at 0.13, growing ~0.005 per 0.005 of kappa).
The switch to the Nakajima lane at exactly 0.10 was therefore forced,
not stylistic: with the pads the inward sweep needs there, no box
contraction was available anywhere on [0.10, 0.16].  The product bound
does three jobs, and each has a contraction-free replacement on the
positive side.  Uniqueness: Nakajima's saddle theorem covers
kappa >= 0 with measured ratio alpha_*/alpha_c <= 0.874 across the
positive branch.  Existence: the endpoint-inward IVT sweep, already
contraction-free.  Location for the G-crossing: dR/dq > 0 (Lemma 2)
plus P' > 0 make q -> P(R(q)) increasing, and with uniqueness its
displacement P(R(q)) - q is positive below q_* and negative above, so
a certified sign bisection locates (q_0, psi_0) to any width with no
Picard shrink.  Huang's local requirement is then discharged by
evaluating (P o R)' on the thin LOCATED interval instead of the slab
rectangle.  The amp and lambda margins both grow toward positive
kappa (0.378 and 0.109 at the current edge), so the next binding
constraint past 0.12 is not yet known - it would be measured, not
projected.

Built and measured the same night (locate_fp_bisect in
certify_km_slab.py, past_wall_0p13.py, results/past_wall_0p13.log):
at the point margin kappa = 0.13, the rectangle product bound on a
slab-sized box reads 1.323 - past the wall, as projected - while the
sign bisection locates the fixed point at both alpha endpoints to
width 2e-8 (three orders below the Picard image floor: thin-point
evaluations have no image-width term), the pointwise contraction on
the located intervals reads 0.794 and 0.798, and the G crossing
resolves with margins ~2e-3.  Nine seconds end to end, and
Nakajima's hypothesis is certified alongside (closed form
E[(kappa-Z)_+^2] = (1+kappa^2)Phi + kappa phi in ball arithmetic:
alpha_ub = 0.7074 < alpha_c(0.13) = 1.03944), so uniqueness rests on
his theorem with a certified premise - this is the fixed-point
condition at kappa = 0.13.  The strip build followed the same
night (verify_slab_nak in certify_km_slab.py, runner certify_nak.py):
the certified premise alpha_ub < alpha_c(kappa) over the kappa ball
hands uniqueness to Nakajima's theorem, and the locate/contraction/G
block runs per kappa sub-ball (n_k = 8) because the kappa width
floors the displacement's sign resolution - on the full 5e-4 ball the
locate returns the whole q box and the located contraction reads
1.05; on sub-balls it reads 0.81 with margin 0.18, matching the point
value.  locate_fp_bisect gained quartile fallback steps at the
resolution floor.  Test slabs at [0.13, 0.1305] and the far edge
[0.1595, 0.16] pass 51/51 checks in ~68 s each with uniform margins
(contraction 0.18, G 2e-3, premise 0.31-0.33, amp and lambda
comfortable).  The full lane batch then certified 120/120 slabs
on [0.10, 0.16] (results/certified_intervals_nak.csv): the strip
now crosses the wall, with the pos2 row in the margin table and
the worst certified Nakajima premise margin 0.311 (alpha_c
still 1.4x alpha_* at 0.16).  Replay:
`python certify_nak.py slabs_pos2_main.json out.json` (and
`slabs_pos2_tail.json`, `slabs_pos3_a.json`, `slabs_pos3_b.json`).  Across the lane's box batch the 1280 inward checks are
all positive with worst margin 3.0e-4 at the kappa = 0.1395 high-alpha
corner and median 7e-4 - the 5e-3 pad is sized right, thin where the
drift geometry says it must be.  The 1920 G-crossing checks are all
correct-signed with worst margin 1.9e-3 and median 2.2e-3, uniform
across the lane (the alpha pad drives them).

## 7. The two-variable global condition (float scans)

`huang2var.py` transcribes S_*(lambda_1, lambda_2) at general kappa
(his eq:def-sS-star-bLam-nu); kappa enters both as an additive shift in
the log Psi argument and inside the planted cavity law N(z).
`scan2var.py` runs, per kappa: the (1,0) anchor, the FD Hessian, the
moment-body clearance of the distinguished point, a coarse global grid,
and far rays.  This is the diagnostic (nonrigorous) analogue of the
certified Region I/II machinery at kappa = 0.

At the measured extremes the landscape holds but weakens on the
relaxed side: at kappa = +1.5 the picture matches kappa = 0 (off-center
max -0.0037, weak eigenvalue -0.0041, clearance 0.013), while at
kappa = -1.5 the weak Hessian eigenvalue has dropped to -0.0013 (from
-0.0045 at zero) and the off-center margin to -0.0012 - the
distinguished direction is measurably approaching degeneracy at deep
negative margin, consistent with the expected RSB territory, though
the condition still holds numerically everywhere scanned.

Two readings of the grids need care.  On roughly the half-plane
lambda_1 < 0 the s-infimum is genuinely unbounded below: alpha E[N^2] =
psi_0 exactly at the fixed point (N = M(u)/sqrt(1-q) and psi = R), so
the s^2 coefficient cancels and a subleading term runs away.  Those
directions satisfy S_* <= 0 trivially and are the S^{s_max} case in
Huang's treatment; the scans record them as unbounded, not as data
holes.  And the "off-center maximum" must be read outside radius ~1.25
of (1,0): at 0.4 grid spacing the nearest ring of cells is the peak's
own shoulder.  With both conventions, every scanned kappa shows a
single peak at (1,0), off-center values at or below about -0.003, and
negative far rays - the same landscape as the certified kappa = 0 case,
with margins that barely move across kappa in [-0.5, 0.5].  The scan
at kappa = 0.13 (inside the Nakajima lane, run 07-14) fits the pattern
exactly: anchor 2.2e-14, eigenvalues (-0.2342, -0.0045), clearance
0.0175, off-center max -0.0037, rays negative (results/s2v_0p13).

## 7. The classification reading of the curve

For binary weights w in {-1,+1}^N the Euclidean norm is fixed at
sqrt(N), so for any feature perturbation e,

    |<w, e>| / sqrt(N)  <=  ||e||_2.

A training constraint y_a <w, x_a>/sqrt(N) >= kappa therefore certifies
the label y_a against every perturbation of x_a of Euclidean norm below
kappa.  With centrally symmetric i.i.d. designs and independent labels,
label folding (g_a = y_a x_a) makes the robust-interpolation event
identical to the satisfiability event studied here, so alpha_*(kappa)
is the phase boundary for how many random labels per parameter a
one-bit linear classifier can memorize with prescribed robustness
radius kappa.  At kappa = 0 the certified value says a binary linear
classifier interpolates M random labels iff M/N is below 0.833...,
i.e. about 1.20 binary parameters per random label bit.

Limits of the reading: nothing here concerns trainability (algorithms
find solutions only below the information-theoretic boundary),
generalization on structured labels, correlated features, or networks
with hidden layers; kappa is a feature-space radius, and translating it
to input space needs a Lipschitz bound for the feature map.

## 8. The next certification step, mapped

The first piece of the two-variable condition to certify at kappa != 0
is the Hessian of S_* at (1,0) (Huang's Claim numeric-M-estimates).
His appendix computes M from three prior-side integrals I_1, I_2, I_3
(closed forms in psi_0, q_0 and p_4(psi) = E tanh^4 - these transfer
to any kappa unchanged) and three constraint-side constants C_1, C_2,
C_3.  The C closed forms via r_2(gamma_0), r_4(gamma_0) are the
kappa = 0 specialization - his derivation says so explicitly, and the
simplifications alpha E[N hH] = -q_0(1-q_0)psi_0 and
alpha E[N^2] = psi_0 that produce them use the zero-margin law
(the second survives at general kappa, the first does not).  At
kappa != 0 the C's must come from the pre-specialization display of
his second-derivative lemma: expectations over hH of
F'_{1-q_0}(hH) (...)^2 and N (...) terms at the shifted law - all
real-cell-Riemann certifiable with the machinery in
certify_km_slab.py.

That transcription is now done and anchored (hessian_kappa.py): the
general-kappa C's collapse to the same (a, b)-quadratic structure,
both kappa = 0 reductions were re-derived symbolically (the 2/(1-q0)
term via alpha E[N^2] = psi0, which holds at every kappa; the psi0/q0
constant via alpha E[N hH] = -q0(1-q0) psi0, which does not), and the
float evaluation at kappa = 0 lands inside every one of Huang's
certified intervals: I_1/I_2/I_3 to their printed digits, C_1
(-0.71781 in [-0.7193, -0.7165]), C_2 (5.05008 in [5.0439, 5.0568]),
C_3 (1.14387 in [1.1345, 1.1526]), det(M) = 2.75e-4 >= 2.246e-4.
The assembled M is the FIXED-TILT Hessian; the finite-difference
Hessian of the inf-over-s functional is more negative in the PSD
order, exactly the Schur relation - the two computations are
consistent, not equal.  results/hessian_kappa.csv tracks M along the
curve; arb-certifying its negativity on the strip is the remaining
piece of this step.

Sweeping M along the curve: the fixed-tilt Hessian is negative
definite for kappa <= 1.15 and loses definiteness between 1.15 and
1.20 (det crosses zero; M22 itself turns positive near 1.3), while the
inf-over-tilt landscape remains a single maximum out to at least
kappa = 1.5.  Both crossings were bisected in float on 07-14: det changes
sign inside (1.1812, 1.1844), so the fixed-tilt wall sits at
kappa = 1.18 to the resolution of the continuation, and M22's own
sign change lands inside (1.3000, 1.3063).

Certifying det M > 0 in arb at a nonzero kappa needs tighter parameter
boxes than the slab rectangles provide: det ~ 1.3e-4 at kappa = 0.05
while the C's move at order dC/dq ~ 10, so the (q0, psi0) box must be
~1e-5 wide - which means locating alpha_*(kappa) itself to ~1e-5 by a
certified bisection of G (about twelve mean-value G evaluations) and
then Picard-locating (q0, psi0) at that alpha.  That build happened
(section 6): the chain now stands certified at five margins spanning
the contraction strip.  So the zero-margin certificate's fixed-tilt treatment of
the center transfers only to kappa ~ 1.17, and beyond that the local
argument must re-optimize the tilt (the Schur-complement route the
capacity paper already uses for its ray certificates) - the report's
warning about fixed-tilt curvature loss, measured and located.

## 9. The two-variable condition certified at kappa = 0.05 (07-14)

The four-piece zero-margin architecture (Region II sweep, Region I
star, stage-2 sweep, star interior) ports to located parameter boxes
with three devices, each exact mathematics rather than tuning; the
paper's Section on the port has the polished statements, and AUDIT.md
maps them to code.  The failure story, kept honest here:

- Plain Phi values carry the located psi-ball width (~2e-5) against
  dual-localization valley gaps of ~1e-7; every weak-direction chunk
  failed.  Fix: the maximizer stays SYMBOLIC (a* = grad Phi(1,0) =
  (psi(1-q), q), s0 = sqrt(1-q) as balls; no stored decimals, no
  origin-inflation ball), x-hulls become offsets, and edge_check
  evaluates through the anchored-Bregman integrand
  log(cosh D + M sinh D) - M D, D = (l1-1)X + l2 M, whose parameter
  fuzz is quadratic in |lambda - (1,0)| (measured 93-114x tighter at
  the failing corners; exact zero ball at the anchor).
- That integrand's two exact forms have disjoint stability regimes:
  cosh/sinh is exact at D = 0 but cancels two e^|D| balls at box
  corners (the guard then fires on every subdivision and the integral
  returns infinite - every plus-side edge_check died at +-inf);
  the split e^D(1+M)/2 + e^{-D}(1-M)/2 is nonnegative-real but
  carries first-order M-width near D = 0 (Breg0(1,0) went from exact
  0 to +-2e-6 and the inner bands died instead).  Branch at |D| = 1.
- The T-side kernels build E'(V), E''(V) from E - V; far-tail cells
  subtract two O(20) balls and explode erratically (certified upper
  bounds +14 to +2145 against a true ray second derivative of -6.6;
  whether a cell straddles the cancellation regime is knife-edge in
  the ball boundaries, which is why the spikes looked random).
  Fix: the Mills gap t = E - V intersected with (0, 1/V) for V > 0,
  E' with (0,1) (truncated-normal variance), E'' with (0, t) (hazard
  convexity plus E'' - t = (E'-1)(E+t)).  Digit-identical on benign
  cells; kappa = 0 regression unchanged; the du-halving cascades
  vanish and wedge bands run 10-30x faster.
- Wedge-edge dual fans need interior radii (5 per angle, not just the
  two arcs): the dual image of a sector stretches ~0.4 in lambda and
  the sublevel intersection bulges between arc-only anchors.
- Stage-2's zone-shrink containment left a wedge-edge ring where
  value-level certification cannot beat the parameter fuzz (~1.3e-4
  enclosure against true S ~ -1e-4).  Fix: containment reads the
  Region-I manifest itself - a certified band covers every direction
  of its chunk to min(t1, T_of_angle), so with zero failed bands the
  certified reach is exactly T_of_angle, no shrink; failed bands
  would cap their directions at their inner radius.  The stage-2
  manifest records the SHA-256 of the Region-I manifest it consumed.
- Reproducibility scar: a sweep rerun without HUANG_GRID_N=3600
  reproduced the coarse-grid failure class - a manifest that does not
  record its grid depth can be "reproduced" at a different depth.
  Launchers pin the env; the manifest now records GRID_N.

Validation battery (validate_final_0p05.py): Breg0(1,0) = [0,0],
correlated-vs-uncorrelated enclosure consistency, and six gate bands
(both wedge edges, cone, smallest chunk, innermost, origin).  Region
II certified (1296 top cells -> 867 leaves, 0 fails, n = 3600); star
interior certified (inradius 0.01481 vs required 0.01209); Region I
(1404 bands) and stage-2 land the day's full-run verdicts.

Toward the strip: the same pipeline at a kappa BALL is only a wider
hull at locate time; the wedge-edge ray margins (~1e-3 to 1e-2 at a
point) and the kappa-sensitivity of the landscape set the affordable
slab width.  A first budget from the float scans (a proxy, to be
replaced by the first slab run's certified margins): the off-center
landscape values move about 0.016 per unit kappa across the scanned
range, so a 1e-3 wedge margin tolerates a kappa half-width near
0.03 - the whole certified strip [-0.65, 0.19] in roughly thirty
2varfn slabs, each a run of today's size.  That is a background
program of days at the current worker policy, not a redesign: the
strip version is an adaptive kappa-subdivision driven by the
certified wedge margins, bisecting where they thin, and nothing else
in the architecture changes.  The remaining margins queue
(queue_margins.sh) runs the point pilots at -0.05, 0.0995, 0.13,
-0.45 with the deep certified alpha intervals first.

## 10. What this does and does not claim

The upper-bound side (Huang's general-kappa theorem) is what these
conditions feed; certifying them on a kappa interval yields an
unconditional capacity **upper bound** curve there.  The lower bound
(Ding-Sun) is proved at kappa = 0 only; its conditioned second-moment
reduction has no general-kappa version yet, so nothing here should be
read as an exact threshold statement at kappa != 0.  All float scans
are diagnostics, not certificates.

## 10. The margins queue and the 0.0995 exclusion-edge ridge (2026-07-14)

The kappa = -0.05 pipeline ran end to end with zero failures on the
first attempt (sweep 884 leaves, Region I 1404 bands, stage-2 1294
leaves, star inradius 0.01527 against required 0.01209), so Condition
2varfn is now certified at both 0.05 and -0.05.  The -0.05 manifest is
the first to carry exact B-matrix packets, which lets the Lean skeleton
check Loewner definiteness per band: 14 kernel theorems (13 chunks of
108 bands plus a total count), alongside the four earlier families.
One decide over all 1404 bands exceeds the kernel recursion limit;
chunking is the fix, with the partition total itself kernel-decided.

At kappa = 0.0995 the Region II sweep failed exactly one MIN_SIDE leaf,
at a2 - a2* in [0.0967, 0.0986] just above the exclusion box's top edge
(offset +0.0961): the dual certificate degenerates in a thin ridge
there ([+/- 0.181] on a 0.0018-wide cell), recovering two leaf-widths
higher.  The top-edge offset is now +0.1030.  This is safe to do
without re-running Region I because the star-interior check and the
stage-2 union containment both recompute their requirement from the
box, so an exclusion region the star cannot cover fails loudly rather
than silently widening the gap between the pieces.  The 0.05 and -0.05
certificates predate the change and remain internally coherent: the
box is fixed per process, stage-2 records the expanded box it tiled
(EXCL_OLD), and the sweep sources are hash-bound.  Sweep manifests
written from 2026-07-14 on also record EXCL directly, and the portable
checker verifies the sweep/stage-2 seam (EXCL_OLD reaches at least
2 x MIN_SIDE beyond EXCL) from the manifests alone.

## 11. The margin gap at two certified margins (diagnostic)

The conditional field distribution among solutions (Section 9's
p(h)) now has curves at both certified margins.  The shape repeats:
as alpha approaches alpha*(kappa) the density piles against the
constraint and the mean gap above kappa shrinks, from 0.70 to 0.59
at kappa = 0.05 and from 0.74 to 0.64 at kappa = -0.05.  Read as
machine learning, a perceptron trained to margin kappa at capacity
still over-satisfies a typical constraint by roughly 0.6 standard
units of field - entropy alone buys that much slack beyond whatever
margin is demanded, and the price of DEMANDING the slack instead
(moving kappa itself) is the capacity drop of the alpha*(kappa)
curve.  Both statements are float diagnostics on the RS branch, not
certificates; the certified objects remain the alpha*(kappa) bounds.

## 12. Ternary prior, first solved points (diagnostic)

The ternary-prior RS system (exploration/ternary_km.py, weights in
{-1, 0, +1} with the self-overlap Q and its conjugate) solved cleanly
once the frozen-branch guard was in place.  The curve now has eight
points (results/ternary_curve.out, box run at the five paper margins
plus 0.2, 0.25, 0.3, 0.35):

    kappa    0.0      0.05     0.0995   0.13     0.2      0.25     0.3      0.35
    tern     1.17448  1.07951  0.99563  0.94835  0.85080  0.78926  0.73357  0.68302
    binary   0.83308  0.78107  0.73348  0.70593  0.64740  0.60926  0.57388  0.54102

all stationarity residuals at 1e-6 or better (an earlier single
solve at kappa = 0.1 exactly gave 0.994833; the curve point is at
0.0995, and the difference matches d alpha/d kappa ~ -1.55 times
0.0005).  The same code path reproduces the binary alpha*(0) =
0.8330786 to the certified digits, which anchors the implementation.
Read against the first-moment bounds, ternary reaches 74 percent of
annealed where binary reaches 83 - the richer prior pays
proportionally more entropy to frustration.  Floats on the RS
branch, not certificates.

## 13. Design rules, read from the numbers (diagnostic)

Three practical readings of the certified and diagnostic results, for
a practitioner storing random patterns in sign-constrained weights:

Capacity price of demanded robustness.  Requiring every constraint to
clear margin kappa caps the load at alpha*(kappa): 0.833 at kappa=0,
0.781 at 0.05, 0.733 at 0.1 (the first and second are certified
digits, the third is the RS value beside the certified 0.0995).  Per
additional 0.05 of demanded margin near zero, the price is about six
percent of capacity.

Free robustness from entropy.  Below capacity, typical solutions
over-satisfy: the conditional mean gap above kappa sits near 0.6-0.7
standard field units and shrinks only mildly as alpha approaches
alpha* (0.70 to 0.59 at kappa=0.05; 0.74 to 0.64 at -0.05).  Demanding
a small margin explicitly therefore buys less than it appears - much
of it was already there for free.

Bits versus states.  Per weight STATE the ternary prior stores more
(1.174 vs 0.833 at kappa=0), but per weight BIT it stores less: 0.741
against binary's 0.833 constraints per bit (dividing by log2 of the
state count).  At this level of the theory, binary weights are the
more bit-efficient quantization at every computed margin
(ternary_figure.py, the eight-point curve): the absolute per-bit gap
widens from 0.092 at kappa=0 and saturates near 0.111 above kappa ~
0.2, while the relative advantage keeps growing, 12 percent at
kappa=0 to 26 percent at 0.35, because both capacities fall.
Floats and diagnostics throughout; the certified objects are the
alpha* bounds.

## 14. Finite-size contact (diagnostic)

A population annealer (24 chains, geometric ramp matched to the
hinge-energy scale, 400 sweeps per spin) trained +-1 perceptrons on
Gaussian patterns at N=101, six disorder samples per point
(finite_size_experiment.py; results/finite_size_N101.csv and the
overlay figure).  Three observations against the theory:

The walls order and sit below alpha*.  Success stays at one through
alpha ~ 0.61-0.67 and collapses before the capacity at every margin,
in the right kappa order; at kappa = 0.1 the last successes appear
at alpha ~ 0.73 - the RS capacity itself - and none above.  The gap
between where this annealer stops and where solutions provably end
is the algorithmic-hardness window, and its width here (~0.1-0.15 in
alpha) is budget-dependent, not a threshold claim.

Found solutions are atypical.  At low load their mean margin-gaps
track the typical-solution law; as alpha grows the typical mean
descends while the found-solution mean holds near 0.65-0.70, sitting
clearly above typical by alpha ~ 0.75.  Algorithms reach the wide,
over-margined solutions - the flat-minima bias, measured here in the
same observable the theory certifies.

The margin price transfers.  The empirical walls shift left with
demanded kappa roughly in parallel with alpha*(kappa), so the
certified robustness price is visible in practice at N=101, not only
in the thermodynamic limit.  At N=201 (same budget in sweeps per
spin) the walls sharpen and shift left to 0.55-0.67 - at fixed
relative budget, larger systems are harder for the annealer, so the
wall is a budget-dependent lower envelope of the true algorithmic
threshold, not an estimate of it.  Scaling the budget measures the
envelope's rate: quadrupling the sweeps moves every wall right by
about one grid step (+0.06 in alpha; kappa=0.05's dead 0.61 point
recovers to full success, kappa=0's stragglers reach 0.73), so the
recession is roughly logarithmic in budget and reaching alpha* this
way would take thousands of times more annealing - the activated
picture, measured.  The pooled gap distributions
(gap_histogram_figure.py) show the full shape: at moderate load the
found-solution histogram tracks the RS law closely - direct empirical
contact with the distribution derived in the paper - while near the
wall the found solutions avoid the tightest gaps and pile into
mid-gaps, the wide-solution bias resolved bin by bin.  The three runs
compress into one empirical law candidate (algorithmic_fraction.py):
within each size and budget, the wall sits at a kappa-INDEPENDENT
fraction of the certified capacity - 0.90 at N=101, 0.75 at N=201
(same per-spin budget), 0.79 at N=201 with 4x sweeps, 0.69 at N=301
(same per-spin budget), each flat across margins to about three
percent.  Demanding margin costs the annealer the same relative
capacity it costs the storage bound, so the certified curve is the
right yardstick for algorithms at every kappa, not only at zero.
Six samples per point; the fractions carry roughly +-0.03.  At fixed
sweeps per spin the fraction falls with N (0.90 / 0.75 / 0.69); the
three sizes happen to sit on a 1/N line whose intercept would be
about 0.59, but with three points and a coarse alpha grid that
intercept is a projection, not a finding - the measured statement is
only that a fixed per-spin budget does not hold a constant fraction
as N grows, i.e. the annealer needs superlinear total work to keep
pace with the certified curve.  The budget axis at N=201 now has
three points: 400 -> 0.748, 1600 -> 0.793, 6400 -> 0.857 (the last
from a targeted grid at kappa {0, 0.1}), consistent with a fixed
gain per budget quadrupling through the measured range, no
saturation visible.  The 6400 walls were predicted before the run
from the 400->1600 increment (+0.06 alpha per 4x: 0.70 at kappa=0,
0.64 at kappa=0.1) and landed exactly there - the pre-registration
is in ops/wrap_2026_07_15.md.  All of this is diagnostic and sits
on top of the certified alpha* bounds, which are the rigorous
objects.


## 15. Proof verification pass (2026-07-16); DS-condition port sized

Adversarial verification of every analytic proof in the paper (four
independent referee agents, each instructed to refute):

- Lemmas 1-2 (stationarity, dR/dq): confirmed by independent
  re-derivation, finite differences at six off-branch points, and new
  integrand-level battery items (17-19: the Stein/IBP assemblies as
  radical-cleared algebraic identities).  Precision repairs applied:
  envelope claim now states its Condition-1 hypothesis; alpha factor
  restored in one prose line; domination/Stein regularity sentence
  added; M' in (0,1) forward-referenced to the new Lemma (Mills
  clamps).
- Mills clamps: E'' > 0 (hazard convexity) had been asserted as
  classical with no proof or citation while the code intersects
  E''-balls with (0, t) - load-bearing for soundness.  Now proved in
  the paper (single-crossing against the equal-mean exponential;
  coefficient of variation below one), attacked by a dedicated
  referee (holds; positivity margin ~ 2/V^4, numerically tight), and
  its algebra added to the battery (items 14-16).  The inequality is
  true at every real V, so no shipped certificate was ever unsound.
- Second-moment lemma: L1/L2 dichotomy closed (diagonal term forces
  f in L2 or the claim is trivial); hypothesis now 0 < int f dPhi <
  infty; error term corrected to O(N^-1 log N); the He_1 vanishing
  case tightened.
- Embedded-perceptron proposition: citation chain repaired - ALS is
  Rademacher-disorder, PX Gaussian-but-conditional; the unconditional
  Gaussian whp source is Altschuler arXiv:2205.02319 (verified
  against the abstract), now cited.
- DS-condition section: the interior-max claim now carries its
  exclusion window (-5e-5 outside |lambda| >= 0.02 of the roots;
  climbs to -1.6e-6 inside), identity count fixed, stray paren gone.
- Hessian C_j: referee fetched Huang's LaTeX source; the
  pre-specialization display is general-kappa by Huang's own words,
  the paper's C_j reduce term for term, kappa=0 values land inside
  his certified intervals near midpoint, and alpha E[N hH] fails at
  kappa=0.05 by 5.1 percent exactly as claimed.  One defect found and
  fixed: hessian_kappa.py's docstring conflated the fixed-tilt and
  tilt-optimized Hessians.
- s-runaway remark: true in substance, region is not the literal
  half-plane (boundary crosses lambda_1 = +0.04 on the lambda_2 = 0
  axis at kappa = 0.05); rewritten to say what is measured and that
  nothing downstream consumes it (the sweep witnesses the uncapped
  infimum at finite tilt).

Portable checker gained the radial-reach clause (outermost Region-I
band level must reach the star radius in the same manifest); proven
both ways - passes all five margins, rejects a 40-band truncation
with consistently rebound hashes.

Lane rectangles: rect_strip.py at delta 5e-4 / n_loc 4000 / 8
sub-balls certifies the hardest slab (contraction 0.957); full
180-slab run launched on the worker box (two halves), collector
collect_rect_strip.py ready (contiguity, CSV agreement, recipe
uniformity, worst contraction).

DS lower-bound condition port, sized and deferred: the kappa=0
certificate is dsfun.py (1571 lines, ~80 gamma-coupled sites) +
blocks 1/2/3a/3bc; the general-kappa cavity is the affine shift
xi_z = kappa/sqrt(1-q) - gamma z, prior-side entropy family
unchanged.  Port order for a fresh session: (1) shift the I_s family
(I, I', I'') and its tail envelopes; (2) block3a grid with located
(alpha, q, psi) balls at one margin; (3) the endpoint windows -
block3bc's PG''(0) argument needs DS's A''(0) display at general
kappa, block2's near-one expansion consumes G_*(alpha) which our
located boxes already certify; (4) blocks at the remaining margins.
Expect the correlated-integrand and thin-endpoint laws to bite in
the shifted truncated inner integral; budget a day-class session.
