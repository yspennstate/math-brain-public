Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so I do not claim otherwise. **D0072 closure state unchanged: `E_NNQ=1 -> 1`; independent-audit count `0/2 -> 0/2`. No new theorem claim is made in this audit-recovery run.**

# P20 / D0072 closure-audit recovery — relative-GRR dependency stress-check, audits still absent

UTC run date: 2026-09-17.

Active source: Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884v2 / Springer Proceedings in Mathematics & Statistics 300 (2020), Section 4.2, Question 4.5.

Canonical claim: `operations/claims/D0072.md` @ creation commit `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`.

Canonical proof candidate: `proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T16-18-23Z__run-report.md` @ creation commit `92b25a56025b3e0905274c554a4104d4acbc0685`, verified blob `d1cad7371762e1c1b2335f3c1d95916b36c37b69`.

Frozen metric: `E_NNQ=1`, target `1`.

Current mathematical status: **SOURCE-MATCHING YES PROOF CANDIDATE / P20 SELF-CHECKED / EXACT FINITE CORE PASS / PRIOR-ART SEARCH BOUNDED NEGATIVE / NOVELTY UNVERIFIED / 0/2 OTHER-track audits / NOT YET CLOSURE-PACKAGED.**

## 1. Required state recovery

I continued from the proof candidate rather than restarting the witness search. I reread or directly recovered the campaign control surfaces, root queue/exclusion state, `operations/FLEET_2026-09-16.md`, the D0072 claim, the proof candidate, the exact checker/output, the newest P26 report, the currently visible P19 report roots, the newest complete P21 report, and the freshest coordinator/task-health state at `operations/task_health/runs/2026-09-17T165600Z/status.md`.

No authorized release/reassignment of D0072 was recovered.

The current P19 track roots contain no 2026-09-17 D0072 audit report: `proofnet24/P19-closure-smr-optimal/runs/` currently terminates at `2026-09-16`, and `proofnet24/P19-hadwiger-nelson/runs/` currently terminates at `2026-09-16`. Repository search for exact `D0072`, the witness ID, and P19/P20 audit wording returned no independent D0072 verdict.

The newest P26 report visible in `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/` is `2026-09-17_19-59-31__run-report.md`; it audits R07/I0077/T22, not D0072. Exact D0072 audit-ID searches likewise returned no P26 verdict.

Therefore the audit count remains honestly **0/2**. Repeated P20 checking below is not counted as an OTHER-track audit.

The newest complete P21 report remains its I0004 six-run retirement/handoff with no new theorem claim. The directed P20->P21 duty therefore still does not authorize a receipt.

## 2. Source statement and current-status recheck — 2026-09-17

The current Grimmett–Li source still defines the non-normal quotient using A-orbits, with two distinct orbits adjacent when some representatives are adjacent, and then asks in Question 4.5 whether there can exist a transitive `Gamma <= Aut(G)` and a non-normal `A <= Gamma` such that:

1. `G_A` is transitive; and
2. there is no normal subgroup `N` of some transitively acting `Gamma'` with `G_A ~= G_N`.

The source immediately asks whether assuming that `A` acts freely might be relevant.

Fresh bounded searches dated 2026-09-17 used the exact question wording, `"Question 4.5"`, `non-normal subgroup`, `G_A`, `G_N`, `graphical regular representation`, the exact source title/authors, and combinations with Leemann/de la Salle. They recovered the Grimmett–Li source and the Leemann–de la Salle GRR paper, but no later paper explicitly claiming a resolution of the exact Question 4.5 quantifiers. This is bounded negative evidence only, not proof of worldwide openness and not a publication-novelty certificate.

## 3. High-value dependency stress-check: the GRR can retain the prescribed finite quotient edges

The highest-risk external step in the P20 proof candidate was not the abstract existence of a GRR but the **relative** assertion that the final GRR generating set can be forced to contain the prescribed finite set

`S_* := (S_3 \ {1}) union (A_5 \ {1})`.

I checked this directly against Leemann–de la Salle, *Cayley graphs with few automorphisms: the case of infinite groups*, Annales Henri Lebesgue 5 (2022), 73–92, DOI `10.5802/ahl.118`.

Their Theorem 1.1 states that every finitely generated non-virtually-abelian group admits a finite-degree Cayley graph whose automorphism group is no larger than the group acting by left translations. More importantly for this witness, their proof is explicitly relative to an arbitrary finite generating set:

- Theorem 3.1 starts from a finite symmetric generating set `S_0` and forms
  `S_1=(S_0 union S_0^2 union S_0^3)\{1}`; hence `S_0 subseteq S_1`.
- Proposition 3.2 starts from a finite generating set `S` and produces a finite symmetric generating set `S_tilde` with `S subseteq S_tilde`.
- In the proof of Theorem 1.1 they choose arbitrary `S_0`, form `S_1`, then take `S_2=S_tilde` from Proposition 3.2. Therefore `S_0 subseteq S_1 subseteq S_2`.

Thus choosing the witness's `S_*` as the initial finite symmetric generating set really does preserve every nonidentity `S_3` generator in the final GRR. This removes the main external-dependency ambiguity in the proof candidate; it is a P20 self-check, not an independent audit.

For `Lambda=S_3*A_5`, the theorem's hypothesis is satisfied: `Lambda` is finitely generated, infinite by free-product normal form, and not virtually abelian (it contains a non-virtually-abelian subgroup `C_2*C_3`; every subgroup of a virtually abelian group would itself be virtually abelian).

## 4. Quotient orientation/coset convention stress-check

The source quotient is by **A-orbits**. In the left-regular action of `Lambda`, the orbit of `g` is `A g`. Since `A=pi^{-1}(H)` and `ker(pi) <= A`, the map

`A g -> H pi(g)`

is a well-defined bijection from A-orbits to the three left cosets of `H=< (12)>` in `S_3`.

The Cayley graph convention in both the source and Leemann–de la Salle is right multiplication along a generator: an edge joins `g` to `g s`. Given distinct cosets `H r`, `H t`, choose `s=r^{-1}t`. Then `s != 1` and `s in S_3\{1} subseteq S`; the edge `r -- r s=t` witnesses adjacency of the corresponding A-orbits. Therefore all three quotient vertices are mutually adjacent and, with loops suppressed by the source convention, `G_A ~= K_3`.

This agrees with the archived finite checker, whose output still ends `ALL_EXACT_CHECKS_PASS` and displays the 3-by-3 adjacency matrix of `K_3`.

## 5. Universal-transitive-overgroup stress-check

For the chosen GRR, `Aut(G)=Lambda_L` and the action is regular. If `Gamma'<=Lambda_L` is transitive, then the orbit of the identity under `Gamma'` equals all vertices `Lambda`. But in the left-regular representation that orbit is exactly the set of group elements represented by `Gamma'`. Hence `Gamma'=Lambda_L`.

So the source's universal quantifier over **all** transitively acting `Gamma'<=Aut(G)` genuinely collapses to a single transitive group; no proper transitive subgroup is missed, even though `Lambda` is infinite.

If `N normal Lambda_L` gave `G_N ~= K_3`, then the quotient graph has exactly three N-orbits, hence the corresponding normal subgroup `N_0 normal Lambda` has index 3. Therefore `Lambda/N_0` has order 3 and is `C_3`. But

`Lambda^ab=(S_3*A_5)^ab ~= S_3^ab x A_5^ab ~= C_2`,

so no surjection to `C_3` exists. The finite checker independently verifies `[S_3,S_3]=A_3` and that `A_5` is perfect.

No defect was found in this universal-quantifier step.

## 6. Closure state

The proof candidate survives all material P20 stress checks performed in this run, including the key relative-GRR preservation property and the left-orbit/right-generator quotient convention. The exact finite core remains PASS.

However, campaign closure still requires two genuinely independent OTHER-track full-proof audits. At the time of this report neither required audit exists in the recoverable repository state. Therefore:

- `E_NNQ` remains **1**;
- source-level answer remains **YES proof candidate**, not yet campaign-closed;
- audit count remains **0/2**;
- no closure package is created yet;
- D0072 remains active for closure/audit recovery, not for a second witness search.

## 7. `ledger_delta` request — P20 does not edit shared ledgers

```text
ledger_delta:
  track: P20
  target: D0072
  source: Grimmett-Li 2020, Question 4.5
  metric: E_NNQ
  before_this_run: 1
  after_this_run: 1
  mathematical_status: SOURCE_MATCHING_YES_PROOF_CANDIDATE
  proof_candidate: P20-D0072-NONNORMAL-QUOTIENT-WITNESS-01
  finite_core: PASS / ALL_EXACT_CHECKS_PASS
  self_check_update:
    relative_GRR_preserves_prescribed_S0: VERIFIED_DIRECTLY_FROM_LEEMANN_DE_LA_SALLE_THEOREM_3_1_PROP_3_2_PROOF_OF_THEOREM_1_1
    quotient_coset_orientation: VERIFIED
    universal_transitive_Gamma_prime_quantifier: VERIFIED
  other_track_audits: 0/2
  audit_requests:
    - P26 full source-quantifier / proof dependency audit
    - P19 distinct full-proof audit under directed P19->P20 duty, or documented qualified independent substitute
  novelty: UNVERIFIED
  prior_art: BOUNDED_NEGATIVE_SEARCH_ONLY
  activity: ACTIVE_CLOSURE_AUDIT_RECOVERY
  shared_ledger_edits_by_P20: NONE
```

## 8. Next-run rule

At the next invocation, first check for newly created P19/P26 D0072 audits and read any verdict at its creation commit. Do not redo the witness search. If an auditor finds a substantive defect, repair it in a new immutable P20 report and revise `E_NNQ` honestly if necessary. If two distinct full-proof audits PASS, immediately create and read back the narrow self-contained closure package, request P26 ledger closure, retire D0072, and execute successor rotation/admission in the same run.

END OF CANONICAL D0072 CLOSURE-AUDIT RECOVERY REPORT
