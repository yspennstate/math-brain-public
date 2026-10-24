# PROB20-12 backfill — prior task-response recovery

**BACKFILL STATUS: RECOVERED FROM ACCESSIBLE PRIOR TASK RESPONSES; NOT A PRIOR GITHUB CHECKPOINT**

This file archives genuine mathematical work visible in earlier completed task responses in the same research thread. The requested task-local GitHub directory did not exist when this run began, so these items were not previously durable in the repository. The backfill does not claim that every earlier sentence is correct: corrections and verification levels are recorded explicitly below.

## Provenance ledger

### Earlier response around 2026-09-14 12:03 UTC

Recovered claims:

1. For a finite full orthogonal decomposition `C^n=H0 direct-sum H1 direct-sum H2`, choosing a unitary `U` with column blocks `Ji` spanning `Hi`, an exact **signed** solution to the full marginal equations is obtained by

   `z(I)=conj(det U) sgn(I0,I1,I2) product_i det U[Ii,Ji]`

   on ordered row partitions `I=(I0,I1,I2)`, followed by taking `Re z(I)`. Laplace expansion and Jacobi complementary-minor identities give the correct one-color marginals. The unresolved point is nonnegativity.

2. The exact Farkas dual is weighted: arbitrary real subset costs are required. Earlier no-rainbow 0/1 family inequalities are necessary but not sufficient as a complete dual description.

3. A recursive conditioning idea was identified as problematic because excluding one coordinate from two different projection kernels generally destroys orthogonality of the residual pair.

Verification at the time: self-checked, not independent/formal.

### Earlier response around 2026-09-14 13:17 UTC

Recovered claims:

1. Finite projection case suffices for countable `E`: finite Naimark dilation gives a positive-contraction version, then finite-coordinate exhaustion and compactness give the countable limit.

2. Every **pair** among a full three-color orthogonal decomposition admits a disjoint coupling. One route is `Hi subset Hj^perp`, stochastic domination, Strassen, and complement duality.

3. All dual costs that are purely additive in one-point indicators are automatic from the ordinary transportation-polytope integrality constraints on the diagonal probabilities.

4. Artificial six-point colored marginals

   `mu0(02)=1`,
   `mu1(13)=mu1(45)=1/2`,
   `mu2(14)=mu2(35)=1/2`

   have correct aggregate vertex degrees but no colored perfect-matching coupling. This is **not** a Lyons counterexample; the pattern is not realizable as squared Pluecker marginals of three mutually orthogonal two-planes.

5. A natural sequential colored-DPP/Householder recursion was numerically diagnosed as wrong on random small unitary examples. This was only a route failure, not a counterexample to the conjecture.

Verification at the time: exact reductions self-checked; numerical diagnoses only.

### Earlier response around 2026-09-14 15:40 UTC

Recovered exact theorem:

Let `C^n=H0 direct-sum H1 direct-sum H2`, with ranks `r0+r1+r2=n`. Let

`p_i(A)=det U[A,Ji]`, `mu_i(A)=|p_i(A)|^2`.

Fix `A2`, put `C=E\A2`, and let `S` be any family of `r0`-subsets `B` of `C`. Define

`T={C\B : B subset C, |B|=r0, B notin S}`.

Then

`mu_2(A2) <= mu_0(S)+mu_1(T)`.

The proof used Jacobi + Laplace to write the `p2(A2)` coordinate as a sum of products `p0(B)p1(C\B)`, Cauchy-Schwarz after choosing one factor from each term according to `S`, and a pairwise disjoint coupling of `P_H0,P_H1` to show the complementary squared norm is at most one.

The equivalent strongest form for fixed `A2` is

`mu_2(A2) <= sum_B min(mu_0(B),mu_1(C\B))`.

This is referred to below as the **single-fibre cover inequality**.

Recovered numerical experiment:

For the first hard rank profile `(2,2,2)` on six points, the candidate marginal polyhedron defined by nonnegativity, color sums, aggregate vertex equations, and all single-fibre cover inequalities was compared against the true 90 colored-perfect-matching vertices in 300 random objective directions. The reported maximum objective discrepancy was at numerical roundoff, and returned optima were integral. This is **numerical evidence only** and not an exact polyhedral proof.

The earlier response also identified the exact separator of the artificial marginals above as a singleton specialization of the fibre-cover inequality, e.g.

`mu_2(14) <= mu_1(35)+mu_0(03)+mu_0(05)+mu_0(23)+mu_0(25)+mu_0(35)`,

whose artificial left side is `1/2` and right side is `0`.

### Earlier 2026-09-15 in-chat draft: rank-one theorem

A later task response re-derived the codimension-one/rank-one difference argument from a monotone coupling. **Correction:** this is historical prior art, not new progress. Lyons 2003 Lemma 10.4 proves exactly the finite-dimensional codimension-one statement, Proposition 10.3 extends the fixed-difference-cardinality monotone coupling, and the paper states that duality plus Lemma 10.4 settles all finite `|E|<=5`.

The finite-to-countable reduction remains useful, but no novelty is claimed for the rank-one argument.

## Recovered failed approaches

- Independent sampling: wrong union law and possible overlaps.
- Stochastic domination alone: for rank difference at least two, it fixes one-point difference intensities but not the full difference-set law.
- Naive iterative rank-one coloring: correct singleton increment marginals do not determine their joint union law.
- Naive residual conditioning of two colors: exclusion/exclusion generally destroys orthogonality.
- Ordinary colored DPP with exact projection blocks: a prior in-chat argument observed that positivity of a block kernel with a projection as a principal block forces the off-diagonal block to vanish, so this construction collapses to independence. This route is closed except for coordinate-disjoint trivial cases.
- Floating-point LP feasibility: evidence only, never an exact certificate.

## Recovery gaps

- No prior task-local GitHub report was available at the start of this run.
- Earlier local sandbox files and exact Python scripts are not assumed to persist. The mathematical statements above were reconstructed from accessible completed task responses, not from missing local files.
- No email/Gmail or Google Drive retrieval was performed in this owner-revised GitHub-only run.

## Verification status

This backfill preserves provenance and distinguishes exact derivations from numerics and corrected prior-art claims. It is not an independent verification pass and is not a full solution of Lyons Question 2.8.
