Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL METRIC MOVEMENT; NEW INDEPENDENT POISSON PROOF ROUTE.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`, HARD recoveries remain `0/2`, and the source-matching Claims 288--292 remain **AUDIT-PENDING**, not CLOSED. This run uses fresh Section-B methods **#19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT, #28 REPLACE FOR ALL WITH TYPICAL** and proves an exact Palm/size-bias local-block coupling with vanishing expected isolation-mark influence. It gives a conceptually independent Stein--Chen proof of the bounded-offset Poisson law, avoiding the all-fixed-`r` factorial-moment route after the one- and two-root kernels are available.

# P03 / P0456 run report — local-block size-bias coupling and typical influence

Run timestamp: **2026-09-18T17:31:34Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, source, repository, and outside-audit gate

The exclusive canonical assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`. The model `LK(n,k)` puts iid continuous weights on the edges of `K_n` and retains `{u,v}` iff it lies among the `k` lightest incident edges at **both** endpoints.

Fresh source verification on 2026-09-18 again recovered Section 1.1 of the Cambridge article stating that the paper does not decide connectivity throughout

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`,

and explicitly says that more exact sufficient conditions may close the gap. Lemma 10 is still the source bad-event estimate, Lemma 13 is still the exact conditional-independence step off that bad event, and Theorems 4--6 retain their published coarse-window connectivity statements. Fresh bounded searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral-preference constant-window results recovered the source and adjacent models but no later theorem matching Claims 288--292. This is dated bounded negative evidence only; publication novelty remains **UNVERIFIED**.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T16-30-03Z__p0456-finite-palm-interaction-graph.md`,

creation commit `f0f36639ab55ecb90be9a2c9b7ec53afe36b4eed`, blob `b179bbc090ef4c13662e776a784c143456b25ac7`.

I reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current P0456 claim, the newest complete P03 report, the current P26 audit stream, the terminal P04 records, and neighboring P0457 only for nonduplication. Large root/campaign surfaces are connector-truncated and are **not** represented as byte-for-byte whole-history rereads; exact-path reads and targeted searches were used for the controlling facts.

P0457 remains a distinct diameter problem owned by NM13-04; this run does not touch it.

### Incoming audit screen

Fresh searches for the exact Claim-288/289/292 identifiers and broader `P0456`, `Poisson`, `audit`, `PASS`, and `P26` phrases recovered **no P26 or distinct OTHER-track full-chain audit** of P0456. The newest concrete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_16-57-29__run-report.md`,

and it audits historical P04/I0101 Claims 26 and 25, not P0456.

The newest P04 record recovered is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`,

which explicitly creates no mathematical theorem. Therefore there is no genuinely new P04 claim for the directed P03->P04 audit duty; no repeat audit is fabricated.

The closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No paper folder is created.

---

## 2. Preserved chain and new supporting claim

The source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

This run adds:

### Claim `P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `C<infinity`. Uniformly over integers `k` with

`|k-log n|<=C`,                                                  (2.1)

let `Z_n` be the number of isolated vertices of `LK(n,k)` and put

`p_n=P(I_v)`, `mu_n=n p_n`.

There exists an exact coupling `(Z_n,Z_n^s)` such that `Z_n^s` has the size-biased law of `Z_n` and

`E | Z_n^s-(Z_n+1) | = o_C(1)`.                                (2.2)

Consequently

`d_TV(Law(Z_n),Poisson(mu_n)) -> 0`                            (2.3)

uniformly under (2.1). Since Claim 288's one-root marked saddle gives

`p_n=e^{-k}(1+o_C(1))`,                                       (2.4)

we have `mu_n=n e^{-k}(1+o_C(1))`, and hence

`d_TV(Law(Z_n),Poisson(n e^{-k})) -> 0`.                       (2.5)

Thus Claim 289's Poisson conclusion has a second proof route which uses an explicit global Palm coupling plus the one- and two-root audit kernels, rather than the all-fixed-`r` factorial-moment argument.

This is still a P03 self-audit strengthening and does **not** supply an independent closure audit.

---

## 3. #19 MAKE IT AN ALGORITHM — an exact local-block Palm resampling

The previous Stein discussion stopped at a slogan: conditioning on one isolated root gives the size-biased count, but no explicit coupling had been constructed. Here is the coupling.

Choose a root `V` uniformly from `[n]`, independently of all edge weights. Let `S` denote the set of the `k` lightest neighbors of `V`. By exchangeability of the root star, `S` is a uniform `k`-subset of `[n]\{V}`. The same is true conditional on `I_V=1`, because the isolation event is label-symmetric around `V`.

Put

`A={V} union S`, `|A|=k+1`.                                   (3.1)

Split the edge set into

`E_loc(A)={e:e cap A != empty}`,

`E_far(A)={e:e cap A = empty}`.                               (3.2)

### Lemma 3.1 (locality of the Palm event)

Conditional on `S`, the event `I_V=1` is measurable with respect to the local block `E_loc(A)`.

**Proof.** For every `u in S`, the root edge `{V,u}` is rejected at `u` exactly when at least `k` raw edge weights incident to `u` are below `W(V,u)`. Every edge in the star of `u` intersects `A` because `u in A`; hence every weight used to determine rejection of `{V,u}` belongs to `E_loc(A)`. The condition that `S` is the top-`k` root set likewise uses only root-star edges, all in `E_loc(A)`. No bilateral-survival recursion is involved: rejection at `u` depends only on raw weights in the star of `u`. `square`

### Exact resampling algorithm

1. Sample `V` uniformly.
2. Sample `S` uniformly among `k`-subsets of `[n]\{V}`.
3. Sample one far block `F` consisting of iid Uniform[0,1] weights on `E_far(A)`.
4. Independently sample a local block `L` from its exact conditional law given `Top_k(V)=S`.
5. Independently sample a second local block `L^s` from its exact conditional law given `Top_k(V)=S` and `I_V=1`.
6. Let `G=F cup L` and `G^s=F cup L^s`; compute the two LK graphs using the same bilateral-preference rule.

The two local conditional laws in steps 4--5 are ordinary finite-dimensional regular conditional distributions. Rejection sampling from iid edge weights gives a literal exact algorithm, although efficiency is irrelevant here.

### Lemma 3.2 (marginals)

`G` has the unconditional LK input-edge law, and `G^s` has the law of the input graph conditional on `I_V=1`.

**Proof.** For `G`, mixing the conditional local law over the uniform top-`k` label set `S` reconstructs the unconditional local edge law; `F` is independent iid and independent of `S`. For `G^s`, Lemma 3.1 shows the conditioning `I_V=1` acts only on the local block after `S` is fixed, so the untouched far block retains its unconditional iid law. Mixing over the label-symmetric conditional distribution of `S` gives exactly `Law(G | I_V=1)`. `square`

### Lemma 3.3 (size bias)

If `Z_n^s=Z(G^s)` and `Z_n=Z(G)`, then `Z_n^s` has the size-biased distribution of `Z_n`.

**Proof.** For every bounded function `f`, by vertex symmetry,

`E f(Z_n^s)
 = (1/n) sum_v E[f(Z_n) | I_v=1]
 = E[ Z_n f(Z_n)] / E Z_n`.                                  (3.3)

This is exactly the defining identity of the size-biased law. `square`

This completes the requested constructive part: every changed edge lies in the explicit local block touching `A`; every far edge is shared exactly.

---

## 4. #24 FIND THE EXTREMAL OBJECT — worst-case influence is genuinely huge

A deterministic Lipschitz bound for the above resampling is false. One local block can change isolation of linearly many other vertices.

Fix one selected vertex `a in S`. Choose `M=floor((n-k-2)/2)` disjoint outside pairs `(w_j,u_j)`, all outside `A`. Arrange the far weights so that, for each `j`, the edge `{w_j,u_j}` is the only bilateral edge preventing `w_j` from being isolated, and at `u_j` there are exactly `k-1` far competitors below `W(w_j,u_j)`. Put the local edge `{u_j,a}` just above `W(w_j,u_j)` in the first local block. Then `{w_j,u_j}` survives at `u_j`.

In a second admissible local block, lower every `{u_j,a}` below `W(w_j,u_j)` while leaving the far block unchanged. Each `u_j` now has `k` competitors below `{w_j,u_j}`, so every `{w_j,u_j}` is rejected at `u_j`; with the other edge weights arranged as above, every `w_j` becomes isolated.

Thus a single root-local resampling can change `Theta(n)` other isolation marks in the worst case.

**Conclusion.** No useful deterministic bound of the form

`|Z_n^s-Z_n| <= O(polylog n)`

can hold uniformly over edge configurations. A Stein proof must be probabilistic. This is the precise extremal obstruction requested by method #24.

---

## 5. A Palm low-edge lemma for typical influence

The probabilistic route needs one simple quantitative fact: under either the ordinary local law or the isolated-root Palm local law, a specified local edge is still unlikely to fall into an `O(k/n)` deadline window.

### Lemma 5.1 (uniform local low-edge bound)

Fix `L<infinity`. Under (2.1), condition on `V,S`, and use either

- the ordinary local law `Law(L | Top_k(V)=S)`, or
- the Palm local law `Law(L^s | Top_k(V)=S,I_V=1)`.

For any local edge `{a,x}` with `a in A`, `x notin A`, and any deterministic or conditionally measurable `D<=Lk/n` not using that edge itself,

`P(W(a,x)<=D | exposed data) <= C_L k/n`                    (5.1)

after averaging over the remaining root/selected-neighbor deadline data. The constant is uniform in bounded offsets.

#### Proof: root endpoint

If `a=V`, then conditional on the root `k`th threshold `T=t` and `x notin S`, the edge `W(V,x)` is Uniform[`t`,1]. Hence

`P(W(V,x)<=D | T=t,x notin S)
 = (D-t)_+/(1-t) <= C_L k/n`.                                (5.2)

This remains true under Palm conditioning because, after `S` and the selected root edges are fixed, isolation only reweights the selected-neighbor stars; a nonselected root edge contributes only through the event that it stays above `T`.

#### Proof: selected-neighbor endpoint

Now let `a in S`, and write `d=W(V,a)` for its proposal deadline. Conditional on all root-star data and on the other internal local edges, the isolation condition at `a` requires at least `h=k-O(1)` qualifying competitors below `d` among `N=n-O(k)` external iid Uniform edges. Let

`B~Bin(N,d)`.

Conditioning on the relevant rejection event gives `B>=h`. By exchangeability of the external edges,

`P(W(a,x)<=d | B>=h,d)
 = E[B | B>=h,d]/N`.                                         (5.3)

Uniformly for `d<=Lk/n`, the conditional binomial mean satisfies

`E[B | B>=h,d]=O_L(k)`.                                      (5.4)

One elementary proof is to split at `2Nd`: if `h<=2Nd`, the ordinary mean is `O(k)` and the upper-tail conditioning changes it by at most a constant depending on `L`; if `h>2Nd`, the binomial mass ratio above `h` is bounded away from one, so the conditional overshoot above `h` is geometric with bounded mean. Thus (5.3) is `O_L(k/n)`.

For the part `d<W(a,x)<=D`, conditional on `W(a,x)>d` the residual edge is Uniform[`d`,1] and contributes at most `(D-d)/(1-d)=O_L(k/n)`. Therefore (5.1) follows. If `d>Lk/n`, the event `W(a,x)<=D` lies below the proposal deadline and the same exchangeability argument with threshold `D` gives the identical `O(k/n)` bound; alternatively split at a fixed multiple of `k/n` and use the root order-statistic tail. `square`

The only feature needed later is the scale `O(k/n)`, not a sharp constant.

---

## 6. #28 REPLACE FOR ALL WITH TYPICAL — isolation-mark flips are rare

We now bound the expected number of other vertices whose isolation indicators differ between `G` and `G^s`.

Fix `w notin A`. Because the far block is shared, all edges from `w` to vertices outside `A` are identical in the two graphs. Let

`R_w = kth smallest far edge from w to V\A`.                 (6.1)

Choose a fixed `L>1` with Chernoff rate `L-1-log L>5`. Then uniformly under (2.1),

`P(R_w>Lk/n) <= n^{-5+o(1)}`.                                (6.2)

The sum over all `w` of this bad probability is `o(1)`.

On `R_w<=Lk/n`, define the shared set `U_w` of the first `k` far neighbors of `w`. If no local edge `{w,a}`, `a in A`, falls below `R_w` in either local block, then `w` has the same top-`k` neighbor set `U_w` in `G` and `G^s`.

For `u in U_w`, the proposal edge `{w,u}` has shared weight at most `R_w`. Its reciprocal acceptance at `u` can differ between `G` and `G^s` only if some changed local edge `{u,a}`, `a in A`, crosses below that proposal deadline. Therefore, on the good far-threshold event, a flip of the isolation mark of `w` forces a **low local witness** among at most

`(k+1) + k(k+1) = O(k^2)`                                    (6.3)

local edges: either an edge from `w` to `A` that changes its proposal list, or an edge from one of the `k` shared proposed neighbors `u` to `A` that changes reciprocity.

Let `B_w(L)` and `B_w(L^s)` denote these witness events in the ordinary and Palm local blocks. Lemma 5.1 and a union bound give, conditional on the shared far data,

`P(B_w(L) | F,S) + P(B_w(L^s) | F,S) <= C_L k^3/n`           (6.4)

on `R_w<=Lk/n`.

A bare witness bound is not enough after summing over `n` vertices; we also need the rare-isolation factor. There are four combinations.

### 6.1 Same-local terms

Claim 291's bounded-omission marked-saddle proof applies verbatim after one specified low local witness is exposed: omit every rejection deadline touched by that witness. The witness itself costs `n^{-1+o(1)}`, while the remaining one-root isolation constraints cost `e^{-k+o(k)}`. Hence

`P(I_w(G)=1, B_w(L)) <= e^{-k+o(k)} n^{-1+o(1)}
                       = n^{-2+o(1)}`.                       (6.5)

For the Palm graph, use the two-root kernel from Claim 291. Before conditioning on `I_V`, a nonzero interaction witness together with `I_V` and `I_w` has probability at most

`e^{-2k+o(k)} n^{-1+o(1)}`.

Since `P(I_V)=e^{-k}(1+o_C(1))`, division by the Palm conditioning probability gives

`P(I_w(G^s)=1, B_w(L^s)) <= n^{-2+o(1)}`.                    (6.6)

### 6.2 Cross-local terms

Conditional on `(F,S)`, the ordinary and Palm local blocks are independent by construction. Thus (6.4) can be multiplied by the isolation probability generated by the other local block.

Using the one-root asymptotic,

`P(I_w(G)=1)=e^{-k}(1+o_C(1))`,                              (6.7)

and using the pair asymptotic from Claim 291,

`P(I_w(G^s)=1)
 = P(I_w cap I_V)/P(I_V)
 = e^{-k}(1+o_C(1)).`                                       (6.8)

Therefore

`P(I_w(G)=1, B_w(L^s)) <= C k^3/n * e^{-k}(1+o(1))
                         = n^{-2+o(1)}`,                     (6.9)

and similarly

`P(I_w(G^s)=1, B_w(L)) <= n^{-2+o(1)}`.                      (6.10)

### 6.3 Expected flips outside A

If the isolation mark of `w` differs, one of the four events in (6.5)--(6.10) occurs, except on the negligible bad far-threshold event. Hence

`P(I_w(G) != I_w(G^s)) <= n^{-2+o(1)}`                      (6.11)

uniformly for `w notin A`. Summing over at most `n` such vertices,

`E # {w notin A: I_w(G) != I_w(G^s)} = o(1)`.               (6.12)

### 6.4 Vertices inside A

The root `V` is isolated in `G^s` by construction. Its contribution to

`Z_n^s-(Z_n+1)`

is exactly `-I_V(G)`, whose expected absolute value is `p_n=O(1/n)`.

There are only `k` vertices in `S`. For each `u in S`, by the one-root and pair asymptotics,

`P(I_u(G)=1)+P(I_u(G^s)=1)=O(e^{-k})=O(1/n)`.                (6.13)

Therefore

`E # {u in S: I_u(G) != I_u(G^s)} = O(k/n)=o(1)`.            (6.14)

Combining (6.12)--(6.14) proves

`E | Z_n^s-(Z_n+1) | = o_C(1)`,                              (6.15)

which is Claim 293's coupling estimate.

---

## 7. Stein--Chen conclusion

For a nonnegative integer-valued `W` with mean `mu` and size-biased version `W^s`, the standard size-bias Poisson bound (e.g. Goldstein--Reinert, *Total Variation Distance for Poisson Subset Numbers*, 2006) gives

`d_TV(Law(W),Poisson(mu))
 <= (1-e^{-mu}) E | W+1-W^s |`.                              (7.1)

Apply this with `W=Z_n`. On the bounded critical window, `mu_n` stays bounded above and below by positive constants, and (6.15) yields

`d_TV(Law(Z_n),Poisson(mu_n))=o_C(1)`.                       (7.2)

Claim 288 gives `mu_n=n e^{-k}(1+o_C(1))`. Coupling two Poisson variables by adding/removing an independent Poisson increment gives

`d_TV(Poisson(mu_n),Poisson(n e^{-k}))
 <= |mu_n-n e^{-k}|=o_C(1)`.                                (7.3)

Thus

`d_TV(Law(Z_n),Poisson(n e^{-k}))=o_C(1)`.                  (7.4)

This recovers the uniform Poisson statement in Claim 289 without invoking all-fixed-`r` factorial moments. It is therefore a genuinely different audit route for the random-variable limit.

The connectivity theorem still also needs the nontrivial-component elimination. That part is unchanged and is not inferred from mean degree:

- sizes `2,...,6`: Claim 291's external-proposal/spanning-tree proof;
- sizes `7,...,12`: Claim 280's Cayley/crossing-edge bound;
- sizes `13,...,floor(n/2)`: the retained Claim 278 global component argument, with its threshold-envelope failure probability paid once.

Hence Claim 293 strengthens auditability of the Poisson half but does not alter the source-level status label by itself.

---

## 8. Adversarial self-audit of the new coupling

The main places where a hidden circularity could have entered are checked explicitly.

### 8.1 Does conditioning on `I_V` alter the far block?

No. Once the top-`k` root set `S` is fixed, every edge used to decide `I_V` touches `A={V} union S`; Lemma 3.1 is exact. Thus the far block remains iid and can be shared without approximation.

### 8.2 Does a distant isolation mark depend recursively on edges beyond one star?

No. As in Claim 292, reciprocal rejection of `{w,u}` at `u` depends on the count of **raw** edge weights in the star of `u`, not on whether those competitor edges survive bilateral preference. The decision tree has depth one.

### 8.3 Could a single low local edge contaminate many deadlines?

Yes, but for a fixed tested outside root `w`, one local edge can touch only the proposal-list test at `w` or the reciprocity test at one proposed neighbor `u`. In the same-local bounds (6.5)--(6.6), all deadlines touched by the witness are omitted, and Claim 291's bounded-omission lemma allows any fixed number of omissions. Multiple-witness events cost extra codimension and are smaller.

### 8.4 Is the worst-case influence argument a contradiction?

No. Section 4 shows deterministic influence can be linear, which is exactly why the proof uses the rare-isolation-weighted expectation rather than a worst-case Lipschitz bound.

### 8.5 Does pair control alone imply the result?

No. Claim 291's exact abstract 0/2-count counterexample remains valid. The extra ingredient here is an **explicit size-biased coupling with absolute expected error `o(1)`**. This is strictly stronger information than the first two factorial moments.

### 8.6 Weakest new lemma

The only genuinely new probabilistic estimate not already encapsulated in Claims 288/291 is Lemma 5.1's `O(k/n)` low-edge bound under the Palm local law. Its proof is an exchangeability/binomial-tail calculation at one selected-neighbor star; no global independence claim is used. An external audit should check (5.3)--(5.4) first.

---

## 9. What the three fresh Section-B methods produced

### #19 MAKE IT AN ALGORITHM — **worked**

The size-biased Palm law is realized exactly by resampling only the local block touching the root and its selected top-`k` neighbors while sharing every far edge. This resolves the previous objection that the Stein route had no actual coupling.

### #24 FIND THE EXTREMAL OBJECT — **worked as a barrier**

A concrete weight configuration makes one local-block change flip `Theta(n)` outside isolation marks. Thus deterministic bounded-influence Stein arguments are impossible in this coupling and should not be pursued.

### #28 REPLACE FOR ALL WITH TYPICAL — **worked**

On typical far thresholds, a flip requires a low local witness. Combining the witness codimension with the rare-isolation factor gives per-vertex flip probability `n^{-2+o(1)}` and total expected influence `o(1)`. This closes the size-bias Stein estimate.

No old coefficient-window optimization was rerun.

---

## 10. Source / prior-art record

Primary source checked fresh: Dabirian--Subramanian, DOI `10.1017/jpr.2025.10051`, Section 1.1 and Lemmas 10--14 / Theorems 4--6. The displayed coarse band remains stated as unresolved in the source.

Fresh bounded searches on 2026-09-18 for the exact title, DOI, authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral/mutual-preference constant-window variants found no later source-matching theorem. This does **not** prove worldwide openness or publication novelty.

The size-bias step is standard methodology. Goldstein and Reinert's 2006 total-variation bound is used only after the LK-specific coupling estimate (6.15) has been proved. Generic size-bias/Stein theory does not itself resolve P0456.

Publication novelty of Claims 288--293 remains `UNVERIFIED`.

---

## 11. Directed peer-audit duty

The directed P03->P04 duty remains active in principle, but P04's newest recovered record

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`

explicitly states `ROTATION STOP / NO NEW RESEARCH RUN COUNTED` and creates no mathematical theorem. Earlier P04 claims listed in the user exclusion list have already been P03-audited. Therefore there is no genuine new P04 claim to audit in this run, and no audit is fabricated.

---

## 12. Current claim ledger for P0456

- Claim 274: preserved proved isolation lower-bound mechanism.
- Claim 276: preserved coarse-window coefficient-zero theorem.
- Claim 278: preserved exact marking/finer-window theorem.
- Claim 280: preserved joint-race bracket and fixed-component machinery.
- Claim 282: preserved ordered-deadline `sqrt(log n loglog n)` coefficient-zero theorem.
- Claim 284: preserved normal-race `sqrt(log n)` bracket.
- Claim 286: preserved sparse-deletion `sqrt(log n)` coefficient-zero theorem.
- Claim 288: **PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING**.
- Claim 289: **PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING**.
- Claim 290: **PROVED / SELF-AUDIT-STRENGTHENING / MARKED-PPP CROSSCHECK / AUDITS-PENDING**.
- Claim 291: **PROVED / SELF-AUDIT-KERNEL / pair + small components / AUDITS-PENDING**.
- Claim 292: **PROVED / SELF-AUDIT-STRENGTHENING / all-fixed-r interaction graph / AUDITS-PENDING**.
- Claim 293: **PROVED / SELF-AUDIT-STRENGTHENING / local-block size-bias Stein route / AUDITS-PENDING**.

No claim in this list is promoted to externally audited closure in this run.

---

## 13. Metrics, stuck state, failures, and exact remaining obligation

The previously admitted fixed-coefficient metrics remain saturated:

- `c_LK^cert=0`;
- `a_LK^fine=0`;
- `b_LK^sqrt=0`.

They are not used for unchanged/stuck counting. Claims 288--293 are in audit/repair state, not a newly admitted metric. HARD recoveries remain `0/2`.

The failed route learned this run is the deterministic influence approach: worst-case local-block resampling can flip linearly many isolation marks. The repaired route is average influence under the Palm coupling.

The exact remaining closure obligations are:

1. an independent P26 full-proof audit of the source-matching chain, now preferably using Claim 291 plus Claim 293 as compact audit kernels;
2. one genuinely distinct OTHER-track full-proof audit;
3. repair any objection either audit raises;
4. continue prior-art verification through author/citation/current-literature paths;
5. only after 1--4 pass, create the self-contained source-matching paper folder and request shared-ledger closure through `ledger_delta`.

Do not count P03 self-checks as either outside audit.

---

## 14. Next concrete attack

Audit-first priority remains absolute: consume any incoming P26/OTHER-track objection before new mathematics.

If no external audit arrives before the next run, use a fresh Section-B triple rather than repeating this coupling:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** write a finite rank/order representation of the Palm local-block coupling in which the only randomness relevant to one outside mark is an explicit finite collection of order ranks;
- **#20 FIND WHY THE ALGORITHM FAILS:** adversarially test Lemma 5.1 at the extreme selected-neighbor deadlines and search for a conditioning regime where the `O(k/n)` low-edge bound is false or loses a factor;
- **#27 SWAP THE QUANTIFIERS:** seek a coupling estimate uniform for all `|k-log n|<=C` with an explicit error function `epsilon_C(n)`, and determine how far `C=C_n` may grow before the proof fails.

A quantitative Stein rate may be stated only if every error term is made explicit. Otherwise retain the qualitative `o_C(1)` result.

---

## 15. `ledger_delta` for P26

```text
P03 | P0456 Dabirian--Subramanian bilateral-preference connectivity | source-scale/fine/sqrtlog coefficient metrics remain 0/0/0 (SATURATED; no fake stuck count) | NEW supporting Claim P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING: exact root-local Palm resampling realizes the size-biased isolated-vertex count and proves E|Z^s-(Z+1)|=o_C(1), giving an independent Stein--Chen TV-Poisson proof on every fixed bounded offset window; candidate-complete Claims 288/289 remain SOURCE-MATCHING / OUTSIDE_AUDITS_FOUND_0_OF_2; publication novelty UNVERIFIED; recoveries 0/2; no paper package yet.
```

Next state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_293_SIZEBIAS_AUDIT_KERNEL_READY`.

**End of complete run report.**