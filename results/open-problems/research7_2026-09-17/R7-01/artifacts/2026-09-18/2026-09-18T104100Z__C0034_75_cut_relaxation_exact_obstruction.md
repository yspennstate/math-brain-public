Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0034 — exact obstruction to the 75-cut H-description

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), Question 2.8; same endpoint as Question 10.1 in Lyons, *Determinantal Probability Measures* (2003).

This artifact addresses only the first unresolved finite rank profile

\[
\mathbb C^6=H_0\oplus H_1\oplus H_2,\qquad \dim H_i=2,
\]

through the 90-vertex colored-perfect-matching marginal polytope.  It does **not** solve or refute Lyons's full source question.

## 1. Why this calculation was necessary

The newest R7-01 reports proved two exact determinantal-valid facet orbits:

1. 30 balanced `3+3` cut facets;
2. 45 `2+4` crossing facets.

The prescribed B3/B19/B20 continuation asked whether affine constraints, nonnegativity, and those 75 cut facets might already define the six-point marginal polytope, in which case one could try a constructive decomposition theorem.

That conjectured H-description is false.  The failure is not numerical: the exact relaxation optimum of one already-known bridge facet is `1/3`, while the true colored-perfect-matching polytope satisfies that bridge facet with right-hand side zero.

## 2. The 75-cut relaxation

For `c in {0,1,2}` and an edge `e in binom([6],2)`, write `x_{c,e}`.  Let `Q_75` be the polyhedron given by

- `x_{c,e}>=0`;
- `sum_e x_{c,e}=1` for each color `c`;
- `sum_c sum_{e contains v}x_{c,e}=1` for each vertex `v`;
- all 30 balanced-cut inequalities

  \[
  t_r(X)\le t_s(X)+t_t(X),\qquad |X|=3,
  \]

  where `t_r(X)` is the color-`r` mass on edges internal to `X` or `X^c`;
- all 45 two-plus-four crossing inequalities

  \[
  c_r(X)\le c_s(X)+c_t(X),\qquad |X|=2,
  \]

  where `c_r(X)` is the color-`r` mass on edges crossing `X|X^c`.

Every genuine colored perfect-matching marginal belongs to `Q_75`, because the 75 inequalities are valid facets and the affine/nonnegativity constraints are necessary.

## 3. The residual bridge facet

Take

\[
L=\{0,3\},\qquad D=\{1,2\},\qquad R=\{4,5\}.
\]

Put

\[
S_A=\{01,02,03,13,23\},\qquad
S_B=\{14,15,24,25,45\}.
\]

The previously proved bridge inequality is

\[
\boxed{B(x):=x_0(S_A)-x_1(S_B)-x_2(S_B)\le0.}\tag{3.1}
\]

The exact checker in this run independently reconfirms on all 90 deterministic colored perfect matchings that `B` takes only the values `0` and `-1`; it is tight on 60 vertices, and those 60 vertices have equality-face affine dimension 36 inside the 37-dimensional polytope. Thus (3.1) is genuinely facet-defining.

## 4. B20 — an exact fractional obstruction

Define `x*` by the following nonzero coordinates; every omitted coordinate is zero.

Color 0:

\[
x^*_{0,01}=\frac16,\quad
x^*_{0,13}=\frac16,\quad
x^*_{0,23}=\frac13,\quad
x^*_{0,45}=\frac13.
\]

Color 1:

\[
\begin{aligned}
x^*_{1,01}&=\frac13,&x^*_{1,02}&=\frac1{12},&x^*_{1,04}&=\frac1{12},\\
x^*_{1,05}&=\frac16,&x^*_{1,12}&=\frac16,&x^*_{1,23}&=\frac1{12},&x^*_{1,34}&=\frac1{12}.
\end{aligned}
\]

Color 2:

\[
\begin{aligned}
x^*_{2,02}&=\frac1{12},&x^*_{2,04}&=\frac1{12},&x^*_{2,12}&=\frac16,\\
x^*_{2,23}&=\frac1{12},&x^*_{2,34}&=\frac1{12},&x^*_{2,35}&=\frac16,&x^*_{2,45}&=\frac13.
\end{aligned}
\]

Direct exact rational arithmetic gives

- all three color-sum equations equal one;
- all six vertex-incidence equations equal one;
- every coordinate is nonnegative;
- all 30 balanced-cut rows are `<=0`;
- all 45 crossing rows are `<=0`;
- but

\[
\boxed{B(x^*)=\frac13.}\tag{4.1}
\]

Hence `x* in Q_75` but `x*` is not in the true colored-perfect-matching marginal polytope.

This already disproves the proposed 75-cut H-description and proves that a decomposition algorithm using only those inequalities cannot be complete.

## 5. B3 — the obstruction is sharp: exact optimum `1/3`

The previous section gives a lower bound

\[
\max_{x\in Q_{75}}B(x)\ge\frac13.
\]

There is also a short exact dual certificate for the matching upper bound.

Let

- `A_1(x)<=0` be the balanced `3+3` inequality with `X={0,1,3}` and singled color 0;
- `A_2(x)<=0` be the balanced `3+3` inequality with `X={0,2,3}` and singled color 0;
- `A_3(x)<=0` be the `2+4` crossing inequality with `X={1,2}` and singled color 0.

Let the nine affine equality rows be ordered as the three color sums followed by the six vertex-incidence sums, and set

\[
\nu=\left(-\frac13,-\frac23,-\frac23,
          \frac23,\frac13,\frac13,\frac23,0,0\right).
\]

The exact checker verifies coefficient by coefficient the identity

\[
-B+\frac16(A_1+A_2+A_3)+\sum_{j=1}^9\nu_jE_j=R,\tag{5.1}
\]

where **every coefficient of `R` is nonnegative**, in fact each is either `0` or `1/3`.

For any `x in Q_75`, nonnegativity gives `R(x)>=0`, the three chosen cut rows satisfy `A_i(x)<=0`, and every affine equality has value one. Therefore

\[
B(x)
\le \frac16(A_1(x)+A_2(x)+A_3(x)) + \sum_j\nu_j
\le \sum_j\nu_j
=\frac13.
\]

Together with (4.1),

\[
\boxed{\max_{x\in Q_{75}}B(x)=\frac13.}\tag{5.2}
\]

Thus the missing bridge inequality is separated from the 75-cut relaxation by a genuine rational margin, not a degeneracy or floating-point artifact.

## 6. B19 — consequence for constructive decomposition

Suppose there were an algorithm that, using only membership in `Q_75`, decomposed every feasible point as a convex combination of the 90 ordered rainbow perfect matchings. Applying it to `x*` would represent `x*` as a true marginal point. But the bridge facet (3.1) is valid for every one of the 90 vertices and hence for every convex combination of them, whereas `B(x*)=1/3`. Contradiction.

Therefore:

**Theorem 6.1.** No exact decomposition theorem can use only the affine constraints, coordinate nonnegativity, the 30 balanced-cut facets, and the 45 crossing facets. At least one additional facet family is logically indispensable; the bridge family is already sufficient to witness this failure.

This does not say the bridge family plus the 75 cuts is complete.

## 7. Cumulative-history correction relevant to the handoff

A path-scoped recovery of useful neighboring reports found materially stronger earlier work on the same finite core than the newest R7-01 checkpoint had incorporated:

- an earlier campaign proved 270 bridge, 360 residue, and 1080 sparse-cover facet orbits determinantal-valid;
- its exact catalogue reached 4,450 facets and was then proved incomplete;
- exact subgroup recursion subsequently found new orbits of sizes 2,160 and 270, raising the catalogue to 6,880, and the new 270 orbit was later proved determinantal-valid;
- further exact subgroup recursion found new orbits of sizes 1,080 and 540, raising the certified **combinatorial** catalogue to at least 8,500 facets;
- the archived 540-orbit work proves several nontrivial Schubert/boundary validity strata but, in the retrieved checkpoint, not the full generic 540 orbit.

These are cumulative dependencies/obligations, not new claims of this run. In particular, 8,500 is a certified lower bound on the number of K6 facets, **not** a completeness theorem.

The present 75-cut obstruction is therefore best interpreted as an exact local diagnosis: the two recent cut-SOS families are useful but far from an H-description. Any future attack on the K6 core should start from the stronger inherited facet ledger rather than repeating a 75-facet completion attempt.

## 8. Exact certificate

Executed artifact:

`research7_2026-09-17/R7-01/artifacts/2026-09-18/2026-09-18T103700Z__C0034_75_cut_relaxation_bridge_gap.py`

Archived exact output:

```text
vertex_count=90
candidate_cut_facets=75
bridge_true_vertex_values={-1,0}
bridge_tight_vertices=60
bridge_equality_face_affine_dimension=36
relaxation_witness_bridge_gap=1/3
dual_cut_rows=bal013_color0,bal023_color0,cross12_color0
dual_cut_weight_each=1/6
dual_affine_multiplier_sum=1/3
dual_reduced_cost_values={0,1/3}
EXACT_RELAXATION_OPTIMUM=1/3
ALL_EXACT_CHECKS_PASS
```

No numerical fit, solver timeout, or approximate LP value is used in the promoted theorem.

## 9. Source metric

The frozen source metric remains

`R_univ := sup{r : every finite-ground-set orthogonal decomposition H=H1⊕H2 with dim H<=r admits the requested union-marginal coupling}`.

This run proves an obstruction only to one proposed finite-core proof architecture. It neither constructs a determinantal counterexample nor proves the rank-four/six-site case. Therefore

`R_univ >= 3 -> R_univ >= 3` — **NO MOVEMENT**.

Status: **PARTIAL / SOURCE OPEN / operational CLOSABLE threshold reached in R7-01**.
