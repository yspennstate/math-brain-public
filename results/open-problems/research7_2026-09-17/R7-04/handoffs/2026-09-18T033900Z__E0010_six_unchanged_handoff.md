Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# R7-04 immutable handoff — E0010 / Durrett Problem 4

Date: 2026-09-18.

Slot: `R7-04 Constructive Model Research`.
Native ID: `6aabe7ea6e1881919a65503f8445a813`.
Source claim: `operations/claims/E0010.md`.
Admission: `research7_2026-09-17/R7-04/admissions/2026-09-17T213400Z__E0010_admission.md`, with source-scope correction `2026-09-17T213700Z__E0010_source_scope_correction.md`.

Outside source: Rick Durrett, *Coexistence in stochastic spatial models*, *Annals of Applied Probability* 19 (2009), Problem 4, arXiv:0906.2293.

Exact source target: for every fixed `beta>4.5`, prove that sufficiently fast stirring gives a unique positive/nontrivial stationary phase, with “nontrivial” read in the source convention as no mass on the absorbing all-zero configuration. The full set of invariant laws should then be the convex hull of `delta_0` and that positive phase.

## Frozen metric and retirement trigger

The source-matching quantity throughout this assignment was

\[
Q_{SR}(\beta,\varepsilon)
=
\sup_{\mu\in I^{nt}_{\beta,\varepsilon}}
\left[\bar\nu_{\beta,\varepsilon}(\eta(0))-\mu(\eta(0))\right].
\]

Its evidenced value remained

`UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

The ordinary unchanged sequence reached **six**. A mandatory thinking-only diagnosis occurred after the first three ordinary unchanged runs; three further ordinary recovery runs, including the current B3/B15/B20 run, still did not prove `Q_SR=0`. Under the owner CLOSABLE protocol, E0010 is therefore **RETIRED FROM R7-04 ACTIVE RESEARCH / HANDOFF**, not source-resolved.

Mathematical status: **PARTIAL / SOURCE OPEN** under the bounded 2026-09-18 current-status review.

This handoff is not an ownership-release edit to `operations/claims/E0010.md`; that canonical claim is left untouched. A stale claim or disabled schedule is not a release.

## Strongest cumulative results worth preserving

### 1. The source process is attractive

The intake's older statement that the sexual-reproduction process was non-attractive was corrected. In the graphical representation, deaths, two-parent births, and common stirring transpositions are all monotone maps. Thus any positive stationary law can be coupled below the upper invariant law.

### 2. Exact stationary discrepancy generator

For an ordered coupling define

\[
A_x=\eta_x,\quad D_x=\xi_x-\eta_x,\quad C_x=1-\xi_x,
\]

and let `K_A,K_D` count common-one and discrepancy neighbors in the source birth neighborhood of size `n`. With

\[
r_n(k)=\frac{k(k-1)}{n(n-1)},
\]

the exact reaction contribution is

\[
R D_x
=-D_x-\beta D_xr_n(K_A)
+\beta C_x\{r_n(K_A+K_D)-r_n(K_A)\}.
\]

Also

\[
r_n(a+d)-r_n(a)\le \frac{2d}{n}.
\]

These are exact identities/inequalities, not mean-field approximations.

### 3. Relative fast-stirring flattening has no `1/Q` loss

Writing `q_x=E D_x` and `Q=sup_x q_x`, stationarity yields

\[
0=\varepsilon^{-2}\Delta_s q(x)-q_x+\beta\Gamma_x,
\qquad -Q\le\Gamma_x\le2Q.
\]

Hence for `h=q/Q`,

\[
\|\Delta_s h\|_\infty\le2\beta\varepsilon^2.
\]

For each fixed displacement `r`,

\[
\sup_x\frac{|q_{x+r}-q_x|}{Q}\to0
\qquad(\varepsilon\downarrow0).
\]

The same relative estimate extends to every fixed finite tagged moment containing a discrepancy factor. This removed the earlier denominator blow-up from **local stirring estimates**, but did not solve Palm branch selection.

### 4. Exact fully-mixed disagreement polynomial and stable-branch margin

In the color-exchangeable finite block, with common-one fraction `a` and discrepancy fraction `d`, the normalized discrepancy reproduction polynomial is

\[
\psi(a,d)=2a-3a^2+d(1-3a)-d^2.
\]

For every `beta>4.5` there is a threshold below the stable mean-field equilibrium `rho_+(beta)` such that sufficiently high common-one density gives a strict discrepancy contraction margin uniformly in admissible `d`.

### 5. Finite-cylinder nucleation in every positive stationary law

If `mu` is stationary and `mu({0-bar})=0`, then for every finite set `Lambda`,

\[
\mu(\eta\equiv1\text{ on }\Lambda)>0.
\]

No translation invariance is needed. The proof first excludes finite-particle configurations under such a stationary law, then uses finite graphical controllability from two occupied particles.

The important limitation is quantitative: the positive cylinder probability need not be uniform over all positive stationary laws or locations.

### 6. Exact discrepancy-Palm local obstruction

For a translation-invariant persistent discrepancy coupling,

\[
\mathbb E^D[g_{\beta,n}(K_A)]\ge0,
\]

where

\[
g_{\beta,n}(k)
=-1-\beta\frac{k(k-1)}{n(n-1)}
+2\beta\left(1-\frac{k}{n}\right).
\]

The current run strengthens this by concavity to

\[
\mathbb E^D K_A
\le
k_*(\beta,n),
\]

with

\[
k_*(\beta,n)=
\frac{-(2n-3)+\sqrt{(2n-3)^2+4n(n-1)(2-1/\beta)}}2.
\]

As `n->infinity`, `k_*/n -> sqrt(3-1/beta)-1`. Thus persistent discrepancies are forced, in Palm mean, toward common-one-poor neighborhoods.

### 7. Scalar and multitype influence criteria

The preceding run proved a dependence-robust scalar criterion: if every deterministic coarse influence path has a history-uniform continuation bound whose total path mass is subcritical, stationary discrepancy vanishes.

The current run upgrades this to a finite-type theorem. If discrepancy-type intensities obey

\[
Q\le M Q
\]

for a nonnegative coarse transfer matrix `M` and

\[
\rho(M)<1,
\]

then `Q=0`. For a two-type high/low decomposition this gives the exact target

\[
\frac{a+d+\sqrt{(a-d)^2+4bc}}2<1.
\]

This theorem is complete; establishing its source hypotheses remains the issue.

### 8. Crucial no-go theorem for worst-history contraction

The current run proves that no subcritical influence criterion can hold uniformly over **all** ordered stationary graphical couplings in the source survival regime. The ordered coupling

\[
(\eta,\xi)=(\mathbf0,\bar\nu)
\]

is stationary and has `D=xi` with positive discrepancy density. Any all-history criterion with spectral radius below one would incorrectly force this discrepancy to vanish.

Therefore a uniqueness proof must use the source restriction that the lower marginal is itself a positive phase. A purely local worst-history estimate is structurally impossible.

### 9. Approximate harmonicity is not enough

The deterministic functions

\[
h_\varepsilon(x)=\frac1{1+\varepsilon^2x_1^2}
\]

have `h_epsilon(0)=1`, vanishing spatial Cesaro mean, and `||Delta h_epsilon||_infinity=O(epsilon^2)`. Thus the relative stirring estimate alone permits mesoscopic order-one islands. Reaction/regeneration information is essential.

## Exact remaining blocker

The correct missing statement is a **positive-phase Palm regeneration lemma**, not an ordinary block estimate and not an all-history estimate.

One source-closing form would be:

> For each fixed `beta>4.5`, for all sufficiently small `epsilon`, construct finitely many discrepancy-ancestry/block types and a deterministic nonnegative transfer matrix `M_{beta,epsilon}` such that every stationary ordered coupling `(eta,xi)` whose lower marginal satisfies `mu({0-bar})=0` obeys the corresponding one-slab influence inequality, and `rho(M_{beta,epsilon})<1`.

The source mature-block theorem controls ordinary future configurations from a seed. It does **not** presently control the environment chosen by conditioning on a terminal discrepancy. Ordinary bad-block probability `delta` becomes only `delta/Q` under discrepancy-Palm conditioning. Conversely, demanding a bound uniformly over arbitrary incoming histories is impossible by the `(0-bar,bar nu)` no-go theorem.

This quantifier gap is the cleanest description of the remaining obstacle.

## Nearest useful analogues

- Durrett--Neuhauser fast-stirring/PDE block construction: gives survival and mature high-density blocks, but not the required discrepancy-Palm regeneration.
- Huang--Durrett, *Motion by mean curvature in interacting particle systems* (2021): later fast-stirring bistable methodology; it does not state Problem-4 uniqueness.
- Sturm--Swart cooperative branching/coalescence: useful ancestry/duality analogy, not a resolution of this source model.
- General disagreement-percolation methods: conceptually close, but dependence must be controlled in the conditional/pathwise direction rather than by ordinary bad-block probabilities.

## Current literature status check

The primary source was rechecked on 2026-09-18. A bounded search for the exact Problem-4 wording/model and later Durrett work did not recover a source-matching uniqueness theorem. This is negative evidence only, not a novelty certificate.

## Key files

- admission: `research7_2026-09-17/R7-04/admissions/2026-09-17T213400Z__E0010_admission.md`
- source-scope correction: `research7_2026-09-17/R7-04/admissions/2026-09-17T213700Z__E0010_source_scope_correction.md`
- relative stirring hierarchy: `research7_2026-09-17/R7-04/artifacts/2026-09-17/2026-09-17T233700Z__E0010_relative_stirring_hierarchy.md`
- nucleation/ancestry recovery: `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T013800Z__E0010_nucleation_ancestry_branch_selection.md`
- local obstruction/uniform influence: `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T024000Z__E0010_neighbor_obstruction_and_uniform_influence.md`
- terminal sixth-run artifact: `research7_2026-09-17/R7-04/artifacts/2026-09-18/2026-09-18T033500Z__E0010_multitype_influence_no_go_and_regeneration_blocker.md`, creation commit `4e791a3621a4a273e40d439ce3d33652b61beb8f`
- preceding immutable report: `research7_2026-09-17/R7-04/runs/2026-09-18/2026-09-18T024300Z__report.md`, creation commit `90470865fb68d824d3f797455d4c15a77bdce659`

## Audit/package status

No source closure is claimed. P26 independent audit: `0/1`. Distinct OTHER-track audit: `0/1`. No self-contained source-closing paper package exists because the central positive-phase Palm-regeneration lemma is missing.

R7-04 must now rotate through the shard-3 admission gate while remaining enabled. It must not resume E0010 merely because the schedule recurs.
