# T225 work log

Task received: 14 November 2026, approximately 21:21 Asia/Tbilisi (17:21 UTC).
Request: “push this problem forward by one checkable piece.”

## 17:22 UTC — setup and literature search begun

Read the task, listed the local directory (only PROMPT.md, codex.log and run.pid),
read the brain navigation index and the compute governor state. Governor reports
`status: ok`, `mode: owner_away_open`. No compute sweep is planned.

The task's explicit folder-only rule overrides global instructions to update the
shared mesh, checklist and memory: those commands can mutate files outside this
folder, so they will not be run. No git or subagents will be used.

Initial web searches:
- `mean field Langevin dynamics low temperature polynomial convergence two layer neural network multi index 2025 2026`
- `mean field Langevin dynamics polynomial time learning Gaussian inputs teacher network log Sobolev`

Potentially relevant hits: arXiv:2408.07254 (multi-index MFLD),
arXiv:2606.31429 (stationary geometry), and Glasgow–Wu–Bruna's COLT 2025 paper
(projected gradient dynamics). Opening primary sources before drawing conclusions.

## 17:25 UTC — literature outcome and chosen piece

Opened the arXiv pages and full HTML for Lénaïc Chizat,
arXiv:2202.01009v3; Alireza Mousavi-Hosseini, Denny Wu, Murat A. Erdogdu,
arXiv:2408.07254v2; and Zong Shang, Tomoya Wakayama, Guillaume Lecué,
Taiji Suzuki, arXiv:2606.31429v2. Also opened the primary COLT page for
Margalit Glasgow, Denny Wu, Joan Bruna (2025), and arXiv pages for
Guillaume Wang, Lénaïc Chizat, arXiv:2602.11999, and Jing An, Lihan Wang,
arXiv:2610.35528. No whole-problem solution found in this short search.
The recent local results and spherical stationary results do not settle the
global unregularized-risk runtime. Literature search ends within ten minutes.

Chosen piece: prove the exact logarithmic low-temperature asymptotic of the
proximal log-Sobolev constant at Gaussian initialization for a one-dimensional,
one-neuron sine teacher with standard Gaussian parameter prior. Completing the
square in the unbounded output weight gives an effective potential of order
`1/lambda^2`, rather than `1/lambda`. The target statement is
`lim lambda^2 log(alpha_lambda) = -max_w g(w)^2/2`, where
`g(w)=E[sin(X) sin(wX)]`. A bounded-density comparison and a Lipschitz shear
should give the lower bound; a sign bottleneck should give the matching upper
bound. This is a correction/obstruction for the uniform-LSI route, not a claimed
lower bound on the time to small prediction risk. Check explicitly whether the
bottleneck is only a parameter symmetry.

Resource limitation: each subsequent shell invocation requests
`OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints
`nice: setpriority: Operation not permitted`; it also denies `ps`, so the actual
priority cannot be verified. No numerical simulation or heavy program will be
run under an unverified priority. The intended result is analytic.

## 17:27 UTC — analytic piece saved

Wrote PROOF.md. It proves the matching logarithmic asymptotic
`lambda^2 log(alpha_lambda) -> -M^2/2` and the same limit for the Poincare
constant, for the proximal law at Gaussian initialization of a sine teacher.
The lower estimate is
`alpha_lambda >= exp(-M^2/(2 lambda^2))/(1+L/lambda)^2`.
The upper estimate uses an odd clipped-linear function of w and the exact
Gaussian-integrated w marginal. Every needed LSI comparison is derived in the
file, including the standard Gaussian LSI via its semigroup.

Found a decisive limitation during the derivation: simultaneous sign reversal
of `(a,w)` preserves every feature `a sin(wx)`. The odd bottleneck perturbation
therefore changes no predictor at all. This is recorded algebraically in
PROOF.md; the result must not be reported as a runtime lower bound.

Primary-source follow-up: arXiv:2408.07254v2, Section 4, Proposition 9,
requires a curvature/temperature condition; the discussion after Proposition 8
explicitly says its diversity condition rules out a fixed number of indices.
arXiv:2606.31429v2, Appendix E, Proposition 11, still supplies a rate involving
`exp(-C/lambda)`, rather than a polynomial low-temperature runtime theorem.
Its discussion of an exponential time guarantee is not taken here as a proved
runtime lower bound.

## 17:30 UTC — independent audit saved

Wrote AUDIT.md and LITERATURE.md. Independent checks include a Hermite-series
derivation of g, a Gaussian-MGF derivation of the marginal, a scaled variational
calculation of the barrier, two derivations of the critical-point equation,
an equality check on the Gaussian LSI normalization, and a second perturbation
check on LSI-to-Poincare normalization. All constants remain symbolic:
`(1-exp(-2))^2/8 <= M^2/2 < 1/8`.

Counterexample/interpretation checks: bounded output weights, zero teacher,
fixed quadratic penalty, finite-KL approximation of the teacher, the loss's
factor 1/2, and the feature-preserving sign symmetry. No gap was found in the
stated proximal-measure theorem. The attempted inference from a slow LSI mode
to slow risk is false for the displayed mode, as its exact predictions agree.
The proof makes no claim of novelty over all existing functional-inequality
literature and does not solve the risk-time question.

## Final verification and handoff

Additional web queries used during the initial literature check were:
- `"mean-field Langevin" "2026" "polynomial" convergence temperature`
- `"mean-field Langevin" "lower bound" "Gaussian" exponential`

Read back REPORT.md and checked the key formulas and timestamps against the
saved proof. Corrected a draft log timestamp from 17:30 to 17:27 UTC for the
initial proof save. Commands used for the final file inspection:

```sh
OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '1,180p' REPORT.md
OMP_NUM_THREADS=1 nice -n 15 rg -n '17:|VERDICT|lambda\^2|lambda\^\{2\}|M\^2|alpha|beta|not|No ' PROOF.md LOG.md
```

The inspection reported PROOF.md 359 lines, AUDIT.md 109 lines,
LITERATURE.md 49 lines, REPORT.md 64 lines (LOG.md subsequently extended).
Every command again printed `nice: setpriority: Operation not permitted`.
The report's first line has the required `VERDICT: PARTIAL` form. No numerical
experiment was run. The deliverable is the analytic theorem and its audit;
the general risk-time problem is left open rather than inferred from the LSI.
