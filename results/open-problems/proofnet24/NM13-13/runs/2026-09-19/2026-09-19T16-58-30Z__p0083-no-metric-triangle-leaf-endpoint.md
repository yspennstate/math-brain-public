Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `A_whisker_cert: 2 -> 2`; actual Section-B methods tried: #7 TAKE THE LIMIT, #21 ASK WHO ELSE HAS THIS SHAPE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# NM13-13 — P0083: exact attached-triangle endpoint obstruction at alpha = 4/3

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-13` / `proofnet24/NM13-13/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0083 / `operations/claims/P0083.md`**  
Canonical dedup key: `sharp_reinforcement_threshold_for_warm_whiskers`  
Canonical shard: **12 mod 13**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED**

## 1. Frozen target, metric, and outcome

The admitted source remains Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Open Problem 13. In the finite graph WARM with uniform firing rates, it asks to improve the sufficient threshold `alpha > 25` under which every connected component of the support of a not-linearly-unstable equilibrium is a whisker, i.e. a tree of diameter at most three. The source explicitly points to the triangle transition at `4/3` and says that perhaps `alpha > 4/3` is sharp.

The frozen metric remains

`A_whisker_cert`

= the smallest strict **universal** sufficient threshold certified on this track in the exact source scope.

History remains

`25 -> 22 -> 43/5 -> 6 -> 2`.

This invocation proves a new exact endpoint obstruction for the smallest attached odd-unicycle motif, but it does **not** prove the universal source theorem below `2`. Therefore:

- metric before: `2`;
- metric after: `2`;
- movement: **none**;
- source status: **PARTIAL / OPEN**;
- unchanged substantive runs since the last metric movement: **4 -> 5**;
- HARD stuck-recovery episodes consumed: **1/2 -> 1/2**;
- P26 audit: **NOT_DONE**;
- NM13-01 audit: **NOT_DONE**.

Because the frozen metric remains unchanged after recovery episode #1 and the no-movement streak remains beyond the Section-I threshold, I treat the **next invocation as mandatory stuck-recovery episode #2**, a thinking/recovery run with no new theorem claim unless the controlling owner policy changes first. A later third stuck episode would require preserved handoff and rotation.

## 2. Runtime and scheduler-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`, but this invocation actually runs as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a guaranteed hour-long execution, or a support escalation.

The exposed task-control schema still offers task title/prompt, schedule or relative-start fields, timing mode, enabled state, listing, and update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated completed-run applied-model/applied-effort receipt**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/admin/API scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` is not evidence of a current global impossibility: current root `RESULTS.md` records that a full P26 update later succeeded from an authorized context. If such a denial recurs, the lawful workaround is the same task's owning or otherwise authorized product/workspace/admin/API context, supported ownership/permission repair, or authorized platform support. It is not duplication, identity substitution, or permission bypass. This invocation did not modify or probe any scheduler or permission.

## 3. Authoritative continuity and required repository reads

The controlling predecessor is

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T15-06-00Z__p0083-stuck-recovery1-finite-motif-deformation-atlas.md`

created at commit

`555540ce41e9af5ed7a69f9237249e102edac5c4`.

That report consumed stuck-recovery episode #1, retained `A_whisker_cert=2`, and selected the exact next special case: the triangle with one pendant leaf at the endpoint `p=3` (`alpha=4/3`). It reserved methods #7/#21/#23 for this invocation and did not mark them tried.

Before new mathematics I freshly read or recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor and the earlier P0083 reports needed for the exact route history;
- current `operations/claims/P0083.md`;
- targeted intake/attempt/claim/audit searches;
- current neighboring NM13-12 and designated secondary-auditor NM13-01 reports.

The current canonical claim still records owner NM13-13, category HARD OUTSIDE, status ACTIVE, canonical key `sharp_reinforcement_threshold_for_warm_whiskers`, SHA-256 `7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`, and residue `12 mod 13`. Fresh audit search still finds no actual P26 or NM13-01 P0083 audit. Neither audit is presumed complete.

The append-only intake/attempt corpora are too large to honestly claim that every unchanged byte was rendered model-visible in one invocation. I make no such claim. P0083's canonical identity, source, active claim, historical attempted-unsolved record, newest own continuity, neighboring state, and current ownership were directly recovered; missing bulk display was not treated as permission to reset history.

## 4. Prewrite Git delta and own artifacts

Immediately before report construction, after the two substantive self-check artifacts below had been created, `master` was observed at

`43874c543ee8f3e58e146b1d2f53d2247f8116fb`.

The exact comparison

`555540ce41e9af5ed7a69f9237249e102edac5c4 .. 43874c543ee8f3e58e146b1d2f53d2247f8116fb`

reported:

- status `ahead`;
- **211 commits ahead**;
- **0 commits behind**;
- total commits **211**.

Concurrent fleet work is heavy, so commit count alone is not used as lifecycle evidence. Current direct reads/searches show no P0083 release, reassignment, retirement, source correction, or completed P26/NM13-01 audit.

This run created only the following substantive artifacts in its own namespace:

- `proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.py`, creation commit `9f755adfd7eb17af86264beecd9345064189ad16`;
- `proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.out`, creation commit `43874c543ee8f3e58e146b1d2f53d2247f8116fb`.

The archived output ends `EXACT_SELF_CHECK_PASS`. It is explicitly a **self-check**, not either required independent audit.

## 5. Fresh source and bounded literature check — 2026-09-19

This is bounded current-status evidence only, not proof of worldwide openness, novelty, or priority.

### 5.1 Current source

The current MATRIX source PDF was reread directly, including the rendered pages containing Open Problems 12 and 13:

`https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`

The source states the finite-graph facts used by this track:

- for `alpha>2`, support components of a not-linearly-unstable equilibrium are trees;
- for `alpha>25` and uniform firing, they are whiskers;
- Open Problem 13 asks to improve `25`;
- the triangle has its edge-loss transition at `4/3`;
- the authors say perhaps `alpha>4/3` is sharp.

### 5.2 Published baseline and nearest exact small graph

Holmes--Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, DOI `10.1063/1.4978683`, still states the finite-graph published baseline `alpha>2` for forest support and `alpha>25` for whisker-forest support.

Van der Hofstad--Holmes--Kuznetsov--Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, Ann. Appl. Probab. 26 (2016), 2494--2539, is the finite-graph equilibrium/stability source containing the small-graph phase-transition analysis behind the `4/3` triangle scale.

### 5.3 Method #21: who else has this spectral shape?

The closest classical graph-spectral analogue recovered is Cardoso--Cvetković--Rowlinson--Simić, *A sharp lower bound for the least eigenvalue of the signless Laplacian of a non-bipartite graph*, Linear Algebra Appl. 429 (2008), 2770--2780, DOI `10.1016/j.laa.2008.05.017`. For fixed order, their extremal connected non-bipartite graph is a triangle with a path attached to one vertex. Follow-up signless-Laplacian work orders non-bipartite unicyclic graphs with pendant vertices, e.g. Guo--Liu--Zhang--Yu, J. Inequal. Appl. 2016:136, DOI `10.1186/s13660-016-1077-1`.

This is a genuine shape match, not an imported proof. The WARM Gram/signless-incidence matrix has nonlinear equilibrium-dependent weights and normalization; the classical unweighted `Q=D+A` extremal theorem does not imply the WARM stability inequality.

### 5.4 Dated bounded queries

Queries included exact title/problem phrases for the MATRIX source, Holmes--Kleptsyn `alpha 25`/`alpha 2`, the 2016 graph-WARM triangle transition, and least-signless-Laplacian non-bipartite unicyclic graphs with pendants. No checked later primary source establishing a universal finite uniform-firing WARM whisker threshold below `25` was recovered. That is negative bounded evidence only.

## 6. Setup at the endpoint

Use the potential parametrization already derived on this track. Put

`p = 1/(alpha-1)`,

so

`alpha=(p+1)/p`, `h=(alpha-1)/alpha=1/(p+1)`.

For a positive-support edge `uv`,

`w_uv=(A_u+A_v)^(-p)`,

`q_{uv,v}=A_v(A_u+A_v)^(-(p+1))`,

and the equilibrium equations are

`A_v sum_{u~v}(A_u+A_v)^(-(p+1)) = 1`.                         (6.1)

The normalized incidence matrix is

`C_{v,uv}=A_v(A_u+A_v)^(-(p/2+1))`.                           (6.2)

A not-linearly-unstable equilibrium must satisfy

`C^T C >= (1/(p+1)) I`.                                       (6.3)

This run takes the exact endpoint `p=3`, equivalently `alpha=4/3`, on the graph consisting of a triangle `r-a-b-r` plus one pendant leaf `ell` attached to `r`.

## 7. Method #7 TAKE THE LIMIT: exact endpoint theorem for the attached triangle

### Claim `NM13-13-P0083-TRIANGLE-LEAF-ENDPOINT-11`

**Theorem.** Let the positive support be exactly a triangle with one pendant leaf, with uniform firing rates. At `alpha=4/3` (`p=3`), every full-support WARM equilibrium is linearly unstable.

This is an exact endpoint theorem for one source-relevant non-whisker motif. It is not the universal Open Problem 13 theorem.

### 7.1 Leaf coordinate and two triangle ratios

Let the pendant leaf be `ell`, attached to triangle vertex `r`. Because `ell` has support degree one,

`q_{r ell,ell}=1`.

Put

`q := q_{r ell,r}`.

At `r`, the three positive incidences sum to one, so

`0<q<1`.

From the leaf equation, `q=A_r/A_ell`, and therefore

`K := A_r^(-3) = (1+q)^4/q^3`.                                (7.1)

Write

`u=A_a/A_r`, `v=A_b/A_r`.

The two triangle incidences at `r` are

`x=K/(1+u)^4`, `z=K/(1+v)^4`,                                (7.2)

with

`q+x+z=1`.                                                     (7.3)

Since `x,z<1`, (7.1)--(7.2) imply

`1+u > (1+q)/q^(3/4) > 2`,

and likewise for `v`; hence

`u>1`, `v>1`.                                                  (7.4)

The strict middle inequality follows from `1+q>2 sqrt(q)>2q^(3/4)` for `0<q<1`.

### 7.2 Endpoint equilibrium forces reflection symmetry

The equilibrium equations at `a` and `b`, divided by the common positive factor `K`, are

`u/(1+u)^4 + u/(u+v)^4 = 1/K`,

`v/(1+v)^4 + v/(u+v)^4 = 1/K`.

Subtracting gives

`F(u,v):=u/(1+u)^4-v/(1+v)^4+(u-v)/(u+v)^4=0`.                (7.5)

Exact factorization gives

`F(u,v)=-(u-v)B(u,v)/[(1+u)^4(1+v)^4(u+v)^4]`.                (7.6)

To determine the sign of `B`, put `u=1+X`, `v=1+Y`. The exact numerator is

`B(1+X,1+Y) =`
`X^7Y+X^7`
`+5X^6Y^2+21X^6Y+16X^6`
`+11X^5Y^3+83X^5Y^2+184X^5Y+112X^5`
`+13X^4Y^4+143X^4Y^3+544X^4Y^2+832X^4Y+416X^4`
`+11X^3Y^5+143X^3Y^4+736X^3Y^3+1808X^3Y^2+2064X^3Y+848X^3`
`+5X^2Y^6+83X^2Y^5+544X^2Y^4+1808X^2Y^3+3184X^2Y^2+2768X^2Y+896X^2`
`+XY^7+21XY^6+184XY^5+832XY^4+2064XY^3+2768XY^2+1792XY+384X`
`+Y^7+16Y^6+112Y^5+416Y^4+848Y^3+896Y^2+384Y`.               (7.7)

Every coefficient is a positive integer. By (7.4), `X,Y>0`, hence `B>0`. Equations (7.5)--(7.6) force

`u=v=:t`.                                                       (7.8)

Thus reflection symmetry is a theorem at the critical endpoint; it is not imposed as an ansatz.

### 7.3 Full support forces `q>1/3`

By (7.3) and (7.8),

`x=z=(1-q)/2`.                                                  (7.9)

Combining this with (7.1)--(7.2) gives

`(1+t)^4 = 2(1+q)^4/[q^3(1-q)]`.                              (7.10)

At vertex `a`, the triangle edge `ab` has positive incidence

`y=1-tx=1-t(1-q)/2>0`.                                        (7.11)

I claim this forces `q>1/3`. Suppose instead `q<=1/3`. From (7.10), the inequality

`t >= 2/(1-q)`

is equivalent, after taking positive fourth powers, to

`2(1+q)^4(1-q)^3 >= q^3(3-q)^4`.                              (7.12)

The difference factors exactly as

`2(1+q)^4(1-q)^3-q^3(3-q)^4 = -(3q-1)P(q)`,                  (7.13)

where

`P(q)=q^6-3q^5+15q^4-33q^3+18q^2+8q+2`.

For `0<q<=1/3`,

`2+8q+18q^2-33q^3 >= 2+8q+7q^2>0`

and

`q^4(15-3q+q^2)>0`,

so `P(q)>0`. Since `3q-1<=0`, (7.13) proves (7.12), hence `t(1-q)/2>=1`, contradicting (7.11). Therefore

`q>1/3`.                                                        (7.14)

### 7.4 A two-coordinate spectral witness

For `p=3` define the conductance of support edge `uv` by

`c_uv=A_u A_v/(A_u+A_v)^5`.

From (6.1)--(6.2),

`CC^T = I-L_c`,                                                (7.15)

where `L_c` is the weighted graph Laplacian with conductances `c`.

The attached triangle is unicyclic, so its support has the same number of vertices and edges and `C` is square. Necessary non-instability at `p=3` would imply all eigenvalues of `CC^T` are at least `1/4`; by (7.15) this requires

`lambda_max(L_c) <= 3/4`.                                      (7.16)

By symmetry, each of the two root-to-triangle conductances equals

`a = t(1-q)/[2(1+t)]`,                                         (7.17)

while the pendant conductance is

`d=q/(1+q)`.                                                    (7.18)

Take the vector that is `+1` at `r`, `-1` at `ell`, and `0` at the other two triangle vertices. Its exact Rayleigh quotient for `L_c` is

`R = a+2d`
`  = t(1-q)/[2(1+t)] + 2q/(1+q)`.                             (7.19)

I now show `R>3/4`.

If `q>=3/5`, then `2q/(1+q)>=3/4` and `a>0`, so the inequality is strict.

Assume `1/3<q<3/5`. Put

`D(q)=-2q^2+5q-1`.

Here `D(q)>0`, and exact simplification of (7.19) shows

`R>3/4  <=>  t > (3-5q)/D(q)`.                                (7.20)

Using (7.10), (7.20) is equivalent to

`D(q)^4 > 8q^3(1-q)^5`.                                       (7.21)

The difference factors as

`D(q)^4-8q^3(1-q)^5=(3q-1)Q(q)`,                              (7.22)

with

`Q(q)=8q^7-64q^6+216q^5-368q^4+307q^3-107q^2+17q-1`.

It remains only to certify `Q(q)>0` on `[1/3,3/5]`. Under the affine substitution

`q=1/3+(4/15)s`, `0<=s<=1`,

the degree-seven Bernstein coefficients of `Q` are exactly

`896/2187,`
`15616/25515,`
`1408/1575,`
`447296/354375,`
`1009024/590625,`
`52352/23625,`
`907136/328125,`
`260416/78125`.

Every coefficient is strictly positive, so `Q(q)>0` throughout the interval. Since `q>1/3`, (7.22) is strict, hence (7.21), (7.20), and finally

`R>3/4`.                                                        (7.23)

Thus `lambda_max(L_c)>3/4`, contradicting the necessary non-instability condition (7.16). Every full-support equilibrium on the triangle with one pendant leaf is therefore linearly unstable at `alpha=4/3`. QED.

## 8. Methods #21 and #23: what the theorem changes

### #21 ASK WHO ELSE HAS THIS SHAPE

The classical least-signless-Laplacian literature independently singles out exactly the same topological family—an odd triangle with a pendant path—as extremal among connected non-bipartite graphs under several constraints. That strongly supports treating attached odd cycles as the next spectral objects rather than returning to local majority inequalities.

What transfers: the usefulness of eliminating pendant branches and looking for a low-dimensional eigenvector localized near the odd core.

What does **not** transfer: a classical `Q=D+A` eigenvalue bound. WARM conductances are nonlinear functions of the unknown equilibrium potentials, so source-valid proof still needs the equilibrium equations.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT

Instead of trying immediately to prove the entire `alpha>4/3` conjectural endpoint, I assumed the first attachment to the critical triangle might preserve a full-support endpoint equilibrium and tried to make that candidate stable. The attempt fails twice, exactly:

1. equilibrium itself forces the two triangle ratios to be equal;
2. once symmetry is forced, the root-vs-leaf mode has Laplacian Rayleigh quotient strictly above the stability ceiling.

Thus the bare triangle is not merely one example where `4/3` appears. Its first pendant perturbation already loses the critical mode in the unstable direction.

## 9. Exact self-check

The checker

`proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.py`

was inspected and executed locally using exact SymPy integer/rational algebra. It verifies:

1. factorization (7.6) and positivity of all **42** shifted coefficients in (7.7);
2. factorization (7.13);
3. factorization (7.22);
4. the eight exact Bernstein coefficients proving `Q>0`.

Archived output:

`proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.out`

ends

`EXACT_SELF_CHECK_PASS`.

This is a self-check of the finite algebraic core. It is not P26 or NM13-01 independent verification.

## 10. Why the universal metric does not move

The theorem eliminates exactly one minimal attached odd-unicycle motif at the conjectural endpoint. The source asks for **every** finite graph and every not-linearly-unstable equilibrium. The prior structural reductions leave two infinite families below `alpha=2`:

1. diameter-at-least-four trees, especially low-endpoint branched trees;
2. odd unicycles with arbitrary attachments and longer odd cores.

This invocation does not prove a reduction from those families to the triangle-plus-one-leaf motif. Therefore `A_whisker_cert` stays `2`. It would be dishonest to relabel a subclass theorem as universal threshold movement.

The most promising route exposed by this endpoint proof is an exact **pendant-elimination inequality** for the equilibrium-dependent signless/Gram matrix: show that any pendant attachment to a non-bipartite unicyclic core strictly pushes the relevant WARM stability eigenvalue in the unstable direction, with equality possible only for the bare triangle as `p -> 3`. Cardoso-type extremal arguments suggest the right shape but cannot supply the nonlinear WARM step.

## 11. Next-step / stuck protocol

Because the universal metric has now stayed at `2` for five consecutive substantive runs and recovery episode #1 did not move it, the next invocation is reserved as **Section-I stuck recovery #2**, with no new theorem claim.

The exact blocker for that recovery is:

`for every 1<=p<3 and every positive equilibrium on a non-whisker tree or odd unicycle, prove lambda_min(C^T C)<1/(p+1)`.

The recovery should compare exactly three genuinely different unused or sufficiently nonrepeated mechanisms and choose one action allowed by Section I. The concrete candidate action is to **port the pendant-path extremal mechanism from signless-Laplacian theory**, but only after deriving a source-valid weighted pendant-elimination inequality from the WARM equilibrium equations. If that second recovery still leaves the same universal obligation and a later third stuck episode occurs, preserve a full handoff and rotate rather than continue indefinitely.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-13
  namespace: proofnet24/NM13-13/
  category: HARD_OUTSIDE
  source_id: P0083
  canonical_claim: operations/claims/P0083.md
  canonical_dedup_key: sharp_reinforcement_threshold_for_warm_whiskers
  shard_residue_mod_13: 12
  source_status: OPEN
  track_status: PARTIAL
  metric:
    name: A_whisker_cert
    before: "2"
    after: "2"
    movement: false
  new_claim:
    id: NM13-13-P0083-TRIANGLE-LEAF-ENDPOINT-11
    scope: "At alpha=4/3, every full-support equilibrium on a triangle with one pendant leaf is linearly unstable."
    status: PROVED_MATHEMATICALLY_SELF_CHECKED_NOT_INDEPENDENTLY_AUDITED
  methods:
    - number: 7
      name: TAKE_THE_LIMIT
      outcome: "SUCCESS: exact p=3 endpoint theorem for triangle+pendant."
    - number: 21
      name: ASK_WHO_ELSE_HAS_THIS_SHAPE
      outcome: "USEFUL_NO_DIRECT_TRANSFER: classical least-signless-Laplacian extremals identify triangle+pendant-path shapes, but WARM weights are nonlinear."
    - number: 23
      name: DO_WHAT_THE_PROPOSER_DID_NOT_EXPECT
      outcome: "SUCCESS: treating the first attached triangle as a possible endpoint survivor forces symmetry and then an explicit unstable root/leaf mode."
  exact_artifacts:
    checker: proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.py
    output: proofnet24/NM13-13/artifacts/2026-09-19/p0083_triangle_leaf_endpoint_exact_selfcheck.out
    output_status: EXACT_SELF_CHECK_PASS
  audits:
    P26: NOT_DONE
    NM13-01: NOT_DONE
  unchanged_substantive_runs:
    before: 4
    after: 5
  hard_recoveries_consumed:
    before: "1/2"
    after: "1/2"
  next_run: "MANDATORY_SECTION_I_RECOVERY_2_THINKING_NO_NEW_CLAIM"
  next_blocker: "Uniform weighted pendant-elimination or equivalent spectral witness for all non-whisker trees and odd unicycles on 1<=p<3."
  literature_check_date: 2026-09-19
  literature_scope: "MATRIX source OP13; Holmes-Kleptsyn 2017; van der Hofstad et al. 2016; signless-Laplacian unicyclic pendant extremal literature; bounded current exact-title/threshold queries."
  closure_claimed: false
```

No shared root, peer namespace, scheduler, workflow, permission, email/Drive resource, public surface, or paid compute was modified. The only GitHub writes before this immutable report were the two substantive exact self-check artifacts in `proofnet24/NM13-13/`.
