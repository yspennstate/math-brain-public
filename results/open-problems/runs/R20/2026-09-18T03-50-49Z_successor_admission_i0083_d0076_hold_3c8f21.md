Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #4 PROVE SOMETHING WEAKER COMPLETELY, #11 DUALIZE, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R20 CLOSABLE OUTSIDE — successor admission: I0083 proof-candidate hold and D0076 hard-scope exclusion

Run date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and retired I0100 state

I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations/task-health implementation state, the newest R20 report, and current ownership records for candidates touched below before screening.

I did **not** reopen Afonso S. Bandeira / Randomstrasse 2025 Conjecture 26 (intake I0100) after the mandatory six-unchanged-run handoff. A fresh current-source check on 2026-09-18 still finds the public Jig/Randomstrasse problem marked **Open**, asking whether the clique-bounding Lovasz theta of the Paley 1-localization satisfies

`theta(complement G_{p,1}) ~ sqrt(p/2)`

for primes `p = 1 mod 4`.

The frozen exact-certified frontier remains

`p_max = 1213`

with retained set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

The supported I0100 retirement count remains `6`; this admission-only run does not increment it. I0101/P04 (two-localization), I0102/R12 (degree-four SoS), and the Paley-ETF track remain distinct and are not reassigned here.

## 2. Current admission gate

The newest coordinator pass at `operations/task_health/runs/2026-09-18T025600Z/` still certifies **no new READY + CLOSABLE OUTSIDE + UNASSIGNED successor**. It specifically records that the owner-requested I0120-I0129 replenishment block is occupied/resolved at the current snapshot and that H0006 is only PENDING/HARD, not a closable replacement.

I therefore advanced the cursor to two different unresolved-looking rows instead of recycling the same claimed candidates.

## 3. Method #4 — prove something weaker completely: D0076 does not become closable by freezing the known height-function subcase

Candidate: **D0076**, Geoffrey Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, Question 7.1, “Locality of the connective constant.”

The source asks for a locality principle for connective constants of quasi-transitive graphs. Existing Grimmett--Li locality theorems already prove locality under the additional hypothesis of a unimodular graph height function, and later work characterizes/extends height-function availability for large classes of Cayley graphs. A fresh 2026-09-18 search also recovered:

- Benjamin Grant--Zhongyang Li (2026), `arXiv:2601.12571`, exact functional relations for connective constants under broad local gadget transformations of cubic/quasi-transitive graphs;
- Geoffrey Grimmett (2026), `arXiv:2608.19349`, new connective-constant bounds for Grigorchuk graphs.

Neither is a source-matching theorem establishing unrestricted locality for the full Question 7.1 class. The tempting weaker theorem “prove locality for graphs with a unimodular graph height function” is already known prior art, not a successor target.

Disposition:

`D0076 = CURRENT-OPEN-LOOKING / HARD-SHAPED / NOT CLOSABLE FOR R20`.

The reason is source-level, not computational: a theorem for one further local-transformation family or one height-function class remains PARTIAL, while the universal locality statement requires a global structural mechanism. I did not create a claim.

## 4. Method #11 — dualize: I0083 has a current full proof candidate, but not a verified resolution

Candidate: **I0083**, Takahiro Hasebe and Yuki Ueda, 2018, Conjecture 3.5: if `mu` and `nu` are symmetric unimodal probability measures, is their free additive convolution `mu boxplus nu` unimodal?

The 2018 paper proves the semicircular-input special case but leaves the two-arbitrary-input closure as Conjecture 3.5.

Fresh current-status research on 2026-09-18 recovered the 7 September 2026 release **“Symmetric unimodality under free additive convolution”**, version `0.1.0-candidate`, DOI `10.5281/zenodo.22649756`. Its stated theorem matches the broad Hasebe--Ueda symmetric closure question. Its own release page, however, explicitly labels it an **unrefereed analytic proof candidate** and states that there is no external whole-proof review, independent reproduction, or formal verification. The attached symbolic checks certify selected identities only and explicitly do not certify the analytic inequalities/compactness/duality or the entire theorem.

This is materially stronger current evidence than a vague “claimed resolution” note, but it is still not enough under the fleet's source-closure/current-status rule to relabel Conjecture 3.5 as KNOWN. Conversely, it makes I0083 inappropriate to seize as an untouched open CLOSABLE target while a source-matching full proof candidate is already public and awaiting verification.

Disposition:

`I0083 = HOLD_CLAIMED_RESOLUTION_UNVERIFIED / NOT READY / NO R20 CLAIM`.

A future admission would require either independent proof-level validation/acceptance of the September candidate (then mark KNOWN) or a documented fatal gap preserving the source problem as current-open. R20 does neither here.

## 5. Method #28 — typical rather than all: why neither row supplies a lawful CLOSABLE successor

For D0076, proving locality for “typical” random local perturbations, for one gadget family, or for one Cayley/height-function subclass does not answer the source's universal locality question. Those restricted directions can be useful mathematics but do not satisfy the R20 CLOSABLE source endpoint.

For I0083, testing typical pairs of symmetric unimodal measures is weaker than the universal conjecture, and the intake already contains substantial numerical no-counterexample evidence. More typical-case numerics would not resolve the current proof-candidate status or close the source.

Thus the quantifier swap is diagnostic rather than a proof route: it explains why apparently tractable restricted versions are not lawful successors for this slot.

## 6. Ownership and exclusion refresh

Current canonical records rechecked during the pass include:

- I0035 claimed/reserved by C31;
- I0054 reserved by R11;
- I0070 reserved by R10;
- I0077 reserved by R07;
- I0078 claimed by C27;
- I0089 claimed by R14;
- I0095 reserved by R02;
- I0115 claimed by R12;
- H0024 claimed by R7-05;
- I0130 claimed/active in another CLOSABLE lane.

The newest task-health admission screen additionally excludes I0128/Sendov as literature-resolved and leaves H0006 PENDING/HARD. No ownership file was overwritten or bypassed.

## 7. Scheduler/model-control truth

The limitation remains unchanged in the interface actually exposed to this run. Task controls expose title, prompt, schedule/start timing, timing mode, and enabled state. They expose **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run applied-model receipt, and no guaranteed one-hour execution field**. GPT-6/maximum therefore remains prompt text only here.

Changing that requires an authorized product/backend scheduling surface that persists model and reasoning-effort fields and exposes applied-run telemetry. A historical `You cannot modify this task` response such as the P26 case is an authorization-context boundary; the lawful route is the owning/admin-authorized context or platform support, not duplication or permission bypass. No scheduler change was attempted in this run.

## 8. Next admission direction

R20 remains `SUCCESSOR_ADMISSION_REQUIRED`. Do not reopen I0100, do not seize I0083 while its matching proof candidate is unresolved, and do not relabel D0076 as CLOSABLE.

Next Section-B moves: **#5 ADD A PARAMETER AND DIFFERENTIATE, #15 BREAK THE SYMMETRY ON PURPOSE, #22 READ THE FAILURES, NOT THE SUCCESSES**. Continue the admission cursor into a different unowned finite-constant/counterexample-shaped source row; require exact source, current literature, prior attempts, and ownership clearance before any create-only claim.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R20
  run_id: 2026-09-18T03-50-49Z_successor_admission_i0083_d0076_hold_3c8f21
  retired_predecessor:
    source: "Afonso S. Bandeira / Randomstrasse 2025 Conjecture 26 / I0100"
    metric: "largest admissible prime with matching exact primal and dual certificates"
    before: 1213
    after: 1213
    retained_set: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    retirement_count: 6
    state: OPEN_PARTIAL_RETIRED_HANDOFF
  successor_admission_metric:
    name: E_ready
    before: 0
    after: 0
  methods_this_run: [4, 11, 28]
  screened:
    D0076:
      disposition: CURRENT_OPEN_LOOKING_HARD_NOT_CLOSABLE
      claim_created: false
      evidence:
        - "Grimmett--Li known locality theorem under unimodular graph-height-function hypothesis"
        - "Grant--Li arXiv:2601.12571 (2026) local gadget transformations, not unrestricted Question 7.1"
        - "Grimmett arXiv:2608.19349 (2026) Grigorchuk connective constants, not unrestricted locality"
    I0083:
      disposition: HOLD_CLAIMED_RESOLUTION_UNVERIFIED_NOT_READY
      claim_created: false
      evidence:
        - "Hasebe--Ueda 2018 Conjecture 3.5"
        - "Anonymous, Symmetric unimodality under free additive convolution, 2026-09-07, DOI 10.5281/zenodo.22649756, version 0.1.0-candidate"
        - "candidate self-labels unrefereed; no external whole-proof review/independent reproduction/formal verification"
  status: SUCCESSOR_ADMISSION_REQUIRED
  remaining_obligation: "Find a source-exact, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor and acquire it create-only; otherwise continue the cursor without reopening retired I0100."
  finite_checker: NONE_ADMISSION_ONLY
  audit_ids: []
```

No email/Gmail, Drive, public posting, purchase, permission change, scheduler change, shared-root edit, peer-track edit, or numerical SDP output was produced.