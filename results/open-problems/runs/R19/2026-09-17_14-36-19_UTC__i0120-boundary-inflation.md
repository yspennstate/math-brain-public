Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime still provides no authenticated model-family selector, reasoning-effort selector, guaranteed-duration control, or applied-runtime attestation, so I do not claim GPT-6 / maximum. **NO MOVEMENT: active R19/I0120 `N_LR 14 -> 14`; supported unchanged count `4 -> 5`; STUCK RECOVERY 1 executed; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.**

# R19 — I0120 factor-aligned recovery: an exact `e_5=2` boundary survivor

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / STUCK RECOVERY 1 EXECUTED / FIRST LEVEL-15 TERMINAL ROUTE OBSTRUCTED / UNAUDITED / NO FIXED-METRIC CREDIT**.

## 1. Continuity: do not restart the scheduler-title target

I began from the complete current repository state rather than the stale scheduler title. I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the create-only active ownership claim `operations/claims/I0120.md`, the newest own report `runs/R19/2026-09-17_13-39-32_UTC__i0120-stuck1.md`, the I0084 handoff history, and the newest neighboring R20 report available at run start (`runs/R20/2026-09-17T13-17-45Z_i0100_projected_simplex_balance_7a4c2e.md`). I also rechecked the current R19 I0120 audit names and current primary literature.

The active canonical claim is still `operations/claims/I0120.md`, owner **R19**. The exact active source case is `LRC(14)`: fifteen total runners after one runner is made stationary, with the exact threshold `1/15` and the full integer-speed input class.

The frozen metric remains

`N_LR` = largest total number of runners for which the full classical Lonely Runner Conjecture is proved at the exact `1/N` threshold for the full source class.

Supported value before this run: **14**. Movement requires a complete unrestricted proof of `LRC(14)`, hence `N_LR=15`. Relation slices, finite gate obstructions, bounded searches, or restricted congruence families remain PARTIAL.

### Frozen predecessor I0084 is preserved exactly

The Hasebe--Ueda handoff remains frozen and is not reopened. Its source is arXiv:1710.08240v2, Conjecture 5.5 / intake I0084. The source-version convention retained by the campaign is ordinary **classical** convolution

`mu * S_t`

in both branches, including when `S_t` is the law of a **free** stable distribution. The asterisk is not replaced by free additive convolution. The exact source hypothesis is the finite `(2+alpha)` moment; stronger moment or compact-support statements remain restricted results. The retained alpha=`1/2` source-case metric is `2/2`, but the target rotated after six unchanged runs. The later two-audit PASS on abstract C010 is claim-scoped and does not close or reopen the parent arXiv-v2 package.

I0110/Salez likewise remains rotated after its own six unchanged runs.

## 2. Current literature gate — checked 2026-09-17

The primary line remains unchanged in scope:

- Touch Sungkawichai and Tanupat Trakulthongchai, arXiv:2604.23906v2, *Eleven, twelve, and thirteen lonely runners*, give the finite-checking framework. Their Definition 2.1 says a tuple at level `l` is proper if either a grid witness exists or, after omitting one coordinate, the gcd with `l` exceeds one. Proposition 3.1 is the exact lifting sieve used by the current route.
- Jaan Allikvere, arXiv:2609.02604v1, *Fourteen lonely runners* (2026-09-02), proves the current full record: fourteen total runners. Its successful certified gates use binary filtering and a terminal `7^13` search at mixed level `14`; every no-witness terminal completion is gcd-proper because all coordinates are divisible by `7`. The recurring two-orbit phenomenon is explicitly empirical for the certified gates, not a general theorem.
- Matthias Beck and Samuel Everett, arXiv:2609.06259v1, *Lonely Runner Relations* (2026-09-05), prove the short-integer-relation localization used in the broader R19 reduction.
- The 2026-09-05 paper *A certified congruence family for fifteen lonely runners* proves only a residue-progression family and explicitly does not settle unrestricted fifteen runners.

A bounded fresh search found no primary-source unrestricted proof or refutation of `LRC(14)`. This is dated negative search evidence only, not a novelty certificate.

## 3. Recovery obligation carried in from the stuck report

The preceding mandatory stuck report chose exactly one recovery action: **port the nearest solved technique**. It asked whether, for the simplest relation slice

`v_2 = 2 v_1`

at `p=37`, a factor-aligned route based on the composite target scale `15=3*5`

`1 -> 3 -> 15`

or

`1 -> 5 -> 15`

could reproduce Allikvere's terminal mechanism: finitely many persistent improper states followed by a gcd-forcing kill at the target composite level.

This run tested that proposition rather than adding another state-space compression.

The result is negative and exact: **factor alignment by itself does not force the gcd clause at level `15`**, even on this easiest support-two relation slice.

## 4. Idea before code: the gcd clause has a sharp defect boundary

For a prime `q|l`, define

`e_q(v)=#{j : q does not divide v_j}`.

The key observation is that the gcd clause is exactly a threshold on this defect count.

### R19-LR6 — exact gcd-boundary criterion

The gcd properness clause

`exists i: gcd(l,v_1,...,omit v_i,...,v_k)>1`

holds **if and only if**

`exists prime q|l: e_q(v)<=1`.

Proof: if the gcd is greater than one, any prime divisor `q` of it divides `l` and all coordinates except possibly the omitted one, so `e_q<=1`. Conversely, if `e_q<=1`, omit the unique nondivisible coordinate (or any coordinate when `e_q=0`), and `q` divides the resulting gcd.

Therefore the first gcd-improper boundary is not mysterious:

`e_q=2`.

Allikvere's successful terminal level is deep inside the killed region (`e_7=0`). A fifteen-runner terminal branch can survive at the minimal boundary `e_5=2`.

## 5. A general mechanism: two-unit inflation

The structural reason is the following.

### R19-LR7 — two-unit inflation lemma

Fix `k>=4`, a prime `p`, a positive integer `l`, and a prime `q!=p`. Suppose

`y=(y_1,...,y_{k-2}) in Z_{p,l}^{k-2}`

has **no** grid witness at the `k`-coordinate threshold `1/(k+1)`: for every integer `a`, at least one core coordinate satisfies

`||a y_j/(lp)|| < 1/(k+1)`.

Choose `z_1,z_2` with

`gcd(z_1,pql)=gcd(z_2,pql)=1`.

Then

`v=(q y_1,...,q y_{k-2},z_1,z_2)`

is `(k,p,ql)`-improper.

**Witness proof.** At a candidate time `t=a/(qlp)`, every scaled core coordinate has

`||t(qy_j)||=||a y_j/(lp)||`.

The core already blocks every numerator, so no full witness exists.

**Gcd proof.** For every prime `r|ql`, both `z_1,z_2` are nondivisible by `r`. After omitting any one coordinate at least one of them remains. Hence no prime divisor of `ql` can divide all retained coordinates, so every omission has gcd one with `ql`.

If a relation is supported on the core, scaling by `q` preserves it modulo the new modulus. Thus this mechanism is compatible with the R19 relation-preserving gate.

This is a theorem-sized claim with the full proof on the page; the exact finite checker below is not being used as a substitute for it.

## 6. Exact `p=37` obstruction on the `(2,1)` relation slice

Take the twelve-coordinate level-3 core

`Y=(3,6,11,5,7,46,1,8,13,2,9,10)`

at modulus `37*3=111`.

The exact checker verifies that every coordinate is nonzero modulo `37`, that

`Y_2=2Y_1 mod 111`,

and that **no** numerator modulo `111` gives all twelve coordinates distance at least `1/15`.

Now apply R19-LR7 with `q=5` and unit padding `1,2`. This gives

`T=(15,30,55,25,35,230,5,40,65,10,45,50,1,2)`.

At level `15`, modulus `555`, the tuple is improper. More sharply,

`e_5(T)=2`,

so it lies exactly on the minimal gcd-improper boundary.

The checker then verifies every natural projection of this same branch at levels `1,3,5,15`:

| `l` | modulus | relation `v_2-2v_1` | witness count | gcd-proper omitted indices | `e_3` | `e_5` |
|---:|---:|---:|---:|---|---:|---:|
| 1 | 37  | 0 | 0 | none | 10 | 8 |
| 3 | 111 | 0 | 0 | none | 11 | 3 |
| 5 | 185 | 0 | 0 | none | 10 | 2 |
| 15| 555 | 0 | 0 | none | 11 | 2 |

Thus the same relation-compatible improper branch survives **both** factor orders through level 15:

`1 -> 3 -> 15`

and

`1 -> 5 -> 15`.

This kills the specific recovery hope that merely reaching a level divisible by all factors of `15` forces the terminal gcd kill. It does **not** establish that the seed is non-eventually-proper: some later level may still eliminate every lift. Therefore this is not a proof that `J_(2,1)^rel(14,37)` is nonempty, and it is not a counterexample to LRC.

## 7. Section-B moves and outcomes

### #6 DEFORM TO A POINT YOU CAN SOLVE

I deformed the full level-15 state space to the sharp divisibility boundary `e_5=2`. On that face the survivor has an exact normal form: a twelve-coordinate lower-level blocking core multiplied by `5`, plus two unit padding coordinates.

**Outcome:** successful. It produced R19-LR7 and the explicit tuple `T`, explaining *why* the factor-aligned terminal route survives.

### #21 ASK WHO ELSE HAS THIS SHAPE

The shape is already implicit in the finite-checking literature: Sungkawichai--Trakulthongchai's gcd clause kills precisely a divisibility boundary, while Allikvere's terminal success lands at defect zero. The restricted fifteen-runner congruence-family result also has to treat common-divisor branches specially because `15` is composite; it is not a general resolution.

**Outcome:** the transferable quantity is `e_q`, not “composite level” itself. Fourteen runners succeeds at a terminal state with `e_7=0`; the present fifteen-runner relation slice survives at the extremal value `e_5=2`.

### #29 ADD THE POINTS AT INFINITY

I organized the divisibility states as boundary strata `e_q=0,1,2,...`. The properness clause removes the first two strata. R19-LR7 shows that the first remaining boundary `e_q=2` is naturally populated by inflated no-witness cores.

**Outcome:** the next obstruction is now sharply named. A valid termination theorem must classify or eliminate `e_q=2` boundary branches rather than hope the target factorization itself eliminates them.

## 8. Exact validation

I wrote the idea and proofs first, then created one exact-arithmetic checker for the finite claims:

`artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check.py`

Archived execution:

`artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check_output.txt`

The checker verifies the relation, the absence of every grid witness at levels `1,3,5,15`, the failure of every gcd-proper omission, the lower-level blocking core, the inflation identity, and the exact boundary count `e_5=2`. It ends

`ALL_EXACT_CHECKS_PASS`.

Full mathematical proof artifact:

`artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_inflation.md`.

These are self-checks for the R19 work; no outside audit is claimed.

## 9. What this changes and what it does not

It changes the research route: **the first factor-aligned `3/5 -> 15` terminal strategy is now explicitly obstructed**. A longer brute-force implementation of the same idea would be poor use of the next run.

It does not move the frozen source metric. `N_LR` remains `14`, because no complete unrestricted fifteen-runner proof has been produced.

The exact remaining obligation is still the termination obligation for enough short-relation gates, but the useful sub-obligation has changed:

> classify or force termination of relation-compatible branches on the minimal gcd-improper boundary `e_q=2`.

No completed `P26-AUDIT-R19-I0120` and no distinct completed `R18-AUDIT-R19-I0120` was found in the current repository search. I0120 remains **UNAUDITED / SOURCE OPEN**. No paper folder is created.

This is the fifth consecutive unchanged active I0120 run. Under the controlling CLOSABLE rule, **one further unchanged run reaches the six-run rotation threshold**. Do not reset the count because the route changed.

## 10. Next new-method assignment

The next run should not repeat #6/#21/#29 and should not add another compression lemma. Use the previously unused I0120 moves:

- **#12 FIND WHAT IS CONSERVED** — determine whether the two exceptional unit coordinates on an `e_q=2` face carry a lift-invariant residue, cross-ratio, or relation class;
- **#13 FIND WHAT ONLY INCREASES** — seek a defect/coverage monovariant that forces the `e_q=2` face either toward a witness or toward a gcd-killed face under additional lifts;
- **#25 COUNT THE SAME THING TWICE** — count blocking incidences between grid times and the scaled core versus the two units, looking for an equality/deficit that forbids indefinite persistence.

If these do not move `N_LR`, the next report must perform the mandatory six-unchanged CLOSABLE rotation and leave the `e_q=2` survivor plus R19-LR7 as the durable handoff.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  active_claim: I0120
  source: "Classical Lonely Runner Conjecture; active source case LRC(14), fifteen total runners"
  target: "prove unrestricted LRC(14) at exact threshold 1/15 for the full integer-speed class"
  metric: "N_LR = largest total number of runners with the full exact-threshold classical conjecture proved"
  before: 14
  after: 14
  movement: "no movement"
  unchanged_count_before: 4
  unchanged_count_after: 5
  status: "PARTIAL / SOURCE OPEN / STUCK RECOVERY 1 EXECUTED / FIRST LEVEL-15 TERMINAL ROUTE OBSTRUCTED / UNAUDITED"
  tried_moves: [6, 21, 29]
  new_claims:
    - "R19-LR6: gcd clause iff e_q<=1 for some prime q|l"
    - "R19-LR7: two-unit inflation embeds a lower-level no-witness core into an improper higher-level boundary state"
    - "exact p=37 relation-(2,1) branch T is improper at levels 1,3,5,15 and has e_5=2 at level 15"
  remaining_obligation: "find a genuine termination mechanism for relation-compatible e_q=2 boundary branches; absent metric movement next run, rotate I0120 after six unchanged CLOSABLE runs"
  evidence:
    proof_artifact: "artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_inflation.md"
    exact_checker: "artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check.py"
    checker_output: "artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check_output.txt; ALL_EXACT_CHECKS_PASS"
  audits:
    I0120: "none found; P26 and distinct R18 end-to-end audits absent"
    preserved_I0084_C010: "two distinct claim-scoped PASS audits exist; parent I0084 remains rotated/partial"
  preserved_predecessor:
    I0084: "arXiv:1710.08240v2 Conjecture 5.5; ordinary classical mu*S_t even for free-stable S_t; alpha=1/2 metric 2/2; rotated, not reopened"
```

## 12. Model / scheduler control

The implementation record remains unchanged in the only way this worker can honestly report it. The exposed scheduler surface has prompt/title/schedule/timing/enabled-state controls but **no model-family selector, no reasoning-effort selector, no guaranteed-hour execution control, and no authenticated per-run model receipt**. GPT-6 / maximum is therefore prompt text only in this context. Enforcing it would require an authorized product/backend surface that exposes those fields and runtime attestation.

The historical P26 response `You cannot modify this task` was an authorization/context boundary. Other repository receipts show that an authorized context later succeeded in modifying P26. The legitimate workaround is the owning/authorized scheduler context or platform support; duplicating the task or bypassing permissions is not legitimate. No scheduler change was attempted in this run.
