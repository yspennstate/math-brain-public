# FOREST account02/B01 — fixed-graph Cocks upgrade pays the contraction debt and removes proper 2-separators

Run: `B01-20260922T021602Z-forest-r12`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent target: **not promoted by this run**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Scope and exact inherited state

Target: for every finite simple graph `G`, a uniformly random acyclic edge subset must satisfy pairwise negative edge correlation.

This run follows the assigned alternative separator/deletion-contraction route. It does **not** reopen installation or benchmark work.

Essential inherited items actually consumed:

- Team-lead candidate `FOREST-KN-HERMITE-REDUCTION-v1` (account01/B01 handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`) and the complete independent account04/B03 review `20260922T014020Z-B03-r43`, report blob `9851f9a7488f7edfe28e9273191551712fc297fc`.
- account01/B03's overlap/deletion-contraction analysis: its first unpaid implication was the sign of the contraction-side conditional gap `D1`; without a weighted contraction theorem the exact identity only gave a debt term.
- account02/B03 `FOREST-2SEP-WEIGHTED-TRANSFER-v1`, blob `5001e9cc0fb18f77c85ad0bb99d100da5937a1c0`, and corrected `FOREST-BOUNDARY-DISCRIMINANT-v2`, blob `abf745feb0430529ebc4ce68458ea99c6d8c4f3f`. These are taken as exact transfer identities, not rederived as new work here.

The named partner `account03/B02` was not present in the canonical collective archive at the fresh main snapshot available to this run. I did not wait. A named **OTHER-account** result was consumed and applied instead: account04/B03's complete end-to-end review above, specifically its source check of the fixed-graph Cocks theorem.

There was a genuine source-scope conflict in inherited work. One earlier account01/B03 report treated Cocks as only a class-level equivalence. The later account04/B03 review checked the final note of Semple--Welsh and found the stronger fixed-graph statement. I independently checked the public primary-source text of Semple--Welsh, *Negative Correlation in Graphs and Matroids*, p. 13, which states that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. This fixed-graph form is the only external theorem used below.

## 2. Conditional end-to-end route for this mechanism

Assume, for contradiction, a lexicographically minimal simple counterexample `(G,e,f)`, first by `|V(G)|`, then by `|E(G)|`, after discarding isolated components.

The intended route is:

1. every smaller simple graph is unit-edge pNC for every pair by minimality;
2. fixed-graph Cocks therefore upgrades **each such smaller graph separately** to all-positive-weight independence correlation;
3. use that upgrade to pay the exact weights created by one-edge contraction and by a proper two-terminal separator;
4. conclude that a minimal counterexample has no proper 0-, 1-, or 2-separation and that every third-edge contraction conditional gap is nonnegative;
5. feed this into the exact overlap identity, leaving only a 3-connected core with strict quantitative all-third-edge sign forcing.

This run proves steps 2--5. It does not prove that the remaining 3-connected core is impossible, so it is not a second full proof.

## 3. First essential missing implication: contraction-side `D1 >= 0`

Let `g=uv` be any third edge, distinct from `e,f`. Condition a uniform forest of `G` on containing `g`, then contract `g`.

Because `G` is simple, `G/g` has no loops coming from another `uv` edge. Its only nonsimple features are parallel pairs: for each common neighbor `w` of `u,v`, the two original edges `uw,vw` become parallel. Hence every parallel class has size exactly `1` or `2`.

Let `H` be the simple graph obtained by replacing each parallel class by one edge `x`, and give `x` activity `m_x`, its class size (`1` or `2`). A forest of the labelled multigraph `G/g` uses at most one edge from each parallel class, so

`Z(G/g) = sum_{I forest of H} product_{x in I} m_x`.

Thus the conditional forest law is exactly the weighted forest law on the **smaller simple graph** `H`.

Marked-copy issue. Suppose the images of the specific original marked edges `e,f` lie in distinct classes `x,y`, of sizes `m_x,m_y`. Write weighted class counts on `H` as `W,W_x,W_y,W_xy`. Symmetry of the parallel copies gives exactly

`Z_e = W_x/m_x`,  `Z_f = W_y/m_y`,  `Z_ef = W_xy/(m_x m_y)`,

and therefore

`Delta_specific(e,f) = (W_x W_y - W W_xy)/(m_x m_y)`.

If `e,f` merge into the same parallel class, `Z_ef=0`, so their correlation inequality is trivial. Hence the sign of the contraction-side gap is always the sign of an ordinary weighted Rayleigh gap on `H`.

Now minimality says that the unit-edge conjecture holds for every pair in `H`, because `|V(H)|=|V(G)|-1`. By the fixed-graph Cocks theorem, `M(H)` is independence correlated for **all positive weights**. In particular it is Rayleigh at the activity vector `m_x in {1,2}`. Therefore

**`D1(g) >= 0` for every third edge `g`.**

This directly pays the first missing weighted implication in the account01/B03 deletion-contraction route. It does not assume a new weighted conjecture; the all-weight statement is supplied by Cocks on a graph already known unit-good by minimality.

### Exact regression for the marked-copy scaling

A small independent check uses `G=K4`, conditions on `g=01`, and marks the specific copies `e=02`, `f=03`. Contraction creates two size-two parallel classes. The exact labelled conditional counts are

`(Z,Ze,Zf,Zef)=(14,4,4,1)`, gap `2`.

The simplified weighted triangle with activities `(2,2,1)` has class counts

`(W,Wx,Wy,Wxy)=(14,8,8,4)`, gap `8`,

so the specific-copy gap is exactly `8/(2*2)=2`.

Checker: `contraction_scaling_check.py`, Git blob `15c2cf2fb017931ab3a00faa15acd9f7798844ad`, SHA-256 `222b223ace3808417bf1c26b480ca596d48ab736f1d9295b3620ba9591504755`, 1772 bytes.  
Captured output: Git blob `fb4d8d6a743364a44bdc0a31fc79544a192e95a8`, SHA-256 `a4be81924a30036415020bf2a09fa1945d195c843500b2abace0e130a07f84e9`, 164 bytes, ending `PASS`.

The check is regression evidence only; the argument above is exact for every simple graph.

## 4. Quantitative consequence: the account01/B03 debt term disappears

Put `G0=G-{e,f}` and choose a uniform forest `H0` of `G0`. Define

- `X=1{H0+e is a forest}`,
- `Y=1{H0+f is a forest}`,
- `S=1{H0+e+f is a forest}`,
- `x=E X`, `y=E Y`, `r=E S`,
- `D=xy-r`.

The target is `D>=0`. In the minimal counterexample write `D=-delta` with `delta>0`.

For a third edge `g`, let `T=1{g in H0}`, `p=P(T=1)`, and let `D0,D1` be the same normalized gap conditional on `T=0,1`. Direct mixture algebra gives

`D=(1-p)D0+pD1-p(1-p)(x1-x0)(y1-y0)`

and therefore

`Cov(X,T) Cov(Y,T) / Var(T) = (1-p)D0+pD1-D`.

Deletion gives `D0>=0` by minimality. Section 3 now gives `D1>=0` with no unpaid weighted assumption. Hence for every third edge

`Cov(X,T) Cov(Y,T) / Var(T) >= delta`.

Also, in the smaller graph `G-f`,

`Delta_{G-f}(e,g) = -N^2 Cov(X,T) >= 0`,

where `N` is the number of forests of `G0`; similarly `Delta_{G-e}(f,g)=-N^2 Cov(Y,T)>=0`. Since `0<p<1` and the product is strictly positive, both covariances are in fact strictly negative. Thus the previous conditional sign-forcing becomes unconditional in a minimal counterexample:

**for every third edge `g`, both marked-edge addability variables are strictly negatively correlated with `1{g in H0}`, and their covariance product is at least `delta Var(T)`.**

This recovers the sign-coherent phenomenon reported earlier by the named-partner line, but with the contraction-side weight debt now paid by a source-checked theorem.

## 5. Proper two-separators are impossible in a minimal counterexample

Now use account02/B03's exact transfer, retaining the actual boundary-connectivity distribution.

Let `G=A union B`, edge-disjoint, with `V(A) intersect V(B)={s,t}`, and take a **proper** 2-separation (each side carries a genuine part of the graph).

### 5a. Marks on opposite sides

For `e in A`, `f in B`, let `d_i^A,c_i^A` count `A`-forests with marked state `i` and `s,t` disconnected/connected, and similarly for `B`. The inherited exact factorization is

`Delta_G(e,f)=(d_0^A c_1^A-d_1^A c_0^A)(d_0^B c_1^B-d_1^B c_0^B)`.

Each factor is a Rayleigh gap between the marked edge and a completed boundary edge `st` on a strictly smaller simple side. If that `st` edge is already present on the side, removing it shows the same factor is the ordinary unit gap with that actual edge; if the marked edge itself is `st`, the factor is manifestly nonnegative because a forest containing `st` is connected across the boundary. Minimality therefore makes both factors nonnegative. A violating pair cannot straddle the separator.

### 5b. Marks on the same side

Take `e,f in A`. Let `D_B,C_B` be the exact numbers of `B`-forests with `s,t` disconnected/connected. Since the empty forest exists, `D_B>0`; set the **actual induced response**

`lambda=C_B/D_B >= 0`.

The exact transfer says the global gap is `D_B^2` times the Rayleigh gap on side `A` with one virtual boundary edge `st` of activity `lambda`.

- If `lambda=0`, this is just the unit gap on the smaller side `A`, hence nonnegative by minimality.
- If `st` is absent from `A`, complete `A` by one simple edge `h=st`. The completed graph is strictly smaller than `G`, hence unit-good by minimality; fixed-graph Cocks upgrades it to all positive activities. Set the activity of `h` to the **actual** value `lambda` and all other activities to one. The transferred gap is nonnegative.
- If an unmarked `st` edge is already in `A`, the virtual edge merges with it and gives that edge total activity `1+lambda`. The simple graph `A` is smaller and unit-good; Cocks again permits exactly this positive weight.
- If the actual boundary edge `st` is one of the marked edges, removing `st` from a forest containing it is a bijection to a boundary-disconnected forest without it. Consequently the `lambda` terms cancel in the two-by-two determinant, and the global gap is `D_B^2` times the ordinary unit gap on `A`.

Therefore a minimal simple counterexample has **no proper 2-separation**.

Disconnected graphs and 1-sums factor over components/blocks, so a minimal counterexample is connected and has no cut vertex as well. Apart from the tiny graphs with fewer than four vertices (directly good), the minimal counterexample must therefore be **3-connected**.

This is the requested separator/deletion-contraction reduction with the real boundary distribution and real induced weight retained throughout. No sectorwise connected/disconnected Rayleigh assertion is inserted.

## 6. What is and is not closed

Closed in this run:

1. the contraction-side weighted gap `D1>=0` for every third edge of a minimal unit-simple counterexample;
2. the resulting strict quantitative all-third-edge sign forcing;
3. every proper two-separator case, including arbitrary actual response `lambda=C_B/D_B`, via fixed-graph Cocks on a smaller simple graph;
4. the earlier source-scope ambiguity about whether Cocks is fixed-graph: the Semple--Welsh final note explicitly records that form, and account04/B03 independently source-checked it.

Still open for this **alternative** mechanism: rule out the remaining 3-connected minimal counterexample using the quantitative sign forcing / overlap reservoir. The lead has a separate complete-graph/Hermite candidate with two independent positive reviews; this report neither re-reviews nor automatically promotes that candidate.

Honest status: **ESSENTIAL_STEP_APPLIED**.  
`CANDIDATE_REFUTED`: no.  
`AUXILIARY_ONLY`: no; a previously conditional induction step and all proper 2-separators are discharged.  
`FULL_PROOF_CANDIDATE`: no for this run.

## 7. Source/provenance notes

Primary external theorem used: Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), final note on p. 13 reporting Cocks's result that graph-specific unit Conjecture 1.1 implies independence correlation of `M(G)`. Cocks: *Correlated Matroids*, CPC 17 (2008), 511--518.

No held-out benchmark material, credentials, scheduler identifiers, unrelated private data, or machine paths are present in this report or checker. Repository retrieval was used only for source/control/history; no authenticated native brain retrieval or receiver-context activation occurred.
