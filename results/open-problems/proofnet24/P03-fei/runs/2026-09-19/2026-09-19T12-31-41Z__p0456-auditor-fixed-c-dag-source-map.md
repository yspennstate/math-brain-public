Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #22 READ THE FAILURES, NOT THE SUCCESSES**. The main new result is an auditor-facing fixed-window theorem with an explicit raw-edge dependency DAG, plus a direct proof that every bad interaction in the source's Lemma-10 event is captured by the canonical `c/p/q` skeleton on the joint-isolation event.

# P03 / P0456 run report — auditor fixed-C DAG and source-failure map

Run timestamp: **2026-09-19T12:31:41Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, and audit-first screen

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run is

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T11-28-49Z__p0456-canonical-incidence-skeleton.md`,

creation commit `ab04ff5bacc26cc69de0608644cdd36d3eaff621`, blob `89fbdea70cf16a733fe06249f2ffa70db5b8d0ee`; its prior exact-commit/blob readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--311. Claims 288/289 remain internally source-matching candidate-complete but outside-audit pending. Claim 301 remains valid only with the explicit repairs and simplifications in Claims 302--311. In particular, Claims 302/304 must retain Claim 309's root-merge repair and may **never** restore the false `r>=3` shortcut saying that a root--root edge below both deleted-array kth thresholds is necessarily bilaterally selected. Claim 311's canonical incidence charge `K=c+p+q` is the controlling interaction decomposition.

Before the mathematical attack I reread or exact-path recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, current `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the newest complete P03 report, current P26 evidence, and neighboring `operations/claims/P0457.md` only for nonduplication. Several policy/ledger surfaces are connector-truncated, so these are targeted current-path reads rather than a claim of byte-for-byte visual rereading. P0457 remains the distinct bilateral-preference diameter problem owned by NM13-04.

The exposed task-control surface still does not provide a binding model-family or reasoning-effort selector. The requested `GPT-6 / maximum` therefore remains prompt-only. This report identifies the runtime as GPT-5.6 Sol; reasoning level is UNVERIFIED.

### 1.1 Incoming outside-audit screen

The newest concrete P26 report recovered before the proof attack is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_12-59-00__run-report.md`,

creation `2761d418d21592951655ca9837a095e5492bd2a5`, blob `e3f511bd2843ffd9334344526ee0b03e66d7842e`.

It is a thinking/stuck run on R06's Romero max-minus-four reliability obstruction, not a P0456 audit. Fresh repository searches for `P0456`, the repaired Claim-288/289/301/311 chain, `PASS`, and P26/OTHER-track audit terminology still recover no P26 or genuinely distinct OTHER-track end-to-end P0456 proof audit. Therefore the gate remains exactly

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. I do **not** label the source CLOSED and do **not** create the final paper package.

### 1.2 Fresh primary-source and 2026 literature/status check

The source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

The current Cambridge PDF was reread, including page images around Lemmas 10--14 and Theorems 3--6. Section 1.1 still states that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and attributes the gap to analytically simpler sufficient conditions, including the no-intersection condition imposed in the isolated-vertex proof. The authors explicitly say a more elaborate or exact set of sufficient conditions could close the gap.

The requested source checkpoints remain unchanged:

- Lemma 10 defines the five bad-interaction events `B_{1;2}`, `B_{2;1}`, `B_{1 union 2}`, `B_{1->2}`, `B_{2->1}` and proves `P(B)=O(k^3/n)`.
- Lemma 11 gives the one-root isolation suppression on the one-sided bad branches.
- Lemma 12 combines Lemmas 10 and 11 to bound `P(I_1 I_2 cap B)` by an extra `exp(-log n)` factor times the one-root isolation scale.
- Lemma 13 gives exact conditional independence of `I_1,I_2` on `B^c`.
- Lemma 14 converts those bounds into the pair-ratio estimate used by Theorem 3.
- Theorem 3 is the source disconnectedness result below `t'<-1/2`.
- Theorem 4 excludes every fixed bounded degree above `t'>1/2`.
- Theorem 5 excludes components in its logarithmic-size-to-`n/2` range for `k=floor(t log n)`.
- Theorem 6 is the source connectivity theorem above `t'>1/2`.

Fresh bounded searches dated 19 September 2026 for the exact DOI/title/authors, bilateral-preference connectivity, Poisson isolated vertices, and 2026 follow-ups recovered the Cambridge paper, the older arXiv preprint, current bibliographic mirrors, the University of Michigan author/group surfaces, and no later source-matching constant-window connectivity/Poisson theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. #3 PROVE SOMETHING STRONGER — a single auditor-facing fixed-C theorem

The correction claims 295--300 are useful historical strengthening but are not logically needed for the source theorem. The source-facing proof can be compressed to the following theorem and a finite dependency DAG.

### Claim `P03-P0456-AUDITOR-FIXED-C-DAG-SOURCE-MAP-312`

**Status:** `PROVED / SELF-AUDIT-PACKAGING / SOURCE-FAILURE-COMPLETE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `C<infinity`. Uniformly for integers

`|k-log n|<=C`,

put

`lambda_n=n exp(-k)`.

Then:

1. for every fixed integer `r>=1` and every deterministic ordered tuple of distinct roots `R=(v_1,...,v_r)`,

   `P(I_{v_1}=...=I_{v_r}=1)=exp(-rk)(1+o_C(1))`;

2. if `Z_n=sum_v I_v` is the isolated-vertex count, then

   `d_TV(Law(Z_n),Poisson(lambda_n))->0`

   uniformly on the fixed `C` window;

3. the probability of any nontrivial connected component of size `2,...,floor(n/2)` is `o_C(1)` under the literal LK rule;

4. consequently

   `P(LK(n,k) is connected)=exp(-lambda_n)+o_C(1)`;

5. for every pair of distinct roots `v_a,v_b`, if `B^{a,b}` denotes the source's Lemma-10 pair-bad event with those roots substituted for 1,2, then on the joint-isolation event

   `{I_{v_1}=...=I_{v_r}=1} cap B^{a,b} subset {K>=1}`,

   where `K=c+p+q` is Claim 311's canonical exhaustive incidence complexity. More precisely, every one of the five source bad-event types maps to collision charge `c`, root-edge charge `p`, or support-edge charge `q` as proved in Section 5 below.

Items 1--4 are the fixed-C source theorem. Item 5 is the stronger auditor-facing statement: it identifies the source's exact pair-proof failure modes inside the repaired all-fixed-r interaction skeleton.

### 2.1 Explicit dependency DAG

The proof uses the following directed acyclic graph. Every arrow below is either deterministic or supported by a named disjoint raw-edge family.

```text
raw iid edge weights W
   |
   +--> delete root-root edges
   |       |
   |       +--> independent root-to-outside proposal arrays A_a
   |       |       |
   |       |       +--> outside-label partition pi --> collision excess c
   |       |       +--> ordered proposal values/deadlines
   |       |
   |       +--> independent root-root raw family
   |               |
   |               +--> endpoint-active pattern --> p,d_a
   |                                   |
   |                                   +--> safe terminal suffix omissions (Claim 309/310)
   |
   +--> collision global-minimum retention (Claim 302/310)
           |
           +--> preliminary retained deadlines L_0
                   |
                   +--> complete support-incidence graph Gamma_0
                             |
                             +--> q=number of positive-degree support-edge vertices
                             +--> simultaneous deletion N(H)
                             +--> residual blocks B_u={W(u,x): x in E}
                                      |
                                      +--> exact residual independence
                                      +--> Claim 303 bounded-omission upper saddle

clean branch (no positive interaction):
root proposal arrays + clean external blocks --> Claim 308 exact one-root saddle h=k
                                         --> Claim 306 clean sufficient lower event

upper + lower --> fixed-r joint isolation
             --> all fixed factorial moments of Z_n
             --> Claim 305 finite Brun inequality
             --> total-variation Poisson

literal LK component branch:
raw W --> sizes 2--6 internal-edge deletion/external proposals
      --> one global kth-threshold envelope for sizes 7--n/2
      --> no nontrivial components

TV Poisson + no nontrivial components --> connectivity = exp(-lambda_n)+o_C(1).
```

No arrow invokes Claims 295--300. No sparse dependency graph, Scheffe argument, subsequence extraction, or black-box Poisson theorem is needed.

---

## 3. Raw-edge sigma-fields behind the DAG

Fix roots `R={v_1,...,v_r}` and delete all `binom(r,2)` root--root edges. Put `N=n-r`.

For root `a`, let

`A_a={W({v_a,x}): x notin R}`.

These raw edge families are pairwise disjoint, hence independent. The first `k` outside order statistics and their ordered labels are measurable with respect to `A_a`. By iid exchangeability, the ordered labels are independent of the ordered values inside each root array.

The root--root family

`A_RR={W({v_a,v_b}):1<=a<b<=r}`

is disjoint from every `A_a` and is therefore independent of all deleted-array proposal data. Claim 309 records endpoint activity relative to the deleted-array threshold `T_a` and Claim 310 proves that omitting the final `d_a` outside ranks is always safe, even though the exact final number `q_a^*` of root edges entering root `a` can be strictly smaller than `d_a`.

If a selected outside label `u` is not among root `b`'s exposed outside proposals and root `b`'s terminal exposed threshold is `T_b=t`, exchangeability of the unexposed tail gives the exact conditional law

`W({v_b,u}) | (proposal array at b, u absent) ~ Uniform[t,1]`.

This is the only special conditional law needed for selected-label/nonowner-root support edges.

After Claim 311's canonical support deletion, write `S` for all proposal labels and

`E=V\(R union S)`.

For each surviving selected label `u`, define

`B_u={W({u,x}):x in E}`.

For `u!=z`, the undirected raw edge sets underlying `B_u` and `B_z` are disjoint because the edge `{u,z}` is excluded from both: `u,z` lie in `S`, not `E`. The `B_u` are also disjoint from every root proposal family, every root--root edge, and every nonexternal support edge already integrated into `Gamma_0`. Hence residual rejection randomness is **exactly independent**. This is the only factorization used in the positive-cluster upper proof.

---

## 4. Proof of Claim 312 items 1--4

### 4.1 Fixed-r upper joint-isolation bound

Apply the canonical algorithm of Claim 311 to the fixed root tuple. On the threshold guard, its complexity is

`K=c+p+q`,

where `c` is collision excess, `p` counts unique endpoint-active root--root raw edges, and `q` counts all unique positive-degree nonexternal support raw edges in the complete predeletion incidence graph `Gamma_0`.

Claim 311 gives a unique exhaustive tie-free skeleton and the literal count

`# skeleton patterns of complexity K <= (C_r k^2)^K`.

Each unit of collision excess costs `n^{-1+o(1)}` from the exact injection ratio, and each prescribed active root/support raw edge costs `O(k/n)` on the guard. Therefore for every fixed `D`,

`P(K>=D, guard) <= sum_{K>=D}(C_r k^3/n)^K = n^{-D+o(1)}`.

Take `D=r+1`. Since `k=log n+O_C(1)`,

`e^{-rk}=n^{-r} e^{O_C(r)}`,

and the high-complexity mass is `o(e^{-rk})`.

For `1<=K<r+1`, the number of root/collision/support deletions is bounded in terms of fixed `r`. Claim 303 applies uniformly to the surviving residual deadlines and gives

`P(residual rejections | skeleton) <= exp[-rk+O_{C,r}(k^(2/3)+log k)]`.

Multiplying by at least one defect codimension `n^{-1+o(1)}` and summing the `k^{O_r(K)}` canonical patterns yields

`P(joint isolation,K>=1)=o(e^{-rk}).`

On `K=0`, no deadline is omitted and the residual raw blocks are clean and disjoint. Claim 308 at the actual quota `h=k` gives the clean one-root factor

`e^{-k}(1+o_C(1))`.

Hence

`P(joint isolation) <= e^{-rk}(1+o_C(1)).`                  (4.1)

### 4.2 Fixed-r lower joint-isolation bound

The lower bound uses a different mechanism and needs no arbitrary-rank omission estimate. Use Claim 306's sufficient event `L_R`:

- all `rk` outside proposal labels are distinct;
- every root--root edge is later than the fixed root threshold guard;
- all root kth outside thresholds satisfy the guard;
- for every selected outside label `u`, at least `k` edges from `u` into the external pool `E=V\(R union S)` are lighter than its root proposal deadline.

The last conditions use the pairwise disjoint blocks `B_u`; they directly force every root proposal to be rejected at its selected neighbor. Root--root edges are too late to enter. Therefore `L_R` implies joint isolation.

Label distinctness and root-edge lateness cost `1-o_C(1)`. Removing only `O_r(k)` roots/selected labels from the external competitor pool perturbs the clean saddle exponent by `O_r(k^2/n)=o(1)`. Claim 308's clean saddle then gives

`P(L_R)=e^{-rk}(1-o_C(1)).`

Thus

`P(joint isolation) >= e^{-rk}(1-o_C(1)).`                  (4.2)

Combining (4.1)--(4.2) proves item 1.

### 4.3 Factorial moments and finite Brun total variation

Let `Z_n=sum_v I_v`. Summing the uniform fixed-root estimate over ordered distinct `r`-tuples gives

`E[(Z_n)_r]=(n)_r e^{-rk}(1+o_C(1))=lambda_n^r+o_C(1)`

for every fixed `r`. On `|k-log n|<=C`, `lambda_n<=e^C`.

Claim 305 gives the explicit finite inequality: if

`delta_m=|E[(Z_n)_m]-lambda_n^m|`, `Lambda=e^C`,

then for every `J>=0` and even `T>=0`,

`d_TV(Law(Z_n),Poi(lambda_n))`
` <= (2Lambda+delta_1)/(2(J+1))`
` + (1/2) sum_{j=0}^J 1/j! [`
`       sum_{t=0}^T delta_{j+t}/t!`
`       + (Lambda^(j+T+1)+delta_{j+T+1})/(T+1)! ].`

First choose `J`, then even `T`, then send `n->infinity`. Only finitely many fixed factorial moments are required at each stage, and all their errors vanish uniformly. This proves item 2 without any subsequence or black-box Poisson theorem.

### 4.4 Literal nontrivial-component elimination

For fixed component sizes `2<=s<=6`, delete all candidate-component internal edges **before** ranking external proposals. A component vertex has at most `s-1` internal preferred edges, so at least

`p_0=k-(s-1)`

external proposals must be rejected. The external proposal/rejection raw-edge families are disjoint from the internal spanning-tree raw edges. Claim 305's boundary audit verifies that if a cross label lies beyond rank `p_0` at another root, conditional on the `p_0`th external threshold its raw edge has the exact Uniform-tail law needed by the repaired interaction analysis. The resulting fixed-size bound is

`P(exists an s-component)`
` <= n^{1-s+o(1)} k^{s-1} + n^{-2+o(1)} k^{s-1}`
` = o(1)`

for every `2<=s<=6`.

For sizes `7<=s<=n/2`, use the one global two-sided kth-threshold event with

`a=5/32`, `b=32/5`.

The two vertexwise Chernoff rates satisfy `I(a)>1` and `I(b)>1`, so the failure probability of the global event is `o(1)` and is paid **once**. On the event, a size-`s` component has an internal spanning tree all of whose edges are at most `bk/(n-1)`, while every crossing edge is at least `ak/(n-1)`. Hence

`P(exists s-component, global event)`
` <= C(n,s) s^(s-2) [bk/(n-1)]^(s-1)`
`    * [1-ak/(n-1)]^(s(n-s)).`

For each fixed `7<=s<=12`, the leading `n` exponent is `1-as`, already negative at `s=7` (`-3/32`). For the uniform tail `13<=s<=n/2`, use `(n-s)/(n-1)>=1/2`; the conservative exponent becomes `1-(a/2)s`, equal to `-1/64` at `s=13`, and the remaining sum is geometric. Thus every nontrivial component vanishes, proving item 3.

This proof uses the literal LK rule throughout and never infers connectivity from mean degree.

### 4.5 Connectivity

If LK is disconnected, it has some component of size at most `n/2`. Item 3 says that, with probability `1-o_C(1)`, the only possible such components are isolated vertices. Therefore

`P(LK connected)=P(Z_n=0)+o_C(1)`.

Item 2 gives

`P(Z_n=0)=exp(-lambda_n)+o_C(1)`,

proving item 4.

---

## 5. #22 READ THE FAILURES, NOT THE SUCCESSES — every source Lemma-10 bad interaction maps to c, p, or q

This is the most source-specific audit in the run. The source defines, for two roots 1 and 2,

- `B_{1;2}`: root 2 lies in root 1's top-k preferred set;
- `B_{2;1}`: the symmetric event;
- `B_{1 union 2}`: the two root top-k preferred sets share a vertex;
- `B_{1->2}`: some `i` preferred by root 1 has in its own top-k preferred set either root 2 or a vertex preferred by root 2;
- `B_{2->1}`: symmetric;
- `B` is their union.

The source throws the entire event `B` into a coarse `O(k^3/n)` exceptional branch. Claim 311 instead records exact local defects. The next lemma proves that none of the source's bad mechanisms escapes the canonical charges when isolation actually occurs.

### Lemma 312.1 — source-bad interaction completeness

Fix a pair of roots `v_a,v_b` inside the fixed `r`-tuple and define the five source bad events with `a,b` substituted for 1,2. On the tie-free event,

`{all r roots isolated} cap B^{a,b} subset {c+p+q >=1}.`       (5.1)

#### Proof

It is enough to prove the contrapositive. Assume all `r` roots are isolated and `K=c+p+q=0`.

Because `p=0`, no root--root edge is endpoint-active relative to any deleted-array kth outside threshold. By Claim 310, a root--root edge heavier than the initial deleted-array threshold can never enter after root edges are restored. Thus the full top-k preferred set of each root consists exactly of its first `k` outside labels.

Because `c=0`, all `rk` outside proposal labels are distinct. Therefore the top-k preferred sets of roots `a` and `b` are disjoint, and neither root can appear in the other's top-k list. Hence

`B_{a;b}`, `B_{b;a}`, and `B_{a union b}`

are all false.

It remains to rule out `B_{a->b}`. Suppose it occurs. Then there exist

`i in R_a^{<=k}`

and

`y in (R_b^{<=k} union {v_b}) cap R_i^{<=k}`.

Since `p=c=0`, `i` is one of the uniquely selected outside labels, while `y` is either root `v_b` or a distinct selected outside label. Therefore `y in (R union S)\{i}`. Let

`D_i=W({v_a,i})`

be the retained proposal deadline for `i`. There are two possibilities.

If

`W({i,y}) < D_i`,

then `{i,y}` is a nonexternal raw support edge lighter than a retained deadline, so it is a positive-degree right vertex of Claim 311's incidence graph `Gamma_0`. Thus `q>=1`, contradicting `K=0`.

If instead

`W({i,y}) > D_i`,

then because `{i,y}` lies in `i`'s top-k set, the strictly lighter edge `{v_a,i}` must also lie in `i`'s top-k set. But `i` lies in root `v_a`'s top-k set by construction. Hence `{v_a,i}` is bilaterally selected, contradicting isolation of root `v_a`.

Ties have probability zero. Thus `B_{a->b}` is impossible under joint isolation and `K=0`. The same argument rules out `B_{b->a}`. Therefore every source bad event is false, proving (5.1). `square`

### 5.1 Exact type-to-charge map

The proof gives the requested source-failure dictionary:

| Source failure type | Canonical charge on joint isolation |
|---|---|
| root `b` directly in root `a` top k (`B_{a;b}`) | `p>=1` (endpoint-active root--root raw edge) |
| root `a` directly in root `b` top k | `p>=1` |
| shared preferred outside label (`B_{a union b}`) | `c>=1` (proposal-label collision) unless already `p>0` |
| selected neighbor of `a` sees root `b` (`B_{a->b}` with `y=b`) | `q>=1`, otherwise the root-a proposal survives bilaterally and isolation fails |
| selected neighbor of `a` sees a selected neighbor of `b` | `q>=1`, otherwise the root-a proposal survives bilaterally and isolation fails |
| symmetric `b->a` cases | same `q` charge |

This is not an equality `B={K>0}`. Claim 311 deliberately sees additional interactions that the source pair event does not record, for example low support edges among selected labels belonging to the same root. The correct statement is the one needed for auditing: **on joint isolation, every source-defined bad interaction belongs to the positive canonical skeleton.**

### 5.2 Relation to source Lemmas 10--14

This map explains precisely how the repaired proof goes beyond the source's failure handling:

- **Lemma 10:** the source upper-bounds the union of direct-root, shared-label, and cross-neighbor interactions by `O(k^3/n)`. Claim 311 resolves those interactions into separate codimension units `p,c,q`, and also records source-unlisted interactions needed for all fixed `r`.
- **Lemma 11:** the source removes carefully chosen interacting edges and proves a one-root necessary-condition bound on the bad branch. Claim 303 is the arbitrary-rank, bounded-omission analogue after the exact finite support deletion of Claims 309--311.
- **Lemma 12:** the source pays one coarse bad-event probability together with one-root isolation suppression. The canonical proof pays each actual defect codimension and retains the `exp[-rk+o(k)]` rejection cost across all fixed roots, which is the scale needed for factorial moments.
- **Lemma 13:** the source obtains exact pair conditional independence only on `B^c`. Claims 310--311 instead make the **residual raw-edge blocks exactly disjoint after deleting the finite support of every canonical skeleton**, so positive interactions need not be discarded wholesale.
- **Lemma 14:** the source only needs a pair-ratio second-moment estimate in its lower window. Claim 312 obtains every fixed joint moment in the constant window and then uses the finite Brun inequality, not pair-only inference, to obtain Poisson total variation.

Most importantly, the source Section 1.1 explicitly identifies no-intersection sufficient conditions as a cause of its gap. The `c/p/q` support-deletion mechanism is exactly a rigorous way to retain intersecting configurations while charging and deleting only the finite raw-edge support that destroys independence.

No source-type bad event escaped all three charges. Therefore this run finds **no new gap** in the repaired source chain.

---

## 6. #14 FIND THE GROUP ACTING — use only the symmetry that genuinely shortens the proof

The useful symmetry is the permutation group on outside labels, not a blanket root/rank symmetry.

Let `N=n-r` and let

`G=S_N`

act on the outside vertex labels while fixing the ordered root tuple. The `rk` ordered proposal positions form

`Omega=[r] x [k]`.

For any feasible set partition `pi` of `Omega` (no block contains two positions from the same root), the group `G` acts transitively on ordered proposal-label arrays having equality pattern exactly `pi`. If `m=|pi|`, the stabilizer may permute the `N-m` unused outside labels freely, so the orbit has size

`(N)_m`.

Because each root's ordered outside-label list is an independent uniform sample without replacement, the total number of ordered arrays is

`(N)_k^r`.

Therefore a fixed feasible equality partition has the **exact** probability

`P(label partition=pi)=(N)_m/(N)_k^r`.                       (6.1)

If its collision excess is `c=rk-m`, the number of partitions with excess `c` is at most `(rk)^{2c}`: starting from singletons, encode any such partition by `c` merge steps, each specified by at most `(rk)^2` choices. Equations (6.1) and this count give the collision codimension used in Claim 311 without hidden label multiplicity.

This is the only quotient that genuinely simplifies the proof. I deliberately do **not** quotient by proposal-rank permutations: ranks carry ordered deadlines, root-suffix omissions, and the global-minimum collision representative, so rank permutation is not a symmetry of the canonical skeleton. Root permutations form only a fixed `S_r` factor and can obscure endpoint-active patterns and deterministic-root conditional laws; removing a constant `r!` does not improve any asymptotic estimate. Thus no symmetry is used to hide root labels or conditional distinctions.

---

## 7. Adversarial checks and preserved counterexamples

Two earlier counterexamples remain mandatory safeguards and are preserved explicitly.

### 7.1 Claim 309 root-merge counterconfiguration

For `r=3`, one can have

`T_{1,k-1}<W12<T_{1,k}`, `T_{2,k-1}<W12<T_{2,k}`,

while other root edges `W13`, `W23` lie below the corresponding `(k-1)` outside thresholds at roots 1,2 but above root 3's threshold. Then `W12` is below both deleted-array kth thresholds yet is pushed out of both final root lists. Thus the old `below both => bilaterally selected` shortcut is false for `r>=3` and must never be restored.

### 7.2 Claim 310 endpoint-active over-omission is not exact occupancy

With `k=2`, outside weights `0.1,0.4`, and root edges `0.2,0.3`, both root edges are endpoint-active relative to the initial threshold `0.4`, so `d=2`, but after `0.2` enters the final top two are `0.1,0.2`; the `0.3` root edge no longer enters. Hence `q^*=1<d=2`. Claim 309's terminal suffix omission is a safe upper-bound deletion, not an exact statement about final root occupancy.

Neither counterexample affects Claim 312 because its upper proof only requires safe deletion and canonical raw-edge charges.

---

## 8. Cumulative claim ledger delta

Preserved without status inflation:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains PPP; Claims 291--300 remain historical supporting self-audit/strengthening kernels but are not dependencies of Claim 312's fixed-C source route.
- `P03-P0456-SOURCE-AUDIT-CAPSULE-301` remains proved only with Claims 302--312.
- Claims 302/304 retain the Claim-309 root-merge repair.
- Claim 305 remains the sole finite Brun/TV conversion.
- Claim 308 remains the clean one-root analytic input at actual quota `h=k`.
- Claim 309 remains the root-merge repair.
- Claim 310 remains the sequential merge/support-deletion lemma.
- Claim 311 remains the canonical exhaustive incidence skeleton and order-independent `K=c+p+q` charge.

New:

### Claim `P03-P0456-AUDITOR-FIXED-C-DAG-SOURCE-MAP-312`

**Status:** `PROVED / SELF-AUDIT-PACKAGING / SOURCE-FAILURE-COMPLETE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

It packages the fixed-C source theorem in one explicit dependency DAG and proves that every exact source Lemma-10 bad interaction maps, on joint isolation, into positive canonical complexity `K>=1`.

The source remains **not CLOSED** because the required outside audits are still absent.

---

## 9. Exact remaining obligation and `ledger_delta` for P26

The mathematical fixed-C chain is internally packaged and self-audited. The exact closure obligation remains external:

1. one full end-to-end independent audit by P26 of Claim 312 and its dependencies Claims 305, 308, 309--311 plus the literal component lemma;
2. one genuinely distinct OTHER-track full end-to-end audit of the same repaired chain;
3. only if both PASS, create the final self-contained source-matching paper folder and request source closure through P26/shared-ledger reconciliation.

Self-audits, repeated P03 derivations, and multiple P26 passes do not fill the second slot.

`ledger_delta` (for P26 only; P03 does not edit shared root ledgers):

```yaml
track: P03
source: P0456
state: P0456_ACTIVE_AUDIT_PENDING
outside_audits_found: 0/2
new_claim:
  id: P03-P0456-AUDITOR-FIXED-C-DAG-SOURCE-MAP-312
  status: PROVED / SELF-AUDIT-PACKAGING / SOURCE-FAILURE-COMPLETE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
  dependencies:
    - P03-P0456-EXPLICIT-BRUN-BOUNDARY-CROSSCHECK-305
    - P03-P0456-AUDITOR-MAP-CUT-BARRIER-306
    - P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308
    - P03-P0456-ROOT-MERGE-SIGMA-COMPLETENESS-309
    - P03-P0456-SEQUENTIAL-MERGE-SUPPORT-DELETION-310
    - P03-P0456-CANONICAL-INCIDENCE-SKELETON-311
  source_failure_map: "on joint isolation, every source Lemma-10 bad event forces c+p+q>=1"
request:
  - "P26: perform one independent end-to-end audit of Claim 312, including the source Lemma-10 failure map and component layer"
  - "Distinct non-P03/non-P26 track: perform the second independent end-to-end audit"
source_closed: false
paper_package_created: false
publication_novelty: UNVERIFIED
metrics:
  c_LK_cert: 0
  a_LK_fine: 0
  b_LK_sqrt: 0
  hard_recoveries: 0/2
```

---

## 10. Next concrete attack

If no outside audit arrives, the next run should not add correction coefficients or enlarge the coefficient window. It should attack the canonical proof at its remaining quantitative union-bound interface rather than re-prove the DAG.

Suggested nonconsecutive Section-B triple:

- **#2 ATTACK THE NEGATION FIRST:** attempt to construct a fixed-r realization with canonical `K=1` or `K=2` whose witness multiplicity exceeds the Claim-311 `(C_r k^2)^K` pattern count after conditioning on the label partition. Any such example would expose a genuine union-bound gap.
- **#25 COUNT THE SAME THING TWICE:** compute the total `K=1` joint-isolation contribution once from the canonical skeleton classes (`c=1`, `p=1`, `q=1`) and independently from the five source pair-bad mechanisms at `r=2`; disagreement identifies an uncharged or multiply charged class.
- **#30 DO ONE SCALE / ONE DIRECTION AT A TIME:** isolate the `q=1` selected-support-edge case and prove its conditional `O(k/n)` codimension uniformly for each of the three support-edge geometries (selected--selected, selected--nonowner-root tail, and root-edge support), with exact sigma-fields.

Incoming outside audits still take priority over all of these.

---

**End of complete run report.**