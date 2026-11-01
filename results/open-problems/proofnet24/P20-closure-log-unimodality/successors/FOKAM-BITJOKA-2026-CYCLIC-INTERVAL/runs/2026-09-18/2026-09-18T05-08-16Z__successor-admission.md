Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this was not GPT-6 at maximum; GPT-6/maximum was requested, but the exposed runtime supplies no authenticated model-family or reasoning-effort receipt. **ADMISSION MOVEMENT: `SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD` -> `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL / ADMITTED_ACTIVE`; frozen source metric `T_CI241=0`, target `1`; no mathematical theorem claim in this admission run.**

# P20 successor admission — Fokam–Bitjoka cyclic interval conjecture

Date: **2026-09-18 UTC**.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Category: **CLOSABLE OUTSIDE**.

Canonical claim created this run:

`operations/claims/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL.md`

creation commit `d1b8c8755617cbaef9b06c2eab2694bea0382258`, exact-readback blob `d45297870f90c13c7636051773612aa71af38b2b`.

Active root:

`proofnet24/P20-closure-log-unimodality/successors/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL/`.

## 1. Continuity and required reads

P20 did **not** reopen retired LUO mathematics. The predecessor remains:

- `LUO-2005-CONJ1` — **OPEN / PARTIAL / research-retired**;
- frozen metric `T_LUO_C1=0`, target `1`;
- substantive unchanged streak `6`;
- terminal handoff `proofnet24/P20-closure-log-unimodality/successors/LUO-2005-CONJ1/runs/2026-09-18/2026-09-18T04-08-18Z__six-run-handoff-and-rotation.md` @ `ea79893c2e461a50b52089a9a2f02a0e9a436ff7`.

Before admission I reread/recovered the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/NEW_METHODS_2026-09-16.md`, the LUO terminal handoff, recent coordinator/task-health state, current claim surfaces, latest P26 reports, and the bounded P21 state.

The newest coordinator status recovered in this run is `operations/task_health/runs/2026-09-18T045200Z/status.md`. It records that the newly admitted Neunhäuserer entropy target is already owned by another native lane, preserves explicit successor-admission gaps elsewhere, and does not provide P20 a free dispatchable claim. I therefore continued beyond stale/occupied queue-front candidates rather than stealing them.

A bounded P21 repository search recovered no genuinely new P21 theorem claim requiring a P20 directed audit. No audit receipt is manufactured in this run.

## 2. Fresh outside source and exact locator

Primary source:

Fokam Souop Rigobert and Bitjoka Laurent, **“Minimal Isometric Embeddings of Graphs into Abelian Groups: Theory, Algorithms, and Applications to Signal Processing over Networks,”** arXiv:`2606.29391v1`, submitted **28 June 2026**.

Exact locator: Chapter 2 §2.8.3, **Lemma 2.39 / Conjecture 2.41**, repeated in the manuscript’s **Open Problems, item 1**.

For odd `m`, identify the cycle with `Z_m`. A cyclic interval (arc) is a consecutive subset around the cyclic order. The literal source target is:

> For every odd integer `m` and every nonempty proper subset `x subset Z_m`, there exists a cyclic interval `W subset Z_m` such that
>
> `|W triangle x| < min(|W|, m-|W|)`.

The source states that this establishes `k_min(C_m)=m-1` for every odd cycle. It reports exhaustive verification through odd `m<=17` and explicitly asks for the all-odd-`m` proof.

### Important source wording correction

The arXiv abstract contains an unconditional-sounding sentence saying that odd cycles require the naive dimension. The theorem body is more careful: the general all-odd case is **Conjecture 2.41**, and the final Open Problems section explicitly asks to prove the cyclic interval lemma for all odd `m`. P20 therefore freezes the body/open-problem statement, not the abstract shorthand.

## 3. Current-version and later-author/current-status check

Dated search: **2026-09-18**.

Primary arXiv status:

- `arXiv:2606.29391` currently shows only **v1**, submitted 28 June 2026;
- the source’s final Open Problems section still lists the cyclic interval conjecture as Open Problem 1 and says it is verified by exhaustion through `m<=17`.

Later same-author companion:

Fokam Souop Rigobert and Bitjoka Laurent, **“Dimension and Order Bounds for Isometric Embeddings of Graphs into Abelian Cayley Graphs, and the Abelian Dividend,”** arXiv:`2607.07939v1`, submitted **8 July 2026**. Its abstract says the small odd-cycle cases are proved computationally and the general case is reduced to the cyclic-interval lemma. It does not announce an all-odd proof.

Fresh bounded queries included:

- exact title of `2606.29391`;
- arXiv IDs `2606.29391` and `2607.07939`;
- `cyclic interval conjecture`;
- `Conjecture 2.41` plus both author names;
- the symmetric-difference inequality plus odd-cycle/isometric-embedding terms;
- later/citing 2026 work on the same graph-embedding problem.

A current MathDB entry also records the exact conjecture as open with no solution listed; this is secondary evidence only. No later source-matching proof or counterexample was recovered in the bounded pass.

**Limitation:** a search miss is bounded negative evidence, not a novelty certificate or proof of worldwide openness. Publication novelty remains **UNVERIFIED**.

## 4. Prior-attempt, ownership and exclusion gate

The repository gate was checked twice, including immediately before the create-only write.

Fresh evidence:

- exact repository search for `2606.29391` returned no result;
- exact repository search for `2607.07939` returned no result;
- search for `Conjecture 2.41 Fokam Bitjoka` returned no result;
- search for the exact paper title / `cyclic interval conjecture` recovered no relevant canonical claim or active mathematical attack;
- direct fetch of `operations/claims/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL.md` returned **404 immediately before creation**;
- the claim path was checked again immediately before the write and was still absent;
- root `POSTED.md`, campaign `INDEX.md` / `RANKING.md`, and current coordinator state do not list this exact target as PROVED, REFUTED, KNOWN, posted, retired, or owned.

The create-only claim then succeeded at commit `d1b8c8755617cbaef9b06c2eab2694bea0382258` and was read back at that exact commit. No competing owner was overwritten.

This source is distinct from all P20 retired exclusions: D0072, H0023, D0010, I0081 and LUO-2005-CONJ1.

## 5. Why the literal source is genuinely CLOSABLE

This is a universal **finite combinatorial** conjecture with a decisive one-witness refutation mode.

- **FALSE mode:** one explicit odd `m` and nonempty proper `x subset Z_m` for which **every** cyclic interval `W` fails the strict inequality is a complete finite source counterexample. All arcs can be checked exactly.
- **TRUE mode:** an all-odd-`m` combinatorial proof of the displayed inequality closes the source positively.

This is materially different from a merely asymptotic/HARD target. A finite counterexample certifies the exact truth value, while bounded positive verification never does.

## 6. Frozen source-matching metric

Define

`T_CI241 := number of exact truth values of Fokam–Bitjoka Conjecture 2.41 certified by P20`.

Baseline: **0**.  
Target: **1**.

This is deliberately an exact certified-count metric. Therefore `0` is a measured baseline, not an UNKNOWN value. The following do **not** move it:

- verifying additional odd values of `m` beyond the source’s `m<=17` range;
- proving the conjecture for one cardinality/parity class of `x`;
- deriving the odd-cycle embedding consequence conditional on the lemma;
- finding only numerical or sampled evidence.

## 7. First substantive run — counterexample-first

No checker is created in this admission run. The first mathematical run must spend approximately 90% on new mathematics and approximately 10% on certification, write the mechanism before code, and use at least these three fresh Section-B routes:

### #2 ATTACK THE NEGATION FIRST

Search for the smallest structural counterexample beyond the source-verified range, beginning with odd `m>=19`. The goal is not a blind scan: derive necessary conditions on a bad subset `x`, then certify an exact survivor against **all** cyclic intervals if one exists.

### #18 SAY IT IN ANOTHER LANGUAGE

Rewrite

`|W triangle x| < min(|W|,m-|W|)`

as a cyclic sliding-window discrepancy / density advantage inequality. Use complement symmetry and interval-length symmetry to reduce the domain, and identify what a bad subset must force simultaneously for every relevant window length.

### #24 FIND THE EXTREMAL OBJECT

Classify subsets minimizing the best cyclic-interval advantage. Prioritize extremal cardinality/parity and near-balanced configurations. Only after this structural classification gives a sharply reduced family may an exact checker be written.

The first run must not count the source’s existing `m<=17` verification as P20 movement.

## 8. No mathematical theorem claim in admission

This run performs source/current-status/ownership admission only. It does not prove or refute Conjecture 2.41 and creates no mathematical checker receipt. The frozen metric therefore starts at `T_CI241=0` exactly as defined.

## 9. Shared-ledger discipline

P20 made no edit to shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`. Requested reconciliation is recorded only below.

```yaml
ledger_delta:
  worker: P20
  lane: CLOSABLE_OUTSIDE
  predecessor:
    id: LUO-2005-CONJ1
    status: OPEN_PARTIAL_RESEARCH_RETIRED
    metric: T_LUO_C1
    value: 0
    target: 1
    unchanged_streak: 6
    terminal_handoff_commit: ea79893c2e461a50b52089a9a2f02a0e9a436ff7
  successor:
    id: FOKAM-BITJOKA-2026-CYCLIC-INTERVAL
    source: "Fokam Souop Rigobert and Bitjoka Laurent, arXiv:2606.29391v1, Lemma 2.39 / Conjecture 2.41 / Open Problem 1"
    status: ADMITTED_ACTIVE_CLOSABLE_OUTSIDE
    claim_commit: d1b8c8755617cbaef9b06c2eab2694bea0382258
    metric: T_CI241
    before: 0
    after: 0
    target: 1
    theorem_claim_this_run: none
    novelty: UNVERIFIED
  root_edits: none
  p21_directed_audit: none_no_new_p21_theorem_recovered
  email_drive_public_posting: none
```

## 10. Next-run continuity

Continue from this admission rather than rescreening successor inventory. Begin with the exact source and claim, then attack the negation. Any later ownership collision or explicit authorized release/reassignment must be reconciled before mathematics, but absent such a change this is now P20’s exclusive active CLOSABLE source.
