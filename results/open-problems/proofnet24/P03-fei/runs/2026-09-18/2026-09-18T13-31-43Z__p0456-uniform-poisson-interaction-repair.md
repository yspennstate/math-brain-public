Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — adversarial interaction repair and uniform Poisson window

**CLAIM 288 SURVIVES SELF-AUDIT, WITH ITS WEAKEST DEPENDENCY STEP REPLACED BY AN EXPLICIT FINITE-INTERACTION ARGUMENT.** The three previously admitted fixed-coefficient metrics remain saturated at zero and are not used to manufacture a stuck count:

- `c_LK^cert=0` at `sqrt(log n) log log n`;
- `a_LK^fine=0` at `sqrt(log n log log n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

HARD recoveries remain `0/2`. The live object is the source-matching constant window. This run strengthens Claim 288 uniformly on bounded offsets and repairs the two points that were explicitly marked for adversarial audit: fixed-root decoupling and fixed small components.

New claim:

`P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed `C<infinity`, uniformly over integers `k` with

`|k-log n|<=C`,

put

`lambda_n=n exp(-k)`

and let `Z_n` be the number of isolated vertices of `LK(n,k)`. Then

`d_TV(Law(Z_n),Poisson(lambda_n)) -> 0`,

and

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.

In particular, whenever `k-log n->c`, Claim 288 follows:

`Z_n => Poisson(e^-c)`,

`P(connectivity)->exp(-e^-c)`.

This remains **candidate complete / audits pending**, not protocol-closed. Fresh repository screening in this run found no P26 audit of Claim 288/289 and no distinct OTHER-track full-proof audit of it. Self-audit does not count toward either required outside audit.

The three required Section-B moves used substantively were **#14 EXACT FINITE REDUCTION, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS**.

---

## 1. Continuity, source, repository, and audit status

Canonical ownership remains

`operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The previous complete report is

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T12-31-09Z__p0456-poisson-critical-window.md`,

creation commit `6d5f33f04f9dfc043ece8fe6f1940635b130fd71`, blob `4a912b3cffb5d0209fbb39058e8e060110a2cf82`. Exact-commit readback there recovered `**End of complete run report.**`.

This run reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the exact P0456 claim, the full relevant sections of Claim 288, current P26/P04 search state, and the newest P04 administrative stop. Large shared-root surfaces are connector-truncated, so I do not claim byte-for-byte rereads of their entire histories; exact-path reads and scoped searches were used for the controlling material.

Fresh source verification on 2026-09-18 recovered the current Cambridge article:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579; published online 18 December 2025; DOI `10.1017/jpr.2025.10051`.

Its Section 1.1 still states that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`

and explicitly says the gap may arise from analytically simpler sufficient conditions. Its Lemma 10 gives `P(B)=O(k^3/n)`, and Lemma 13 proves conditional independence of the two isolation events on `B^c` by deleting precisely the edge sets that could be common to the two rejection tests.

Fresh bounded searches for the exact title/authors/DOI, `LK(n,k) Poisson isolated vertices`, and `LK(n,k) log n+c connectivity` recovered the Cambridge paper but no later constant-window / Poisson isolated-vertex theorem. This is dated bounded negative evidence only, not a worldwide openness or publication-priority certificate.

A fresh repository search likewise found no incoming P26 or distinct OTHER-track audit of Claim 288. Recent P26 runs found in this check audit P04/I0101 claims rather than P0456. Thus Claim 288/289 still has **0/2 independent OTHER-track closure audits found by P03**.

The newest P04 invocation after its I0101 handoff is explicitly administrative and creates no mathematical claim. Therefore the directed P03->P04 duty has no genuinely new claim to audit here; I do not repeat an old audit merely to fill the slot.

---

## 2. #20 — the actual gap in the old Lemma 5.1 argument

The previous Claim-288 proof correctly identified all *types* of interaction among finitely many roots, but its upper-bound sentence

> condition on one first witness and delete every other cross-block edge

was too compressed to justify the multiplicative asymptotic. A configuration can have several selected-label collisions and several active cross edges. Conditioning only a single witness does not by itself show that every remaining shared rejection list has disappeared, and a shared selected label couples two roots through the same outside edge list.

This is a genuine proof-presentation gap in the weakest part of Claim 288. It does **not** produce a counterexample. The repair is to stratify by the *entire finite interaction pattern* up to a fixed complexity and prove that large-complexity patterns are already negligible on the `e^{-rk}` scale.

The same diagnosis applies to the old size-`2,...,6` component paragraph: conditioning on a spanning tree and then immediately multiplying rejection costs can conceal dependence of the roots' preferred sets on the internal tree edges. The repair below uses the first `k-(r-1)` **external** proposals, whose definition is independent of all internal tree weights.

---

## 3. Generalized fixed-defect marked-saddle lemma

We first record the exact extension of Claim 288 Lemma 3.1 needed below.

### Lemma 3.1 (fixed proposal/threshold defects)

Fix integers `a,b`. Let

`p=k-a`, `h=k-b`,

with `p,h>=1`, and let `m=n+O(1)`, `N=n+O(k)`, `k->infinity`, `k=O(log n)`. Define

`q_h(x)=P(Bin(N,x)>=h)`,

`Q_h(x)=int_0^x q_h(u) du`.

Let `M_{p,h}(m,N)` be the probability that the first `p` points, in increasing order, among `m` iid Uniform[0,1] points are all independently marked, where a point at `x` is marked with probability `q_h(x)`. Then

`M_{p,h}(m,N)=e^{-h}(1+o(1))`,

uniformly when `a,b` range over any fixed finite set and, in particular, uniformly for `|k-log n|<=C` with fixed `C`.

#### Proof

Exactly as in Claim 288, rank integration gives

`M_{p,h}=(m)_p/(p-1)! int_0^1 q_h(x) Q_h(x)^(p-1) (1-x)^(m-p) dx`.

Using `d(Q_h^p)=p q_h Q_h^(p-1) dx` and integrating by parts,

`M_{p,h}=(m)_{p+1}/p! int_0^1 Q_h(x)^p (1-x)^(m-p-1) dx`.      (3.1)

Let

`B_h~Beta(h,N-h+1)`, `mu=h/(N+1)`.

Beta-binomial duality gives

`Q_h(x)=E[(x-B_h)_+]`,

and `Var(B_h)=O(k/n^2)`. Replacing `B_h` by its mean in (3.1) gives the exact beta integral

`(m)_{p+1}/p! int_mu^1 (x-mu)^p (1-x)^(m-p-1) dx=(1-mu)^m`.   (3.2)

The saddle of the mean integrand lies at

`x=mu + (p/m)(1-mu)=(h+p+o(k))/n=(2+o(1))k/n`,

whereas `B_h` fluctuates only on scale `sqrt(k)/n`. Split at `mu+k/(2N)`. On the upper region the beta upper tail is `exp(-Omega(k))`, hence

`Q_h(x)^p=(x-mu)^p(1+o(1))`

uniformly. On the lower region the normalized log integrand loses `Omega(k)` relative to the saddle; in the `O(sqrt(k)/n)` neighborhood of `mu`, the factor `Q_h(x)^p` is at most `k^{-p/2+O(p)}`. These estimates are unchanged by fixed `a,b`. Thus

`M_{p,h}=(1-mu)^m(1+o(1))`.

Finally

`m log(1-h/(N+1))=-h+O(k^2/n)=-h+o(1)`.

This proves the lemma. `square`

The point of allowing `h>p` by a fixed amount is that the component proof below uses `p=k-(r-1)` external proposals but each must still be rejected by `k` lighter competitors at the other endpoint.

---

## 4. #14 — exact finite two-root clean-core reduction

Remove the root-root edge `{v_1,v_2}` temporarily when forming the roots' preference orders. Among the `N=n-2` nonroot labels let `S_1,S_2` be the first `k` labels of the two roots. Rank-label symmetry makes them independent uniform `k`-subsets of `[N]`, independent of their numerical order statistics.

Set `J=|S_1 cap S_2|`. Then, **exactly**,

`P(J=j)=binom(k,j) binom(N-k,k-j) / binom(N,k)`,              (4.1)

`0<=j<=k`.

In particular

`P(J=0)=binom(N-k,k)/binom(N,k)=1-O(k^2/n)`.                 (4.2)

Conditional on `J=0`, put

`U={v_1,v_2} union S_1 union S_2`.

For each selected neighbor retain only edges to `V\U`. There are

`N_0=n-2-2k`

retained competitors per selected neighbor. These edge lists are pairwise disjoint over all `2k` selected neighbors. Therefore the exact disjointized clean-core probability is

`P(J=0) M_{k,k}(n-2,N_0)^2`.                                (4.3)

By Lemma 3.1 this is

`e^{-2k}(1+o(1))`.                                          (4.4)

Adding back the root-root edge changes the lower clean event only if it falls below one of the two kth root thresholds; on the usual `O(k/n)` threshold event this costs `O(k/n)=o(1)`. Formula (4.1)--(4.3) is the finite reduction that was missing from the old prose proof: the main `e^{-2k}` term is an exact hypergeometric factor times two exact one-root marked integrals.

The same clean-core reduction extends to fixed `r`. If the root-root edges are temporarily removed, then

`P(S_1,...,S_r pairwise disjoint)
 = product_{a=0}^{r-1} binom(N-a k,k)/binom(N,k)
 =1-O_r(k^2/n)`.                                             (4.5)

On that event, retaining only edges from selected neighbors to the complement of all roots and all selected labels leaves pairwise disjoint rejection lists and yields `M_{k,k}(n-r,n-r-rk)^r=e^{-rk}(1+o(1))`.

---

## 5. Full interaction-pattern repair for fixed factorial moments

### Lemma 5.1 (repaired fixed-root decoupling)

For every fixed integer `r>=1`, uniformly for `|k-log n|<=C`,

`P(I_{v_1}...I_{v_r})=e^{-rk}(1+o_C(1))`                    (5.1)

for any fixed distinct roots `v_1,...,v_r`.

#### Proof

Temporarily remove all root-root edges and let `S_a` be the first `k` nonroot labels at root `v_a`. Choose a constant `L=L(r)` with

`L-1-log L>r+3`

and let `G` be the event that every root kth threshold is at most `Lk/n`. Standard binomial/order-statistic Chernoff bounds give

`P(G^c)=o(e^{-rk})`.                                         (5.2)

We quantify the ways the clean blocks can fail to be disjoint.

**Label collision complexity.** Put

`C_lab=rk-|S_1 union ... union S_r|`.

For every fixed `t`,

`P(C_lab>=t)<= (C_r k^2/n)^t`.                               (5.3)

Indeed, expose the `rk` labeled slots sequentially. Collision excess at least `t` requires at least `t` declarations that a new slot repeats a previously exposed label. There are at most `(rk)^{2t}` choices of the repeated-slot/previous-slot witnesses and each prescribed equality contributes a factor at most `(n-r-O(k))^{-1}`. This union bound also handles triple and higher coincidences correctly because a label appearing `q` times contributes `q-1` to `C_lab`.

**Active cross-edge complexity.** Assume first that collided selected labels have been marked for deletion. An edge with at least one endpoint among the remaining selected labels and its other endpoint in

`U={v_1,...,v_r} union S_1 union ... union S_r`

is called active if it lies below a target deadline to which it could contribute a competitor. On `G`, every such deadline is at most `Lk/n`. There are `O_r(k^2)` candidate selected-selected edges and `O_r(k)` root-selected candidates. Conditional on the root rank labels and numerical thresholds, distinct selected-selected edge weights are independent uniforms, and nonselected root-selected weights are stochastically no more likely than `O_r(k/n)` to lie below another root's deadline. Consequently, for every fixed `t`, if `A` is the number of distinct active cross edges,

`P(G, A>=t, C_lab<=t)<= (C_{r,L} k^3/n)^t`.                 (5.4)

One may see (5.4) directly by choosing `t` distinct candidate edges and requiring each to fall into an interval of length at most `Lk/n`; conditioning a nonselected root incident edge to exceed that root's own kth threshold only reduces, up to the harmless factor `(1-Lk/n)^{-1}`, the chance that it lies below another `O(k/n)` deadline.

Root-root edges are only `binom(r,2)` in number. The event that a specified one falls below a root kth threshold has probability `O_r(k/n)` on `G`; any such occurrence is recorded as an additional fixed interaction defect.

Choose a fixed integer `D>2r+4`. By (5.3)--(5.4), configurations with either `C_lab>D` or `A>D` have probability `o(e^{-rk})`: each costs at least `n^{-D+o(1)}`, while `e^{-rk}=n^{-r+o(1)}` in the bounded-offset window. Thus it remains to handle the finitely many strata with

`C_lab<=D`, `A<=D`,

and a fixed root-root interaction pattern.

Fix one such **complete interaction pattern**. For every repeated selected label, drop from the rejection test every deadline using all but one occurrence of that label. For every active cross edge, either delete the edge and lower the affected competitor threshold by one, or, equivalently for an upper bound, omit the at most two deadlines it can help. Root-root interactions alter only `O_r(1)` proposal ranks. Because `r,D` are fixed, each root loses or shifts only `O_{r,D}(1)` deadlines/competitors.

After these deletions, all remaining selected labels are distinct and every remaining rejection list uses only edges to `V\U`. Hence the remaining outside edge lists are pairwise disjoint across all roots. Lemma 3.1, or equivalently the fixed-defect ordered-deadline form retained from Claim 286, gives for each root

`P(all remaining rejection constraints | fixed pattern)
 <= exp(-k+o(k))`,                                           (5.5)

uniformly over the finitely many fixed defects. The factors multiply after disjointization.

If the interaction pattern is nonempty, at least one independent label coincidence, active-edge inequality, or root-root early-edge inequality was prescribed. Its pattern probability carries a factor `n^{-1+o(1)}`; further interaction constraints can only reduce it. Therefore summing all bounded-complexity nonempty strata gives

`P(I_{v_1}...I_{v_r}, interaction)
 <= e^{-rk+o(k)} n^{-1+o(1)}
 =o(e^{-rk}).                                                (5.6)

On the zero-interaction stratum, actual isolation forces the clean disjointized events, so by (4.5)

`P(I_{v_1}...I_{v_r}, no interaction)<=e^{-rk}(1+o(1))`.    (5.7)

For the matching lower bound, impose pairwise disjoint selected sets and require every selected neighbor to have `k` competitors in `V\U` below its target. Those retained lists are disjoint and Lemma 3.1 gives `e^{-rk}(1+o(1))`; adding back the finitely many root-root edges spoils the event with probability only `O_r(k/n)=o(1)`. Therefore

`P(I_{v_1}...I_{v_r})>=e^{-rk}(1-o(1))`.                    (5.8)

Combining (5.2), (5.6)--(5.8) proves (5.1). `square`

### Why this repairs the old proof rather than renaming the gap

The old proof classified the right interaction *types* but conditioned on only one witness. The repaired proof controls the complete pattern: large collision/active-edge complexity is negligible even before imposing isolation; bounded complexity is absorbed as a fixed number of omitted deadlines/competitor shifts, after which the outside lists are literally disjoint. A shared selected label is never allowed to remain in two product factors: all but one of its deadlines are explicitly removed before multiplication.

---

## 6. #20 — repairing fixed component sizes `2,...,6`

The old component proof conditioned on a spanning tree and then invoked a product rejection cost. To prevent the tree weights from biasing the proposal sets, define proposals using **external edges only**.

Fix a labeled vertex set `S` with `|S|=r`, `2<=r<=6`, and a spanning tree `T` on `S`. Choose `L` with `L-1-log L>2`. With probability `1-o(1)` simultaneously for all vertices, every kth incident order statistic is at most `Lk/n`.

If `S` is a connected component and contains `T`, every tree edge is bilaterally preferred, hence necessarily has weight at most `Lk/n`. The `r-1` tree-edge weights are distinct independent uniforms, so

`P(all tree edges <=Lk/n)<=(Lk/n)^(r-1)`.                   (6.1)

Now ignore **all internal edges of `S`** when ordering proposals from a vertex `v in S`. Let

`p=k-(r-1)`.

The first `p` external incident edges of `v` must lie among its first `k` incident edges in the full graph, because at most `r-1` internal edges can precede them. If `S` is a component, each of these `p` external proposals must therefore be rejected by its outside endpoint, and that endpoint must have at least `k` other lighter incident edges.

Crucially, the first `p` external root edges and the outside rejection lists are independent of all internal tree weights. Thus (6.1) can be separated from the rejection calculation without conditioning bias.

For one root, the rejection probability is exactly the generalized marked event `M_{p,k}` with only `O_r(1)` changes in `m,N`; by Lemma 3.1,

`M_{p,k}=e^{-k}(1+o(1))`.                                   (6.2)

For the `r` roots together, apply the repaired interaction-pattern argument of Lemma 5.1 to their first `p` external selected sets. Pairwise label collisions and active cross edges are still `n^{-1+o(1)}` corrections, while the clean lists are disjoint. Hence

`P(all r external proposal blocks rejected)=e^{-rk+o(k)}`.   (6.3)

Therefore, for fixed `S,T`,

`P(S is a component containing T)
 <=(Lk/n)^(r-1) e^{-rk+o(k)}+o(n^{-2r})`.                    (6.4)

There are at most `binom(n,r) r^(r-2)` choices of `S,T`. Since `k=log n+O(1)`, summing (6.4) gives

`P(exists r-component)
 <= n^{1-r+o(1)} k^(r-1)->0`                                (6.5)

uniformly for bounded offsets and every fixed `2<=r<=6`.

This removes the conditioning defect in the old paragraph. Sizes `7,...,12` remain covered by Claim 280's exact exponential-score/Cayley crossing bound, and Claim 278's uniform component envelope handles `13<=r<=n/2`. Thus

`sup_{|k-log n|<=C} P(exists nontrivial component of size <=n/2)->0`. (6.6)

---

## 7. #27 — uniform Poisson theorem on every bounded offset window

The marked-saddle proof and Lemma 5.1 are uniform for `|k-log n|<=C`. Hence for every fixed integer `r>=1`,

`sup_{|k-log n|<=C} | P(I_1...I_r)/e^{-rk} -1 | ->0`.        (7.1)

Let

`lambda_n=n e^{-k}`.

Then uniformly in the same window,

`E[(Z_n)_r]=lambda_n^r(1+o_C(1))`.                           (7.2)

Because `lambda_n in [e^{-C+o(1)},e^{C+o(1)}]`, this already implies a uniform total-variation Poisson approximation by a compactness argument.

Suppose otherwise. Then for some `epsilon>0` there is a sequence `n_j,k_j`, `|k_j-log n_j|<=C`, such that

`d_TV(Law(Z_{n_j}),Poisson(lambda_{n_j}))>=epsilon`.          (7.3)

Pass to a subsequence with `lambda_{n_j}->lambda in [e^{-C},e^C]`. Equation (7.2) gives convergence of every fixed factorial moment to `lambda^r`, hence of every ordinary moment to the corresponding Poisson moment. The Poisson law is moment-determinate, so

`Z_{n_j}=>Poisson(lambda)`.                                  (7.4)

For integer-valued variables, (7.4) gives convergence of each point mass (evaluate distribution functions at half-integers). Since both sides have total mass one, Scheffe's lemma on counting measure yields

`d_TV(Law(Z_{n_j}),Poisson(lambda))->0`.                     (7.5)

Also `Poisson(lambda_{n_j})->Poisson(lambda)` in total variation. The triangle inequality contradicts (7.3). Therefore

`boxed{ sup_{|k-log n|<=C} d_TV(Law(Z_n),Poisson(n e^-k))->0. }` (7.6)

By (6.6), disconnection differs from `{Z_n>0}` by `o_C(1)`. Consequently

`boxed{ P(LK(n,k) connected)=exp(-n e^-k)+o_C(1) }`         (7.7)

uniformly for `|k-log n|<=C`.

Taking `k-log n->c` recovers Claim 288 with `lambda=e^-c`.

---

## 8. Adversarial checks and remaining honesty boundary

### 8.1 Shared-label failure mode

This was the most concrete omitted dependency in the old prose: if one nonroot vertex belongs to two roots' preferred sets, its outside rejection list is literally shared. The repaired proof does not multiply through that shared list. It assigns a collision defect and deletes every repeated deadline except one; collision excess `t` costs `n^{-t+o(1)}`.

### 8.2 Multiple active cross edges

A single-witness argument is not enough when several cross edges help several deadlines. The repaired proof truncates the **total** active-edge complexity at fixed `D`; tail probability is `n^{-D+o(1)}`, and every bounded pattern is fully deleted before product factorization.

### 8.3 Tree-conditioning bias

The old small-component argument could be read as conditioning the roots' entire preference structure on the internal tree. The repaired proof uses the first `k-(r-1)` external proposals. These remain proposals whatever the internal tree weights are, and their edge families are independent of the tree.

### 8.4 What remains unaudited

This run is still a self-audit by P03. The marked-saddle lemma, interaction-complexity bounds, and component repair need independent full-proof checking. No P26 or distinct OTHER-track Claim-288/289 audit was found in the fresh repository check. Therefore neither Claim 288 nor Claim 289 is called protocol-closed, and no paper folder is created yet.

---

## 9. Directed P03 -> P04 audit duty

The newest P04 report recovered this run is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T12-46-33Z__rotation-stop-administrative.md`,

creation commit `b7a9428af44babeffdb81737b6a71b4b5c39a8e5`.

It explicitly says `ROTATION STOP / NO NEW RESEARCH RUN COUNTED` and creates no mathematical claim. Earlier P04 Claim 45 and older claims have already been P03-audited as recorded in the continuity prompt. Therefore no genuinely new P04 theorem is available for a new P03 audit, and I do not fabricate a repeat.

---

## 10. Status, obligations, and next state

Mathematical source target: **candidate complete after an explicit self-audit repair**, with the stronger uniform bounded-window law (7.6)--(7.7).

Protocol status remains

`P0456_ACTIVE_AUDIT_PENDING / CLAIM_288_289_SELF_REPAIRED / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Exact remaining obligations:

1. P26 independently audits the entire marked-saddle, interaction-pattern, factorial-moment, and component chain.
2. A distinct OTHER track performs an end-to-end proof audit; a self-check or second P26 pass does not count.
3. Any audit objection to (5.3)--(5.6), especially conditional probabilities for root-selected cross edges, must be repaired before closure.
4. Fresh prior-art checking must continue through authors/citations and specifically seek a Poisson/constant-window result for `LK(n,k)`.
5. Only after two independent PASS audits should P03 create the source-matching paper folder and request P26 shared-ledger closure.

No rotation occurs while this audit/repair obligation is active.

---

## 11. `ledger_delta` for P26

Requested reconciliation only; P03 does not edit shared root ledgers.

- Track: `P03`.
- Canonical target: `P0456`, Dabirian--Subramanian Section 1.1 connectivity window.
- Preserved candidate-complete claim: `P03-P0456-POISSON-CRITICAL-WINDOW-288`.
- New strengthening/repair: `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289`.
- Status: `PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Stronger theorem: for every fixed `C`, uniformly over integer `|k-log n|<=C`, with `lambda_n=n e^-k`, `d_TV(Law(Z_n),Poisson(lambda_n))->0` and `P(connectivity)=exp(-lambda_n)+o_C(1)`.
- Repair: replaces Claim-288 Lemma 5.1's single-witness prose by complete finite interaction-pattern truncation, and replaces the size-2--6 tree-conditioning step by external-proposal marked saddles.
- Coarser fixed-coefficient metrics remain saturated at zero; no stuck count is attached to saturation.
- Audits: fresh P03 search found `0/2` independent Claim-288/289 closure audits; P26 and one distinct OTHER-track audit remain required.
- Directed P03->P04 audit: no new P04 mathematical claim exists after its administrative rotation-stop report, so none was fabricated.
- Next state: `P0456_ACTIVE_AUDIT_PENDING`.

---

## 12. Model / tool limitations

Requested model: GPT-6, reasoning maximum. Actual exposed runtime for this report: **GPT-5.6 Sol; reasoning level UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The scheduler/task-control interface available to this track still exposes task title/prompt, schedule or relative start, timing mode, and enabled state, but no model-family selector, reasoning-effort selector, or authenticated applied-routing telemetry. A real routing change requires those persistent fields in the owning scheduler/workspace/API layer and verifiable runtime receipts. Permission denial must be handled through the owning context/admin/support path, never by task duplication or permission bypass.

GitHub was the only delivery destination. No Gmail/email, Drive, public posting, paid compute, access changes, unreviewed external scripts, workflow execution, or additional schedules were used.

**End of complete run report.**