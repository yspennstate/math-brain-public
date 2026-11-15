# T133 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 08:29 Asia/Tbilisi (04:29 UTC).

## Orientation and bounded literature check (04:29–04:32 UTC)

Read the original REPORT.md, LOG.md and SOLVED_ELSEWHERE.md; that
directory contains no PROOF.md or scripts. Read the round 3 and round 4
reports, logs and proofs; their scripts are being read before computation.
All earlier directories are read-only. All new writes stay in this folder;
the task-specific restriction therefore rules out global mesh, checklist,
recall logging and memory updates outside it. Startup memory and compute
state were read directly. No git, subagents or external messages.

Governor: status warn, mode owner_away_open, CPU saturated. Workloads will
be small, single-threaded and launched under the requested nice prefix.
The shell prints `nice: setpriority: Operation not permitted`; earlier
workers measured inherited nice 20. Verify this inside our own script.

Web search queries (completed within three minutes):

- `six vertex arctic curve proof Bufetov 2609.20576`
- `six vertex domain wall arctic curve disordered regime proof 2026`
- `"2609.20576" proof`
- `"six-vertex" "arctic" "proof" "2026" Bufetov`

Opened https://arxiv.org/abs/2609.20576 and
https://arxiv.org/html/2609.20576v1. Alexey Bufetov, *Limit shape for
domain-wall six-vertex model*: submission history still lists only v1,
17 September 2026. Its abstract says announcement; Theorem 3.2 covers
-1 < Delta <= 1/2, and Remark 3.3 omits 1/2 < Delta < 1. The inspected
note supplies statements and a strategy, not complete proofs. No later
complete solution was found in this bounded check. This does not certify
absence from the literature; the stop-on-solved rule is not triggered.

## Earlier-result audit in progress

Re-derived round 4's identity from C(0)=e(0)a''(0)/a(0)-e''(0):

`2 pi C = E(R-q) + h cot(hT/2)(h^2 qh-q)`.

Here E=cot(T/2)-h cot(hT/2), q=1/(1-cos T),
qh=1/(1-cos(hT)), h=pi/(pi-gamma). Factoring the two cosine
denominators gives `R-q = tan(w)(tan(w)-tan(v))/2`, with
v=(gamma+u)/2 and w=(gamma-u)/2. For u>=gamma it is nonnegative;
the other two differences are strictly positive. Thus the earlier
midpoint sign proof holds algebraically. The collar Jacobian follows
independently from X0'=C(b,-a)/W and (a,b).V=C/2:
`det[V,X0']=-C^2/(2W)`. Numerical independent recheck follows.

## Independent recheck passed

Read all three earlier scripts in full and the remaining round 3 proof.
Wrote recheck.py independently, using high-precision symmetric finite
differences in addition to analytic differentiation. It does not import
or execute earlier code. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
```

```text
PASS earlier midpoint sign/decomposition/collar checks: 25
max relative finite-difference error: 2.948028402980549e-26
max relative decomposition error: 5.944128499161529e-60
resources: elapsed_seconds=0.0342 nice=20 peak_rss_MiB=18.984375
```

The earlier result holds. Cases include u=gamma, gamma near zero and
pi/2, and u very close to delta. Data: recheck.json.

## Choice of extension, before doing it

Target the complete sign C(theta)>0 at the particular omitted-regime
parameter gamma=pi/4 (Delta=1/sqrt(2)), for all 0<u<3pi/4 and
|theta|<3pi/4-u. This includes the previously missing weights u<gamma
and every interior point of each candidate arc. The local critical-branch
collar then follows by the same Jacobian argument. Commensurate angles
permit exact rational formulas after a tangent substitution; an explicit
polynomial sign certificate would be independently checkable. This is a
single special-case geometry extension, not a convergence theorem.

Preliminary exploration of the general midpoint identity confirmed that
R-q is negative at u<gamma while C remains positive in the sampled
cases. A conjectural stronger comparison e''/e < 1/(1-cos(delta+u))
was positive-regime plausible but fails at gamma=2.4. No general inequality
is asserted. Prefer an exact special-case certificate over extrapolating
those samples.

## Rational reduction obtained

Set p=(T+theta)/6, q=(T-theta)/6, x=tan p, y=tan q.
Then x,y>0 and x+y+xy<1. At gamma=pi/4 the normalized
coefficients are 2pi*a=A(x), 2pi*b=A(y), 2pi*e=f(x)+f(y), where

`A(x)=(1+x^2)^3/[2x(x-1)(x^2-3)(x^2+4x+1)]`,

`f(x)=x(x^4+7)/[6(x-1)(x+1)(x^2-3)]`.

The theta derivative is [(1+x^2)d_x-(1+y^2)d_y]/6.
Wrote derive_certificate.py to compute the exact rational C using this
operator. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 derive_certificate.py
```

Exit 0, elapsed 2.656 seconds. Full exact factorization is saved in
rational_curvature.txt. Its residual symmetric polynomial has bidegree
(12,12); its ordinary coefficients have mixed signs, so this alone is
not a sign proof. Investigating a rational parametrization of the entire
domain by the positive quadrant. One exploratory print failed because
SymPy Boolean values cannot be added with Python sum; changed the count
to sum(int(c>0) ...). It did not alter the rational calculation.

## Positive-quadrant certificate found

The transformation x=r/(1+r), y=t/[(1+t)(1+2r)] is a bijection
from r,t>0 to x,y>0, x+y+xy<1. After multiplying the residual
polynomial -P by (1+r)^12(1+t)^12(1+2r)^12, every nonzero
coefficient is positive: 324 entries, minimum 63, maximum
692394213766656. The single missing entry is the constant term.
The previous print needed Python conditional filtering rather than int
on a SymPy Boolean; the corrected exploratory run exited 0.

This gives a candidate exact sign proof on the whole open domain.
Next: generate a complete integer certificate and independently verify
both the rational curvature numerator and this polynomial substitution
with a separate standard-library integer-arithmetic implementation.
Also compare the rational formula with numerical derivatives of the
original trigonometric functions, including near the parameter edges.

## Two independent exact checks passed

Extended derive_certificate.py to save certificate.json (complete integer
coefficient arrays), curvature_polynomial.txt and positive_quadrant_polynomial.txt.
It now prints a compact summary. Same command as above:

```text
PASS exact rational certificate:
Q_bidegree=[12,12], R_bidegree=[24,12]
positive_coefficients=324, zero_coefficients=1
minimum_positive_coefficient=63
maximum_coefficient=692394213766656
coefficient_sum=17765219441341512
elapsed_seconds=6.119, peak_rss_MiB=72.953125, nice=20
```

Wrote audit_certificate.py using only the Python standard library.
It reconstructs the curvature numerator with polynomial differentiation
and integer multiplication, then verifies the substitution by independent
binomial sums. It does not import SymPy or execute the derivation script.
The initial denominator clearing used too small a power for mixed terms
with i+j=3; an assertion caught it. Corrected the common denominator from
d^4(1+x)^3 to d^5(1+x)^3; no claimed identity was weakened.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_certificate.py
```

```text
PASS independent integer numerator identity and all coefficient signs
numerator_monomials=1211, positive_coefficients=324
minimum_positive_coefficient=63, maximum_coefficient=692394213766656
coefficient_sum=17765219441341512
elapsed_seconds=0.02994, peak_rss_MiB=15.890625, nice=20
```

The finite exact certificate is a proof of the rational sign, rather than
a sample-based sign claim. The separate trigonometric check is now running.

## Trigonometric and geometric audit passed

Wrote verify_geometry.py without importing the symbolic generator. It
compares the integer certificate with numerical derivatives of the original
trigonometric coefficients, differentiates the closed envelope independently
to check x0'>0, y0'<0 and f''=W^2/(Cb^3)>0, and verifies the collar
Jacobian. The 63 cases include u/delta=10^-6 and 1-10^-6,
and theta/T=+/- (1-10^-6), as well as both sides of u=gamma.

The first run at 100 digits failed the fixed 1e-70 coefficient-identity
tolerance when u/delta=.999999, theta/T=-.999999: relative error
1.0026e-66. Here separate pole terms cancel severely. Increasing to
160 digits, without relaxing any tolerance, resolved it.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py
```

```text
PASS trigonometric/rational/tangent/convexity/collar checks: 63
maximum rational curvature relative error: 3.2568557259319356e-127
maximum coefficient relative error: 3.2568557259419804e-127
elapsed_seconds=5.1442 nice=20 peak_rss_MiB=19.96875
```

Wrote PROOF.md: full rational reduction, explicit Q coefficient table,
positive-quadrant substitution, integer recurrences certifying the numerator,
and graph/collar consequences. Strict C>0 and W>0 give x0'>0 along the
whole arc, which also gives uniform small-B injectivity on compact subarcs
by compactness. Endpoints and distant critical points are excluded.

An additional finite-B check is being run from the integral itself, using
scalar Neumann iteration and analytic derivatives of the rescaled kernel.

## Finite-B audit passed

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_branch.py
```

Four cases use u/delta=.05,.2,.5,.9 and nonzero theta/T=.4,-.6,.3,-.5.
The first two are outside round 4's sufficient midpoint weight range.
At B/scale=.04,.02,.01, the computed critical point lies strictly above
the candidate graph. This tests the normal side rather than requiring
both coordinate displacements to be positive: at u/delta=.05 the predicted
x displacement is negative, and at .2 the predicted y displacement is
negative, as is allowed by the nonzero tangential component.

Material output:

```text
u/delta=.05 extrapolation_relative_error=5.842331185778537e-7
u/delta=.2  extrapolation_relative_error=7.658357224690807e-6
u/delta=.5  extrapolation_relative_error=1.4324428513598208e-6
u/delta=.9  extrapolation_relative_error=4.800227784826225e-6
maximum 64-to-128-node refinement error=5.919570389423257e-14
all 12 graph gaps positive
PASS finite-B displacements and convex-side checks: 4
elapsed_seconds=0.1988 nice=20 peak_rss_MiB=20.109375
```

Full coefficients, observations, normal gaps and refinement data:
branch_checks.json. Neither this script nor any other task script imports
or executes an earlier worker's code. All task outputs are in this folder.

## Final audit and result

Created REPORT.md with the required first-line verdict and explicit scope:
the candidate geometry is proved at Delta=1/sqrt(2), for all positive
weight ratios; T133 is not proved. PROOF.md now also checks that
sin(T)/sin(u) decreases from infinity to zero over the full u interval.

Final audit command was a bounded Python script under the same env/nice
prefix. It parsed all five task scripts with ast.parse, checked Markdown
for control characters, reconstructed the complete Q matrix from the
triangular table in PROOF.md and compared it with certificate.json, checked
every row minimum in the proof's R table, checked the report verdict, and
compared the independent exact coefficient summaries. Output:

```text
syntax OK: audit_certificate.py derive_certificate.py recheck.py
           verify_branch.py verify_geometry.py
recheck.json: 25 checks
geometry_checks.json: 63 checks
branch_checks.json: 4 checks
PASS final proof-table, sign-summary, verdict and artifact audit
```

Load-bearing signs were checked with exact symbolic differentiation,
independent integer polynomial arithmetic, and numerical derivatives of
the original formulas. The normal displacement was also checked by direct
finite-interval quadrature. At nonzero theta its tangential part can make
one coordinate decrease; the graph-side test correctly remains positive.
Near u=0, u=delta or theta=+/-T, no uniform collar size or endpoint
statement is inferred from the open-domain result.

Next checkable step: compute and match joining-point limits at gamma=pi/4
to determine whether the four open-arc collars extend to a collar of a
simple closed convex candidate curve. A general-gamma sign representation
remains a separate extension. All earlier files were left unchanged.
