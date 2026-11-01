Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so I do not claim otherwise. **D0072 closure movement: `E_NNQ=1 -> 1`; independent-audit count `0/2 -> 1/2`. P19 supplied a genuine distinct end-to-end PASS; P26 is still required. No new P20 theorem claim is made in this closure-recovery run.**

# P20 / D0072 closure-audit recovery — first independent audit PASS

UTC run date: 2026-09-17.

Active source: Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884v2 / Springer Proceedings in Mathematics & Statistics 300 (2020), Section 4.2, Question 4.5.

Canonical claim: `operations/claims/D0072.md` @ creation commit `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`.

Canonical P20 proof candidate: `proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T16-18-23Z__run-report.md` @ creation commit `92b25a56025b3e0905274c554a4104d4acbc0685`.

Previous P20 closure self-check: `proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T17-23-26Z__closure-audit-recovery.md` @ creation commit `91100f3519c91538dfa47c8126ac446487d44a98`.

Frozen metric: `E_NNQ=1`, target `1`.

Current mathematical status after this run: **SOURCE-MATCHING YES PROOF CANDIDATE / EXACT FINITE CORE PASS / ONE DISTINCT OTHER-TRACK FULL-PROOF AUDIT PASS / P26 AUDIT STILL MISSING / PRIOR-ART SEARCH BOUNDED NEGATIVE / NOVELTY UNVERIFIED / NOT YET CLOSURE-PACKAGED.**

## 1. Required repository continuity

I continued from the exact proof and audit-recovery state rather than restarting witness mathematics. Before acting I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, the D0072 canonical claim at its creation commit, the P20 proof report and preceding closure-recovery report at their creation commits, the current P19 and P26 report directories, the newest complete P21 state, and the freshest task-health state recoverable at `operations/task_health/runs/2026-09-17T175800Z/status.md`.

No authorized release or reassignment of D0072 was recovered. The frozen source metric remains `E_NNQ=1`; this run changes only the independently audited closure evidence.

The task-health screen again reports no newly certified `READY + CLOSABLE + UNASSIGNED` admissions. That is relevant only if/when D0072 reaches the 2/2 audit gate and rotates; it is not a reason to dilute the present closure obligation.

## 2. New independent P19 full-proof audit recovered and read at its creation commit

A genuinely new directed P19->P20 audit now exists:

`proofnet24/P19-closure-smr-optimal/runs/2026-09-17/2026-09-17T17-56-34Z__rotation-hold-d0072-audit.md`.

Path-scoped Git history identifies its creation commit as

`8debd604cb2090d04a64564ba6d29a8d70198bde`

(commit message: `Add P19 rotation-hold report and independent P20 D0072 audit`). I read the report from that exact creation commit rather than from filename ordering alone.

The audit verdict is:

`P19-AUDIT-P20-D0072-ENDTOEND-23 — PASS`.

Its scope is explicitly the **full canonical K3 source witness** `P20-D0072-NONNORMAL-QUOTIENT-WITNESS-01`, not the later main-agent all-`K_m` strengthening and not publication novelty.

P19 independently reconstructed all source-critical components rather than merely agreeing with P20's prose:

1. it inspected the exact Grimmett–Li Question 4.5 source scope and quotient convention;
2. it checked that `Lambda=S_3*A_5` is infinite, finitely generated and non-virtually-abelian;
3. it checked the Leemann–de la Salle 2022 dependency in the relative form needed here — Theorem 3.1 starts from arbitrary finite symmetric `S_0`, and Proposition 3.2 enlarges while retaining the supplied generating set, so the final GRR may keep every element of `S_*=(S_3\{1}) union (A_5\{1})`;
4. it independently proved `A=pi^{-1}(<(12)>)` is non-normal and acts freely;
5. it rederived the left-coset/right-generator identification `G_A ~= K_3`;
6. it verified that `Aut(G)=Lambda_L` is regular, hence every transitive `Gamma'<=Aut(G)` is the whole `Lambda_L`;
7. it independently excluded every normal `K_3` quotient by observing that such a quotient would be a normal index-three subgroup and hence a `C_3` quotient, whereas `(S_3*A_5)^ab ~= C_2`.

No source-scope, quotient-orientation, GRR-relative-preservation, automorphism-overgroup, non-normality or normal-quotient defect was found.

This is a qualifying OTHER-track end-to-end audit under the directed `P19 -> P20` duty. It is not a P20 self-check and therefore advances the closure audit count from `0/2` to `1/2`.

## 3. P19's audit finite core is independently executed

P19 did not reuse the P20 executable. It created a separate pure-Python exact checker:

`proofnet24/P19-closure-smr-optimal/artifacts/2026-09-17/2026-09-17T17-56-34Z__p20_d0072_independent_core.py`

creation commit `1ad02ccf3984a4a1dc2b5ceff7c046a21d68bd11`, read-back blob `10422d388a81f11692d04c58548f142a6401ce83`.

Its independently executed output is:

`proofnet24/P19-closure-smr-optimal/artifacts/2026-09-17/2026-09-17T17-56-34Z__p20_d0072_independent_core.out`

creation commit `c4100bf0075ea008f8d0bfca2a61e5c8dc5128c5`, read-back blob `30b14dedcbe086b0f9daecd83ad0813b9fedcc6e`.

I read that output at the exact creation commit. It verifies index three and non-normality of `H`, the `K_3` coset adjacency, `S_3^ab=C_2`, `A_5^ab=1`, and ends

`P19-AUDIT-P20-D0072-ENDTOEND-23 FINITE_CORE_PASS`.

The audit correctly does not pretend that this finite computation machine-proves the infinite free-product normal-form or the published GRR theorem; those dependencies are audited in writing.

## 4. P26 audit gate remains open

I inspected the P26 2026-09-17 report directory before claiming closure. The latest P26 report whose timestamp is not later than this run is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_17-58-40__run-report.md`.

It is an independent audit of `R20/I0100`, the exact `p=41` one-localized Paley-theta theorem, with audit ID `P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24`. It is **not** a D0072 audit. Repository searches for `D0072 P26-AUDIT` and the exact P20 D0072 witness ID returned no P26 D0072 PASS verdict in the current-time repository state.

Therefore the honest closure count is exactly:

`OTHER-track audits: 1/2`,

with P19 PASS present and the mandatory P26 full-proof/source-quantifier audit still missing.

No closure package is created in this run, because doing so before P26's verdict would violate the protocol.

## 5. Main-agent strengthening is useful corroboration but is not an audit

Repository search also recovered

`proofnet24/MAIN-nonnormal-quotients/runs/2026-09-17/2026-09-17T173200Z__report.md`

and its companion note extending the mechanism to complete quotients `K_m` for all `m>=3`. That report explicitly preserves P20's canonical ownership, preserves `E_NNQ=1`, and records **zero** independent audits created by that run. I therefore do not count it toward the 2/2 gate.

This distinction matters: mathematical strengthening or same-mechanism corroboration is not a substitute for the independent P26 audit required by the fleet protocol.

## 6. Fresh source/current/literature recheck — 2026-09-17

I reran bounded current checks using, among others:

- `arXiv 1704.05884 Grimmett Li Self-avoiding walks connective constants Question 4.5` restricted to arXiv;
- `arXiv 2010.06020 Leemann de la Salle Cayley graphs few automorphisms infinite groups` restricted to arXiv;
- exact combinations of `Question 4.5`, the source title, `non-normal subgroup`, `G_A`, `G_N`, and Grimmett/Li;
- combinations of the question with `graphical regular representation`, Leemann and de la Salle.

The primary-source search again recovered Grimmett–Li's arXiv record, and the GRR search recovered Leemann–de la Salle's arXiv:2010.06020. The exact-phrase/later-literature queries did not surface a paper explicitly claiming resolution of the exact Grimmett–Li Question 4.5 quantifiers. This is **bounded negative evidence only**. It neither proves worldwide openness at every bibliographic surface nor certifies publication novelty.

P19's independent source audit reached the same bounded-negative conclusion and explicitly declined any novelty claim.

## 7. P21 directed-audit duty

The newest complete P21 state recovered remains the I0004 six-run handoff/retirement state, with no genuinely newer P21 theorem claim requiring a P20 directed audit. I therefore do not manufacture a P20->P21 receipt.

## 8. Current closure state and ledger delta request

The source-level mathematics itself does not move in this run:

- frozen metric: `E_NNQ = 1 -> 1`;
- source answer: **YES proof candidate**;
- P20 finite core: PASS;
- independent P19 finite core: PASS;
- P19 end-to-end source audit: PASS;
- P26 end-to-end source audit: MISSING;
- independent-audit count: **`0/2 -> 1/2`**;
- source closure package: NOT YET CREATED;
- publication novelty: UNVERIFIED.

P20 does not edit shared `RESULTS.md`, `QUEUE.md` or `POSTED.md`. Requested merge input for P26/coordinator:

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
  p20_finite_core: PASS / ALL_EXACT_CHECKS_PASS
  independent_audits_before: 0/2
  independent_audits_after: 1/2
  audit_1:
    track: P19
    verdict: P19-AUDIT-P20-D0072-ENDTOEND-23 PASS
    creation_commit: 8debd604cb2090d04a64564ba6d29a8d70198bde
    scope: FULL_CANONICAL_K3_SOURCE_WITNESS
    independent_finite_core: PASS
  audit_2:
    track: P26
    status: REQUIRED_MISSING
  main_agent_strengthening: NOT_COUNTED_AS_AUDIT
  novelty: UNVERIFIED
  prior_art: BOUNDED_NEGATIVE_SEARCH_ONLY
  activity: ACTIVE_CLOSURE_AUDIT_RECOVERY
  shared_ledger_edits_by_P20: NONE
```

## 9. Next-run rule

The next invocation begins by searching for a **new P26 D0072 full-proof/source-quantifier audit** and reading any verdict at its creation commit. Do not restart the witness search and do not create a redundant P20 checker.

- If P26 finds a substantive defect, repair that exact defect in a new immutable P20 report and revise `E_NNQ` honestly if the canonical witness ceases to certify the source.
- If P26 PASSes the same canonical `K_3` source witness, then with P19's distinct PASS already secured the audit gate becomes `2/2`. In that same run, immediately build and read back the narrow self-contained D0072 closure package containing the exact source statement, full canonical witness proof, the Leemann–de la Salle dependency, P20 finite checker/output, the two independent audit identifiers and dated prior-art limitations; request P26 shared-ledger closure, retire D0072, and execute the CLOSABLE successor rotation/admission rule.
- Do not claim public posting or publication novelty.

**END OF CANONICAL D0072 CLOSURE-AUDIT RECOVERY REPORT**
