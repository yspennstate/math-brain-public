Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#2 ATTACK THE NEGATION FIRST, #21 ASK WHO ELSE HAS THIS SHAPE, #20 FIND WHY THE ALGORITHM FAILS**. The adversarial pass found one real proof-surface defect in Claim 301's stated collision-block disjointization, repaired it exactly, and found no counterexample to the source-matching theorem.

# P03 / P0456 run report — defect-completeness audit and collision-block disjointization repair

Run timestamp: **2026-09-19T02:32:51Z**  
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

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T01-27-30Z__p0456-source-proof-capsule.md`,

creation commit `a272069bd353e62aff63e74626db4b68d4987b8a`, blob `95044755a3d4b7e0cd5cfdafdbf0dd4e3d54483d`; exact blob readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286, 288--300. Claim 301 is preserved **with the Step-D repair proved below**.

This run reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/FLEET_2026-09-16.md`, the current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the complete Claim-301 report at its exact blob, the Claim-292 interaction report, the current P26 directory/newest P26 report, P04 state, and neighboring P0457 ownership only for nonduplication. Large connector-rendered root/policy surfaces were truncated and are therefore not represented as byte-for-byte whole-file rereads; exact paths, exact blobs, and targeted repository queries were used for the mathematical dependencies.

### 1.1 Incoming outside-audit screen

A newer P26 report has appeared since Claim 301:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_05-00-09__run-report.md`,

creation commit `9d433d504a2cfb254fe061005a345b4e51ae25d9`.

It audits **P04/I0101 Claim 38 at p=4177**, reconciles that finite theta-plus certificate with an earlier distinct P03 audit, and does **not** audit P0456. Repository-wide searches for `P0456`, Claim 288/289/301, `audit`, and `PASS` still recover no P26 or genuinely distinct OTHER-track full-chain P0456 audit. P04 remains rotation-stopped; there is no new P04 successor theorem for the directed P03 audit duty.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper folder are created.

### 1.2 Fresh source / current-literature screen

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies the literal model and Section 1.1 statement: connectivity remains stated as unknown in

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and the authors explicitly attribute the gap to analytically simpler sufficient conditions, including a no-intersection condition among preferred sets. Lemma 10 still gives its pair bad-event bound `O(k^3/n)`; Theorem 3 gives disconnectedness below coefficient `-1/2`; Theorem 6 gives connectivity above coefficient `+1/2`.

Fresh bounded searches for the DOI/title/authors, 2026 bilateral-preference connectivity/Poisson updates, and author pages recovered the Cambridge article, the older arXiv/preprint version, and bibliographic mirrors but no later source-matching constant-window or isolated-vertex Poisson theorem. This is dated bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

Neighboring P0457 remains a distinct diameter problem owned by NM13-04 and is not duplicated here.

---

## 2. #2 ATTACK THE NEGATION FIRST — a real local counterexample to Claim 301's literal Step-D sentence

Claim 301's theorem is not refuted, but one sentence in its stated disjointization algorithm was too strong as written.

Claim 301 Step D said that in a repeated-label block one may "retain one occurrence and omit every other attached rejection deadline", after which every remaining rejection list uses only edges from a distinct selected label to the external pool. If the retained occurrence is arbitrary, that last assertion is false.

### Minimal counterconfiguration

Take two roots `v_1,v_2` and one outside label `u` selected by both roots. Let

`D_1=W(v_1,u)`, `D_2=W(v_2,u)`,

and suppose `D_2<D_1`. This is a collision block of size two, so its collision excess is `c=1`. Assume there are no other active selected--selected or cross edges and no early root--root edge, so the old bookkeeping has `q=p=0`.

If Step D arbitrarily retains the `D_1` rejection constraint at `u` and omits the `D_2` constraint, then the raw edge

`{v_2,u}`

has weight `D_2<D_1` and is itself a lighter competitor in the retained rejection test at `u`. It is not in the external pool, and it is not a root-selected cross edge of the old `q` type because `u` is selected by `v_2`. Thus the literal sentence "every remaining rejection list uses only external edges" does not follow from arbitrary retention.

This is a genuine **proof-surface gap**, not a theorem counterexample: the collision already paid one factor `n^{-1+o(1)}`, and a deterministic choice of the retained occurrence removes the issue completely.

### Exact repair

For every repeated-label block, retain **the occurrence with minimum proposal deadline** and omit every other deadline in that block. If the block has deadlines

`D_(1)<D_(2)<...<D_(s)`,

retain `D_(1)`. Every other root-to-label proposal edge in that block has weight `>=D_(1)` and therefore cannot be a lighter competitor for the retained rejection test. Ties have probability zero.

An even coarser valid repair would omit all deadlines in every repeated-label block; the minimum-deadline rule is stronger and preserves one constraint without changing the collision codimension.

This repair is the main mathematical output of the run. Claim 301 remains proved after repair; its prior Step-D wording should not be reused verbatim. Claim 292 is not downgraded: its earlier bounded-skeleton formulation allowed deletion of deadlines touched by collision defects and did not require the faulty arbitrary-retention assertion.

---

## 3. New supporting repair theorem

### Claim `P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302`

**Status:** `PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix a root set `R={v_1,...,v_r}` with fixed `r`, temporarily remove root--root edges, expose the first `k` nonroot proposal labels/deadlines, and work on the threshold guard `G_L` of Claim 301. Define

`K=c+q+p`,

where

- `c` is selected-label collision excess;
- `q` is the number of **unique** active selected--selected or selected--root cross edges which lie below at least one applicable retained proposal deadline;
- `p` is the number of early root--root edges.

Then every way in which two root-isolation rejection tests can share a raw edge, or in which reinserting a root--root edge can alter the relevant proposal list, belongs to one of those three classes. Moreover there is a deterministic disjointization such that, after only `O_{r,K}(1)` deadline omissions, every surviving rejection constraint is supported on a raw-edge family disjoint from every other surviving rejection constraint.

Consequently the Claim-301 skeleton bound

`P(fixed complexity-d skeleton,G_L) <= n^{-d+o(1)}`

and the bounded-omission marked-saddle estimate still imply that all positive-complexity skeletons contribute `o(e^{-rk})`. Thus the all-fixed-`r` joint-isolation asymptotic and the source-matching Poisson theorem are unchanged.

### Proof

We give an exhaustive classification.

#### 3.1 Collision blocks

A selected outside label `u` may be proposed by several roots. If it occurs in a block of size `s`, the equality partition contributes collision excess `s-1`, with exact label probability already given by

`(N)_m/(N)_k^r`.

Order the `s` proposal deadlines at `u` and retain only the smallest one `D_min`; omit the other `s-1` rejection constraints. Every other proposal edge from a root in the same block has weight at least `D_min`, hence none can be counted as a lighter competitor in the retained test. This removes the counterconfiguration of Section 2 without any additional probability charge.

After this step, each retained rejection deadline is attached to a **distinct selected label**.

#### 3.2 Selected--selected internal edges

Let `u,z` be distinct retained selected labels. The only raw edge shared between their two one-star rejection environments is `{u,z}`. If its weight is below an applicable deadline at `u` or `z`, it is an active selected--selected defect and is counted once in `q`. Omit every retained deadline that this edge can help. One unique edge may touch two deadlines, but it is correctly charged only once because the two effects are caused by the same single rare edge. If `{u,z}` is above both applicable deadlines, it is irrelevant to both rejection tests.

#### 3.3 Selected--root cross edges

Let `u` be a retained selected label, selected at root `v_a`, and let `v_b` be another root.

If `u` was also selected by `v_b`, then `v_b` belongs to the same collision block. By the minimum-deadline rule, the edge `{v_b,u}` is not below the retained block deadline.

If `u` was not selected by `v_b`, then conditional on root `b`'s nonroot `k`th threshold `T_b=t`,

`W(v_b,u) | (u nonselected at b,T_b=t) ~ Uniform[t,1]`.

If this edge falls below the retained deadline at `u`, it is exactly a root-selected cross defect and is counted once in `q`; omit that retained deadline. Otherwise it is irrelevant. Thus no selected--root edge survives below a retained deadline without being either paid by the collision excess or paid as an active cross edge.

#### 3.4 Root--root reinsertion

Let `e={v_a,v_b}` be a temporarily deleted root--root edge, and let `T_a,T_b` be the nonroot `k`th thresholds.

- If `W(e)<=T_a` and `W(e)<=T_b`, then after reinsertion `e` is selected by **both** roots and therefore survives the bilateral rule. The joint-isolation event has probability zero on this branch.
- If `e` is early at exactly one endpoint, say `W(e)<=T_a` but `W(e)>T_b`, then reinsertion displaces exactly one terminal nonroot proposal at root `a` and changes no proposal edge value. Omit that displaced terminal deadline. It does not alter root `b`'s selected nonroot set.
- If `e` is early at neither endpoint, it changes nothing.

With fixed `r`, all root--root edges together displace at most `r-1` terminal nonroot deadlines at any root, so the total number of omissions remains bounded. Each early root--root edge is charged once in `p`; charging it once is correct even though the impossible both-end branch could affect two ranks, because that branch contributes zero to joint isolation.

#### 3.5 Exact residual edge partition

Let `S` be the set of all selected nonroot labels appearing anywhere in the temporary proposal arrays and put

`E=V \ (R union S)`.

After the preceding omissions, consider a surviving deadline `D(u)` attached to selected label `u`.

Any raw edge incident to `u` whose other endpoint lies in `R union S` has already been handled:

- another root selecting `u`: collision block, and its edge is `>=D(u)` by minimum retention;
- another root not selecting `u`: cross edge, charged/omitted if below `D(u)`;
- another selected label: selected--selected edge, charged/omitted if below `D(u)`.

Therefore every raw edge that can still count as a lighter competitor for `D(u)` has the form

`{u,x}`, `x in E`.

For two distinct retained labels `u != z`, the families

`{{u,x}:x in E}` and `{{z,x}:x in E}`

are disjoint as sets of undirected edges. Equality of one edge from each family would force the other endpoint of one to equal a selected label, contradicting `x in E`. Thus the surviving rejection lists are **deterministically disjoint**, not merely weakly dependent.

This exhausts every raw edge incident to a selected label. Rejection depends only on such one-star raw weights and does not recursively inspect survival of competitor edges, so there is no further dependency class at greater depth. This proves defect completeness and exact disjointization. `square`

### 3.6 Probability bookkeeping is unchanged

Collision blocks retain their exact codimension `c`. On `G_L`, each prescribed active selected--selected/cross edge and each early root--root edge costs `O_L(k/n)`, so a witness-labelled skeleton of complexity `d=c+q+p` still costs

`n^{-d+o(1)}`.

There are only `k^{O_{r,d}(1)}=n^{o(1)}` witness-labelled skeletons of fixed complexity. The repaired omissions are bounded, so Claim 301 Lemma 3.1(b) still gives rejection cost `exp[-rk+o(k)]`. Hence every positive-complexity contribution remains

`e^{-rk+o(k)} n^{-1+o(1)}=o(e^{-rk})`.

The zero skeleton contains no collisions, active internal/cross edges, or early root--root edges and is unchanged. Therefore Claim 301's equation for every fixed-`r` joint isolation probability remains valid.

---

## 4. #20 FIND WHY THE ALGORITHM FAILS — execute the worst bounded skeleton symbolically

I ran the repaired checklist symbolically on a deliberately hostile mixed skeleton.

Take roots `v_1,v_2,v_3`.

1. A label `u` is selected by all three roots, with deadlines
   `D_1<D_2<D_3`. This is a triple collision with cost `c=2`.
2. A label `x` is selected only by `v_1`, and `{v_2,x}` lies below `x`'s deadline. This is one active root-selected cross edge.
3. Distinct labels `y,z` are retained selected labels and `{y,z}` lies below at least one of their deadlines. This is one active selected--selected edge.
4. The root--root edge `{v_1,v_3}` is early at `v_1` but not at `v_3`.

Thus the skeleton has

`K=2+2+1=5`.

Apply the repaired algorithm.

- At `u`, retain `D_1` and omit the `D_2,D_3` constraints. The same-block root edges `{v_2,u}`, `{v_3,u}` have weights `D_2,D_3>D_1`, so neither is a lighter competitor for the retained test.
- The active cross edge `{v_2,x}` causes the retained deadline at `x` to be omitted.
- The active selected--selected edge `{y,z}` causes every deadline it can contaminate to be omitted; if it is below both, both are omitted while the edge is charged only once.
- Reinserting `{v_1,v_3}` displaces one terminal nonroot proposal at `v_1`; omit that terminal deadline. Since the edge is not early at `v_3`, no rank changes there. Had it been early at both roots, joint isolation would have been impossible and the branch would terminate immediately.

Now inspect any deadline that remains. Its selected label is unique among retained blocks. Every edge from that label to a root or another selected label is either above the deadline or belongs to a charged defect whose deadline was omitted. Hence all remaining lighter competitors lie in `E`, and each raw edge belongs to exactly one remaining one-star list.

This hostile example simultaneously exercises a multiway collision, a cross edge, an internal selected edge, and a root--root rank shift. It exposes exactly the old arbitrary-retention failure and confirms that the minimum-deadline repair closes it.

---

## 5. #21 ASK WHO ELSE HAS THIS SHAPE — terminology map for an outside auditor

The repaired interaction proof has a recognizable relation to three standard Poisson-approximation patterns, but none can be imported verbatim.

### 5.1 Dissociated-indicator language

Barbour--Holst--Janson's *Poisson Approximation* treats dissociated indicator arrays as a natural extension of independence. Claim 302 reaches something stronger **after conditioning on a finite defect skeleton**: the surviving raw-edge families are exactly disjoint, hence independent. Before conditioning/disjointization, however, the vertex-isolation indicators in `LK(n,k)` are not a sparse dissociated family; the naive deterministic dependency graph is effectively complete.

Thus the right vocabulary is:

`rare overlap skeleton -> delete/charge overlap support -> exact dissociation of residual raw-edge blocks`.

This is a structural mapping, not an invocation of a black-box theorem.

### 5.2 Dependency-cluster / overlap expansion language

The equality partition and active-edge skeleton can be viewed as a finite dependency cluster. Collision excess and active-edge count form a codimension: each independent overlap defect costs one power `n^{-1+o(1)}`. The zero-defect cluster factors, and every positive-defect cluster is negligible after the bounded-omission rejection saddle. This is analogous to the usual cluster principle behind factorial-moment proofs for rare substructures, but here the clusters are generated by **proposal-label coincidences and low raw edges**, not by graph-distance neighborhoods.

### 5.3 Random-intersection-graph analogy

Random intersection graphs provide a useful comparison because dependence is created when vertices share auxiliary objects. Shang (2011), *On the Isolated Vertices and Connectivity in Random Intersection Graphs*, proves Poisson convergence of isolated vertices and threshold connectivity in that model using Stein--Chen. Rybarczyk--Stark likewise use Stein methods for Poisson counts of fixed subgraphs in random intersection graphs.

The analogy is precise only at the overlap level: a repeated LK proposal label plays the role of a shared object and creates a small dependency cluster. The difference is essential: LK proposal sets arise from **order statistics of shared edge weights**, and root-selected cross edges have the conditional truncated law `Uniform[T,1]`. Those rank and truncation effects are exactly why a generic random-intersection or dependency-neighborhood theorem cannot simply replace Claims 301--302.

This terminology should make the outside audit easier: the proof is a factorial-moment / rare-cluster argument whose residual blocks are exactly dissociated at the raw-edge level.

---

## 6. Re-audit of Claim 301's global component envelope

I rechecked all four requested numerical thresholds and the "pay the global failure once" logic under the literal LK definition.

Set

`a=5/32`, `b=32/5`.

For `I(s)=s-1-log s`, Claim 301 needs `I(a)>1` and `I(b)>1`.

### 6.1 Lower threshold: an exact inequality, not a decimal

`I(a)>1` is equivalent to

`log(32/5)>59/32`.

Put

`z=((32/5)-1)/((32/5)+1)=27/37`.

The positive atanh series gives

`log(32/5)=2 sum_{j>=0} z^(2j+1)/(2j+1)`.

Keeping only `j=0,...,4` gives the exact rational lower bound

`8395950040270578 / 4548660892827695`

which exceeds `59/32` by

`299408611824491 / 145557148570486240 > 0`.

Hence `I(5/32)>1` rigorously.

### 6.2 Upper threshold

The exponential series gives

`e^2 > 1+2+2^2/2!+2^3/3!+2^4/4! = 7 > 32/5`.

Therefore `log(32/5)<2`, and

`I(32/5)=27/5-log(32/5)>27/5-2=17/5>1`.

Thus the global threshold event

`H={ak/(n-1) <= T_v <= bk/(n-1) for every v}`

has `P(H^c)=o(1)` by a single union bound over vertices. This complement is paid **once**, before summing over component sizes.

### 6.3 Fixed component threshold really starts at r=7

On `H`, the component bound of Claim 301 has leading fixed-`r` exponent

`1-ar = 1-5r/32`.

At `r=7` this equals

`1-35/32=-3/32<0`,

and it is strictly smaller for every `r>=8`. Thus the direct global-envelope estimate starts exactly where Claim 301 said: it covers all fixed `7<=r<=12`.

### 6.4 Uniform geometric threshold really starts at r=13

For `13<=r<=n/2`, Claim 301 reduces the bound to

`C n/(bk r^2) * q_n^r`,

with

`q_n = O(k n^{-a/2}) = O(k n^{-5/64})`.

The first power in the geometric tail is `r=13`, and

`1-13*(5/64)=1-65/64=-1/64`.

Therefore

`sum_{r=13}^{floor(n/2)} P(exists r-component,H)
 <= n^{-1/64+o(1)}=o(1)`.

No component conclusion is inferred from mean degree. On `H`, retained tree edges are forced below the upper kth-threshold envelope and every crossing edge is forced above the lower envelope; those are literal raw-weight consequences of bilateral preference.

The component proof therefore survives this audit unchanged.

---

## 7. Consequence for Claims 301 and 288/289

The adversarial search found a local defect in **how Claim 301 described collision-block disjointization**, but not a counterexample to its theorem.

The correct status is now:

- `P03-P0456-SOURCE-AUDIT-CAPSULE-301 = PROVED / SELF-AUDIT-CAPSULE / STEP-D-REPAIRED-BY-302 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

The all-fixed-`r` joint isolation proof remains

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`

uniformly on fixed `|k-log n|<=C`; the factorial-moment Poisson argument and literal component elimination are unchanged. Hence Claims 288/289 remain source-matching candidate-complete **subject to outside audit**, not CLOSED.

The repair should be the first thing an outside auditor checks: in every collision block, the retained rejection deadline must be the **minimum** deadline (or all block deadlines may be omitted). Arbitrary retention is not valid if one wants literal external-only rejection lists.

---

## 8. Directed P03 -> P04 duty

P04 has no `2026-09-19` run directory in the current repository and remains rotation-stopped. The newest P26 work continues to audit preserved historical P04/I0101 finite claims; it does not create a new P04 successor theorem. Therefore there is no genuinely new P04 mathematical claim for P03 to audit this run, and I do not fabricate or repeat one.

---

## 9. Cumulative state, remaining obligation, and `ledger_delta`

Preserved source-matching chain:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290 marked PPP;
- Claims 291--300 supporting self-audit/strengthening kernels;
- Claim 301 source-audit capsule, now explicitly repaired by Claim 302;
- new `P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302` as above.

Protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_302_COLLISION_REPAIR_READY`.

Exact remaining obligation: P26 and one genuinely distinct OTHER track must independently verify the **repaired** capsule, in particular (i) the bounded-omission marked saddle; (ii) minimum-deadline collision-block disjointization and exhaustive `K=c+q+p` classification; (iii) all-fixed-`r` factorial moments to uniform TV; and (iv) small- and large-component elimination. Any outside gap overrides the self-audit labels.

`ledger_delta` for P26:

```yaml
track: P03
source: P0456
status: SOURCE_MATCHING_CANDIDATE_COMPLETE_AUDIT_PENDING
new_claim: P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302
new_claim_status: PROVED_SELF_AUDIT_REPAIR_SUPPORTING
claim_301_status: PROVED_SELF_AUDIT_CAPSULE_STEP_D_REPAIRED_BY_302
independent_audits_found: 0/2
source_closed: false
paper_package_created: false
metrics:
  c_LK_cert: 0_saturated
  a_LK_fine: 0_saturated
  b_LK_sqrt: 0_saturated
stuck_increment: 0
hard_recoveries: 0/2
repair_note: >-
  In every repeated selected-label block, retain the minimum proposal deadline
  (or omit all block deadlines). Arbitrary retention can leave another root's
  proposal edge below the retained deadline and invalidates literal external-only
  disjointness. With minimum retention, K=c+q+p is exhaustive.
outside_audit_request:
  - verify Claim 301 Lemma 3.1 bounded-omission saddle
  - verify Claim 302 minimum-deadline collision repair and K=c+q+p exhaustiveness
  - verify root-root reinsertion dichotomy, including impossible both-end-early isolation branch
  - verify component envelope constants a=5/32, b=32/5 and single payment of H^c
```

---

## 10. Next state

Further first/second-correction asymptotics and coefficient-window optimization remain suspended. Incoming outside audits retain absolute priority. If no outside audit arrives, the next useful self-audit should target a different possible failure surface: the analytic bounded-omission Lemma 3.1 under adversarial omitted ranks and the exact transition from its per-root rejection integral to the product over repaired residual blocks. The collision combinatorics should not be re-proved again unless an outside auditor objects.

The requested GPT-6/maximum setting remains prompt-only in the exposed task controls; this run actually used GPT-5.6 Sol and reasoning metadata is UNVERIFIED. No permission denial occurred. GitHub only; no Gmail/email, Drive, public posting, workflow execution, paid compute, access changes, peer-file edits, or additional schedules.

**End of complete run report.**