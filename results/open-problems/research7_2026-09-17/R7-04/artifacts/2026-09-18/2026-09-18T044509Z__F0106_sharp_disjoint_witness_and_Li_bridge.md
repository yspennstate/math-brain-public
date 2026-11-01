Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# F0106: sharp obstruction, disjoint-witness theorem, and the Chen-Li bridge

Target: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Conjecture 7.9 in the current author-hosted `prizes/small.pdf` copy.

Frozen source metric:

`alpha_dom := sup({a in (0,1): Conjecture 7.9 holds with alpha=a for all finite S,p,nu} union {0}).`

This artifact records one ordinary research iteration with methods **B2 / B18 / B25**. The source conjecture is **not** closed.

---

## 1. Setup

For a finite set `S`, let `mu_p` be Bernoulli-`p` product measure on `2^S`. For `I⊆S`, write

`H_I={J⊆S:I⊆J}`.

A law `nu` on `2^S` is `r`-spread when

`nu(H_I) <= r^{|I|}`

for every `I⊆S`. Given `0<alpha<1`, write `T_alpha nu = W_alpha(nu)` for the law obtained by first sampling `J~nu` and then independently retaining every element of `J` with probability `alpha`.

Talagrand asks whether there is one universal `alpha>0` such that

`nu is alpha p-spread  ==>  T_alpha nu <=_st mu_p`

for every finite `S` and every `0<p<1`.

---

# B2 — attack the negation first

## 2. A sharp universal upper obstruction on the possible constant

Define `alpha_*` to be the unique number in `(0,1)` satisfying

`-alpha_* log(1-alpha_*) = 1`.

Equivalently,

`alpha_* = 1-exp(-1/alpha_*)`.

Numerically,

`alpha_* = 0.7407536433...`.

### Theorem 2.1

For every `alpha>alpha_*`, Talagrand's Conjecture 7.9 fails with that value of `alpha`. Consequently

`alpha_dom <= alpha_* = 0.7407536433...`.

### Proof

Fix `alpha>alpha_*`. For an integer `N` large enough that `p_N:=1/(alpha N)<1`, let

`S_N={1,...,N}`

and let `nu_N` be the uniform law on the `N` singleton sets.

For a singleton `{i}`,

`nu_N(H_{ {i} }) = 1/N = alpha p_N`.

For `|I|>=2`,

`nu_N(H_I)=0`.

Thus `nu_N` is exactly `alpha p_N`-spread.

Let `A_N={K⊆S_N:K != emptyset}`. An `alpha`-thinning of a singleton is nonempty with probability exactly `alpha`, hence

`W_alpha(nu_N)(A_N)=alpha`.

On the other hand,

`mu_{p_N}(A_N)=1-(1-p_N)^N
               =1-(1-1/(alpha N))^N
               -> 1-exp(-1/alpha)`.

Because `alpha>alpha_*`,

`-alpha log(1-alpha)>1`,

which is equivalent to

`alpha > 1-exp(-1/alpha)`.

Therefore for all sufficiently large `N`,

`W_alpha(nu_N)(A_N) > mu_{p_N}(A_N)`.

So `mu_{p_N}` does not dominate `W_alpha(nu_N)`. This proves the theorem. `□`

### Comments

This is a genuine source-level obstruction on the universal constant, not a refutation of the existential conjecture. It says any positive proof must use `alpha<=alpha_*`.

The same one-point family is discussed by Talagrand in testing later stronger conjectures, so no novelty claim is made for the example itself. The exact sharp threshold `alpha_*` becomes more useful below because it is also the sharp constant for an entire disjoint-witness class.

---

# B18 — translate the statement and use the newest comparison theorem

## 3. Noise squares the spread parameter

Let

`kappa := W_alpha(nu)`

when `nu` is `alpha p`-spread. Then for every `I⊆S`,

`kappa(H_I)
 = alpha^{|I|} nu(H_I)
 <= alpha^{|I|}(alpha p)^{|I|}
 = (alpha^2 p)^{|I|}`.

Hence

`kappa is q-spread with q=alpha^2 p`.                    (3.1)

This recovers the useful part of the old intake attempt, but the next step uses new September-2026 mathematics.

## 4. Chen Li's two-product coupling and the exact missing strengthening

Chen Li, *On p-Spread Measures*, arXiv:2609.08967v1 (2026-09-08), proves the following coupling theorem (Theorem 3.3): for every `q`-spread law `kappa`, there are jointly distributed

`X,R_1,R_2`

such that

`X~kappa`, `R_1~mu_q`, `R_2~mu_q`, and `X⊆R_1 union R_2` almost surely.

Apply this with `q=alpha^2 p` from (3.1). This is already extremely close to Talagrand's desired one-product domination.

If Li's pair could additionally be chosen **independent**, then

`R_1 union R_2 ~ mu_s`,

where

`s=1-(1-q)^2=2q-q^2 <= 2 alpha^2 p`.

Therefore, for every `alpha<=1/sqrt(2)`,

`s<=p`,

and we would have the chain

`W_alpha(nu)=kappa <=_st mu_s <=_st mu_p`.

Thus the following statement is a source-closing sufficient lemma.

### Lemma target 4.1 — independent two-cover for noisy spread laws

There exists `alpha_0>0` such that whenever `nu` is `alpha_0 p`-spread and

`kappa=W_{alpha_0}(nu)`,

one can couple `X~kappa` with **independent** `R_1,R_2~mu_{alpha_0^2 p}` so that

`X⊆R_1 union R_2` almost surely.

If Lemma 4.1 holds for any `alpha_0<=1/sqrt(2)`, then F0106 is proved with that `alpha_0`.

### Why the extra hypothesis `kappa=W_alpha(nu)` is essential

Li's theorem cannot in general be strengthened to independent `R_1,R_2` for an arbitrary `q`-spread `kappa`.

Take `kappa` uniform on the `N` singleton sets, with `q=1/N`. Then `kappa` is `q`-spread and is nonempty with probability one. But if `R_1,R_2` were independent `mu_q`,

`P(R_1 union R_2 != emptyset)
 = 1-(1-q)^{2N}
 -> 1-e^{-2}<1`.

Hence no coupling can satisfy `X⊆R_1 union R_2` almost surely.

The possible strengthening must therefore exploit the **alpha-divisibility/noise representation** of `kappa`, not spreadness alone. This localizes the new gluing problem sharply.

---

# B25 — double-count / exploit a disjoint witness decomposition

## 5. A complete sharp theorem for up-classes with pairwise disjoint minimal witnesses

Let an up-class `A` have minimal elements

`B_1,...,B_m`

that are pairwise disjoint. Their cardinalities may be different. Thus

`A = union_{j=1}^m H_{B_j}`

and `B_i ∩ B_j=emptyset` for `i!=j`.

The next theorem gives the exact same sharp constant `alpha_*` as the singleton obstruction.

### Theorem 5.1 — sharp disjoint-witness domination

If `0<alpha<=alpha_*`, `0<p<1`, and `nu` is `alpha p`-spread, then

`W_alpha(nu)(A) <= mu_p(A)`

for every up-class `A` whose minimal elements are pairwise disjoint.

Moreover the constant `alpha_*` is sharp for this class, already for the subclass where every minimal witness is a singleton.

### Proof

Sample `J~nu`, then let `K` be its independent `alpha`-thinning. Put

`k_j=|B_j|`,
`c_j=alpha^{k_j}`,
`x_j=p^{k_j}`,

and define

`Z_j(J)=1{B_j⊆J}`.

Conditional on `J`, the events

`{B_j⊆K}`

are independent over `j`, because the `B_j` are pairwise disjoint and thinning acts independently on coordinates. Also, if `B_j⊆J`, the entire block survives with probability exactly `c_j`; if `B_j` is not contained in `J`, it cannot survive. Therefore

`P(K notin A | J)
 = product_j (1-c_j)^{Z_j(J)}
 = exp(-Y(J))`,

where

`Y(J) := sum_j lambda_j Z_j(J)`,
`lambda_j := -log(1-c_j)>0`.

The function `y -> exp(-y)` is convex, so Jensen gives

`P(K notin A)
 = E exp(-Y)
 >= exp(-E Y)`.                                      (5.1)

Spreadness yields

`E Z_j = nu(H_{B_j})
       <= (alpha p)^{k_j}
       = c_j x_j`.

Hence

`E Y <= sum_j lambda_j c_j x_j`.                      (5.2)

Now the scalar function

`g(c):=-c log(1-c)`

is strictly increasing on `(0,1)`. By definition `g(alpha_*)=1`. Since

`c_j=alpha^{k_j}<=alpha<=alpha_*`,

we have

`lambda_j c_j = -c_j log(1-c_j) <= 1`.                (5.3)

Combining (5.1)--(5.3),

`P(K notin A) >= exp(-sum_j x_j)`.

For every `0<=x<1`, `1-x<=e^{-x}`, so

`product_j(1-x_j) <= exp(-sum_j x_j)`.

But under `mu_p`, because the blocks `B_j` are disjoint, the events `H_{B_j}` are independent and

`mu_p(A^c)=product_j(1-p^{k_j})=product_j(1-x_j)`.

Therefore

`W_alpha(nu)(A^c) >= mu_p(A^c)`,

or equivalently

`W_alpha(nu)(A) <= mu_p(A)`.

This proves domination for the entire disjoint-witness class.

For sharpness, take `B_j={j}` for `j=1,...,N` and use the singleton law in Theorem 2.1. Every `alpha>alpha_*` fails for all sufficiently large `N`. `□`

## 6. What Theorem 5.1 says about the real obstruction

Talagrand explicitly treated the special family

`A={X:X != emptyset}`

and obtained a sufficient small-alpha proof (his displayed calculation closes with `alpha<=1/2`). Theorem 5.1 pushes that special case to its exact sharp constant `alpha_*` and simultaneously handles arbitrary collections of **pairwise disjoint minimal witnesses of arbitrary sizes**.

Hence any counterexample for `alpha<=alpha_*`, or any obstruction to proving F0106 in that range, must use genuine **overlap geometry among minimal witnesses**. Mere abundance of disjoint witnesses is not enough.

This is the cleanest new structural localization from the present run.

---

## 7. Frozen metric movement

Before this run:

`alpha_dom = UNKNOWN/UNMEASURED`.

After B2:

`0 <= alpha_dom <= alpha_*`,

where

`alpha_*` is the unique root of `-alpha log(1-alpha)=1`,

`alpha_* = 0.7407536433...`.

This is **MOVEMENT** of the frozen source-matching quantity: every constant above `alpha_*` is now rigorously excluded.

No positive universal lower bound for `alpha_dom` is proved here, so F0106 remains **PARTIAL / SOURCE OPEN**.

Stagnation count for F0106 after this run: `0`.

---

## 8. Exact remaining gap and next attack

The disjoint case is completely controlled. The missing mathematics is overlap.

There are two equivalent-looking high-value routes:

1. **Independent-cover route.** Prove Lemma 4.1 for the special `alpha`-divisible laws `W_alpha(nu)`. Li has already proved the corresponding two-cover theorem without independence.
2. **Overlap/Jensen route.** Extend Theorem 5.1 from disjoint minimal witnesses to overlapping antichains by replacing the exact conditional product with a lower bound of Shearer/Janson type that retains enough of the spread inequalities.

The next nonrepeating Section-B triple should be **B11 / B30 / B21**:

- B11: dualize Lemma 4.1 as a transport/Farkas inequality and identify its extremal obstruction;
- B30: localize the first failure of the disjoint proof to one overlap component and identify the precise gluing loss;
- B21: import Shearer/Janson or hard-core partition-function inequalities to lower-bound the no-witness probability under conditional thinning.

---

## 9. Dated source/literature notes used in this iteration

Checked 2026-09-18:

- Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, current author-hosted `https://michel.talagrand.net/prizes/small.pdf`, Conjecture 7.9 and dual Conjecture 7.12.
- Chen Li, *On p-Spread Measures*, arXiv:2609.08967v1, posted 2026-09-08. Theorem 3.3 is the two-product coupling used in Section 4 above.
- Talagrand's current homepage still points to the prize problems as problems worth solving. Bounded exact-phrase searches found no later source-level proof/refutation of Conjecture 7.9. Search failure is not treated as a novelty or openness certificate.
