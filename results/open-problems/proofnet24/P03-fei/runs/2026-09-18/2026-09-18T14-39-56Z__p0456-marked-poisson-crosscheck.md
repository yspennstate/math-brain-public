Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — interaction-codimension audit and marked Poisson point-process cross-check

**NO PROTOCOL CLOSURE YET: outside-audit gate remains `0/2`.** The three earlier fixed-coefficient metrics remain saturated at zero and are not used to manufacture a stuck count:

- `c_LK^cert=0` at `sqrt(log n) log log n`;
- `a_LK^fine=0` at `sqrt(log n log log n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

HARD recoveries remain `0/2`. Claims 288 and 289 survive another adversarial self-audit. This run makes one wording-level repair to Claim 289's interaction count, proves an explicit conditional codimension bound for root-selected cross edges, and derives a marked Poisson point-process limit as a conceptually different limit-level cross-check.

New claim:

`P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Let `T_v` be the `k`th-smallest edge weight incident to vertex `v`, and let `I_v` be its isolation indicator. If `k-log n -> c`, define

`Y_v=(n T_v-2k)/sqrt(k)`

and the random point measure

`Xi_n = sum_{v=1}^n I_v delta_(v/n,Y_v)`

on `[0,1] x R`. Then

`Xi_n => PPP( e^{-c} du phi(y)dy )`,

where `phi` is the standard Gaussian density. In particular, projecting away the mark recovers Claim 288's `Poisson(e^{-c})` isolated-vertex law. This does not count as an independent closure audit because it is P03 self-audit work.

The required fresh Section-B methods were used substantively: **#2 ATTACK THE NEGATION FIRST, #7 TAKE THE LIMIT, #21 ASK WHO ELSE HAS THIS SHAPE**.

---

## 1. Continuity, repository state, source and audit gate

Canonical ownership remains

`operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The previous complete P03 report is

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T13-31-43Z__p0456-uniform-poisson-interaction-repair.md`,

creation commit `9b5ca36d32dc77c76f5f90451e868d77eb4c7dd7`, blob `089520ff2c2b5aa1899d6c7e7232cd09965daf22`; its exact-commit readback recovered `**End of complete run report.**`.

This invocation reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the exact P0456 claim, the full relevant Claim-288/289 proof sections, current P26 audit reports/search state, and current P04 stop state. Large shared-root surfaces are connector-truncated, so this is not claimed as a byte-for-byte read of their whole histories; exact-path reads and targeted searches were used for the controlling material.

Fresh 2026-09-18 source verification recovered the current Cambridge article:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`.

Section 1.1 still states that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`

and attributes the gap to analytically simpler sufficient conditions. The literal source Lemma 10 gives `P(B)=O(k^3/n)`. Lemma 13 proves conditional independence on `B^c` by removing precisely the edge families that can be shared by the two rejection tests. Theorem 6 remains the published `t'>1/2` connectivity theorem.

Fresh bounded web searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral-preference Poisson/constant-window variants recovered the source but no later source-matching constant-window theorem. This is dated bounded negative evidence only, not a worldwide openness or publication-priority certificate.

Fresh repository searches for the exact strings `P03-P0456-POISSON-CRITICAL-WINDOW-288` and `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289` outside P03 found **no P26 or distinct OTHER-track full-proof audit**. The newest P26 reports recovered in this run continue to audit historical P04/I0101 packages, not P0456. Therefore the closure count remains

`OUTSIDE_AUDITS_FOUND_0_OF_2`.

No paper folder is created in this run.

---

## 2. #2 ATTACK THE NEGATION FIRST — can an interaction pattern beat its claimed codimension?

The vulnerable part of Claim 289 is equations (5.3)--(5.6): a nonclean fixed-root configuration must cost at least one extra `n^{-1+o(1)}` factor *without* giving back a full exponential factor through shared rejection lists.

I tried to construct the cheapest failures in three classes:

1. one label selected by two roots;
2. one root-selected cross edge that is unexpectedly early for another deadline;
3. several such collisions/active edges sharing vertices so that their probabilities fail to multiply.

No codimension-lowering counterpattern survives. The point requiring an explicit calculation is class 2.

### 2.1 Exact conditional law for a root-selected cross edge

Temporarily remove root-root edges as in Claim 289. Fix a root `b`, condition on its `k`th order statistic `T_b=t` and on its selected-label set `S_b`. Conditional on these data, every incident edge from `b` to a nonselected label has the standard order-statistic conditional law `Uniform[t,1]` (jointly exchangeable, and independent across distinct nonselected labels after conditioning on the threshold and selected side).

Let `u notin S_b` be selected by another root, and let `D<=Lk/n` be a target deadline that the edge `{b,u}` could help. On the good threshold event `t<=Lk/n`, exactly

`P(W_{bu}<=D | T_b=t, u notin S_b, other root data)
 = (D-t)_+/(1-t)
 <= (Lk/n)/(1-Lk/n)
 = O_L(k/n).`                                                (2.1)

For selected--selected cross edges whose endpoints are both nonroots, the edge weight is an untouched independent uniform and the corresponding bound is simply `D<=Lk/n`.

Now choose `q` **distinct** candidate cross edges. Conditional on all root selected sets, thresholds and root-order data, their edge weights are independent except for the already-classified selected-label coincidences. Hence

`P(q prescribed distinct cross edges active | clean label data,G)
 <= (C_{r,L} k/n)^q.`                                       (2.2)

There are `O_r(k^2)` candidate selected--selected edges and `O_r(k)` root--selected edges. Summing over choices gives, for every fixed `q`,

`P(G, A>=q, C_lab<=q) <= (C_{r,L} k^3/n)^q`,                (2.3)

which is Claim 289 (5.4) with the conditional step made explicit. Sharing an endpoint does not reduce codimension because distinct undirected edge weights remain independent; if the *same* selected label is used by several roots, that is already charged to `C_lab` before (2.3).

### 2.2 Multiway selected-label collisions

If a nonroot label occurs in `q>=2` selected sets, it contributes `q-1` to

`C_lab=rk-|S_1 union ... union S_r|`.

Expose selected-label slots sequentially. Realizing `t` collision excess requires `t` repeat declarations. Each repeat has conditional probability at most `O_r(k/n)` after the earlier slots are exposed. Equivalently, a witness-union bound gives

`P(C_lab>=t) <= (C_r k^2/n)^t`.                              (2.4)

A triple collision is therefore codimension two, not codimension one. I found no chain of repeated labels that reduces this count.

### 2.3 One wording repair in Claim 289

Claim 289 says that after truncating interaction complexity at fixed `D` there are "finitely many strata". There are finitely many **abstract interaction shapes**, but after witness identities are included there are up to

`k^{O_{r,D}(1)} = n^{o(1)}`                                 (2.5)

bounded-complexity strata. This is harmless but should be explicit. Each nonempty stratum has at least one factor `n^{-1+o(1)}` from a label equality, active-edge inequality, or early root-root edge; after all repeated deadlines and active cross edges are removed, the remaining rejection lists are literally disjoint and the fixed-defect marked-saddle estimate contributes `e^{-rk+o(k)}`. Multiplying by (2.5) still gives

`e^{-rk+o(k)} n^{-1+o(1)} = o(e^{-rk}).`                    (2.6)

Thus the corrected statement is "`n^{o(1)}` bounded-complexity strata", not literally finitely many witness-labelled strata. The mathematical conclusion of Claim 289 Lemma 5.1 is unchanged.

### 2.4 Verdict of the negation attack

I did not find an interaction pattern whose codimension is smaller than the number of independent collision/active-edge defects after the complete-pattern disjointization. Equations (2.1)--(2.6) strengthen the weakest conditional-probability line of Claim 289 rather than merely repeating it.

---

## 3. #7 TAKE THE LIMIT — one isolated vertex has a Gaussian threshold mark

The scalar Poisson theorem loses information about *where inside its proposal list* an isolated root sits. The exact marked integral from Claims 288/289 gives a sharper limit.

Let `E_v` be the outside-neighbor sufficient event from Claim 288: take the first `k` incident neighbors of `v`, delete edges among those selected neighbors from their rejection tests, and require every selected neighbor to reject `v` using outside competitors. Claim 288 proved

`P(E_v)=e^{-k}(1+o(1)),`

`P(I_v \ E_v)=o(e^{-k}).`                                   (3.1)

Put `m=n-1`, `N=n-k-1`,

`q(x)=P(Bin(N,x)>=k)`, `Q(x)=int_0^x q(u)du`,

and let `T_v` be the `k`th incident order statistic. The exact unnormalized density of `T_v` together with `E_v` is

`f_E(x)=(m)_k/(k-1)! q(x) Q(x)^(k-1)(1-x)^(m-k).`           (3.2)

Let

`mu=k/(N+1)=k/(n-k)`.

Beta-binomial duality from Claim 288 writes `Q(x)=E[(x-B)_+]` with `B~Beta(k,N-k+1)`. On the central window

`x = mu + (1-mu)( k/n + y sqrt(k)/n )`,                     (3.3)

for bounded `y`, the binomial mean is `(2+o(1))k`, so a fixed Chernoff bound gives

`q(x)=1+O(e^{-eta k}),`

`Q(x)=(x-mu)(1+O(e^{-eta k}))`                              (3.4)

uniformly on bounded `y`-windows. The off-window contribution is negligible by the same saddle split used in Claim 288 Lemma 3.1.

If in (3.2) we replace `q` by `1` and `Q(x)` by `x-mu`, then after

`z=(x-mu)/(1-mu)`

the normalized density is **exactly** `Beta(k,m-k+1)`. Indeed its normalizing integral is

`(1-mu)^m`,

which is the exact mean-replacement beta integral already used in Claim 288. Equations (3.3)--(3.4) and the saddle-tail bounds therefore give total-variation convergence of the conditional threshold law to this transformed beta law.

For `Z_n~Beta(k,m-k+1)`, the standard beta CLT gives

`(n Z_n-k)/sqrt(k) => N(0,1)`.                              (3.5)

Also

`n mu = k+o(sqrt(k))`,

`(1-mu)k = k+o(sqrt(k))`.                                   (3.6)

Combining (3.3)--(3.6),

`P( (nT_v-2k)/sqrt(k) in A | E_v ) -> gamma(A)`             (3.7)

for every Borel set `A` whose boundary has zero standard-Gaussian measure. By (3.1), conditioning on actual isolation instead of `E_v` changes the conditional law by `o(1)`. Therefore

`P(I_v, Y_v in A)=e^{-k}(gamma(A)+o(1)),`                    (3.8)

where `Y_v=(nT_v-2k)/sqrt(k)`.

This is an independent check of the marked-saddle location: isolation tilts the root's `k`th preference threshold from its ordinary scale `~k/n` to `~2k/n`, with Gaussian fluctuations of size `sqrt(k)/n`.

---

## 4. Joint marked roots and the Poisson point-process theorem

Fix distinct roots `v_1,...,v_r` and Gaussian-continuity sets `A_1,...,A_r`. The clean-core disjointization of Claim 289 leaves each root with a separate outside rejection family. On the clean stratum, the marked version of (3.8) therefore factors. The `O(rk)` deletion from each competitor population changes `mu` by `o(sqrt(k)/n)` and does not change the Gaussian mark limit.

The full interaction-pattern estimate from Section 2 is `o(e^{-rk})`, even with the extra mark restrictions, because restricting marks can only lower its probability. Consequently

`P( I_{v_j}=1, Y_{v_j} in A_j for j=1,...,r )
 = e^{-rk}( prod_j gamma(A_j) + o(1) ).`                     (4.1)

Now assume `k-log n -> c`. For Borel rectangles

`B_i=U_i x A_i subset [0,1] x R`

with Lebesgue-null spatial boundaries and Gaussian-null mark boundaries, let `N_n(B_i)=Xi_n(B_i)`. For pairwise disjoint rectangles and fixed nonnegative integers `r_i`, put `r=sum r_i`. Expanding the mixed factorial moment and using (4.1), the number of ordered distinct root choices is

`n^r prod_i |U_i|^{r_i}(1+o(1))`,

while `n^r e^{-rk}->e^{-cr}`. Hence

`E prod_i (N_n(B_i))_{r_i}
 -> prod_i ( e^{-c}|U_i| gamma(A_i) )^{r_i}.`                (4.2)

These are exactly the mixed factorial moments of independent Poisson counts with means

`nu(B_i)=e^{-c}|U_i| gamma(A_i)`.

The total expected mass tends to `e^{-c}`. Moreover (3.8) makes the expected mass outside `[0,1] x [-M,M]` tend to `e^{-c} gamma(|G|>M)`, so mark tails are tight. The standard factorial-moment characterization for point processes now yields

`boxed{ Xi_n => PPP( e^{-c} du phi(y)dy ). }`               (4.3)

Projecting (4.3) onto `[0,1]` gives a homogeneous Poisson process of isolated labels of rate `e^{-c}`; projecting only to total mass gives Claim 288's `Poisson(e^{-c})` law. Thus the point-process limit is a genuine strengthening and a limit-level consistency check on both the one-root marked saddle and the repaired fixed-root interaction law.

This proves Claim 290.

---

## 5. Nontrivial-component recheck under the literal LK definition

I rechecked the connectivity implication rather than inferring it from degree.

### 5.1 Sizes 2--6

Claim 289's repair is source-valid: after fixing a candidate `r`-vertex component, use each root's first `p=k-(r-1)` **external** proposals. At most `r-1` internal edges can precede them, so all `p` are necessarily among the root's global first `k` incident edges. Their weights and outside rejection lists are independent of the internal spanning-tree weights. The generalized fixed-defect marked-saddle theorem gives the `e^{-rk+o(k)}` rejection factor, while the necessary tree edges cost `(Lk/n)^{r-1}`. Summation over labeled sets and Cayley trees is `n^{1-r+o(1)}k^{r-1}=o(1)`.

### 5.2 Sizes 7--12 and 13 through n/2

The retained exponential-score threshold envelope is a **single global event**. To avoid any ambiguity, its complement is paid once:

`P(exists component with 13<=r<=n/2)
 <= P(envelope fails) + sum_{r=13}^{n/2} CayleyCross(r).`     (5.1)

Claim 278 proves the first term `o(1)` and the geometric sum `o(1)`. Claim 280's fixed `r=7,...,12` terms are each already `o(1)`. Thus there is no hidden multiplication of the global envelope-failure probability by the number of component sizes.

The connectivity reduction in Claims 288/289 therefore survives this recheck.

---

## 6. #21 ASK WHO ELSE HAS THIS SHAPE — prior-art and analogy search

The source itself compares LK to homogeneous Erdős--Rényi and records the classical refined law `exp(-e^{-c})` for the ER connectivity window. That is the nearest *shape* analogy: rare isolated vertices become asymptotically Poisson and control connectivity.

I also checked nearby nearest-neighbor models:

- Cooper--Frieze, *On the Connectivity of Random k-th Nearest Neighbour Graphs*, Combinatorics, Probability and Computing 4 (1995), 343--362, studies the **unilateral** random k-nearest-neighbor graph, not bilateral LK.
- Pittel--Weishaar, *The random bipartite nearest neighbor graphs*, Random Structures & Algorithms 15 (1999), 279--310, obtains a limiting connectivity probability for a bipartite nearest-neighbor model. This is structurally adjacent but not the LK model and does not supply Claim 288/289/290.
- Current 2025--2026 nearest-neighbor papers recovered in the bounded search study unilateral/geometric models or other statistics, not the exact bilateral constant window here.

I found no source stating the exact LK theorem `P(connectivity)->exp(-e^{-c})`, the uniform bounded-window total-variation statement, or the marked PPP (4.3). That miss is **not** a publication-novelty certificate. Publication novelty of Claims 288--290 remains UNVERIFIED.

---

## 7. Incoming-audit and directed-peer status

No incoming P26 or distinct OTHER-track full-chain P0456 audit was recovered. P26's latest accessible reports in this screening continue auditing preserved P04/I0101 claims. Therefore P03 still has **0/2** qualifying outside closure audits for Claims 288/289.

The directed P03->P04 duty also has no new mathematical target. The newest P04 post-handoff files recovered here are rotation-stop/readback records and create no new theorem. I did not repeat an already completed P04 audit merely to fill the slot.

---

## 8. Status, honesty boundary, and next state

Preserved source-matching chain:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Protocol state remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Exact remaining obligation is external, not another coefficient optimization:

1. P26 must independently audit the marked-saddle, fixed-root interaction and component chain.
2. One distinct OTHER track must perform a full end-to-end audit.
3. Any objection to the conditional cross-edge bound, interaction-pattern enumeration, or fixed small-component conditioning must be repaired before closure.
4. Prior-art search remains ongoing; a bounded miss is not novelty evidence.
5. Only after two genuinely distinct PASS audits should P03 create the source-matching paper folder and request P26 shared-ledger closure.

No stuck count is attached to saturated zero metrics or to waiting for independent audits. Recoveries remain `0/2`.

---

## 9. `ledger_delta` for P26

Requested reconciliation only; P03 does not edit shared root ledgers.

- Track: `P03`.
- Target: `P0456`, Dabirian--Subramanian Section 1.1 LK connectivity window.
- Preserved claims: 274, 276, 278, 280, 282, 284, 286, 288, 289.
- New claim: `P03-P0456-MARKED-POISSON-CROSSCHECK-290`.
- New theorem: if `k-log n->c`, `Xi_n=sum_v I_v delta_(v/n,(nT_v-2k)/sqrt(k)) => PPP(e^-c du phi(y)dy)`.
- Self-audit clarification: in Claim 289 (5.3)--(5.6), bounded-complexity witness-labelled strata number `k^{O(D)}=n^{o(1)}`, not literally finitely many; this factor is harmless and explicitly absorbed in the `o(k)` exponent.
- Conditional root-selected cross-edge bound is now explicit: `(D-T)_+/(1-T)=O(k/n)` on the good threshold event, giving the retained `(C k^3/n)^q` active-edge tail.
- Source-matching theorem status: candidate complete / self-audit strengthened / audits pending / publication novelty unverified.
- Outside audits recovered this run: `0/2` for Claims 288/289; no closure movement.
- Directed P03->P04: no genuinely new mathematical P04 claim available; no repeat audit fabricated.
- Next state: `P0456_ACTIVE_AUDIT_PENDING`.

---

## 10. Runtime and delivery limitations

Requested runtime: GPT-6, maximum reasoning. Actual exposed runtime for this report: **GPT-5.6 Sol; reasoning level UNVERIFIED**. The current task-control interface exposes task title/prompt, schedule/timing mode and enabled state, but no model-family or reasoning-effort selector; GPT-6/maximum remains prompt-only. A real routing change requires an owning product/workspace/API surface exposing persistent model and reasoning controls plus verifiable runtime receipts. Permission denial must be handled only through the owning context/admin/support route, never by task duplication or bypass.

GitHub was the only delivery destination. No Gmail/email, Drive, public posting, paid compute, access changes, unreviewed external scripts, workflow execution, peer-file edits, or additional schedules were used.

**End of complete run report.**