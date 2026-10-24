# FOREST B03 conditioning/reconnection audit — run 20260922T014518Z-account01-B03-forest-auto11

Outcome: **CANDIDATE_REFUTED** for the current lead's claimed end-to-end closure step. The complete-graph Hermite subtheorem is **not** refuted here. Parent target remains **OPEN**. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Current lead and named other-account input

Latest complete lead handoff consumed: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. It claims a conditional chain

`unit p-NC on every K_n -> fixed-graph Cocks upgrade to all positive weights on M(K_n) -> Semple-Welsh minor closure -> every finite simple graph by deletion`.

Named OTHER-account partner result consumed and applied: account02/B01 run `B01-20260922T0004Z-forest-r11`, report blob `bf7b362f6cdb15453102b54e91be937cd89258f5`. Its `K_{2,2}` exact witness shows that conditioning on a boundary-connectivity sector can destroy Rayleigh even when the correctly mixed positive virtual-edge response remains positive. I therefore do **not** use sectorwise conditioning below; every conditional formula retains the full induced response.

## 2. Decisive source audit of the lead closure step

The lead's fixed-graph implication is not supplied by the cited Semple-Welsh/Cocks results I could verify.

Semple-Welsh define `independence correlated` to mean the Rayleigh inequality for **all positive edge weights**. Their Proposition 3.5 proves that this weighted class is minor-closed. Immediately afterward they explicitly distinguish this from the unit conjecture and state that they do not know whether the class of graphs satisfying unit Conjecture 1.1 is minor-closed; before Proposition 3.7 they likewise say they cannot show that a unit-good graph remains unit-good after a series or parallel extension.

Cocks's 2008 result is a **class-level equivalence**: the class of graphic matroids is independence-correlated iff the unit forest conjecture holds for all graphs. The converse direction rationally approximates a bad positive weighting, scales it to integer multiplicities, replaces edges by parallel copies to create a generally different graph `G'`, and then invokes the unit conjecture on that enlarged graph. Thus the verified implication is of the form

`unit p-NC for every graph (including the required parallel extensions) -> all graphic matroids positive-weight p-NC`,

not

`unit p-NC for this one graph G -> M(G) positive-weight p-NC`.

Therefore proving the unit inequality only for the family `K_n` does **not** presently justify the weighted `M(K_n)` conclusion needed before invoking Semple-Welsh minor closure. Equivalently, the missing bridge is at least:

> prove unit p-NC for every integer parallel extension of every `K_n`, or directly prove the positive-weight Rayleigh inequality for every `M(K_n)`.

Without such a bridge, deleting edges from `K_n` is exactly the unit-minor-closure step that Semple-Welsh say is not known from unit p-NC alone. This refutes the current **proof candidate as written**, not the Hermite calculation and not the forest conjecture.

Primary references checked: C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423–435, especially Propositions 3.5 and 3.7; C. C. Cocks, *Correlated Matroids*, CPC 17 (2008), 511–518, class-equivalence argument.

## 3. Exact overlap/reconnection reduction, with no connectedness assumption

Let `G0=G-{e,f}` and let `H` be uniform over **all** forests of `G0`, including disconnected forests. Define

- `X(H)=1` iff `H+e` is a forest;
- `Y(H)=1` iff `H+f` is a forest;
- `S(H)=1` iff `H+e+f` is a forest;
- `Q(H)=X(H)Y(H)-S(H)`.

Thus `Q=1` exactly when both marked edges are individually addable but together create the unique overlap cycle. Put

`x=E X`, `y=E Y`, `r=E S`, `q=E Q`, `N=#Forests(G0)`.

Then

`Cov(X,Y)=r+q-xy`,

and the exact marked-edge Rayleigh gap is

`F_e(G)F_f(G)-F_{ef}(G)F(G) = N^2(xy-r) = N^2(q-Cov(X,Y))`.

Hence the target is exactly

`r <= x y`,

or equivalently `Cov(X,Y) <= q`. This formulation automatically handles disconnected `H`, disjoint marked edges, and marked edges sharing a vertex. In the shared-vertex case `Q=1` precisely when the two nonshared endpoints lie in the same `H`-component while the shared endpoint lies in another component.

## 4. New exact third-edge conditioning identity

Fix any third edge `g in E(G0)` and let `T=1_{g in H}`, `p=P(T=1)`. For `t in {0,1}` define

`x_t=E[X|T=t]`, `y_t=E[Y|T=t]`, `r_t=E[S|T=t]`, `D_t=x_t y_t-r_t`,

and `D=xy-r`. Direct expansion gives the exact Simpson/reconnection identity

`D = (1-p)D_0 + p D_1 - p(1-p)(x_1-x_0)(y_1-y_0)`.

Equivalently,

`Cov(X,T) Cov(Y,T) / Var(T) = (1-p)D_0 + pD_1 - D`.

This is valid without any connectivity condition on `H` and with overlapping marked cycles.

For a lexicographically minimal **simple-graph** counterexample, the deletion side is source-safe: `D_0>=0`, since `T=0` is the uniform forest law on the proper deletion `G-g`. Also, using the exact extension identity

`Cov_{G-f}(1_e,1_g) = Cov_{G0}(X,T)/(1+x)^2`

(and symmetrically for `Y`) plus unit p-NC of the proper deletions gives

`Cov(X,T)<=0`, `Cov(Y,T)<=0`.

The extension identity uses only the two extensions `H` and `H+e` and does not invoke contraction or positive weights.

## 5. Where the contraction/weight gate enters — exact debt accounting

If one additionally knew `D_1>=0`, then a strict marked violation `delta=-D=r-xy>0` would force, for **every** third edge `g`,

`Cov(X,T)Cov(Y,T)/Var(T) >= delta > 0`.

Together with the deletion signs, both covariances would be strictly negative. This is the desired sign-forcing reconnection estimate.

However `T=1` is the contraction side. Contracting `g` may create parallel classes, so after simplification the law carries positive integer activities. The source audit in Section 2 shows that one may not silently infer this positive-weight inequality from unit p-NC of a single smaller simple graph. The exact fail-closed replacement is

`Cov(X,T)Cov(Y,T)/Var(T) = (1-p)D_0 + pD_1 + delta >= delta - p*max(0,-D_1)`.

Thus every failure of the quantitative sign-forcing estimate is paid for by an explicit **contraction-weight debt** `max(0,-D_1)`. This isolates the precise missing implication instead of hiding it inside a minor-closure assertion.

Boundary contractions close automatically:

- if contraction makes `e` or `f` a loop, then the corresponding conditional addability is zero and `D_1=0`;
- if contraction makes `e,f` parallel, then `S=0` conditionally and `D_1=x_1y_1>=0`;
- therefore only contractions where the marked pair remains distinct/nonparallel and unmarked parallel classes induce genuine positive weights require the missing weighted gate.

## 6. Conditional obtuse-packing estimate if the weighted contraction gate is later proved

Assume for this paragraph only that every `D_1>=0`. Let `k=|E(G0)|`, and standardize

`u=(X-x)/sqrt(Var X)`, `v=(Y-y)/sqrt(Var Y)`, `w_g=(T_g-p_g)/sqrt(Var T_g)`.

Proper deletion p-NC gives `<w_g,w_h><=0` for `g!=h`, and the extension identities above give `<u,w_g><=0`, `<v,w_g><=0`. Write `a_g=<u,w_g>`, `b_g=<v,w_g>` and `theta=delta/sqrt(Var X Var Y)`. The conditioning identity gives `a_g b_g>=theta`.

Elementary obtuse Bessel lemma: if unit vectors `w_i` have pairwise nonpositive inner products and `<z,w_i><=0`, then

`sum_i <z,w_i>^2 <= ||z||^2`.

Proof: set `c_i=-<z,w_i>/||w_i||^2>=0` and expand `||z+sum c_i w_i||^2`; all cross terms among distinct `w_i` are nonpositive.

Applying this to `u` and `v` gives

`sum a_g^2 <=1`, `sum b_g^2<=1`, hence `k theta<=1`.

Applying it to `u+v` gives the sharper overlap-aware form

`2k theta <= 1 + Corr(X,Y)`.

Since `Corr(X,Y)=(q+delta)/sqrt(Var X Var Y)`, this is

`(2k-1) delta <= sqrt(Var X Var Y) + q`.

This does not close the conjecture, but it is a quantitative reconnection estimate showing exactly what a valid positive-weight contraction theorem would buy.

Variance boundary: a strict violation forces `0<x,y<1`; if `x=0` or `y=0`, then `r=0`, while if `x=1`, then `r<=y`, so `D>=0`. Thus the normalization above is legitimate in the only case where it is needed. For every ordinary base edge of a simple graph, `0<p<1` because both the empty forest and the singleton `{g}` occur.

## 7. Exact finite audit

A fresh exact-rational checker exhaustively tested all simple graphs on at most five vertices and all choices of distinct marked `e,f` and third edge `g`: **46,563** triple instances.

Results:

- conditioning/reconnection identity failures: `0`;
- extension-identity failures: `0`;
- instances with `Cov(X,T_g)>0`: `0`;
- instances with `Cov(Y,T_g)>0`: `0`;
- instances with conditional `D_1<0`: `0`;
- marked pairs with `Cov(X,Y)>0`: `5,973`, confirming that the overlap correction `q` is genuinely necessary.

First positive-`Cov(X,Y)` witness found is `K_4-{23}` with `e=01`, `f=02`: `N=8`, `x=3/4`, `y=7/8`, `r=3/8`, `q=3/8`, `Cov(X,Y)=3/32`, and `D=9/32`; hence the marked Rayleigh gap is `N^2 D=18>0` even though raw addability covariance is positive.

Checker SHA-256: `3c29770048086ca86e8a19f0d5075c3b4f4844e6281d500cb84278c7a8624581`.
Output SHA-256: `1a470dc77feed11481d3e84e74f4ba28ec595b6cd9e770b5ad5e53b65716a205`.

Finite enumeration is regression evidence only.

## 8. Current end-to-end state and next exact obligation

Compact conditional chain now reads:

1. lead Hermite calculation proves unit p-NC on every `K_n` (pending its own independent formula audit);
2. **missing:** prove positive-weight p-NC for every `M(K_n)`, equivalently enough unit control over all required parallel extensions;
3. then Semple-Welsh Proposition 3.5 permits deletion/minor closure;
4. every finite simple `G` is an edge-deletion restriction of `K_{|V(G)|}`.

For the local reconnection route, the first essential missing implication is the same phenomenon in miniature: establish `D_1>=0` for contraction-induced positive weights, or replace contraction conditioning by a direct unit-simple switching that controls the explicit debt term above. Partner account02/B01's `K_{2,2}` witness rules out proving this by separate boundary sectors.

No full proof is claimed. No benchmark/install work was performed. No protected control was modified.
