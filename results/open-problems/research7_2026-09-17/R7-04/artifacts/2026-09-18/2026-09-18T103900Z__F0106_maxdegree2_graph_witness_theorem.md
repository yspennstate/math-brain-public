Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# F0106 — maximum-degree-two witness graphs, cycle extremality, and the branching gluing obstruction

Date: 2026-09-18  
Slot: `R7-04`  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, canonical Conjecture 7.9 / author-copy Conjecture 7.8, with canonical dual Conjecture 7.12 / author-copy Conjecture 7.11.  
Methods: **B3 prove something stronger / B14 find the group acting / B30 localize and identify the gluing failure**.

This is a restricted theorem inside the admitted source problem. It does **not** claim source-level closure, a positive universal lower bound for `alpha_dom`, or publication novelty.

## 1. Setup and recovered source reduction

Let `S` be finite. For `I subseteq S`, write

`H_I={J subseteq S: I subseteq J}`.

A probability law `nu` on `2^S` is `r`-spread if

`nu(H_I) <= r^{|I|}`

for every `I subseteq S`. Given `0<alpha<1`, let `W_alpha(nu)` be the law obtained by sampling `J~nu` and retaining every element of `J` independently with probability `alpha`.

Talagrand's source asks whether there is a universal `alpha>0` such that, for every finite `S`, every `0<p<1`, and every `alpha p`-spread `nu`,

`W_alpha(nu) <=_st mu_p`,

where `mu_p` is Bernoulli product measure and stochastic domination is tested on every up-class.

The frozen source metric remains

`alpha_dom := sup({a in (0,1): the exact source statement holds at alpha=a for every finite S,p,nu} union {0}).`

Earlier R7-04 work proved

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`,

where `alpha_*` is the unique root of

`g(alpha_*)=1`,  `g(x):=-x log(1-x)`.

It also proved the triangle edge-witness case and, in the immediately preceding run, the six-cycle edge-witness case throughout the entire source-relevant interval. The present run replaces graph-by-graph checking by a theorem for **all** witness graphs of maximum degree at most two.

For a finite simple graph `G=(V,E)` define the edge-witness up-class

`A_G={K subseteq V: K contains both endpoints of at least one e in E}`.

Equivalently, `A_G^c` is the family of independent vertex sets of `G`.

---

# 2. B3 — a stronger theorem for every maximum-degree-two witness graph

## Theorem 2.1 — maximum-degree-two edge-witness domination

Let `G` be any finite simple graph with `Delta(G)<=2` and at least one edge. If

`g(alpha^2) <= 1/2`,

then for every `0<p<1` and every `alpha p`-spread probability law `nu` on `2^{V(G)}`,

`W_alpha(nu)(A_G) <= mu_p(A_G)`.

In particular, the conclusion holds for every `alpha<=alpha_*`. Thus every disjoint union of arbitrary finite paths and cycles is safe throughout the entire parameter interval still viable for the full Talagrand conjecture.

### Step 1 — an FKG/Jensen lower bound for the thinned independent-set event

Sample `J~nu` and then obtain `K` by `alpha`-thinning `J`. Conditional on `J`, let `E_J` be the set of graph edges whose two endpoints lie in `J`, and write `e_G(J)=|E_J|`.

For each `e in E_J`, the event that `e` is **not** fully retained in `K` is decreasing in the independent Bernoulli retention variables. By Harris/FKG for product measure,

`P(K in A_G^c | J) >= product_{e in E_J} P(e not subseteq K | J)`

`= (1-alpha^2)^{e_G(J)}`.

Set `L=-log(1-alpha^2)>0`. Averaging and using Jensen for the convex function `x -> exp(-Lx)`,

`W_alpha(nu)(A_G^c)`

`>= E exp(-L e_G(J))`

`>= exp(-L E e_G(J)).`

Spreadness gives, edge by edge,

`E e_G(J)=sum_{e in E} nu(H_e) <= |E| (alpha p)^2.`

Therefore, with `m=|E|`,

`W_alpha(nu)(A_G^c) >= exp(-m p^2 alpha^2[-log(1-alpha^2)])`

`= exp(-m p^2 g(alpha^2)).`                                      (2.1)

This uses only exact source hypotheses; no independence of `nu` is assumed.

### Step 2 — product-measure independent sets on a path

Put

`t=1-p^2/2.`

Let `P_m` denote the `mu_p`-probability that a path with `m` edges contains no occupied edge. Conditioning on its first vertex gives

`P_m=(1-p)P_{m-1}+p(1-p)P_{m-2}`                               (2.2)

for `m>=2`, with

`P_0=1`,  `P_1=1-p^2`.

The key exact identity is

`t^2-(1-p)t-p(1-p)`

`= (p^2/4)((1-p)^2+1) > 0.`                                    (2.3)

Also `P_0=1=t^0` and `P_1=1-p^2 <= 1-p^2/2=t`. If inductively `P_{m-1}<=t^{m-1}` and `P_{m-2}<=t^{m-2}`, then by (2.2) and (2.3),

`P_m <= t^{m-2}[(1-p)t+p(1-p)] <= t^m.`

Hence

`P_m <= t^m`                                                    (2.4)

for every path length `m`.

### Step 3 — every cycle reduces to the four-cycle

The two roots of

`x^2-(1-p)x-p(1-p)=0`

are denoted `lambda_+>0>lambda_-`. The weighted independent-set transfer matrix for a cycle gives exactly

`Z_m := mu_p(C_m contains no occupied edge) = lambda_+^m+lambda_-^m.`    (2.5)

Identity (2.3) says the characteristic polynomial is positive at `t`; since `t>0`, it follows that

`t >= lambda_+.`                                                (2.6)

If `m` is odd, the second term in (2.5) is negative, so immediately

`Z_m <= lambda_+^m <= t^m.`                                     (2.7)

Suppose `m` is even, `m>=4`. Define

`a=lambda_+/t <=1`,  `rho=|lambda_-|/lambda_+ in (0,1)`.

Then

`Z_m/t^m = a^m(1+rho^m).`

Both factors are nonincreasing as even `m` increases. Therefore

`Z_m/t^m <= a^4(1+rho^4)=Z_4/t^4.`                              (2.8)

Thus every even cycle reduces to `C_4`. Directly,

`Z_4=1-4p^2+4p^3-p^4`.

The required inequality has the following exact positive certificate:

`(t^4-Z_4)/p^2`

`= 2(1-p)^6`

`  + 8 p(1-p)^5`

`  + (25/2) p^2(1-p)^4`

`  + 10 p^3(1-p)^3`

`  + (9/2) p^4(1-p)^2`

`  + p^5(1-p)`

`  + (1/16)p^6 >=0.`                                           (2.9)

So `Z_4<=t^4`; by (2.8), every even cycle also satisfies `Z_m<=t^m`. Together with (2.7),

`Z_m <= t^m`                                                    (2.10)

for every finite cycle.

### Step 4 — glue path/cycle components

A graph with maximum degree at most two is a disjoint union of isolated vertices, paths, and cycles. Isolated vertices do not affect `A_G^c`, and product measure factorizes over connected components. Applying (2.4) and (2.10) component by component gives

`mu_p(A_G^c) <= t^m`.

Since `1-x<=e^{-x}`,

`mu_p(A_G^c) <= (1-p^2/2)^m <= exp(-m p^2/2).`                  (2.11)

If `g(alpha^2)<=1/2`, then (2.1) and (2.11) imply

`W_alpha(nu)(A_G^c)`

`>= exp(-m p^2 g(alpha^2))`

`>= exp(-m p^2/2)`

`>= mu_p(A_G^c)`.

Taking complements proves Theorem 2.1. `QED`

### Step 5 — why every source-relevant alpha satisfies the scalar condition

It remains to compare the endpoint `alpha_*` with `g(alpha^2)=1/2` without relying on decimal arithmetic.

First,

`g(3/4)=(3/4)log 4=(3/2)log 2 >1`,

because

`log2 = integral_1^2 dx/x > 2/3`

(the strict midpoint/Jensen inequality for the convex function `1/x`). Since `g` is strictly increasing and `g(alpha_*)=1`,

`alpha_*<3/4`, hence `alpha_*^2<9/16`.

Next,

`g(9/16)=(9/16)log(16/7)<1/2`

is equivalent to `log(16/7)<8/9`. For the latter, the exponential series gives the exact rational certificate

`exp(8/9) > 1+8/9+(8/9)^2/2+(8/9)^3/6`

`=5251/2187`

and

`5251/2187 - 16/7 = 1765/15309 >0.`

Therefore `exp(8/9)>16/7`, so indeed `g(9/16)<1/2`. By monotonicity of `g`, every `alpha<=alpha_*` satisfies `g(alpha^2)<1/2`.

This completes the source-relevant corollary.

### B3 outcome

The previous single `C6` theorem extends to an **infinite graph family**: every finite maximum-degree-two edge-witness hypergraph, with arbitrary numbers and lengths of components, is safe through the entire viable source interval. This is a complete restricted theorem, not movement of the universal source metric.

---

# 3. B14 — cycle symmetry identifies `C4` as the sole extremal finite core

The transfer-matrix proof above is also a symmetry reduction. Cyclic symmetry collapses the product-side independent-set calculation to the two eigenvalues `lambda_+,lambda_-`. Relative to the comparison scale `t`,

`Z_m/t^m = a^m(1+(-rho)^m)`.

This immediately explains the entire cycle hierarchy:

1. odd cycles are easier because the negative eigenmode subtracts;
2. among even cycles, both `a^m` and `1+rho^m` decrease with `m`;
3. consequently **the four-cycle is extremal among all cycles** for the normalized bound `Z_m<=t^m`.

Thus the only algebraic finite core required for all cycle lengths is the positive certificate (2.9). This is why the preceding `C6` obstruction could be repaired: degree-two overlap never creates a new product-side gluing obstruction beyond `C4`.

### B14 outcome

The group/transfer-matrix quotient does not merely shorten a checker. It proves a monotone extremality statement that removes every `C_m`, `m>=5`, from separate consideration.

---

# 4. B30 — the scalar gluing proof fails exactly at branching, but the first branch is still safe

The B3 proof deliberately discarded all overlap information on the thinned side except the total number `m` of edge witnesses. A natural question is whether the same scalar comparison can hold for arbitrary graphs. It cannot.

## Proposition 4.1 — high-degree stars destroy every edge-count-only product bound

For the star `K_{1,d}`, the product-measure no-edge probability is exactly

`Z_d(p)=(1-p)+p(1-p)^d.`                                       (4.1)

Indeed either the center is absent, or it is present and all `d` leaves are absent.

Fix any `p in (0,1)`. Then `Z_d(p)->1-p>0` as `d->infinity`, and hence

`c_d(p):=-log Z_d(p)/(d p^2) ->0.`                              (4.2)

Therefore there is **no** universal constant `c>0` for which

`mu_p(A_G^c) <= exp(-c |E(G)|p^2)`                              (4.3)

holds for all finite graphs.

The FKG/Jensen lower bound (2.1), after throwing away all geometry, depends only on `|E|p^2`. Hence an edge-count-only gluing proof of Talagrand domination must fail at branching witness graphs.

This is **not** a source counterexample: previous R7-04 work proved every sunflower, including every star, safe throughout the source-relevant interval. The failure of (4.3) identifies the datum that the scalar proof erased: at a branch, one must retain the common-core/articulation occupancy state rather than charge every incident witness independently.

## Proposition 4.2 — the first non-sunflower degree-three branch is still safe

Consider the paw graph: a triangle with one pendant edge attached to one triangle vertex. It is connected, has maximum degree three, and its four minimal edge witnesses are not a sunflower.

Its independent sets consist of the empty set, four singleton sets, and exactly two independent pairs. Therefore its product no-edge probability is

`q^4+4pq^3+2p^2q^2`,  `q=1-p`.

Expanding gives

`q^4+4pq^3+2p^2q^2 = 1-4p^2+4p^3-p^4 = Z_4.`                  (4.4)

Thus the paw has exactly the same product-side no-edge polynomial as `C4`. Its thinned-side FKG/Jensen bound also uses four size-two witnesses, so the proof of Theorem 2.1 applies verbatim. Hence the paw edge-witness up-class is safe whenever `g(alpha^2)<=1/2`, in particular for every `alpha<=alpha_*`.

### B30 outcome

The first genuine breakdown is not merely `Delta=3`; the smallest connected non-sunflower degree-three pattern is still controlled. What fails is **scalar composition under unbounded branching**. A successful extension must carry a finite state/message at articulation vertices (at minimum, whether the articulation is occupied) and glue those state-conditioned certificates. This is the precise next obstruction, not another longer-cycle enumeration.

---

# 5. Exact finite self-check

A standard-library exact-rational checker accompanies this artifact. It verifies:

1. the path comparison identity (2.3);
2. the degree-six positive-basis identity (2.9) for `C4`;
3. the exact paw=`C4` product polynomial identity (4.4);
4. the rational exponential certificate `5251/2187 - 16/7 = 1765/15309>0` used at the endpoint.

The archived executed output terminates `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not one of the independent closure audits required by the owner protocol.

---

# 6. What is and is not proved

Proved in this run:

- all finite edge-witness graphs of maximum degree at most two satisfy the Talagrand domination inequality whenever `g(alpha^2)<=1/2`;
- hence all such graphs are safe for every `alpha<=alpha_*`;
- `C4` is the unique extremal cycle core for the product-side scalar bound;
- edge-count-only exponential gluing provably cannot cover arbitrary branching graphs;
- the paw, the simplest connected non-sunflower degree-three edge graph, is nevertheless safe in the same regime.

Not proved:

- no positive universal lower bound for `alpha_dom` is obtained;
- arbitrary witness hypergraphs may have hyperedges of size greater than two;
- even for graph witnesses, arbitrary high-degree branching requires state-sensitive rather than scalar gluing;
- no full proof or refutation of Talagrand's source conjecture follows.

Accordingly the canonical status remains **PARTIAL / SOURCE OPEN**, and the frozen source metric has **NO MOVEMENT**.

---

# 7. Next mathematical attack

Use a nonrepeating triple:

- **B12 — find what is conserved:** derive the minimal two-state articulation message (articulation absent/present) whose product-side recursion and Talagrand-dual budget are both composable across block trees.
- **B15 — break symmetry on purpose:** test asymmetric double-stars and lopsided theta/block graphs to determine whether two articulation states suffice or whether a higher-dimensional message is forced.
- **B25 — count the same thing twice:** charge witness contributions simultaneously by edges and articulation blocks, seeking a block-tree dual budget that exactly recovers the previous sunflower and degree-two certificates.

The goal is not another finite graph checker; it is a compositional theorem for bounded block-tree complexity, or an exact smallest graph showing why that state space is insufficient.
