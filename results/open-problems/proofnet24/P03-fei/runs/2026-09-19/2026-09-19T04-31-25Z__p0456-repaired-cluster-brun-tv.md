Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #22 READ THE FAILURES, NOT THE SUCCESSES**. The main result is a single finite repaired-cluster lemma that subsumes Claims 302--303 for the fixed-root interaction proof, plus a self-contained Brun/Bonferroni argument upgrading the all-fixed-factorial-moment statement to uniform total-variation Poisson convergence without the previous subsequence/Scheffe step.

# P03 / P0456 run report — repaired cluster lemma and direct Brun total variation

Run timestamp: **2026-09-19T04:31:25Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T03-28-43Z__p0456-uniform-bounded-omission-saddle.md`,

creation commit `e2b353ef99903c46c07ba71814dc34e6be130a36`, blob `2f9f1cccbdf6783625b6e4a68a1e429c8a260918`; exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--303. Claim 301 remains valid only with Claim 302's minimum-deadline collision repair and Claim 303's arbitrary-rank bounded-omission saddle. This run adds Claim 304 below.

Before the main attack I reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, the current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical P0456 claim, Claims 301--303 at their exact paths/creation commits, the current P26 directory/newest P26 report, and neighboring P0457 only for nonduplication. Large root/policy/campaign surfaces rendered by the connector are truncated, so I do not represent those reads as byte-for-byte whole-file rereads; exact-path and targeted reads/searches were used for the controlling instructions and target state.

### 1.1 Incoming outside-audit screen

A newer P26 report than the one named in the incoming handoff is now present:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_06-59-00__run-report.md`,

creation commit `2e97642f918ed90b6985e3626239ad25ab34af01`, blob `5ace0bae51f531681f4597c80eaa8f2603982e31`.

It audits **P04/I0101/p=257 degree-aware dual**, not P0456. Fresh exact-string repository searches for Claims 301 and 303 still recover only P03 reports; I found no P26 or genuinely distinct OTHER-track end-to-end audit of the repaired P0456 chain. P04 remains rotation-stopped/disabled; the newest P26 report confirms that state while auditing a historical finite claim. There is no new P04 successor theorem for the directed P03->P04 duty, so I do not fabricate a repeat audit.

Thus the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper folder are created.

### 1.2 Fresh primary-source and current-literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies Section 1.1: the authors state that connectivity is not known throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and attribute the gap to analytically simpler sufficient conditions, specifically including the no-intersection condition in their isolated-vertex argument; they explicitly say a more elaborate or exact set of sufficient conditions could close the gap. Lemma 10 still gives the source bad-interaction estimate `P(B)=O(k^3/n)`, Theorem 3 the lower disconnectedness regime, and Theorem 6 the upper connectivity regime.

Fresh bounded searches for the exact DOI/title/authors and for 2026 bilateral-preference connectivity, isolated-vertex and Poisson updates recovered the Cambridge paper, bibliographic mirrors, and author records, but no later source-matching constant-window or isolated-vertex Poisson theorem. This is dated bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

Neighboring P0457 remains a distinct diameter problem under its own ownership/rotation history; it is not duplicated here.

---

## 2. #3 PROVE SOMETHING STRONGER — one repaired finite cluster lemma

Claims 302 and 303 can be combined into one finite hypothesis/conclusion package. The purpose is not a new source theorem; it is to remove prose-level dependencies from the fixed-root interaction proof.

### Claim `P03-P0456-REPAIRED-CLUSTER-BRUN-TV-304`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix finite `C,r,M`. Let `|k-log n|<=C`. Consider `r` distinguished roots. After deleting the finitely many root--root edges (or, in the small-component application, all internal root-set edges), expose for root `a` the first

`p_a = k + O_M(1)`

proposal slots into a common outside pool of size `n-O_r(1)`. A **repaired finite cluster datum** consists of the following explicit objects.

1. A partition `pi` of all proposal slots into equal-label blocks, with no two slots of the same root in one block. If `m(pi)` is the number of blocks, set

   `c = sum_a p_a - m(pi)`.

2. In each block, the occurrence having the **minimum proposal deadline** is the only retained representative; every other deadline in that block belongs to the omission set `O`.

3. A list `A` of unique active raw edges between retained selected labels, or between a retained selected label and another root which does not select that label. Every retained deadline below which an edge of `A` can act as a competitor is placed in `O`. Put `q=|A|`.

4. An endpoint-early pattern for the deleted root--root edges. If one such edge is early at both endpoints, the joint-isolation branch is declared impossible. Otherwise each edge early at exactly one endpoint is charged once and the displaced terminal proposal deadline is placed in `O`. Put `p` equal to their number.

5. For every retained deadline, an outside-competitor quota `h_i` satisfying `k-M<=h_i<=k+M`.

Write

`K=c+q+p`.

Assume `K` and `|O|` are bounded by constants depending only on `r,M`. On the root-threshold guard `G_L` where all relevant terminal proposal thresholds are at most `Lk/n`, with fixed `L`, the following hold.

**(A) Skeleton cost.** Every prescribed witness-labelled cluster datum of complexity `K` has probability

`<= n^{-K+o(1)}`,

and the number of witness-labelled data of any fixed complexity is `k^{O_{r,M,K}(1)}=n^{o(1)}`.

**(B) Exact residual dissociation.** Let `S` be the set of selected nonroot labels and `E=V\(R union S)`. After the stated minimum-deadline retention and omissions, every raw edge which can be a lighter competitor for a surviving deadline attached to label `u` is of the form `{u,x}` with `x in E`. Hence for distinct retained labels `u != z`, the residual raw-edge families

`{{u,x}:x in E}` and `{{z,x}:x in E}`

are disjoint. They are also disjoint from every root proposal array and from the already integrated active edges.

**(C) Uniform rejection cost.** Conditional on the complete cluster datum and proposal-value arrays, after active-edge factors are paid pointwise, Claim 303 applies root by root. Therefore

`P(all residual rejections | cluster datum,G_L)`
` <= exp[-r k + O_{C,r,M}(k^(2/3)+log k)].`                 (2.1)

In particular, every positive-complexity fixed cluster contributes `o(e^-rk)`, and the union of all positive-complexity clusters contributes `o(e^-rk)`.

**(D) Zero cluster.** The zero-complexity branch has clean rejection probability `e^-rk(1+o_C(1))`; moreover the total joint-isolation probability is

`P(I_{v_1}=...=I_{v_r}=1)=e^-rk(1+o_C(1))`                 (2.2)

uniformly for every fixed `r,C`.

### Proof

#### 2.1 Skeleton cost is purely finite

For a fixed equality partition `pi`, the ordered label arrays are independent injections into the common outside pool. If `m=m(pi)`, its exact probability is

`(N)_m / product_a (N)_{p_a}`,

so for fixed collision excess `c=sum p_a-m` it is `n^{-c+o(1)}`. A multiway block of size `s` contributes exactly `s-1` to `c`.

On `G_L`, every applicable proposal deadline is `O_L(k/n)`. A prescribed selected--selected active edge has probability `O_L(k/n)`. If `u` is selected by root `a` but is absent from the exposed proposal list of root `b`, then conditional on root `b`'s terminal exposed threshold `T_b=t`, exchangeability gives the exact law

`W(v_b,u) | (u absent from b's exposed list,T_b=t) ~ Uniform[t,1]`.

Thus for every applicable deadline `D<=Lk/n`,

`P(W(v_b,u)<=D | T_b=t,u absent)=((D-t)_+)/(1-t)=O_L(k/n)`

pointwise in the threshold. This formulation also covers the small-component application where `p_b=k-(r-1)`: “absent” means absent from those first `p_b` external slots, not absent from all first `k` incident edges.

A deleted root--root edge is early at a specified endpoint with probability `O_L(k/n)`. If early at both endpoints it is selected by both roots and survives bilaterally, so the joint-isolation branch has probability zero. Multiplying the exact collision cost and the pointwise active-edge/root-edge costs gives `n^{-K+o(1)}`. Choosing witnesses among `O_r(k)` slots and `O_r(k^2)` possible local pairs contributes only `k^{O(K)}=n^{o(1)}`.

#### 2.2 Minimum-deadline retention makes the residual partition literal

Fix a repeated-label block and retain its minimum proposal deadline `D_min`. Every other root-to-that-label edge in the block is at least `D_min`, so it cannot be a lighter competitor in the retained test. This is exactly the Claim-302 repair.

For two distinct retained labels, their only shared one-star raw edge is the selected--selected edge joining them. If it lies below either relevant deadline, it is listed in `A` and every deadline it can contaminate is omitted. Likewise, a selected-label/root edge is either in the same collision block and therefore too heavy for the retained minimum, or belongs to `A` if it lies below a surviving deadline. One-end-early root--root edges only displace boundedly many terminal proposal slots; those deadlines are omitted.

Consequently a surviving deadline attached to `u` has no lighter competitor whose other endpoint lies in `R union S`. Every remaining candidate competitor is `{u,x}` with `x in E`. Different retained labels give disjoint undirected edge sets. This proves (B), with no probabilistic approximation.

#### 2.3 Claim 303 applies after, not before, active-edge integration

Active edges are first integrated out using their pointwise `O(k/n)` factors. Conditional on the resulting fixed skeleton and on the label partition, the proposal-value arrays of different roots are independent: raw root incident edge sets are disjoint after the temporary root--root deletion, and ordered labels are independent of ordered values by iid exchangeability. The residual competitor blocks are disjoint from those arrays and from one another by 2.2.

For each root, the number of omitted deadlines and the quota shifts are bounded, while the exposed slot count is `k+O(1)`. Claim 303 therefore gives

`exp[-k+O(k^(2/3)+log k)]`

for that root, uniformly over the actual omission ranks. Exact block disjointness permits multiplication across roots, proving (2.1).

For `1<=K<D_0`, summing the `n^{o(1)}` witness choices gives

`e^-rk * n^{-K+o(1)}`

up to the `exp[O(k^(2/3))]=n^{o(1)}` factor, hence `o(e^-rk)`. Choose fixed `D_0>r+2`. The same sequential exposure gives

`P(G_L,K>=D_0)<=n^{-D_0+o(1)}=o(e^-rk)`.

Finally choose `L` with `L-1-log L>r+D_0+3`; then the root-threshold Chernoff bound gives `P(G_L^c)=o(e^-rk n^-D_0)`. Thus every nonzero or unguarded branch is negligible at the joint-isolation scale.

#### 2.4 Zero-cluster upper and lower bounds

On `K=0`, all exposed labels are distinct, no local active edge can help before a retained deadline, and root--root edges do not alter the exposed arrays. Joint isolation therefore forces the clean outside rejection event. The clean marked-saddle lemma gives

`P(all roots isolated,K=0)<=e^-rk(1+o_C(1)).`                (2.3)

For the lower bound, impose a sufficient event rather than guessing independence under isolation:

- all proposal labels are distinct;
- every deleted root--root edge is later than `Lk/n`;
- `G_L` holds;
- every exposed selected neighbor has `k` lighter competitors in the external pool `E`.

The last condition is sufficient for rejection regardless of any omitted/internal competitors. The external blocks are disjoint. For each root its probability is `e^-k(1+o_C(1))`. Label distinctness costs `1-O_r(k^2/n)` and root--root lateness costs `1-O_r(k/n)`. The clean rejection event intersected with `G_L` loses at most `P(G_L^c)=o(e^-rk)`. Hence the sufficient event has probability

`e^-rk(1-o_C(1)).`                                           (2.4)

It may contain positive-complexity configurations, but 2.3 already proved that the total positive-complexity joint-isolation mass is `o(e^-rk)`. Subtracting that mass shows the zero cluster itself also has the matching lower bound. Equations (2.3)--(2.4) prove (D) and (2.2). `square`

This is the repaired fixed-root interaction proof in one lemma. It contains the label partition, minimum-deadline rule, active-edge list, omission list, quota vector, probability costs, and exact factorization condition explicitly.

---

## 3. #18 SAY IT IN ANOTHER LANGUAGE — rare clusters, dissociated blocks, factorial cumulants

The repaired proof has a standard probabilistic shape once its model-specific rank bookkeeping is exposed.

### 3.1 Rare dependency clusters

For a fixed tuple of roots, the equality partition plus active local edges is a **dependency cluster**. Its codimension is the integer `K=c+q+p`. The zero cluster factors after the raw one-star blocks are exposed; every positive cluster pays at least one factor `n^{-1+o(1)}` before the common rejection cost.

This is not a sparse dependency graph on the vertex-isolation indicators themselves. Those indicators share raw edges globally, so a naive deterministic dependency graph is essentially complete. The useful sparsity appears only after conditioning on a fixed root tuple and resolving its finite overlap skeleton.

### 3.2 Exact dissociation after cluster surgery

Conditional on a repaired cluster datum, the surviving rejection blocks are stronger than weakly dependent: they are **dissociated at the raw-edge level**, because distinct retained selected labels use disjoint sets `{{u,x}:x in E}`. The cluster lemma therefore implements the pattern

`rare overlap cluster -> charge/delete its support -> exact residual dissociation`.

This is the correct point at which “dissociated blocks” terminology applies; applying it directly to the unconditioned isolation indicators would be false.

### 3.3 Factorial-cumulant translation

Let

`M_j(n)=E[(Z_n)_j]`.

Claim 304 gives, uniformly on every fixed `C` window,

`M_j(n)=lambda_n^j+o_C(1)`                                  (3.1)

for every fixed `j`, because `(n)_j e^{-jk}=lambda_n^j(1+O_j(1/n))` and `lambda_n` stays in `[e^-C,e^C]`.

Define formal factorial cumulants by

`log E[(1+t)^{Z_n}] = sum_{j>=1} kappa_j^F(n) t^j/j!`.

For each fixed order, `kappa_j^F` is a finite polynomial in `M_1,...,M_j`. Substituting (3.1) gives

`kappa_1^F(n)=lambda_n+o_C(1)`,

`kappa_j^F(n)=o_C(1)` for every fixed `j>=2`.                (3.2)

Thus the repaired cluster statement is exactly the usual Poisson signature in factorial-cumulant language: only the first factorial cumulant survives.

### 3.4 Which standard Poisson theorem is actually being invoked?

A fresh literature check recovered B. A. Sevast'yanov's classical paper *Poisson Limit Law for a Scheme of Sums of Dependent Random Variables*, Theory of Probability and Its Applications 17(4), 695--699 (English publication metadata lists 1973), DOI `10.1137/1117082`. It is clearly adjacent in spirit. The accessible current page did not expose the full theorem hypotheses, so I do **not** claim literal verification of Sevast'yanov's black-box assumptions.

Instead, the next section proves the needed Brun/Bonferroni inversion directly. This is shorter than mapping LK onto a generic local-dependence theorem, and it gives the uniform total-variation conclusion with no unverified external hypothesis.

---

## 4. #22 READ THE FAILURES, NOT THE SUCCESSES — direct uniform Brun total variation

The least rechecked logical step in Claim 301 was the passage from all fixed factorial moments to **uniform total variation**. The previous compactness/subsequence/Scheffe argument is correct, but an auditor can avoid all topology by using a finite exact inversion.

### Lemma 4.1 (finite Brun/Bonferroni TV lemma)

Let `X_n` be nonnegative integer-valued, and let `lambda_n` lie in a fixed compact interval `[0,Lambda]`. Suppose for every fixed `m>=1`, uniformly in the parameter family under consideration,

`E[(X_n)_m]=lambda_n^m+o(1)`.                                (4.1)

Then

`d_TV(Law(X_n),Poisson(lambda_n))->0`                        (4.2)

uniformly.

#### Proof

For fixed `j,T>=0`, define

`B_T^X(j)=sum_{t=0}^T (-1)^t E[(X_n)_{j+t}]/(j! t!).`        (4.3)

For a deterministic integer `z>=j`,

`sum_{t=0}^T (-1)^t (z)_{j+t}/(j!t!)`
` = C(z,j) sum_{t=0}^T (-1)^t C(z-j,t).`                    (4.4)

If `z=j` this equals one. If `z>j` and `T<z-j`, the elementary alternating-binomial identity gives

`sum_{t=0}^T (-1)^t C(z-j,t)=(-1)^T C(z-j-1,T)`.             (4.5)

If `T>=z-j`, the full alternating sum is zero. Therefore for every even `T`, after expectation,

`B_{T+1}^X(j) <= P(X_n=j) <= B_T^X(j)`,                      (4.6)

and the width of this exact Bonferroni bracket is

`B_T^X(j)-B_{T+1}^X(j)=E[(X_n)_{j+T+1}]/[j!(T+1)!].`         (4.7)

Apply the same identities to `P_lambda~Poisson(lambda_n)`, whose factorial moments are exactly `lambda_n^m`. For even `T`, equations (4.6)--(4.7) imply

`|P(X_n=j)-P(P_lambda=j)|`
` <= sum_{t=0}^T |E[(X_n)_{j+t}]-lambda_n^(j+t)|/(j!t!)`
`    + max{E[(X_n)_{j+T+1}],lambda_n^(j+T+1)}/[j!(T+1)!].`   (4.8)

Now fix `epsilon>0`. The first moments are uniformly bounded by `Lambda+o(1)`, so choose `J` large enough that both `P(X_n>J)` and `P(P_lambda>J)` are uniformly below `epsilon` by Markov's inequality. Next choose an even `T` so large that

`sup_{0<=j<=J} Lambda^(j+T+1)/[j!(T+1)!] < epsilon`.

For this fixed finite set of moment orders, (4.1) makes every difference in (4.8) uniformly small; the `X_n` bracket width is also below `2epsilon` for large `n`. Summing over `0<=j<=J` and adding the two tails proves (4.2). `square`

Apply Lemma 4.1 with `X_n=Z_n`, `Lambda=e^C`, and (3.1). This proves Claim 301's total-variation statement uniformly on `|k-log n|<=C` directly. No pair-only argument, sparse dependency graph, subsequence extraction, moment-determinacy theorem, or Scheffe step is needed.

This is also the precise standard-language answer: the source proof is a **Brun/factorial-moment Poisson proof with rare dependency clusters**, not a Chen--Stein dependency-graph proof.

---

## 5. #22 continued — sizes 2--6 component argument, including the tail-rank issue

The second least-rechecked step was the small-component argument after deleting internal edges. I tried to break it at the point where only `p_0=k-(s-1)` external proposals per root are exposed.

Fix `s in {2,...,6}` and a candidate component set `S`, `|S|=s`. Delete every edge internal to `S` **before** ranking external proposals. Put

`p_0=k-(s-1)`.

The first `p_0` external proposals from each `v in S` are necessarily among its global first `k` incident edges, because at most `s-1` deleted internal edges can precede them. Hence if `S` is a component, every one of those external proposals must be rejected by its outside endpoint.

A possible hidden issue is that a selected outside label `u` for root `a` may lie at external rank `p_0+1,...,k` for another root `b`; it is then not in the exposed collision partition for `b`. The repaired cluster lemma handles this exactly. Conditional on `u` being absent from **the first `p_0` external labels** of root `b` and on the `p_0`th external threshold `T_b=t`, the raw edge `{v_b,u}` is Uniform[`t`,1]. Since on the global threshold guard `T_b<=Lk/n`, its chance to fall below any applicable exposed deadline is still `O_L(k/n)`. Thus no assumption that `u` is absent from all of root `b`'s first `k` global edges is required.

Now let `G^+` be the global event that every vertex's global `k`th threshold is at most `Lk/n`, choosing fixed `L` with `L-1-log L>2`. Then `P((G^+)^c)=o(1)`. If `S` is a connected component on `G^+`, it contains a spanning tree whose `s-1` internal edges all have weight at most `Lk/n`. For a fixed labelled tree this event has probability at most

`(Lk/n)^(s-1)`.

The tree event uses only internal edges of `S`. The external-proposal rejection event just described uses only raw edges outside the internal edge set, because those internal edges were deleted before proposal ranking. The two events are therefore independent, not merely conditionally comparable.

Claim 304 applied to the `s` roots with `p_a=p_0=k-O_s(1)` gives, after choosing any fixed complexity cutoff `D>=3`,

`P(all exposed external proposals rejected)`
` <= e^{-s k+o(k)} + n^{-D+o(1)}.`                           (5.1)

Summing over sets and Cayley spanning trees,

`P(exists s-component,G^+)`
` <= C_s n^s (Lk/n)^(s-1) [e^{-s k+o(k)}+n^{-3+o(1)}]`
` = n^{1-s+o(1)}k^{s-1}+n^{-2+o(1)}k^{s-1}`
` = o(1).`                                                    (5.2)

Thus the sizes `2,...,6` proof is free of the historical tree-conditioning bias and also free of an unspoken “first `k`” tail-rank assumption.

For sizes `7,...,n/2`, the Claim-301 global two-sided threshold envelope remains unchanged: `a=5/32`, `b=32/5`; the lower and upper Chernoff exponents exceed one; fixed sizes start with exponent `-3/32` at `s=7`; the geometric large-size tail starts with exponent `-1/64` at `s=13`; and the global threshold-failure event is paid once before summing component sizes. No mean-degree inference is used.

---

## 6. Consequences for the source-matching chain

For every fixed `C` and fixed `r`, Claim 304 gives the repaired joint-isolation asymptotic

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`.

Hence the fixed factorial moments satisfy (3.1), and Lemma 4.1 gives

`d_TV(Law(Z_n),Poisson(lambda_n))->0`, `lambda_n=n e^-k`,

uniformly on `|k-log n|<=C`.

The literal component argument in Section 5 plus the preserved global envelope gives

`P(exists nontrivial component)=o_C(1)`.

Therefore

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`

uniformly on every fixed offset window. This is the source-audit capsule conclusion, now with the two most delicate proof-surface points (finite cluster disjointization and uniform TV inversion) stated as standalone lemmas.

Claims 288/289 are unchanged in status: candidate-complete internally, but **AUDITS-PENDING** and publication novelty unverified.

---

## 7. Method outcomes and failed variants

### #3 PROVE SOMETHING STRONGER — SUCCESS

Claims 302 and 303 are now packaged as one repaired cluster lemma which also covers `p_a=k-O(1)` external-proposal lists. Its hypotheses and data are finite and explicit, so an outside auditor does not have to reconstruct which edge is charged or which deadline is omitted from prose.

### #18 SAY IT IN ANOTHER LANGUAGE — SUCCESS, with a boundary

The correct translation is “rare dependency clusters, followed by exact dissociation of residual raw-edge blocks; Poisson via Brun/factorial moments.” The factorial cumulants beyond order one vanish. A generic sparse dependency graph on isolation indicators is still the wrong language. Sevast'yanov's dependent-sum Poisson paper is adjacent methodology, but its full theorem hypotheses were not exposed by the accessible source, so no black-box invocation is claimed.

### #22 READ THE FAILURES, NOT THE SUCCESSES — SUCCESS

Three least-rechecked points were attacked directly:

1. the zero-cluster lower bound was separated into a sufficient external-rejection event and then purified by subtracting the already bounded positive-cluster mass;
2. the sizes-2--6 proof was checked at the `p_0=k-(s-1)` tail-rank boundary, using the exact Uniform[`T`,1] law relative to the **exposed p_0 threshold**;
3. the factorial-moment-to-TV step was replaced by a finite exact Bonferroni inversion.

No downgrade was required.

### Failed/abandoned route

I did not force a Chen--Stein or Sevast'yanov theorem onto the model. Before cluster conditioning, the isolation indicators do not have a useful sparse deterministic dependency neighborhood; after cluster conditioning, the direct factorial-moment calculation is already shorter and stronger for the fixed-window source statement.

---

## 8. Cumulative claim ledger delta

Preserved unchanged:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 marked PPP and Claims 291--300 supporting self-audit/strengthening kernels.
- `P03-P0456-SOURCE-AUDIT-CAPSULE-301 = PROVED / SELF-AUDIT-CAPSULE / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

New:

- `P03-P0456-REPAIRED-CLUSTER-BRUN-TV-304 = PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Claim 304 is a P03 self-audit/packaging strengthening and does not count toward either required outside audit.

All fixed coefficient metrics remain saturated at zero. HARD recoveries remain `0/2`.

---

## 9. Exact remaining obligations and `ledger_delta` for P26

The remaining source-matching obligation is independent verification, not another internal coefficient or correction calculation.

1. P26 must independently audit the repaired chain Claims 288/289/301/302/303/304 end to end.
2. One genuinely distinct OTHER track must independently audit the same source-matching chain.
3. Publication novelty remains unverified; repeated bounded search misses do not become a novelty certificate.
4. Only after both outside PASS audits should the self-contained paper folder be created and closure requested through P26's shared-ledger authority.

Suggested `ledger_delta` for P26 only:

```text
P03 / P0456:
  source_status: OPEN_IN_PRIMARY_SOURCE / SOURCE-MATCHING-CANDIDATE-COMPLETE_INTERNAL
  metrics: c_LK^cert=0, a_LK^fine=0, b_LK^sqrt=0 (SATURATED)
  new_claim: P03-P0456-REPAIRED-CLUSTER-BRUN-TV-304
  claim_301_status: PROVED / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / CLUSTER-TV-PACKAGED-BY-304 / AUDITS-PENDING
  outside_audits: 0/2
  closure: DO_NOT_CLOSE
  paper_package: DO_NOT_CREATE_YET
```

---

## 10. Model control and next state

The exposed scheduler still provides schedule/prompt/timing controls but no model selector or reasoning-effort selector. GPT-6/maximum therefore remains prompt-only. This run actually reports GPT-5.6 Sol; the reasoning level is not exposed and is recorded as UNVERIFIED. Changing the actual runtime model/effort requires platform/product configuration outside this task's exposed controls; no duplicate task or permission bypass is attempted.

Current state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_304_REPAIRED_CLUSTER_BRUN_READY`.

The next run must begin with incoming P26/OTHER audits. If none exists, the useful next attack is **not** another Poisson correction or wider coefficient window: audit the repaired cluster lemma against the exact source sufficient events and produce a line-by-line outside-auditor dependency map, or attempt a direct finite-size error bound only if it shortens the audit surface.

**End of complete run report.**