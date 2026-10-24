# FOREST / account04 B01 — rational-weighted 3-connected core with all-edge Simpson constraints

**Run:** `account04-b01-20260922T071144Z-forest-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-Q3C-ALL-EDGE-SIMPSON-v1`  
**Parent target:** OPEN  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact target and inputs consumed

The target remains the uniform law on **all** acyclic edge subsets of every finite simple graph, with unit edge weights, including the empty forest and disconnected forests. For distinct edges `e,f`, with

`Z(y)=sum_(F forest) prod_(h in F) y_h`,

write

`Delta_G(e,f;y) = Z_e Z_f - Z Z_ef`.

At unit weights the target is `Delta_G(e,f;1)>=0`.

The latest complete team-lead report consumed was account01/B01 run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, report blob `cd6fde1f2bd0c68f7372629e7d4fbee9f8df5f92`. It correctly keeps the fixed-graph Cocks globalization withdrawn and isolates a Simpson/conditioning mechanism.

The assigned partner account01/B02 report consumed was run `20260922T044633Z-b02-64cb61a7`, blob `85c4df9879eeb33fa02a9abf6ec9967ddf19823f`. I use its explicit warning that contraction-created parallel classes must be aggregated by their **summed activity**, never silently simplified to unit edges.

The named OTHER-account result applied is account01/B20 run `20260922T061735Z-B20-forest-r11`, candidate `FOREST-MULTIGRAPH-MINIMAL-SIMPSON-v1`, report blob `22e2028fde7b86505935c9fe137676c5374cf7e7`. Its decisive source-valid idea is to choose a minimal counterexample in a contraction-closed labelled multigraph category, which makes deletion/contraction conditioning exact for every third edge and removes the lead's STAR-2 restriction.

I also inherit account04/B01 `FOREST-Q-3CONN-EXACT-v1`: exact two-cut bridge algebra plus exact rational two-terminal realization reduce the class-level separator problem to positive-rational weighted simple 3-connected cores. The present run supplies the missing connection between that rational 3-connected core and the all-edge Simpson geometry.

## 2. Source correction: use the proved ground-set homogenization, not an unproved rank homogenization

The lead and B20 state a stronger CLC row budget using a polynomial homogenized to graphic rank `R`. I rechecked the primary source before importing it.

Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, Theorem 4.1, proves complete log concavity for the standard homogenization

`g_M(t,z)=sum_(I independent) t^(m-|I|) prod_(h in I) z_h`,

where `m` is the ground-set size. The primary source is arXiv:1811.01600, not the `1811.01816` identifier appearing in the lead report. I did not find in the checked source a theorem allowing `m` to be replaced by rank `R` in this polynomial. Therefore I do **not** use the stronger rank-denominator budget.

This correction does not damage the argument below: the source-proved ground-set homogenization already gives the needed all-parameter row inequality, and the forest bound `E|F|<=R` recovers the cyclomatic term later.

Positive rational edge activities are handled by the positive diagonal substitution `z_h -> y_h z_h`, which preserves complete log concavity.

## 3. Minimal rational-weighted loopless counterexample is simple

Assume the source conjecture fails. A unit simple counterexample is then also a counterexample in the larger class of finite loopless multigraphs with positive rational edge activities. Choose a counterexample lexicographically minimal in

`(number of nonisolated vertices, number of labelled edges)`

and fix a positively correlated pair `e,f`.

For a parallel class `C`, put `Y_C=sum_(h in C)y_h`. A forest uses at most one member of a parallel class, so collapsing all classes gives an underlying simple graph whose forest polynomial is exactly the original polynomial after the substitutions `Y_C=sum y_h`.

If `e,f` lie in the same class, they cannot occur together and their covariance is negative. Thus a violating pair lies in distinct classes `E,F`. For a specified labelled copy,

`partial_(y_e) Z = partial_(Y_E) Z`,
`partial_(y_f) Z = partial_(Y_F) Z`,
`partial_(y_e)partial_(y_f)Z = partial_(Y_E)partial_(Y_F)Z`.

Consequently the Rayleigh gap is exactly preserved by parallel collapse, and the actual covariance changes only by the positive factor `(y_e/Y_E)(y_f/Y_F)` relative to the aggregate class indicators. Any nontrivial parallel class would therefore produce a counterexample with the same vertex count and fewer labelled edges. Minimality forbids this.

**Conclusion 3.1:** the chosen minimal rational-weighted loopless counterexample is a **simple** graph.

This is precisely where the partner's parallel-class warning is applied: the class activity is the sum of its member activities; no multiplicity is discarded.

## 4. Every third edge satisfies the exact Simpson inequality

Let the minimal simple weighted graph be `G`, let `e,f` be a violating pair, and write

`C_ij=Cov(X_i,X_j)`, `V_i=p_i(1-p_i)`, `rho_ij=C_ij/sqrt(V_i V_j)`,
`a=rho_ef>0`.

Fix any third edge `g`.

Conditioning on `X_g=0` is the positive-rational weighted forest law of `G\g`, a smaller member of the allowed class. Conditioning on `X_g=1` and deleting the compulsory edge is the weighted forest law of `G/g`. Contraction may create loops and parallel classes. Delete loops and aggregate each parallel class by summing its rational activities; this preserves the conditional law on the surviving class indicators and yields a smaller positive-rational weighted loopless instance. If a marked edge becomes a loop, its conditional covariance is zero. Hence lexicographic minimality gives

`Cov(X_e,X_f | X_g=0)<=0`,
`Cov(X_e,X_f | X_g=1)<=0`.

The exact binary law of total covariance is

`C_ef = E[ Cov(X_e,X_f | X_g) ] + C_eg C_fg / V_g`.

Therefore, for **every** third edge,

`C_eg C_fg / V_g >= C_ef`,

or equivalently

**(S)** `rho_eg rho_fg >= a > 0`.

Applying (S) cyclically to any three positively correlated pairs gives `x<=yz`, `y<=xz`, `z<=xy`. Since distinct edge indicators are not almost surely identical (the empty forest and singleton forests all have positive weight), `0<xyz<1`, contradicting `xyz<=(xyz)^2`.

Thus positive covariance pairs form a matching. In particular, for the fixed violating pair `e,f`, every third edge satisfies

**(N)** `C_eg<0` and `C_fg<0`.

This transfers account01/B20's all-edge Simpson geometry from unit labelled multigraphs to the positive-rational weighted class needed by the separator reduction.

## 5. Exact two-cut gluing forces the minimal weighted counterexample to be 3-connected

Disconnected graphs and one-vertex sums factor their forest partition functions, so a minimal counterexample is 2-connected.

Suppose `G` has a genuine two-vertex cut `{u,v}`. Separate a physical `uv` edge, if present, as its own singleton bridge. Let the remaining `uv`-bridges be `B_i`. Write

`D_i = forest sum in B_i with u,v disconnected`,
`C_i = forest sum in B_i with u,v connected`.

Then, exactly,

`Z_G = prod_i D_i + sum_i C_i prod_(j!=i) D_j`.

All `D_i,C_i` are positive rational numbers at positive rational activities.

### Same bridge

If `e,f in B_i`, put

`A_i=prod_(j!=i)D_j`,
`lambda_i=sum_(j!=i) C_j/D_j`.

Then `lambda_i` is positive rational and

**(G1)** `Delta_G(e,f)=A_i^2 Delta_(B_i+g_i)(e,f)` at `y_(g_i)=lambda_i`,

where `g_i` is a virtual `uv` edge. Because the original physical `uv` edge was separated as a singleton bridge, the augmented non-singleton bridge is simple. A genuine 2-cut in a 2-connected graph has at least two non-singleton component bridges, so `B_i+g_i` has fewer vertices than `G`. Minimality makes its gap nonnegative, contradicting a same-bridge violation.

### Different bridges

If `e in B_i`, `f in B_j`, `i!=j`, then

**(G2)** `Delta_G(e,f)=A_ij^2 R_i(e) R_j(f)`,

where

`R_i(e)=D_i C_(i,e)-C_i D_(i,e)`.

For a non-singleton bridge,

`R_i(e)=Delta_(B_i+g_i)(e,g_i)`

(the gap is independent of the two marked variables), so minimality makes `R_i(e)>=0`. For a singleton original `uv` edge, `R_i=1`. Thus cross-bridge gaps are also nonnegative.

Therefore a minimal weighted counterexample has no 2-cut. The only low-order 2-connected exception is a triangle. For a weighted triangle with edge activities `x,y,z`,

`Z=1+x+y+z+xy+xz+yz`

and for the pair `x,y`,

`Delta_xy=(1+y+z)(1+x+z)-Z=z(1+z)>0`,

with the other pairs symmetric. Hence no triangle is a counterexample.

**Conclusion 5.1:** any source failure yields a positive-rational weighted **3-vertex-connected simple** counterexample that can be chosen lexicographically minimal as above and obeys (S) and (N) for every third edge.

This is the requested all-parameter gluing/three-connected connection, with the original separator-edge and contraction-created-parallel cases both explicit.

## 6. Source-secure all-parameter CLC budget on that 3-connected core

Let `m=|E|`, `R=|V|-1` (the graph is connected), `K=|F|`, `mu=E K`, and `c_h=Cov(X_h,K)`.

Use the source-proved degree-`m` homogenization

`g(t,z)=sum_(F forest) (prod_(h in F)y_h) t^(m-|F|) prod_(h in F) z_h`.

At `(t,z)=(1,1)`, the monomial law is exactly the desired weighted forest law. Log concavity gives

`diag(EU)-Cov(U) >= 0`

for the exponent vector `U=(m-K,X_1,...,X_m)`. Normalizing by `diag(EU)` and using `0<=N<=I`, hence `N^2<=N`, gives for every edge `e`

**(C1)**

`T_e + sum_(h!=e)(1-p_h) rho_eh^2 <= p_e`,

where

`T_e = c_e^2 / ((m-mu)p_e(1-p_e)) >=0`.

Here `m-mu>0` because the empty forest has positive weight.

Add (C1) for the violating pair and put `s=p_e+p_f`:

`T_e+T_f +(2-s)a^2`
` + sum_(g!=e,f)(1-p_g)(rho_eg^2+rho_fg^2) <= s`.

By (S), `rho_eg^2+rho_fg^2 >= 2a`. Therefore

**(C2)**

`T_e+T_f +(2-s)a^2 + 2a sum_(g!=e,f)(1-p_g) <= s`.

Now

`sum_(g!=e,f)(1-p_g)=m-2-mu+s`.

Every forest has at most `R` edges, so `mu<=R`. With cyclomatic number

`beta=m-R=m-|V|+1`,

we obtain the source-secure 3-connected obstruction

**(C3)**

`boxed: T_e+T_f +(2-s)a^2 + 2a(beta-2+s) <= s.`

This is the all-parameter replacement for the earlier unit-only simplification. It does **not** assume `p_h<=1/2`, which is false for general positive activities.

For a simple 3-connected graph on at least four vertices, minimum degree is at least three, so `beta>=3`. Also every finite positive activity gives `p_e,p_f<1`, hence `0<s<2`. Dropping the nonnegative `T` and quadratic terms gives

`a <= s/[2(beta-2+s)] < 1/beta`.

Thus every minimal rational-weighted 3-connected witness forced by a source failure would satisfy the strict quantitative localization

**(C4)** `0<a<1/beta`.

A sharper form retained from (C3) is

`a <= [sqrt(d^2+(2-s)(s-T_e-T_f))-d]/(2-s)`,

where `d=beta-2+s`, whenever the right side is defined; (C3) itself is the canonical statement.

## 7. Compact conditional end-to-end chain

The current source-safe chain is now:

1. source failure gives a counterexample in the positive-rational weighted loopless class;
2. lexicographic minimality plus exact parallel aggregation makes that counterexample simple;
3. deletion/contraction conditioning stays inside the rational weighted loopless class, so every third edge obeys all-edge Simpson (S), and positive pairs form a matching;
4. disconnected and cut-vertex factorization plus exact two-cut identities (G1)--(G2) force the minimal simple weighted counterexample to be 3-vertex-connected;
5. the **source-proved degree-`m`** CLC homogenization, not the unsupported rank replacement, yields (C3) and `a<1/beta`;
6. account04/B01's earlier exact rational unitization maps any rational-weighted simple violation back to a unit simple violation, so this core is compatible with the original source scope rather than an unrelated weighted conjecture.

## 8. First remaining essential implication

The parent conjecture is still open. The first unpaid universal step is now sharply confined:

> Rule out a positive-rational weighted 3-connected simple graph and pair `e,f` satisfying all of (S), (N), and (C3), or show that any failure of the existing labelled path-cut/Hall transport produces a forbidden positive covariance with a third edge.

The all-parameter separator cases, contraction-created parallel classes, and triangle-conditioning strata are no longer the obstruction in this chain.

## 9. Failure/correction record

- I do **not** use the withdrawn fixed-graph Cocks implication.
- I do **not** simplify parallel classes to unit edges; activities are summed exactly.
- I do **not** use the stronger rank-homogeneous CLC budget from the lead/B20 because the checked primary source proves the degree-`m` homogenization instead. The weaker source-secure form is enough for (C3).
- No finite census or numerical search is counted as proof evidence in this run.
- No claim of novelty or full FOREST closure is made.

**Outcome: `ESSENTIAL_STEP_APPLIED`.** The exact all-parameter gluing/three-connected step is connected to the current all-edge Simpson mechanism, and the remaining witness class is now rational-weighted, simple, 3-connected, externally negative to every third edge, and subject to (C3). The parent FOREST conjecture remains **OPEN**.
