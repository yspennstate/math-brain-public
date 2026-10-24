# F0106 — oriented-star conflict theorem and the full forest edge-witness class

Date: 2026-09-18  
Slot: `R7-04`  
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, source Conjecture 7.8 in the author copy / canonical repository Conjecture 7.9.

This is a restricted theorem inside the admitted source problem. It does **not** prove the full Talagrand conjecture and does **not** move the frozen full-source metric `alpha_dom`. The purpose is to solve a genuinely larger branching class than the preceding maximum-degree-two theorem and to expose the exact finite-state quantity needed for further gluing.

## 1. Setup

Let `S` be a finite set. For `I subseteq S`, write

`H_I={J subseteq S: I subseteq J}`.

A probability measure `nu` on `2^S` is `r`-spread when

`nu(H_I) <= r^{|I|}`

for every `I subseteq S`. Given `J~nu`, retain every element of `J` independently with probability `alpha`; the resulting law is `W_alpha(nu)`.

Let `G=(V,E)` be a finite simple graph, with `V subseteq S`, and define the edge-witness up-class

`A_G={K subseteq S: there exists {u,v} in E with u,v in K}`.

Fix an orientation `D` of `E`. For every vertex `v` with positive outdegree, let

`N^+(v)={u: v->u in D}`,
`d_v=|N^+(v)|`,
`C_v={v} union N^+(v)`,

and define the oriented-star event

`H_v={K: v in K and K cap N^+(v) != emptyset}`.

Because every edge is oriented exactly once,

`A_G = union_{v:d_v>0} H_v`.                                           (1)

For `0<p<1`, define the product-law hazard

`h_v(p)=mu_p(H_v)=p[1-(1-p)^{d_v}]`,

and

`Lambda_D(p)=sum_{v:d_v>0} h_v(p)`.

Let `Gamma_D` be the conflict graph on the active vertices `{v:d_v>0}`, joining distinct `v,w` iff

`C_v cap C_w != emptyset`.

For a nonempty graph `G`, `Lambda_D(p)>0`. Define the weighted independent-set fraction

`rho_D(p)= max_{I independent in Gamma_D} (sum_{v in I} h_v(p))/Lambda_D(p)`.       (2)

Finally write

`g(alpha)=-alpha log(1-alpha)`.

## 2. Main theorem

### Theorem 2.1 — oriented-star conflict domination

Fix `0<alpha,p<1`, a finite simple graph `G`, and an orientation `D` of `G`. If

`g(alpha) <= rho_D(p)`,                                               (3)

then for every `alpha p`-spread probability law `nu` on `2^S`,

`W_alpha(nu)(A_G) <= mu_p(A_G)`.                                      (4)

In particular, if `Gamma_D` is `chi`-colorable, then

`g(alpha) <= 1/chi`                                                    (5)

is sufficient for (4), uniformly in `p`.

### Proof

The proof has two sides. The thinned side is controlled by an oriented-star hazard that remains valid under arbitrary dependence in `nu`; the product side is controlled by one maximum-weight collection of pairwise support-disjoint stars.

#### Step 1. Conditional star hazards under thinning

Sample `J~nu`, and condition on `J`. Let `K` be the independent `alpha`-thinning of `J`.

For an active vertex `v`, put

`D_v(J)=|N^+(v) cap J|`.

The conditional probability of the event `H_v` is exactly

`x_v(J)=P(H_v | J)
      = alpha 1_{v in J}[1-(1-alpha)^{D_v(J)}].`                       (6)

Each complement `H_v^c` is a decreasing event of the independent retention bits on `J`. Therefore Harris/FKG gives

`P(K notin A_G | J)
 = P(cap_v H_v^c | J)
 >= product_v [1-x_v(J)].`                                             (7)

Here (1) is used for the equality on the left.

Set

`phi(x)=-log(1-x)`, `0<=x<1`.

Since `0<=x_v(J)<=alpha`, convexity of `phi`, together with `phi(0)=0`, implies that `phi(x)/x` is increasing and hence

`phi(x_v(J)) <= [-log(1-alpha)/alpha] x_v(J).`                         (8)

Thus (7) becomes

`P(K notin A_G | J)
 >= exp(-sum_v phi(x_v(J))).`                                          (9)

#### Step 2. A source-valid expectation bound for one oriented star

Put

`r=alpha p`,
`q_v=nu(v in J)`.

Spreadness gives `q_v<=r`. If `q_v=0`, then `E x_v=0`. Assume `q_v>0`.

For every `u in N^+(v)`, two-point spreadness gives

`P(u,v in J)<=r^2`.

Therefore

`E[D_v(J) | v in J]
 <= d_v r^2/q_v.`                                                      (10)

The function

`f(t)=1-(1-alpha)^t`, `t>=0`,

is increasing and concave. Jensen and (10) give

`E x_v
 = alpha q_v E[f(D_v(J)) | v in J]
 <= alpha q_v f(d_v r^2/q_v).`                                        (11)

For fixed `C>0`, the function

`psi(q)=q[1-(1-alpha)^{C/q}]`

is increasing on `q>0`. Indeed, with `a=-log(1-alpha)>0` and `z=aC/q`,

`psi'(q)=1-e^{-z}(1+z)>0`,

because `e^z>1+z` for `z>0`. Since `q_v<=r`, (11) yields

`E x_v
 <= alpha r [1-(1-alpha)^{d_v r}]
 = alpha^2 p [1-(1-alpha)^{d_v alpha p}].`                             (12)

Assumption (3) automatically implies `g(alpha)<=1`, because `rho_D(p)<=1`. Hence

`alpha p[-log(1-alpha)] = p g(alpha) <= p <= -log(1-p)`,

so

`(1-alpha)^{alpha p} >= 1-p`.                                         (13)

Raising (13) to the power `d_v` and substituting into (12) gives the clean hazard bound

`E x_v <= alpha^2 p[1-(1-p)^{d_v}]
          = alpha^2 h_v(p).`                                           (14)

#### Step 3. The thinned no-edge lower bound

Average (9) over `J`. Because `y -> e^{-y}` is convex,

`W_alpha(nu)(A_G^c)
 >= exp(-sum_v E phi(x_v(J))).`                                        (15)

By (8) and (14),

`sum_v E phi(x_v(J))
 <= [-log(1-alpha)/alpha] alpha^2 sum_v h_v(p)
 = g(alpha) Lambda_D(p).`                                              (16)

Therefore

`W_alpha(nu)(A_G^c)
 >= exp[-g(alpha)Lambda_D(p)].`                                        (17)

This is the crucial source-valid bound: it uses only the exact spread inequalities, not independence of `J`.

#### Step 4. The product-law conflict bound

Let `I` be a maximum-weight independent set in `Gamma_D` for the weights `h_v(p)`. The support sets `C_v`, `v in I`, are pairwise disjoint. Hence the events `H_v`, `v in I`, are independent under the product measure `mu_p`.

Since `A_G` contains their union,

`mu_p(A_G^c)
 <= product_{v in I}[1-h_v(p)]
 <= exp[-sum_{v in I}h_v(p)]
 = exp[-rho_D(p)Lambda_D(p)].`                                        (18)

Under (3), (17) and (18) imply

`W_alpha(nu)(A_G^c)
 >= exp[-g(alpha)Lambda_D(p)]
 >= exp[-rho_D(p)Lambda_D(p)]
 >= mu_p(A_G^c)`.

Taking complements proves (4).

For the coloring corollary, if `Gamma_D` has a proper coloring with `chi` colors, the total hazard `Lambda_D(p)` is partitioned among `chi` independent color classes. One color class has weight at least `Lambda_D(p)/chi`, hence `rho_D(p)>=1/chi`. This proves (5). `QED`

---

## 3. B12 — the conserved finite-state message

The preceding run showed that scalar edge count cannot survive high-degree branching. The theorem above identifies the first state-sensitive replacement:

`(h_v(p), C_v)` for each oriented star, together with the weighted conflict ratio `rho_D(p)`.

The thinned side pays the **sum** of local hazards,

`g(alpha) Lambda_D(p)`,

whereas the product side earns the maximum support-disjoint hazard mass,

`rho_D(p)Lambda_D(p)`.

Thus the exact finite-state comparison is not the number of edges. It is the ratio

`rho_D(p)=maximum disjoint star hazard / total star hazard`.

This quantity is stable under arbitrary branching degree and records precisely the articulation interference discarded by the old scalar proof.

---

## 4. B15 — break symmetry: asymmetric double-stars become easier

Consider the tree formed from adjacent hubs `u,v`, with `a` additional leaves at `u` and `b` additional leaves at `v`. Orient the central edge `u->v`, all `u`-leaves away from `u`, and all `v`-leaves away from `v`.

There are two active star messages:

`h_u=p[1-(1-p)^{a+1}]`,
`h_v=p[1-(1-p)^b]`.

Their support sets intersect at `v`, so the conflict graph is a single edge. Hence

`rho_D(p)=max(h_u,h_v)/(h_u+h_v).`                                    (19)

Theorem 2.1 gives domination whenever

`g(alpha) <= max(h_u,h_v)/(h_u+h_v).`                                 (20)

The right side lies in `[1/2,1)`. It equals `1/2` only in the balanced-hazard case and tends to `1` when one hub dominates the other. Thus deliberate asymmetry **helps** this method; balanced two-hub branching is the extremal local obstruction.

For reference, the exact product no-edge probability of this double-star is

`mu_p(A_G^c)
 = (1-p)^2 + p(1-p)^{a+1} + p(1-p)^{b+1}.`                            (21)

Equation (21) is consistent with the conflict-message interpretation: the obstruction is not high degree itself, but competition between comparably weighted overlapping articulation messages.

---

## 5. B25 — double count by stars and by conflict colors

The same edge-witness event is now counted in two genuinely different ways:

1. **Source/thinning count.** Every oriented edge is assigned to exactly one tail star. Spreadness plus conditional Harris/FKG converts the total star hazard to the exponent `g(alpha)Lambda_D(p)`.
2. **Product/disjoint-support count.** The conflict graph groups stars whose support sets overlap. An independent set in this graph is a family of product-independent star events. The best such family has hazard `rho_D(p)Lambda_D(p)`.

The inequality `g(alpha)<=rho_D(p)` is exactly the point where these two counts cross. The chromatic corollary is simply the averaging statement `rho_D(p)>=1/chi(Gamma_D)`.

This gives a compositional block rule rather than another finite graph enumeration.

---

## 6. Complete forest corollary

### Corollary 6.1 — every finite forest edge-witness family

Let `G` be any finite forest. If

`-alpha log(1-alpha) <= 1/2`,                                         (22)

then for every `0<p<1` and every `alpha p`-spread `nu`,

`W_alpha(nu)(A_G) <= mu_p(A_G)`.

Equivalently, the entire forest edge-witness class is safe for

`alpha <= alpha_F`,

where `alpha_F` is the unique solution of

`-alpha_F log(1-alpha_F)=1/2`,

numerically

`alpha_F = 0.5785953651248433...`.

### Proof

Root each tree component and orient every edge away from its root. For an active vertex `v`, `C_v` consists of `v` and its children.

Color each active vertex by the parity of its depth. If two active vertices have the same depth parity, their star support sets are disjoint: vertices at equal depth lie in disjoint rooted branches or are distinct siblings/branches, while vertices whose depths differ by at least two have neither a parent-child relation nor a shared child. Hence `Gamma_D` is bipartite and

`chi(Gamma_D)<=2`.

Theorem 2.1 therefore applies whenever `g(alpha)<=1/2`. `QED`

This strictly extends the preceding maximum-degree-two theorem in graph structure: arbitrary finite branching and unbounded degree are now permitted. It does not supersede every previous constant — the theorem is designed to discover a compositional branching mechanism, not to optimize every restricted class separately.

---

## 7. What this does and does not settle

Newly proved here:

- a general orientation/conflict theorem for **every finite graph edge-witness class** at a graph- and `p`-dependent threshold `g(alpha)<=rho_D(p)`;
- a clean chromatic sufficient condition `g(alpha)<=1/chi(Gamma_D)`;
- every finite forest, with arbitrary branching degree, is safe for the explicit universal range `alpha<=0.5785953651248433...`;
- asymmetric double-stars are easier than balanced ones for this route, identifying balance rather than degree as the local worst case;
- the finite-state gluing object is a weighted support-conflict message, not scalar edge count.

Still missing:

- the full source quantifies over **all up-classes**, equivalently all minimal-witness hypergraphs, not merely graph edge witnesses;
- even within graph edge witnesses, `rho_D(p)` can be small for dense cyclic support-conflict geometry and this proof alone gives no universal source-level lower bound for `alpha_dom`;
- higher-order witnesses require messages containing more than one center-plus-neighborhood bit;
- there is no source-level proof/refutation, no closure package, and no independent P26/OTHER audits.

Accordingly this artifact is **PARTIAL** and does not change the frozen full-source metric.

## 8. Prior-art status

The source is Talagrand's 2010 STOC paper. A bounded 2026-09-18 check also inspected Chen Li, *On p-Spread Measures*, arXiv:2609.08967v1 (posted 2026-09-08), whose abstract reports the fractional discrete-convexity solution and two comparison theorems for p-spread measures, and the Park-Pham 2024 selector-process result. No bounded-search hit was identified as the exact unrestricted one-product stochastic domination of F0106. This is **negative evidence only**. No novelty claim is made for the oriented-star/forest theorem without a dedicated literature review.
