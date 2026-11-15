# T092 work log

Started 2026-11-15 04:47 +04 (Asia/Tbilisi).
Task: “take the NEXT checkable step on this problem, building on that work.”

## Scope and startup

All writes stay in this folder. The task-specific instruction excludes
global checklist, mesh and brain writes. No git, subagents, publication or
external messages. Read both earlier REPORT.md and LOG.md files, the round
3 PROOF.md and CLAIM_AUDIT.md, and the original SOLVED_ELSEWHERE.md.
Directory listings confirm neither earlier folder has computation scripts,
and the original folder has no PROOF.md. Read the startup memory index and
compute_state.json: status warn, CPU 100%, mode owner_away_open.

The initial directory-discovery command used pwd and rg directly; subsequent
tiny shell reads use `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox prints `nice: setpriority: Operation not permitted` and executes
the reads. No substantive local computation or build will be launched
without the required priority. File writes use apply_patch.

## Bounded literature check

Web search queries:

- `Banach simple Lebesgue spectrum probability transformation 2026 solution`
- `"Banach" "ControlledBlocks" spectrum`

Opened the primary introductory TeX of OpenAI, *A smooth three-torus
diffeomorphism with simple Lebesgue spectrum*, September 23, 2026:
https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/01-introduction.tex

It still claims the exact finite-probability conclusion. No independently
verified resolution was established. Opened the arXiv page of el Houcein
el Abdalaoui, arXiv:2210.15480: latest version remains v2, June 9, 2023.
No new SOLVED_ELSEWHERE.md is warranted. End general status search here,
within five minutes; further web opens concern only the selected audit.

## Earlier result independently checked

Write a_n=<h,U^n g>. The cyclic subspace and its orthogonal complement
reduce U, so projection of h to the cyclic subspace has norm at most A
and displacement at most b. In its bilateral-shift representation,
sum |a_n|^2<=A^2 and sum |a_(n+1)-a_n|^2<=b^2. Telescoping |a_n|^2
from both infinities and Cauchy--Schwarz give sup |a_n|^2<=Ab.
The best F-supported approximation captures sum_(n in F)|a_n|^2, hence
A^2-epsilon^2<=|F|Ab. This independently re-derives the earlier claim;
it holds, including the zero-residual and incomplete-orbit cases.
For sin(2 pi u), A^2=1/2, epsilon^2=1/8 and Ab<=sqrt(2) pi delta,
so the stated constant 3/(8 sqrt(2) pi delta) also holds.

## Chosen extension, before the work

Audit one centered block estimate behind the simultaneous prediction
and square-root-density-loss claims, as the round 3 report requests.
Reconstruct its scalar probability model and prove or refute the needed
estimate independently, including the degenerate mixture and centering
error cases. This addresses the finite construction rather than repeating
the top-level theorem trace. Opened ControlledBlocks.lean and
CyclicPrediction.lean through the web tool; the latter exports repeated
block bounds but delegates the single-block calculation further down.
The exact next dependency will be recorded when inspected.

## Single-block model reached; precise result selected

Opened the manuscript's `build/main.tex`, then its `sections/04-blocks.tex`,
and the Lean files `FiniteBlocks.lean` and `ColorBlocks.lean`. Primary URLs:

- https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/04-blocks.tex
- https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/FiniteBlocks.lean
- https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/ColorBlocks.lean

The relevant model is a mixture of positive product densities with a
common phase sample and color-dependent bias b_r-q. The manuscript's
single-block argument is at lines 272–415; `block_diagonal_transfer` in
ColorBlocks is at lines 95–115. The displayed model formulas are consistent
with both claims: the estimator is unbiased under each tilted color law,
while centering cancels the first-order mixture fluctuation. No immediate
contradiction was found.

Precise extension now selected: prove the single-block analytic transfer
lemma independently, sharpening the square-root loss from 300 delta^2
to 3 delta^2 under the same scalar hypotheses, while keeping the
prediction increase at 4/delta. Include arbitrary successive frequency
lower bounds and L1 density perturbations. The physical passage producer
is outside this lemma; no geometric existence conclusion will be inferred.

Reason: the crude bound uses |b_r-q|<=3 separately for every color.
The identity sum t_r|b_r-q|^2 = sum t_r|b_r-beta|^2+|beta-q|^2
retains the unit-disk tag constraint and makes a much smaller bound
available. A second improvement is the exact Hellinger identity
1-E sqrt(R) = (1/2) E(sqrt(R)-1)^2 <= (1/2) Var(R).
All constants will be verified with rational inequalities, with no
numerical script needed.

## Single-block proof completed and constants checked

Saved PROOF.md. For s=n lambda^2, x=|beta-q|^2, and
v=sum t_r|b_r-q|^2, proved

    Var(R) <= 2 s x + 2 s^2 v^2/(1-18s),
    v^2 <= 1+11x.

The first proof expands the mixture into orthogonal terms indexed by
subsets of phases. A separate direct pair-product calculation gives the
same variance series. The exact Hellinger identity bounds the loss by
half the variance. After weighting by sqrt(p), the coefficient is at most

    1+(50/41)(3/2+11/100) = 243/82 < 3.

Second numerical derivation: coefficient<3 is equivalent to
I+47 delta<2; I<=sqrt(2)<3/2 and delta<=1/100 give <197/100.
The estimator is unbiased separately in each color and at each z.
Its exact variance is 1/s-|b_r-q|^2/n, also derived independently
from diagonal and off-diagonal terms in |sum Z_i|^2. Integrating with
mass<=2 and s>=delta/2 gives the same 4/delta prediction increase.

The proof includes simultaneous diagonalization of two finite Laurent
tests, arbitrary recursive lower bounds on phase frequencies, and an
explicit density-error tolerance fixed before those frequencies:

    e0=min{(nu/2)^2, nu/[2(W+1)]},
    W=(||A||infinity+2+1/lambda+k+1)^2.

This proves the analytic analogue of `block_diagonal_transfer` with
3 delta^2 in place of 300 delta^2, under even weaker measurable input
regularity. It neither asserts nor checks the physical realization of
the model densities. It supplies no upper bound on Laurent support and
therefore no contradiction to the earlier orbit-count constraint.

Checks so far: zero total density, zero colors, one color, n=1, complex
tags, arbitrary old estimator depending on z, both signs in Fourier
frequencies, g depending on the chosen frequencies, and the absence of
independence on the diagonal. No executable calculation was necessary.

## Final adversarial check and saved-file audit

Added a countercheck without the centering hypothesis: p=1, b=1, q=0,
n=1, lambda=sqrt(delta) gives mixture variance 2delta and square-root
loss at least delta/5. Thus the quadratic claim is not being asserted
outside its hypotheses. Checked conjugation symmetry directly for the
diagonal estimator and color densities.

Read the written proof's main variance, square-root, prediction and
diagonal-transfer calculations back with sed, and read REPORT.md with cat.
`wc -l LOG.md PROOF.md REPORT.md` returned 134, 435, 80 before this final
entry. The first report line has the required VERDICT: PROVED prefix.
An earlier provisional heading was given an incorrect future clock time;
removed that heading's timestamp rather than leave a false chronology.
No mathematical defect was found on the second derivations. The constant
comparison also follows from 2-(3/2+47/100)=3/100>0.

Deliverables: PROOF.md, LOG.md, REPORT.md, all in this folder. No script
was needed or run, and no earlier-session file was changed. The single
new piece is the strengthened analytic block lemma and its simultaneous
diagonal/L1 transfer; physical realization remains unaudited.
