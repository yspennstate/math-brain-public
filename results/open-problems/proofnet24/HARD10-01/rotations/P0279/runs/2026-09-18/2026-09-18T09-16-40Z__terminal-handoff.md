Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; this was not GPT-6 at maximum, and I do not claim otherwise. **TERMINAL HANDOFF / NO NEW MATHEMATICAL MOVEMENT: `C_Ising: 0 -> 0`; supported unchanged count preserved at `7`; HARD recovery count `2/2`; no Recovery 3.**

# P0279 — terminal HARD handoff

## 0. Identity and continuity

- Native slot: `6aa7eca50c1c8191b3c26254b14d65fd`.
- Target: `P0279`, HARD OUTSIDE.
- Exclusive claim: `operations/claims/P0279.md`.
- Own root: `proofnet24/HARD10-01/rotations/P0279/`.
- Input master captured before this handoff: `751e6334a9c5e296eccd2ab5e65d94845b9ee993`.
- Previous current-target report: `proofnet24/HARD10-01/rotations/P0279/runs/2026-09-18/2026-09-18T08-25-09Z__report.md`.
- Previous report creation commit: `6090afdcf91df441337c881a24f9443ff600935a`.
- Previous report readback blob: `c9a1140ca4ef7e32c42a1aa9ecf118faf3e5b96b`.
- Frozen metric: `C_Ising in {0,1}`.
- Final supported value: `0`.
- Final mathematical status: `OPEN / PARTIAL`.
- HARD recoveries consumed: `2/2`.

This file is a preservation/handoff record only. It adds no ordinary P0279 theorem, lemma, checker, certificate, or novelty claim. The supported unchanged count is therefore carried forward at `7` rather than being inflated by terminal bookkeeping.

## 1. Outside source and unresolved source target

Outside source: Justin Salez (2025), *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.8.

Exact target: establish total-variation cutoff throughout the rapidly-mixing regime for the Gibbs sampler of the zero-field ferromagnetic Ising model on bounded-degree graphs, preserving the source graph class, heat-bath/Gibbs dynamics, total-variation cutoff notion, and the full rapid-mixing/tree-uniqueness scope.

The preceding dated source/literature reconciliation re-read the source on 2026-09-18 and found Problem 2.8 still printed. Pedrotti--Salez, *The local product condition implies cutoff*, arXiv:2607.05345, supplies a general non-equilibrium local-Poincare cutoff criterion and a mixing-window refinement, but does not establish the full Ising target. The bounded search recorded in the predecessor report found no source-matching resolution. Negative search evidence is not a novelty certificate.

## 2. Preserved route inventory

The following P0279 work is preserved for any future reassignment. None is represented here as closing the source.

1. **Dynamic AT to local Poincare.** For the relevant single-site dynamics, the track proved the comparison
   `gamma(mu) >= 2 a / C_AT(mu)`, reducing a sufficient cutoff route to non-equilibrium approximate tensorization of the actual time marginals.

2. **Exact auxiliary heat-bath duality.** For any positive law `mu`, if `H_mu` is its auxiliary single-site heat-bath sampler, then
   `C_AT(mu) = 1 / gap(H_mu)`.
   Hence a uniform lower bound for the auxiliary gap gives the needed dynamic AT bound.

3. **Exact score evolution.** The local log-density score for `mu_t = pi h_t` satisfies an exact forward equation containing second discrete derivatives. This shows why naive first-order Dobrushin contraction does not close beyond the already-solved high-temperature region.

4. **Pinned-sector evolution.** Exact evolution under arbitrary pinnings has a boundary-injection term coupling neighboring pinning sectors. Equilibrium spectral-independence information does not simply propagate to all time-marginal pinnings.

5. **Two-spin exact theorem.** For the zero-field ferromagnetic single edge, every `beta >= 0`, deterministic start, and `t>0`, the auxiliary dynamic gap is at least the equilibrium heat-bath gap. This is a restricted theorem only.

6. **Short-time auxiliary-gap perturbation.** For deterministic start `x`,
   `gap(H_{mu_t^x}) = 1 - t lambda_max(M_x) + O(t^2)`
   with an explicit edge-supported matrix `M_x` satisfying a diagonal reversibility relation.

7. **Mixed starts matter.** The internal all-plus/all-minus worst-start reduction is false. On `K4`, a balanced `++--` start has strictly larger short-time auxiliary-gap deterioration than `++++`; an exact `theta=1/4` certificate lies strictly inside uniqueness and Dobrushin. This does not refute the source question or the stronger equilibrium-gap comparison.

8. **Tree root/edge coordinates.** On a tree, `R=sigma_o` and `eta_e=sigma_u sigma_v` transform the equilibrium zero-field Ising law into an exact product law, while the original Glauber dynamics becomes an overlapping state-dependent star-flip dynamics in the edge variables.

9. **Dynamic product structure fails immediately.** On `T_{2,1}` from all-plus at `theta=1/4`, the derivative of the covariance between the two edge variables at time zero is exactly `18/17 > 0`.

10. **Static/local squared influence budget.** For `F_d(z)=tanh(beta sum z_i)`, the exact derivative bound yields
    `sum_S |S| Fhat_d(S)^2 <= d theta^2`.
    On the selected strict binary-tree uniqueness strip, the directed budget satisfies `2 theta^2 < 1/2` and the internal degree-three budget satisfies `3 theta^2 < 3/4`.

11. **Recovery-2 quantifier correction.** Pedrotti--Salez Remark 2 shows that the all-time local-Poincare target is stronger than necessary: it suffices to lower-bound the appropriate constant in the actual total-variation mixing window (`gamma_epsilon`). Thus short-time pathologies can be irrelevant after burn-in.

12. **KL factorization-defect monovariant.** Conditional subtree total correlation is bounded by `D(mu_t || pi)`, which decreases in time. This is a genuine burn-in monovariant, but it is insufficient for the required `L^2` control because rare events can have arbitrarily small mutual information while retaining maximal correlation one.

13. **Projection-commutator formulation.** For conditional-expectation projections,
    `(I-P_A)P_B = P_B(I-P_A) + [P_B,P_A]`,
    hence the dynamic failure of the static tree Variance-Mixing product step is quantified by the `L^2` commutator norm between separated block projections.

14. **Latent separator-history mixture inequality.** Conditioning on a full separator trajectory restores exact descendant independence and gives the bound
    `Var(E[f|Y]) <= epsilon E Var(f|H) + Var(E[f|H])`.
    The extra term is exactly predictability of the hidden separator history from far terminal observables.

15. **Raw Harris history size is the wrong object.** In the non-Dobrushin binary-tree strip, the ordinary backward dependency exploration is supercritical even though the squared influence budget is subcritical. Any viable port must therefore exploit weighted second moments rather than unweighted history size.

## 3. Exact terminal blocker

The last selected action reduced the unresolved complete-tree port to a mixing-window `L^2` defect estimate. A representative sufficient form is a summable block-commutator bound

`sup_{t in mixing window} || [P_A^(t), P_B^(t)] ||_{2->2}`

for separated tree blocks at the scales used by a Variance-Mixing recursion, or an equivalent weighted Harris-history collision estimate in which the amplification

`(D + Coll) / D`

stays uniformly/summably controlled, where `D` is the diagonal squared-weight mass and `Coll` is the cross-term mass created by multiple causal paths sharing old update randomness.

What is missing is a theorem showing that the strict local squared contraction (`b theta^2 < 1`) survives temporal revisits, branch reconvergence, hidden separator histories, arbitrary deterministic starts, and the relevant pinning sectors in the mixing window. Existing Information Percolation, equilibrium spectral independence/entropy factorization, static Variance Mixing, and the Pedrotti--Salez criterion do not by themselves supply this transfer.

## 4. Why the target is handed off

P0279 used both allowed HARD stuck-recovery cycles. Recovery 1 selected the complete-tree uniqueness special case; that action produced the exact local `L^2` contraction but did not prove dynamic AT/local Poincare. Recovery 2 corrected the quantifiers to the mixing window and selected a port of Martinelli--Sinclair--Weitz Variance Mixing; that final action isolated the commutator/latent-history weighted-collision blocker but did not settle the source.

Therefore there is **no Recovery 3**. The same native slot must not continue ordinary P0279 research. A future return to P0279 requires an explicit later owner reassignment with a genuinely fresh route.

## 5. Scheduler/model-control truthfulness

The exposed scheduler surface still has no authenticated model-family selector, reasoning-effort selector, or per-run runtime attestation. GPT-6/maximum is request text only. This handoff therefore truthfully records GPT-5.6 Sol with reasoning level UNVERIFIED. Making the requested model/reasoning binding would require an authorized product/workspace/API/admin surface that actually exposes those controls and runtime attestation.

## 6. Successor state

No successor is declared by this handoff file. Successor admission must occur only after a fresh exact-source/current-open/ownership/exclusion check and a create-only canonical claim. A missing `operations/claims/<ID>.md` is not sufficient if historical ownership, handoff, current literature, or an exclusion applies.

```yaml
ledger_delta:
  native_id: "6aa7eca50c1c8191b3c26254b14d65fd"
  target: "P0279"
  report_kind: "TERMINAL_HARD_HANDOFF"
  metric:
    name: "C_Ising"
    before: 0
    after: 0
  supported_unchanged_count: 7
  recovery_count: "2/2"
  source_status: "OPEN / PARTIAL"
  ordinary_research_permitted: false
  recovery_3_permitted: false
  final_blocker: "mixing-window weighted L2 collision / block-projection commutator amplification"
  previous_report: "proofnet24/HARD10-01/rotations/P0279/runs/2026-09-18/2026-09-18T08-25-09Z__report.md"
  previous_report_creation_commit: "6090afdcf91df441337c881a24f9443ff600935a"
  previous_report_blob: "c9a1140ca4ef7e32c42a1aa9ecf118faf3e5b96b"
  successor_state: "ADMISSION_REQUIRED"
```
