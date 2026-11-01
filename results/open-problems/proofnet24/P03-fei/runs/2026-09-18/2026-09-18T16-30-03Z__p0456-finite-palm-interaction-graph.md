Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**, and I do not claim otherwise.

**NO SOURCE-LEVEL METRIC MOVEMENT.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`. This run used fresh Section-B methods **#18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE, #29 ADD THE POINTS AT INFINITY** and proves a new all-fixed-`r` supporting theorem which replaces Claim 289's prose-level “complete interaction pattern” by an explicit finite interaction graph plus an exact no-late-influence statement. The source-matching chain remains **AUDIT-PENDING**, not CLOSED.

# P03 / P0456 run report — finite Palm interaction graph and no-late-influence compactification

Run timestamp: **2026-09-18T16:30:03Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, status, sources, and incoming-audit gate

The exclusive canonical assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The exact source is Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`. The model `LK(n,k)` places iid Uniform[0,1] weights on the edges of `K_n` and keeps an edge exactly when it is among the `k` lowest-weight incident edges at both endpoints.

A fresh read of the Cambridge article and PDF confirms that Section 1.1 still says connectivity is not known in

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`

and explicitly attributes the gap to analytically convenient sufficient conditions. I reread the literal pair mechanism in Lemmas 10--14 and the connectivity statements in Theorems 4--6. A fresh bounded 2026-09-18 search for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral/mutual-preference constant-window variants recovered the source and structurally adjacent nearest-neighbour work but no later theorem matching Claims 288--291. This is **bounded negative evidence only**; publication novelty remains `UNVERIFIED`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T15-44-27Z__p0456-pair-smallcomp-audit-kernel.md`,

creation commit `aa3a334c23fcf3ab8039cde7c25fda77104f0530`, blob `a13c4efd3046bca3101870728fe03780006d5cbc`.

I recovered/reread the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, the current `FLEET_RULES.md` / owner directive, the current P0456 claim, the newest P03 report, the campaign/root status surfaces by targeted reads/search, the newest P26 work, the terminal P04 records, and neighbouring P0457 only for nonduplication. Large search/connector surfaces were targeted and can be truncated by the connector; those are **not** represented here as byte-for-byte whole-repository rereads. Exact-path/commit reads were used for the proof inputs that matter below.

### Incoming audit screen

Fresh searches for the exact Claim-288/289/291 identifiers plus broader `P0456`, `Poisson`, `audit`, and `PASS` phrases recovered **no P26 or distinct OTHER-track full-chain audit** of the source-matching proof. The newest P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_16-57-29__run-report.md`;

it audits historical P04/I0101 Claims 26 and 25, not P0456. Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits by P03 do not count. No final paper folder is created.

### Preserved source-matching chain

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

For each fixed `C`, Claim 289 states uniformly on integer `|k-log n|<=C`, with `lambda_n=n e^{-k}`,

`d_TV(Law(Z_n), Poisson(lambda_n)) -> 0`

and

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.

The proof input still most deserving of external scrutiny is the all-fixed-`r` joint isolation asymptotic. Claim 291 gave a compact `r=2` kernel but correctly warned that pairs alone do not imply Poisson. This run attacks exactly that gap in presentation.

---

## 2. New supporting theorem

### Claim `P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix integers `r>=1` and a real `C<infinity`. Uniformly over integer `k` with

`|k-log n|<=C`,                                                (2.1)

for any fixed distinct roots `v_1,...,v_r`,

`P(I_{v_1} cap ... cap I_{v_r}) = e^{-rk}(1+o_C(1)).`          (2.2)

Moreover the dependence among these `r` isolation events has an explicit **depth-one finite interaction graph**: its vertices are root proposal slots and selected labels, and its only non-product defects are

1. repeated selected labels;
2. selected--selected edges lying below a proposal deadline;
3. root--selected cross edges lying below another root's selected-neighbour deadline; and
4. early root--root edges.

After these defects are removed/charged, the remaining rejection lists are literally disjoint. There is no hidden recursive dependency beyond depth one: an edge outside this finite interaction graph cannot change any root's isolation mark once it is above every deadline at an incident selected label.

This theorem reproves the all-fixed-`r` input of Claim 289 in a form designed for external audit. It gives **no new source-level closure label** and is not an independent audit.

---

## 3. #18 SAY IT IN ANOTHER LANGUAGE — from interaction strata to a finite exploration graph

Fix roots `R={v_1,...,v_r}`. Temporarily delete the `binom(r,2)` root--root edges from all root preference orders. Put

`N=n-r`.

For root `v_a`, list the first `k` nonroot proposal labels in increasing edge-weight order as

`L_{a,1},...,L_{a,k}`,

with proposal weights / deadlines

`D_{a,i}=W(v_a,L_{a,i})`.

Because the root stars are disjoint after root--root edges are removed, the ordered label tuples

`(L_{a,1},...,L_{a,k})`

are independent across `a`, and each is a uniform ordered `k`-tuple without replacement from the same `N` labels. Numerical root order statistics are independent of these rank labels.

### 3.1 Interaction graph

Construct a finite bipartite/multigraph `H` as follows.

- There is a proposal-slot vertex `(a,i)` for every `a<=r`, `i<=k`.
- Proposal slots carrying the same nonroot label are identified with one selected-label vertex. Equivalently, the equality pattern of the `rk` labels is a partition `pi` of the proposal slots, with the constraint that no block contains two slots from the same root.
- Add a defect edge for every unique selected--selected graph edge whose weight lies below at least one proposal deadline at an incident selected label, so that it could be counted as a competitor deleted by an outside-only rejection test.
- Add a defect edge for every root--selected edge `{v_b,u}` where `u` is selected by another root, is **not** selected by `v_b`, and the edge weight lies below a proposal deadline at `u` that it could help.
- Add a root--root defect for every temporarily removed root--root edge which lies below at least one of its endpoint root `k`th nonroot thresholds.

The complexity `K(H)` is

`collision excess + number of unique active selected/root-selected edges + number of early root-root edges`.   (3.1)

If a selected label occurs in `q` root blocks, it contributes `q-1` to collision excess. An edge that could help several contaminated deadlines is counted once as an edge defect; when disjointizing below, all deadlines it can help are omitted. Since `r` is fixed, one defect removes only `O_r(1)` deadlines.

### 3.2 Exact no-late-influence lemma

The change of language exposes a point which is easy to obscure in prose.

**Lemma 3.1 (depth-one / no late influence).** Conditional on the root proposal labels and proposal weights, whether root `v_a` is isolated is determined by the edge inequalities

`W(L_{a,i},z) < D_{a,i}`,

with `i<=k` and `z != v_a,L_{a,i}`, together with the finitely many root--root rank comparisons. In particular:

- edges not incident to a selected label cannot affect rejection of a root proposal;
- an edge inside `R union {selected labels}` which lies above every proposal deadline it could serve is deterministically irrelevant;
- after every repeated selected-label deadline and every deadline touched by an active internal edge is omitted, every remaining rejection constraint uses only an edge from one selected label to the external vertex set, and those edge sets are pairwise disjoint.

**Proof.** Edge survival in `LK(n,k)` for a root proposal `{v_a,u}` fails at the endpoint `u` exactly when at least `k` edges incident to `u` have smaller raw weight than `W(v_a,u)`. Determining this count requires only the one-star family `{W(u,z):z != u}`. It does **not** require asking whether any competitor edge `{u,z}` itself survives bilateral preference, and therefore does not recursively inspect the preference list of `z`. Hence an edge can influence a root isolation mark only if it is incident to one of the root's selected labels and lies below that selected label's proposal deadline. Once all such internal edges have been charged and the affected deadlines omitted, the remaining competitors are external edges attached to distinct selected labels; two such lists contain different undirected edges even when their external endpoint `z` is the same. They are therefore independent iid edge families. `square`

This exact depth-one property is the requested #29 compactification mechanism in embryonic form: there are no undiscovered “points at infinity” after the selected-neighbour star boundary.

---

## 4. #25 COUNT THE SAME THING TWICE — exact finite label skeletons

The first count is entirely finite and exact.

Let `pi` be a compatible partition of the `rk` ordered proposal slots, and let `m(pi)` be its number of blocks. Put

`c(pi)=rk-m(pi)`                                                (4.1)

for its collision excess.

### Lemma 4.1 (exact partition probability)

For every compatible `pi`,

`P(the equality partition of the proposal labels is exactly pi)
 = (N)_{m(pi)} / (N)_k^r`.                                    (4.2)

**Proof.** The total number of independent ordered root label arrays is `(N)_k^r`. Once `pi` is fixed, choose a distinct nonroot label for each of its `m(pi)` blocks. There are exactly `(N)_{m(pi)}` injective assignments. Each assignment determines one ordered label array realizing `pi`, and every realizing array arises uniquely this way. `square`

For fixed collision excess `c`, (4.2) gives

`P(pi)=N^{-c}(1+O_{r,c}(k^2/N))`.                             (4.3)

The number of witness-labelled compatible partitions with collision excess `c` is at most `(rk)^{2c}`: sequentially, each of the `c` repetitions can be witnessed by the repeated slot and an earlier slot carrying its label. Therefore, for fixed `c`,

`P(collision excess >=c) <= (C_r k^2/n)^c`.                  (4.4)

This recovers Claim 289's collision rate but now from an exact finite count rather than an unnamed stratum.

---

## 5. Active-edge skeletons and their codimension

Choose a fixed integer cutoff `D_0>r+3`. Then choose a constant `L=L(r,D_0)>2` such that

`rho(L):=L-1-log L > r+D_0+3`.                               (5.1)

Let `T_a` be the `k`th nonroot root threshold and put

`G_L={max_a T_a <= Lk/n}`.

A standard binomial/order-statistic Chernoff bound gives, uniformly under (2.1),

`P(G_L^c) <= r exp[-rho(L)k+o(k)]
           = o(e^{-rk} n^{-D_0}).`                            (5.2)

On `G_L`, every proposal deadline is at most `Lk/n`.

### 5.1 Selected--selected active edges

Conditional on all root stars, a selected--selected edge between two distinct nonroot selected labels is an untouched iid Uniform[0,1] edge. A specified such edge is active with conditional probability at most

`2Lk/n`.                                                       (5.3)

The factor 2 merely allows the edge to lie below an applicable deadline at either endpoint.

### 5.2 Root--selected cross edges

Suppose `u` is selected by root `v_a`, `a != b`, but is not selected by `v_b`. Condition on root `b`'s selected labels and its `k`th nonroot threshold `T_b=t`. Then the edge weight `W(v_b,u)`, conditional on being nonselected, is exactly Uniform[`t`,1]. Therefore for any deadline `D<=Lk/n`,

`P(W(v_b,u)<=D | T_b=t, u nonselected at b)
 = (D-t)_+/(1-t)
 <= C_L k/n`.                                                  (5.4)

Distinct prescribed cross edges remain conditionally independent after the selected-label equality pattern is fixed, because they are distinct iid graph edges.

### 5.3 Root--root edges

A temporarily removed root--root edge is independent of all nonroot root stars. On `G_L` it is early with probability at most

`2Lk/n`.                                                       (5.5)

There are only `binom(r,2)` such edges.

### Lemma 5.1 (explicit skeleton cost)

Fix a witness-labelled interaction skeleton with collision excess `c`, `q` unique active selected/root-selected edges, and `p` early root--root edges. Let

`d=c+q+p`.                                                     (5.6)

Then on `G_L`, uniformly under (2.1),

`P(this skeleton) <= n^{-d+o(1)}`.                            (5.7)

For each fixed `d`, the number of witness-labelled skeletons is `k^{O_{r,d}(1)}=n^{o(1)}`.

**Proof.** Use (4.2) for the label partition. Conditional on the labels and numerical root thresholds, expose each prescribed unique internal graph edge once. Equations (5.3)--(5.5) contribute at most `(C_{r,L}k/n)^{q+p}`. The witness identities contribute only a fixed power of `k`. Since `k=log n+O(1)`, all powers of `k` are `n^{o(1)}`. `square`

The same sequential enumeration, summed geometrically over `c,q` and over the finitely many root--root choices, gives the **total-complexity** tail

`P(G_L, K(H)>=D_0) <= n^{-D_0+o(1)}=o(e^{-rk}).`             (5.8)

This is slightly stronger conceptually than bounding collision and active-edge tails separately: defects split among types still pay their full summed codimension.

---

## 6. Bounded nonzero skeletons: disjointization without prose strata

Fix a skeleton `H` with

`1<=K(H)<D_0`.                                                (6.1)

Perform the following deterministic operation.

1. In each selected-label collision block, choose one occurrence to retain and omit every rejection deadline attached to the other occurrences.
2. For every active selected/root-selected edge, omit every rejection deadline for which that edge could serve as a competitor.
3. For every early root--root edge, omit/shift the at most `O_r(1)` root proposal deadlines whose ranks can be changed by reinserting it.

Because `r,D_0` are fixed, this omits at most `O_{r,D_0}(1)` deadlines per root.

By Lemma 3.1, after these omissions every surviving rejection list consists only of edges from one distinct selected label to

`V \ (R union all selected labels)`,                           (6.2)

and the surviving lists are literally disjoint edge families.

Claim 291's bounded-omission marked-saddle lemma therefore gives, conditional on the fixed skeleton,

`P(all remaining rejection constraints)
 <= exp[-rk+o(k)].`                                           (6.3)

The `o(k)` is uniform over bounded offsets and over the bounded number of fixed defects.

Combining (5.7) and (6.3), a skeleton of positive complexity `d` contributes at most

`e^{-rk+o(k)} n^{-d+o(1)}.`                                  (6.4)

Summing the `n^{o(1)}` bounded-complexity skeletons gives

`P(all roots isolated, 1<=K(H)<D_0, G_L)
 <=e^{-rk+o(k)} n^{-1+o(1)}
 =o(e^{-rk}).`                                                (6.5)

Together with (5.2) and (5.8), **all nonzero interaction skeletons are negligible on the joint-isolation scale**.

---

## 7. Zero skeleton and the matching lower bound

### 7.1 Upper bound on the zero skeleton

If `K(H)=0`, then

- all selected labels are distinct;
- no internal selected/root-selected edge lies below a deadline it could help;
- no root--root edge lies below a root `k`th nonroot threshold.

Hence actual isolation forces every selected neighbour to find all `k` lighter competitors in the external pool (6.2). Those external lists are disjoint. Their common pool size is `n-O_r(k)`, so the clean marked-saddle estimate from Claims 288/291 gives independently for every root

`M_{k,k}=e^{-k}(1+o_C(1)).`                                   (7.1)

Therefore

`P(all roots isolated, K(H)=0)
 <= e^{-rk}(1+o_C(1)).`                                      (7.2)

### 7.2 Sufficient event for the lower bound

Require simultaneously:

1. all `rk` selected nonroot labels are distinct;
2. `G_L` occurs;
3. every root--root edge has weight greater than `Lk/n`;
4. every selected neighbour has at least `k` lighter competitors in the external pool (6.2).

Then all root proposals are rejected using only external competitors, and reinserting root--root/internal edges cannot destroy a rejection. Hence all `r` roots are isolated.

The exact partition count gives pairwise-distinct labels probability

`prod_{a=0}^{r-1} (N-ak)_k/(N)_k = 1-O_r(k^2/n)`.             (7.3)

The root--root late-edge condition costs `1-O_r(k/n)`. By (5.2), restricting to `G_L` loses `o(e^{-rk})`. The external marked blocks are independent and each have probability `e^{-k}(1+o_C(1))`. Consequently

`P(all roots isolated) >= e^{-rk}(1-o_C(1)).`                (7.4)

Combining (6.5), (7.2), and (7.4) proves Claim 292:

`boxed{ P(I_{v_1}...I_{v_r})=e^{-rk}(1+o_C(1)) }.`           (7.5)

---

## 8. #25 again — the same skeleton in Palm / Poisson language

The second count is the limiting/Palm version of the finite skeleton calculation.

Condition on `r` distinguished root stars and view each ordered proposal slot as a marked atom `(a,i,L_{a,i},D_{a,i})`. The selected-label marks are asymptotically uniform in a label space of size `n`. A repeated label is therefore a diagonal coincidence of codimension one. More precisely, the exact finite formula (4.2) says that a partition with collision excess `c` has rate

`n^{-c+o(1)}`.                                                (8.1)

After scaling an internal edge weight by `n/k`, a specified selected--selected or nonselected root--selected edge falls into a bounded deadline interval with probability

`(k/n) theta + o(k/n)`                                        (8.2)

for a bounded mark-dependent `theta`; (5.4) is the exact finite conditional version of this Palm statement. Thus a skeleton with `c` diagonal coincidences and `q+p` active-edge inequalities has Palm rate

`n^{-(c+q+p)+o(1)}`,                                         (8.3)

exactly the finite rate (5.7). The polynomial powers of `k` count the possible marked proposal slots in either language and are `n^{o(1)}`.

So the two descriptions agree skeleton by skeleton:

`finite rank-labelled codimension = Palm defect codimension = K(H)`. (8.4)

In particular, for fixed roots the limiting Palm interaction graph is empty with probability tending to one on the `e^{-rk}` isolation scale; every nonempty finite skeleton carries one extra power of `n` after the root rejection cost.

This is a cross-check, not an independent OTHER-track audit.

---

## 9. #29 ADD THE POINTS AT INFINITY — exact compactification by `G_L` and depth one

There are two possible “infinities” in the exploration: an unusually late root proposal threshold, or a recursively expanding rejection neighbourhood. Both are now closed explicitly.

### 9.1 Late proposal thresholds

The compact event `G_L` cuts every root star at the deterministic scale `Lk/n`. By choosing `L` after fixed `r,D_0`, (5.2) makes the complement negligible not merely absolutely but relative to `e^{-rk} n^{-D_0}`. Thus no tail configuration can compensate for its rarity by gaining rejection probability.

### 9.2 Recursive influence

There is no recursive influence. A selected neighbour rejects a root proposal by **counting raw incident edge weights**, not by asking whether those competitors survive the bilateral rule. Lemma 3.1 therefore gives an exact finite Markov blanket: selected-neighbour stars up to their proposal deadlines. Beyond that depth-one boundary, every edge has zero influence on the root isolation indicators. The “point at infinity” in a hypothetical exploration tree is an absorbing irrelevant state, not another probabilistic tail that needs summation.

This is the main structural simplification of the run. It turns Claim 289's general fixed-`r` proof into a finite skeleton theorem with a literal terminal boundary.

---

## 10. Attempted Stein/Palm coupling and why I still do not claim it

The size-bias identity retained from Claim 291 is exact: for a uniform root `V`,

`Law(Z_n | I_V=1)`

is the size-biased law of `Z_n`. The finite interaction graph suggests a natural resampling algorithm: expose a root proposal block, force its selected neighbours to reject, and attempt to leave all other root isolation marks unchanged outside the depth-one blanket.

However, conditioning a root to be isolated biases `k` selected-neighbour stars, each with `Theta(n)` raw edge weights. Although the skeleton theorem says a **fixed number of other distinguished roots** interacts with this conditioning only through rare codimension-one defects, I do not yet have a coupling proving that the *total* number of isolation marks changed over all `n-1` other roots is `o(1)` in absolute expectation. The all-fixed-`r` factorial-moment proof already suffices for Poisson, but using it to justify such a global coupling would not be an independent Stein certificate.

Accordingly this run makes **no quantitative Stein--Chen rate claim** and does not use generic “local dependence” rhetoric as a substitute for an explicit coupling.

---

## 11. Connectivity-side recheck

Claim 292 concerns factorial moments, not components. I nevertheless rechecked the literal source definition against the retained component decomposition.

- Sizes `2,...,6`: Claim 291 uses each vertex's first `k-(r-1)` **external** proposals; these are necessarily among the global first `k` proposals regardless of internal tree weights. The tree-edge event and the external rejection event use disjoint edge families.
- Sizes `7,...,12`: retained Claim 280's Exp(1)/Cayley crossing-edge bound.
- Sizes `13,...,n/2`: retained Claim 278's global threshold-envelope argument; its envelope failure is paid once before summing component sizes.

No step infers connectivity from mean degree.

Thus this run finds no new connectivity-side gap, but the source-level theorem remains audit-pending until independent tracks check the chain.

---

## 12. Directed P03 -> P04 audit duty

The newest recovered P04 record remains

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`,

which explicitly creates no new mathematical theorem. Therefore there is no genuinely new accessible P04 successor claim to audit. I do **not** fabricate or repeat a previous P03 audit.

---

## 13. Cumulative P03 / P0456 ledger

Preserved:

- `P03-P0456-HARRIS-ISOLATION-ROOT2-274 = PROVED / STRUCTURAL-PARTIAL / SOURCE-SHAPED / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-OPTIMIZED-CUTOFF-WINDOW-ZERO-276 = PROVED / SOURCE-SCALE-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-EXACT-MARKING-FINE-WINDOW-278 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-JOINT-RACE-FINE-BRACKET-280 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-ORDERED-DEADLINE-FINE-WINDOW-ZERO-282 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-NORMAL-RACE-SQRTLOG-BRACKET-284 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-SPARSE-DELETION-SQRTLOG-ZERO-286 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

The exact abstract failure model from Claim 291 remains part of the honesty boundary: correct first and pair rare-event asymptotics alone do not imply Poisson.

---

## 14. Metric / stuck / protocol state

The frozen coefficient metrics remain

- `c_LK^cert=0` — SATURATED;
- `a_LK^fine=0` — SATURATED;
- `b_LK^sqrt=0` — SATURATED.

No saturated zero is counted as an unchanged stuck run. Claims 288--292 are in audit/repair state, not a new frozen-metric campaign. HARD recoveries remain `0/2`.

Current state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_292_ALL_R_AUDIT_KERNEL_READY`.

Exact remaining obligations:

1. P26 must independently audit the full source-matching 288/289 chain, preferably using Claims 291/292 as compact audit kernels rather than trusting P03 status labels.
2. One distinct OTHER track must independently audit the same implication chain.
3. Any audit objection takes priority over further strengthening.
4. Prior-art checking must continue; bounded search misses do not certify publication novelty.
5. Only after two distinct full-proof PASS audits should P03 create the self-contained paper folder and request shared-ledger closure through P26.

---

## 15. Next state / next concrete attack

If an incoming outside audit exists at the next invocation, read it first and repair any concrete objection immediately.

If the outside-audit gate is still empty, do **not** re-optimize the already saturated connectivity windows and do not rewrite the factorial-moment proof a fourth time. A fresh route should target an explicit global Palm coupling, using a new Section-B triple such as **#19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT, #28 REPLACE FOR ALL WITH TYPICAL**:

- algorithmically resample the graph under `I_V=1` while exposing exactly which other root isolation marks can change;
- identify the configuration maximizing the number of changed marks;
- prove the bad high-influence configurations are atypical strongly enough to make the absolute size-bias coupling error `o(1)`.

This would be genuinely independent of fixed factorial moments if successful. If it fails because conditioning one isolated root can globally perturb too many near-isolated vertices, record that failure rather than hiding it behind generic Stein language.

---

## 16. `ledger_delta` for P26

```text
track: P03
canonical_target: P0456
owner: P03
source: Dabirian--Subramanian J. Appl. Probab. 63(2) (2026), Section 1.1
source_status_in_primary_source: OPEN
source_matching_candidate_claims: 288,289
supporting_claims: 290,291,292
new_claim: P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292
new_claim_status: PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
new_claim_content: for every fixed r and bounded k-log n, joint isolation probability is e^{-rk}(1+o_C(1)); explicit finite depth-one interaction graph, exact compatible-partition count, defect codimension, and no-late-influence lemma replace vague complete-pattern language
metrics: c_LK^cert=0 SATURATED; a_LK^fine=0 SATURATED; b_LK^sqrt=0 SATURATED
metric_movement: none; saturated zeros are not stuck counts
hard_recoveries_used: 0/2
outside_full_chain_audits_found: 0/2
p26_audit_found: no
second_other_audit_found: no
closure_status: ACTIVE_AUDIT_PENDING
paper_folder: not created
p04_directed_audit: no new P04 mathematical claim exists; no repeat audit fabricated
requested_p26_action: independently audit Claims 288/289 using Claims 291/292 as compact kernels; do not close without a distinct second OTHER-track PASS
```

No shared root ledger was edited by P03.

**End of complete run report.**