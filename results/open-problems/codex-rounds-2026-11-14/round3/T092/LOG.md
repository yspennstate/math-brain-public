# T092 work log

Started 2026-11-15 01:20 +04 (Asia/Tbilisi).
Task: “take the NEXT checkable step on this problem, building on that work.”

## Startup and constraints

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in
`~/codex_op_1114/briefs/T092`. That directory contains
no PROOF.md or computation scripts. The previous result is a claim notice,
not a verified construction. All writes in this session stay in the current
folder; no global brain, mesh or checklist writes, git, or subagents.

Read the compute-state file: status `warn`, CPU 99.7%, mode
`owner_away_open`. No heavy computation or Lean build is planned.
The shell prefix `env OMP_NUM_THREADS=1 nice -n 15` reports
`nice: setpriority: Operation not permitted` but still executes tiny file
reads. Do not launch substantive computation without the required priority.

Commands: `pwd`; `ls -la` on the old/current folders; `cat` on the old
reports and compute state; `rg --files` to locate startup memory;
`date '+%Y-%m-%d %H:%M:%S %z'` -> `2026-11-15 01:20:54 +0400`.

## Initial literature check

Web search queries: `"A smooth three-torus diffeomorphism with simple
Lebesgue spectrum"`; `"Banach" "simple Lebesgue" "2026" solution`.
The same OpenAI preprint is still returned, along with secondary commentary.
These search results do not certify it. Next open the primary theorem and
the solution dependencies named by the earlier report. Literature status
checking is limited to five minutes; the subsequent work is proof auditing.

## Chosen extension

Audit the named Lean theorem's mathematical definitions and dependencies,
beginning with `exists_physical_basis` and `mainConclusion_of_basis`.
This is the earlier report's explicit next step. The aim is one checkable
result: determine whether a concrete dependency supplies the claimed
finite-probability construction or assumes its essential content. A
source-level audit is feasible without a resource-intensive Lean build.

## Earlier result independently rechecked

Opened the primary introductory TeX and `Main.lean`, comparator JSON,
`SpectralTransport.lean`, scope note and citation README through the web
tool. The author and date are OpenAI, September 23, 2026; no arXiv id was
located. The main source invokes `exists_physical_basis` and transports
its basis to the standard torus. This confirms the earlier report's scope
and artifact identification.

Independent check by Fourier coefficients: for a unitary U and a unit
vector f with a complete bilateral orthonormal orbit, define
`Vg(z)=sum_n <g,U^n f> z^n` (inner product linear in its first argument).
Parseval makes V an onto isometry, and reindexing gives VUg=zVg.
Conversely, pull back the Fourier basis under such an equivalence. Thus
the earlier mathematical equivalence holds, independently of its
finite-linear-combination argument. This verifies scope, not existence.

Additional status queries: `"A smooth three-torus" error gap review` and
`"simple_lebesgue_spectrum" "exists_physical_basis"`. No independently
validated resolution appeared. Stop general status searching here, within
five minutes of startup. Continue only the selected primary-source audit.

## Dependency trace, first segment

Web-opened `PhysicalBasis.lean`, `DynamicsLimit.lean`, `SmoothLimits.lean`,
and the comparator challenge's definitions. Recorded source chain:
`Main -> SpectralTransport -> PhysicalBasis -> DynamicsLimit ->
SmoothLimits -> Stages`.
`exists_physical_basis` uses a countable total family of continuous real
tests, repeats each test at errors 2^-m by Nat.pair, and calls
`exists_physical_limit`. That limit calls `exists_stage_diagonal`, whose
successor step calls `StageState.exists_step`. This has reached a specific
finite-stage producer rather than an assumed limiting basis. No gap found
in the checked scope or the elementary repeated-test closure argument.
The entire dependency closure has not been checked.

## Precise mathematical piece selected from the audit

The source trace now reaches `Stages.exists_one_stage`, which calls
`exists_predicted_whitening`, then `actual_controlled_tagged_prediction`
in ControlledBlocks. Source inspection alone will not certify that
construction. Rather than report another unverified top-level proof body,
the selected audit will establish a quantitative necessary condition on its
finite prediction output.

Choice: prove a lower bound on the number of orbit terms needed to
approximate an observable that was invariant under the preceding twist.
For a flat vector g of the new map R, target h of norm H, residual
`b=||h o R-h||_2`, and approximation error ε<H, the proposed bound is
`#supp(P) >= (H^2-ε^2)/(H b)` when b>0. This will be proved before any
numerical use. It tests the arbitrary-closeness quantifier in the stage:
as the new map approaches an old map fixing h, its Laurent polynomial
must acquire more terms. It does not contradict a stage theorem that
allows unbounded polynomials.

This remains one extension of the earlier result: a quantitative audit
condition for the finite construction, with the dependency trace serving
to identify where it applies. The diagonal and finite-stage existence
claims themselves will not be certified.

## Result proved and saved

Wrote PROOF.md. For U unitary and g with orthonormal bilateral orbit,
the coefficients a_n=<h,U^n g> satisfy, by two applications of Bessel,
`sum |a_n|^2 <= H^2` and `sum |a_(n+1)-a_n|^2 <= b^2`, where
`H=||h||` and `b=||Uh-h||`. Telescoping from both ends and
Cauchy--Schwarz give `sup |a_n|^2 <= H b`. Orthogonal projection onto
the terms of a polynomial then gives
`#supp(P) H b >= H^2-ε^2`.

Independent verification: Fourier transform the coefficient sequence;
weighted Cauchy--Schwarz with weight `lambda+4 sin^2(pi t)` gives
`|a_k|^2 <= (lambda H^2+b^2)/sqrt(lambda(lambda+4))`.
Taking `lambda=b^2/H^2` implies the same coefficient bound. The integral
was evaluated by `x=tan(pi t)`, not numerically.

Sharpness check for the coefficient constant: `a_n=r^|n|` gives
`||a||^2=(1+r^2)/(1-r^2)` and
`||Delta a||^2=2(1-r)/(1+r)`; their norm product tends to 1 as r tends
to 1, while `a_0=1`. Re-derived the second sum from the adjacent-product
identity as well as directly from its two geometric half-line sums.

For the old twist and target `h=sin(2 pi u)`, a forward map perturbation
of uniform size δ has `b<=2 pi δ`. At error `||h||/2` this forces
`#supp(P)>=3/(8 sqrt(2) pi δ)`.
Re-derived `||h||^2=1/2` from both the double-angle identity and its
two Fourier coefficients. Checked the final constant a second way after
normalizing h to norm one. No floating-point numbers are used.

## Attempts to break the result

- If b=0, all orbit coefficients vanish: approximation below ||h|| is
  impossible. The proof handles this before dividing.
- Completeness of the orbit is unnecessary: both Bessel bounds and the
  finite-dimensional projection remain valid in a proper cyclic subspace.
- Sparse Laurent polynomials with very large exponents are covered by
  the support-count bound. Degree alone cannot bypass it.
- Complex coefficients and negative powers are included. Rechecked the
  inverse in `a_(n+1)-a_n=<U^-1 h-h,U^n g>`; its norm equals b.
- The estimate is independent of coefficient size and closeness of the
  old and new generators. It requires exact orthonormality of the new
  orbit, which the claimed whitened stage supplies.
- The bound concerns forward map closeness only. After a changing chart,
  use the physical target's Lipschitz constant; no uniform chart bound is
  asserted.
- A bounded-degree version of the stage would fail as δ tends to zero.
  The actual stage does not impose bounded degree or bounded support, so
  no contradiction with it has been established.

No computation script, numerical sweep, or Lean compiler was run. All
mathematical verification was symbolic; resource limits were respected.

## Final saved-file verification, 01:27 +04

Created REPORT.md and CLAIM_AUDIT.md with the theorem, scope, source trace,
limitations and next finite-block audit. Did not create SOLVED_ELSEWHERE.md:
no resolution was independently established.

Commands and important output:

```
env OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md REPORT.md CLAIM_AUDIT.md
nice: setpriority: Operation not permitted
152 LOG.md
230 PROOF.md
73 REPORT.md
33 CLAIM_AUDIT.md
488 total

env OMP_NUM_THREADS=1 nice -n 15 head -n 1 REPORT.md
nice: setpriority: Operation not permitted
VERDICT: PROVED a necessary orbit-count bound for finite-stage approximations near an invariant observable

env OMP_NUM_THREADS=1 nice -n 15 date '+%Y-%m-%d %H:%M:%S %z'
nice: setpriority: Operation not permitted
2026-11-15 01:27:18 +0400
```

The LOG.md line count precedes this appended verification entry. The
niceness restriction still prevents substantive local computation; the
listed commands are only tiny read-only checks. Rechecked the proof's
division cases and the distinction between optimality of the coefficient
constant and optimality of the orbit-count bound.
