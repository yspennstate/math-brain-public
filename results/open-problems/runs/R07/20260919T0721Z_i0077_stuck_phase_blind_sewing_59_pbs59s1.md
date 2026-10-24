Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: 59 -> 59; unchanged count 3 -> 4; mandatory STUCK/THINKING recovery #1; Section-B moves actually used: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, PTRF 160 (2014), 95–126; arXiv:1302.6958v4, Problem 7.8 / intake I0077: generalize Theorem 4.3 from parabolic regions to other space-time shapes.

Status: **PARTIAL / STUCK-RECOVERY-1**. This is the mandatory thinking run after three consecutive unchanged fixed-metric reports. Per the owner protocol I make **no new theorem-sized claim and no new metric claim** in this report. The purpose of the run is to isolate the exact remaining obstruction, record every route already tried against that obstruction and why it fails, and choose exactly one recovery action.

# R07 CLOSABLE OUTSIDE — phase-blind sewing obstruction for periodic square-root tubes

## 1. Continuity / admission / ownership / source readback

Before thinking about the obstruction I re-read the current repository state on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- canonical reservation `operations/claims/I0077.md`;
- newest own report `runs/R07/20260919T0624Z_i0077_periodic_perkins_second_moment_59_psm59n3.md`;
- the current R15 history around the distinct Burdzy–Scheutzow Problem 7.2 predecessor and its later successor handoffs;
- repository-wide searches for `I0077`, `1302.6958`, and the source title.

The canonical claim still says `Owner: R07` and `Status: PENDING_ADMISSION, not READY`. No duplicate I0077 owner appeared. R15's distinct Problem 7.2 predecessor remains retired/handoff and is not reopened. `INDEX.md`/`RANKING.md` settle Problem 7.5, not Problem 7.8; `POSTED.md` contains no Problem 7.8 closure. The old R07 KPZ route remains preserved by immutable handoff.

I re-opened the primary PDF this run. Definition 2.2 is the crucial point for the present obstruction: if a decomposable FBM is represented by Brownian pieces `(B^k,T_k)`, then the **stopped pairs**

\[
\left(T_k,\{B^k_t:0\le t\le T_k\}\right),\qquad k\in\mathbb Z,
\]

must be independent across `k`, not merely the underlying infinite Brownian drivers. Theorem 4.3 has the source's three clauses at the threshold `lambda_0(c1,c2)=1`, and Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Levy sentence is separate Problem 7.9.

The source's subcritical construction (Theorem 4.3(ii)–(iii)) uses Perkins slow points plus Brownian time reversal, support, **continuous Brownian scaling**, and deterministic `k`-dependent stopping rules. In the constant parabolic case the shape has no logarithmic phase, so the stopping rule for piece `k` never needs information carried by later pieces.

## 2. Fresh bounded literature check, dated 2026-09-19

I searched the current web for the exact source/problem and for the obstruction using combinations of:

- `"Forward Brownian Motion" "Problem 7.8"`;
- `"Forward Brownian Motion" Burdzy Scheutzow later paper citations Problem 7.8`;
- `"Brownian slow points" periodic moving boundary`;
- `"slow points" "moving boundary" Brownian`;
- `"On the slow points of fractional Brownian motion" 2026`;
- periodic/killed Ornstein–Uhlenbeck and moving-domain Floquet terminology.

The primary paper remains the 2014 PTRF article / arXiv:1302.6958v4. Relevant established background still includes Perkins (1983), *On the Hausdorff dimension of the Brownian slow points*, and Bass–Burdzy (1996), *A critical case for Brownian slow points*. A current nearby development is Khoshnevisan–Lee, *On the slow points of fractional Brownian motion*, arXiv:2603.07483 (submitted March 2026), which develops localization methods for slow points but does not supply a decomposable-FBM sewing theorem for periodic moving boundaries.

The bounded search did **not** surface an accessible later primary source explicitly resolving Burdzy–Scheutzow Problem 7.8, nor a theorem that removes the independent-stopped-piece obstruction below. This is bounded negative evidence only. Worldwide openness and publication novelty remain **UNVERIFIED**.

## 3. What the preceding three unchanged runs actually achieved

The metric has been frozen at 59 since the remote-scale Haar family. The last three runs deliberately stopped adding exotic families and moved back toward a source-level analogue for the already-counted log-periodic square-root-tube family.

1. `...floquet_supercritical_refinement_59_fs59n1.md` established a strict-supercritical Floquet obstruction for periodic moving intervals, strengthening the old duty-cycle theorem without claiming a new family.
2. `...critical_periodic_floquet_boundary_59_cf59n2.md` extended the universal escape half through the critical Floquet value `Lambda=1` by inward erosion and strict moving-domain monotonicity.
3. `...periodic_perkins_second_moment_59_psm59n3.md` supplied the missing **subcritical periodic slow-point existence input**: a sharp two-terminal second-moment estimate with `r^{-Lambda}` rather than the naive `r^{-2 Lambda}`, and then a probability-one all-phase slow-terminal statement.

Thus the analytic slow-point threshold is no longer the current blocker. The remaining obligation is to turn the subcritical slow terminals into a **decomposable** FBM while keeping the stopped Brownian pieces independent.

## 4. (a) Exact blocking statement

Fix a nonconstant `P`-periodic Lipschitz interval field

\[
I_r=[a(r),b(r)],\qquad a(r)<0<b(r),\qquad \Lambda(a,b)<1,
\]

where `Lambda(a,b)` is the periodic killed-OU Floquet exponent. The missing source-facing clause is a construction of independent stopped Brownian pieces

\[
W_k:=\left(T_k,\{B^k_t:0\le t\le T_k\}\right),\qquad k<0,
\]

with each `T_k` a stopping time of the filtration of `B^k` **alone**, such that if

\[
S_0=0,\qquad S_k=-\sum_{j=k}^{-1}T_j,
\]

and the pieces are concatenated as in Definition 2.2, then

\[
\boxed{
\sqrt{-t}\,a(\log(-t))\le X_t\le
\sqrt{-t}\,b(\log(-t))
\quad\text{for every }t\le0
}
\tag{BLOCK}
\]

almost surely (or, for the asymptotic clause, with the corresponding eventual/asymptotic inequalities).

The obstruction is that the natural phase at the seam before piece `k` is

\[
\Theta_k:=\log(-S_{k+1})\pmod P,
\]

which is measurable with respect to **later/future stopped pieces**. If one uses the all-phase theorem by setting

\[
T_k=\tau_{\Theta_k}(B^k),
\]

then `B^k` is independent of `Theta_k`, but the **law of the stopped pair** `W_k` generally depends on `Theta_k`. Consequently `W_k` is then coupled to the sigma-field generated by later stopped pieces, violating Definition 2.2. The all-phase existence theorem solves `for every phase there is a slow terminal`; decomposability needs a phase-blind sewing mechanism.

This is the exact statement that blocks the periodic Theorem-4.3 analogue.

## 5. (b) Routes tried against this blocker and the precise failure of each

This list concerns the present **sewing/decomposability** obstruction, not the dozens of earlier unrelated shape-family constructions.

### Route 1 — adapt each stopping rule to the actual random seam phase

Use the all-phase slow-point theorem and set `T_k=t(B^k,Theta_k)` for the actual phase inherited from later pieces.

**Failure:** although `Theta_k` is independent of the raw Brownian driver `B^k`, the conditional law

\[
\mathcal L(W_k\mid\Theta_k=\theta)
\]

varies with `theta` for a nonconstant periodic boundary. Since `Theta_k` is a function of later stopped pieces, the stopped pair `W_k` is not independent of those later pieces. This violates the explicit independence requirement in Definition 2.2.

### Route 2 — prove slow terminals simultaneously for every phase

The preceding run did exactly this, by inward erosion plus a finite phase net. On one Brownian probability-one event, every phase has infinitely many slow terminals.

**Failure:** simultaneous existence does not produce a single phase-independent stopping time. Selecting *which* terminal to use still depends on the random seam phase and therefore recreates Route 1's dependence.

### Route 3 — discretize the phase circle and select by a finite phase cell

Approximate `Theta_k` by one of finitely many deterministic phases, using erosion to absorb the phase approximation error.

**Failure:** the selected cell is still a function of later pieces. Replacing a continuum-valued dependency by a finite-valued dependency does not restore independence of the stopped pair. It only makes the coupling finite-state.

### Route 4 — randomize the phase using an auxiliary independent uniform variable

Choose an independent phase `U_k` and use a stopping rule `tau_{U_k}(B^k)`.

**Failure:** if `U_k` is independent of the actual seam phase, the resulting piece satisfies the wrong moving boundary. If `U_k` is coupled to the seam phase, the stopped piece is again coupled to later pieces. A stationary phase marginal is not enough; the target constraint is pathwise at the actual absolute time.

### Route 5 — deterministic phase sequence `theta_k`

Choose the stopping rule for piece `k` using a deterministic phase, preserving independence exactly.

**Failure:** under ordinary scales the actual phases `log(-S_k) mod P` need not approach the deterministic sequence. The mismatch remains order one and cannot in general be absorbed by a fixed inward erosion.

### Route 6 — force stopping lengths onto a discrete multiplicative lattice

Try to choose each `T_k` close to `e^{mP}` so that logarithmic phase is almost deterministic.

**Failure:** the relevant absolute time is a *sum* of independent stopping lengths, not a product. Multiplicative lattice information is not stable under addition. Requiring exact deterministic lengths also destroys the slow-terminal stopping construction; requiring a narrow random interval leaves a residual random seam phase.

### Route 7 — directly transplant the source's telescoping square-root inequalities

In the constant case the source sums piecewise endpoint errors and uses square-root subadditivity/telescoping coefficients.

**Failure:** for a periodic profile the coefficient itself is `a(log u)` or `b(log u)` and changes with the total absolute lag `u`. Square-root subadditivity controls magnitude but not logarithmic phase.

### Route 8 — Markov-renewal / invariant phase law

Treat `Theta_k` as a state on the phase circle and look for an invariant law under the seam recursion.

**Failure:** an invariant phase distribution would at best give stationarity in law. Definition 2.2 asks for independence of the stopped pairs. If the stopped-pair kernel depends on the phase state, the shared phase chain creates dependence between adjacent pieces. A Markov-renewal construction could be interesting for general FBM, but does not by itself yield a decomposable FBM.

### Route 9 — Floquet/Doob transformed survivor pieces

Use the periodic principal Floquet eigenfunction to define a phase-dependent conditioned survivor and try to concatenate these pieces.

**Failure:** this reorganizes the same phase dependence rather than eliminating it. The source construction requires each piece to be an ordinary Brownian path stopped at a stopping time, and the stopped-pair law would still depend on the inherited phase unless one proves an additional phase-erasure identity that is presently absent.

## 6. The three Section-B thinking moves used in this run

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT — deform from the solved constant tube

For the symmetric test class

\[
w_\eta(r)=c+\eta q(r),\qquad
I_r^{(\eta)}=[-w_\eta(r),w_\eta(r)],
\]

`eta=0` is exactly the source's constant parabolic case and is sewable by Theorem 4.3.

The deformation shows where the genuinely new issue begins. If the constant inner envelope

\[
w_{\min}=\inf_r w_\eta(r)
\]

itself satisfies

\[
\lambda_0(-w_{\min},w_{\min})<1,
\]

then one can simply use the source's constant-tube decomposable FBM inside the whole periodic tube. That is a trivial containment argument, not a periodic theorem.

Therefore the first genuinely periodic regime is

\[
\boxed{
\Lambda(w)<1
\quad\text{but}\quad
\lambda_0(-w_{\min},w_{\min})\ge1.
}
\tag{NT}
\]

In this regime the average/Floquet environment is subcritical even though the phase-independent intersection tube is not. Deforming from `eta=0` therefore does not close the problem once (NT) is reached; it identifies the boundary where a new sewing idea is necessary.

### #12 FIND WHAT IS CONSERVED — search for a phase law that survives concatenation

The natural candidate invariant is the phase circle `R/PZ`. One can write a seam recursion schematically as

\[
\Theta_{k-1}=\log\bigl(R_k+T_k\bigr)\pmod P,
\]

where `R_k=-S_{k+1}` is determined by later pieces.

A stationary law for `Theta_k` does **not** solve the problem. The conserved quantity needed by decomposability is stronger: the conditional stopped-pair law must not reveal the phase state. In other words, one would need either

\[
\mathcal L(W_k\mid\Theta_k=\theta)=G_k
\quad\text{independent of }\theta,
\]

or a stopping rule not using `Theta_k` at all. No route so far supplies this phase-erasure property. This explains why the Markov-renewal formulation does not by itself help.

### #27 SWAP THE QUANTIFIERS — test whether one stopping time can serve every phase

The all-phase slow-point theorem has the form

\[
\forall\theta\ \exists t=t(\theta):\quad
\text{the backward Brownian segment at }t
\text{ fits phase }\theta.
\]

A completely phase-blind stopping rule would follow from the much stronger statement

\[
\exists t\ \forall\theta:\quad
\text{the same backward segment fits every phase }\theta.
\]

For a symmetric profile this forces the segment into the constant intersection tube of half-width `w_min`. Hence in the genuinely periodic regime (NT), the quantifier-swapped target is exactly the static slow-point problem at a critical/supercritical inner radius. It is therefore too strong in general. This route explains, rather than removes, the obstruction.

**Outcome of the three moves:** all three reject the idea that the all-phase slow-point theorem alone can be converted into decomposability. The next proof must be phase-blind at the level of the stopping rule **without** requiring one Brownian segment to satisfy every phase simultaneously.

## 7. (c) What a successful proof must contain that no route so far contains

A successful proof needs a **phase-blind sewing lemma** with deterministic scale separation.

Concretely, it must construct deterministic scale windows `A_n -> infinity` and deterministic stopping functionals

\[
T_{-n}=\tau_n(B^{-n})
\]

that depend only on the current Brownian driver and on `n`, never on later pieces, while ensuring that the absolute-time shift contributed by all later pieces is negligible on the primary part of the current piece.

The promising geometry is superexponential dominance. If

\[
R_n:=\sum_{j=-n+1}^{-1}T_j
\]

and the deterministic windows force

\[
R_n\le \varepsilon_n A_n,
\qquad \varepsilon_n\downarrow0,
\]

then for local lags `h` satisfying `h >> R_n`,

\[
\left|\log(R_n+h)-\log h\right|
\le \frac{R_n}{h}+O\!\left((R_n/h)^2\right),
\]

so an inward erosion can absorb the phase error while the stopping rule uses the deterministic phase schedule `a(log h),b(log h)`.

No previous route contains the second half of the required lemma: a **near-seam bridge** for `h=O(R_n)` that inherits margin from the already-sewn future tail and does not require knowing the random value of `R_n` when `T_{-n}` is selected. This near-seam bridge is the genuinely missing ingredient.

A proof must therefore combine all three of the following in one phase-blind stopping event:

1. a superexponentially large slow primary block, selected using only `B^{-n}`;
2. deterministic upper/lower bounds on the cumulative later length `R_n` coming from the preassigned scale windows;
3. an endpoint/bridge condition with enough inward spatial margin to absorb every `R_n` in that deterministic bracket.

This would preserve the Definition-2.2 independence exactly and would make the actual logarithmic phase asymptotically irrelevant without asking for a universal-in-phase slow terminal.

## 8. (d) Simplest special case still unproved

The simplest source-valid case that is **not** already reducible to a constant inner tube is:

- a nonconstant positive `P`-periodic Lipschitz function `w`;
- symmetric tube

\[
\mathcal D_w=
\{(-u,x): |x|\le \sqrt u\,w(\log u),\ u>0\};
\]

- subcritical Floquet exponent `Lambda(w)<1`;
- but static inner envelope at or above the source threshold,

\[
\lambda_0(-w_{\min},w_{\min})\ge1.
\]

The still-unproved special-case statement is:

\[
\boxed{
\text{There exists a decomposable FBM }X
\text{ with }|X_{-u}|\le\sqrt u\,w(\log u)
\text{ for every }u>0\quad a.s.
}
\tag{SC}
\]

The symmetry and the fact that `0` lies strictly inside every cross-section remove the one-sided/nonconvex complications from the source proof. Condition (NT) prevents (SC) from collapsing to the trivial constant-inner-tube construction. This is the cleanest test of whether superexponential phase-blind sewing actually works.

## 9. (e) Nearest solved problem and exactly what its proof has that this one lacks

The nearest solved problem is the source's own Theorem 4.3(iii) for a **constant parabolic strip**

\[
c_1\sqrt u\le x\le c_2\sqrt u,
\qquad c_1\le0\le c_2,
\qquad \lambda_0(c_1,c_2)<1.
\]

Burdzy–Scheutzow combine Perkins's slow points with time reversal, the support theorem, Brownian scaling, and independent stopped Brownian pieces. The key ingredient that the constant problem has and the periodic problem lacks is **continuous scale invariance**: after scaling a Brownian segment, the same constants `c_1,c_2` define the same shape. Hence piece `k` can use a deterministic `k`-dependent stopping rule, independent of all later pieces, and the square-root inequalities telescope without any seam phase.

The periodic tube has only discrete logarithmic self-similarity. The additive seam time is random, so the phase `log(-S_k) mod P` is random; continuous Brownian scaling no longer erases it. The preceding run ported the Perkins slow-point input, but it did not port this phase-erasure feature. That is precisely what the new sewing lemma must replace.

## 10. Exactly one recovery choice

**Chosen recovery:** `prove the simplest unproved special case from (d)`.

The next research run, and only that route, should attack (SC) by the superexponential **dominant-block / near-seam bridge** scheme outlined in Section 7. It should not add another exotic shape family and should not revisit the already-proved Floquet or slow-point estimates unless a specific step of the bridge requires them.

A concrete proof attempt should freeze deterministic scales, for example `A_{n+1} >= A_n^4`, and require each current stopping time to lie in a deterministic window `[A_n,2A_n]`. Then the cumulative later duration has a deterministic bracket dominated by the immediately later scale. The primary region `h >> R_n` should be controlled by phase Lipschitzness plus erosion; all creativity should go into the `h=O(R_n)` bridge and endpoint slack. If that bridge cannot be made phase-blind, the report should identify the exact inequality that fails rather than return to phase-adaptive stopping.

This is recovery choice **1** for the current stuck episode. The fixed metric remains 59 and the unchanged count becomes 4. Under the CLOSABLE policy the source is not yet rotated; retirement/rotation occurs at six unchanged runs unless genuine metric movement intervenes.

## 11. Closure / audit state

No new theorem is claimed in this stuck report and therefore no new finite checker or audit request is created. The earlier periodic Floquet/slow-point claims remain self-authored and do not satisfy closure by themselves. Exact Problem 7.8 remains **PARTIAL**, not PROVED/REFUTED/KNOWN. No source-level paper package is authorized from this report.

Publication novelty remains **UNVERIFIED**. A bounded search finding no later resolution is not a certificate of novelty.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  source: Burdzy-Scheutzow_2014_Problem_7.8
  intake: I0077
  lane: CLOSABLE_OUTSIDE
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: distinct_nonparabolic_shape_families_complete_source_appropriate_theorem_frozen_equivalence
  metric_before: 59
  metric_after: 59
  movement: none
  unchanged_count_before: 3
  unchanged_count_after: 4
  stuck_protocol: mandatory_thinking_run
  stuck_recovery_number: 1
  new_theorem_claims: 0
  new_finite_claims: 0
  selected_recovery: prove_simplest_unproved_special_case
  selected_special_case: symmetric_nonconstant_log_periodic_sqrt_tube_Lambda_lt_1_static_inner_threshold_ge_1
  next_route: superexponential_dominant_blocks_plus_phase_blind_near_seam_bridge
  source_status: PENDING_ADMISSION_not_READY
  publication_novelty: UNVERIFIED
```

## 13. Model / scheduler control reality

The actual runtime model for this report is GPT-5.6 Sol; no authenticated reasoning-effort metadata is exposed, so the reasoning level is reported as `UNVERIFIED` and I do not claim GPT-6 maximum.

The exposed automation control schema still offers title/prompt, schedule or start-offset, enablement, and timing mode. It does **not** expose a binding model-family selector, reasoning-effort selector, guaranteed-duration control, or authenticated completed-run model receipt. Thus the phrase `Model: GPT-6. Reasoning: maximum` remains a prompt request rather than a verifiable routing setting here.

The repository records that a `You cannot modify this task` result (including the historical P26 incident) is authorization-context-specific. The legitimate remedy for any still-denied task is to use the owning/authorized workspace/account, an authorized ownership/admin correction, or platform support. Do not create a duplicate task and do not bypass permissions. No scheduler, permission, email, Drive, public-posting, purchase, or workflow change was attempted in this run.
