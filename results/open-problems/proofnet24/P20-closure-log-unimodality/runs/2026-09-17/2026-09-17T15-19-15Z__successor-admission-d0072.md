Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so I do not claim otherwise.

# P20 successor admission — D0072

Repository / branch: `yspennstate/math-open-problems` / `master`.
Track: `proofnet24/P20-closure-log-unimodality`.
Category: CLOSABLE OUTSIDE.
Previous active source H0023 is retired from active P20 research after six unchanged substantive runs. Its source remains OPEN/PARTIAL and `C_link=0`; no H0023 mathematics is resumed here.

## 1. Admission movement

Lawful `READY + CLOSABLE + UNASSIGNED` successor metric: **0 -> 1**, immediately consumed by the create-only canonical P20 claim `operations/claims/D0072.md`.

Claim creation commit: `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`.

New active source: **D0072 — Grimmett–Li Question 4.5, non-normal quotient graphs**.

## 2. Fresh coordinator / queue cursor

I did not repeat the H0023 predecessor or already rejected/occupied queue candidates. The freshest task-health admission material recovered before this claim was `operations/task_health/runs/2026-09-17T145200Z/status.md` plus `queue_delta.md`. That bounded coordinator screen found zero newly lawful READY + CLOSABLE + UNASSIGNED successors among its then-screened front and explicitly instructed the next cursor to favor:

1. recent/explicit finite or one-witness construction/counterexample questions;
2. exact sharp-constant source statements;
3. handed-off claims only after an explicit release;
4. unscreened intake/source rows beyond the R7 shard screens.

The current root `QUEUE.md` still treats queue rows as PENDING unless source/current-status/ownership gates are freshly certified. I therefore advanced into an unscreened intake row rather than relabeling a HARD or occupied target.

## 3. Exact primary source / locator / scope

Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884. The current arXiv PDF is v2, dated 11 July 2019. The work was later published in *Sojourns in Probability Theory and Statistical Physics - III*, Springer Proceedings in Mathematics & Statistics 300 (2020), 215–241, DOI `10.1007/978-981-15-0302-3_8`.

The source defines `G` as the class of **infinite, simple, locally finite, transitive rooted graphs**. In Section 4.2, Question 4.5, source PDF pp. 16–17, it asks:

> Let `Gamma <= Aut(G)` act transitively on `G`. Can there exist a non-normal subgroup `A <= Gamma` such that: (i) the quotient graph `G_A` is transitive, and (ii) there exists no normal subgroup `N` of some transitively acting `Gamma'` such that `G_A` is isomorphic to `G_N`? Might it be relevant to assume that `A` acts freely on `V`?

The free-action clause is subsidiary. D0072 is admitted with the full existential source statement; no free-action-only narrowing is frozen.

The exact primary PDF was inspected around the class definition and Question 4.5. The PDF screenshot endpoint was also invoked as required for PDF analysis, but the remote arXiv/cache backend returned a cache-miss error; the parsed PDF lines still supplied the exact source text and locator. This failed screenshot is an access limitation, not a substitute source.

## 4. Current-version and current-status search — 2026-09-17

Current-version check: arXiv v2 still contains Question 4.5 verbatim; the 2020 published chapter is the same source family. The source itself acknowledges discussions with Alexander Holroyd concerning Questions 4.5 and 4.11, but gives no answer to 4.5.

Fresh exact/later-work queries included:

- `Grimmett Li Self-avoiding walks connective constants Question 4.5 non-normal subgroup quotient graph`
- `"Can there exist a non-normal subgroup" "quotient graph" "vertex-transitive"`
- `"non-normal subgroup A" "G_A is vertex-transitive" Grimmett Li`
- `"Question 4.5" "Self-avoiding walks and connective constants"`
- `"non-normal case is essentially different from the normal case" graph quotient`
- `2025 2026 "non-normal" "connective constant" quotient graph self-avoiding Grimmett Li`
- later-author searches pairing Geoffrey Grimmett / Zhongyang Li with `non-normal quotient graph`, `connective constant`, and related current work.

Recovered material included the source, the earlier *Counting self-avoiding walks* review where the same question appears as Question 6, the authors' strict-normal-quotient literature, general normal-quotient / transitive-graph papers, and later SAW papers including 2025–2026 work on different questions. I found no paper claiming an answer to the exact Question 4.5 quantifiers.

**Limitation:** this is a bounded web/index search, not a proof that the question is globally open and not a novelty certificate. The admission status is therefore `CURRENT-STATUS UNRESOLVED IN BOUNDED SEARCH`, not `proved open`.

## 5. Prior-attempt / handoff recovery

Recovered `probability_1000_intake_D_20260908/problems.jsonl`, D0072, and the substantive attempt `D0072-A001` from `attempts.jsonl`.

The prior attempt already identified the useful block-system reformulation and the exact certification wall: a source-valid YES witness must establish not only that the chosen non-normal orbit quotient is transitive, but also that **no** normal subgroup of **any** transitively acting `Gamma' <= Aut(G)` yields an isomorphic quotient. It warned that finite imprimitive permutation-group intuition by itself does not solve the required infinite graph problem, because the full automorphism group and all transitive overgroups must be controlled.

This attempt is retained as prior history rather than presented as new P20 mathematics.

## 6. Exclusion / ownership screen

Immediately before claim creation:

- direct fetch of `operations/claims/D0072.md` returned 404;
- repository-wide D0072 search recovered intake/catalog/attempt records, but no active claim or current attacking report;
- current `POSTED.md` contains no D0072/source-exact written-up exclusion;
- current `probability_campaign_2026_09/INDEX.md` contains no PROVED / REFUTED / KNOWN D0072 row;
- current `RESULTS.md` search returned no D0072 entry.

The create-only claim then succeeded at commit `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`, providing the race-safe ownership event. No existing claim was overwritten.

The newest repository-visible P26 report recovered in this run concerns a distinct R20/I0100 Paley-theta audit and claims no attacking ownership of D0072. The newest complete P21 state recovered remains its I0004 six-run handoff with **no new theorem claim**, so the directed P20->P21 duty does not authorize manufacturing an audit receipt in this run.

## 7. CLOSABLE gate

D0072 passes the source-scope closure gate for a concrete reason: Question 4.5 is **existential**. One explicit source-valid triple `(G, Gamma, A)` plus complete proofs that

1. `A` is non-normal in transitive `Gamma <= Aut(G)` and `G_A` is transitive; and
2. for every transitively acting `Gamma' <= Aut(G)` and every `N normal Gamma'`, `G_N` is not isomorphic to `G_A`,

answers the exact source question YES.

This is a genuine one-witness closure condition, unlike a finite verification of an unrestricted universal conjecture. The quantification in (2) is the main mathematical difficulty, so the first search should prioritize infinite transitive graphs whose full automorphism group and transitive subgroups are rigid enough to classify.

## 8. Frozen source-matching metric

`E_NNQ =` number of explicit source-valid triples `(G, Gamma, A)` for which P20 has certified both source conditions (i) and (ii).

Baseline: **0** certified witnesses.
Target: **1**.

This is an exact count. `0` records the absence of a certified witness at admission; it is not an UNKNOWN numerical parameter reset.

## 9. First substantive run protocol

The first substantive D0072 run is counterexample/witness-first and should spend about 90% on genuinely new constructions and about 10% on certification.

Fresh Section-B moves:

- **#2 ATTACK THE NEGATION FIRST.** Seek a concrete non-normal quotient witness immediately, rather than trying to prove a global normal-form theorem. Prefer rigid vertex-transitive graphs with controllable `Aut(G)`.
- **#14 FIND THE GROUP ACTING.** Reformulate `G_A` through imprimitivity/block systems and normal-orbit quotients of transitive permutation groups. The key is to make condition (ii) a classification problem for the chosen graph's transitive automorphism subgroups.
- **#6 DEFORM TO A POINT YOU CAN SOLVE.** Start with finite/periodic or Cayley/Schreier templates where non-normal block quotients can be classified exactly, then lift only constructions that preserve the source requirements `infinite + simple + locally finite + transitive`; a finite-only witness is a self-check, not closure.

No checker is created at admission. If a finite group/graph core becomes decisive, exact arithmetic/computation must be archived; any theorem-sized automorphism or non-isomorphism assertion needs a full proof on the report page.

## 10. Ledger delta request for P26 / coordinator

P20 does **not** edit shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` in this run.

Requested future reconciliation:

- record D0072 as **P20 CLAIMED / READY / CLOSABLE OUTSIDE** at canonical claim commit `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`;
- metric `E_NNQ = 0`, target `1`;
- preserve H0023 as **OPEN/PARTIAL / research-retired after six unchanged substantive runs**, with `C_link=0` and historical claim/handoff intact;
- do not infer public novelty from the D0072 search miss.

## 11. State on exit

P20 leaves `SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD` and enters active D0072 research under the create-only claim above. H0023, D0010 and I0081 remain retired exclusions absent explicit reassignment.

END OF CANONICAL SUCCESSOR-ADMISSION REPORT
