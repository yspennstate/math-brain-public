# T227 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 08:48 Asia/Tbilisi (04:48 UTC).

## 1. Orientation and bounded literature update

Read the startup memory index and compute governor state. State: warn,
owner_away_open, CPU saturation. Only small standard-library, single-thread
calculations will run, with OMP_NUM_THREADS=1 and nice -n 15. The task's
specific restriction to writes in this folder supersedes global shared
brain/checklist/mesh updates; none of those stores will be changed. No git,
subagents, GPU, torch, or MLX. Earlier session folders are read-only.

Read earlier reports, logs and proofs; continuing through every script.
The literature check began around 08:48 and is capped at five minutes.
Queries: catapult deep nonlinear networks convergence theorem 2026;
catapult phase finite width nonlinear networks proof; catapult deep proof
2026; catapult convergence finite-width nonlinear 2025 2026.

Opened arXiv pages: 2003.02218 (Lewkowycz et al., original), 2205.11787
(Zhu et al., neural quadratic models), 2301.07737v2 (Meltzer, Chen, Liu,
quadratic and two-layer homogeneous models), 2603.10079v2 (Gess,
Heydecker, shallow SGD), 2610.23007 (Nguyen, Yadav, Mody, Schmidt,
minimal shallow ReLU classifier), 2607.04993 (Hofmann, solvable maps),
and 2610.13524 (layer-wise random-feature simulations; scope being checked).
No matching deep finite-width product-initialization theorem found so far.
This is a bounded update check, not an exhaustive absence claim.

The initial read-only shell commands were not all given the requested
nice/environment prefix; corrected from 08:49 onward. The sandbox prints
`nice: setpriority: Operation not permitted`, as in earlier sessions;
actual inherited priority will be checked by every numerical script.

## 2. Independent recheck underway

Direct differentiation confirms the actual-coordinate gradients:
with W=sqrt(m)B, u=tanh(c), v=tanh(Wu/m), q=1-v²,
A=v, D_ij=a_i q_i u_j, C_j=(1-u_j²)mean_i(a_i q_i W_ij),
the derivatives in (a,B,c) are A/m, D/(m sqrt(m)), C/m.
Thus m times a cross-gradient inner product equals the A product
average plus the D product average over m² entries plus the C product
average. Will independently check the signed entrance and full tail by
fresh rational code, without executing or importing prior scripts.

Completed the bounded web update around 08:50; no matching solution found.
The layer-wise random-feature paper supplies a simulation framework, not
the theorem requested here. No further literature search is planned.
Read all three earlier REPORT.md, LOG.md, PROOF.md files and every Python
script. No prior script was imported or executed.

Created `recheck_signed.py`: rational exponential enclosures by argument
reduction to [0,1/16], degree-18 series, outward rounding and squaring;
direct signed endpoint extrema instead of midpoint decomposition; literal
Euclidean-coordinate trajectories and finite differences. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_signed.py
```

Exit 0, PASS. Independently certified a1 in
(5.905999288745205,6.815068374658852), W1 in
(-28.593597842986263,-16.236200399445977), c1>.8432462666708463,
34.578099314709206<m*lambda0<41.77240168944187, L0<7.587657135068594.
All loss-spike and saturated-tail invariance/contraction bounds passed.
21 literal-coordinate trajectories at widths 4,40,80 passed; finite
difference error 1.96e-10; maximum tail ratio .10000000004173974.
RSS 15,581,184 bytes; nice 20; runtime .30 s. Data:
`previous_recheck.json`. **The round-4 result holds.**

## 3. Chosen extension, before its calculation

Prove the first bootstrap requested by round 4 for unbiased independent
middle-layer signs, retaining the same dense architecture, positive
outer-layer boxes and zero-label datum. Only change P(S=1) from 3/4 to
1/2. Aim: with high probability at all sufficiently large finite widths,
uniformly for eta in [.9m,1.1m], the small initial residual grows until
it exits a fixed window, in O(log m) steps. Control the entire parameter
space during these steps, without tying neurons or ignoring the common
residual. This is the early instability/escape lemma, not a convergence
or full catapult theorem.

Proposed proof: a row concentration event controls initial preactivations.
In a small convex tube around the initial middle weights, bound the
full cross-gradient between 50/m and 63/m. This would amplify residuals
by a factor between 40 and 69 per step. The backwards geometric sum of
earlier residuals then closes the tube until |F| first reaches .02.
A conditional one-coordinate density bound will exclude an excessively
small initial residual; bounded differences will give the initial upper
bound. Target tube: a in [7.9,8.1], c in [1.97,2.03],
|W-W0|<=.2. All constants and probability bounds remain to be checked.
The intended next fixed window is [.02,1.38]. Further nonlinear entrance
and convergence beyond that window will remain open.

## 4. Centered bootstrap: first certificate

Created `verify_bootstrap.py`, exact rational bounds plus independently
implemented literal (a,B,c) updates. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_bootstrap.py
```

Exit 0, PASS. Main rational constants:

```text
initial |z| <= .02527; tube |z| <= .21927 < .225
7.20006 < D_ij < 7.857; |C_j| < .76268304
51.20855358409636 < m*cross-gradient < 62.36475941950364
total h*|F| before and including exit update <= 22/975
movements: a <= .005076923076923077
           W <= .17728615384615384
           c <= .017209258338461538
common shift approximation error < .007446153846153846 < .0075
single-coordinate initial derivative lower: 7.66550189042784/m² > 7/m²
bounded difference range constant: 16.03602/m² per W coordinate
failure probability at m=200000 < 3.5766993501988253e-9
uniform exit-time bound at m=200000: 13 steps
```

The same sum bound also controls a common shift of every W entry:
`W_ij,t = W_ij,0 - 7.53 sum_{s<t} h F_s + error_ij,t`,
with absolute error < .0075 through exit. This follows from
|D_ij-7.53|<.33 and supplies explicit fluctuation control as part of
the same bootstrap lemma.

39 small-network trajectories at widths 4,20,100 passed conditional on
the row event; cases include balanced circulants, identical balanced
rows (arbitrary column imbalance), row-event boundary values, random
amplitudes and opposing corners. All three learning-rate values .9,1,1.1
were checked. Residual ratios were 52.48239310108449 to
64.8187097520408; maximum observed exit time 3; finite-difference
gradient error 8.53e-11. Segment samples also passed the metric bound.
These samples audit formulas, not the large-width probability theorem.
RSS 26,525,696 bytes, nice 20, runtime .92 s.
Data: `bootstrap_verification.json`. Some exact/nearly balanced numerical
cases were skipped below a 1e-12 initial residual; a separate arbitrary-
precision near-zero test will address that numerical limitation.

The probability proof to be written uses only row concentration:
failure <= 2m exp(-m/5000). A bounded-difference calculation gives
P(|F0|>=.02) <= 2 exp(-m²/400000). Conditioning on every variable
except U_11 gives P(row event and |F0|<m^-4) <=143/m².
Their union is below 4e-9 at every m>=200000. Need to audit these
calculations independently and finish every proof step.

## 5. Full proof and second audit

Wrote `PROOF.md`: actual-coordinate gradients, uniform cross-gradient
bounds on the convex tube, endpoint containment before using segment
integration, finite exit, common displacement, and all probability steps.
The upper residual bound is proved by the conditional-expectation
martingale, with its exponential-moment estimate derived in the text.
The lower residual bound conditions on U_11, which has density 500;
the derivative stays above 7/m² on the entire conditional interval.
The row event depends only on signs, so that conditioning does not
truncate or change U_11's uniform law. The one good event works for
every step in the stated interval.

Created `audit_bootstrap.py`; no imports from any other task script.
Independent transcendental enclosures use binomial limits, not series.
Initial row extrema use positive and negative endpoint assignments,
not the midpoint expansion. Literal (a,B,c) interval-gradient sums at
square widths 1,4,25 include signed products between unequal gradients.
Those algebraic checks do not assert that the row event is feasible at
every checked width. General-width validity is supplied by the proof.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_bootstrap.py
```

Exit 0, PASS. Independent tube |z| bound .21664406; cross-gradient
interval [51.7359979108704,61.95180738555273]; movement bounds
[.004896410256410256,.17673784615384616,.016787587608].
An exact integer-power Chernoff bound at m=200000 gives row-event
failure <=1.6948154377045731e-12. It uses the generating function
of Bin(m,1/2) at z=51/49 and no exponential series. Rechecked
the one-coordinate density, bounded-difference constants, common-shift
error and the integer exit-time bound independently. The combined
probability bound is below 3.576694823934413e-9 at that width.

24 arbitrary-precision literal-coordinate trajectories passed with
single-coordinate perturbations 1e-20 and 1e-30 of an exactly balanced
matrix, both perturbation signs, h=.9,1,1.1, precision 80 and 110
decimal digits. Smallest initial residual about 9.64e-31; longest
exit time 17. Exit times agree at both precisions and exit outputs
agree to absolute error <1e-40. This directly tests the tiny-residual
case that binary floating-point audits could not resolve. These small
widths audit the deterministic bootstrap, not its large-width time
bound based on m^-4. The exact balanced state has F0=0 and remains fixed.
RSS 18,579,456 bytes; nice 20; runtime .96 s.
Data: `bootstrap_audit.json`.

## 6. Attempts to break the result and remaining gap

- Exact balance is a counterexample to an unconditional deterministic
  escape statement. It is explicitly excluded by the lower-residual
  event; the conditional derivative proves the probability estimate.
- Arbitrarily small nonzero residuals do not break the backwards
  geometric-sum argument. The arbitrary-precision audit targets this.
- Arbitrary column imbalance is allowed at this early stage. Identical
  balanced rows, which invalidate the old saturation entrance estimate,
  pass the new bootstrap. The C bound takes column absolute values.
- No frozen-kernel replacement is used. The exact integral includes
  the full simultaneous Euclidean update, and endpoint containment is
  proved before applying the integral.
- Positive W0 entries remain positive throughout this bootstrap:
  W_t >= .999-.177287 > .8217. Negative ones remain negative.
  Thus the earlier saturated region (every W<-15) cannot be reached
  during these steps. This explains why this lemma supplies growth,
  not yet the nonlinear entrance or subsequent curvature drop.
- The NTK remains between 50/m and 63/m up to escape. Calling this
  stage a completed catapult phase would be wrong. Nothing here proves
  later convergence, a maximal stable step, or divergence.
- The middle layer is centered. The positive output and input layers,
  mean output normalization, and single zero-label datum remain as in
  round 4. This is not a conventional centered-all-layers theorem.

No mathematical certificate failed. No dense network at the theorem's
large minimum width was allocated. All runs are standard-library,
single-thread scalar programs, under 27 MB measured RSS, under one
second of script-reported time, with a 120-second CPU limit and nice 20.

## 7. Report and final inspection

Wrote `REPORT.md` with the required PARTIAL verdict, the exact law and
bootstrap statement, reproduction commands, failed blanket escape and
one-step saturation claims, unresolved continuation, checked sources,
and the next nonlinear entrance problem. `PROOF.md` contains all steps.

Final inspection used a single-thread, nice-prefixed standard-library
stdin Python script: parsed all three scripts with ast.parse; loaded
all saved JSON outputs; checked every status PASS, nice>=15, measured
RSS<1GB, runtime<20 minutes, deliverables present, and REPORT.md's
required first line. Output: `Final artifact inspection PASS`.
Recorded sizes before this append: REPORT.md 6831 bytes, PROOF.md
12413 bytes, LOG.md 11849 bytes. No further numerical reruns were
needed after the passing audits. All authored artifacts stay in this
folder; earlier folders and external stores were not changed.

Task T227: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 08:48 Asia/Tbilisi.
