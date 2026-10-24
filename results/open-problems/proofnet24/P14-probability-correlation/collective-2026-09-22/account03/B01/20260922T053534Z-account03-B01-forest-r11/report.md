# FOREST / account03 B01 — exact STAR-2 split-conditioning representation

**Run:** `20260922T053534Z-account03-B01-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-STAR2-SPLIT-CONDITIONING-v1`  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof or novelty claim is made here.

## 1. Fresh source state used

The source target remains the Grimmett-Winkler unit law: for every finite simple graph `G`, choose uniformly from **all** acyclic edge subsets (empty, disconnected and every size included), and prove pairwise edge negative correlation.

The latest complete campaign-lead report available to this run is account01/B01

`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T050946Z-b01-forest-auto11/report.md`, blob `cd6fde1f2bd0c68f7372629e7d4fbee9f8df5f92`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`.

That report correctly withdraws the earlier fixed-graph Cocks globalization: the available class-level theorem does not justify `unit-good G => weighted-good same G`. The surviving source-safe lead argument is:

1. choose a simple counterexample with the minimum number of edges and a positively correlated pair `e,f`;
2. conditioning on any third edge `g` that lies in no triangle stays inside smaller **simple** graphs after deletion/contraction, so exact total covariance yields the Simpson inequality there;
3. rank-homogeneous complete log concavity supplies a global correlation/susceptibility budget;
4. if `g=uv` lies in triangles, contraction creates multiplicity-two classes only on the star of the contracted vertex `x`;
5. the first missing implication is the lead's `STAR-2` comparison: prove the marked pair nonpositively correlated in that smaller simple contraction when those source-generated star edges have weight 2 and all other edges have weight 1.

I also consumed the exact named partner result account04/B02

`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T051158Z-account04-B02-forest-r12/report.md`, blob `cc992f69b6c61b629f992fc360f24ce97c36ebf9`.

It proves that **every fixed-radius same-k path-cut/join Hall support fails on some simple graph**, including a 3-connected six-vertex positive-gap witness for radius two. I use that result below to rule out treating the new conditional representation with another bounded-radius local switch.

## 2. New theorem: STAR-2 is exactly a source-law disconnection conditioning

The lead's weighted contraction can be removed from the statement entirely.

### Proposition 1 (split/contraction identity)

Let `J` be a finite simple graph and let `u,v` be distinct **nonadjacent** vertices. Identify `u` and `v` to one vertex `x` and simplify the resulting multigraph to a simple graph `H`. For every edge class `a` of `H`, let `m_a` be its number of preimages in `J`. Then:

- `m_a=1` off the star of `x`;
- `m_{xw}=2` exactly when `w` is adjacent to both `u` and `v` in `J`;
- otherwise `m_{xw}=1`.

For a forest `K` of `H`, put

`m(K)=product_{a in K} m_a`.

Then contraction induces the exact counting identity

`# {F forest of J : u not connected to v in F, projection(F)=K} = m(K)`.

Consequently the projection of the **uniform** forest law of `J`, conditioned on `u` and `v` being disconnected, is exactly the weighted forest law on `H` with edge weights `m_a in {1,2}`.

### Proof

Take a forest `F` of `J` with `u` and `v` disconnected. It cannot contain both edges `uw` and `vw` for a common neighbor `w`, because those two edges alone would connect `u` to `v`. Identifying `u,v` therefore selects at most one preimage from every contraction class. Identification cannot create a cycle: if the quotient contained a cycle, lifting it would either give a cycle in `F` or a path from `u` to `v`, both impossible. Hence the projection is a forest `K` of `H`.

Conversely, take a forest `K` of `H`. For each selected class `a` independently choose one of its `m_a` preimages. Every such lift is acyclic: a lifted cycle would project to a cycle of `K`; and a lifted `u-v` path would become a cycle after identifying its endpoints. Therefore every lift is a forest with `u` and `v` disconnected. Different preimage choices give different forests, and there are exactly `product_{a in K}m_a` choices. This proves the identity. QED.

This is an exact unrooting statement: no rooted-forest law, fixed-size law, asymptotic limit or external-field approximation is used.

### Marked-edge sign transfer

Let original marked edges `e,f` of `J` project to distinct classes `a,b` of `H`, with multiplicities `m_a,m_b`. Conditional on the projected forest, a selected class chooses its preimage uniformly and independently across distinct classes. Therefore

`P_J(e | u !~ v) = P_H^m(a)/m_a`,

`P_J(e,f | u !~ v) = P_H^m(a,b)/(m_a m_b)`,

and hence

`Cov_J(1_e,1_f | u !~ v) = Cov_H^m(1_a,1_b)/(m_a m_b)`.

Thus the covariance sign is identical. If `e,f` collapse to the **same** doubled class, the conditioning event makes them mutually exclusive, so their conditional covariance is automatically nonpositive.

## 3. Exact application to the lead's STAR-2 debt

Return to the lead's edge-minimal simple counterexample `G` and a triangle conditioner `g=uv`. Put `J=G\g`. Since `J` has fewer edges than `G`, it is a smaller simple source instance. The event

`A_g = {u not connected to v in the chosen forest of J}`

is exactly the event that `g` is addable.

Contracting `g` and simplifying gives the lead's graph `H`: every common neighbor of `u,v` produces one weight-two star edge at the contracted vertex, and every other edge has weight one. Proposition 1 therefore gives the equivalence

**STAR-2 on H**

`<=>`

**conditional source inequality on J**

`Cov_J(1_e,1_f | A_g) <= 0`,

with only the trivial same-class exception already settled negatively.

In exact count form, if `N_A,N_{eA},N_{fA},N_{efA}` count uniform forests of `J` in the addability/disconnection event, the missing implication is

`N_{eA} N_{fA} - N_A N_{efA} >= 0`.                         `(SPLIT-STAR)`

This does **not** prove the implication. It does sharpen it in two ways:

1. the weighted contraction is now represented entirely inside the original source model on a smaller simple graph;
2. it identifies the extra structure that unit minimality still does not pay for: preservation of pairwise negative correlation after conditioning on one global two-terminal disconnection/addability event.

So the lead's current obstacle is not "arbitrary star weights" in isolation. It is the source-native conditional inequality `(SPLIT-STAR)`.

## 4. Second exact representation: delete the star center first

The same weighted law has a component-factor representation that may be useful for a determinant/integral attack.

Let `H` be any simple graph with distinguished vertex `x`. Give the star edge `xw` weight `r_w>0` and all nonstar edges unit weight. Let `K=H-x`. For a forest `R` of `K`, write its connected components as `C`. Once `R` is fixed, an acyclic extension may choose **at most one** edge from `x` into each component `C`. Therefore the exact unrooted partition function is

`Z_H(r) = sum_{R forest of K} product_{C component of R} (1 + sum_{w in C, xw in E(H)} r_w)`.       `(CF)`

For STAR-2, every `r_w` is 1 or 2. Formula `(CF)` keeps every forest size and every disconnected base forest. It is not the ordinary rooted matrix-forest determinant: the additive `1` is one **component-level** no-star choice, not one root choice per vertex.

For a marked star edge `a=xu`, its numerator is obtained by forcing the component containing `u` to choose `a`:

`Z_a = r_u sum_R product_{C != C_R(u)} (1+s_C)`,

where `s_C=sum_{w in C} r_w` over star neighbors. For two marked star edges `a=xu,b=xv`, only base forests with `C_R(u) != C_R(v)` contribute, and the two corresponding component factors are removed. These identities are exact and give a concrete component-partition interface for the remaining sign problem.

## 5. Named partner result applied: bounded-radius switching is now ruled out here too

The account04/B02 theorem is directly relevant to `(SPLIT-STAR)`. Its family shows that for every fixed radius `R`, a same-k path-cut/join support can have a Hall-deficient left subset even when the **true global Rayleigh gap is zero**; it also supplies a 3-connected six-vertex radius-two failure with positive gap 658.

Under Proposition 1, STAR-2 is a global conditioning on `u !~ v`. A bounded-radius attempt that only repairs this conditioning by cutting and joining within a fixed distance is therefore exactly the kind of local support the partner has shown cannot be universal. A viable coupling for `(SPLIT-STAR)` must be geometry-adaptive/unbounded, or must use a different global support/flow/integral mechanism. Merely increasing a fixed radius is not a permissible surviving universal strategy.

## 6. New exact counterexample to a tempting STAR-2 monotonicity lemma

Another natural repair would be:

> if the unit Rayleigh gap is nonnegative, increasing one star-edge weight from 1 toward 2 cannot decrease that gap.

That claim is false.

Take the six-vertex simple graph with edge list

`(05),(01),(14),(04),(24),(45),(13),(03),(12),(15),(35),(25)`.

Use marked edges

`e=(05)`, `f=(12)`,

and vary only the star edge

`h=(15)`

at center `1`, with weight `t`. Exact forest enumeration gives

`Z(t)    = 722 + 292 t`,

`Z_e(t)  = 244 + 72 t`,

`Z_f(t)  = 268 + 82 t`,

`Z_ef(t) = 86 + 20 t`.

Therefore

`Delta(t)=Z_e Z_f-Z Z_ef = 3300 - 248 t + 64 t^2`.

In particular

`Delta(1)=3116`,

`Delta(2)=3060 < 3116`.

So coordinatewise monotonicity of the Rayleigh gap under star doubling is refuted. The gap stays positive here, so this is **not** a counterexample to STAR-2 or to the parent FOREST conjecture; it only eliminates a proof mechanism.

## 7. Exact finite diagnostics

The accompanying standard-library checker uses integer arithmetic only.

It exhaustively verifies Proposition 1 for every simple graph on at most five vertices and every nonedge split pair:

- 5,325 `(J,u,v)` instances;
- 103,481 conditional forests counted through the exact contraction multiplicities;
- zero identity failures.

It also exhaustively checks every nonempty `{1,2}` star-weight assignment on every simple graph on at most five vertices:

- 21,400 weighted graph/star instances;
- 319,554 distinct marked-edge pair checks;
- no negative Rayleigh gap.

This is finite evidence only, not a theorem beyond the enumerated range. The monotonicity witness above is checked in the same script. Captured output terminates `ALL_EXACT_ASSERTIONS_PASSED`.

Checker SHA-256: `6749528ce234ee51572edee09629159222b9f344584cc84b41d9977a524f6255`.  
Captured-output SHA-256: `f345cf9f484baffb43e99cb0209243b52562bda0a408c29489ac12f5366419b5`.

## 8. First remaining universal implication

The new source-native missing statement is now:

> **SPLIT-STAR conditional inequality.** In the edge-minimal-counterexample configuration of the lead, for every triangle edge `g=uv` distinct from the marked pair, the smaller simple graph `J=G\g` satisfies
>
> `Cov_J(1_e,1_f | u !~ v) <= 0`.

Unconditional negative correlation in `J` follows from edge-minimality, but unconditional pairwise NC alone does not automatically imply NC after this global disconnection conditioning. That conditional-preservation step is the precise unpaid implication.

Formula `(CF)` supplies one exact component decomposition for attacking it. The partner theorem rules out a universal fixed-radius path-cut/join Hall proof, and the six-vertex witness rules out coordinatewise gap monotonicity under star doubling. The next useful mechanism should therefore be a global component coupling/flow or a genuinely source-valid integral inequality for `(CF)`, not another local-radius or monotonicity argument.

## 9. Status

**Outcome: `ESSENTIAL_STEP_APPLIED`.**

The old `FOREST-KN-COCKS-RECONCILED-v3` full-candidate chain is no longer current because its fixed-graph globalization was withdrawn by the lead. The parent Grimmett-Winkler conjecture remains OPEN. This run contributes an exact unrooting/splitting theorem that converts the lead's STAR-2 weighted contraction debt into a conditional inequality in a smaller simple source graph, an exact component-factor formula, and an exact counterexample eliminating a tempting monotonicity proof route.
