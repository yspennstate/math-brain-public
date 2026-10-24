Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-02 strict-delta admission screen — released VDH-8.3-DUALITY is shard-compatible but not CLOSABLE

## Snapshot / continuity

- Repository: private `yspennstate/math-open-problems`, existing `master`.
- Invocation-start captured master: `e56b07fd70494c80c70e53000a572439110937f6`.
- Fresh pre-write master: `cd63886a7cece76af26e5913fde73a367f4c9c94`.
- Previous own immutable report: `research7_2026-09-17/R7-02/runs/2026-09-19/2026-09-19T222500Z__report.md`, creation commit `25416f1311c7ccbe5727e251c09b827a439bb644`.
- Native identity recovered from `operations/research7_2026-09-17/REGISTRY.md`: `6aabe797a39081919acc889f29f4c556`.
- Current target remains `PENDING_ADMISSION`.
- Exact shard rule: `sum(ord(c) for c in canonical_id) % 7 == 1`.

The previous durable cursor was

`POST_P0169_SHARD1_CORPUS_EXHAUSTED_STRICT_DELTA_G0004_RELEASE_HARD_H0021_REASSIGNED_NO_CLOSABLE_SUCCESSOR`.

Accordingly this screen examines only material repository delta rather than restarting the already exhausted original P/C/D/E/F/G/H/I source corpus.

## Repository delta since the previous R7-02 report

Exact comparison from `25416f1311c7ccbe5727e251c09b827a439bb644` to `cd63886a7cece76af26e5913fde73a367f4c9c94` is 110 commits ahead, 0 behind, with a complete changed-file set (`too_large=null`). Admission-relevant shared roots in that set are:

- `POSTED.md`, changed only by the 20 September ResearchGate metadata reconciliation; the file itself states that this changes no assignment, ownership, audit count or mathematical closure status;
- four canonical claim mutations:
  - `BHS-MST-CM-UNIV`,
  - `CAMPBELL-OROURKE-2022-Q1.8`,
  - `P0151`,
  - `VDH-8.3-DUALITY`.

There is no mutation to root `QUEUE.md`, root `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md`, campaign `RANKING.md`, or any `probability_1000_intake_*/problems.jsonl` in this exact comparison. The subsequent fresh-master movement from the invocation-start snapshot through `cd638...` likewise contains no additional `operations/claims` mutation after `e56b...`.

Exact case-sensitive shard arithmetic for the four claim IDs is:

| canonical ID | character-code sum | mod 7 | R7-02 consequence |
|---|---:|---:|---|
| `CAMPBELL-OROURKE-2022-Q1.8` | 1692 | 5 | off shard |
| `VDH-8.3-DUALITY` | 1009 | 1 | on shard; substantive class gate required |
| `P0151` | 279 | 6 | off shard |
| `BHS-MST-CM-UNIV` | 1066 | 2 | off shard |

Thus `VDH-8.3-DUALITY` is the only newly material shard-1 lifecycle event.

## Exact current source / claim state for VDH-8.3-DUALITY

Canonical outside source recorded in the claim:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255.

Exact source question in the claim: in the finite-third-moment barely supercritical configuration model, after observing that the high-degree vertices should lie in the unique largest component, the source asks **“Does the discrete duality principle still hold?”** The retained source scope is deterministic-degree configuration models with `nu_n=1+epsilon_n`, `epsilon_n -> 0`, outside the critical window, under the source's nondegenerate finite-third-moment limiting degree law; determine the second-largest-component scaling / a discrete duality reduction after deleting the giant.

Current ownership is explicit:

`UNASSIGNED AFTER R14 HANDOFF`.

Current mathematical status is explicit:

`SOURCE OPEN / PARTIAL / AUDIT-PENDING PROOF CANDIDATES / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`.

The claim also preserves bounded literature checking through 19 September 2026: the 4 August source still poses the question; 2019 barely-supercritical giant-component work does not determine the source second-largest scaling; bounded-degree duality and general subcritical upper bounds do not settle the full finite-third-moment source scope. This is bounded negative evidence only. Because R7-02 rejects the source at the CLOSABLE class gate below, no admission-specific 20 September worldwide-openness claim is made.

## Why the strong inherited proof package does not make this a CLOSABLE finite-certificate target

The released claim is unusually advanced, so the class decision must use the literal remaining theorem rather than the amount of prior progress.

The frozen source metric was

`Delta_dual,n := |(1-nu_n^dual)/epsilon_n - 1|`.

HARD7-04 proved `Delta_dual,n -> 0`; R14 inherited that supported floor and it remained `0 -> 0`. R14 additionally established, at proof-candidate level, all of the following:

1. fixed-set factorization: conditional on a prescribed set being the unique largest component, the complement pairing is a fresh configuration model conditioned only against another component of that scale;
2. a giant-scale truncated-susceptibility theorem removing that unique-largest conditioning in total variation;
3. quenched fresh-pairing duality of the actual complement of the giant, conditional on its realized degree sequence;
4. an exact warning that independent extinction-thinning is not a correct full marginal total-variation proxy because its fluctuation scale is too small;
5. an adaptive-cutoff / tree-census transfer under third-moment uniform integrability;
6. the source-size proof candidate
   `|C_{2,n}|=(1+o_p(1)) [2 R_*/epsilon_n^2] log(n epsilon_n^3)`
   together with a weighted residual-degree-profile estimate.

Those are substantial source-level ingredients. They still leave an asymptotic lower-extreme / deterministic barely-subcritical core theorem and audit obligations. In particular, closure must control a sequence of configuration models whose size tends to infinity and whose supercriticality `epsilon_n` tends to zero while preserving the source moment/critical-window hypotheses. There is no source theorem reducing the remaining assertion to a fixed finite list of graphs, degree sequences, or exact certificates.

A finite exact checker can certify a chosen degree sequence, a bounded cutoff, or a finite tree-census identity, but none of those implies the source's uniform asymptotic extreme-component lower bound without an additional theorem. Conversely, a source refutation would require a parameterized family satisfying all asymptotic hypotheses, not one isolated finite configuration-model instance. Therefore the target is theorem-sized even though the surviving obstruction is sharply localized.

This is exactly the distinction R7-02's admission rule requires: **advanced / nearly closed is not the same classification as CLOSABLE finite-certificate**.

## Non-inheritance and noncircularity

R7-02 does not inherit R14's floor metric `Delta_dual,n=0`. The slot has not admitted this target, so its successor metric remains `UNKNOWN/UNMEASURED`.

Nor are R14's proof candidates silently promoted to established lemmas for R7-02. They are useful evidence for classifying the remaining obligation, but the canonical claim itself labels the combined package audit-pending and source-open. Treating those candidate theorems as already certified closure would be circular.

## Other shard-1 finite-looking sentinels remain unavailable

Two tempting shard-1 rows are unchanged and therefore are not re-screened as fresh inventory:

- `D0007` is CLOSABLE-shaped but has an explicit canonical exclusive owner (`6aa7b3ccce548191a639ec23c50a6e73`); release has not occurred.
- `I0126` is the Kelly--Ulam Graph Reconstruction Conjecture, has canonical P03 ownership/history, and is classified HARD OUTSIDE with certified all-graphs baseline order 13.

The previous R7-02 report already rejected released `G0004` as HARD and recorded active `H0021` under R17. No current claim mutation changes those dispositions.

## Gate verdict

`VDH-8.3-DUALITY` passes:

- exact shard residue 1;
- explicit current ownership release;
- a precisely recovered outside source and source statement;
- a bounded current-open-looking repository record.

It fails the mandatory class gate:

- literal full source scope is an infinite asymptotic configuration-model duality / second-largest-component theorem;
- no proved finite reduction or finite cutoff is available;
- a finite certificate cannot close the remaining source quantifiers.

Disposition:

`RESIDUE_1 / UNASSIGNED / SOURCE_OPEN-PARTIAL / HARD_OUTSIDE / NOT_ADMITTED_BY_R7-02`.

No `operations/claims/VDH-8.3-DUALITY.md` write is made, because that file is a released canonical history owned by no current worker and R7-02 is not lawfully taking it under the CLOSABLE-only selection rule.

## Method / metric accounting

No candidate crossed admission. Therefore candidate screening is not charged as a target-specific research iteration and no Section-B method is falsely spent.

- B2: RESERVED / NOT_TRIED ON SUCCESSOR.
- B16: RESERVED / NOT_TRIED ON SUCCESSOR.
- B19: RESERVED / NOT_TRIED ON SUCCESSOR.

Successor metric before: `UNKNOWN/UNMEASURED`.

Successor metric after: `UNKNOWN/UNMEASURED`.

Movement: `NO ADMITTED TARGET`.

Target-specific stagnation count: `NOT_STARTED`.

Unknown is not converted to zero.

## Next admission cursor

Continue strict delta only. Inspect genuinely new canonical source rows, explicit releases, source-scope corrections, or status changes after the current master. Apply shard residue first, then settlement/ownership, then literal CLOSABLE source shape. Do not reopen `VDH-8.3-DUALITY` for R7-02 unless a material new theorem supplies a source-valid finite reduction/cutoff or the owner explicitly changes this slot's source-class rule.

Durable cursor:

`POST_P0169_SHARD1_CORPUS_EXHAUSTED_STRICT_DELTA_VDH_RELEASE_R1_HARD_PROOF_CANDIDATE_NO_CLOSABLE_SUCCESSOR`.
