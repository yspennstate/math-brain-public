Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE**. The strongest new result is a fully conditioned positive-cluster upper lemma: after fixing one canonical interaction skeleton, all codimension variables live in a finite nonexternal raw-edge sigma-field that is disjoint from the residual external rejection blocks, so Claim 313 and Claim 303 glue without conditioning bias. This yields the explicit uniform bound `P(all fixed roots isolated, K>=1)=o(e^{-rk})`.

# P03 / P0456 run report — positive-cluster conditional glue

Run timestamp: **2026-09-19T15:31:14Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, and audit-first screen

The exclusive ownership claim remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run is

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T14-31-19Z__p0456-clean-lower-exact-factorization.md`,

creation commit `8a7cdbb49d7d6fb0b78da6c7a85a51827770e25b`, blob `d23e1d44cb604b832d05eda5e9c728644e291d47`; exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--314. In particular:

- Claim 288 remains `PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 289 remains the repaired fixed-root interaction strengthening.
- Claims 291--300 are historical support only; the auditor-facing fixed-`C` route does not use correction coefficients.
- Claim 303 remains the uniform arbitrary-rank bounded-omission saddle estimate.
- Claim 305 remains the sole finite Brun/Bonferroni total-variation conversion.
- Claim 308 remains the clean one-root marked-saddle input at the actual quota `h=k`.
- Claim 309's `r>=3` root-merge repair remains mandatory; the false shortcut “below both deleted-array kth thresholds implies bilaterally selected” is never restored.
- Claim 310's example `q_a^*<d_a` remains a mandatory guard against interpreting the safe root suffix as exact occupancy.
- Claim 311's canonical incidence graph `Gamma_0` and `K=c+p+q` remain the exhaustive interaction skeleton.
- Claim 312 remains the auditor-facing fixed-`C` dependency DAG and source-failure upper cover.
- Claim 313 remains the exact conditional low-complexity codimension lemma for prescribed `p`/`q` raw edges.
- Claim 314 remains the exact clean lower factorization, independent of Claim 303.

This run reread or exact-path recovered the root `README.md` (current blob `8c3b91a330998e1ee80f2f67186284e5099e003e`), `proofnet24/HOURLY_PROTOCOL_2026-09-15.md` (blob `a5773ae98d59ab7d6420f809452c3b20565c3379`), current `FLEET_RULES.md`, current `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical P0456 claim, the newest complete P03 report, Claim 303 and Claim 313 in full, current task-health evidence, the newest P26 report, and neighboring `operations/claims/P0457.md` only for nonduplication. Large control/root surfaces such as `FLEET_RULES.md`, `OWNER_DIRECTIVE.md`, `POSTED.md`, and `RESULTS.md` are connector-truncated, so this is a targeted current-path reread rather than a claim of byte-for-byte visual recovery of every row. P0457 remains the distinct diameter problem owned by NM13-04.

The exposed scheduler control surface still has no binding model-family selector and no binding reasoning-effort selector. GPT-6/maximum therefore remains prompt-only. The actual runtime available to this report is the model stated in the first line, and reasoning effort is UNVERIFIED.

### 1.1 Incoming outside-audit evidence

The newest P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_18-00-45__run-report.md`,

creation commit `d058ef0854f9ed8b76f807744604213cd7b12d1c`, blob `81083fb3dff5f51bf371b7048dc8b87aa96d570f`.

Its claim is `P26-AUDIT-R04-FM-C2-BLOCK-GOE-70 = PASS_FULL_MATHEMATICAL_PROOF`, reconciling an R04 block-GOE Minami package with an existing R03 audit. It does **not** audit P0456. Fresh repository searches for `P0456 PASS`, `P0456 audit`, the repaired Claim-288/289 chain, and Claims 311--314 still recover no P26 or genuinely distinct OTHER-track end-to-end P0456 PASS. Thus the closure gate remains exactly

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. I do **not** label the source CLOSED and do **not** create the final source-matching paper folder.

---

## 2. Fresh source / status / prior-art check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

The current Cambridge PDF and page images were freshly reopened on 19 September 2026. Section 1.1 still says that it is unknown whether connectivity holds throughout

`log n - (1/2) loglog n sqrt(log n) <= k <= log n + (1/2) loglog n sqrt(log n)`,

and explicitly says that the gap may arise from analytically simpler sufficient conditions, including the no-intersection condition in the isolation argument; the authors say a more elaborate or exact sufficient condition could close the gap. The requested source checkpoints are unchanged: Lemma 10 proves the pair bad-event estimate `P(B)=O(k^3/n)`; Lemmas 11--13 isolate the bad branch and establish exact conditional independence on the source good event; Lemma 14 gives the pair second-moment comparison in the lower regime; Theorem 3 is the `t'<-1/2` disconnectedness theorem; Theorems 4--5 exclude nontrivial component ranges; Theorem 6 is the `t'>1/2` connectivity theorem.

Fresh bounded searches dated 19 September 2026 for the exact DOI/title/authors, bilateral-preference connectivity, isolated-vertex Poisson limits, and 2026 follow-ups recovered the Cambridge publication and current author/bibliographic records but no later source-matching fixed-window connectivity / isolated-vertex Poisson theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 3. Target of this run: the last upper-branch conditioning interface

Claim 314 made the lower fixed-root bound exact. The remaining place an outside auditor could reasonably suspect hidden dependence is the **upper positive-cluster glue**:

1. Claim 313 conditions on the first `k` root proposal arrays and charges a prescribed finite family of active raw edges by `O(k/n)` per unique edge;
2. the canonical algorithm then omits root-suffix, collision, and support-contaminated deadlines;
3. Claim 303 integrates the residual rejection constraints over arbitrary bounded omission ranks.

The question is whether conditioning on the charged codimension events biases the residual raw-edge blocks or the root order-statistic law in a way that invalidates Claim 303.

The answer is no. This run isolates one finite sigma-field that contains **all** nonexternal interaction randomness and proves that the residual rejection blocks are literally disjoint from it. It then performs the charge and saddle integration in the correct order.

---

## 4. #18 SAY IT IN ANOTHER LANGUAGE — a finite generative model

Fix `r,C<infinity`, deterministic distinct roots

`R={v_1,...,v_r}`,

and an integer `k` with `|k-log n|<=C`. Temporarily delete all root--root edges.

For root `v_a`, let

`X_{a,1}<...<X_{a,k}=T_a`

be the first `k` outside order statistics and let `U_{a,j}` be their ordered outside labels. Define

`F_P = sigma((X_{a,j},U_{a,j}) : 1<=a<=r, 1<=j<=k)`.

Let `pi` be the equality partition of the `rk` proposal occurrences by their outside labels. Let `S` be the set of distinct proposal labels and

`E=V \ (R union S)`.

Both `S` and `E` are `F_P`-measurable. Conditional on the equality partition, all ordered proposal **values** retain their ordinary independent root-array law because proposal labels are independent of the ordered values.

### 4.1 The complete nonexternal interaction family

Define the finite raw-edge family

`A(S)`

as the union of

1. all root--root edges `{v_a,v_b}`;
2. all edges `{u,y}` with `u in S` and `y in (R union S)\{u}`.

Some root-to-selected edges in item 2 are already exposed proposal coordinates in `F_P`; the others are named root-tail coordinates. Repetition in the generating list is harmless because the sigma-field is generated by raw edge variables, not by list occurrences.

Now set

`G_* = F_P join sigma(W(e): e in A(S))`.

This is the requested **single finite conditioning sigma-field**. It determines, with probability one under the continuous-weight model:

- the endpoint-active root--root pattern and hence Claim 309's counts `p,d_a` and safe terminal suffixes;
- the equality partition `pi` and collision excess `c`;
- whether the global minimum proposal deadline in each collision block survives the suffix, and hence the preliminary retained set `L_0`;
- every right vertex and every incidence in Claim 311's complete support graph `Gamma_0`;
- the set `H` of positive-degree support raw edges, its size `q`, and the simultaneous deletion `N(H)`;
- the final retained deadline set and therefore the canonical complexity `K=c+p+q`.

There is no iterative discovery of new support edges after deletion: deleting deadlines removes left vertices from `Gamma_0` and cannot create a new strict inequality `W(e)<D`.

### 4.2 The residual family

For each selected label `u in S`, define

`B_u = { W({u,x}) : x in E }`.

Let

`B = union_{u in S} B_u`.

The underlying unordered raw-edge sets `B_u` are pairwise disjoint. Indeed, if `u!=z` and an edge lay in both `B_u` and `B_z`, its other endpoint would have to be the other selected label; but selected labels are in `S`, not in `E`. Moreover, `B` is disjoint from every root proposal edge, every root--root edge, and every edge in `A(S)`.

Since the model starts from independent continuous raw edge weights, **conditional on `G_*`, all coordinates in `B` remain independent Uniform[0,1] variables**. This is literal raw-edge dissociation, not a sparse dependency-graph approximation.

### 4.3 Exact residual rejection event

After the canonical deletion closure, each surviving selected label has at most one retained proposal deadline; call it `D_u`. By construction there is no raw edge from `u` to another vertex of `R union S` strictly lighter than `D_u`. Therefore, if the owner root of `D_u` is isolated, the proposal edge must fail at `u`, and that forces

`#{x in E : W({u,x})<D_u} >= k`.                         (4.1)

There is no quota subtraction here: after support deletion, all strictly lighter nonexternal competitors have been removed along with the deadline they could help reject. Thus the surviving residual quota is exactly `k`. Claim 303 allows bounded quota shifts, but the present glue does not need that extra flexibility.

Conditional on `G_*`, the probability of all residual constraints is therefore the exact product

`product_{u retained} P(Bin(|E|,D_u)>=k)`.                 (4.2)

This finite generative model is the entire upper-branch dependence structure.

---

## 5. Charge variables before the residual saddle

To combine Claim 313 with (4.2), expose the model in two stages rather than conditioning on `G_*` all at once.

### 5.1 Stage 1: proposal arrays

Condition first on `F_P` and on a fixed feasible equality partition `pi`. Let

`G_L = {T_a <= L_r k/n for every a}`,

where for definiteness in this run

`L_r = 8(r+1)`.

The partition event is independent of the proposal values. If its collision excess is `c`, its exact feasible probability is

`(N)_{rk-c}/(N)_k^r`,  `N=n-r`,

and hence is `n^{-c+o(1)}` for fixed `r` and `k=O(log n)`.

### 5.2 Stage 2: a fixed abstract skeleton

Fix one canonical low-complexity skeleton `sigma` compatible with `pi`. It records:

- the `p` unique endpoint-active root--root raw edges and their endpoint-activity orientations;
- the root suffix ranks removed;
- the collision representative in every block (always the global minimum on the exact skeleton event), or the fact that the block is entirely omitted because that minimum was lost to a suffix;
- the `q` unique support raw edges and their incidence orientations;
- the final omission set at every root.

Let `A_sigma` be only the **positive charge conditions** required by this skeleton: the prescribed root edges are endpoint-active where required and the prescribed support edges have the incidences required to contaminate their recorded deadlines. We deliberately drop conditions saying that other candidate support/root edges are inactive; dropping them enlarges the event and is valid for an upper bound.

Claim 313 gives the conditional codimension of `A_sigma` on `F_P` and `G_L`, but it is useful to restate the three raw geometries.

#### Root--root charge

A prescribed root--root edge is independent Uniform[0,1] conditional on `F_P` and is active somewhere only if its weight is at most `max(T_a,T_b)`. Hence it costs at most

`L_r k/n`.                                                   (5.1)

#### Selected--selected support charge

A prescribed edge `{u,z}` between two selected labels is an independent raw Uniform[0,1] variable, disjoint from the root proposal arrays. It has positive incidence only if it is below one of the at-most-two retained endpoint deadlines, hence on `G_L` it costs at most

`L_r k/n`.                                                   (5.2)

#### Selected--nonowner-root support charge

Suppose `{u,v_b}` contaminates a retained deadline `D_u`. If `u` had appeared in root `b`'s first `k` deleted-array proposals, that same raw edge would be a proposal deadline in `u`'s collision block; global-minimum retention would force `W({u,v_b})>=D_u`, so strict contamination would be impossible. Therefore every such support edge is necessarily a **named tail coordinate** absent from root `b`'s exposed prefix.

Conditional on `F_P`, it has the exact law

`Uniform[T_b,1]`.

Thus

`P(W({u,v_b})<D_u | F_P,G_L)`
` = (D_u-T_b)_+/(1-T_b)`
` <= 2 L_r k/n`                                              (5.3)

for all sufficiently large `n`.

Distinct charged raw edges are distinct coordinates. Type-SS variables, root-tail variables, and root--root variables are mutually disjoint raw-edge families. Therefore, for this fixed skeleton,

`P(A_sigma | F_P,G_L) <= (2L_r k/n)^(p+q)`.                 (5.4)

An exact endpoint/incidence orientation can only lower this probability.

---

## 6. The omission count is uniformly bounded by the defect complexity

The canonical algorithm's deletions can be counted without any probabilistic estimate.

1. Collision canonicalization removes exactly `c` nonrepresentative proposal occurrences.
2. Claim 309's root suffixes remove at most

   `sum_a d_a <= 2p`

   occurrences, because a unique active root edge has two endpoints at most.
3. If a suffix removes the global minimum of a collision block, the whole block is omitted. The other occurrences of that block were already among the `c` collision removals, so the loss of the minimum itself is already one of the suffix removals; there is no new unbounded term.
4. Each selected--selected support raw edge can contaminate at most two retained deadlines, one at each selected endpoint. Each selected--root tail support edge can contaminate at most one retained selected-label deadline. Hence simultaneous support deletion removes at most `2q` additional deadlines.

Thus the total number of omitted proposal ranks over all roots is at most

`c + 2p + 2q <= 2K`.                                        (6.1)

For the low-complexity range `K<=r`, this is bounded by a constant depending only on fixed `r`. In particular every root has an arbitrary but bounded omission set, including the possibility that the first or last proposal rank is omitted. This is exactly the quantifier range of Claim 303.

---

## 7. The key conditional-glue lemma

### Claim `P03-P0456-POSITIVE-CLUSTER-CONDITIONAL-GLUE-315`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `r,C<infinity`. Uniformly over integers `|k-log n|<=C` and deterministic distinct roots `R={v_1,...,v_r}`, let `K=c+p+q` be the canonical interaction complexity of Claims 309--313. Then

`P(I_{v_1}=...=I_{v_r}=1, K>=1) = o_C(e^{-rk})`.             (7.1)

More quantitatively, with `L_r=8(r+1)` and `G_L` as above,

`P(I_R=1, 1<=K<=r, G_L)`
` <= exp[-rk + O_{C,r}(k^(2/3)+log k)]`
`    * sum_{K=1}^r (C_r k^3/n)^K,`                           (7.2)

while

`P(K>=r+1,G_L) <= n^{-r-1+o(1)}`                            (7.3)

by Claim 311, and

`P(G_L^c) <= r exp[-49(r+1)k/32] = o(e^{-rk}).`              (7.4)

#### Proof

Fix a low-complexity canonical skeleton `sigma` of complexity `K<=r` and its equality partition `pi`.

On the exact skeleton event, joint isolation implies the residual external constraints (4.1). Therefore

`{I_R=1, sigma, G_L}`

is contained in an enlarged event in which

- the partition `pi` occurs;
- the prescribed positive charge conditions `A_sigma` occur;
- the fixed residual rejection constraints associated with the skeleton's retained ranks occur;
- all exact “no other active support edge” conditions, exact orientation inequalities not needed for positivity, and cross-root comparisons saying that the designated collision representative really is the global minimum are dropped.

Dropping those conditions is legitimate because the exact skeleton event is a subset. Keeping the same fixed representative and fixed omission pattern still contains every exact-skeleton realization. The enlarged event need not itself characterize joint isolation; it only has to contain the exact skeleton branch being bounded.

Conditional on `F_P`, the charge variables in `A_sigma` and the residual raw edges in `B` are disjoint. Hence

`P(A_sigma and residual | F_P,G_L)`
` = P(A_sigma | F_P,G_L) P(residual | F_P,G_L)`.             (7.5)

Using (5.4),

`<= (2L_r k/n)^(p+q) P(residual | F_P)`.                    (7.6)

The guard can now be dropped from the residual factor because the integrand is nonnegative.

After conditioning only on the equality partition, the root proposal values are still independent root order-statistic arrays. The skeleton supplies a fixed omission set at each root, with at most `2K` omissions total by (6.1). The external competitor pool has size

`|E|=n-r-|S|=n-O_r(k)`,

and the surviving quota is exactly `k`. The residual blocks are disjoint across all retained labels. Therefore Claim 303 applies root by root, simultaneously and uniformly over these arbitrary omission ranks, giving

`E[P(residual | F_P) | pi]`
` <= exp[-rk + O_{C,r}(k^(2/3)+log k)].`                    (7.7)

There is no conditioning bias from collision minima here: on the exact skeleton the representative rank is fixed, and for the upper bound the cross-root comparison asserting it is the minimum has been discarded. Claim 303 needs only the fixed omitted-rank pattern, not that comparison.

The exact partition probability contributes `n^{-c+o(1)}`. Claim 311 counts at most `(C_r k^2)^K` abstract skeleton patterns of complexity `K`. Combining this count, the partition codimension, (7.6), and (7.7), every fixed `K` family is bounded by

`exp[-rk + O_{C,r}(k^(2/3)+log k)] (C_r k^3/n)^K`.           (7.8)

Summing `1<=K<=r` gives (7.2).

Because `log n=k+O_C(1)`,

`exp[O(k^(2/3)+log k)] * k^3/n`
` = exp[-k + O(k^(2/3)+log k)] -> 0`.                        (7.9)

Thus the low positive-complexity contribution is `o(e^{-rk})`.

For `K>=r+1`, Claim 311 gives (7.3), and since `e^{-rk}=n^{-r}e^{O_C(1)}`, this is also `o(e^{-rk})`.

It remains only to justify the guard. For one root,

`T_a > L_r k/n`

iff `Bin(n-r,L_r k/n)<=k-1`. For all sufficiently large `n`, the binomial mean is at least

`(L_r/2)k=4(r+1)k`.

Since `k/mu<=1/[4(r+1)]<=1/8`, the standard lower-tail Chernoff inequality gives

`P(T_a>L_r k/n)`
` <= exp[-mu(1-k/mu)^2/2]`
` <= exp[-49(r+1)k/32].`                                    (7.10)

A union bound over the fixed `r` roots gives (7.4). The exponent exceeds `rk` by a positive multiple of `k`, so the guard failure is `o(e^{-rk})`.

Combining the low-complexity, high-complexity and guard-failure pieces proves (7.1). `square`

---

## 8. #26 HUNT THE SPORADIC CASE — mixed-skeleton audit

The requested sporadic configurations are precisely where a hidden double conditioning could have lived. I checked them separately.

### 8.1 A support edge is a root-tail coordinate and contaminates a collision-retained deadline

Let label `u` occur in a collision block of proposals owned by roots other than `b`, and let the block's global-minimum deadline `D_u` survive. Suppose the raw edge `{u,v_b}` is lighter than `D_u`.

If `u` were among root `b`'s first `k` deleted-array labels, then `{u,v_b}` itself would be another deadline in the same collision block, contradicting strict inequality with the retained global minimum. Therefore `u` is absent from root `b`'s exposed prefix. The edge is exactly a named tail coordinate with conditional law `Uniform[T_b,1]`, so it is charged once by (5.3). It is not part of any residual block because `v_b in R`, not `E`.

Thus a root-tail support edge and a collision block coexist without double conditioning: collision structure is in the label/proposal sigma-field, the tail value is one charged coordinate, and all residual competitors lie in disjoint external blocks.

### 8.2 Root suffix deletion removes a collision-block minimum

Suppose the global minimum proposal occurrence in a repeated-label block lies in a safe terminal suffix forced by endpoint-active root edges. The canonical rule is **not** to promote the next-smallest occurrence. The entire collision block is omitted.

This is essential. Promoting a later occurrence could make the deleted minimum proposal edge into a lighter nonexternal competitor for the promoted deadline and would require a new support charge. The no-promotion rule avoids that recursion. In the canonical algorithm, all nonminimum block occurrences were already collision omissions; deleting the minimum adds exactly the suffix omission and leaves no retained deadline for that label.

The label still remains in `S`, so it is excluded from `E`. Hence an edge from another retained selected label to this now-unretained selected label is still correctly classified as nonexternal and, if it is lighter, is present in `Gamma_0`. No support interaction is lost.

### 8.3 One selected--selected support edge contaminates two retained deadlines

A raw edge `{u,z}` with `u,z in S` can be below both retained deadlines. Claim 311 charges this **one raw edge once**, while the incidence graph records both incidences and simultaneous deletion removes both deadlines. In (5.2) the charge probability remains at most `max(D_u,D_z)<=L_r k/n`; it is not squared. In (6.1) it can create two omissions. The residual blocks omit the raw edge completely because neither selected endpoint belongs to `E`.

Thus the codimension is one and the deletion multiplicity is two, exactly as the canonical `q` count requires.

### 8.4 One root--root edge is endpoint-active at both roots

Likewise, a single root--root raw edge can be endpoint-active at both endpoints. It is charged once in `p`, but contributes one to each corresponding `d_a` and can therefore justify two safe suffix omissions. The root raw variable is disjoint from all residual blocks. This is precisely why the omission estimate uses `sum_a d_a<=2p` rather than `<=p`.

### 8.5 Claim 309's counterconfiguration remains a real safeguard

Nothing in the present proof assumes that an edge below both deleted-array kth thresholds survives at both roots. Claim 309's explicit `r=3` counterconfiguration still shows that statement is false: other root edges can displace it from both final top-`k` lists. The present proof only uses endpoint activity to obtain the safe prefix/suffix bound.

### 8.6 Claim 310's `q_a^*<d_a` example remains a real safeguard

With `k=2`, outside weights `0.1,0.4` and root edges `0.2,0.3`, both root edges are endpoint-active relative to the deleted threshold but only one finally occupies a top-`k` slot. The current proof uses the conservative `d_a` suffix and never identifies it with exact final root occupancy.

No mixed sporadic configuration escapes `K=c+p+q`, and no charged raw variable is reused in a residual rejection block.

---

## 9. #3 PROVE SOMETHING STRONGER — standalone positive-cluster negligibility

The original target of this run was only to justify the interface between Claims 313 and 303. Claim 315 proves more: **the entire positive canonical-interaction mass is negligible at the exact fixed-root isolation scale**, uniformly in the fixed critical window.

Together with Claim 314's explicit clean lower event and the existing clean upper branch from Claims 308/306, we retain the two-sided fixed-root estimate

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`               (9.1)

for every fixed `r,C`, uniformly over every deterministic tuple of distinct roots and every integer `|k-log n|<=C`.

The implication chain is therefore still:

fixed-`r` joint isolation (Claims 308, 314, 315)  
`->` all fixed factorial moments of the isolated count  
`->` Claim 305 finite Brun/Bonferroni TV convergence  
`->` literal nontrivial-component elimination  
`->` fixed-window connectivity law.

If `Z_n` is the number of isolated vertices and `lambda_n=ne^{-k}`, then internally the candidate-complete result remains

`d_TV(Law(Z_n),Poi(lambda_n)) -> 0`,                         (9.2)

and

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.                (9.3)

This is still **AUDITS-PENDING** and **PUBLICATION-NOVELTY-UNVERIFIED**. The present P03 self-audit does not count toward the two required outside audits.

---

## 10. Literal nontrivial components remain unchanged

The component proof was not modified this run, but I rechecked the interface under the literal bilateral rule.

- Sizes `2--6`: delete all internal candidate-component edges before ranking external proposals. The light spanning-tree event then uses only internal raw weights, while external proposal/rejection events use disjoint external raw-edge families. The repaired fixed-size rejection bound applies after this deletion.
- Sizes `7--12`: use the fixed-size part of the single global kth-threshold envelope.
- Sizes `13--n/2`: use the geometric tail under the same global envelope.
- The global-envelope failure event is paid once, not once per candidate set or component size.

No connectivity claim is inferred from mean degree.

---

## 11. What failed / what was deliberately not used

### Method #3 outcome

Succeeded. The desired conditioning-interface check strengthened to the standalone quantitative positive-cluster estimate (7.1)--(7.4).

### Method #18 outcome

Succeeded. The upper branch is now a finite generative model with one complete nonexternal conditioning sigma-field `G_*` and a disjoint external residual family `B`. No Sevast'yanov, Chen--Stein, Barbour, or generic dependency-graph theorem is invoked.

### Method #26 outcome

Succeeded as an adversarial audit. The two requested sporadic interfaces and the two historical root-merge safeguards were checked explicitly. No new defect class was found.

### Routes deliberately not taken

- No new Poisson correction coefficients were computed.
- No coefficient window was enlarged.
- No component cutoff was re-optimized.
- No pair-only second moment was substituted for all fixed factorial moments.
- No global rank symmetry was introduced.
- No false `r>=3` root-edge shortcut was restored.

---

## 12. Cumulative claim ledger delta

Preserved:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains PPP; Claims 291--300 remain historical support, not fixed-`C` dependencies.
- Claim 301 remains valid only with the explicit subsequent repairs.
- Claim 302 remains repaired by Claim 309 at the root-merge clause.
- `P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 304 remains repaired by Claim 309 and strengthened by Claims 305, 311, 313, 315.
- `P03-P0456-EXPLICIT-BRUN-BOUNDARY-CROSSCHECK-305 = PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 306 remains the asymmetric auditor map, with lower branch now superseded in proof surface by Claim 314.
- Claim 307 remains the quota-aware clean-saddle quantifier correction.
- `P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-ROOT-MERGE-SIGMA-COMPLETENESS-309 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-SEQUENTIAL-MERGE-SUPPORT-DELETION-310 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-CANONICAL-INCIDENCE-SKELETON-311 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-AUDITOR-FIXED-C-DAG-SOURCE-MAP-312 = PROVED / SELF-AUDIT-PACKAGING / SOURCE-FAILURE-COMPLETE / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-LOW-COMPLEXITY-CODIMENSION-313 = PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MAP-TAXONOMY-CLARIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-CLEAN-LOWER-EXACT-FACTORIZATION-314 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

New:

- `P03-P0456-POSITIVE-CLUSTER-CONDITIONAL-GLUE-315 = PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

All three frozen coefficient metrics remain saturated at zero:

`c_LK^cert=0`, `a_LK^fine=0`, `b_LK^sqrt=0`.

No stuck count is manufactured. HARD recoveries remain `0/2`.

---

## 13. Exact remaining obligation and next state

The mathematical source chain is internally candidate-complete but cannot be closed by P03 self-checks. The exact closure obligation remains:

1. one genuine independent **P26** end-to-end audit of the repaired fixed-`C` source chain, including Claims 305, 308, 309--315 and the literal component argument;
2. one genuinely distinct **OTHER track** end-to-end audit of the same repaired chain;
3. repair any gap either auditor identifies;
4. only after both passes, create the self-contained source-matching paper package and request closure through P26's shared-ledger process.

Current state after this run:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_315_POSITIVE_CLUSTER_GLUE_READY`.

### Next concrete P03 attack if no outside audit arrives first

Audit-first remains controlling. First reread every incoming P26/OTHER-track P0456 audit and repair its exact objection before new self-audit work.

If the gate is still `0/2`, a useful nonconsecutive triple is **#6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT**:

- #6: interpolate the positive-cluster support family from the empty nonexternal family to the full `Gamma_0` support family one raw edge at a time; prove directly that the upper event is monotone under adding charged support coordinates after the corresponding deadlines are deleted, or identify the exact obstruction.
- #11: dualize the component-elimination layer into a cut/witness certificate only to see whether the existing `2--6` versus `7+` split can be expressed in one auditor-readable statement without changing its proof. Do not optimize constants.
- #24: identify the fixed-s interaction skeleton maximizing the low-complexity contribution after the exact codimension and Claim-303 saddle factors. The goal is a clean worst-case auditor bound, not a correction coefficient.

Do not revisit Claim 314's lower exact product unless an outside auditor objects.

---

## 14. `ledger_delta` for P26 reconciliation only

P03 does not edit the shared root ledgers. The following is the exact delta P26 may use if/when reconciling this target:

```yaml
ledger_delta:
  target: P0456
  owner: P03
  category: HARD_OUTSIDE
  source_status: OPEN_IN_PRIMARY_SOURCE_AS_OF_2026-09-19
  mathematical_status: PROVED_CANDIDATE / SOURCE_MATCHING / AUDITS_PENDING
  publication_novelty: UNVERIFIED
  fixed_metrics:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    note: SATURATED_ZERO_DO_NOT_COUNT_AS_STUCK
  hard_recoveries: "0/2"
  outside_audits:
    p26: 0
    distinct_other: 0
    required: 2
  new_claim:
    id: P03-P0456-POSITIVE-CLUSTER-CONDITIONAL-GLUE-315
    status: PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
    theorem: "For fixed r,C, uniformly on |k-log n|<=C and deterministic distinct roots, P(all roots isolated, K>=1)=o(e^{-rk}) for the canonical K=c+p+q interaction complexity."
  closure_request: false
  paper_package_created: false
  reason: "No P26 P0456 PASS and no distinct OTHER-track P0456 PASS exist in the screened repository state."
```

No peer file, shared root ledger, Gmail/email surface, Drive, workflow, permission, billing, or public-posting surface was modified in this run.

**End of complete run report.**
