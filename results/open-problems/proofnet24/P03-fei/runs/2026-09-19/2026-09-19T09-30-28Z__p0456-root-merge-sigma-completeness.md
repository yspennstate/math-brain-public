Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE**. It finds one real `r=3` counterconfiguration to the literal root--root reinsertion shortcut used in Claims 302/304, repairs that shortcut without changing the source theorem, and makes the fixed-root proof into an explicit raw-edge sigma-field diagram.

# P03 / P0456 run report — root-merge repair and sigma-field completeness audit

Run timestamp: **2026-09-19T09:30:28Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, repository state, and audit-first screen

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run is

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T08-27-37Z__p0456-interpolated-dual-clean-saddle.md`,

creation commit `5304da5ca95493a0be1e809709fcda6a79597065`, blob `4cb58e98e1a0ab95bd9386f1aac4c3772c780366`; its exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286, 288--308, with the explicit root--root clause repair proved in this report. In particular Claims 302 and 304 remain usable only with Claim 309 below; their literal sentence that a root--root edge lying below both deleted-array `k`th thresholds must survive bilaterally is valid for `r=2` but is false for `r>=3`.

Before the mathematical attack I reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, the current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim at its creation commit, the complete Claims 302, 304, 306 and 308 reports needed for this audit, current task-health state, the current P26 run directory, and neighboring P0457 only for nonduplication. Connector-rendered large root/policy surfaces are truncated; I do not represent them as byte-for-byte whole-file rereads.

The current task-health snapshot `operations/task_health/runs/2026-09-19T090100Z/status.md` does not release or reassign P0456. Neighboring P0457 remains a distinct diameter problem owned by NM13-04.

### 1.1 Incoming outside-audit screen

The P26 directory now contains reports later than the one named in the handoff. The newest concrete report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_11-59-00__run-report.md`,

blob `481a3f44b96cdd9639a2fc5e24fb6370b76592e7`.

It audits the R06 Romero max-minus-three diagonal, not P0456. Exact-string repository searches for `P03-P0456-POISSON-CRITICAL-WINDOW-288`, `P0456`, and the repaired claim chain still recover no P26 or genuinely distinct OTHER-track end-to-end P0456 PASS. The closure gate therefore remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper package are created.

### 1.2 Fresh primary-source and current-literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 still states in Section 1.1 that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and says the gap may arise from analytically simpler sufficient conditions, including the no-intersection condition used for isolated vertices. The source still records Lemma 10's `O(k^3/n)` bad-interaction bound, Lemmas 11--14's pair-isolation/conditional-independence chain, Theorem 3 below coefficient `-1/2`, and Theorem 6 above coefficient `+1/2`.

The required PDF screenshot calls were attempted for the open-problem and Lemmas 10--14 / Theorems 3 and 6 pages, but Cambridge's screenshot backend returned 404/cache-miss errors; the PDF text extraction and Cambridge HTML were available and were used instead. Fresh bounded searches for the exact title/DOI/authors and 2026 bilateral-preference connectivity/Poisson follow-ups found the published article and bibliographic/author records, but no later source-matching constant-window theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. #2 ATTACK THE NEGATION FIRST — the `r=2` proof survives, but the first `r=3` sporadic branch breaks the old shortcut

Claims 302/304 temporarily delete the root--root edges, expose each root's first `k` outside proposals, then reinsert the finitely many root--root edges. Their literal proof used the following shortcut:

> If a root--root edge is below the deleted-array `k`th threshold at both endpoints, then it is selected by both endpoints and the joint-isolation branch is impossible.

This is correct when there are only **two** distinguished roots. It is not correct as soon as one endpoint can have a second root--root competitor.

### 2.1 `r=2`: exhaustive check

Let the roots be `v_1,v_2`, delete the single edge `e={v_1,v_2}`, and let `T_1,T_2` be the `k`th outside thresholds.

- If `W(e)>T_1,T_2`, reinsertion changes neither top-`k` list.
- If `W(e)<=T_1` but `W(e)>T_2`, then `e` is certainly in `v_1`'s merged top `k` and displaces exactly the `k`th outside proposal there; it is not selected at `v_2`.
- Symmetrically for the other one-end case.
- If `W(e)<=T_1,T_2`, there is no other root--root edge at either endpoint, so `e` is selected by both and survives bilaterally. Joint isolation is impossible.

Thus the old shortcut is literally valid for `r=2`.

The other `r=2` overlap classes are also exhaustive. A label chosen by both roots is a collision block, repaired by minimum-deadline retention. For distinct selected labels `u` at `v_1` and `z` at `v_2`, the only selected--selected shared raw edge is `{u,z}`; it is charged once if active and every deadline it contaminates is omitted. The cross raw edges `{v_2,u}` and `{v_1,z}` are tail edges at the opposite roots unless a collision occurs, and conditional on the opposite terminal threshold have the exact truncated-Uniform law already used in Claim 304. No fourth raw-edge type exists.

### 2.2 `r=3`: an explicit positive-probability counterconfiguration

Let the roots be `v_1,v_2,v_3`. Delete all three root--root edges. At roots 1 and 2 write the last two exposed outside order statistics as

`T_{1,k-1}<T_{1,k}`, `T_{2,k-1}<T_{2,k}`.

Choose root--root weights on a positive-measure open set satisfying

`T_{1,k-1}<W_{12}<T_{1,k}`,
`T_{2,k-1}<W_{12}<T_{2,k}`,

`W_{13}<T_{1,k-1}`,  `W_{13}>T_{3,k}`,

`W_{23}<T_{2,k-1}`,  `W_{23}>T_{3,k}`.

Such inequalities are compatible on a positive-probability set because all underlying weights and outside order statistics are continuous and independent across the relevant deleted/raw families.

The edge `{v_1,v_2}` is below the deleted-array `k`th threshold at **both** endpoints. Nevertheless it is not selected at either endpoint after all root--root edges are restored:

- at `v_1`, the `k-1` outside edges preceding `T_{1,k-1}` together with `{v_1,v_3}` already give `k` edges lighter than `W_{12}`;
- at `v_2`, the `k-1` outside edges preceding `T_{2,k-1}` together with `{v_2,v_3}` do the same.

Meanwhile `{v_1,v_3}` and `{v_2,v_3}` are not selected at `v_3` by the last two displayed inequalities. Thus no root--root edge survives bilaterally merely from the old "both-end early" condition. If the actual outside proposals are rejected by their selected neighbors, all three roots can still be isolated.

This is a real counterexample to the **literal reinsertion sentence** in Claims 302/304. It is not a counterexample to the P0456 source theorem. The offending branch already contains three rare root--root raw edges, and the exact repair below handles it with the same `n^{-p+o(1)}` defect accounting and bounded omissions.

---

## 3. Claim 309 — exact root-merge repair

### Claim `P03-P0456-ROOT-MERGE-SIGMA-COMPLETENESS-309`

**Status:** `PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `r` distinguished roots. Delete every root--root edge and expose the first `k` outside proposal values at root `a`, with terminal value `T_a`. For a root--root edge `e={v_a,v_b}`, define its **endpoint-activity set**

`A(e)={a: W(e)<=T_a} union {b: W(e)<=T_b}`.

Call `e` active iff `A(e)` is nonempty, and let

`p = #{root--root edges e : A(e) != emptyset}`.

For each root `a`, let

`d_a = #{e incident to v_a : a in A(e)}`.

Then:

1. after reinserting **all** root--root edges, every actual outside proposal of root `a` lies among its first `k` deleted-array outside proposals, and the first `k-d_a` of those outside proposals are certainly still selected;
2. therefore only the terminal ranks `k-d_a+1,...,k` can be displaced, so omitting those `d_a` deadlines is always sufficient, whether or not every active root--root edge is itself ultimately selected;
3. on the threshold guard `max_a T_a<=Lk/n`, each prescribed active **unique** root--root edge costs at most `Lk/n` conditionally on the outside proposal arrays, and the distinct root--root raw weights are independent, so a prescribed set of `p` active edges costs `n^{-p+o(1)}`;
4. one root--root edge active at two endpoints is charged **once** but may trigger omissions at both endpoints, exactly as one active selected--selected edge is charged once while every deadline it can contaminate is omitted;
5. after combining this rule with Claim 302's minimum-deadline collision retention and its selected--selected / root-selected active-edge omissions, every surviving rejection list is again supported only on a distinct selected label's external raw-edge block. Hence `K=c+q+p` remains exhaustive and the fixed-`r` joint-isolation asymptotic is unchanged.

### Proof

Fix root `a`. Root--root edges with weight greater than `T_a` cannot enter the final top `k`: the deleted array already contains `k` outside edges lighter than them, and adding more competitors can only push a raw edge down in rank. Thus every root--root edge actually selected at `a` is among the `d_a` endpoint-active edges.

Now merge the first `k` deleted-array outside weights with those `d_a` active root--root weights. The final top `k` is obtained by deleting at most `d_a` elements from these `k+d_a` candidates. For any outside rank `j<=k-d_a`, at most `j-1` outside weights plus all `d_a` active root edges can precede it, for a total at most

`(k-d_a-1)+d_a = k-1`.

Hence every outside rank `1,...,k-d_a` is necessarily in the final top `k`. The only outside proposals which can be lost are the last `d_a`. This proves (1)--(2) without deciding which active root edges themselves survive the merge.

Conditional on the deleted-array outside sigma-fields, a root--root raw weight is independent Uniform`[0,1]`. The event `A(e)!=emptyset` is

`W(e)<=max(T_a,T_b)`,

so on the guard its probability is at most `Lk/n`. Distinct root--root edges have independent raw weights even when they share a root, because the outside thresholds have already been conditioned on and use disjoint raw edges. Multiplying gives `(Lk/n)^p=n^{-p+o(1)}` for any prescribed active set. This proves (3).

For (4), there is no reason to pay twice for one raw edge simply because it lies below both endpoint thresholds. Its one random value is one codimension-one defect. The correct response to two possible rank effects is to omit the affected terminal deadlines at **both** endpoints, not to invent a second probability factor and not to declare the branch impossible.

Finally apply the existing collision/cross-edge repair after the root merge. Let `S` be all exposed selected outside labels and `E=V\(R union S)`. Collision blocks retain only their minimum deadline. Any selected--selected edge or root-selected tail edge that lies below a surviving deadline is charged once in `q` and every deadline it contaminates is omitted. The new root-merge rule omits every external deadline that could have been displaced. Hence for a surviving deadline attached to selected label `u`, no lighter competitor can have its other endpoint in `R union S`; every remaining lighter competitor has the form `{u,x}`, `x in E`. Distinct retained labels have disjoint such raw-edge blocks. This proves (5). `square`

### 3.1 Consequence for the old claims

The theorem statements of the repaired source chain survive, but the following literal proof sentence must be retired for `r>=3`:

`W(e)<=T_a,T_b  =>  e is selected at both endpoints`.

Accordingly the statuses should be read as

- Claim 302: `PROVED / SELF-AUDIT-REPAIR / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SUPPORTING / ...`;
- Claim 304: `PROVED / SELF-AUDIT-STRENGTHENING / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SOURCE-MATCHING-SUPPORT / ...`;
- Claim 301: proved only with Claims 302--309.

No source-level conclusion is downgraded after the same-run repair.

---

## 4. #26 HUNT THE SPORADIC CASE — mixed `r=3` skeletons

The `r=3` counterconfiguration above is the first place where precise root--root merging matters. I therefore checked the mixed skeleton requested by the handoff rather than merely patching that one example.

Take a repaired collision block `u` selected by roots 1 and 2, one root--root edge active at one or two endpoints, and one active cross edge involving the third root. There are only the following raw-edge possibilities.

### 4.1 Collision-block edges

The raw proposal edges `{v_1,u}` and `{v_2,u}` are themselves block deadlines. Retain the smaller deadline and omit the larger. The omitted same-block proposal edge is then too heavy to be a lighter competitor for the retained deadline. If one occurrence lies in a terminal rank omitted by the root-merge rule, the block may lose its retained constraint entirely; this only weakens an upper-bound necessary event and remains covered by Claim 303's bounded-omission estimate. The label equality still has its exact collision codimension.

### 4.2 Cross edge from the third root

The edge `{v_3,u}` has exactly two cases.

- If `u` is also exposed-selected by `v_3`, it is not a new cross-edge class; it enlarges the same collision block and increases `c` by one.
- If `u` is absent from `v_3`'s exposed prefix, then conditional on root 3's terminal threshold its raw value is a tail Uniform on `[T_3,1]`. If it lies below a surviving deadline at `u`, it is one active cross defect, charged once in `q`, and **every** deadline it can contaminate is omitted.

There is no third possibility.

### 4.3 Root--root edge

A root--root edge is disjoint as an undirected raw edge from every collision-block and selected-label cross edge because selected labels lie outside `R`. Under Claim 309 it is charged once if active at at least one endpoint. If two root--root edges are active at the same root, we do not decide their internal merged ordering: we simply omit the last two outside deadlines there. This is exactly the sporadic configuration which broke the old shortcut, and the terminal-prefix lemma of Claim 309 handles it deterministically.

### 4.4 One raw edge touching several constraints

A selected--selected or root-selected active edge can sit below two retained deadlines. It is still one raw edge and contributes one unit to `q`; all contaminated deadlines are omitted. Likewise one root--root edge can be endpoint-active at two roots, contributes one unit to `p`, and causes terminal omissions at both roots. Thus `K=c+q+p` counts **raw defect edges/equalities**, not the number of logical consequences of one defect.

### 4.5 No escaping mixed class

Every raw edge in the finite root/selected-label neighborhood belongs to exactly one of:

1. a root proposal edge in a collision block;
2. a selected--selected edge;
3. a root-to-selected-label tail edge at a nonowner root;
4. a root--root edge.

These endpoint-type classes are disjoint because selected labels are outside `R`. After the repaired omissions, any remaining edge relevant to rejection has one selected endpoint and one endpoint in the common external pool `E`. Therefore the mixed collision + root-merge + cross-edge skeleton introduces no extra defect class beyond `c,q,p`.

The branch found in Section 2 is therefore a repair to **how root--root defects are interpreted**, not evidence that `K` needs a fourth summand.

---

## 5. #18 SAY IT IN ANOTHER LANGUAGE — finite raw-edge sigma-field dependency diagram

The repaired fixed-root proof can now be stated as a finite dependency diagram with every independence attached to disjoint raw-edge families.

Fix roots `R={v_1,...,v_r}` and put `O=V\R`.

### Layer A — deleted root proposal arrays

For root `a`, let

`E_a^O={{v_a,x}:x in O}`

and let `F_a` be the sigma-field generated by the identities and values of its first `k` outside order statistics. The raw families `E_a^O` and `E_b^O` are disjoint for `a!=b`; hence the `F_a` are independent. Conditional on `F_a`, any named outside label absent from the exposed prefix has raw value independent Uniform`[T_a,1]`; jointly, finitely many such named tail edges are independent truncated Uniforms.

### Layer B — label partition

The equality partition `Pi` of the exposed outside labels is measurable with respect to the exposed identity arrays. Within each root the labels form a uniform injection; across roots the injections are independent. For a fixed partition with collision excess `c`, the exact probability is

`(N)_m / product_a (N)_k = n^{-c+o(1)}`.

Ordered identities are independent of the corresponding ordered values by iid exchangeability.

### Layer C — root--root merge sigma-field

Let

`E_RR={{v_a,v_b}:a<b}`.

This raw family is disjoint from every `E_a^O`, so its weights are independent of `vee_a F_a`. Conditional on the outside thresholds, Claim 309 reads only which unique edges satisfy `W(e)<=max(T_a,T_b)`. The resulting endpoint-activity sets determine terminal omission counts `d_a`; no assertion about exact internal root-edge merged ranks is needed.

### Layer D — local active selected-label edges

Given the label partition, let `S` be the exposed selected outside labels. The selected--selected raw edges lie in

`E_SS={{u,z}:u,z in S,u!=z}`,

which is disjoint from all root-incident raw edges. A root-to-selected-label edge `{v_b,u}` is either an exposed proposal edge belonging to a collision block, or a named tail edge of `E_b^O`; in the tail case its exact conditional law is Uniform`[T_b,1]`. Integrate the finite active-edge list first and record every deadline it can contaminate in the omission map.

### Layer E — deterministic omission map

The omission map is a deterministic function of:

- collision blocks and their minimum-deadline representatives;
- active selected--selected / root-selected cross edges;
- root--root endpoint-activity counts `d_a`.

It removes only `O_r(1)` deadlines for a fixed-complexity skeleton. Claim 303 therefore applies to the surviving arbitrary ranks and bounded quota shifts.

### Layer F — residual dissociated blocks

Set

`E=V\(R union S)`.

For each surviving retained selected label `u`, define

`B_u={{u,x}:x in E}`.

Conditional on the finite preceding data, the `B_u` are pairwise disjoint raw-edge sets, disjoint from the root arrays, root--root edges, and integrated active selected--selected edges. Hence the residual rejection blocks are **exactly independent**, not approximately independent. This is the only place the product factorization is used.

The diagram is therefore

`root outside arrays (independent)`
` -> label partition`
` + independent root-root raw edges -> endpoint activity -> terminal omissions`
` + finite selected-label active edges -> contaminated-deadline omissions`
` -> pairwise-disjoint residual B_u blocks`
` -> fixed-r joint isolation`
` -> factorial moments`
` -> Claim-305 finite Brun TV`
` + literal component elimination`
` -> connectivity`.

No sparse dependency graph for the unconditioned isolation indicators is asserted.

---

## 6. Probability bookkeeping after the repair

The only changed finite object is the root--root clause. The probability scale is unchanged.

For a witness-labelled repaired skeleton,

`K=c+q+p`,

where `p` now unambiguously counts **unique root--root edges active at at least one endpoint of the deleted-array threshold test**. On the fixed threshold guard:

- the label partition costs `n^{-c+o(1)}`;
- each unique active selected--selected/root-selected edge costs `n^{-1+o(1)}`;
- each unique active root--root edge costs `n^{-1+o(1)}`.

Witness choices are still only `k^{O_{r,K}(1)}=n^{o(1)}`. Claim 303 supplies

`exp[-rk+O_{C,r}(k^(2/3)+log k)]`

for the residual bounded-omission rejection event. Therefore every positive-complexity skeleton is

`e^{-rk+o(k)} n^{-1+o(1)} = o(e^{-rk})`.

The zero cluster has no active root--root edge, meaning every root--root raw edge exceeds both relevant deleted-array thresholds. Hence root--root reinsertion changes no proposal array at all. The lower sufficient event in Claim 306 is therefore unaffected. Claim 308 remains the clean one-root input at quota `h=k`, and Claim 305 remains the sole factorial-moment-to-TV conversion.

Thus for every fixed `C,r`, uniformly on `|k-log n|<=C`,

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`,

and the repaired source chain still gives

`d_TV(Law(Z_n),Poi(lambda_n))->0`, `lambda_n=n e^-k`,

and

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.

If `k-log n->c`, these specialize to `Z_n => Poi(e^-c)` in total variation and connectivity probability `exp(-e^-c)`.

---

## 7. Literal nontrivial-component audit

The root--root reinsertion issue above belongs to the fixed-root factorial-moment proof. It does not alter the component proof.

For candidate component sizes `2<=s<=6`, the proof deletes **all** internal candidate-set edges before ranking external proposals. The light spanning-tree event uses only internal raw weights, while external proposal/rejection events use only external raw weights; the two sigma-fields are disjoint. Claims 303--305 then give the external rejection bound, and the fixed-`s` union estimate remains

`n^{1-s+o(1)} k^{s-1} + n^{-2+o(1)} k^{s-1}=o(1)`.

For sizes `7<=s<=n/2`, Claim 306's one-global threshold envelope remains literal: with `a=5/32`, `b=32/5`, pay `P(H^c)=o(1)` once; fixed sizes 7--12 use exponent `1-as`, and the uniform 13+ tail uses `1-(a/2)s`, beginning at `-1/64` for `s=13`. A disconnected graph with no isolated vertex therefore has probability `o_C(1)`. No mean-degree inference is used.

---

## 8. What failed, what was repaired, and what remains external

The requested #2/#26 adversarial pass succeeded in finding a real proof-surface failure: for `r>=3`, being below both **deleted-array** `k`th thresholds does not force a root--root edge into both final top-`k` lists, because other root--root edges can push it back out. The first such sporadic branch occurs at `r=3`.

The repair is simpler than exact merged-rank casework: mark every root--root edge that lies below at least one deleted-array threshold, charge that **unique raw edge** once, and omit enough terminal outside deadlines at every endpoint it can affect. The deterministic prefix lemma proves those omissions cover every possible rank displacement. This restores the exact disjoint-block architecture without changing a probability exponent.

No other `r=2` or `r=3` raw-edge class escaped the repaired cluster datum. In particular, mixed collision/cross/root-edge skeletons still fall under `K=c+q+p`.

This remains a P03 self-audit. It does **not** satisfy either outside-audit slot. The source remains candidate-complete/audit-pending, not CLOSED.

---

## 9. Claim/status ledger delta and exact remaining obligation

New claim:

`P03-P0456-ROOT-MERGE-SIGMA-COMPLETENESS-309`

Status:

`PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Read the repaired chain as follows:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 301 remains proved only with Claims 302--309;
- Claim 302 is `ROOT-MERGE-CLAUSE-REPAIRED-BY-309`;
- Claim 304 is `ROOT-MERGE-CLAUSE-REPAIRED-BY-309`;
- Claim 308 remains the clean analytic input and is unchanged.

Frozen metrics remain:

- `c_LK^cert=0` — SATURATED;
- `a_LK^fine=0` — SATURATED;
- `b_LK^sqrt=0` — SATURATED;
- HARD recoveries `0/2`.

The exact closure obligation remains:

1. one genuine P26 end-to-end full-proof PASS on the repaired 288/289/301--309 source chain;
2. one genuinely distinct OTHER-track end-to-end full-proof PASS on the same chain;
3. only after both passes, create the self-contained paper package and request P26 closure via `ledger_delta`.

```yaml
ledger_delta:
  track: P03
  source: P0456
  source_claims:
    P03-P0456-POISSON-CRITICAL-WINDOW-288: "PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289: "PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-SOURCE-AUDIT-CAPSULE-301: "PROVED / SELF-AUDIT-CAPSULE / REPAIRED-BY-302-309 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302: "PROVED / SELF-AUDIT-REPAIR / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-REPAIRED-CLUSTER-BRUN-TV-304: "PROVED / SELF-AUDIT-STRENGTHENING / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308: "PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-ROOT-MERGE-SIGMA-COMPLETENESS-309: "PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
  metrics:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    saturation: true
    hard_recoveries: "0/2"
  outside_audits:
    P26: 0
    OTHER_distinct: 0
  newest_P26_screened:
    path: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_11-59-00__run-report.md
    blob: 481a3f44b96cdd9639a2fc5e24fb6370b76592e7
    target: R06 Romero max-minus-three, not P0456
  next_state: "P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_309_ROOT_MERGE_REPAIR_READY"
  paper_package: "NOT_CREATED"
```

---

## 10. Next-run attack

Reuse a nonconsecutive proof-simplification triple **#6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #25 COUNT THE SAME THING TWICE**. Do not return to correction coefficients or component-cut optimization unless an outside auditor identifies a source-level need.

1. Audit incoming P26/OTHER reports first; repair any source-chain objection before self-directed work.
2. **#6:** deform all root--root weights from `+infinity` down to their realized values one edge at a time. Prove a deterministic rank-stability lemma saying exactly how many terminal outside slots can change after each insertion, and compare it with Claim 309's simultaneous prefix bound.
3. **#10:** separate probability from combinatorics completely: state a deterministic finite "support deletion lemma" whose inputs are label partition, endpoint-active root-edge set, active selected-label edge set, and omission map, and whose conclusion is exact disjointness of the residual raw-edge blocks. Then the probabilistic proof should be only the codimension estimates plus Claim 308/303.
4. **#25:** derive the root--root merge omission rule twice: once by simultaneous rank counting and once by sequential insertion/exchange. Any disagreement identifies the next repair.
5. Keep the `r=3` counterconfiguration in the auditor-facing package so no future proof reuses the false both-end-impossible shortcut.
6. Freshly verify the Cambridge source/current literature and literal components; a bounded search miss is never a novelty certificate.

**End of complete run report.**