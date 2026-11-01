Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0034 — a 30-facet genuinely colored orbit has an exact Plücker sum-of-squares certificate

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Question 2.8; same endpoint as Question 10.1 in Lyons, *Determinantal Probability Measures* (2003).

Scope of this artifact: the first unresolved finite core from the R7-01 STUCK1 diagnosis,

\[
\mathbb C^6=H_1\oplus H_2\oplus H_3,\qquad \dim H_1=\dim H_2=\dim H_3=2,
\]

viewed through the ordered-rainbow-perfect-matching marginal polytope. This artifact proves one complete nontrivial colored facet orbit on the Pluecker image. It does **not** prove all facets and does **not** settle the six-point core or the full source.

## 1. Finite polytope and a correction to the preceding diagnosis

For each color `r in {1,2,3}` and each two-set `e subset [6]`, let the color-edge coordinate be `x^r_e`. The deterministic vertices are ordered triples `(A,B,C)` of pairwise disjoint two-sets whose union is `[6]`; equivalently, ordered rainbow perfect matchings. There are

\[
15\binom42=90
\]

such vertices in `R^(3*15)=R^45`.

The exact checker in this run gives

- linear rank of the 90 incidence vectors: `38`;
- affine dimension of their convex hull: `37`.

The preceding STUCK1 report called `38` the affine dimension. That was a terminology/dimension error: `38` is the linear rank; the affine dimension is `37`. The immutable old report is not rewritten; this artifact records the correction.

The affine-dimension count is consistent with the obvious equalities: three color sums equal one and six vertex-incidence sums equal one, with one dependency among these affine equations.

## 2. A balanced-cut colored inequality

Fix a balanced coordinate cut

\[
[6]=X\sqcup Y,\qquad |X|=|Y|=3,
\]

and let

\[
T_X:=\binom X2\cup\binom Y2
\]

be the six edges internal to the two sides. For a color `r`, define

\[
t_r(X):=\sum_{e\in T_X}x^r_e.
\]

For every deterministic ordered rainbow perfect matching and every permutation `(r,s,t)` of the three colors,

\[
\boxed{t_r(X)\le t_s(X)+t_t(X).}\tag{2.1}
\]

### Combinatorial proof

A perfect matching of six vertices crosses a `3+3` cut in either one edge or three edges, since each side has odd cardinality. Therefore the total number of internal matching edges is respectively two or zero. If color `r` is internal, exactly one of the other two colors is internal, so both sides of (2.1) equal one. If color `r` is crossing, the other two colors are either both crossing or both internal, so the right side is respectively zero or two while the left side is zero. Thus the slack is always `0` or `2`.

The exact checker shows, for the canonical cut `X={0,1,2}` and singled color `r=1`, that 72 of the 90 vertices are tight and 18 have slack two. Those 72 tight vertices have affine dimension `36`, exactly one below the full affine dimension `37`. Hence (2.1) is a genuine facet.

Under `S_6 x S_3`, the canonical coefficient vector has orbit size `30`: ten unordered balanced cuts times three choices of singled color. Thus (2.1) supplies a complete 30-facet orbit.

This is genuinely two-body/colored rather than an additive one-body inequality. For example, the internal-edge indicator of a balanced cut has nonzero quadrilateral alternating sum: if `1,2` lie on one side and `4,5` on the other,

\[
1_{12\in T_X}+1_{45\in T_X}-1_{14\in T_X}-1_{25\in T_X}=2,
\]

whereas any edge cost of the additive form `a_i+a_j+c` has alternating sum zero.

## 3. Pluecker specialization

Now let `H_1,H_2,H_3` be mutually orthogonal two-planes spanning `C^6`. Choose an orthonormal basis of each `H_r`. For each coordinate edge `e={i,j}`, let

\[
w^r_e=|\Delta^r_e|^2
\]

be the squared `2 x 2` Pluecker minor. These are the rank-two projection-DPP edge probabilities and satisfy `sum_e w^r_e=1`.

For the fixed balanced coordinate cut, put

\[
t_r:=\sum_{e\in T_X}w^r_e.
\]

We prove the facet inequality

\[
\boxed{t_1\le t_2+t_3}\tag{3.1}
\]

for every such orthogonal flag, and by symmetry the whole 30-facet orbit follows.

## 4. B11 — exterior-square/block-projection reduction

Let `P_X` be the coordinate projection onto `span{e_i:i in X}`. Express it in the orthonormal basis obtained by concatenating bases of `H_1,H_2,H_3`, and call the resulting rank-three projection `Q`. Write it in `2 x 2` blocks `Q_rs`, with block `B_r` corresponding to `H_r`.

Set

\[
J:=2Q-I_6,
\qquad
A_r:=J_{rr}=2Q_{rr}-I_2,
\qquad
a_r:=\operatorname{tr}A_r,
\]

and for `r != s`

\[
h_{rs}:=\|J_{rs}\|_F^2=4\|Q_{rs}\|_F^2.
\]

Because `J` is a Hermitian involution, `J^2=I`. Taking the trace of its `(r,r)` block gives

\[
\operatorname{tr}(A_r^2)+h_{rs}+h_{rt}=2.\tag{4.1}
\]

Also `tr J=2 rank(Q)-6=0`, hence

\[
a_1+a_2+a_3=0.\tag{4.2}
\]

By Cauchy-Binet, the sum of the squared Pluecker minors of `H_r` using two coordinates from `X` is `det(Q_rr)`, while the corresponding sum using two coordinates from `Y` is `det(I_2-Q_rr)`. Therefore

\[
t_r=\det(Q_{rr})+\det(I_2-Q_{rr})
=\frac{1+\det A_r}{2}.\tag{4.3}
\]

For every `2 x 2` matrix `A_r`,

\[
2\det A_r=(\operatorname{tr}A_r)^2-\operatorname{tr}(A_r^2).
\]

Combining this with (4.1) gives

\[
4t_r=a_r^2+h_{rs}+h_{rt}.\tag{4.4}
\]

Subtract the `r=1` identity from the other two and use (4.2):

\[
4(t_2+t_3-t_1)
= a_2^2+a_3^2-a_1^2+2h_{23}
=2(h_{23}-a_2a_3).\tag{4.5}
\]

If

\[
q_r:=\operatorname{tr}Q_{rr},
\]

then `a_r=2(q_r-1)` and `h_23=4||Q_23||_F^2`, so (4.5) becomes

\[
\boxed{
 t_2+t_3-t_1
 =2\left(\|Q_{23}\|_F^2-(q_2-1)(q_3-1)\right).
}\tag{4.6}
\]

Thus the colored facet has been reduced to one scalar block-projection inequality.

## 5. B25 — count the same quantity as a projection-DPP occupation deficit

Let `Z` be any `3 x 6` matrix with orthonormal rows such that

\[
Q=Z^*Z.
\]

Cauchy-Binet gives

\[
\sum_{|S|=3}|\det Z_S|^2=\det(ZZ^*)=1.
\]

Hence

\[
\Pr(Y=S):=|\det Z_S|^2,\qquad |S|=3,
\]

defines a probability law on three-subsets of the six `H`-adapted basis indices. It is the rank-three projection determinantal law with kernel `Q`.

Let

\[
N_r:=|Y\cap B_r|,
\]

where each `B_r` has two elements. Then

\[
N_1+N_2+N_3=3\quad\text{a.s.},\qquad 0\le N_r\le2.\tag{5.1}
\]

Therefore, pointwise,

\[
(N_2-1)(N_3-1)\le0.\tag{5.2}
\]

Indeed, the only cases with nonzero product allowed by (5.1) are `(N_2,N_3)=(2,0)` and `(0,2)`, and in both cases the product is `-1`.

The determinantal inclusion identities give

\[
\mathbb E N_r=q_r
\]

and

\[
\mathbb E[N_2N_3]
=\sum_{i\in B_2}\sum_{j\in B_3}
\det\begin{pmatrix}Q_{ii}&Q_{ij}\\Q_{ji}&Q_{jj}\end{pmatrix}
=q_2q_3-\|Q_{23}\|_F^2.
\]

Consequently

\[
\mathbb E[(N_2-1)(N_3-1)]
=(q_2-1)(q_3-1)-\|Q_{23}\|_F^2\le0.
\]

Inserted into (4.6), this proves (3.1).

More is true: because the pointwise product in (5.2) is exactly minus the indicator of the two extreme occupation patterns,

\[
\boxed{
 t_2+t_3-t_1
 =2\Pr(N_2=2,N_3=0)
 +2\Pr(N_2=0,N_3=2).
}\tag{5.3}
\]

This is the desired positive combinatorial decomposition of the colored-facet slack.

## 6. Explicit four-square Pluecker certificate

Write the two-element block sets as `B_1,B_2,B_3`. The event `(N_2,N_3)=(2,0)` means

\[
Y=B_2\cup\{i\},\qquad i\in B_1,
\]

and `(N_2,N_3)=(0,2)` means

\[
Y=B_3\cup\{i\},\qquad i\in B_1.
\]

Using `Pr(Y=S)=|det Z_S|^2` in (5.3) gives the manifest sum-of-squares identity

\[
\boxed{
 t_2+t_3-t_1
 =2\sum_{i\in B_1}|\det Z_{B_2\cup\{i\}}|^2
 +2\sum_{i\in B_1}|\det Z_{B_3\cup\{i\}}|^2
 \ge0.
}\tag{6.1}
\]

There are exactly four squared `3 x 3` minors on the right. This is a complete written proof of the whole balanced-cut/singled-color facet orbit on the orthogonal Pluecker image.

Equality holds exactly when all four displayed minors vanish, equivalently when the auxiliary rank-three projection law gives zero mass to the two extreme block-occupation patterns.

## 7. B30 — one facet orbit is now completely solved

The preceding stuck diagnosis asked to stop broad LP search and solve one genuinely colored orbit completely. Equation (6.1) does that for the 30 balanced-cut facets. The proof uses only:

1. the balanced-cut matching parity;
2. Cauchy-Binet;
3. the involution identity `(2Q-I)^2=I`;
4. a three-particle occupation count over three two-element blocks.

This supplies a reusable mechanism: a colored matching facet may become tractable when its slack can be represented as the expectation of a pointwise nonnegative (or nonpositive) polynomial in block occupation numbers of an auxiliary projection DPP.

The mechanism does **not** yet imply every colored facet inequality. No complete irredundant facet enumeration is certified in this artifact, and no claim is made that the 30 balanced-cut facets exhaust the genuinely colored facets. Therefore the six-point rank-`2+2` source core remains open.

## 8. Exact finite certificate

The exact checker

`2026-09-18T082400Z__check_C0034_balanced_cut_colored_facet.py`

uses only integer/Fraction arithmetic. Its archived output verifies

```text
vertex_count= 90
linear_rank= 38
affine_dimension= 37
canonical_gap_counts= {0: 72, 2: 18}
tight_vertex_count= 72
tight_face_affine_dimension= 36
S6xS3_orbit_size= 30
balanced_cut_x_singled_count= 30
ALL_EXACT_CHECKS_PASS
```

The checker certifies the finite polyhedral statements. The Pluecker/DPP inequality itself is established by the written proof above, not by numerical sampling.

## 9. Source scope and metric

The frozen source-matching metric remains

`R_univ := sup{r : every finite-ground-set orthogonal decomposition H=H1⊕H2 with dim H<=r admits the requested union-marginal coupling}`.

The currently evidenced source-aware value remains

`R_univ >= 3`.

This artifact proves one nontrivial family of dual inequalities on the first unresolved total-rank-four/six-point core but does not prove that all dual inequalities hold. Therefore

`R_univ >= 3 -> R_univ >= 3` — **NO MOVEMENT**.

Status: **PARTIAL / SOURCE OPEN / CLOSABLE OUTSIDE**.

## 10. Dated literature boundary — 2026-09-18

The ICM proceedings still state Question 2.8 exactly as the orthogonal-decomposition union-marginal coupling question. Lyons--Thom proves monotone couplings for ordered determinantal measures, which is related but does not impose the required union law. Vander Werf's *Simplex links in determinantal hypertrees* gives a special affirmative determinantal-hypertree instance of Lyons's earlier Question 10.1 rather than an unrestricted solution. A bounded fresh search did not locate a later theorem resolving the general source question. This is negative evidence only: current global openness and publication novelty remain **UNVERIFIED**.

## 11. Next mathematical target

The next run should not repeat B11/B25/B30. The natural next triple is:

- **B16 — exact small cases:** identify and exact-certify one next low-complexity genuinely colored facet orbit beyond the balanced-cut family;
- **B18 — translate the statement:** seek an occupation-statistic representation of that next facet in the auxiliary rank-three projection law;
- **B24 — extremal object:** optimize the next facet slack over the `2+2+2` flag manifold, aiming either at a sum-of-squares lower bound or an exact violating flag.

The source metric should remain fixed. If these methods do not prove all remaining six-point facets or exhibit a counterexample, report no movement rather than redefining the metric.
