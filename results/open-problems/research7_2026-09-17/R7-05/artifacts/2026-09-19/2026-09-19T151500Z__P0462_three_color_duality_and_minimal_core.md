Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0462 — three-color duality, exact finite dual, and the minimal 2+2+2 core

Worker: `R7-05`  
Target: `P0462`, Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Question 2.8.  
Status of this artifact: **PARTIAL**. It proves several exact finite reductions and new positive classes but does not settle the full source question.

## 1. Source problem and finite determinant coordinates

Let `E` be finite. Let `H_1,H_2` be orthogonal subspaces of `C^E`, and put

`H = H_1 \oplus H_2`.

Write `r=dim H_1`, `s=dim H_2`, and let `P_1,P_2,P=P_1+P_2` be the orthogonal projections. A projection DPP with range `H_i` has deterministic cardinality `dim H_i`.

Choose orthonormal-column matrices `U` and `V` spanning `H_1,H_2`. For `|A|=r`, `|B|=s`, and `|C|=r+s`,

`P^{H_1}(A)=|det U_A|^2`,
`P^{H_2}(B)=|det V_B|^2`,
`P^H(C)=|det [U V]_C|^2`.

A desired finite coupling is therefore a nonnegative array `w(A,B)` on disjoint pairs `A cap B=empty` satisfying

`sum_B w(A,B)=P^{H_1}(A)`,
`sum_A w(A,B)=P^{H_2}(B)`,
`sum_{A disjoint B, A union B=C} w(A,B)=P^H(C)`.

This is an exact finite transportation problem, not an approximation.

## 2. B2 — attack the negation first: the first obstruction cannot be small or additive

### Theorem 2.1 — finite counterexamples require three ranks at least two

Let

`K := H^perp`, `t:=dim K = |E|-r-s`.

If any one of `r,s,t` is `0` or `1`, then the finite source coupling exists.

#### Proof

The rank-zero cases are immediate, so assume one rank equals one.

**Case 1: `s=1`.** Let `H_2=span{u}` for a unit vector `u`. Since `H_1 subset H`, the standard stochastic-domination theorem for projection DPPs gives a monotone coupling

`A ~ P^{H_1}`, `C ~ P^H`, `A subset C` almost surely.

Projection-DPP cardinalities are deterministic, so `|C|-|A|=1`. Hence `B:=C\A` is a singleton and `A cap B=empty`, `A union B=C`.

For every coordinate `e`,

`P(B={e}) = P(e in C)-P(e in A)`
`            = P(e,e)-P_1(e,e)`
`            = P_2(e,e)`
`            = |u(e)|^2`.

That is exactly the rank-one projection-DPP law `P^{H_2}`. Thus `(A,B)` is the required coupling. The case `r=1` is symmetric.

**Case 2: `t=0`.** Then `H=C^E` and `H_2=H_1^perp`. Sample `A~P^{H_1}` and put `B=E\A`. Projection-DPP complement duality gives `B~P^{H_2}` and `A union B=E`, whose law is `P^H`.

**Case 3: `t=1`.** Let `K=span{z}`. Apply Case 1 to the orthogonal decomposition `H_1 \oplus K`. There is a coupling of

`A~P^{H_1}`, `D~P^K`

such that `A cap D=empty` and

`S:=A union D ~ P^{H_1 \oplus K}`.

Put `B:=E\S`. By complement duality,

`B ~ P^{(H_1\oplus K)^perp} = P^{H_2}`.

Moreover `A cap B=empty`, and

`A union B = E\D`.

Again by complement duality,

`E\D ~ P^{K^perp} = P^{H_1\oplus H_2}=P^H`.

So `(A,B)` is the required source coupling. This completes the proof. `square`

### Corollary 2.2 — the minimal finite obstruction is 2+2+2 on six coordinates

If the source question fails on a finite ground set, then

`r>=2`, `s>=2`, `t>=2`.

Hence `|E|=r+s+t>=6`. In particular **every finite instance on at most five coordinates is positive**.

At `|E|=6`, the only possible rank profile of a counterexample is

`(r,s,t)=(2,2,2)`.

Thus a finite refutation can be searched for without loss at the first unresolved size by studying three mutually orthogonal two-dimensional subspaces of `C^6`.

This strictly strengthens the previously recorded rank-one special case: co-rank one is also automatically positive.

### Theorem 2.3 — additive dual witnesses can never refute the coupling

Suppose `H_1,H_2,K` form an orthogonal decomposition of `C^E`, with projections `P_1,P_2,P_3`. For each color `c in {1,2,3}`, let

`f_c(S)=sum_{e in S} a_{c,e}`

be an additive set potential on subsets of the prescribed cardinality `r_c=rank(P_c)`.

Then the finite Farkas inequality for a partition coupling is automatically satisfied:

`E f_1(A)+E f_2(B)+E f_3(D)`
` >= min_{E=A' disjoint-union B' disjoint-union D'} [f_1(A')+f_2(B')+f_3(D')]`.

#### Proof

For projection DPPs, one-point inclusion probabilities are projection diagonals. Set

`m_{c,e}:=(P_c)_{ee}`.

Orthogonal decomposition gives

`sum_c m_{c,e}=1` for every `e`,

while traces give

`sum_e m_{c,e}=r_c` for every color `c`.

Hence `m=(m_{c,e})` is a feasible point of the transportation polytope with row capacities `(r_1,r_2,r_3)` and unit column demands. Therefore

`E f_1+E f_2+E f_3 = sum_{c,e} a_{c,e} m_{c,e}`.

The constraint matrix of this transportation problem is totally unimodular and all margins are integral. Its vertices are exactly the `0/1` matrices corresponding to coordinate partitions of `E` into blocks of sizes `r_1,r_2,r_3`. Hence the minimum of the linear cost over the fractional polytope equals the minimum over actual partitions. Since `m` is merely one feasible fractional point, its cost is at least that common minimum. `square`

**Interpretation.** Any finite obstruction must detect genuinely nonlinear subset correlations. One-point intensities, diagonal projection data, and every additive Farkas witness are provably incapable of refuting Question 2.8.

## 3. B11 — dualize: turn union coupling into a three-color partition problem

### Proposition 3.1 — complement / three-color equivalence

Let `K=H^perp`. The following are equivalent in the finite problem.

1. There is a source coupling `(A,B)` with
   `A~P^{H_1}`, `B~P^{H_2}`, and `A union B~P^H`.
2. There is a coupling `(A,B,D)` with
   `A~P^{H_1}`, `B~P^{H_2}`, `D~P^K`, such that
   `A,B,D` partition `E` almost surely.

#### Proof

If (1) holds, deterministic cardinalities give

`|A|=r`, `|B|=s`, `|A union B|=r+s`.

Thus `|A cap B|=0`, so `A` and `B` are disjoint almost surely. Put

`D=E\(A union B)`.

Projection-DPP complement duality gives

`D~P^{H^perp}=P^K`.

Conversely, from a partition coupling, `A union B=E\D`; complement duality gives

`E\D ~ P^{K^perp}=P^H`.

So (1) and (2) are equivalent. `square`

This formulation is useful because all three marginals are now symmetric: Question 2.8 asks whether the three projection-DPP base measures of an orthogonal decomposition admit a joint coloring of every coordinate exactly once.

### Proposition 3.2 — exact finite Farkas/Kantorovich criterion

Let `mu_c` be the three projection-DPP laws on subsets of sizes `r_c`, where `r_1+r_2+r_3=|E|`. A partition coupling exists if and only if for every three real functions `f_c` on their respective fixed-cardinality subset spaces,

`E_{mu_1} f_1 + E_{mu_2} f_2 + E_{mu_3} f_3`
` >= min_{E=A disjoint-union B disjoint-union D} [f_1(A)+f_2(B)+f_3(D)]`.

#### Proof

Necessity is immediate: under any partition coupling, the random value

`f_1(A)+f_2(B)+f_3(D)`

is pointwise at least its minimum over all allowed partitions; take expectation.

For sufficiency, introduce nonnegative variables `w(A,B,D)` only for partitions of `E` with the prescribed block sizes. The marginal equations are a finite linear feasibility system. If it is infeasible, Farkas separation supplies dual multipliers attached to the three sets of marginal equations whose weighted value on every allowed partition is nonnegative while their expectation under the prescribed marginals is negative. After adding a constant to normalize the partition lower bound, this is exactly a violation of the displayed inequality. Conversely, such a violation separates the prescribed marginal vector from the convex hull of partition incidence vectors and hence precludes a coupling. `square`

This proposition specifies what an exact finite refutation must look like: an explicit projection decomposition plus an explicit exact nonlinear triple `(f_1,f_2,f_3)` violating the inequality. Floating-point LP infeasibility is not enough.

### Proposition 3.3 — canonical signed coupling in the real orthogonal case

Assume now `E={1,...,n}` and work over the reals. Let

`R^n = H_1 \oplus H_2 \oplus K`

with ranks `r,s,t`, and choose an oriented orthogonal matrix

`Q=[U V W] in SO(n)`

whose three column blocks span the three subspaces.

For an ordered row partition `E=A disjoint-union B disjoint-union D` with `|A|=r`, `|B|=s`, `|D|=t`, let `epsilon(A,B,D)` be the sign of the row permutation that lists `A`, then `B`, then `D`, each increasingly. Define

`omega(A,B,D) = epsilon(A,B,D) det(U_A) det(V_B) det(W_D)`.

Then `omega` is a signed measure of total mass one and has exactly the three desired projection-DPP marginals:

`sum_{B,D: A disjoint-union B disjoint-union D=E} omega(A,B,D)=det(U_A)^2`,

and analogously for fixed `B` and fixed `D`.

#### Proof

Expand `det Q=1` by the three column blocks. The resulting full Laplace expansion is

`1 = sum_{A,B,D} epsilon(A,B,D) det(U_A)det(V_B)det(W_D)`,

so the total mass is one.

Fix `A`. Expanding the complementary minor `Q_{A^c, V∪W}` first into the `V` and `W` column blocks gives exactly the signed sum over `(B,D)` that appears above, divided by `det(U_A)`. Jacobi's complementary-minor identity for an orthogonal matrix gives the complementary minor, including its cofactor sign, as `det(U_A)` because `Q^{-1}=Q^T` and `det Q=1`. Multiplying back by `det(U_A)` yields `det(U_A)^2`. The same argument with the other column blocks fixed gives the other two marginals. `square`

**Interpretation.** Algebra already gives a perfect signed solution. The whole finite source problem is positivity: can the signed Plucker/Laplace mass be moved inside the kernel of the three marginal maps until it is nonnegative? A finite counterexample would mean the prescribed marginal point lies outside the convex hull of genuine partitions even though it has this canonical signed lift.

## 4. B5 — add a parameter: exact Givens-rotation positive families

The source problem is not fragile under a single elementary cross-color rotation.

### Proposition 4.1 — one Givens rotation has an explicit coupling for every angle

Start from a coordinate decomposition

`E=S_1 disjoint-union S_2 disjoint-union S_3`,

`H_c=span{e_i:i in S_c}`.

Choose two different colors `a,b`, coordinates `i in S_a`, `j in S_b`, and rotate the ambient two-plane `span(e_i,e_j)` by angle `theta`, leaving all other coordinates fixed. Apply this same orthogonal change to the three subspaces.

Then the resulting three projection-DPPs admit an exact partition coupling for every real `theta`:

- every unaffected coordinate keeps its original color;
- on the pair `{i,j}`, keep the original colors with probability `cos^2(theta)`;
- swap the two colors with probability `sin^2(theta)`.

#### Proof

For color `a`, an orthonormal basis consists of all its unchanged coordinate vectors plus the rotated vector

`cos(theta)e_i + sin(theta)e_j`

(up to the harmless sign convention of the Givens matrix). Therefore its projection DPP contains every unchanged coordinate of `S_a` and chooses `i` with probability `cos^2(theta)` or `j` with probability `sin^2(theta)`. Color `b` has the complementary rotated vector, so its DPP makes the opposite choice with the same two probabilities. The proposed shared Bernoulli swap realizes both marginals simultaneously and preserves a partition. The third color is unchanged. `square`

### Corollary 4.2 — disjoint elementary rotations remain positive

If one applies any collection of Givens rotations supported on pairwise disjoint coordinate pairs, with each pair joining two colors, then independent Bernoulli swaps on those coordinate pairs give an exact partition coupling.

Thus the first possible `2+2+2` obstruction cannot be generated by one local two-coordinate mixing, nor by a product of noninteracting such mixings. Any obstruction must use genuinely interacting/noncommuting multi-coordinate geometry.

## 5. The exact first unresolved finite core: colored perfect matchings of K6

For the minimal profile `(r,s,t)=(2,2,2)` on six coordinates, each projection DPP is a probability distribution on the 15 two-element subsets of `E`, i.e. on the edges of `K_6`:

`p_c({i,j}) = |det Q_{ {i,j}, c }|^2`,

where the two columns indexed by color `c` span the corresponding rank-two subspace.

A three-color partition of six coordinates into three 2-sets is exactly a **labeled perfect matching** of `K_6`: one edge assigned to each color. Therefore the minimal source question becomes:

> Given the three rank-two projection-DPP edge laws induced by an orthogonal decomposition of `C^6`, do they lie in the convex hull of labeled perfect matchings with those three color marginals?

There are 15 ordinary perfect matchings and `3!` assignments of their three edges to the colors, hence only `90` labeled perfect-matching atoms. This is the first finite core that an exact rational/algebraic certificate can decide.

The one-point constraints are automatically satisfied. Indeed, for a rank-two projection DPP of color `c`,

`sum_{j ne i} p_c({i,j}) = (P_c)_{ii}`.

Summing over the three colors gives one at each vertex because `P_1+P_2+P_3=I_6`. Theorem 2.3 explains why these degree constraints cannot be the obstruction. The missing inequalities must live at the level of correlated edge events / non-additive facets of the labeled matching marginal polytope.

## 6. What was ruled out and what remains

This run rules out four easy counterexample mechanisms:

1. no counterexample exists with `|E|<=5`;
2. rank-one or co-rank-one decompositions are always positive;
3. no additive/one-point Farkas witness can ever refute the problem;
4. one or several disjoint cross-color Givens rotations of a coordinate decomposition have explicit positive couplings.

It also provides two exact reformulations:

- three-color partition coupling;
- a canonical signed Plucker/Laplace coupling whose only defect is possible negativity.

The sharp remaining finite question is the `2+2+2` / six-coordinate colored-perfect-matching problem. A negative answer here would refute the full source question. A positive theorem here would not settle the source, but it would push the smallest possible finite obstruction beyond six and reveal which nonlinear facets must be controlled next.

## 7. Metric

Frozen source metric: `UC_RESOLVED`.

- before: `0`
- after: `0`
- movement: **NO MOVEMENT**

All results above are `PARTIAL`: they sharpen the finite obstruction architecture but neither construct the source coupling in full generality nor provide an exact counterexample.

## 8. Next nonrepeating methods

Next mathematical triple:

- **B16 — compute every small case and stare at the sequence:** enumerate the 90 atoms of the `2+2+2` core and derive the exact facet/dual structure with rational arithmetic, not floating-point feasibility.
- **B19 — make it an algorithm:** attempt a positivity-restoration algorithm that starts from the signed Plucker coupling and performs marginal-preserving cycle pivots.
- **B25 — count the same thing twice:** use complementary-minor identities and perfect-matching decompositions to test whether the projection/Plucker relations force every nontrivial matching-polytope facet.

Any finite infeasibility candidate must be upgraded to an exact Farkas certificate before it counts.
