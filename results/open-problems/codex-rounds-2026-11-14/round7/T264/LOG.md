# T264 round 7 log

Task received: 2026-11-15 19:25 +04, “take the NEXT checkable step on this problem, building on that work.”

## 1. Scope and startup (19:25–19:30 +04)

All writes stay in this folder; predecessor folders are read-only. No git,
subagents, external messages, or external state writes. The task-specific
folder-only rule overrides the global mesh/checklist/memory write commands.
Read the startup memory index, brain navigation index, mesh protocol and
compute-state file. The compute state says `warn`, `owner_away_open`, with CPU
saturation and low disk; only small scalar calculations are planned.
Every Python run uses one-thread environment variables and `nice -n 15`.
The inherited nice level will be checked because this sandbox denies an
additional priority adjustment.

Commands: `rg --files` in this and all five predecessor folders; `wc -l` on
their reports, logs, proofs and scripts; `cat` on the predecessor reports
and first, round-3 and round-6 proofs. Remaining predecessor files are being
read before new mathematical work.

## 2. Literature check (started 19:26, ended 19:29 +04; under five minutes)

Used the web search tool for ReLU tempered/minimum-norm overfitting, fixed
dimension, expected risk and recent work. Opened these primary arXiv pages:

* Neil Mallinar, James B. Simon, Amirhesam Abedsoltan, Parthe Pandit, Mikhail
  Belkin, Preetum Nakkiran, *Benign, Tempered, or Catastrophic: A Taxonomy of
  Overfitting*, https://arxiv.org/abs/2207.06569.
* Guy Kornowski, Gilad Yehudai, Ohad Shamir, *From Tempered to Benign
  Overfitting in ReLU Neural Networks*, https://arxiv.org/abs/2305.15141.
* Nirmit Joshi, Gal Vardi, Nathan Srebro, *Noisy Interpolation Learning with
  Shallow Univariate ReLU Networks*, https://arxiv.org/abs/2307.15396.
* Kedar Karhadkar, Alexander Sietsema, Deanna Needell, Guido Montufar,
  *Harmful Overfitting in Sobolev Spaces*, https://arxiv.org/abs/2602.00825.
  This concerns Sobolev norm minimization, not the homogeneous ReLU atomic
  norm used in the predecessor results.
* Greg Ongie, Rebecca Willett, Daniel Soudry, Nathan Srebro, *A Function
  Space View of Bounded Norm Infinite Width ReLU Nets: The Multivariate
  Case*, https://arxiv.org/abs/1910.01635. This characterizes a function
  norm; its abstract does not resolve the stated statistical question.

No later full resolution was found. This bounded search is not an exhaustive
novelty claim. No SOLVED_ELSEWHERE.md is warranted by the sources found.

## 3. Choice, before attempting it (19:30 +04)

Choose **B: finite mean risk for d >= 4**, at every fixed sample size in the
predecessors' homogeneous sphere/Rademacher model. A possible route is an
explicit interpolating competitor with norm at most C(n,d)/delta, where
delta is minimum projective separation. Since a close or antipodal pair
has codimension d-1, delta^{-2} should be integrable exactly when d>3.
This needs a construction controlling all degeneracies, not just one pair.
First independently recheck round 6, as required, before pursuing this route.

## 4. Earlier result independently confirmed

Finished reading every predecessor REPORT.md, LOG.md, PROOF.md and Python
script, including the exploratory round-3 LP and round-6 artifact audit.
The predecessors' warnings about mean versus probability, opposite
hemispheres, projected-ratio ties, and antipodal degeneracies are substantive.

Re-derived the round-6 certificate: with p^2+q^2<=1, the absolute numerator
of its dual price is min(a|p|,b|q|)<=ab. Equality forces the four planar
directions (plus/minus b, plus/minus a). Their response columns fix the four
coefficient totals and attain the bound under the stated label signs.
Independently, the zero-extra-label function is
sign(x_1*x_2) min(|x_1|/a,|x_2|/b), bounded by |x_1|/a. Its pointwise limit
is x_1 sign(x_2). The correction terms tend to A sigma(x_2)+B sigma(-x_2).
Reflection in x_1 removes their cross terms, so the limiting spherical risk
is [1+(A^2+B^2)/2]/d. The main round-6 result holds.

Created a fresh standard-library verifier, recheck_round6.py. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_round6.py > prior_output.txt
```

Exit 0. Output:

```text
PASS round 6: 20 interpolation/cost cases, two independent circle integrands
PASS ambient dual identity: 1800 directions
Maximum circle-risk discrepancy: 1.0193068611386025e-11
Smallest-angle circle risks: [(0.0, 0.0, 0.4999997877961904), (-1.0, -1.0, 0.9999997877925415), (-1.0, 1.0, 1.0000002877998433), (1.0, -1.0, 0.9999992877835415), (1.0, 1.0, 0.9999997877908435)]
All assertions passed.
Resources: {'seconds': 0.07869708305224776, 'peak_rss_bytes': 15400960, 'nice': 20, 'threads': 1}
```

The shell denied nice's attempted adjustment; the script checked compliant
inherited nice 20 before computation. No mathematical check failed.

## 5. B construction to prove

For each input e=x_i, choose a unit tangent direction z perpendicular to e
which is not nearly perpendicular to any projected other input. A Gaussian
union bound will give |z.x_j| >= sin(angle(x_i,x_j)) /
[8(n-1)sqrt(d-1)]. Let delta_i be the minimum such sine and set
L=8(n-1)sqrt(d-1)/delta_i. The three-ReLU second difference

    h_i(x)=sigma((Lz+e).x)+sigma((Lz-e).x)-2 sigma(Lz.x)
          = (|e.x|-L|z.x|)_+

equals one at x_i and zero at every other input. Its balanced parameter
cost is at most 2 sqrt(1+L^2)+2L <= 2+4L. Summing y_i h_i gives an
interpolating competitor with cost at most C(n,d) H/delta, for |y_i|<=H.
An elementary dependence elimination should compress its 3n atoms to at
most n without increasing cost, covering the predecessors' fixed widths.

This construction handles arbitrary clusters and near-antipodes together.
The risk bound R<=Q^2/(2d) then reduces moment finiteness to that of
min_{i<j} sin(angle(X_i,X_j))^{-2r}. Its expectation is bounded by a sum
of pair moments, finite for 2r<d-1. For r=1 the pair moment should equal
(d-2)/(d-3). All constants and the compression step still need full audit.

## 6. Proof written

Wrote PROOF.md. The construction works: the tangent Gaussian union bound
loses probability less than 1/4 for small scalar projections and at most 1/4
for excessive length, giving the stated 1/[8(n-1)sqrt(d-1)] direction bound.
Each second-difference tent interpolates a coordinate label vector and has
cost <=2+4L. Summing gives K(n,d)=n[2+32(n-1)sqrt(d-1)].

The width reduction is explicit: orient any response-column dependence so
its coefficient sum is nonnegative, subtract it until a positive coefficient
vanishes, and repeat. It preserves the label vector and does not increase
atomic cost. Consequently the bound covers every minimum at fixed width
m>=n, as well as unrestricted width; finite-dimensional compactness also
proves existence.

The resulting pair-moment integral is finite for r<(d-1)/2. At r=1 it equals
(d-2)/(d-3), derived both by integration by parts and by the beta/gamma ratio.
This proves finite mean risk at each fixed n in d>=4. Combining the new
upper bound with the explicitly cited round-5 lower theorem yields the exact
moment threshold and matching tail power for every fixed n>=3. The lower
theorem is an input from that predecessor, not a new result of this session.

The bound grows polynomially in n and does not decide the limit of expected
risk as n tends to infinity. Next: independent construction/compression
checks, clustered and near-antipodal samples, and numerical pair integrals.

## 7. Independent verification implemented and run

Created verify_finite_moments.py using only the standard library, bounded
small lists, CPU/wall limits, and a peak-RSS check. It constructs actual
ReLU competitors, compares them to the absolute-value tent formula,
independently computes pair separation by exterior products and tangent
projection norms, and checks their cost bounds. Configurations include
random inputs, close pairs, near-antipodes, whole clusters, and planar
rank-deficient samples embedded in higher dimension.

The width reduction uses exact rational arithmetic on the actual sample
response columns, rather than toleranced floating-point elimination. It
checks exact response preservation and nonincreasing cost, then evaluates
the compressed networks against the prescribed labels. The networks are
competitors; no numerical minimizer is asserted.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_moments.py > verification_output.txt
```

Exit 0 on the first run. Full output is in verification_output.txt and all
per-case values in verification_data.json. The only stderr was the denied
nice adjustment; the actual-priority assertion passed before computation.
The remaining audit will examine sharpness, excluded parallel inputs,
width restrictions, and the distinction between fixed-n integrability and
a uniform-in-n risk bound.

## 8. Attempts to break the result and final verification

* The tangent-direction lemma has a second proof using the exact spherical
  coordinate density. A gamma-integral Cauchy--Schwarz inequality bounds
  that density near zero; a direct union bound recovers the same constant
  1/[8(n-1)sqrt(d-1)] without Gaussian length truncation. The verifier now
  checks these small-ball integrals for tangent dimensions k=2..20.
  Dimension k=1 is separate: every unit direction has absolute projection one.
* Re-derived the second-difference tent through sigma(t)=(t+|t|)/2, and
  independently evaluated its three ReLUs at samples and arbitrary test
  directions. The norm cost is computed from actual weight lengths and
  separately as 2 sqrt(1+L^2)+2L. Orthogonality is essential to this formula.
* Checked near-antipodes as well as close pairs. Their common singular
  variable is sin(angle), not chordal distance without identifying antipodes.
  Both caps enter the pair distribution. Exact parallelism has delta=0 and
  is excluded; the sample law makes it a null event. The bound need not be
  sharp near antipodes: an upper bound is all that integrability requires.
* Checked complete clusters and planar samples embedded in higher dimension.
  The construction needs pairwise nonparallelism, not linear independence
  of the inputs. No condition number of a full input matrix is inserted.
* Audited the compression sign choice for mixed-sign dependencies, zero
  coefficient sums, and possible zero response columns. Subtracting until
  one coefficient vanishes preserves nonnegativity and cannot increase
  cost. Iteration terminates after finitely many removals. Exact rational
  response preservation in eleven examples independently checks this step.
  The compressed function may change off-sample; only its cost is needed.
* Tightened all uncompressed and compressed sample errors to an absolute
  tolerance 1e-8; this replaces the earlier scale-dependent audit tolerance.
  Every example passes. The largest uncompressed error is 7.4431e-10.
* Re-derived the mean pair factor by both the sine-integral recurrence and
  beta/gamma identities, and checked both against direct quadrature.
  Values start at 2 for d=4 and 3/2 for d=5. The moment endpoint gives
  constant mass on successive logarithmic angular shells and diverges.
* Rechecked the transfer to every minimizer: a feasible competitor bounds
  Q_min, and the L2 triangle inequality bounds risk by Q_min^2/(2d).
  Nothing requires that the tents themselves minimize norm or that the
  compression preserve their population risk. Width m>=n is retained.
* The new upper moment bound and imported round-5 lower bound have identical
  models and width conventions. Their combination gives an exact moment
  threshold and matching tail power. It does not give a sharp tail constant.
* The resulting mean bound is O_d(n^6), so no uniform-in-n conclusion is
  possible from it. Positive finite risk for each n is not a proof that
  its n-to-infinity limit is positive finite. No GD conclusion is inserted.

Reran the same extension command after the second proof and tighter checks.
Exit 0. Complete final output:

```text
PASS construction: 51 configurations, d=2,3,4,5,8,12, n=2,3,4,6,10
PASS near-coincident pairs, near-antipodes, whole clusters, planar rank deficiency
Maximum interpolation error: 7.443091698533522e-10
Maximum tangent-selection trials: 2
PASS exact rational compression: 11 networks reduced to at most n units, exact response preservation and cost decrease
PASS mean pair factor: direct sine integrals, gamma ratios, and (d-2)/(d-3), d=4..12
Pair factors: [(4, 2.0), (5, 1.5000000000000286), (6, 1.3333333333333333), (7, 1.2499999999999782), (8, 1.2000000000000002), (9, 1.1666666666666667), (10, 1.1428571428571428), (11, 1.1250000000000002), (12, 1.1111111111111112)]
PASS independent tangent constant: spherical small-ball integrals, k=2..20
PASS threshold: decreasing, constant, increasing angular shells below/at/above (d-1)/2
PASS projective tail: both angular caps and exponent d-1
PASS excluded degeneracy: exact parallelism has delta=0; no positive-separation claim
All assertions passed.
Resources: {'seconds': 0.13628179201623425, 'peak_rss_bytes': 17055744, 'nice': 20, 'threads': 1}
```

The first extension run used 17,940,480 bytes peak RSS and 0.152701 seconds;
the final run used 17,055,744 bytes and 0.136282 seconds. Both are far below
the resource limits. No mathematical run failed. The only execution warning
was the denied nice adjustment, with compliant inherited priority verified.

## 9. Completion audit

REPORT.md starts with the required PROVED verdict and states option B's
fixed-sample conclusion, exact model and width conventions, the imported
lower bound, both reproduction commands, resource records, failures,
uncertainties and a next step. Its mean bound and moment threshold agree
with PROOF.md. No n-to-infinity classification is claimed.

Saved the read-only audit_artifacts.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > audit_output.txt
```

Exit 0. Output:

```text
PASS: scripts parse; 51 competitors, 11 compressions, 20 prior cases;
cost/interpolation bounds, output files, resource records and report agree.
```

All requested deliverables are in this folder. No predecessor edits, git,
subagents, external-store writes, accounts, or external messages were used.
The result resolves option B at every fixed n in the inherited model and
provides the previously missing finiteness half of its moment threshold.

Task: T264, “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 19:25 +04.
