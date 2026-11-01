Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# H0008 admission-feasibility mathematics: finite-group covariance collapses a genuinely nonreversible multitype harmonic problem to one-type Galton-Watson

Date: 2026-09-19 UTC  
Worker: `R7-07` / native ID `6aabe8413f60819197825dd81ca138ae`  
Status: **PENDING_ADMISSION / H0008 NOT OWNED BY R7-07**  
Methods: **B7 TAKE THE LIMIT / B26 HUNT THE SPORADIC CASE / B14 FIND THE GROUP ACTING**

## 0. Scope, ownership, and source

This is bounded admission-feasibility mathematics on released HARD OUTSIDE source `H0008`. The canonical path `operations/claims/H0008.md` already exists and records `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`. R7-07's installed acquisition rule permits only create-only `operations/claims/<ID>.md` and requires a collision skip. Therefore this artifact does **not** claim H0008, does not modify the canonical history, and does not start an R7-07 source metric or stagnation counter.

The outside source is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), **Boundary fluctuations**. The still-open clause retained by R14 asks for the harmonic measure of the failed cluster and its expected dimension drop in the finite-type branching reduction.

The immediately preceding R7-07 run found a reversible slice through Altok's cycle criterion but had to correct an overstatement: cycle balance alone does not imply positive exit intensity in a general multitype environment. The present run deliberately attacks the first genuinely nonreversible case instead of trying to strengthen that reversible argument.

The key result below is a complete reduction for a large group-covariant family, including strongly nonreversible three-type examples. It uses the classical one-type harmonic-measure theorem of Lyons--Pemantle--Peres as prior art. It is **PARTIAL** with respect to H0008 and novelty is **UNVERIFIED**.

---

# 1. Source finite-type law

Let the finite type set be `D`. Under the H0008 failed-cluster reduction, a type-`i` vertex has a common potential-child count `nu`, with

\[
 m_*:=E\nu<\infty,
\]

and each potential child independently receives type `j` with probability `q_j` and transmits failure with probability `p_{ij}`. Thus the failed-child mean matrix is

\[
 M_{ij}=m_*q_jp_{ij}.
\]

The harmonic measure on a realized failed tree is the ordinary simple-random-walk harmonic measure on the unit-edge tree. Hence, once the **unlabelled** failed genealogy is fixed, the type marks do not alter electrical conductances or harmonic child probabilities.

This observation is useless in a general multitype model because the unlabelled genealogy itself depends on parent type. The point of the group action below is that it removes exactly that dependence while still allowing a nonreversible type circulation.

---

# 2. Method B14 — FIND THE GROUP ACTING

## 2.1 Group-covariant transmission family

Let `G` be a finite group of order `m`. Identify the type set with `G`. Assume

\[
 q_j=\frac1m\qquad(j\in G)
\]

and that there is a function

\[
 r:G\to[0,1]
\]

such that

\[
 \boxed{p_{ij}=r(i^{-1}j).}
 \tag{2.1}
\]

Thus transmission depends only on the group increment from parent type to child type. Put

\[
 R:=\sum_{g\in G}r(g),\qquad
 t:=\frac{R}{m},\qquad
 \alpha(g):=\frac{r(g)}R
\]

when `R>0`.

Assume the support of `r` generates `G`; then the mean matrix is irreducible.

## 2.2 Exact marked-Galton-Watson representation

### Theorem 2.1 (group-covariant collapse)

Under (2.1), the complete typed failed genealogy can be generated in the following equivalent way.

1. Generate an **ordinary one-type Galton--Watson tree** with offspring variable `K` satisfying, conditional on `nu`,
   \[
   \boxed{K\mid\nu\sim\operatorname{Bin}(\nu,t).}
   \tag{2.2}
   \]
2. Give every retained edge an independent group increment `Y_e` with law
   \[
   \boxed{P(Y_e=g)=\alpha(g).}
   \tag{2.3}
   \]
3. Choose a root type `U`; for a vertex `v` reached along edges `e_1,...,e_n`, set
   \[
   \operatorname{type}(v)=U\,Y_{e_1}\cdots Y_{e_n}.
   \tag{2.4}
   \]

The unlabelled tree is independent of all edge increments. In particular, survival is an event of the unlabelled Galton--Watson tree alone.

### Proof

Fix a parent type `i`. For a potential child and a group increment `g`, the probability that the child both receives type `ig` and transmits is

\[
 q_{ig}p_{i,ig}=\frac1m r(g).
\]

Summing over `g` gives total transmission probability

\[
 t=\frac1m\sum_gr(g).
\]

Conditional on transmission, the increment has law

\[
 P(g\mid\text{transmission})
 =\frac{m^{-1}r(g)}{t}
 =\frac{r(g)}R
 =\alpha(g),
\]

which is independent of `i`. Different potential children are independent, so conditional on `nu` the number retained is `Bin(nu,t)` and their increments are iid `alpha`, independent of that retained count.

Now iterate. If a retained child has type `ig`, its descendant transmission probabilities are

\[
 p_{ig,igh}=r((ig)^{-1}igh)=r(h),
\]

so after translating labels by the current vertex type the same law restarts independently. Induction over generations gives the representation (2.2)--(2.4). QED.

### Corollary 2.2 (Perron root and source boundary dimension)

The rows of `M` all sum to

\[
 m_*t.
\]

Since `M` is irreducible and nonnegative,

\[
 \boxed{\rho(M)=m_*t=EK.}
 \tag{2.5}
\]

Hence the source's failed-boundary dimension `log rho(M)` is exactly the ordinary one-type Galton--Watson boundary dimension `log EK` on this family.

### Proof

By (2.1),

\[
 \sum_jM_{ij}
 =\frac{m_*}{m}\sum_{g\in G}r(g)
 =m_*t.
\]

Thus the constant vector is a positive eigenvector with eigenvalue `m_*t`. Irreducibility makes this eigenvalue the Perron root. Equation (2.2) gives `EK=m_*t`. QED.

---

# 3. Exact harmonic-stationary lift without reversibility

The previous run used Altok to seek a **reversible** stationary environment before inducing harmonic exits. In the group-covariant family this detour is unnecessary: the unlabelled tree is exactly one-type, so the classical one-type harmonic environment can be lifted by independent group marks.

Assume throughout this section that

\[
 EK=m_*t>1,
\]

and the ordinary source moment/nondegeneracy hypotheses hold; in particular the finite-variance H0008 regime implies `E[K log K]<infinity`.

Let `P_GW^surv` be the one-type law in (2.2) conditioned on survival. Let `mu_GW` denote the classical Lyons--Pemantle--Peres harmonic-stationary environment on the forward tree. Their theorem gives, for a nondegenerate supercritical one-type Galton--Watson tree, an ergodic harmonic-descendant stationary law equivalent to `P_GW^surv` and strict harmonic-dimension drop outside the regular case.

## Theorem 3.1 (nonreversible group-covariant harmonic stationarity)

For every finite group-covariant H0008 law (2.1), there exists an ergodic probability `mu_G` on surviving **typed** forward trees such that

\[
 \boxed{\mu_G\sim P^{surv}}
 \tag{3.1}
\]

for any source root-type mixture with strictly positive mass on every type, and `mu_G` is stationary for the one-generation harmonic-descendant shift.

No transmission cycle-balance or reversibility condition is required.

### Proof

**Step 1: lift the one-type stationary tree.** Sample the unlabelled rooted tree `T` from `mu_GW`.

**Step 2: independently mark edges.** Conditional on `T`, assign iid increments `Y_e~alpha` to all forward edges.

**Step 3: choose root type uniformly.** Let `U` be uniform on `G`, independent of `T` and all marks, and assign vertex types by (2.4). Call the resulting typed-tree law `mu_G`.

**Step 4: harmonic selection ignores marks.** Given the unlabelled tree, the harmonic child is chosen using only the electrical escape conductances of child subtrees. Those conductances are functions of the unlabelled tree and are independent of the edge increments. Therefore the increment `Y_*` on the selected harmonic edge still has law `alpha` and is independent of the selected unlabelled forward subtree.

**Step 5: the new root type is again uniform.** After shifting to the chosen child, the new root type is

\[
 U'=UY_*.
\]

For every fixed `g`, right multiplication sends the uniform measure on a finite group to itself. Hence a mixture over `Y_*~alpha` also preserves uniformity:

\[
 U'\sim\operatorname{Unif}(G).
\]

The forward edge increments below the new root remain iid `alpha` by construction and branching independence.

**Step 6: the unlabelled law is stationary.** By the defining property of `mu_GW`, the selected unlabelled forward subtree again has law `mu_GW`.

Steps 4--6 show that the complete typed law after one harmonic-descendant shift is exactly `mu_G`. Thus `mu_G` is stationary. Ergodicity follows from the ergodicity of the one-type harmonic environment together with the irreducible iid increment process on the finite group (or, if the increment support generates a proper periodic class, after taking the corresponding finite cyclic component; the source irreducibility hypothesis rules out decomposition into different communicating type classes).

Finally, the source survival law itself has exactly the product representation `P_GW^surv` times the iid mark law, up to a strictly positive finite change in root-type weights. Since `mu_GW~P_GW^surv`, taking the same conditional mark kernel preserves mutual absolute continuity. This proves (3.1). QED.

## Corollary 3.2 (positive exit intensity on this entire slice)

The physical simple random walk on the group-covariant typed tree has exactly the same trajectory after forgetting types as simple random walk on the one-type Galton--Watson tree (2.2). Therefore its speed and last-exit intensity are the classical one-type quantities. In particular they are strictly positive in the nondegenerate supercritical regime covered by Lyons--Pemantle--Peres.

Thus the positive-exit-intensity hypothesis that remained open in the corrected cycle-balanced argument is **automatically discharged on the group-covariant slice**, even when the type kernel is nonreversible.

---

# 4. Harmonic dimension drop is completely inherited from one type

## Theorem 4.1 (dimension drop for group-covariant H0008 laws)

Under the hypotheses of Theorem 3.1,

\[
 \boxed{
 \dim_H(\mathrm{HARM})<\log\rho(M)
 }
 \tag{4.1}
\]

unless the failed genealogy is a deterministic regular tree. In the H0008 group-covariant parametrization, the equality/regular case is exactly

\[
 \boxed{
 t=1,\quad \nu\equiv k\ge2,
 }
 \tag{4.2}
\]

which is equivalent to

\[
 \boxed{
 r(g)=1\ \forall g\in G,\quad \nu\equiv k.
 }
 \tag{4.3}
\]

Thus the group-covariant slice matches the R14 zero-KL rigidity class: deterministic regular no-thinning.

### Proof

The harmonic cylinder mass of a ray depends only on the unlabelled tree, because all graph edges have unit conductance and the type marks do not enter the simple-random-walk transition probabilities. The generation metric on the boundary is also unchanged by adding marks. Therefore the typed harmonic local dimension is exactly the one-type harmonic local dimension for offspring `K`.

The one-type Lyons--Pemantle--Peres theorem gives strict dimension drop for every nondegenerate supercritical Galton--Watson offspring law and equality for the deterministic regular tree. By (2.5), the full boundary dimension is `log EK=log rho(M)`, proving (4.1).

It remains only to identify when `K` is deterministic. The conditional-binomial decomposition gives

\[
 \operatorname{Var}(K)
 =t(1-t)E\nu+t^2\operatorname{Var}(\nu).
 \tag{4.4}
\]

In a supercritical model `E nu>0` and `t>0`. Hence `Var(K)=0` iff `t=1` and `Var(nu)=0`. Since every `r(g)<=1` and

\[
 t=\frac1m\sum_gr(g),
\]

`t=1` forces every `r(g)=1`. This is (4.3). QED.

## Corollary 4.2 (circulation can vary while harmonic dimension is frozen)

Within the group-covariant family, the entire unlabelled harmonic law, speed, and harmonic dimension depend on `r` **only through its average**

\[
 t=|G|^{-1}\sum_gr(g).
\]

The antisymmetric/circulation part of `r` can change arbitrarily without changing any of those quantities, provided `t` and the potential-offspring law `nu` are fixed.

This is a structural warning for the general H0008 problem: transmission nonreversibility by itself cannot be the quantity controlling harmonic dimension.

---

# 5. Method B26 — HUNT THE SPORADIC CASE: the smallest genuinely nonreversible example

Take

\[
 G=\mathbb Z/3\mathbb Z,
 \qquad q_0=q_1=q_2=1/3,
\]

and

\[
 r(0)=1,
 \qquad r(1)=3/4,
 \qquad r(2)=1/4.
 \tag{5.1}
\]

Set `nu=4` deterministically. Then

\[
 R=2,
 \qquad t=2/3,
 \qquad EK=4(2/3)=8/3>1,
\]

so

\[
 K\sim\operatorname{Bin}(4,2/3)
\]

is supercritical and nondegenerate.

The conditional transmitted-child increment law is

\[
 \alpha=(1/2,3/8,1/8),
\]

so the type kernel is

\[
 \boxed{
 \Pi=
 \begin{pmatrix}
 1/2&3/8&1/8\\
 1/8&1/2&3/8\\
 3/8&1/8&1/2
 \end{pmatrix}.
 }
 \tag{5.2}
\]

Uniform type weights are stationary because `Pi` is circulant, but detailed balance fails:

\[
 \frac13\pi_{01}=\frac18,
 \qquad
 \frac13\pi_{10}=\frac1{24}.
\]

More sharply, around the directed three-cycle

\[
 0\to1\to2\to0
\]

the transmission product is

\[
 (3/4)^3=27/64,
\]

whereas the reverse-cycle product is

\[
 (1/4)^3=1/64.
\]

Hence the Kolmogorov/Altok cycle ratio is exactly

\[
 \boxed{27.}
 \tag{5.3}
\]

This is genuinely nonreversible, not a perturbative reversible example. Nevertheless Theorems 3.1 and 4.1 apply exactly, so it has an equivalent ergodic harmonic-stationary environment and strict harmonic dimension drop.

The exact checker

`research7_2026-09-17/R7-07/artifacts/2026-09-19/2026-09-19T190900Z__H0008_c3_group_slice_exact.py`

verifies the shard residue, all fractions in (5.1)--(5.3), uniform stationarity, failure of detailed balance, supercriticality, and

\[
 \operatorname{Var}(K)=8/9>0.
\]

Its archived output ends `ALL_EXACT_CHECKS_PASS`.

---

# 6. Method B7 — TAKE THE LIMIT: unbounded cycle defect with exactly constant harmonic geometry

The previous example sits in a one-parameter family that cleanly separates type circulation from harmonic geometry.

For `0<epsilon<1`, still on `C_3`, take

\[
 r_\varepsilon(0)=1,
 \qquad
 r_\varepsilon(1)=1-\varepsilon,
 \qquad
 r_\varepsilon(2)=\varepsilon.
 \tag{6.1}
\]

Then for every `epsilon`,

\[
 \sum_gr_\varepsilon(g)=2,
 \qquad
 t_\varepsilon=2/3.
\]

Therefore if `nu` is fixed, the **entire unlabelled failed genealogy is exactly the same for every epsilon**:

\[
 K\mid\nu\sim\operatorname{Bin}(\nu,2/3).
\]

In particular the simple-random-walk speed, exit intensity, harmonic stationary tree law, and harmonic dimension are all independent of `epsilon`.

Yet the directed three-cycle defect is

\[
 \boxed{
 D(\varepsilon)
 =\frac{p_{01}p_{12}p_{20}}{p_{10}p_{21}p_{02}}
 =\left(\frac{1-\varepsilon}{\varepsilon}\right)^3.
 }
 \tag{6.2}
\]

Hence

\[
 D(\varepsilon)\to\infty
 \qquad(\varepsilon\downarrow0),
\]

while the harmonic geometry is **exactly frozen**.

This gives a precise negative result about one prospective route:

> No quantitative dimension-drop estimate for the full H0008 problem can depend monotonically only on the Kolmogorov cycle defect, entropy production of the finite type chain, or distance from reversibility. Those quantities can diverge while the complete unlabelled harmonic problem remains unchanged.

The correct obstruction in the general multitype case must therefore measure how type circulation couples back into the **unlabelled offspring/conductance law**, not circulation alone.

The same construction works on every finite group: keep the average of `r` fixed while moving mass asymmetrically among group increments. The one-type tree remains fixed while the finite type chain can move far from reversibility.

---

# 7. Relation to the preceding H0008 frontier

This run changes the interpretation of the previous cycle-balanced route.

1. **Reversibility is sufficient but not necessary.** The prior Altok slice remains valid as a route when positive exit intensity can be shown, but Theorem 3.1 gives a large nonreversible slice with exact stationarity.
2. **The positive-exit-intensity gap is not universal.** It disappears whenever group covariance makes the unlabelled genealogy one-type, because classical one-type positive speed applies.
3. **Cycle defect is not the general obstruction.** The family (6.1) has arbitrarily large defect and identical harmonic geometry.
4. **The genuine remaining obstruction is type-dependent unlabelled branching.** Outside the group-covariant/lumpable categories, the parent type changes the law of the number and conductances of surviving children, so harmonic selection and type circulation no longer decouple.

A useful next abstraction is therefore not a stronger reversible theorem. It is a **quotient/lumpability theorem**: identify the broadest partition or hidden group action for which the unlabelled descendant law is independent of the current type, then lift the one-type harmonic environment through an independent or Markovian mark kernel.

---

# 8. Prior-art and novelty scope

This artifact does **not** claim the following classical ingredients as new:

- the one-type Galton--Watson harmonic-measure dimension-drop theorem and positive speed of Lyons--Pemantle--Peres;
- the general reversible multitype environment criterion of Altok;
- standard facts about iid edge markings and finite-group random walks.

The source-specific derivation here is the exact H0008 group-covariant collapse (2.2)--(2.4), its lift to a nonreversible harmonic-stationary typed environment, the exact equality-class identification, and the explicit fixed-geometry/unbounded-cycle-defect family (6.1)--(6.2).

A bounded 2026-09-19 search recovered the primary Kumar source still at arXiv:2608.15987v1, the Kumar--Duddala companion arXiv:2608.21125 on different open directions, Altok's 2013 multitype reversibility paper, Lyons--Pemantle--Peres's one-type harmonic-measure theorem, and Rousselin's later one-type random-environment extension. It did not surface this exact group-covariant H0008 reduction. That is negative search evidence only. **Novelty remains UNVERIFIED.**

---

# 9. Mathematical status

**PARTIAL FEASIBILITY / SOURCE OPEN / H0008 NOT OWNED BY R7-07.**

What is fully proved in this artifact:

- exact reduction of every finite-group-covariant H0008 law to a one-type Galton--Watson tree plus iid group increments;
- `rho(M)=m_*t`;
- exact construction of an equivalent harmonic-stationary typed environment without cycle balance;
- strict harmonic dimension drop on the whole group-covariant slice outside deterministic regular no-thinning;
- an exact nonreversible three-type supercritical example with cycle defect 27;
- a one-parameter family with unbounded cycle defect and exactly constant harmonic geometry.

What remains open:

- the general finite-type H0008 harmonic clause when parent type genuinely changes the unlabelled descendant/conductance law;
- an ownership-compliant canonical reassignment to R7-07;
- source-level closure, independent audits, and paper packaging.

The fixed R7-07 source metric remains `UNMEASURED` because no canonical source has been admitted to this slot.
