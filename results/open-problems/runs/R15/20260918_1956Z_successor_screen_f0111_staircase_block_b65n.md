Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; free admission `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111 I prove an exact `r`-coordinate block-Pascal factorization through a new monotone staircase microkernel `E_r`, identify `E_2` as the first genuinely non-read-once obstruction, and prove that the tempting coarse block compression cannot yield a source-valid heterogeneous `C_gamma` proof because its base-point distortion is infinite on sparse bases. Methods #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — exact block-Pascal staircase factorization

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source or previously proved R15 material. I do not mark Talagrand Problem 10.9, Burdzy–Scheutzow Problem 7.2, or any larger source problem solved. No novelty claim is made without independent audit and a fuller citation-graph search.

## 1. Continuity, exact source fidelity, and admission state

I continued from the newest repository state rather than restarting the native title. I reread or exact-target-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- current coordinator status `operations/task_health/runs/2026-09-18T190200Z/status.md`;
- controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- immediately preceding R15 report `runs/R15/20260918_1924Z_successor_screen_f0111_coupled_pascal_cgamma_s64x.md`;
- preceding read-once report `runs/R15/20260918_1917Z_successor_screen_f0111_readonce_c1_s64w.md`;
- neighboring admission reading `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T18-56-30Z__post-e0086-admission-delta-screen-5-f0111-endpoint.md`;
- current F0111 repository search history.

The current coordinator status has admitted one finite CLOSABLE source to another native slot, `CHEN-CHEN-QI-2026-SMALL6`, but explicitly records **no additional free READY CLOSABLE target**. Thus the bounded free-admission metric remains

`E_READY_CLOSABLE: 0 -> 0`.

I create no successor claim and do not steal or auto-promote a PENDING queue row.

### Burdzy–Scheutzow source remains unchanged and is not reopened

Primary source rechecked on 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

- FBM: there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion.
- BBM: the time reversal is an FBM.
- 2BM: there exists one random time `S` such that the complete centered forward and backward half-paths at `S` are independent **standard Brownian motions**.
- Problem 7.2 asks whether FBM + BBM + independence, at an arbitrary random time `T`, of the two complete centered half-paths forces 2BM.

The source does **not** assume `T` is a stopping time and does **not** assume either half at `T` is Brownian. Problem 7.5 is different and remains excluded.

The six-run handoff remains controlling. The Theorem-6.1-derived candidate was eliminated because it had no source-valid independent real seam. The later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually 2BM by the excursion-Palm argument. There is therefore no surviving frozen counterexample candidate. The carried `2/4` is only the historical retirement value of the positive-route metric, not a claim that two obligations are verified on a live construction. I0076 stays `OPEN / PARTIAL / RETIRED-HANDOFF`; its unchanged counter is not incremented after retirement.

Fresh public queries dated 2026-09-18 for the exact title, `Problem 7.2`, the random-time independence wording, later Burdzy/Scheutzow material and citing pages recovered the original paper/publication record and no accessible later primary paper explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not an openness certificate.

## 2. Retained F0111 state from the preceding run

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9. For an up-class `A`, with product hazards `t=(t_i)`, write

`F_A(t) = -log(1-zeta_t(A))`.

Talagrand defines `A in C_gamma` if at every base `q>=0` there is a positive multilinear polynomial `P` with no constant term such that

`F_A(t) <= P(t)` for all `t>=0`,

and

`P(gamma q) <= gamma F_A(q)`.

Problem 10.9 asks for one universal `gamma>0` for all cardinality thresholds

`A_{n,k}={X subset[n]: |X|>=k}`.

Write

`F_{m,j}(t) = -log P_t(N_m<j)`

and use the harmless conventions `F_{m,m+1}=0` and only indices `1<=j<=m+1` below. The earlier Pascal work proved

`G_{m,j}=F_{m,j-1}-F_{m,j} >=0`,

and the pointwise gap ordering

`G_{m,2} >= G_{m,3} >= ... >= G_{m,m+1}`.                    (2.1)

The immediately preceding run proved, SELF_CHECK_ONLY and conditional on the preceding endpoint `gamma=1` theorem, the full finite-dimensional heterogeneous estimate

`A_{n,k} in C_{1/(n-k+1)}`.                                (2.2)

Its exact one-coordinate recursion is

`F_{m+1,k}(t,s)=F_{m,k}(t)+Phi(s,G_{m,k}(t))`,              (2.3)

where

`Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-u-v})`.                   (2.4)

The factor `1/(n-k+1)` in that proof is asymptotically sharp for this **one-coordinate** route. The explicit next instruction in that report was therefore to seek a genuine multi-coordinate update rather than another lemma on (2.3). That is what this run does.

## 3. Method #25 — COUNT THE SAME THING TWICE: exact latent-deficit representation

The right state is not one gap. It is the entire short string of adjacent gaps describing the old count deficit.

Fix integers

`1 <= r <= k-1`, `k <= m+1`,

and split the variables into an old block of size `m` with hazards `t`, and a new block of size `r` with hazards

`u=(u_1,...,u_r)`.

Let

`S_{m,j}(t)=P_t(N_m<j)=exp(-F_{m,j}(t))`.

For `d=1,...,r`, define the adjacent old gaps

`g_d(t)=G_{m,k-d+1}(t)`

`       =F_{m,k-d}(t)-F_{m,k-d+1}(t)`.                      (3.1)

Conditional on the old block having failed to reach level `k`, the exact probability that its deficit is `d`, i.e. that `N_m=k-d`, is

`P(N_m=k-d | N_m<k)`

` = [S_{m,k-d+1}-S_{m,k-d}]/S_{m,k}`

` = exp(-(g_1+...+g_{d-1})) (1-exp(-g_d)).`                 (3.2)

Now introduce, only as an exact probabilistic representation, independent Bernoulli variables

`Z_d ~ Bernoulli(1-exp(-g_d)), d=1,...,r`.                  (3.3)

Then the right side of (3.2) is exactly the probability that `d` is the **first** index with `Z_d=1`. No-success among `Z_1,...,Z_r` has probability

`exp(-(g_1+...+g_r))=S_{m,k-r}/S_{m,k}`,                   (3.4)

which is exactly the conditional probability that the old count is at most `k-r-1`.

Thus the count deficit under the old failure law has been represented exactly by a first-success process whose independent hazards are the adjacent Pascal gaps.

This is the block analogue of the scalar `G_{m,k}` state in (2.3).

## 4. Method #3 — PROVE SOMETHING STRONGER: an exact `r`-coordinate block recursion

Let `X_1,...,X_r` be the independent inclusion indicators in the new block, with hazards `u_i`, and put

`M_X=sum_{i=1}^r X_i`.

Define the monotone staircase class on the `2r` variables `(X_1,...,X_r,Z_1,...,Z_r)` by

`E_r = { exists d in {1,...,r}: Z_d=1 and M_X>=d }`.        (4.1)

Equivalently, if

`D=min{d:Z_d=1}`, with `D=infinity` if no such `d` exists,

then

`E_r={D<=M_X}`.                                             (4.2)

Let `F_{E_r}(u,g)` denote the hazard of this class under independent hazards `u_i` on the `X` variables and `g_d` on the `Z` variables.

### Theorem R15-F0111-BLOCK — exact block-Pascal staircase factorization

For every admissible `m,k,r` and every `t,u>=0`,

`F_{m+r,k}(t,u)`

` = F_{m,k}(t)`

`   + F_{E_r}(u_1,...,u_r;`

`               G_{m,k}(t),G_{m,k-1}(t),...,G_{m,k-r+1}(t)).`             (4.3)

#### Proof

Condition on the old failure event `{N_m<k}`. By (3.2)--(3.4), we may generate the old deficit `D=k-N_m` up to level `r` by the first-success index of the independent `Z_d`'s. If no `Z_d` succeeds for `d<=r`, then `N_m<=k-r-1`, and even all `r` new successes cannot reach total `k`.

If the first success is at `d<=r`, then the old count is exactly `k-d`, so the combined threshold is reached if and only if the new count satisfies `M_X>=d`.

Therefore, conditional on `{N_m<k}`, the event that adding the new block crosses level `k` is exactly `{D<=M_X}`.

It remains to justify the monotone form (4.1), which drops the apparent conditions `Z_1=...=Z_{d-1}=0`. For a fixed realization of the `Z` variables, `D<=M_X` if and only if **some** success occurs among `Z_1,...,Z_{M_X}`. That is exactly

`exists d: Z_d=1 and M_X>=d`.

Hence the conditional failure probability is `exp(-F_{E_r}(u,g))`. Multiplying by the old failure probability gives

`exp(-F_{m+r,k}(t,u))`

` = exp(-F_{m,k}(t)) exp(-F_{E_r}(u,g))`,

and taking `-log` proves (4.3). QED.

### Checks against the previous state

For `r=1`,

`E_1={Z_1=1 and X_1=1}`,

so

`F_{E_1}(u_1,g_1)=Phi(u_1,g_1)`.

Thus (4.3) reduces exactly to the previous scalar recursion (2.3); no convention has changed.

For `r=2`, the first genuinely new outer class is

`E_2`

` = [Z_1 and (X_1 or X_2)]`

`   or [Z_2 and X_1 and X_2]`,                              (4.4)

and

`F_{m+2,k}`

` =F_{m,k}`

`  +F_{E_2}(u_1,u_2;G_{m,k},G_{m,k-1}).`                   (4.5)

So a two-coordinate update does not require a vague collection of overlap corrections: it requires one explicit four-variable monotone microkernel.

## 5. Method #14 — FIND THE GROUP ACTING: quotient the outer obstruction before attacking it

The new class `E_r` is not an arbitrary `2r`-variable up-class.

The symmetric group `S_r` acts on the `X` variables while fixing the ordered `Z` variables. The class depends on the `X` block only through the count `M_X`. Its minimal true sets are exactly

`{Z_d} union A`, where `A subset {X_1,...,X_r}` and `|A|=d`,               (5.1)

for `d=1,...,r`.

Thus there are only `r` minterm orbits under `S_r`, one in each size `d+1`. The quotient state is the pair

`(M_X, D)`,

and the event is the triangular region `D<=M_X`.

This is a much smaller object than the original `n`-variable threshold. Any future block proof should attack this staircase quotient first rather than carrying all `2r` labels.

### The first block kernel is genuinely outside the read-once compiler

The preceding R15 run proved, conditional on the endpoint `C_1` theorem, that every monotone read-once formula is in `C_1`. It also isolated variable reuse as the obstruction for interior thresholds.

That obstruction already occurs at `E_2`.

#### Lemma 5.1 — `E_2` is not a monotone read-once AND/OR formula

The minterms of `E_2` are

`M_1={Z_1,X_1}`,

`M_2={Z_1,X_2}`,

`M_3={Z_2,X_1,X_2}`.                                       (5.2)

Suppose a reduced read-once monotone formula exists and split its root into two nonempty disjoint variable blocks.

- If the root is OR, every minterm lies wholly in one child block. But `M_1` and `M_2` force `Z_1,X_1,X_2` into one block, and then `M_3` forces `Z_2` into that same block, leaving the other root block empty. Contradiction.
- If the root is AND, the parent minterms are the Cartesian products of the two child minterm families. Since there are exactly three parent minterms, one child must have exactly one minterm. That child's nonempty minterm is therefore contained in **every** parent minterm. But

`M_1 intersect M_2 intersect M_3 = emptyset`.

Contradiction.

Hence `E_2` is not read-once. QED.

This gives a precise minimal target for the next route: the read-once `C_1` compiler stops not at an enormous threshold family, but at the four-variable staircase (4.4).

## 6. The tempting coarse block compression, and the exact factor it appears to gain

The staircase factorization also explains a seductive but invalid shortcut.

From (4.1),

`E_r subset {M_X>=1} intersect {some Z_d=1}`.                (6.1)

The two events on the right depend on disjoint independent blocks. Their hazards are

`U=sum_i u_i`,

and

`G=sum_{d=1}^r g_d`

` =F_{m,k-r}(t)-F_{m,k}(t)`.                               (6.2)

Therefore the exact block identity implies the global coarse bound

`F_{m+r,k}(t,u)`

` <= F_{m,k}(t) + Phi(U, F_{m,k-r}(t)-F_{m,k}(t)).`          (6.3)

Now the gap ordering (2.1) makes the cumulative gap look dramatically better than the one-coordinate gap. Indeed,

`G=sum_{j=k-r+1}^k G_{m,j}`                                (6.4)

is the sum of the first `r` (hence largest `r`) terms in the tail decomposition

`F_{m,k-r}=sum_{j=k-r+1}^{m+1} G_{m,j}`.                   (6.5)

There are `m-k+r+1` terms in (6.5), so

`G >= [r/(m-k+r+1)] F_{m,k-r}`.                            (6.6)

Since `n=m+r`, this is

`G >= [r/(n-k+1)] F_{m,k-r}`.                              (6.7)

If (6.3) were an **exact contact-preserving** recursion, batching `r` coordinates would appear to replace the one-coordinate factor `1/(n-k+1)` by

`r/(n-k+1)`.                                                (6.8)

Taking a macroscopic block would then look like a path to a dimension-free constant.

The next lemma proves why that argument is false in the actual heterogeneous `C_gamma` problem.

## 7. The coarse block route fails source-valid base budgets by an infinite factor

### Lemma 7.1 — sparse-base obstruction to coarse batching

Fix `k>=3` and `2<=r<=k-1`. Take `m>=k-r`. There are heterogeneous base vectors `(t,u)` for which

`F_{m+r,k}(t,u)=0`,                                         (7.1)

but the right side of the coarse increment in (6.3) is strictly positive:

`F_{m,k}(t)+Phi(U,F_{m,k-r}(t)-F_{m,k}(t))>0`.              (7.2)

#### Proof

Choose `t` with exactly `k-r` positive coordinates and every other old coordinate zero. Choose `u` with exactly one positive coordinate and every other new coordinate zero.

The combined base then has only

`(k-r)+1 <= k-1`

coordinates with positive inclusion probability. Hence it is impossible to select `k` elements under the product law, so the source threshold has probability zero and its hazard is exactly zero. This proves (7.1).

On the old block, reaching level `k` is impossible, so

`F_{m,k}(t)=0`.

But reaching level `k-r` has positive probability, because precisely `k-r` old coordinates have positive hazards. Thus

`F_{m,k-r}(t)>0`.

Also `U>0`. Therefore

`Phi(U,F_{m,k-r}(t))>0`,

which proves (7.2). QED.

### Consequence

The distortion ratio of the coarse outer event to the actual threshold is **infinite** on legitimate base points allowed by Talagrand's Definition 10.1. Thus no fixed positive `gamma` proof can simply:

1. replace the exact staircase `E_r` by the coarse AND event in (6.1),
2. build a contact/budget certificate for that larger event,
3. and transfer the budget back to `A_{n,k}`.

At the sparse base above, the target budget is exactly zero while the coarse event already has positive hazard.

So the factor `r` in (6.8) is real in the cumulative-gap arithmetic but **cannot be harvested by forgetting the deficit level**. Any valid block proof must preserve the staircase state (4.1), or an equally fine state that still knows how many new successes are required.

This is the main negative lesson of the run and prevents a false universal-constant claim.

## 8. What a successful block proof now has to contain

The preceding one-coordinate proof lost a factor because it remembered only one adjacent gap. The present theorem shows the exact state needed to avoid that loss:

- the new-block count `M_X`;
- the old deficit encoded by the ordered first-success hazards

`g_1=G_{m,k}, g_2=G_{m,k-1}, ..., g_r=G_{m,k-r+1}`;

- the staircase comparison `D<=M_X`.

The source gap ordering becomes

`0<=g_1<=g_2<=...<=g_r`,                                    (8.1)

because `G_{m,j}` decreases with `j`.

Thus the next small mathematical target is no longer “prove a better Pascal lemma.” It is:

> Build a positive multilinear majorant for the four-variable kernel
> 
> `E_2=(Z_1 AND (X_1 OR X_2)) OR (Z_2 AND X_1 AND X_2)`
> 
> that is compatible with the cone `0<=g_1<=g_2` **and** with substitution
> `g_1=F_{m,k-1}-F_{m,k}`, `g_2=F_{m,k-2}-F_{m,k-1}` without separately certifying either non-polynomial difference.

If this can be done with a source-valid base budget stronger than two consecutive scalar applications, it is the first genuine route around the sharp `1/(n-k+1)` loss.

A general solution should then exploit the `S_r` quotient of `E_r`, not a label-by-label `2r`-variable expansion.

## 9. Literature / prior-art pass

Dated public queries on 2026-09-18 included:

- Talagrand exact title, Definition 10.1, `Problem 10.9`, `C_gamma`, cardinality-threshold wording;
- later Talagrand-threshold literature including DeMarco–Kahn, *Note on a problem of M. Talagrand* (RSA 2015), Frankston–Kahn–Park, *On a problem of M. Talagrand* (RSA 2022), and Warnke, *Note on down-set thresholds* (RSA 2024);
- exact and nearby searches for the block/staircase hazard formulation, Pascal gaps and cardinality thresholds;
- Burdzy–Scheutzow exact title / Problem 7.2 / random-time independent halves / later author and citing material.

The primary Talagrand PDF was reread at Definition 10.1 and Problem 10.9. The related later papers found in public indexing concern other threshold / weakly-small / down-set formulations; the bounded search did not expose a publication explicitly resolving this exact positive-multilinear-majorant Problem 10.9 or stating the staircase factorization (4.3).

For Burdzy–Scheutzow the search recovered the original publication and citing pages but no accessible later primary paper explicitly claiming to settle exact Problem 7.2.

These are **bounded negative searches only**. Public indexing is incomplete, and the factorization above is elementary enough that it may be folklore in reliability / Poisson-binomial language. Novelty is **UNVERIFIED**.

## 10. Methods outcome and next route

### #3 PROVE SOMETHING STRONGER

Succeeded. The scalar Pascal recursion was upgraded to the exact `r`-coordinate factorization (4.3), with no approximation and no symmetry assumption on the original base vector.

### #14 FIND THE GROUP ACTING

Succeeded. The outer obstruction has `S_r` symmetry on the new coordinates and only `r` minterm orbits. The first unresolved block object is the four-variable quotient kernel `E_2`, not a generic high-dimensional class.

### #25 COUNT THE SAME THING TWICE

Succeeded. The same old conditional deficit law was counted both through threshold failure ratios `S_{m,j}/S_{m,k}` and through the first-success distribution of independent latent Bernoulli hazards `g_d`. This yields the exact staircase representation.

The next research pass should not return to the coarse block envelope. The smallest source-relevant special case is `E_2` with ordered gap hazards. A useful next triple, avoiding the present one, is:

- #7 TAKE THE LIMIT — identify the high-activity and sparse boundary extremizers of the `E_2` support problem;
- #8 DISCRETIZE — reduce the ordered-gap support inequality to an exact finite sign/region decomposition if possible;
- #26 HUNT THE SPORADIC CASE — search for a genuinely asymmetric `E_2` base at which every natural positive support ansatz fails, before conjecturing a uniform block rule.

No numerical sample will be counted as a Brownian-law or threshold-theorem verification.

## 11. Model / scheduler / denied-task boundary

The exposed scheduler control surface still provides task identity/title/prompt, schedule/start information, timing mode and enabled state. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed-duration field**. Therefore GPT-6 / maximum remains prompt text only here; actual reasoning effort is UNVERIFIED.

The historical P26 response `You cannot modify this task` was authorization-context-specific. Repository continuity records a later successful P26 update from another authorized P/C context. The lawful workaround is the owning/authorized task context or an owner/admin/product/backend/support surface that exposes the required controls — not task duplication, permission bypass, or a repository edit represented as scheduler repair.

No scheduler, permission, email, Drive, public-posting, purchase or external side-effect action was taken in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  native_source:
    id: I0076
    source: Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2
    metric: four source-matching obligations on one frozen counterexample candidate
    before: 2/4  # historical carried retirement value, not a live candidate score
    after: 2/4
    status: OPEN / PARTIAL / RETIRED-HANDOFF
    surviving_frozen_candidate: NONE
    unchanged_count: 6  # preserved at mandatory rotation; not incremented after retirement
    remaining_obligation: common-re-rooting relative-phase/cocycle obstruction from six-run handoff
    evidence:
      - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
    audits: []
  free_admission:
    metric: E_READY_CLOSABLE
    before: 0
    after: 0
    note: current coordinator has one newly admitted CLOSABLE target owned by another native slot; no additional free READY target
  retained_screen:
    id: F0111
    source: Talagrand, Are Many Small Sets Explicitly Small?, Definition 10.1 / Problem 10.9
    parent_status: PARTIAL / NOT CLAIMED
    prior_bound: A_{n,k} in C_{1/(n-k+1)}  # SELF_CHECK_ONLY
    movement:
      - exact r-coordinate block-Pascal factorization through staircase class E_r
      - exact S_r quotient/minterm-orbit description
      - proof E_2 is not monotone read-once
      - cumulative r-gap fraction r/(n-k+1) identified
      - sparse-base theorem proving coarse block compression has infinite target-budget distortion
    status: SELF_CHECK_ONLY / NOVELTY_UNVERIFIED
    audits: []
  tried_moves: [3, 14, 25]
  next_moves: [7, 8, 26]
  checker_created: false
  checker_reason: theorem-sized parameter-uniform analytic claims; full proofs are on page
  scheduler_model_binding: UNAVAILABLE_ON_EXPOSED_SURFACE
  requested_model: GPT-6 maximum
  actual_model_reported: GPT-5.6 Sol
  reasoning_effort: UNVERIFIED
```
