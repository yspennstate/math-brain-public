# The engine's unsplit term is positive-increment noise stability

Date: 2026-08-16  
Status: exact finite-product reduction proved; geometric inputs open; independent
referee review required before this is used as a campaign lemma.

Pinned inputs:

- `MG2B_framework_lemma_draft.md`, SHA-256
  `59c4b5a42edca0a7d53508f9b669cfaab3ba800d04b3e7effbd0312f040ab3f7`.
- `BLOCK_CHAOS_SPECTRAL_SPLIT_20260816.md`, SHA-256
  `03c4be46815478939699d98846121f9b4a938a963037b4052aaeeac5bb93336a`.

The second input isolates the spectrum of the block-use indicators. This note
applies the same noise calculation one step earlier in MG2B, before the two
Cauchy--Schwarz inequalities that split the engine into a fourth moment and an
unweighted block-overlap term. The result is a different conditional route, not
a proof of variance halving.

## 1. Keep the positive increment intact

Use the notation of MG2B. Let `X=X_(Mn)`, let `w_L'` be the independent
reservoir for block `L`, and put

`Delta_L=X^L-X,                 z_L=(Delta_L)^+.`              (1)

If the canonical old geodesic does not use `L`, that unchanged path remains
available after `L` is resampled, so `X^L<=X`. Consequently

`z_L=1_(U_L)(Delta_L)^+.`                                      (2)

This argument uses neither uniqueness nor a continuous weight law.

Write

`A_2^+=sum_L E[z_L^2].`                                       (3)

By exchangeability of `w_L,w_L'`, MG2B's endpoint identity also gives

`E[z_L^2]=E[Var(X | w_(L^c))].`                               (4)

Thus `A_2^+` is the total block-conditional variance. It is at most the
two-sided `A_2` used in MG2B.

Let `F_t` be the MG2B revealed-pair filtration and set `t=1-kappa`. The proof
of MG2B Theorem 8.1, stopped after its label-split step and before conditional
Cauchy--Schwarz, gives the sharper intermediate inequality

`Var(X) <= kappa A_2^+ + S_z(t),`                             (5)

where

`S_z(t)=sum_L E[(E[z_L | F_t])^2].`                           (6)

Indeed, the time split contributes `kappa sum_L E[z_L^2]`. For the other
piece, MG2B Lemma 5.2 gives

`(1-kappa)E[(E[z_L|F_t^(+L)])^2]
 <= E[(E[z_L|F_t])^2]`

for each `L`. Summing proves (5).

There is also a coupling reading. Take two conditionally independent
completions given `F_t`, and call their positive increments `z_L^(1),z_L^(2)`.
Then

`S_z(t)=sum_L E[z_L^(1) z_L^(2)].`                            (7)

This is an increment-weighted block overlap. A common block with negligible
resampling effect is automatically cheap.

This object is known in kind as a dynamical co-influence. At edge granularity,
Ahlberg--Deijfen--Sfragara (arXiv:2302.11367) developed a dynamical covariance
formula for FPP and compared edge co-influences with common-geodesic edges. The
campaign-specific point here is narrower: (6) is the term already present in
MG2B before its `A_4`--`Pbar` factorization, and it admits the block-pair ANOVA
split below. Existing edge-overlap chaos does not by itself bound (7): two paths
may traverse the same macroscopic block on disjoint edges.

## 2. Exact product-space spectrum

Regard each pair `(w_i,w_i')` as one product coordinate. For each `L`, let

`z_L=sum_(S subseteq I) z_(L,S)`

be its Hoeffding--ANOVA decomposition. The same retained-coordinate
calculation as in the block-label note gives

`E[(E[z_L|F_t])^2]
 =(E z_L)^2+sum_(S != empty)t^|S| ||z_(L,S)||_2^2.`            (8)

The labels disclose an independent Bernoulli-`t` subset of the pair
coordinates. Conditional expectation keeps exactly the ANOVA terms supported
inside that subset, and orthogonality removes all cross terms.

Exchangeability makes `Delta_L` symmetric, so

`C_z:=sum_L(E z_L)^2
    =(1/4)sum_L(E|X^L-X|)^2.`                                 (9)

This is the squared `L^1` block-influence mass. It is the full-resampling
floor of (6), replacing the unweighted collision floor `sum_L P(U_L)^2`.

For an integer `r>=2`, define

`B_(z,<r):=sum_L sum_(1<=|S|<r)||z_(L,S)||_2^2.`               (10)

Since

`sum_(S != empty)||z_(L,S)||_2^2=Var(z_L)<=E[z_L^2]`,

(8) yields the exact low/high split

`S_z(t) <= C_z+B_(z,<r)+t^r A_2^+.`                           (11)

Combining (5) and (11),

`Var(X) <= (kappa+t^r)A_2^+ + C_z+B_(z,<r).`                  (12)

## 3. Exact and approximate decision algorithms

Suppose first that a randomized adaptive algorithm `A_L` determines `z_L` by
querying pair coordinates. Its private randomness is independent of all block
variables, and let

`delta_L=max_i P(A_L queries i).`

The product-space Schramm--Steif estimate gives, for `k>=1`,

`sum_(|S|=k)||z_(L,S)||_2^2
 <= k delta_L Var(z_L).`                                     (13)

The proof is unchanged from the indicator case: center `z_L`, apply the
algorithm to its level-`k` ANOVA projection, and compare the top-level terms
before and after fixing the adaptive transcript. Unqueried coordinates retain
their product law. The lost level-`k` mass is supported on sets meeting the
query set, whose probability is at most `k delta_L`.

It follows that

`B_(z,<r)
 <= r(r-1)/2 sum_L delta_L Var(z_L).`                          (14)

Exact identification of a geodesic event may require exploring a large
region. An approximate form is therefore useful. Let an adaptive transcript
`T_L` query coordinates with revealment `delta_L`, but do not require it to
determine `z_L`, and set

`e_L=E[Var(z_L | T_L)].`                                     (15)

The approximate Schramm--Steif calculation gives

`sum_(|S|=k)||z_(L,S)||_2^2
 <= (sqrt(k delta_L Var(z_L))+sqrt(e_L))^2.`                   (16)

To verify (16), repeat the conditional Cauchy--Schwarz proof of (13). The
constant component of the restricted level-`k` projection costs at most
`sqrt(k delta_L Var(z_L))`; the part of the centered `z_L` left unresolved by
the transcript costs `sqrt(e_L)`. Divide by the level norm and square.

Let

`a_r=sum_(k=1)^(r-1) sqrt(k).`

Summing (16) and applying Cauchy--Schwarz over `L` gives

`B_(z,<r)
 <= r(r-1)/2 sum_L delta_L Var(z_L)
    +(r-1)sum_L e_L
    +2a_r sqrt((sum_L delta_L Var(z_L))(sum_L e_L)).`          (17)

Equation (14) is recovered when every `e_L=0`.

The original Boolean-cube exact and approximate estimates are Theorem 1.8
and equation (2.5) of Schramm--Steif,
*Quantitative noise sensitivity and exceptional times for percolation*,
arXiv:math/0504586. Their restriction-of-coordinates proof extends verbatim to
the present finite product spaces through the Hoeffding--ANOVA decomposition.

## 4. A variance-halving criterion

Let `D=Var(X_n)`. Assume the corrected moment ledger supplies

`A_2^+ <= beta C_occ M D.`                                   (18)

For exact algorithms define

`iota_z=C_z/(M D),`

`Delta_z=(1/(M D))sum_L delta_L Var(z_L).`                    (19)

Equations (12) and (14) give

`Var(X_(Mn))/(M D)
 <= beta C_occ (kappa+(1-kappa)^r)
    +iota_z+r(r-1)Delta_z/2.`                                 (20)

Hence the right side being at most `1/2` is sufficient for variance halving.
If every `delta_L<=delta`, then

`Delta_z<=delta beta C_occ`,

and a transparent four-way budget is

`kappa <= 1/(8 beta C_occ),`

`(1-kappa)^r <= 1/(8 beta C_occ),`

`iota_z <= 1/8,`

`delta <= 1/(4 beta C_occ r(r-1)).`                           (21)

For approximate algorithms also define

`epsilon_z=(1/(M D))sum_L e_L.`                               (22)

Then (12) and (17) give the more flexible sufficient condition

`beta C_occ (kappa+(1-kappa)^r)+iota_z
 +r(r-1)Delta_z/2+(r-1)epsilon_z
 +2a_r sqrt(Delta_z epsilon_z) <= 1/2.`                       (23)

No fourth-moment constant occurs in (20)--(23).

## 5. Relation to the old chaos gate

The old `A_4`--`Pbar` term is a sufficient upper bound on (6), not the exact
quantity produced by the engine. Conditional Cauchy--Schwarz gives

`(E[z_L|F_t])^2
 <= E[1_(U_L)(Delta_L^+)^2|F_t] P(U_L|F_t).`

The two later Cauchy--Schwarz steps in MG2B then give

`S_z(t)<=sqrt(A_4 Pbar(kappa)).`                              (24)

Thus (5) implies the published MG2B engine, while (12) retains information
discarded in (24). In particular, unweighted block persistence by itself no
longer forces failure; persistence matters in proportion to the positive
resampling increment.

This does not make the remaining work easy. The new obligations are:

1. a strict constant bound on the squared `L^1` block influences `C_z`;
2. low revealment for the increment `z_L`, or a transcript with small residual
   variance `e_L`;
3. the existing variance-scale block-conditional moment bound (18).

The straight-path control is still rejected. There `z_L` depends on its own
block pair alone, so its spectrum is entirely at degrees zero and one and any
exact algorithm must query that coordinate. Noise cannot push this mass to
high degree.

A recent last-passage paper explicitly warns that exploration algorithms can
be inadequate for optimizing paths because identifying a maximizer requires
large regions: Ahlberg--Hillairet--Toropova,
arXiv:2601.05361, Section 1. That warning applies to the missing construction
here. The approximate criterion (23) identifies exactly what a truncated or
localized exploration must prove instead of assuming exact low-revealment
identification.

The next useful geometric lemma is therefore not unweighted block chaos. There
are two attack surfaces for the same engine term: construct transcripts that
make (23) close, or bound the weighted conditional collision (7) directly at a
strict fraction of `M D`. The transcript criterion is sufficient; no converse
is asserted.
