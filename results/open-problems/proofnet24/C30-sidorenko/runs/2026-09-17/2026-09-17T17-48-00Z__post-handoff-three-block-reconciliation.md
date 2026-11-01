Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT on C30's frozen metric: complete host order remains `10`; the previous mandatory HARD handoff remains in force and its raw unchanged count is not incremented by this admission/reconciliation run. A late same-root contribution proves a new restricted equal-three-block stability theorem, but it is off-metric and does not authorize STUCK RECOVERY 3. Section-B moves used here on the handoff/admission problem: B17, B22, B30.**

# C30 post-handoff reconciliation — preserve the equal-three-block theorem without reopening the retired same-target run chain

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C30-sidorenko`.
Frozen source graph: `H=K_{5,5}\setminus C_{10}`, ten vertices and fifteen edges.
Frozen metric: largest host order `n` for which **every** finite simple host on at most `n` vertices is proved to satisfy the source normalization

\[
\operatorname{hom}(H,G)|V(G)|^{20}\ge (2|E(G)|)^{15}.
\]

Status after this run: **PARTIAL / HARD RESERVE / SUCCESSOR ADMISSION REQUIRED**. No claim of universal Sidorenko closure is made.

## 1. Continuity: the mandatory handoff remains controlling

I continued from the newest durable C30 run report

`proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T23-14-50Z__m28-m30-support-profile-and-mandatory-handoff.md`.

That report was the ordinary research run selected by STUCK RECOVERY 2/2. It proved `C30-N11-M28-M30-SUPPORT-PROFILE-03`, extending the structural order-eleven coverage through `m<=30`, but it left the frozen complete-host-order metric at 10. It explicitly records:

- complete exact verification of all `12,005,168` unlabeled ten-vertex hosts;
- `K_10` as the finite normalized minimizer at order ten, with `hom(H,K_10)=2073451770`;
- order-eleven coverage through `m<=30`, combining the retained `m<=26` whole-image bound, the exact `m=27` structural theorem, and the `m=28,29,30` support-profile dual theorem;
- first unsupported order-eleven density `m=31` for the support-profile certificate;
- recovery count `2/2 already consumed; no STUCK RECOVERY 3`;
- next state `HARD RESERVE / successor admission required`.

Therefore this run does **not** restart the same-target stagnation clock, does not create an eighth same-target research count, and does not treat an auxiliary restricted theorem as movement of the frozen complete-order metric.

I also reread the controlling campaign surfaces `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, the current C30 claim/history, recent C30/C31 commits, and the latest fleet-restoration note. `RESULTS.md` is stale on C30 (`8->9`) and explicitly tells workers to recover newer complete reports before changing supported values; it is not used to reset the proven baseline 10.

## 2. Late same-root contribution: preserve it exactly, but classify it correctly

After the mandatory handoff, a contribution appeared under

`proofnet24/C30-sidorenko/contributions/2026-09-17_three-block-stability/`.

Its claim is

`C30-EQUAL-THREE-BLOCK-STABILITY-20260917`.

Let `A=(A_{ij})_{i,j=0}^2` be a symmetric entrywise nonnegative matrix representing an equal-three-block kernel, with each row summing to 3. Put

\[
\rho=1-\min_{i,j}A_{ij}.
\]

The contribution proves the restricted quantitative inequality

\[
\boxed{
 t_H(A)\ge 1+\frac{725117}{3179904}\rho^4
       \ge 1+\frac15\rho^4,
}
\]

and equality in the Sidorenko bound `t_H(A)>=1` occurs only at the all-ones matrix. It also records

\[
\boxed{t_H(A)\ge 1+\frac1{20}\|A-1\|_{L^2}^4.}
\]

By homogeneity this yields the corresponding inequality for equal-three-block regular kernels of arbitrary degree.

This is a genuine continuum restricted theorem and is mathematically stronger than a finite sample check. It is nevertheless **PARTIAL relative to the source**: it covers uniform three-block weights and symmetric regular `3 x 3` kernels, not arbitrary unequal block measures, arbitrary irregular three-block hosts, arbitrary block number, arbitrary graphons, or all finite simple hosts.

## 3. Exact certificate already attached to the contribution

The contribution contains

- `verify.py`, which regenerates the graph polynomial and certificate from scratch using Python integers and exact `Fraction` arithmetic;
- `results.json`, whose status is `ALL_EXACT_CHECKS_PASS`.

The archived result records:

- 664 nonzero monomials in the exact homomorphism-gap polynomial;
- 39 triple-pattern classes;
- all 6 block permutations checked;
- 6 independent direct complete-coloring regressions, each over all `3^10=59049` colorings;
- the admissible polytope vertex/face geometry checked exactly;
- 12,288 Bernstein control coefficients across the four face/half certificates;
- zero negative control coefficients;
- exact global radial constant `725117/3179904`, with simplified certified lower constant `1/5`;
- `external_independent_audits = Not performed`.

The finite core is therefore internally exact-checked, but the theorem has **no independent OTHER-track audit yet** and no novelty certificate. I do not upgrade it to fleet closure.

## 4. Why the theorem does not cancel the handoff

The owner-fixed measurable quantity is complete simple-host order. The equal-three-block theorem proves an infinite but restricted host class and therefore leaves

\[
 n_{\rm complete}=10.
\]

More importantly, the hard-task stuck protocol is route-count based, not 'any new lemma resets the clock'. C30 already consumed both permitted recoveries and the mandatory handoff report explicitly forbids STUCK RECOVERY 3. A useful theorem arriving after that handoff is preserved as mathematical work, but it does not retroactively authorize another same-target research cycle.

The precise finite blocker also remains unchanged at the handoff level: all eleven-vertex hosts with `m<=30` are certified, while the support-profile dual first fails to certify the degree profile

\[
(4,5,5,6,6,6,6,6,6,6,6)
\]

at `m=31`. That failure is only a failure of the sufficient certificate, not a Sidorenko counterexample.

## 5. B17 / B22 / B30 outcomes

### B17 — look for the new quantitative gap elsewhere

The new constant `725117/3179904` is useful as a stability witness around the regular all-ones three-block kernel, but it measures a different axis from the frozen finite-order quantity. Comparing it with the earlier rank-two regular theorem makes the structural pattern clearer: C30 can now control two distinct low-complexity regular classes (operator rank at most two; equal three-block regular kernels), yet neither result constrains every eleven-vertex simple host. The numerical gap therefore belongs in the HARD RESERVE handoff as structural evidence, not as fake host-order movement.

### B22 — read the failure rather than manufacture a third recovery

The last support-profile route failed first because independent degree/codegree/triple-codegree relaxations lose joint realizability information at `m=31`. The new three-block theorem attacks a different continuum geometry and does not repair that missing finite-host joint profile. The lesson from the failure remains: a future reassignment of this source would need a genuinely new mechanism coupling support-four/five cyclic patterns or a source-wide graphon inequality, not another refinement of the same profile dual and not another checker-only density slice.

### B30 — localize the handoff instead of gluing incompatible metrics

I kept the three pieces separate:

1. **complete finite host order:** certified through `n=10`;
2. **partial order-eleven densities:** certified through `m<=30`;
3. **restricted continuum classes:** rank-two regular kernels and now equal-three-block regular kernels.

These are all valid results, but their quantifiers differ. They cannot be added together to claim `n=11`, and they cannot be used to bypass the mandatory hard-target switch.

## 6. Current-source / literature refresh — 17 September 2026

Fresh bounded searches used:

- `"K_{5,5}" "C_{10}" Sidorenko 2026`;
- `Yuqi Zhao Sidorenko K5,5 C10 arXiv 2606.15368`;
- `K5,5 minus C10 Sidorenko weakly norming Lee Schülke`.

The refresh recovered Yuqi Zhao, *Conjugacy Class Averages and Sidorenko's Conjecture* (submitted 13 June 2026), which gives the conjugacy-averaging reduction but not a proof for this fixed graph, and Zhao's *Tensor Amplification and Spectral Transfer for Sidorenko-Type Inequalities* (submitted 2 July 2026), which gives transfer machinery but again not a source-exact proof of this `H`. Lee--Schülke's paper continues to identify `K_{5,5}\setminus C_{10}` as the notorious unresolved Sidorenko example while proving it is not weakly norming. I found no later source-exact resolution in this bounded search. That is dated negative-search evidence only, not proof of worldwide openness or novelty.

## 7. Successor admission and directed C31 audit duty

The current `QUEUE.md` still states that newly certified READY entries are zero and that queue rank alone is not dispatch permission. The previous C30 handoff already screened the top apparent HARD successors and found them claimed, resolved, held, or insufficiently admitted. No newer READY+unassigned HARD successor was established in this run, so I create no replacement claim and retain

**SUCCESSOR ADMISSION REQUIRED.**

For the directed C31 duty, the newest C31 mathematical state remains the six-run rotation-hold report at commit `e58593e3977ce84ea61f7174c1a81fa2f34f90f8`, which explicitly creates no new C31 theorem-sized claim. Therefore there is no actual next C31 claim to audit in this run. I preserve, without repeating, the latest legitimate claim-scoped successor audit

`C30-AUDIT-C31-I0035-PAIR-RESISTANCE-06 = PASS`,

and separately preserve the retired-source theorem audit

`C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS`.

The latter remains scoped only to the no-universal-diameter-constant source theorem and does not certify every auxiliary claim in the larger paper. P26's direct-duality PASS remains a distinct independent source-claim audit; no receipt-only reconciliation is fabricated here.

## 8. Model/task-control status

The currently exposed task-control surface still permits title/prompt, schedule/timing mode, and enabled-state changes, but exposes no binding model-family selector, reasoning-effort selector, guaranteed execution duration, or authenticated applied-runtime telemetry. GPT-6/maximum therefore remains prompt-only, not verified scheduler configuration.

The historical P26 `You cannot modify this task` event is not a current universal limitation: repository restoration records show later authorized P26 updates succeeded and the latest restoration invocation reproduced no permission denial. The lawful workaround is to use a context that actually owns permission to modify that task; do not bypass a denial or create a duplicate schedule.

## 9. Ledger delta for P26

```yaml
ledger_delta:
  track: C30
  target: "Sidorenko H=K55 minus C10"
  frozen_metric: "largest completely certified simple-host order"
  before: 10
  after: 10
  movement: "NO MOVEMENT"
  handoff_state: "HARD RESERVE / successor admission required"
  same_target_recovery_count: "2/2 consumed; no STUCK RECOVERY 3"
  late_preserved_claim: "C30-EQUAL-THREE-BLOCK-STABILITY-20260917 = PROVED (PARTIAL, restricted equal-three-block regular kernels)"
  late_claim_external_audits: "0 independent OTHER-track audits recorded"
  n11_partial_coverage: "all hosts with m<=30"
  first_support_profile_failure: "m=31 sufficient certificate fails; not a counterexample"
  directed_c31_audit: "no newer theorem claim; preserve C30-AUDIT-C31-I0035-PAIR-RESISTANCE-06 = PASS"
  af449_audit_preserved: "C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS, source-claim scoped"
  successor: "none admitted; READY+unassigned HARD successor not established"
  methods_tried: [17, 22, 30]
```

This report preserves useful mathematics while enforcing the mandatory handoff. It does not reopen the same Sidorenko research target.