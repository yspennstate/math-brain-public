# F0106 — overlap-sensitive domination, sunflower localization, and the exact dual LP

Date: 2026-09-18
Slot: `R7-04`
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, canonical Conjecture 7.9 (alternate author-hosted numbering Conjecture 7.8), with dual canonical Conjecture 7.12 / alternate Conjecture 7.11.

This artifact continues the admitted source problem. It does **not** claim a source-level solution or publication novelty. Its purpose is to isolate, with complete proofs, a substantially narrower remaining geometry after the previous disjoint-witness theorem.

## 1. Setup

Let `S` be finite. For `I subseteq S`, write

`H_I = {J subseteq S : I subseteq J}`.

A probability law `nu` on `2^S` is `r`-spread if

`nu(H_I) <= r^{|I|}`

for every `I subseteq S`.

Given `J subseteq S`, let `theta_{J,alpha}` be the law obtained by retaining each element of `J` independently with probability `alpha`. If `J~nu` and then `K~theta_{J,alpha}`, the law of `K` is `W_alpha(nu)`.

Talagrand's conjecture asks whether there is a universal `0<alpha<1` such that, for every `0<p<1`, every finite `S`, and every `alpha p`-spread `nu`,

`W_alpha(nu) <=_st mu_p`,

where `mu_p` is the Bernoulli product law and stochastic domination is tested on all up-classes.

Fix a proper nonempty up-class `A`. Let its distinct minimal witnesses be

`B_1,...,B_m`,

so

`A = union_j H_{B_j}`

and every `B_j` is nonempty. Put

`k_j=|B_j|`,
`S_p = sum_j p^{k_j}`.

Define

`g(alpha) = -alpha log(1-alpha)`.

The previous run defined `alpha_*` as the unique root of

`g(alpha_*)=1`,

numerically

`alpha_* = 0.740753643351695...`.

The frozen source metric remains

`alpha_dom := sup({a in (0,1): Talagrand's exact domination statement holds with alpha=a for all finite S,p,nu} union {0}).`

The previous run proved the source-valid upper obstruction

`alpha_dom <= alpha_*`.

The methods here are `B11 / B30 / B21`, different from the preceding `B2 / B18 / B25` triple.

---

## 2. B11 — exact covering LP and its spread-law dual

Talagrand's dual formulation can be made into an exact finite LP whose objective is precisely the worst stochastic-domination ratio.

Let

`r=alpha p`,
`m_A=mu_p(A)>0`,
`theta_J=theta_{J,alpha}(A)`.

Define

`h(I,J)=r^{-|I|} 1_{I subseteq J}`

for all `I`, with the convention `h(emptyset,J)=1`.

Consider the covering LP

`C_{r,A} = min sum_I w_I`

subject to

`w_I >= 0`

and, for every `J subseteq S`,

`sum_{I subseteq J} r^{-|I|} w_I >= theta_J/m_A`.

### Proposition 2.1 — exact dual norm identity

For every proper nonempty up-class `A`,

`C_{r,A} = (1/m_A) sup_{nu r-spread} W_alpha(nu)(A)`.

Consequently, Talagrand's domination statement at a fixed `alpha` is equivalent to

`C_{alpha p,A} <= 1`

for every finite `S`, every `0<p<1`, and every proper nonempty up-class `A`.

### Proof

The LP is finite. Its dual has one nonnegative variable `lambda_J` for each `J subseteq S`. The coefficient of `w_I` in the `J`-constraint is `r^{-|I|}1_{I subseteq J}`, hence the dual is

`maximize (1/m_A) sum_J theta_J lambda_J`

subject to

`lambda_J >= 0`

and, for every `I subseteq S`,

`r^{-|I|} sum_{J supseteq I} lambda_J <= 1`.

Equivalently,

`sum_{J supseteq I} lambda_J <= r^{|I|}`.

The `I=emptyset` constraint says

`sum_J lambda_J <= 1`.

Thus `lambda` is a subprobability measure satisfying all the `r`-spread inequalities. Pad its missing mass at the empty set. This does not change any nonempty principal-upset mass, and because `A` is proper and increasing, `emptyset notin A`, so

`theta_{emptyset,alpha}(A)=0`.

Therefore padding does not change the objective. The feasible dual objects are consequently equivalent, for the objective, to `r`-spread probability laws `nu`.

Finally,

`sum_J theta_J nu(J)=W_alpha(nu)(A)`.

Finite-dimensional LP duality gives the displayed identity. `QED`

### Corollary 2.2 — what a counterexample must maximize

At fixed `(alpha,p,A)`, a failure of domination is exactly the assertion

`C_{alpha p,A}>1`.

Thus it is enough to derive upper bounds on the dual norm `C` from structural information about the witness hypergraph of `A`.

This turns the overlap estimates below into direct restrictions on any genuine source counterexample.

---

## 3. B21 — Harris/FKG plus Janson gives a positive overlap regime

The previous run handled pairwise disjoint minimal witnesses. The next question is whether a controlled amount of overlap is still harmless.

Define the **ordered Janson overlap sum**

`Delta_p = sum_{i != j, B_i cap B_j != emptyset} p^{|B_i union B_j|}`.

The sum is ordered; this convention matches the `Delta/2` form of Janson's inequality below.

### Theorem 3.1 — overlap-sparse witness domination

For every `0<alpha<1`, every `0<p<1`, every `alpha p`-spread law `nu`, and every proper nonempty up-class `A` with minimal witnesses `B_1,...,B_m`,

`W_alpha(nu)(A^c) >= exp(-g(alpha) S_p)`.

Moreover, if

`Delta_p/2 <= (1-g(alpha)) S_p`,

then

`W_alpha(nu)(A) <= mu_p(A)`.

In particular, for every `alpha<alpha_*`, Talagrand domination holds for every up-class whose minimal-witness overlap obeys the displayed strict positive-overlap budget.

### Proof of the universal lower bound on the no-witness probability

Sample `J~nu`, then retain the elements of `J` independently with probability `alpha` to obtain `K`.

Conditional on `J`, for every witness with `B_j subseteq J`, the event

`E_j^c = {B_j not subseteq K}`

is a decreasing event in the independent Bernoulli retention variables on `J`. Harris/FKG for product measure therefore gives

`P(K notin A | J)
 = P(cap_{j:B_j subseteq J} E_j^c | J)
 >= product_{j:B_j subseteq J} P(E_j^c | J)
 = product_{j:B_j subseteq J} (1-alpha^{k_j}).`

Put

`lambda_j = -log(1-alpha^{k_j})`.

Then

`P(K notin A | J) >= exp(-sum_j lambda_j 1_{B_j subseteq J}).`

Average over `J`. Since `x -> exp(-x)` is convex, Jensen gives

`W_alpha(nu)(A^c)
 >= exp(-sum_j lambda_j nu(H_{B_j})).`

Spreadness implies

`nu(H_{B_j}) <= (alpha p)^{k_j}`,

hence

`W_alpha(nu)(A^c)
 >= exp(-sum_j [-log(1-alpha^{k_j})] alpha^{k_j} p^{k_j})
 = exp(-sum_j g(alpha^{k_j}) p^{k_j}).`

The function

`g(x)=-x log(1-x)`

is strictly increasing on `(0,1)`, because

`g'(x)=-log(1-x)+x/(1-x)>0`.

Since every `k_j>=1`, `alpha^{k_j}<=alpha`, and therefore

`W_alpha(nu)(A^c) >= exp(-g(alpha) S_p).`

This proves the first assertion.

### Comparison with product measure

Under `mu_p`, let `X_j=1_{B_j subseteq R}`. Then

`E X_j=p^{k_j}`

and the standard Janson inequality, with the ordered-pair convention above, gives

`mu_p(A^c)=P(X_1=...=X_m=0)
 <= exp(-S_p+Delta_p/2).`

If

`Delta_p/2 <= (1-g(alpha)) S_p`,

then

`-g(alpha)S_p >= -S_p+Delta_p/2`.

Consequently

`W_alpha(nu)(A^c)
 >= exp(-g(alpha)S_p)
 >= exp(-S_p+Delta_p/2)
 >= mu_p(A^c).`

Taking complements gives

`W_alpha(nu)(A) <= mu_p(A)`.

`QED`

### Corollary 3.2 — a necessary dense-overlap condition for any counterexample

Fix `alpha<alpha_*`. Since `g(alpha)<1`, any source counterexample at this `alpha` must have a minimal-witness hypergraph satisfying

`Delta_p > 2(1-g(alpha)) S_p`

at its offending value of `p`.

Thus a counterexample below `alpha_*` cannot merely contain overlaps: its weighted overlap density must exceed an explicit positive threshold.

### Corollary 3.3 — dual norm bound

Whenever `S_p>Delta_p/2`, Theorem 3.1 and Janson yield

`C_{alpha p,A}
 <= [1-exp(-g(alpha)S_p)]/[1-exp(-S_p+Delta_p/2)].`

In particular the right side is at most `1` under the hypothesis of Theorem 3.1.

This is the exact B11/B21 bridge: witness-overlap data bounds the LP norm whose crossing of `1` is equivalent to source failure.

---

## 4. B30 — exact localization to sunflower overlap, with a stronger constant

The simplest connected overlap component beyond disjoint witnesses is a sunflower. Surprisingly, nontrivial common-core sunflowers are easier than the core-free case.

Suppose the minimal witnesses have the form

`B_j = C union P_j`,

where the petals `P_1,...,P_m` are pairwise disjoint and nonempty, and each is disjoint from the common core `C`.

Write

`c=|C|`,
`k_j=|P_j|`,
`q=alpha^2 p`,
`T=sum_j p^{k_j}`.

The case `c=0` is the pairwise-disjoint theorem proved in the preceding run. Here assume `c>=1`.

### Theorem 4.1 — nontrivial-core sunflower domination

Let `alpha_*` be the unique root of `-x log(1-x)=1`. If

`alpha <= sqrt(alpha_*) = 0.8606704615308318...`,

then for every `p`, every `alpha p`-spread law `nu`, and every up-class whose minimal witnesses form a sunflower with nonempty common core,

`W_alpha(nu)(A) <= mu_p(A)`.

Hence, combining with the previous core-free theorem, **every sunflower minimal-witness family is safe for every `alpha<=alpha_*`**.

### Proof

First, occurrence of `A` after thinning requires every element of `C` to survive. Therefore

`W_alpha(nu)(A)
 <= P(C subseteq K)
 = alpha^c nu(H_C)
 <= alpha^c (alpha p)^c
 = q^c.`

Second, by the union bound over the full witnesses,

`W_alpha(nu)(A)
 <= sum_j P(B_j subseteq K)
 = sum_j alpha^{c+k_j} nu(H_{B_j})
 <= sum_j alpha^{c+k_j}(alpha p)^{c+k_j}
 = q^c sum_j q^{k_j}.`

Combining the two bounds,

`W_alpha(nu)(A)
 <= q^c min(1, sum_j q^{k_j}).`

Because every `k_j>=1`,

`sum_j q^{k_j}
 = sum_j alpha^{2k_j}p^{k_j}
 <= alpha^2 T.`

Thus

`W_alpha(nu)(A)
 <= alpha^{2c}p^c min(1,alpha^2 T).`

Under the product law, the common core is independent of all petals and the petals are mutually independent. Hence the exact product-law probability is

`mu_p(A)
 = p^c [1-product_j(1-p^{k_j})].`

Using `product_j(1-x_j)<=exp(-sum_j x_j)`,

`mu_p(A) >= p^c(1-exp(-T)).`

It remains to prove

`alpha^{2c} min(1,alpha^2 T) <= 1-exp(-T)`

for all `T>=0`. Since `c>=1`, set `x=alpha^2` and bound `alpha^{2c}<=x`. It is enough to show

`x min(1,xT) <= 1-exp(-T)`

for every `T>=0`.

For `0<T<=1/x`, the left side is `x^2T`. The function

`phi(T)=(1-exp(-T))/T`

is decreasing on `(0,infinity)`, so the worst point in this interval is `T=1/x`. The required inequality is then

`x^2 <= x(1-exp(-1/x))`,

i.e.

`x <= 1-exp(-1/x)`.

For `T>=1/x`, the left side is `x` and the right side is increasing, so again the worst point is `T=1/x` and the same scalar condition results.

Finally,

`x <= 1-exp(-1/x)`

is equivalent to

`-x log(1-x) <= 1`.

Because `g(x)=-x log(1-x)` is increasing and `g(alpha_*)=1`, this holds exactly when

`x<=alpha_*`.

Thus the sunflower domination follows whenever

`alpha^2<=alpha_*`,

i.e. `alpha<=sqrt(alpha_*)`.

`QED`

### Structural meaning

At the source-relevant range `alpha<=alpha_*`, every sunflower is already safe. Therefore any counterexample in this range must exhibit genuinely non-sunflower overlap: at least two intersecting witnesses whose intersections cannot all be explained by a single common core with disjoint residual petals.

Together with Corollary 3.2, any counterexample at `alpha<alpha_*` must simultaneously be

1. **weighted-overlap dense:** `Delta_p > 2(1-g(alpha))S_p`; and
2. **non-sunflower:** its minimal witnesses are not a single sunflower component of the above form.

This is a substantially narrower gluing regime than at the beginning of the run.

---

## 5. What did not close

None of the three methods proves a universal positive `alpha` for all witness hypergraphs, and none produces a counterexample below the existing `alpha_*` upper obstruction.

The exact unresolved geometry is now a dense-overlap, non-sunflower minimal-witness hypergraph. The current bounds do not control configurations in which many witnesses share several incompatible overlap cores. In that regime Janson's `Delta_p` can be of the same order as, or larger than, `S_p`, while the elementary sunflower factorization is unavailable.

The frozen metric therefore does **not** move in this run:

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`

before and after.

No restricted theorem is being promoted to source closure.

---

## 6. Next mathematical attack

Use a nonrepeating triple:

- **B14 — exploit symmetry:** symmetrize a putative extremal dual law / witness hypergraph under its automorphism group and determine whether a minimal counterexample can be reduced to a small orbit structure.
- **B24 — find the extremal object:** for fixed `(S_p,Delta_p)` or fixed witness sizes, optimize the exact dual norm `C_{alpha p,A}` over overlap patterns; test whether complete intersections, projective-plane-like designs, or another highly regular geometry is extremal.
- **B5 — add a parameter and differentiate:** introduce thinning parameter `t` and study the derivative of `C_{tp,A}` or of the no-witness functional as `t` moves from the controlled disjoint/sunflower regime toward the target `alpha`.

The specific goal is to replace the coarse pair-overlap statistic `Delta_p` by a higher-order cluster quantity that remains controlled in dense but structured overlap systems.
