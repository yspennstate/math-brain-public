# T248 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First clock reading: 15 November 2026, 08:52:40 +04 (04:52:40 UTC).

## Orientation and literature check

All writes stay in this folder. The task-specific restriction overrides the
global brain, checklist and mesh write rituals, which mutate other folders.
Read the startup memory and compute state: `warn`, `owner_away_open`, CPU
saturated. No heavy computation, subagents, git or external writes are planned.
Read the original session's REPORT.md, LOG.md and SOLVED_ELSEWHERE.md (there
is no PROOF.md or script there); read the round 3 and round 4 REPORT.md,
LOG.md, PROOF.md and both verification scripts. Original folders are read-only.

The literature check, within five minutes of the first clock reading, used
the web search tool with queries:

- `"conjugate kernel" "Tracy" 2026`
- `"2610.41416" Chen Lyu Tracy Widom`
- `random neural networks edge universality Tracy Widom nonlinear 2026`
- `"random features" "Tracy-Widom" "2026" edge`
- `"conjugate kernel" "universality" November 2026`

Opened the arXiv page and full HTML of Guangchen Chen and Xing Lyu,
*Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, arXiv:2610.41416v2, and the full HTML of Renyuan Ma and
Theodor Misiakiewicz, *The anisotropic local law for sample covariance
matrices under quadratic-form concentration*, arXiv:2609.09440v2.
Chen–Lyu's current page still lists v2, revised 4 November 2026. Read its
Assumptions 1.1–1.2 and edge definitions; the theorem used by the predecessors
has not changed there. No newer solution of the full T248 statement was
found. This is a bounded search, not a claim of exhaustive coverage.

## Independent audit in progress

The round 4 covariance identity has been re-derived from the Gaussian
Hermite generating function. Its fourth-trace calculation has the three
closed-walk patterns pair, star and four-cycle, with multiplicities
`(N)_2`, `2(N)_3`, `(N)_4`. An independent exact computation and a rerun
of the earlier script will be recorded next, before choosing an extension.

## Round 4 audit: holds

Re-ran the round 4 script read-only, suppressing bytecode writes:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T248/verify_subcritical.py
```

Relevant complete output:

```text
nice: setpriority: Operation not permitted
Predecessor rational cancellation identity: 3 exact checks passed
Spherical sixth and centered eighth moments: exact checks passed
d=2: coordinate integrations pair/star/cycle = 3/128, 1/64, 1/128
d=3: coordinate integrations pair/star/cycle = 16/945, 16/2025, 16/10125
Fourth-trace walk multiplicities: exhaustive n=2,...,7 passed
r=0.25: n*(edge-e0)=0.562485236; independent first-order coefficient=0.562500000
r=0.5: n*(edge-e0)=1.030297487; independent first-order coefficient=1.030330086
r=2: n*(edge-e0)=4.121100777; independent first-order coefficient=4.121320344
r=4: n*(edge-e0)=8.999325151; independent first-order coefficient=9.000000000
Edge solver maximum disagreement: 1.776e-15
Subcritical / critical / supercritical pole signs: passed
Transposition normalization: both rectangular orientations passed
PASS: exact algebra and scalar edges only; elapsed 0.023s
```

The priority warning occurred again, but the script's guard checked an
effective nice value of at least 15 before doing any computation. It exited
successfully. Independently checked the proof: covariance trace cancellation
is exact; the fourth-trace identity gives an operator remainder tending to
zero; the scalar stationary point has pole margin positive precisely when
`q alpha sqrt(b)<v`; the finite-dimensional edge shift is `O_p(N^-1)`.
Read the external theorem through Corollary 1.4 and Remark 1.5 on the opened
arXiv HTML. Its stated assumptions match the conditional application. No
error in the round 4 result was found. This audit accepts the cited theorem
as an external input and does not referee its proof.

## Selected extension, before doing it

Prove TW1 for the explicitly projected kernel

    K_P = Y(I-ee^T)Y^T/N,  e=1/sqrt(N) (1,...,1)^T,

for spherical inputs, a fixed Lipschitz activation with `a_0=a_1=0`, and
`b!=1`, with no condition on the size of `q=a_2^2`. This is the next step
named by round 4. Projection kills its isolated quadratic covariance spike,
including at criticality and in the supercritical regime. It preserves
independence across feature rows and their quadratic-form concentration.

Two details need proof: work in dimension `N-1` rather than applying a
positive-definite covariance theorem to a singular `N`-dimensional matrix;
and replace exact trace cancellation (lost after projection) by a bounded
trace defect plus a bounded squared Hilbert–Schmidt defect. Both should
give a covariance-edge displacement `O_p(N^-1)`, negligible at TW scale.
This extension makes no claim about the second eigenvalue of the original
unprojected kernel. Interlacing will be recorded only as a bound.

## Proof written

Created PROOF.md with a complete conditional argument for the chosen
projected model. The covariance on an orthonormal basis Q of `e^perp` is

    T=Q^T Sigma Q=(v-q/d)I_(N-1)+q Q^T B Q+Q^T R Q.

Thus `||T-vI||_op=o_p(1)` without a subcriticality assumption. The exact
trace defect is `Tr(T-vI)=-e^T(Sigma-vI)e=-q(N-1)/d+o_p(1)`; its squared
Hilbert–Schmidt defect is bounded by `Tr((Sigma-vI)^2)=O_p(1)`. A proved
edge lemma retaining both the mean defect and its second moment gives
`E_T-v(1+sqrt((N-1)/m))^2=O_p(N^-1)`. Uniform high-probability design
events justify integration of the conditional Chen–Lyu conclusion.

The exact scalar reference for normalization by N is

    Etilde=v(sqrt(m/N)+sqrt((N-1)/N))^2,
    gtilde=(b_N c_N)^(1/6)/(v(sqrt(b_N)+sqrt(c_N))^(4/3)),
    c_N=(N-1)/N.

Its center differs from the round 4 center by `O(N^-1)`. The proof also
re-establishes the fourth-trace bound and quadratic-form concentration,
so it does not require copying a proof file from the earlier folders.
Next: independent algebra checks of projection and normalization, and
failure examples for the inferences the proof deliberately does not make.

## Independent verification and attempts to break the extension

Created `verify_projection.py`, a standard-library script with matrices of
size at most eight, an effective-priority guard, and a 60-second budget.
The compute state was read again before running it: `ok`, `owner_away_open`.
Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_projection.py
```

Complete output:

```text
nice: setpriority: Operation not permitted
Effective nice value: 20
Exact rational P^2=P, trace, Frobenius identity, and spike removal:
  N=2,...,8 and q=0,2/7,3/4 all passed
Independent Fourier integrations at d=2: pair=0.023437500000, star=0.015625000000, cycle=0.007812500000
Cosine covariance: characteristic-function / Hermite max error 2.776e-17
  quadratic spike ratio q*alpha*sqrt(b)/v=0.460336797; projection identity independent of ratio
  quadratic spike ratio q*alpha*sqrt(b)/v=1.000000000; projection identity independent of ratio
  quadratic spike ratio q*alpha*sqrt(b)/v=7.365388754; projection identity independent of ratio
Nonzero-trace edge lemma: max solver disagreement 1.776e-15
  linear-mean / quadratic-variance expansion max relative error 3.415e-05
Projected N-1 normalization in both orientations: scale error 2.220e-16, center error 3.553e-15
Trace-defect sign: n*(shifted-reference)=-1.748455710; limit coefficient=-1.748528137
Interlacing failure example: lambda1(K)=104, lambda1(K_P)=4, lambda2(K)=3
  The projected top cannot be identified with the original second by interlacing.
PASS: algebra checks only; elapsed 0.026s; peak RSS 13.8 MiB
```

The new script independently checks the predecessor's pair/star/cycle
constants by Fourier integration on the circle, rather than its coordinate
polynomial integrations. It checks projection identities exactly over the
rationals, and confirms the quadratic covariance coefficient for a bounded
Lipschitz cosine activation both from a characteristic function and its
Hermite series. Scalar edge solvers use derivative bisection and direct
minimization, agreeing within 1.776e-15. The nonzero-trace expansion retains
both positive and negative mean defects. Three separate expressions agree
for projected centering/scaling, including the singular-value formula.

Two tempting failures were confirmed rather than ignored: a pure projected
constant population shift has a negative edge defect (so a universal
nonnegative-shift assertion would be wrong), and rank-one interlacing
allows an order-one gap between the projected top and the original second
eigenvalue, even with a separated top eigenvalue. The b=1 entry in the
script checks only threshold algebra, not universality; the theorem still
excludes b=1. No TW simulation or finite-size outlier law was inferred.

The launcher warning is harmless here because the process explicitly
measured nice value 20 before working. Peak RSS was 13.8 MiB, execution
took 0.026 seconds, and no arrays grew with the scalar large-N values.

## Document and proof audit

Read PROOF.md back in full. Restored inline math delimiters after the
initial tool-string escaping removed some backslashes; the one-time
folder-local formatting command used guarded `nice -n 15 python3 -B -`
with the same one-thread environment. It printed 158 parenthesized
expressions restored, 49 opening and 49 closing display delimiters, and
effective nice value 20. Corrected four delimiters crossing line breaks
by patch. No mathematical statement or computation changed.

Rechecked the load-bearing orders: `E Tr B^4=O(N^-1)` gives failure
`O(N^-1/2)` at threshold `N^-1/8`; the R bound gives `O(N^-3/4)`;
the squared-defect threshold `N^1/6` gives `O(N^-1/6)`. On the retained
design event the edge perturbation is `O(N^-5/6)`, and multiplying by
`m^(2/3)` gives `O(N^-1/6)`. The sharper stochastic bound remains
`O_p(N^-1)`. Both exponents are strictly below the required edge scale.

Finalized REPORT.md with the explicit theorem, source, checks, scope,
failed shortcuts and next comparison target. No additional numerical
run was needed after the successful checks because only document
formatting and the report changed.

Final read-only checks at 09:01:50 +04: a guarded, one-thread, low-priority
Python document check confirmed 49 matched display equations, balanced
inline math on every line, no unintended control characters, the required
first-line verdict, and the four artifacts. It printed `PASS: final
document delimiters, verdict, and artifact checks`. Read REPORT.md back
in full and the end of LOG.md. Refined one report sentence to distinguish
negative corrections allowed by the general edge lemma from a sign
theorem for this network, which is not claimed. The reported research
result and computational output are unchanged. Task complete.
