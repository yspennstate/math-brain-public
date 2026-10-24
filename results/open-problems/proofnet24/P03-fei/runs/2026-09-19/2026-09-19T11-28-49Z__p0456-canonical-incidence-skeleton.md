Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM, #28 REPLACE FOR ALL WITH FOR TYPICAL**. The main new result is a canonical, order-independent incidence skeleton for Claims 309--310, together with an explicit `k^{O(K)}` skeleton count and a geometric high-complexity tail. The exact canonical charge is conserved; a greedy “first edge that deletes a deadline” charge is not.

# P03 / P0456 run report — canonical incidence skeleton and deletion invariant

Run timestamp: **2026-09-19T11:28:49Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run is

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T10-28-24Z__p0456-sequential-root-merge-support-deletion.md`,

creation commit `753a1270d018cabbbbafc28103627f71c196549e`, blob `e88d1a9635dd36c82bd3a73c24207de1b4c19197`; its exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286, 288--310. Claim 309 remains the controlling repair for the false `r>=3` both-end-impossible shortcut in Claims 302/304, and Claim 310 remains the deterministic root-merge/support-deletion simplification. This run adds Claim 311 below.

Before the attack I reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, current `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the newest complete P03 report, current audit evidence, and neighboring `operations/claims/P0457.md` only for nonduplication. Several of the root policy/ledger surfaces and the newest report are large connector-rendered files; those reads were truncated by the connector and are **not** represented here as byte-for-byte rereads. Exact target paths and target-scoped evidence were recovered directly.

`P0457` remains the distinct bilateral-preference **diameter** problem owned by NM13-04, not a duplicate of P0456.

### 1.1 Incoming outside-audit screen

The newest P26 report recovered this run is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_12-59-00__run-report.md`,

creation commit `2761d418d21592951655ca9837a095e5492bd2a5`, exact blob `e3f511bd2843ffd9334344526ee0b03e66d7842e` according to its readback sidecar.

It is a P26 **thinking/stuck** run about the R06 Romero max-minus-four obstruction, not an audit of P0456. Fresh repository searches for `P0456 PASS`, Claim 288, Claim 310, and the repaired chain recover no P26 or genuinely distinct OTHER-track end-to-end P0456 PASS. Therefore

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`

remains exact. Self-audits do not count. I do **not** label the source CLOSED and do **not** create the final paper package.

### 1.2 Fresh primary-source / literature check — 19 September 2026

The controlling source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge PDF text and page-image verification again show Section 1.1 stating that connectivity is unknown in the band

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and attributing the gap to analytically simpler sufficient conditions, including the no-intersection condition for isolated vertices. The source says that more elaborate or exact sufficient conditions could close the gap.

The requested source checkpoints were reverified from the current PDF:

- Lemma 10: `P(B)=O(k^3/n)` for the pair bad event.
- Lemma 11: the source one-root isolation upper bound on the bad branches.
- Lemma 12: the corresponding extra `exp(-log n)` suppression of `P(I_1 I_2 cap B)`.
- Lemma 13: exact conditional independence on the source good event `B^c`.
- Lemma 14: under the source lower-window hypothesis `t'<-1/2`, `limsup E[I_1I_2]/E[I_1]^2 <= 1`.
- Theorem 3: disconnectedness with high probability below the source `-1/2` frontier.
- Theorem 4: absence of every fixed bounded degree above the source `+1/2` frontier.
- Theorem 5: absence of components from `ceil(8.24/t)` through `n/2` for `k=floor(t log n)`.
- Theorem 6: connectivity with high probability above the source `+1/2` frontier.

Fresh bounded web searches for the exact title, DOI, authors, `bilateral preference random graphs`, Poisson isolated vertices, and 2026 connectivity follow-ups recovered the Cambridge paper and current bibliographic records but no later source-matching constant-window connectivity/Poisson theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. Exact problem for this run

Claims 309--310 already separate the fixed-root interaction proof into deterministic support deletion plus probability costs. The remaining audit question is whether the deletion/charging process itself has an order-independent invariant and whether the repeatedly used statement

`number of witness-labelled skeletons at complexity K = k^{O(K)}`

can be replaced by a literal finite algorithm and an explicit count.

The danger is real: if one greedily charges only the first low nonexternal edge that deletes a deadline, the number of charged edges can depend on processing order. For example, if one retained deadline is contaminated by two distinct low support edges `e_1,e_2`, processing `e_1` first deletes the deadline and a naive implementation may never “see” `e_2`; reversing the order gives a different encountered edge. Thus **greedy encountered charge is not the invariant**.

The correct invariant is the complete incidence support present **before** active-edge deletion.

---

## 3. Canonical data after root merge and collision pruning

Fix `r` distinguished roots

`R={v_1,...,v_r}`

with `r` fixed as `n->infinity`. Delete all root--root edges. At root `a`, write the outside raw weights in increasing order

`x_{a,1}<...<x_{a,n-r}`

and let `u_{a,j}` be the outside endpoint of `x_{a,j}`. For `j<=k`, define the proposal occurrence

`alpha=(a,j)`, label `s(alpha)=u_{a,j}`, deadline `D_alpha=x_{a,j}`,

and terminal outside threshold `T_a=x_{a,k}`.

Let `Omega=[r] x [k]` denote the `rk` deleted-array proposal occurrences. With continuous raw weights, all relevant comparisons are strict almost surely; the null tie event may be discarded.

### 3.1 Canonical root activity

For a root--root edge `e={v_a,v_b}`, record the endpoint-activity marks

`(e,a) active iff W(e)<=T_a`,

`(e,b) active iff W(e)<=T_b`.

Let `A_R^end` be this marked endpoint-active set, let `A_R` be its underlying set of unique root--root raw edges, and put

`p=|A_R|`,

`d_a=#{e incident to v_a : (e,a) in A_R^end}`.

Claim 309/310 gives the deterministic safe root suffix omission

`O_R(a)={k-d_a+1,...,k}`.

The exact final number of root edges occupying the top `k` can be strictly smaller than `d_a`; the previous report's `k=2`, outside `0.1,0.4`, root edges `0.2,0.3` example has `q_a^*=1<d_a=2`. We deliberately retain the safe `d_a` over-omission.

### 3.2 Canonical collision partition

Partition `Omega` by equal outside label. Call the partition `pi`. If it has `m` blocks, define its collision excess

`c=rk-m`.

For each block `B`, let `alpha_B` be the occurrence in `B` with the globally smallest proposal deadline. Apply the Claim-310 rule:

- if `alpha_B` lies in the root suffix omission `O_R`, omit **all** of `B`;
- otherwise retain exactly `alpha_B` and omit `B\{alpha_B}`.

There is never promotion to a later occurrence if the global minimum was already omitted.

Let `L_0` be the resulting set of preliminarily retained occurrences and let

`S={s(alpha): alpha in Omega}`

be the set of **all** outside proposal labels, retained or not. Put

`E=V\(R union S)`.

---

## 4. #12 FIND WHAT IS CONSERVED — the incidence invariant

### Lemma 311.1 — canonical support-incidence invariant

For the tie-free realization above, define a finite bipartite incidence graph `Gamma_0` as follows.

- Left vertices are the preliminarily retained deadlines `alpha in L_0`.
- Right vertices are unique raw nonexternal edges `e={u,y}` with `u=s(alpha)` for at least one `alpha in L_0` and `y in (R union S)\{u}`.
- Put an incidence `alpha ~ e` exactly when `e` is incident to `u=s(alpha)` and

  `W(e)<D_alpha`.

The proposal edge defining `D_alpha` never creates a strict self-incidence because its weight equals `D_alpha`. Other root-to-the-same-label proposal edges in a collision block are at least as heavy as the globally retained minimum and therefore also create no forbidden same-block lighter incidence.

Let

`H={right vertices e of Gamma_0 with degree >=1}`

and

`q=|H|`.

Define the final active-edge omission set

`O_A=N_{Gamma_0}(H)`

and final retained set

`L_infty=L_0\O_A`.

Then:

1. `Gamma_0`, `H`, `q`, and `O_A` are uniquely determined by the raw realization after the canonical root/collision preprocessing.
2. Processing contaminated deadlines and active support edges in any order yields the same safe final retained set `L_infty` provided no deleted occurrence is ever promoted.
3. Every lighter competitor of a surviving retained deadline `alpha in L_infty` has its other endpoint in `E`.
4. The canonical complexity

   `K=c+p+q`

   is deletion-order independent.

#### Proof

All deadlines in `L_0`, all raw nonexternal edge weights, and all strict inequalities `W(e)<D_alpha` are fixed before active-edge deletion. Thus the full incidence graph `Gamma_0` is fixed.

Deleting a contaminated deadline removes a **left vertex** from this fixed graph; it cannot create a new incidence because neither any edge weight nor any surviving deadline changes. Therefore every deadline that is ever eligible for active-edge deletion is already in the fixed neighborhood `N(H)`. Conversely every deadline in `N(H)` is contaminated by at least one actual low nonexternal raw edge and is deleted by the stated rule. Hence the safe final set is exactly `L_0\N(H)`, independent of processing order.

If `alpha in L_infty` and a lighter competitor edge `e={s(alpha),y}` had `y in R union S`, then by definition `alpha~e` in `Gamma_0`, forcing `alpha in N(H)`, contradiction. Hence every surviving lighter competitor has `y in E`.

Finally `c` is fixed by the label partition, `p` by the endpoint-active root-edge family, and `q=|H|` by the complete predeletion incidence graph. Thus `K=c+p+q` is canonical and order independent. `square`

### 4.1 What is *not* conserved

The number of active support edges **encountered by a greedy deletion routine** is not invariant. One deadline with two incident edges already gives a counterexample: deleting the deadline after seeing the first edge can hide the second from a lazy routine. Likewise a minimal hitting set of contaminated deadlines need not be unique.

This run therefore deliberately does **not** define `q` as a minimum cover or as a first-seen count. It defines `q` as the number of all unique raw support edges that are genuinely low relative to at least one preliminary retained deadline. That exhaustive support charge is canonical, and overcharging only helps the probability estimate because every charged edge really occurred as a separate rare raw-edge event.

### 4.2 One-pass closure

An additional simplification follows: after root suffixes and collision minima are fixed, the active-edge “closure” is actually one pass. There is no recursive discovery mechanism. The fixed graph `Gamma_0` already contains every nonexternal lighter relation. Removing `N(H)` cannot create a new one. Thus Claims 302/304/310 should be read with a **canonical support incidence pass**, not an order-sensitive recursive exploration.

---

## 5. #19 MAKE IT AN ALGORITHM — canonical skeleton map

### Algorithm `CANONICAL_P0456_SKELETON(r,k,W)`

Input: a tie-free raw edge-weight realization `W` and fixed root tuple `R=(v_1,...,v_r)`.

**Step 1 — delete root--root edges.**  
For every root `a`, sort its outside incident edges and record `(u_{a,j},D_{a,j})` for `1<=j<=k`, plus `T_a=D_{a,k}`.

**Step 2 — label partition.**  
Partition the `rk` occurrences by equal outside label. Record `pi` and `c=rk-|pi|`.

**Step 3 — endpoint-active root edges.**  
For every root--root raw edge `e={v_a,v_b}`, record independently whether `W(e)<=T_a` and/or `W(e)<=T_b`. Let `A_R^end` be the marked pattern, let `A_R` be its unique underlying raw edges, set `p=|A_R|`, and compute each `d_a`.

**Step 4 — root suffix deletion.**  
At root `a`, omit ranks `k-d_a+1,...,k`.

**Step 5 — collision canonicalization.**  
For each label block, locate its unique global minimum deadline. If that minimum is already suffix-omitted, omit the whole block. Otherwise retain exactly that minimum and omit every other occurrence. This produces `L_0`.

**Step 6 — build the full support incidence graph.**  
Let `S` be all proposal labels and `E=V\(R union S)`. For each retained occurrence `alpha in L_0` with label `u`, inspect every raw edge `{u,y}` with `y in (R union S)\{u}`. Insert the unique raw edge as a right vertex of `Gamma_0` and the incidence `alpha~e` exactly when `W(e)<D_alpha`. Let `H` be the set of right vertices of positive degree and set `q=|H|`.

**Step 7 — delete all contaminated deadlines simultaneously.**  
Set `L_infty=L_0\N(H)`. Do not promote any omitted collision occurrence.

**Step 8 — emit residual blocks.**  
For each surviving selected label `u=s(alpha)`, emit

`B_u={{u,x}: x in E}`.

Output the canonical skeleton

`Sigma=(pi,A_R^end,Gamma_0|_{L_0 x H},L_infty)`

and complexity `K=c+p+q`.

### Proposition 311.2 — correctness of the algorithm

For every tie-free realization:

- the output is unique; no arbitrary tie-breaking occurs;
- Claims 309 and 310 imply that every nonomitted outside proposal rank remains available after root-edge reinsertion;
- Claim 310's global-minimum collision rule removes every possible same-label hidden lighter competitor;
- Lemma 311.1 removes every remaining low competitor whose other endpoint lies in `R union S`;
- therefore every residual rejection event is measurable only with respect to the external block `B_u`;
- for distinct surviving labels `u!=w`, the blocks `B_u` and `B_w` are disjoint because `w in S`, hence the edge `{u,w}` is excluded from both external blocks;
- all `B_u` are also disjoint from root proposal edges, root--root edges, and the integrated support edges in `H`.

Thus residual rejection randomness is **exactly independent across the surviving selected-label blocks** after conditioning on the exposed root proposal arrays and the charged finite skeleton.

This remains an upper-bound support algorithm, not an equivalence for joint isolation: bilateral-failure conditions on root--root edges that actually enter final root lists may be dropped for the upper bound. The lower bound remains Claim 306's clean sufficient event with late root--root edges.

---

## 6. #28 REPLACE FOR ALL WITH FOR TYPICAL — uniqueness is stronger than needed

The intended test was whether only a typical interaction realization admits a canonical minimal representation, or whether bounded-multiplicity cover control is enough. The result is stronger:

> **Every tie-free realization has one canonical exhaustive skeleton.**

The exceptional tie family has probability zero because all raw weights are continuous. No `o(e^{-rk})` exceptional family is needed for canonicalization.

Minimality is neither true nor required. A deadline can be incident to several low support edges, and a minimum hitting set need not be unique. The exhaustive `H` records all of them. What matters for the union bound is that the number of possible canonical patterns of complexity `K` is only `k^{O_r(K)}` and every charged raw edge contributes its own codimension.

The next subsection makes this literal.

---

## 7. Explicit skeleton count and codimension

Let `N=n-r` and `M_0=rk` be the number of proposal occurrences.

### Lemma 311.3 — collision-pattern count

The number of partitions of `M_0` occurrence positions with collision excess exactly `c` is at most

`M_0^{2c}`.

#### Proof

Fix once and for all an ordering of the `M_0` occurrence positions. In each collision block, mark its first position as leader. There are exactly `c` nonleaders. Choose their positions in at most `M_0^c` ways and, for each nonleader, record its block leader in at most `M_0` ways. This over-encodes partitions but gives at most `M_0^{2c}` possibilities. `square`

For a feasible fixed partition `pi` with `m=M_0-c` blocks, the ordered proposal-label arrays at different roots are independent uniform injections into the same outside pool. Hence the exact partition probability is

`P(pi)=(N)_m/(N)_k^r`.

Uniformly for `k=O(log n)`,

`P(pi) <= N^{-c}(N/(N-k))^{rk} = n^{-c} exp(O_r(k^2/n)) = n^{-c+o(1)}`.

This is the exact codimension `c` of the label equalities.

### Lemma 311.4 — active-root and support-pattern counts

For fixed `r`:

- the marked endpoint-active root-edge pattern has only `O_r(1)` possibilities; a pattern containing `p` unique active root--root raw edges costs at most `(C_r k/n)^p` on the standard threshold guard;
- after collision canonicalization, `|S|<=rk`, so there are at most

  `|S|(|R|+|S|) <= C_r k^2`

  possible unique nonexternal support raw edges touching a retained selected label;
- choosing `q` such edges and their one- or two-deadline incidence pattern has at most `(C_r k^2)^q` possibilities;
- conditional on the exposed proposal arrays, each distinct charged support raw edge costs at most `C_r k/n` on the threshold guard.

#### Proof of the probability statement

A selected-label--selected-label support edge is a raw Uniform`[0,1]` edge independent of all root proposal arrays, so being below an `O(k/n)` retained deadline costs `O(k/n)`.

If a support edge joins a selected label `u` to a root `v_b` that did not select `u`, then conditional on the exposed root-`b` top-`k` array and terminal threshold `T_b=t`, its raw value is exactly Uniform`[t,1]`. Thus falling below another guarded deadline `D=O(k/n)` costs

`(D-t)_+/(1-t)=O(k/n)`.

Distinct named nonselected tail edges remain conditionally independent after the full root proposal arrays are exposed. Root--root weights and selected-label--selected-label weights are disjoint raw families. Hence each **unique** charged raw edge contributes its cost once even if it contaminates two deadlines. `square`

### Corollary 311.5 — explicit `k^{O(K)}` bound and high-complexity tail

For fixed `r`, the total number of abstract canonical skeleton patterns with complexity

`K=c+p+q`

is at most

`(C_r k^2)^K`.

Moreover, on the standard threshold guard, the total probability of canonical skeletons with complexity at least a fixed integer `D` is bounded by

`sum_{K>=D} (C_r k^3/n)^K = n^{-D+o(1)}`.

#### Proof

Combine Lemmas 311.3--311.4. The collision part contributes at most `k^{2c} n^{-c+o(1)}`; root activity contributes a constant pattern factor and `(C_r k/n)^p`; support activity contributes at most `k^{2q}(C_r k/n)^q`. Bound every per-unit factor by `C_r k^3/n`. Since `k=log n+O(1)`, the ratio tends to zero and the tail is geometric. `square`

This is the promised literal replacement for the previous prose `k^{O(K)}=n^{o(1)}` statement.

---

## 8. Consequence for the fixed-r joint-isolation proof

Choose once and for all

`D=r+1`.

### High complexity

By Corollary 311.5 and the inherited threshold-guard failure bound,

`P(K>=D)=n^{-r-1+o(1)}=o(e^{-rk})`

uniformly on `|k-log n|<=C`, because `e^{-rk}=n^{-r}e^{O_r(1)}`.

### Low positive complexity

For `1<=K<D`, all omissions are bounded in terms of `r,D`:

- root suffix omissions contribute at most `sum_a d_a <=2p`;
- collision canonicalization contributes `O(c+p)` omitted occurrences (if a collision minimum was already root-omitted, the whole block is removed but the extra root omission is already represented in `p`);
- every support edge contaminates at most two retained selected-label deadlines, so active support deletion contributes at most `2q` more omissions.

Thus Claim 303 applies with one fixed omission constant `M=M(r,D)`. Conditional on a low-complexity canonical skeleton, the residual external blocks are exactly disjoint by Proposition 311.2, and Claim 303 gives

`P(residual necessary rejections | skeleton)
 <= exp[-rk + O_{C,r,D}(k^(2/3)+log k)]`.

Summing over all positive low-complexity canonical patterns yields

`exp[-rk+o(k)] * O(C_r k^3/n)=o(e^{-rk})`.

Therefore all positive interaction complexity contributes `o(e^{-rk})` exactly as required by Claims 301/304, now with a canonical skeleton map and explicit counting proof.

The zero-complexity branch remains the clean branch from Claims 306/308. Claim 308 gives the clean one-root marked saddle at the actual quota `h=k` with relative error tending to zero; Claim 306's asymmetric lower construction uses distinct labels, late root--root edges, and fully external rejection witnesses. Consequently the repaired fixed-r statement remains

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`

for every fixed `r`, uniformly on `|k-log n|<=C`.

No first/second correction coefficient is used here.

---

## 9. Poisson and connectivity implications remain unchanged

Let

`Z_n=sum_v I_v`, `lambda_n=n e^{-k}`.

The fixed-r result gives every fixed factorial moment

`E[(Z_n)_r]=lambda_n^r+o_C(1)`.

Claim 305's **finite Brun/Bonferroni inequality** remains the sole total-variation conversion, so

`d_TV(Law(Z_n),Poisson(lambda_n))->0`

uniformly on every fixed `|k-log n|<=C` window. No subsequence/Scheffe argument and no unchecked black-box Poisson theorem is reintroduced.

The component elimination layer is unchanged and was rechecked under the literal LK definition:

- sizes `2--6`: delete internal candidate-component edges before external proposal ranking; the internal spanning-tree raw weights and external rejection raw weights are then disjoint and independent;
- sizes `7--12`: use the fixed-size part of the single global two-sided kth-threshold envelope;
- sizes `13--n/2`: use the geometric tail from the same envelope;
- the global envelope failure probability is paid once.

No connectivity inference is made from mean degree.

Hence the internally candidate-complete source statement remains

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`

on fixed `C` windows, and if `k-log n->c` this tends to `exp(-e^{-c})`.

This is still **AUDITS-PENDING**, not source CLOSED.

---

## 10. Failure analysis and why this run matters

### #12 — useful, with a negative sub-result

The conserved object is the complete support-incidence graph after canonical root/collision preprocessing. The canonical exhaustive charge `q=|H|` and total `K=c+p+q` are invariant. A greedy first-seen charge count or a minimal hitting-set size is **not** invariant.

### #19 — useful

Claims 309--310 are now an explicit finite algorithm with no arbitrary choices on the probability-one tie-free event. The omission set and residual blocks are functions of the raw realization.

### #28 — stronger than requested

No merely “typical” representation is needed. Every tie-free realization has a unique canonical exhaustive skeleton. The relaxed cylinder events used to upper-bound exact skeleton probabilities may overlap, but the number of abstract patterns at complexity `K` is at most `(C_r k^2)^K`; their total probability is already geometrically summable. Thus multiplicity cannot outrun the existing `k^{O(K)}` budget.

### Historical failures preserved

- Claim 309's explicit `r=3` counterconfiguration remains mandatory: a root--root edge below both deleted-array kth thresholds need not survive bilaterally after multiple root-edge insertions.
- Claim 310's `q_a^*<d_a` example remains mandatory: endpoint-active count is a safe suffix bound, not the exact final root occupancy.
- The global-minimum collision rule remains mandatory: if the minimum occurrence of a repeated label is omitted, later occurrences are not promoted.

No future simplification should erase these counterexamples.

---

## 11. Claim ledger delta

Preserved without downgrade:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains PPP.
- Claims 291--300 remain supporting self-audit/strengthening kernels.
- Claim 301 remains proved only with Claims 302--311.
- Claim 302 and Claim 304 retain the explicit Claim-309 root-merge repair.
- Claim 308 remains the clean one-root analytic input at actual quota `h=k`.
- Claim 309 remains the root-merge sigma-field repair.
- Claim 310 remains the sequential merge/support-deletion simplification.

New:

### Claim `P03-P0456-CANONICAL-INCIDENCE-SKELETON-311`

**Status:** `PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

**Statement.** For every fixed root count `r`, on the probability-one event of distinct raw weights, Claims 309--310 admit a unique canonical finite skeleton obtained by: endpoint-active root-edge marking; safe root suffix omission; global-minimum collision canonicalization; construction of the complete nonexternal support-incidence graph; simultaneous deletion of all contaminated deadlines; and emission of disjoint external selected-label blocks. The canonical complexity `K=c+p+q` is deletion-order independent. The number of abstract skeleton patterns of complexity `K` is at most `(C_r k^2)^K`, and on the standard threshold guard their total probability for `K>=D` is `n^{-D+o(1)}` for every fixed `D`. Hence positive-complexity fixed-root interaction mass remains `o(e^{-rk})` after Claim 303 residual rejection bounds.

This is a self-audit/supporting theorem. It does not count as either required outside audit.

---

## 12. Exact remaining obligation and next state

The mathematical source chain is internally candidate-complete but externally unaudited. The exact remaining closure obligation is unchanged:

1. a genuine P26 end-to-end audit of the repaired source-matching chain, including Claims 305, 306, 308, 309--311 and the literal component elimination;
2. one genuinely distinct OTHER-track end-to-end audit of the same repaired chain;
3. only after both PASS results exist may the final self-contained source-matching paper folder be created and P26 closure requested through `ledger_delta`.

No P03 self-check counts toward either slot.

Current protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_311_CANONICAL_INCIDENCE_READY`.

### `ledger_delta` for P26

```yaml
ledger_delta:
  target: P0456
  owner: P03
  source_closed: false
  outside_full_proof_audits: 0/2
  closure_request: NONE
  metric:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    hard_recoveries: 0/2
  new_supporting_claim:
    id: P03-P0456-CANONICAL-INCIDENCE-SKELETON-311
    status: PROVED_SELF_AUDIT_SUPPORT_AUDITS_PENDING
  required_audit_focus:
    - preserve Claim-309 r>=3 root-merge counterexample
    - verify Claim-311 canonical incidence graph and k^{O(K)} count
    - verify Claim-308 clean h=k saddle
    - verify Claim-305 finite Brun TV conversion
    - verify literal sizes-2--6 and sizes-7+ component elimination
  shared_root_ledger_edit_by_P03: false
```

---

## 13. Next-run handoff

Audit-first remains dominant. If no outside audit arrives, the next useful proof attack should not return to correction coefficients. Suggested nonconsecutive Section-B triple:

**#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #22 READ THE FAILURES, NOT THE SUCCESSES.**

Concrete agenda:

1. First read every new P26/OTHER P0456 audit; repair any stated gap before anything else.
2. #3: package Claims 305/306/308/309--311 plus the component lemma into one auditor-facing theorem with a dependency DAG and no references to obsolete correction claims.
3. #14: quotient the fixed-root skeleton enumeration by permutations of roots and proposal ranks **only if** this reduces audit surface without changing the canonical map; do not use symmetry to hide deterministic root labels.
4. #22: compare the package against the source's exact Lemmas 10--14 failure modes and list precisely which source bad events are absorbed by `c`, `p`, and `q`. Any source-type bad event not represented by one of those charges is a real gap and must downgrade immediately.
5. Freshly repeat source/literature screening. A bounded search miss remains non-certifying.
6. Recheck nontrivial components under literal LK; never infer connectivity from mean degree.

---

## 14. Model / tool limits

The runtime identifies the model as **GPT-5.6 Sol**. Reasoning level is not exposed and is therefore **UNVERIFIED**. This is not GPT-6 at maximum. The exposed scheduler update surface still provides title, prompt, schedule, timing mode, and enablement, but no binding model-selector or reasoning-effort field. `GPT-6 / maximum` therefore remains prompt-only in this context. Changing that requires an owning product/admin/support context that exposes such controls; duplicating schedules or bypassing permissions is not an acceptable workaround.

GitHub only was used for repository continuity and delivery. No Gmail/email, Drive, public posting, paid compute, access changes, unreviewed external scripts, workflow execution, or additional schedules were used.

**End of complete run report.**