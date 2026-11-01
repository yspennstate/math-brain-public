Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SUCCESSOR METRIC STARTED; retired D0069 remains frozen at `C5=5/5` with unchanged count `6`; Section-B moves tried: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES NOT THE SUCCESSES, #26 HUNT THE SPORADIC CASE.**

# R06 — successor-admission pass: I0128/Sendov is no longer an open CLOSABLE candidate

Date: 2026-09-17 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and frozen predecessor state

I continued from `runs/R06/20260917T1828Z_successor_gate_refresh_23.md`. I did not reopen either retired predecessor.

- **I0056 / Lyons--Peres, Probability on Trees and Networks, Question 6.20.** The exact original source question retained by this track is: “What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?” The frozen R06 regime is `H_{5,5}` with outer vertex-boundary normalization `Phi_V(G)=inf_{0<|K|<infinity}|partial_V K|/|K|`; its certified interval is `[sqrt(5),sqrt(5)]`, width `0`. The full source question remains **PARTIAL**. A fresh 2026-09-17 source/literature check again recovered Haslegrave--Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, DOI `10.1002/rsa.20946`, whose paper explicitly says its triangular and square hyperbolic-lattice results answer Lyons--Peres Question 6.20 for face degrees `3` and `4`. Those cases remain excluded prior art and are not relabelled new.
- **D0069 / Grimmett--Li nonsimple connective-constant extension.** Its frozen degree-five metric reached `C5=5/5`, then accumulated six unchanged runs and was formally rotated. The full source remains **PARTIAL**. No D0069 research is restarted here.

The operative state remains `SUCCESSOR_ADMISSION_REQUIRED`: a new claim is permitted only after exact source, current-open scope, ownership and genuinely CLOSABLE source metric all pass simultaneously.

## 2. Repository refresh and ownership state

Before the admission screen I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest R06 report, and the freshest available coordinator admission delta `operations/task_health/runs/2026-09-17T175800Z/queue_delta.md`. I also performed exact-ID claim lookups/searches rather than treating the queue table as ownership truth.

The connector truncates the very large intake JSONLs when rendered wholesale, so I used exact-ID/source retrieval for the active screen and do not claim a byte-for-byte visible reread of every intake row.

The owner-added famous finite block `I0120`--`I0129` has changed substantially since its PENDING queue proposal. Canonical claims are now visible for `I0120`, `I0121`, `I0122`, `I0123`, `I0124`, `I0125`, `I0126`, `I0127`, and `I0129`. Direct fetch of `operations/claims/I0128.md` returned `404`, so I0128 was the only row in that ten-problem block that still looked ownership-free before the current-status check.

## 3. #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — the queued Sendov degree frontier is obsolete

`QUEUE.md` describes I0128 as a CLOSABLE-shaped Sendov target, based on the older landscape “proved through small degree, proved for sufficiently large degree, close the intermediate fixed-degree gap.” That was a reasonable finite-metric shape when the row was proposed, but it is not current in September 2026.

Dated current-status queries run 2026-09-17 included:

- `Terence Tao Sendov conjecture August 2026 Mazur Lean proof`;
- `Sendov conjecture Mazur Lean formalization August 2026`;
- `Sendov.sendov_conjecture Lean`;
- `Sendov conjecture solved 2026 Tao Mazur`.

The decisive current evidence is Terence Tao's 12 August 2026 post **“A digestion of the proof of Sendov's conjecture.”** Tao states that Lech Mazur obtained a proof for **all `n>=2`**, verified in Lean, and that Tao digested/reorganized the proof; the same argument proves the stronger Phelps--Rodriguez conjecture. Tao also maintains a separate public Lean repository `teorth/sendov` whose top-level theorem states Sendov's conjecture in full generality for every degree `n>=2`, with the stronger Phelps--Rodriguez theorem alongside it.

Therefore the queued metric “largest fixed degree verified / bridge the finite degree gap” is not an open mathematical target anymore. Even if one distinguishes journal publication/refereeing from a public proof plus formal verification, it is operationally impossible to admit I0128 as an **open** outside problem under the fleet rules.

**I0128 disposition:** `EXCLUDE_FROM_DISPATCH / CURRENT_RESOLUTION_WITH_FORMALIZATION`. No claim is created.

## 4. #22 READ THE FAILURES, NOT THE SUCCESSES — chronology matters here

This candidate is a useful example of why a queue row cannot be promoted from stale “open” metadata.

An earlier ProofAtlas page dated 2 August 2026 described Mazur's Revision 14 only as an all-degree **proof candidate** and explicitly said formal verification was planned/not yet complete. That page would not by itself justify closing the problem. But it is chronologically superseded by Tao's 12 August digestion and the later public `teorth/sendov` formalization, which explicitly records the full theorem.

So the correct conclusion is not “an AI paper claimed it, therefore solved”; the correct conclusion is that the exact finite-gap premise used to nominate I0128 has been overtaken by a later expert-checked, independently reorganized argument with a separate Lean formalization. The unresolved-publication-status nuance is recorded, but it does not restore I0128 to the open queue.

## 5. #26 HUNT THE SPORADIC CASE — the only free row in I0120--I0129 disappears

The attraction of I0128 was precisely the sporadic finite interval between low-degree verification and Tao's older sufficiently-large-degree theorem. That sporadic interval is now gone.

This also means the entire famous finite replenishment block `I0120`--`I0129` currently supplies **no lawful R06 successor**: nine rows have canonical owners, while the remaining ownership-free row I0128 fails the CURRENT_OPEN_SCOPE gate. I do not steal an owned problem and I do not create a decorative replacement metric for a resolved one.

I also preserved earlier admission exclusions rather than rerunning them as research: I0105/I0106 are broad mechanism-dependent programs, I0087's queued `H^2 x R` scope is later-literature covered, I0050 is materially overlapped by later annealed configuration-model Ising work, and the freshest coordinator pass classifies I0045/I0046/I0048 as scope/known-likely and I0047/I0031 as HARD rather than CLOSABLE.

## 6. Current conclusion and next admissible direction

No candidate cleared all four gates in this pass:

`OUTSIDE_SOURCE AND CURRENT_OPEN_SCOPE AND UNOWNED AND CLOSABLE_SOURCE_METRIC`.

Accordingly R06 remains **`SUCCESSOR_ADMISSION_REQUIRED`**. No new metric is started and no claim file is created. The next admission pass should move beyond the now-exhausted famous-finite block and continue through genuinely unclaimed queue/intake rows, prioritizing an exact yes/no, finite constant, finite counterexample, or short construction whose original source and 2026 literature can both be checked. It must not reopen I0056, D0069, I0079, or any currently claimed I012x row.

## 7. Model / scheduler control status

The configuration limitation remains unchanged in the interface actually exposed to this worker: task controls provide prompt/title, schedule/timing mode and enabled state, but no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed one-hour execution field. GPT-6/maximum therefore remains a prompt request rather than an enforceable or verifiable scheduler setting.

The historical P26 `You cannot modify this task` response was an authorization-context boundary; repository deployment history records that P26 prompt changes later succeeded from another authorized context. That does not create model/reasoning selectors. The legitimate fix is an owning/admin/product surface or platform support exposing persistent `model` and `reasoning_effort` fields plus applied-run telemetry, not duplication or permission bypass.

No scheduler mutation was attempted.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  run_id: 20260917T1917Z_successor_sendov_exclusion_24
  retired_predecessor:
    target_id: D0069
    metric: C5
    before: 5/5
    after: 5/5
    unchanged_count: 6
    state: RETIRED_FROZEN
  original_native_source:
    target_id: I0056
    source: "Lyons--Peres, Probability on Trees and Networks, Question 6.20"
    frozen_regime: H_5_5
    metric: "certified interval width U-L for Phi_V"
    before: 0
    after: 0
    status: PARTIAL_RETIRED_FROM_R06_ACTIVE_RESEARCH
    exclusion_rechecked: "Haslegrave--Panagiotis DOI 10.1002/rsa.20946 covers triangular/square hyperbolic lattices"
  methods_this_run: [17, 22, 26]
  successor_screen:
    I0128:
      queued_target: "Sendov conjecture fixed-degree gap"
      ownership: "no canonical operations/claims/I0128.md at screen time"
      current_status: EXCLUDE_CURRENT_RESOLUTION_WITH_FORMALIZATION
      dated_evidence:
        - "Terence Tao, A digestion of the proof of Sendov's conjecture, 2026-08-12"
        - "teorth/sendov Lean formalization, full n>=2 theorem"
      claim_created: false
      metric_started: false
      reason: "all-degree proof/formalization overtakes the queued small-vs-large degree gap"
  successor_metric: UNMEASURED
  overall: SUCCESSOR_ADMISSION_REQUIRED
  audit_ids: []
  finite_checker: NONE_NO_NEW_FINITE_MATHEMATICAL_CLAIM
```

No Gmail/email, Drive write, public posting, purchase, permission change, shared-root edit, peer-file edit, force-push, or schedule change was performed.