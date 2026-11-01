Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0034 — source-baseline correction, rank-four dual reduction, and the minimal six-point colored-matching obstruction

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Question 2.8 (the same question appears as Question 10.1 in Lyons, *Determinantal Probability Measures*, Publ. Math. IHES 98 (2003)).

Status: **PARTIAL / SOURCE OPEN**. Nothing below is claimed as a full solution. Publication novelty is **UNVERIFIED**.

Run-start master snapshot for the surrounding R7-01 iteration: `ba20c7a8616be8c287584570222f6e8826278de7`. Fresh ownership recheck before delivery found the existing R7-01 claim `operations/claims/C0034.md` still intact on master `891ffbd11bebb7f5b92f0ad0db23b28687f7d094`.

## 1. Material source correction: the frozen metric did not start at rank one

The previous R7-01 C0034 artifact proved the total-rank-two case by a new fractional-orientation argument and recorded

`R_univ >= 1 -> R_univ >= 2`.

That movement claim was source-inaccurate. The proof itself remains mathematically useful, but the 2003 primary source already proves a stronger partial case.

Lyons proves stochastic domination for nested projection DPPs. More specifically, his Lemma 10.4 shows in codimension one that if `H' = H \oplus [u]`, then under any monotone coupling of `P^H` and `P^{H'}`, the added set has exactly law `P^[u]`. Proposition 10.3 extends the relevant monotone-coupling statement to the countable setting. Thus Question 10.1/2.8 is already positive whenever **one orthogonal summand has rank one**. The same source also explicitly states that duality gives a positive answer whenever the ambient ground set has size at most five.

Therefore the source-evidenced value of the frozen metric

`R_univ := sup{r : every finite-ground-set orthogonal decomposition H=H1\oplus H2 with dim H<=r admits the requested union-marginal coupling}`

is at least

`R_univ >= 3`.

Indeed, every nontrivial decomposition of total rank at most three has a rank-one summand. Hence the honest correction is

`previously recorded >=1 baseline -> source-corrected >=3 baseline`,

which is a **baseline correction, not research movement**. The previous exact rank-two argument is an independent reproof of a source-known consequence and must not be advertised as a new increase of `R_univ`.

The first rank shape not covered by this source argument is therefore

`rank(H1)=rank(H2)=2`, `rank(H)=4`.

Because the source also settles every ambient set with `|E|<=5`, the doubly minimal finite obstruction is a `2+2` decomposition on `|E|=6`.

## 2. B18 — translate the rank `2+2` problem to an exact transportation LP

Let `E` be finite. Let `H=H1\oplus H2` with `dim H1=dim H2=2`. For two-subsets `A,B` and four-subsets `T`, write

`a_A = P^{H1}(X1=A)`,

`b_B = P^{H2}(X2=B)`,

`c_T = P^H(X=T)`.

Since projection DPP cardinalities equal the projection ranks, any source-valid coupling is automatically disjoint. It is therefore exactly a family of numbers

`x_{A,B} >= 0`, indexed by disjoint two-subsets `A,B`,

such that

`sum_{B: B cap A=empty} x_{A,B} = a_A`,

`sum_{A: A cap B=empty} x_{A,B} = b_B`,

and

`sum_{A disjoint B, A union B=T} x_{A,B} = c_T`.

This is the exact finite source problem in the first unresolved rank.

### Exact Farkas dual

Introduce real potentials `alpha_A`, `beta_B`, `gamma_T`. Farkas' lemma says the LP is feasible if and only if

`sum_A a_A alpha_A + sum_B b_B beta_B + sum_T c_T gamma_T >= 0`

for every triple of potentials satisfying

`alpha_A + beta_B + gamma_{A union B} >= 0`

for every disjoint pair `(A,B)`.

For fixed `alpha,beta`, the smallest admissible `gamma_T` is

`gamma_T = - min_{A disjoint B, A union B=T} (alpha_A+beta_B)`.

Hence feasibility is equivalent to the nonlinear family

`sum_A a_A alpha_A + sum_B b_B beta_B`

`>= sum_T c_T min_{A disjoint B, A union B=T} (alpha_A+beta_B)`      (2.1)

for every pair of potentials `alpha,beta`.

Equation (2.1) is the exact blocking formula for the first unresolved rank. It is also a clean finite-certificate route to a counterexample: one exact rational orthogonal decomposition plus one exact dual violation would refute the source.

## 3. B21 — importing stochastic domination removes all one-body dual obstructions

The old source's monotone-coupling theorem gives a strong reduction of (2.1) that does **not** assume the desired union coupling.

### Theorem 3.1 (additive potentials can never separate)

Let `E` be finite and let `H=H1\oplus H2` be any finite-rank orthogonal decomposition. Consider the analogous exact union-coupling LP. If the first marginal dual potential has the additive form

`alpha_A = sum_{i in A} r_i`,

then the Farkas inequality holds for every second potential `beta`, however nonlinear. The symmetric statement holds with the roles of `alpha` and `beta` reversed.

#### Proof

Use stochastic domination `P^{H2} <=st P^H`, proved by Lyons for nested projection subspaces, and Strassen to choose a monotone coupling `(B,T)` with

`B ~ P^{H2}`, `T ~ P^H`, and `B subset T` almost surely.

Set `D=T\B`. Projection DPPs have deterministic cardinality equal to rank, hence `|D|=dim H1`. For each coordinate `i`,

`P(i in D) = P(i in T)-P(i in B)`

`= (P_H)_{ii}-(P_{H2})_{ii}`

`= (P_{H1})_{ii}`.

Consequently

`E alpha_D = sum_i r_i P(i in D)`

`= sum_i r_i (P_{H1})_{ii}`

`= E_{A~P^{H1}} alpha_A`.

Also `E beta_B = E_{B~P^{H2}} beta_B`. For every realization `T=D union B`,

`min_{A disjoint B', A union B'=T}(alpha_A+beta_{B'}) <= alpha_D+beta_B`.

Taking expectations gives exactly the Farkas inequality. QED.

### Consequence for the first unresolved `2+2` case

A rank-four counterexample cannot be detected by a dual witness that is only a sum of vertex prices on either side. Any genuine separating potential must contain **two-body interaction on both colors**.

For pair potentials, the additive subspace consists of `alpha_{ij}=r_i+r_j`. Modulo this gauge, the first genuinely relevant quantities are four-point cycle curvatures such as

`alpha_{ij}+alpha_{kl}-alpha_{ik}-alpha_{jl}`.

Thus an exact counterexample search should quotient out vertex potentials and search only the interaction/cycle space on both marginals. This is a substantial reduction in the dual search space and explains why ordinary one-point or degree constraints cannot see the obstruction.

## 4. B25 — on six points the uncolored perfect-matching obstruction always vanishes

Now take the doubly minimal case `E={1,...,6}`, `dim H1=dim H2=2`, and let

`H3 := H^perp`.

Since `dim H=4`, `dim H3=2`, and

`H1 \oplus H2 \oplus H3 = C^6`.

By determinantal complement duality, the original source coupling is equivalent to a joint law on a partition

`E = X1 disjoint-union X2 disjoint-union X3`

such that `Xr ~ P^{Hr}` for `r=1,2,3`. Thus the six-point problem is a **three-color perfect-matching coupling**.

For each color `r` and edge `{i,j}`, put

`w^r_ij := P^{Hr}(Xr={i,j}) = det(P_r[{i,j}])`,

where `P_r` is projection onto `Hr`, and define the uncolored edge weight

`m_ij := w^1_ij+w^2_ij+w^3_ij`.

### Theorem 4.1 (exact uncolored matching theorem)

The vector `m` always belongs to the perfect-matching polytope of `K6`. Equivalently, `m` is a convex combination of ordinary perfect matchings of the six coordinates.

#### Proof: degree equations

For a rank-two projection DPP,

`sum_{j != i} w^r_ij = P^{Hr}(i in Xr) = (P_r)_{ii}`.

Because `P_1+P_2+P_3=I`,

`sum_{j != i}m_ij=1`                                      (4.1)

for every vertex `i`.

#### Proof: the only nontrivial blossom inequalities

For `K6`, with (4.1), Edmonds' perfect-matching description reduces to checking

`m(E(S)) <= 1`                                             (4.2)

for every three-set `S`; five-set inequalities follow automatically from the degree equations.

Fix `|S|=3` and let

`A_r := P_S P_r P_S`

be the `3x3` positive-semidefinite compression to the coordinate subspace on `S`. Then

`A_1+A_2+A_3=I_3`, and `rank A_r<=2`.

The sum of the principal `2x2` minors of `A_r` is its second elementary symmetric function `e_2(A_r)`, hence

`m(E(S)) = sum_r e_2(A_r)`.                                (4.3)

Since `det A_r=0`,

`det(I-A_r)=1-tr(A_r)+e_2(A_r)`.

Summing over `r` and using `sum_r tr(A_r)=3` gives

`sum_r e_2(A_r)=sum_r det(I-A_r)`

`=det(A_2+A_3)+det(A_1+A_3)+det(A_1+A_2)`.                 (4.4)

It remains to bound the right side by one. Consider

`p(t1,t2,t3)=det(t1 A_1+t2 A_2+t3 A_3)`.

Every coefficient of this homogeneous cubic is nonnegative. Indeed, factor each `A_r=C_r C_r^*`; then Cauchy-Binet applied to the concatenated matrix

`[sqrt(t1) C_1 | sqrt(t2) C_2 | sqrt(t3) C_3]`

expresses `p` as a sum of squared `3x3` minors times monomials in the `t_r`.

Because `det A_r=0`, the pure-color cubic coefficients vanish. Each determinant `det(A_r+A_s)` is exactly the sum of the nonnegative monomials involving those two colors and no third color. The three pairwise sums are disjoint portions of the full coefficient sum, while the remaining three-color coefficient is also nonnegative. Therefore

`det(A_2+A_3)+det(A_1+A_3)+det(A_1+A_2)`

`<= det(A_1+A_2+A_3)=det I_3=1`.

Together with (4.3)-(4.4), this proves every blossom inequality (4.2), hence `m` is in the perfect-matching polytope. QED.

### Interpretation

At the first ambient size where the source was not already settled, **ordinary matching geometry cannot obstruct the coupling**. Any six-point counterexample must be genuinely colored: it must fail to synchronize the three rank-two DPP marginals even though their sum is already an exact fractional perfect matching.

## 5. A second exact six-point constraint: a rainbow support atom always exists

The DPP structure gives more than the uncolored theorem.

Choose orthonormal bases for `H1,H2,H3` and put them as three two-row blocks of a `6x6` unitary matrix `U`. Expanding `det U` by the three row blocks gives

`det U = sum_{A disjoint B disjoint C, A union B union C=E}`

`          eps(A,B,C) det(U_1[:,A]) det(U_2[:,B]) det(U_3[:,C])`.

There are exactly

`binom(6,2) binom(4,2) = 90`

ordered colored partitions. Moreover

`|det(U_r[:,A])|^2 = w^r_A`.

Since `|det U|=1`, the triangle inequality yields

`sum_{A,B,C partition E} sqrt(w^1_A w^2_B w^3_C) >= 1`.    (5.1)

Hence at least one rainbow partition satisfies

`w^1_A w^2_B w^3_C >= 1/8100`.                            (5.2)

In particular, every orthogonal `2+2+2` decomposition has at least one perfect matching in which all three assigned colored edges have positive marginal mass.

This is only a support atom, not yet a coupling. Subtracting an atom from the three marginal laws need not preserve the orthogonal/Pluecker structure, so naive induction stops here.

## 6. Counterexample to the tempting weaker colored relaxation

The preceding theorem might tempt one to hope that the following soft constraints are sufficient for a colored coupling:

1. each color has total edge mass one;
2. the uncolored sum has vertex degree one;
3. the uncolored sum satisfies every `K6` blossom inequality.

They are **not** sufficient.

On vertices `0,...,5`, define three edge distributions by

Color 0:

`w^0_23=1/3`, `w^0_45=2/3`;

Color 1:

`w^1_02=1/3`, `w^1_13=1/3`, `w^1_25=1/3`;

Color 2:

`w^2_01=2/3`, `w^2_34=1/3`,

with every other weight zero.

Exact rational enumeration verifies that every color has mass one, every vertex has total uncolored degree one, and every three-set has internal uncolored weight at most one. Thus the uncolored sum belongs to the perfect-matching polytope.

However there is **no supported rainbow perfect matching** at all. If color 0 uses `23`, the only disjoint color-2 choice is `01`, leaving `45`, absent from color 1. If color 0 uses `45`, color 2 must use `01`, leaving `23`, again absent from color 1. The other color-2 edge `34` intersects both color-0 options. Therefore no joint colored matching law can have these three marginals.

This point is **not** claimed to arise from orthogonal rank-two projections; in fact (5.1) proves that it cannot. Its role is to identify the gluing failure: Edmonds/blossom constraints alone lose essential determinantal color information.

The exact checker for this finite claim is archived beside this artifact as

`2026-09-18T055000Z__check_C0034_colored_relaxation.py`

with output

`2026-09-18T055000Z__check_C0034_colored_relaxation.out`.

The output ends `ALL_EXACT_CHECKS_PASS`.

## 7. What this run actually changes

Frozen metric, after correcting it against the primary source:

`R_univ >= 3  ->  R_univ >= 3` (**NO MOVEMENT**).

The run does **not** prove total rank four. It does, however, sharply reduce the first unresolved rank:

- the exact `2+2` Farkas obstruction is now written down;
- all dual witnesses that are additive on either marginal are ruled out by source-known stochastic domination;
- on the minimal ambient set `|E|=6`, every uncolored blossom obstruction is ruled out by an exact determinant argument;
- every genuine six-point DPP instance has a quantitatively positive rainbow support atom;
- a certified synthetic example proves that ordinary uncolored matching constraints are insufficient, so the missing ingredient must be a specifically colored determinantal/Pluecker inequality.

The clean next target is therefore: characterize the interaction part of the `2+2`, `|E|=6` Farkas dual after quotienting additive vertex potentials, and prove its inequalities from the Pluecker/orthogonality identities — or find an exact orthogonal decomposition violating one.

## 8. Dated literature/source check — 2026-09-18

Primary sources checked:

- Russell Lyons, *Determinantal Probability Measures*, Publ. Math. IHES 98 (2003), Question 10.1, Proposition 10.3, Lemma 10.4: https://numdam.org/articles/10.1007/s10240-003-0016-0/
- Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Question 2.8: https://arxiv.org/abs/1406.2707

Relevant later work checked in the bounded search:

- Russell Lyons and Andreas Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, ETDS 36 (2016), arXiv:1402.0969. This is an invariant monotone-coupling theorem for ordered equivariant DPPs, not a general solution of the orthogonal-decomposition union-marginal question.
- Andrew Vander Werf, *Simplex links in determinantal hypertrees*, J. Applied and Computational Topology 8 (2024), arXiv:2208.08534. Its abstract/introduction describes a special determinantal-hypertree case answering Lyons's Question 10.1 affirmatively, not the unrestricted source question.

The bounded exact-phrase and follow-up search did not locate a later theorem settling unrestricted Question 2.8/10.1. This is negative evidence only; it does **not** certify current openness or publication novelty.
