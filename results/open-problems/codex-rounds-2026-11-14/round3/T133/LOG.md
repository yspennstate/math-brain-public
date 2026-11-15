# T133 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 01:33 Asia/Tbilisi (UTC+4).

## 01:33–01:37: orientation, earlier result, bounded literature check

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in
`~/codex_op_1114/briefs/T133`. Directory listing confirms
that the earlier worker left no PROOF.md or computation scripts. No earlier
files were edited. Read startup memory and compute state directly. The
task-specific prohibition on writes outside this directory overrides the
global instructions to update the mesh, checklist and memory stores; those
commands were not run. No git, subagents or external messages.

Web queries (under five minutes):

- `"Bufetov" "Limit shape for domain-wall six-vertex model"`
- `"2609.20576" proof`
- `six vertex arctic curve general weights proof 2026`
- `"Alexey Bufetov" "domain-wall" "full proof"`
- `"six-vertex" "limit shape" "2026" "arctic" proof Bufetov`

Opened https://arxiv.org/abs/2609.20576 and
https://arxiv.org/html/2609.20576v1, including its definitions, theorem
section and history. Author: Alexey Bufetov. The abstract page lists only
v1 (17 September 2026); its abstract explicitly says this is an announcement.
The ranges remain Delta < -1 and -1 < Delta <= 1/2. No full proof or later
version was found in this bounded check. Thus there is no new solved-elsewhere
result triggering the stop rule. Absence from this search is not proof of
absence from the literature.

Independent recheck of the earlier result: arXiv submission history, the
abstract, theorem ranges, and the formulas for the outer boundary agree with
the earlier transcription. The earlier result holds as a report about an
announcement, not an independent proof of its announced theorems.

Resource check:

```sh
env OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("effective_nice", os.getpriority(os.PRIO_PROCESS, 0))'
```

Output: `nice: setpriority: Operation not permitted`; `effective_nice 20`.
The inherited process is already at priority 20, lower than the requested
15. Use the required launch prefix for computations. Governor says `warn`,
`owner_away_open`, CPU saturated. Only short single-thread checks are planned.

## Choice before doing the extension

Prove a deterministic analytic lemma for the disordered Fredholm kernel,
especially the omitted range 1/2 < Delta < 1: a strict contraction bound,
well-defined linear determinant functional, and its small-B expansion giving
the envelope equations. This tests whether loss of operator invertibility
could explain the announced parameter restriction. It also turns the note's
formal small-B boundary prescription into a locally controlled analytic
statement. It does not identify this functional with a six-vertex limit
height, or prove existence/uniqueness of its global critical point.

The formulas under examination are equations (2.1)–(2.4), (2.13), and
(4.1)–(4.3) of the opened announcement. For the omitted interval, continuing
those formulas is a definition to be checked, not an asserted theorem of the
source. All new deductions will be written independently in PROOF.md.

## Analytic derivation: first findings

The substitution t = tanh(z/2) evaluates the full-line kernel mass as
`1 - 2 gamma/pi`; the sign is constant, so its L1 norm is the absolute
value of this number, strictly below one for every fixed 0 < gamma < pi.
Schur's test therefore gives invertibility on every finite interval, including
0 < gamma < pi/3 (the omitted interval). The free-fermion kernel is zero.
The priority warning was independently explained by reading the effective
nice value 20; no raised-priority computation is being attempted.

A stronger local consequence is available: the two critical equations are
linear in (x,y). After division of the theta equation by 2B, their coefficient
matrix has at B=0 exactly the envelope Wronskian. Its sign is strictly
positive, because sin(t)/(cos(t)+cos(gamma)) is strictly increasing on
(-delta,delta). Thus the formulas have a unique local analytic critical
branch at every interior envelope parameter, even in the omitted interval.
Next: write the full proof, derive its B^2 coefficient twice, and check it
against direct finite-interval quadrature and determinant ratios.

## First bounded numerical run

Wrote PROOF.md and verify_local.py. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_local.py
```

First run: all assertions passed; 5 mass checks, 3 independent
determinant/resolvent comparisons, 8 branch checks. Runtime 0.60 s,
peak RSS 37.6 MiB, effective nice 20. Quadratic-coefficient extrapolation
errors ranged from 7.91e-10 to 2.19e-6; 64-to-128-panel refinement errors
were at most 1.60e-12.

The run also emitted runtime warnings. Some came from evaluating unused
meromorphic functions exactly at their separate-term poles; these values
were discarded but should never have been evaluated. BLAS-backed matmul
and slogdet also emitted floating-status warnings despite finite checked
outputs. These warnings require resolution before treating the numerical
audit as complete. Split the function evaluators, use explicit finite sums
for matrix-vector products, and use a separate scalar LU determinant
implementation; rerun with warnings treated as errors.

## Warning-free rerun and independent audit

Split A and L evaluators so unused functions are never evaluated at poles.
Replaced the flagged BLAS matrix-vector multiplication by an explicit sum,
and the determinant audit by scalar partial-pivot elimination independent
of NumPy's linear solver. Runtime warnings now raise exceptions. Repeated
the same command: exit 0, no Python warnings, runtime 0.58 s, peak RSS
34.5 MiB, effective nice 20. All 16 checks passed with the same branch
errors. The remaining shell `nice` warning reflects the already lower
inherited priority, as checked above.

Proof audit: the two leading constants in the critical equations are 1/2
and 1/6. Re-derived them independently from the zeroth and second moments
of the even resolvent density, rather than the Neumann expansion. Also
checked the sign of the Wronskian directly as a difference of logarithmic
derivatives, not by numerical determinant signs. Endpoint parameters and
limits Delta -> +/-1 are excluded explicitly; there is no parameter-uniform
inverse bound at those endpoints.

One further audit against an exactly solvable case is appropriate: at
gamma=pi/2, u=pi/4, theta=0 the critical pair can be derived directly as
`x(B)=y(B)=1/2 - 1/(2 sqrt(2) cosh(B))`. Its quadratic coefficient is
`1/(4 sqrt(2))`, providing a check that does not use either perturbative
derivation. Add this identity to the proof and check finite B numerically.

## Final run and file audit

The exact free-fermion calculation is now in PROOF.md. The same command
passed all 19 checks, with runtime warnings treated as errors:

```text
branch gamma=0.02 u/delta=0.35 theta/T=+0.40 B2_error=7.91e-10 refinement=2.78e-15
branch gamma=0.4 u/delta=0.30 theta/T=-0.40 B2_error=3.02e-09 refinement=2.43e-15
branch gamma=0.4 u/delta=0.50 theta/T=+0.00 B2_error=1.28e-08 refinement=2.32e-15
branch gamma=0.4 u/delta=0.75 theta/T=+0.30 B2_error=8.93e-08 refinement=9.5e-15
branch gamma=1.0471976 u/delta=0.40 theta/T=+0.20 B2_error=8.11e-07 refinement=2.05e-13
branch gamma=1.5707963 u/delta=0.50 theta/T=+0.00 B2_error=1.4e-06 refinement=1.95e-13
branch gamma=2.4 u/delta=0.30 theta/T=-0.20 B2_error=2.19e-06 refinement=2.6e-13
branch gamma=3.1215927 u/delta=0.70 theta/T=+0.25 B2_error=4.93e-07 refinement=1.6e-12
mass checks: 5; determinant/resolvent checks: 3; local branch checks: 8
exact free-fermion checks: 3; max error 2.7e-10
PASS elapsed_seconds=0.60655 maximum_matrix_dimension=129 nice=20 peak_rss_MiB=33.828125
```

Full mass values, all observed quadratic displacements, finite-difference
derivative checks and resource measurements are in verification.json.
The independent scalar determinant/resolvent discrepancies are at most
3.82e-14. Direct full-line and transformed kernel integrals agree with the
exact signed mass to better than 1e-45 in five parameter cases.

A failed patch exposed stripped inline math delimiters in PROOF.md from
string escaping. Repaired these to dollar delimiters and removed one tab
inside a theta symbol. Audited the repaired text: zero control characters
other than newlines. A subsequent patch command had a JavaScript quoting
error before execution; it changed no files and was rerun correctly.

Reopened the already-inspected PDF at its final comments and references;
the comments give a strategy and named inputs, not a complete proof.
This source audit does not extend the initial bounded search. No extra
paper is cited on the strength of the reference list alone.

Created REPORT.md with the required first-line verdict, explicit limited
scope, reproducible command, failures, remaining gaps, and a next target:
prove the sign of the envelope curvature quantity C in the omitted
interval, then establish which side the local branch enters. T133 remains
unproved by this work. All task-created files are confined to this folder.
