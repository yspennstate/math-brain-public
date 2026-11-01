Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT: `E_geom = 1 -> 1`; D0057 remains REFUTED at owner-proof level but NOT CLOSED pending `0/2` independent source-level audits; unchanged count `2 -> 3`; STUCK_RECOVERY_1 / THINKING-ONLY; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #22 READ THE FAILURES, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R01 — D0057 STUCK-1: isolate the repaired finite-moment problem and port the stable-critical machinery

Run date: 2026-09-17 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`. Delivery: private GitHub only.

This is the mandatory Section-I thinking run after three consecutive fixed-metric non-movements. **No new theorem-sized mathematical claim is asserted in this report.** The source-level counterexample from the earlier R01 report remains the owner proof; the purpose here is to identify exactly what is still missing, why the existing routes cannot provide it, and what one genuinely different recovery should try next.

## 0. Continuity, exclusions, ownership, and runtime control

I did not reopen any predecessor.

- `I0024` / Aldous--Fill Open Problem 3.44 remains frozen at the exact `C=1` internal closure package with its prior independent audits.
- `I0113` remains rotated.
- `G0012` remains rotated after its six-run handoff.
- The old R01 FEI assignment remains retired; P03 owns FEI.
- The active create-only claim remains `operations/claims/D0057.md`, owned exclusively by R01.

Before this thinking run I refreshed the required repository state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the D0057 claim, the newest own report `runs/R01/20260917T1558Z_d0057_burst_window_d4a91e73.md`, and the newest neighboring R02 report `runs/R02/20260917T151431Z_9808cdd2.md`. The root `RESULTS.md` R01 row is historical/stale and explicitly says to recover newer complete reports; continuity therefore comes from the immutable R01 chain plus the exclusive D0057 claim. R02's active I0121 / Frankl package is still OPEN/PARTIAL and not a complete neighboring closure package, so no independent-audit budget was spent.

The runtime/model limitation is still unchanged. The exposed scheduler/task-management schema provides prompt/title/schedule/timing/enabled controls but no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed one-hour execution control. `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records the historical P26 edit failure `You cannot modify this task` for scheduler ID `6aa7b43682948191b697d72fec69d539`. The lawful remedy is an owning/authorized scheduler context or a platform/support ownership migration; duplicating the job or bypassing permissions is not a valid workaround. No scheduler change was attempted in this run.

## 1. Source and fixed metric

Active source: Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787 / Springer Proceedings in Mathematics and Statistics 300 (2019), Conjecture 2.

For fixed integer `m>=2`,

\[
X_{n+1}=\bigl(X_n^{(1)}+\cdots+X_n^{(m)}-1\bigr)_+,
\]

with the printed critical condition

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty.
\]

Conjecture 2 predicts

\[
\mathbf P(X_n=k\mid X_n>0)\longrightarrow \frac{m-1}{m^k},\qquad k\ge1.
\]

The fixed metric remains

`E_geom in {0,1}`,

where `E_geom=1` only after a complete source-valid proof or counterexample decides the literal deterministic-offspring conjecture under the printed condition. It moved `0 -> 1` in `runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md`. The two subsequent runs strengthened the same counterexample but did not change the metric. This run is therefore the third consecutive no-movement run and activates Section I.

The literal source statement is already refuted at owner-proof level. **The thing blocking protocol closure is external verification, not another owner lemma:** D0057 still has `0/2` required independent source-level audits.

## 2. Dated source / current-primary-literature refresh — 2026-09-17

I rechecked the original arXiv source and current primary/later-author literature rather than relying on the intake label.

- Original source: https://arxiv.org/abs/1705.04787 . Immediately after Conjectures 1--4 the authors explicitly say that additional integrability, for example `E[X_0^3 m^{X_0}]<infinity`, may be necessary. This is important: the lacunary refutation attacks the printed minimal hypothesis, not that natural repaired problem.
- X. Chen, Y. Hu, Z. Shi, *The sustainability probability for the critical Derrida--Retaux model*, arXiv:2108.05610 / PTRF 182 (2022), proves the survival scale `P(X_n>0)=n^{-2+o(1)}` under stronger hypotheses; it does not identify the conditional Yaglom law in the fixed deterministic-`m` recursion.
- X. Chen and Z. Shi, *The stable Derrida--Retaux system at criticality*, arXiv:2006.06140, studies critical regular heavy-tail regimes and develops domination/truncation and generating-function derivative estimates. It explicitly distinguishes the finite-third-weighted-moment regime from stable regimes and does not supply the missing fixed-`m` conditional geometric limit.
- Z. Li and R. Zhang, arXiv:2411.13068 / J. Stat. Phys. 2025, obtains conditional asymptotics for a generalized recursion with a geometric offspring count, not the deterministic `m` offspring of D0057.
- G. Alsmeyer, Y. Hu, B. Mallein, arXiv:2502.02991, likewise studies a geometric Galton--Watson/generalized model rather than the source model.
- X. Chen, 2026 work on infinite differentiability concerns the free energy, not the conditional law.

Dated bounded searches included: `"Derrida Retaux" "Conjecture 2" deterministic m conditional geometric`, `"Derrida Retaux" finite third moment conditional law`, `"Derrida Retaux" Yaglom fixed m`, and `"Derrida Retaux" stable critical third moment`. They did not surface a source-matching resolution of the finite-third-moment conditional law. **This negative search is not a novelty or openness certificate.** A publication-grade citation audit would still have to inspect the older Collet--Eckmann--Glaser--Martin line and the full citation graph.

## 3. (a) Exact statement that now blocks the mathematical route

The source conjecture itself is already refuted by the R01 lacunary law, so there is no honest reason to keep proving stronger pathologies of the same counterexample. The natural repaired question, explicitly suggested by the source authors and not touched by the lacunary construction, is:

\[
\boxed{
\begin{gathered}
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty,
\qquad \mathbf E[X_0^3m^{X_0}]<\infty \\
\Longrightarrow\quad
\mathcal L(X_n\mid X_n>0)\xrightarrow[n\to\infty]{}
\left\{\mathbf P(Y=k)=\frac{m-1}{m^k}\right\}_{k\ge1}.
\end{gathered}}
\tag{B}
\]

Statement (B) is **not** substituted for D0057 and does not change `E_geom=1`; it is the clean residual that tells us whether the source's proposed repair removes the counterexample mechanism.

## 4. (b) Routes tried and the precise reason each stops

### Route 1 — lacunary remote atoms / attack the negation

The successful owner counterexample places critical budget on extremely remote atoms `K_j`. It proves that the printed Conjecture 2 is false and even produces expanding windows where conditioned mass escapes to infinity.

**Why it stops:** the previous R01 moment calculation shows that forcing the isolated `n^{-2}`-scale survival bursts to remain macroscopic makes the weighted third moment diverge. Within this exact critical-mass parametrization, `E[X_0^3m^{X_0}]<infinity` kills the burst amplitude. The mechanism therefore cannot decide (B) without a fundamentally different construction.

### Route 2 — pulse windows / conservation / quantifier swap

The last run upgraded a bad subsequence to growing windows and showed `q_{n+1}/q_n -> m`, the largest possible one-step growth factor, throughout pulse interiors.

**Why it stops:** this is a sharper description of the same isolated-remote-atom pathology. It does not create a new mechanism compatible with finite weighted third moment. Further widening the window would be another lemma on a route that has already saturated the fixed metric.

### Route 3 — conditional generating functions / dual tilt

The initial D0057 work rewrote the target in terms of survival ratios and size/`m^k`-tilted generating functions. In particular, the geometric Yaglom limit would force `q_{n+1}/q_n -> 1`.

**Why it stops:** the critical generating-function identities control weighted moments but do not, by themselves, supply uniform conditional tightness. Passing to a subsequential conditional law requires controlling the tail after division by `q_n`; the identities alone permit rare remote mass to dominate that normalization. That is exactly what the counterexample exploits.

### Route 4 — import exact solutions from generalized/geometric-offspring models

The 2025 generalized-model papers prove much more explicit conditional behavior in models with random geometric offspring.

**Why it stops:** the offspring mechanism is changed. Their exact solvability is not a theorem for `eta=m` almost surely, and using it directly would silently alter the source domain.

## 5. (c) What a proof of the repaired statement would need that no current route contains

Any serious proof of (B) appears to need two ingredients simultaneously.

1. **Uniform conditional tightness at the survival scale:** a bound strong enough to rule out mass escaping to heights growing with `n` after normalizing by `q_n`. Ordinary weighted-moment finiteness before conditioning is not enough by itself.
2. **Identification / attraction:** once tightness gives subsequential limits, an argument showing that every such limit is the geometric quasi-stationary law. Equivalently, one needs enough regularity to turn the one-step recursion into `q_{n+1}/q_n -> 1` and then identify all fixed points compatible with the critical normalization.

The lacunary construction addresses neither requirement in the finite-third-moment regime. The most promising missing ingredient is a **domination/truncation estimate uniform enough to survive conditioning**.

## 6. (d) Simplest special case still unproved by R01

The cleanest finite-support laboratory is `m=2` with

\[
\mathbf P(X_0=2)=\frac15,
\qquad
\mathbf P(X_0=0)=\frac45.
\]

It is exactly critical because

\[
\mathbf E[X_0 2^{X_0}]=8/5
=\mathbf E[2^{X_0}],
\]

and it has every exponential/weighted polynomial moment finite. R01 has no proof that

\[
\mathbf P(X_n=k\mid X_n>0)\to2^{-k}
\]

for this two-point law. The bounded literature search above did not find a theorem stated at this exact conditional level for this fixed deterministic-offspring law. That search result is only a research locator, not a claim of literature priority.

This is a better recovery test than inventing another exotic initial law: if a proposed finite-moment method cannot settle this two-point case, it is not yet close to (B).

## 7. (e) Nearest solved problem and what its proof has that this one lacks

The closest useful machinery I found is Chen--Shi, *The stable Derrida--Retaux system at criticality* (arXiv:2006.06140), together with the later sustainability work. In structured critical heavy-tail regimes they obtain sharp control by **truncating the initial law and dominating the resulting generating functions / derivatives across scales**. In the stronger-integrability literature, related arguments control the critical process well enough to prove survival-scale estimates.

What those results have that D0057/(B) currently lacks is a tail structure or domination hypothesis that makes the truncation error quantitatively summable across the recursion. What they still do **not** supply is a uniform conditional-tail estimate strong enough to identify the Yaglom law for the arbitrary finite-third-moment fixed-`m` recursion.

This makes the technique worth porting, but only after explicitly targeting the conditional normalization rather than another unconditioned moment estimate.

## 8. Section-B methods used in this thinking run

### #6 DEFORM TO A POINT YOU CAN SOLVE

I deformed the repaired problem first to the finite-support two-point law `m=2`, `P(X_0=2)=1/5`. Outcome: it removes every heavy-tail excuse while retaining the exact source recursion; no current R01 route settles its conditional limit. This is the simplest honest test case for a new method.

### #22 READ THE FAILURES, NOT THE SUCCESSES

I reread the source's own warning about extra integrability and the stable-critical papers' division between finite-third-moment and heavy-tail regimes. Outcome: the old R01 counterexample is correctly diagnosed as a failure of the printed hypothesis, not evidence against the source's suggested finite-third-moment repair.

### #28 REPLACE FOR ALL WITH FOR TYPICAL

I asked whether one could first prove the conditional geometric law for a regular subclass of finite-third-moment initial laws rather than arbitrary laws. Outcome: the literature already gives structured tail regimes and generalized models, but the finite-support two-point case shows that “typical tail regularity” alone is not the right simplification. The more useful weakening is **finite support first**, not “typical law”.

No code/checker was built because this is a thinking-only stuck run and contains no new finite claim requiring certification.

## 9. Exactly one recovery choice

**Chosen recovery: port the technique from (e).**

On the next mathematical R01 run, do not extend the lacunary counterexample. Instead, port Chen--Shi's truncation/dominability framework to the conditional distribution, beginning with the two-point critical law above. The target of that experiment is a conditional-tail estimate of the schematic form

`sup_n P(X_n >= K | X_n>0) -> 0 as K->infinity`,

with constants derived from the source recursion rather than assumed. This line is exploratory and is not claimed here.

If that port fails, the failure must be recorded at the precise step where unconditioned domination loses the factor `q_n`; do not replace it with another remote-atom construction.

## 10. Next three Section-B moves

The next triple is deliberately different from this run and from the preceding `#7/#12/#27` triple:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** settle the finite-support/two-point conditional-tightness subproblem before attempting identification.
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the truncation recursion as a spine/size-biased operator acting on the conditional law, keeping the exact deterministic `m` model.
- **#20 FIND WHY THE ALGORITHM FAILS:** if iterative truncation cannot close after conditioning, isolate the exact multiplicative loss in `q_n` and make that obstruction the next theorem-sized target rather than adding auxiliary estimates.

## 11. Closure / audit status

The literal D0057 source verdict remains **REFUTED at owner-proof level / NOT CLOSED**. Repository search this run found no independent D0057 source-level PASS audit; audit count remains `0/2`. A self-check by R01 would not count. The newest neighboring R02 package is still OPEN/PARTIAL, so no reciprocal audit was appropriate.

The owner proof remains in `runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md`; later R01 reports are strengthenings and diagnostics, not substitutes for the required independent audits.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R01
  source: "Chen--Derrida--Hu--Lifshits--Shi, arXiv:1705.04787 / SPMST 300 (2019), Conjecture 2"
  canonical_id: D0057
  source_scope: "deterministic m-offspring Derrida--Retaux recursion under the printed critical condition"
  metric: "E_geom in {0,1}"
  metric_before: 1
  metric_after: 1
  movement: NO_MOVEMENT
  unchanged_count_before: 2
  unchanged_count_after: 3
  status: "REFUTED_OWNER_PROOF / NOT_CLOSED / STUCK_RECOVERY_1"
  run_kind: "THINKING_ONLY_NO_NEW_CLAIMS"
  tried_moves: [6, 22, 28]
  selected_recovery: "PORT_NEAREST_SOLVED_TECHNIQUE"
  next_moves: [4, 18, 20]
  exact_blocker: "conditional tightness + identification for the finite-third-weighted-moment repaired problem; protocol closure also awaits 0/2 independent audits"
  simplest_unproved_special_case: "m=2, P(X0=2)=1/5, P(X0=0)=4/5"
  nearest_solved_technique: "Chen--Shi stable-critical truncation/dominability and later sustainability estimates"
  remaining_source_obligation: "two independent source-level audits of the owner counterexample; no additional owner lemma needed to decide the printed Conjecture 2"
  evidence:
    - "runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md"
    - "runs/R01/20260917T1502Z_d0057_four_conjectures_c8a4f271.md"
    - "runs/R01/20260917T1558Z_d0057_burst_window_d4a91e73.md"
    - "operations/claims/D0057.md"
  audit_ids: []
```

No shared root, peer-track file, email, Drive item, public post, purchase, permission, or scheduler state was changed.