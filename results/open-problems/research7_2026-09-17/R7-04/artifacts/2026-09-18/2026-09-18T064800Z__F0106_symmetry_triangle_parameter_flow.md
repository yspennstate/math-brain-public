Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# F0106 — symmetry reduction, exact triangle obstruction, and monotone parameter flow

Date: 2026-09-18
Slot: `R7-04`
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, canonical Conjecture 7.9 / author-preprint Conjecture 7.8, with canonical dual Conjecture 7.12 / author-preprint Conjecture 7.11.

This artifact continues the already admitted and exclusively claimed outside target. It does **not** claim a source-level solution or publication novelty. The immediately preceding method triple was `B11 / B30 / B21`; this artifact executes the required nonrepeating triple `B14 / B24 / B5`.

The frozen source metric remains

`alpha_dom := sup({a in (0,1): the exact source domination theorem holds with alpha=a for all finite S,p,nu} union {0}).`

Before this run the proved source-valid bracket was

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`,

where `alpha_*` is the unique root of

`-alpha_* log(1-alpha_*) = 1`.

The preceding run reduced any possible counterexample below `alpha_*` to a dense-overlap, non-sunflower minimal-witness hypergraph. The present run attacks the first genuinely non-sunflower overlap geometry exactly and studies how failures propagate in the thinning parameter.

---

## 1. Setup

For a finite set `S`, let `mu_p` be Bernoulli-`p` product measure on `2^S`. For `I subseteq S`, let

`H_I = {J subseteq S : I subseteq J}`.

A probability law `nu` on `2^S` is `r`-spread if

`nu(H_I) <= r^{|I|}`

for every `I subseteq S`.

Given `0<t<1`, let `W_t(nu)` be the law obtained by sampling `J~nu` and retaining each element of `J` independently with probability `t`.

The source statement at parameter `alpha` is

`nu is alpha p-spread  ==>  W_alpha(nu) <=_st mu_p`

for every finite `S`, every `0<p<1`, and every `nu`.

For a proper up-class `A`, the preceding run proved the exact finite dual norm identity

`C_{r,A} = (1/mu_p(A)) sup_{nu r-spread} W_alpha(nu)(A)`

when `r=alpha p`. Hence a single up-class violates the source statement precisely when its corresponding worst-case ratio exceeds one.

---

# 2. B14 — average over the automorphism group before optimizing

The unresolved regime contains witness hypergraphs with substantial symmetry. The first question is whether the maximizing spread law can be made to share that symmetry without loss.

### Lemma 2.1 — exact group symmetrization

Let `Gamma <= Sym(S)` be a finite permutation group, and suppose the up-class `A` is `Gamma`-invariant. For every `0<r,t<1`,

`sup_{nu r-spread} W_t(nu)(A)`

has a `Gamma`-invariant maximizer.

### Proof

Take any feasible `r`-spread probability law `nu`. For `g in Gamma`, let `g_#nu` be its pushforward under the coordinate permutation `g`, and define

`bar(nu) = |Gamma|^{-1} sum_{g in Gamma} g_#nu`.

For every `I subseteq S`,

`bar(nu)(H_I)
 = |Gamma|^{-1} sum_g nu(H_{g^{-1}I})
 <= |Gamma|^{-1} sum_g r^{|g^{-1}I|}
 = r^{|I|}`.

Thus `bar(nu)` is again `r`-spread. Independent thinning commutes with coordinate permutations, and `A` is invariant, so

`W_t(g_#nu)(A)=W_t(nu)(A)`

for every `g`. Averaging gives

`W_t(bar(nu))(A)=W_t(nu)(A)`.

Because the feasible set of laws on the finite space `2^S` is compact and the objective is linear, a maximizer exists; symmetrizing one yields an invariant maximizer. `QED`

### Corollary 2.2 — threshold up-classes reduce to a factorial-moment LP

For

`A_{n,k}={K subseteq [n]: |K|>=k}`,

the group `S_n` acts transitively on every level. An invariant law is determined by

`x_j = P(|J|=j)`, `0<=j<=n`.

Conditional on `|J|=j`, `J` is uniform among the `j`-sets. Hence for a fixed `s`-set `I`,

`P(I subseteq J | |J|=j) = binom(j,s)/binom(n,s)`.

Therefore the exact spread constraints are

`sum_{j=s}^n x_j binom(j,s)/binom(n,s) <= r^s`, `s=1,...,n`,

with `x_j>=0` and `sum_j x_j=1`. The thinning objective is

`sum_{j=0}^n x_j P(Bin(j,t)>=k)`.

Thus every fully symmetric threshold instance is an exact one-dimensional factorial-moment linear program. No exchangeability or independence assumption is being added: it follows from averaging an optimizer.

This is the B14 reduction used below.

---

# 3. B24 — solve the first dense non-sunflower witness geometry exactly

The smallest connected minimal-witness hypergraph that is not a sunflower is the triangle

`B_12={1,2}`, `B_13={1,3}`, `B_23={2,3}`.

Its up-class is simply

`A_triangle={K subseteq {1,2,3}: |K|>=2}`.

The previous overlap theorem does not automatically settle all parameters here, because every pair of witnesses overlaps and there is no common core shared by all three witnesses. We now solve its worst spread-law LP exactly throughout the entire source-relevant interval `alpha<=alpha_*`.

### Theorem 3.1 — exact triangle optimizer in the source-relevant range

Fix `0<alpha<=alpha_*`, `0<p<1`, and write

`r=alpha p`.

Then

`sup_{nu r-spread} W_alpha(nu)(A_triangle)`

is equal to

`3 alpha^2 r^2` if `0<r<=1/2`,

and to

`alpha^2 r (3r + 2alpha - 4alpha r)` if `1/2<=r<1`.

In particular, for every `alpha<=alpha_*`, every `p`, and every `alpha p`-spread `nu`,

`W_alpha(nu)(A_triangle) < mu_p(A_triangle)`.

Thus the first dense connected non-sunflower witness pattern is strictly safe throughout the complete interval not already excluded by the singleton obstruction.

### Proof — exact LP

By Lemma 2.1 we may average under `S_3`. Let

`x_j=P(|J|=j)`, `j=0,1,2,3`.

The exact `r`-spread constraints are

`(x_1+2x_2+3x_3)/3 <= r`,

`x_2/3+x_3 <= r^2`,

`x_3 <= r^3`,

`x_0+x_1+x_2+x_3=1`,

with all `x_j>=0`.

If `|J|=0` or `1`, an `alpha`-thinning cannot land in `A_triangle`. If `|J|=2`, it lands there with probability `alpha^2`. If `|J|=3`, it lands there with probability

`3 alpha^2(1-alpha)+alpha^3 = alpha^2(3-2alpha)`.

Hence the objective is

`alpha^2 x_2 + alpha^2(3-2alpha)x_3`.

Since `x_1` has zero objective coefficient, moving any mass from `x_1` to `x_0` preserves the objective and weakens every spread constraint. Thus an optimizer exists with `x_1=0`.

For fixed `x_3`, the objective is increasing in `x_2`, so we take the largest feasible `x_2`:

`x_2 <= min{1-x_3, (3/2)(r-x_3), 3(r^2-x_3)}`.      (3.1)

The three pairwise intersection abscissae are

`A=2r^2-r`  (pair constraint = singleton constraint),

`B=(3r^2-1)/2`  (pair constraint = mass constraint),

`C=3r-2`  (singleton constraint = mass constraint).

Direct subtraction gives

`A-B=(r-1)^2/2 >= 0`,

`A-C=2(r-1)^2 >= 0`,

and

`r^3-A = r(r-1)^2 >=0`.                               (3.2)

#### Case 1: `r<=1/2`

At `x_3=0`, the pair constraint `x_2<=3r^2` is the smallest bound in (3.1). Since its slope in `x_3` is `-3`, while the other two slopes are `-3/2` and `-1`, it remains the active bound throughout the feasible interval. Substituting

`x_2=3(r^2-x_3)`

into the objective, the coefficient of `x_3` becomes

`alpha^2[(3-2alpha)-3] = -2alpha^3 <0`.

Therefore the optimum is at `x_3=0`, with

`x_2=3r^2`, `x_0=1-3r^2`,

and objective

`3alpha^2r^2`.

#### Case 2: `r>=1/2`

The pair and singleton bounds meet at

`x_3=A=2r^2-r>=0`.

Before the pair bound becomes active, the active bound is either the mass line and then the singleton line (when `r>=2/3`) or just the singleton line (when `1/2<=r<=2/3`). Along the mass line the objective slope is

`alpha^2[(3-2alpha)-1] = 2alpha^2(1-alpha)>0`.

Along the singleton line it is

`alpha^2[(3-2alpha)-3/2]
 = alpha^2(3/2-2alpha)`.

Since `alpha<=alpha_*<3/4`, this slope is nonnegative. After `x_3=A`, the pair line is active and the slope is the strictly negative value `-2alpha^3` computed above. Hence the maximum is attained exactly at `x_3=A`.

Using (3.2), this point respects `x_3<=r^3`. Its coordinates are

`x_3=2r^2-r`,

`x_2=3(r^2-x_3)=3r(1-r)`,

`x_0=1-x_2-x_3=(1-r)^2`.

The objective is

`alpha^2[3r(1-r)+(3-2alpha)(2r^2-r)]`

`= alpha^2 r(3r+2alpha-4alpha r)`.

This proves the exact optimizer formula.

### Proof — comparison with the product law

Under `mu_p`,

`mu_p(A_triangle)=3p^2(1-p)+p^3=p^2(3-2p)`.

If `r<=1/2`, the worst spread-law probability is

`3alpha^2r^2=3alpha^4p^2`.

Since `3-2p>=1` and

`3alpha^4 <= 3alpha_*^4 = 0.9032676147... <1`,

we get strict domination.

If `r>=1/2`, then necessarily `alpha>=1/2` and `p>=1/(2alpha)`. Dividing the exact optimum by the product-law probability gives

`R(alpha,p)
 = alpha^4 [2+p(3-4alpha)]/[p(3-2p)]`.                (3.3)

Because `alpha<=alpha_*<3/4`, the coefficient `3-4alpha` is positive, so

`2+p(3-4alpha) <= 5-4alpha`.

On the interval `p in [1/(2alpha),1]`, the concave function `p(3-2p)` is minimized at an endpoint. At `p=1` it equals `1`, while at `p=1/(2alpha)` it equals

`(3alpha-1)/(2alpha^2) >=1`,

because

`3alpha-1-2alpha^2 = -(2alpha-1)(alpha-1) >=0`

for `alpha in [1/2,1]`. Therefore the denominator in (3.3) is at least one. Finally, the function

`alpha^4(5-4alpha)`

is increasing on `(0,1)`, since its derivative is `20alpha^3(1-alpha)>0`. Hence

`R(alpha,p)
 <= alpha^4(5-4alpha)
 <= alpha_*^4(5-4alpha_*)
 = 0.6133143225... <1`.

So strict domination also holds in the second regime. `QED`

### Structural consequence

Below `alpha_*`, a source counterexample was already known to require dense weighted overlap and non-sunflower geometry. Theorem 3.1 excludes the **minimal** such geometry. Thus any counterexample in the source-relevant interval must have a more complicated overlap complex than a three-edge triangle: the obstruction cannot occur on three coordinates with all two-coordinate minimal witnesses.

This is a restricted theorem and does not move `alpha_dom`.

---

# 4. B5 — the valid-parameter set is downward closed

The source asks only for existence of some positive parameter. A useful global structural question is whether validity at one parameter implies validity at smaller parameters.

For `0<a<1`, let `P(a)` denote the exact universal source statement at parameter `a`.

### Theorem 4.1 — downward closure in the thinning parameter

If `P(beta)` holds for some `0<beta<1`, then `P(alpha)` holds for every `0<alpha<beta`.

Equivalently, the set of universally valid parameters is downward closed. In particular, if failure is established at some `alpha`, then failure must also occur at every larger parameter `beta>alpha` (possibly with a different witness instance).

### Proof

Assume `P(beta)`. Let `0<alpha<beta`, let `0<p<1`, and let `nu` be `alpha p`-spread. Define

`p' = alpha p / beta`.

Then `0<p'<1` and

`beta p' = alpha p`,

so `nu` is `beta p'`-spread. By `P(beta)`,

`W_beta(nu) <=_st mu_{p'}`.

Now thin both random sets independently with retention

`t=alpha/beta`.

Independent thinning preserves stochastic order, and thinning semigroups compose. Therefore

`W_alpha(nu)
 = W_t(W_beta(nu))
 <=_st W_t(mu_{p'})
 = mu_{tp'}`.

But

`tp' = (alpha/beta)(alpha p/beta)
     = alpha^2 p / beta^2
     <= p`.

Product measures are monotone in their coordinate density, hence

`mu_{tp'} <=_st mu_p`.

Combining gives

`W_alpha(nu) <=_st mu_p`.

This is exactly `P(alpha)`. `QED`

### Consequence for the frozen metric

The definition of `alpha_dom` is not merely a supremum over a scattered set: the valid set is an initial interval of `(0,1)`, up to whether the endpoint itself is valid. The singleton obstruction above `alpha_*` therefore identifies a genuine one-sided forbidden region rather than isolated bad parameters.

This theorem alone gives no positive lower bound on `alpha_dom`.

---

# 5. B5 continued — exact derivative of the instance gap

The preceding theorem changes both the spread scale and target product density. There is also an exact monotone flow for one fixed spread law.

Fix a finite up-class `A`, a number `0<r<1`, and an `r`-spread law `nu`. For `t in (r,1)`, set

`p(t)=r/t`

and define the instance domination gap

`D(t)=mu_{p(t)}(A)-W_t(nu)(A)`.

The same `nu` is exactly eligible for the source comparison along the entire curve because

`t p(t)=r`.

### Proposition 5.1 — Russo derivative and single-crossing property

For every `t in (r,1)`,

`D'(t)
 = -(r/t^2) sum_{i in S} Inf_i^{p(t)}(A)
   - E_{J~nu} sum_{i in J} Inf_i^{J,t}(A)
 <=0`.                                                (5.1)

Here `Inf_i^q(A)` is the usual pivotal probability for coordinate `i` under Bernoulli-`q` product measure on `S`, and `Inf_i^{J,t}(A)` is the pivotal probability for `i` under product-`t` measure on the coordinates of `J` with all coordinates outside `J` frozen to zero.

Consequently `D(t)` is nonincreasing. If one fixed `(r,nu,A)` instance fails at a parameter `t_0`, then the same instance, with target density changed to `r/t`, continues to fail for every `t>t_0`.

### Proof

For an increasing event on a finite product space, Russo's formula gives

`d/dq mu_q(A)=sum_i Inf_i^q(A)`.

Since `p(t)=r/t`,

`p'(t)=-r/t^2`,

and therefore

`d/dt mu_{p(t)}(A)
 = -(r/t^2) sum_i Inf_i^{p(t)}(A)`.

Conditional on `J`, the law defining `W_t(nu)` is an ordinary product-`t` law on the coordinates of `J`, with all others fixed absent. Russo's formula on that finite subcube gives

`d/dt theta_{J,t}(A)
 = sum_{i in J} Inf_i^{J,t}(A)`.

Averaging over the finite law `nu` yields

`d/dt W_t(nu)(A)
 = E_{J~nu} sum_{i in J} Inf_i^{J,t}(A)`.

Subtracting proves (5.1), and every term on its right is nonpositive. `QED`

### What the derivative does not yet provide

Equation (5.1) is exact, but it does not by itself lower-bound the initial gap uniformly over all finite `S`, all up-classes, and all spread laws. The missing source-closing ingredient can now be stated as a quantitative barrier problem: find a positive universal time interval on which no eligible gap trajectory can cross zero, using spreadness to control the second pivotal sum relative to the first or to the initial margin.

This is more precise than simply asking for a new correlation inequality, but no such uniform barrier is proved here.

---

# 6. Combined result and honest metric

The three new methods give:

1. `B14`: every automorphism-invariant up-class has a symmetry-invariant worst spread law; fully symmetric threshold classes reduce exactly to factorial-moment LPs.
2. `B24`: the triangle witness hypergraph, the smallest dense connected non-sunflower obstruction left by the previous run, is strictly safe for every `alpha<=alpha_*`, with an exact worst-law formula.
3. `B5`: universal validity is downward closed in `alpha`, and every fixed-spread instance gap follows an exact nonincreasing Russo flow.

These are theorem-sized partial results. They do **not** prove any universal positive `alpha`, and they do not construct a counterexample below `alpha_*`.

Frozen metric before:

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`.

Frozen metric after:

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`.

**NO MOVEMENT.**

Status remains **PARTIAL / SOURCE OPEN / CLOSABLE OUTSIDE**.

---

# 7. Exact failures / remaining obstruction

The symmetry lemma helps only when the offending up-class itself has a useful automorphism group. A generic dense non-sunflower hypergraph may have trivial symmetry.

The triangle computation rules out the first obstruction but does not imply that every denser intersection complex decomposes into safe triangles or sunflowers. In particular, incompatible four-witness clusters can contain higher-order inclusion data invisible to pairwise overlap statistics.

The parameter-flow theorem proves a single-crossing structure but no dimension-free barrier against the first crossing. The exact missing inequality is a spread-sensitive comparison between

`E_{J~nu} sum_{i in J} Inf_i^{J,t}(A)`

and either

`(r/t^2) sum_i Inf_i^{r/t}(A)`

or the current positive gap `D(t)`.

No such inequality is established in this artifact.

---

# 8. Next nonrepeating attack

Use the next distinct triple **B15 / B18 / B27**:

- **B15 — break symmetry on purpose:** perturb the triangle into the smallest asymmetric non-sunflower clutter, such as a triangle plus one additional witness or unequal orbit weights, and determine exactly which moment-LP facet first becomes dangerous.
- **B18 — say it in another language:** encode the minimal-witness family as an intersection complex / reliability polynomial and express the Russo gap derivative through cluster coefficients rather than raw pair overlaps.
- **B27 — swap the quantifiers:** attack Talagrand's dual formulation directly by seeking, for one explicit small `alpha`, a single witness-sampling law `eta_A` that controls all `J` simultaneously, rather than optimizing separately over spread laws.

The concrete goal is a universal positive lower bound on `alpha_dom`; restricted safe geometries will no longer count as metric movement.
