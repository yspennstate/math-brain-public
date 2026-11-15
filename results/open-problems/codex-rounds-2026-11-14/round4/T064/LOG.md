# T064 work log

Task: “take the NEXT checkable step on this problem, building on that work” —
15 November 2026, 04:33 Asia/Tbilisi (00:33 UTC).

## Orientation and literature check, 04:33–04:36

Read both preceding folders' REPORT.md and LOG.md, the original folder's
SOLVED_ELSEWHERE.md, and round 3's complete PROOF.md and
check_level_stability.py. The original folder has no proof or scripts.
No preceding files were edited. Read the startup MEMORY.md and compute
state: `warn`, `owner_away_open`, CPU saturated. Only tiny, single-thread
standard-library audits are planned. The task's folder-only write rule
overrides global brain/mesh/checklist writes; those were not run.

Web-tool queries: `random plane wave Cardy SLE percolation conjecture 2025
2026`; `random plane wave crossing probabilities critical percolation 2026`.
Opened https://arxiv.org/abs/2010.11770,
https://arxiv.org/html/2010.11770v3, and
https://link.springer.com/article/10.1007/s00440-025-01367-8.
No later solution was found in this bounded check (under five minutes).
The first paper proves noncritical phase transition, not Cardy/SLE; the
later spherical-ensemble paper concerns supercritical giant components.
This search cannot certify exhaustive absence of a solution.

Reads used `cat`, `rg --files`, and subsequently
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 /bin/cat ...`. The initial discovery/read lacked the prefix;
it did no numerical work. `nice` prints a priority-change warning; the
audit will check actual priority before computing.

## Independent re-derivation of the preceding result

From the angular spectral measure, gradient covariance is I/2 and,
conditional on f=t, Hessian eigenvalues are -t/2 +/- sqrt(Z), where Z
is exponential of rate 4. Thus E|det H| =
(t^2-1+2 exp(-t^2))/4. The edge second derivative conditional on f=t is
N(-t/2,1/8); its absolute mean is
exp(-t^2)/(2 sqrt(pi)) + t erf(t)/2. These recover exactly the prior
alpha and beta, with gradient densities 1/pi and 1/sqrt(pi).
The level-strip isotopy includes all boundary strata, so the earlier
upper bound holds. Its leading area term is phi(0) A/(4 pi).
An independent numerical check will use a different quadrature rule,
and will also verify the earlier closed-form height integrals.

## Chosen extension, before doing it

Prove a sharper explicit bound by a local classification of possible
crossing thresholds. Interior extrema cannot change a crossing; only
saddles can. On vertical target edges the candidate must be a tangential
maximum with positive inward derivative; on horizontal edges it must be
a tangential minimum with negative inward derivative. At each corner
only one of the four derivative-sign patterns is eligible. Establish
these statements by local surgeries and then count eligible points by
marked Kac–Rice. This is the local part of the preceding report's
pivotality suggestion, with no unproved macroscopic arm estimate.
It should sharpen the boundary constants and discard an O(|u|^5)
interior contribution near zero, but should not change the R^(-2)
sufficient level scale. The signs, especially at corners, need audit.

## Prior-script rerun and deterministic lemma

Command (read-only execution in the old folder):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T064/check_level_stability.py
```

Output: actual niceness 20; total interior intensity 0.091888149237;
saddle intensity 0.045944074618; edge intensity 0.275664447711;
conditional determinant error 5.394e-11; edge conditional-mean error
7.527e-14; I and J errors 3.469e-18 and 1.388e-17.
`PASS; elapsed=0.077s; peak RSS=12.78 MiB`.

Opened Definition 2.7, Lemma 2.9 and Lemmas B.4–B.5 of the full
arXiv:2010.11770v3 paper. B.4 supplies a crossing path strictly above
the threshold except at its unique threshold location. This makes
the local sign classification particularly direct: if its two arms
can be joined locally in the strict superlevel, or its endpoint can
be moved onto the target edge in that superlevel, it was not a threshold.
For an edge normal form +/-r +/-s^2 (r inward), only -r+s^2 has
two positive components; only r-s^2 has positive access to the edge
point without access to a nearby point on that edge.

Provisional resulting dominating height density, for Q=[0,L]x[0,H]:

    D(t) = A phi(t) exp(-t^2)/(4 pi)
         + P beta(t)/4 + (H-L) t phi(t)/(4 sqrt(pi)) + phi(t).

The total edge term is nonnegative despite its signed representation:
it is a sum of two one-sided Gaussian means. The corner coefficient
is 1, since each of four corners has one eligible gradient quadrant
of conditional probability 1/4. Next: independent quadrature,
orientation reversal, thin-rectangle and corner audits.

## Proof and independent audit, 04:39

Created PROOF.md and check_local_threshold.py. The proof gives the
local classification, conditional one-point counts, the exact
interval bound and its integrated form. It also proves that the
corner coefficient 1 cannot be reduced in a bound with fixed area
and perimeter densities: shrink a rectangle to a point, when its
crossing threshold converges almost surely to the field value there.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_local_threshold.py
```

Complete substantive output (the shell also prints the same priority
warning; actual niceness is independently checked):

```text
niceness=20; threads=1; CPU cap=60s
conditional jets / signed edge max error=5.305e-10
corner eligible quadrant=0.250000000000; four-corner factor=1.000000000000
24 interval / orientation / prior-I audits; max error=5.107e-15
644 pointwise positivity / domination / duality audits passed
total saddle density=0.045944074618
vertical eligible: +normal,-tangent: grid threshold=0.000000
vertical excluded: +normal,+tangent: grid threshold=0.250000
vertical excluded: -normal,-tangent: grid threshold=-2.000000
vertical excluded: -normal,+tangent: grid threshold=-1.750000
horizontal eligible: -normal,+tangent: grid threshold=0.000000
horizontal excluded: +normal,+tangent: grid threshold=2.000000
horizontal excluded: +normal,-tangent: grid threshold=1.750000
horizontal excluded: -normal,-tangent: grid threshold=-0.250000
affine a=-1.3 b=-0.7: grid=-1.300000; exact=-1.300000
affine a=-1.3 b=+0.7: grid=-0.600000; exact=-0.600000
affine a=+1.3 b=-0.7: grid=0.000000; exact=0.000000
affine a=+1.3 b=+0.7: grid=0.700000; exact=0.700000
square u=R^(-3), prior and refined bounds:
  R=10: old=0.00731019492568; refined=0.00420855888845
  R=100: old=0.000344461403166; refined=0.000324216485545
  R=1000: old=3.200238828e-05; refined=3.18107105453e-05
small square d=.1; refined bound approaches Phi(.1)-Phi(0):
  R=0.1: bound=0.040495413801; Gaussian=0.039827837277
  R=0.01: bound=0.039891751938; Gaussian=0.039827837277
  R=0.001: bound=0.039834200313; Gaussian=0.039827837277
PASS; elapsed=0.178s; peak RSS=13.19 MiB
```

The quadrature uses midpoint extrapolation rather than the predecessor's
Simpson rule. It directly integrates the exponential determinant tail
and both truncated Gaussian means before comparing to the closed forms.
The finite-grid maximum-capacity path calculation independently checks
all four edge sign patterns in both orientations, and all four affine
corner cases. Those grid examples audit signs only; they do not prove
the general continuous result.

## Attempts to break the result

1. Tested very thin rectangles in both orientations and positive/negative
   levels. The signed term in D cannot be discarded; it changes sign
   under t -> -t or L <-> H. The full expression stays nonnegative
   because it is the sum of two one-sided expectations.
2. Checked D_{L,H}(t)=D_{H,L}(-t) both algebraically and numerically.
3. Checked pointwise domination by the earlier density, including
   |t| up to 8, and directly integrated the old alpha to recheck I.
4. Checked corner signs by the exact affine maximin formula; excluding
   every corner would fail even for linear functions. The shrinking-
   rectangle argument independently forces the total corner constant
   to be at least 1.
5. Re-expanded alpha-s near zero: its leading term is phi(0)t^4/(8 pi),
   whose integral is phi(0)d^5/(40 pi), not order d^3. Thus removing
   extrema does not reduce the leading area contribution.
6. Rechecked local path surgery: a strict path is compact, so moving
   it off the threshold point gives a crossing at a strictly higher
   level. Endpoint moves must stay on the same vertical target side;
   horizontal edges cannot be treated as target edges.

No failed numerical checks. A misleading draft comment about an
address-space limit was removed: the script enforces CPU and priority
and reports actual RSS; it does not impose a virtual-memory cap.
All allocations are small and bounded by the fixed 41x41 grid and
constant-memory quadrature. No heavy experiment was run.

## Final artifact audit

Created REPORT.md with the required first-line verdict. Reread the
complete round-3 log in a bounded command to recover any text hidden
by the initial combined-output truncation, and read back REPORT.md.
Rechecked the load-bearing factors directly: saddle determinant tail
e^(-t^2)/4 times gradient density 1/pi; edge sign probability 1/2
times one-sided second-derivative mean; four corner quadrants of
probability 1/4 each. Formula (14) has vertical length 2H and
horizontal length 2L; its asymmetry coefficient is H-L.

Final script run used the identical command above and reproduced all
constants, examples and comparisons. Its final line was
`PASS; elapsed=0.191s; peak RSS=13.11 MiB`.
No mathematical or script changes followed that run. The four new
deliverables are REPORT.md, PROOF.md, LOG.md and check_local_threshold.py.
The corner-sharpness argument and the remaining R^(-2) limitation are
included in the report. No SOLVED_ELSEWHERE.md was created because the
scaling-limit problem was not found solved.

Task completed: “take the NEXT checkable step on this problem, building
on that work” — received 15 November 2026, 04:33 Asia/Tbilisi.
