# fleet03/B03 — Pluecker random-cut decoupling for the exact-rank-three branch

**Run:** `20260922T125813Z-fleet03-B03-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Decoupled time integral`  
**Classification:** `ESSENTIAL_STEP_APPLIED / RANK3_BRANCH_ADVANCE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only.

## 0. Exact target, mechanism change, and corrections

The live target is the full statement: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension- and law-independent essential density bound for `Q=X^TAX`, or give a genuine counterexample. Continuity is separate.

This run deliberately changes mechanism from the preceding B03 all-order collision hierarchy. The preceding run proved the exact Gaussian-mollified collision identity `J_m(epsilon)=int p_epsilon^m` and showed that controlling every copy order exponentially is equivalent to an `L^infinity` density bound. Here I instead ask whether one can **decouple the original coordinates into two blocks before paying any reciprocal minor**, and use the already-proved integrated cross-block Fourier theorem on the resulting block.

The fresh correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is applied as a correction to the previous B03 report: conditioning on a conjugate sum/difference variable does not preserve a unit density cap. I do not use that step here. The all-order collision identities themselves are unaffected, but the challenged conditional-cap corollary from the previous report is not a premise of this run.

Other live corrections retained: no law-uniform pointwise one-dimensional Fresnel decay, no independence after spectral rotation, no naive fiber-supremum argument, no rank-two-cross-minor closure, and no universal constant `pi`.

The designated assignment partner `fleet04/B03` still had no completed current-QFORM handoff at the final partner scan. I therefore did not invent partner consumption. The compatible completed same-programme theorem actually applied below is the source-pinned cross-block result

`QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`,

from

`yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc:proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`.

For a partition of the **original coordinates** into two blocks whose cross block has rank `r>2` and nonzero singular-value product `Delta`, that theorem gives

`||p_Q||_infinity <= [2r/(r-2)] Delta^(-1/r)`.

For `r=3` this is `6 Delta^(-1/3)`. The proof preserves the independence of the two original-coordinate blocks and absorbs all within-block quadratic phases, so it is compatible with the current route corrections.

I also use the source-valid fleet02/B03 overlap-collapse adversary

`yspennstate/math-open-problems@ac57190328fc109873ebe3b17122d835abbc2c3a:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T121352Z-b03-qform-auto11/REPORT.md`

as a stress test. It shows why selecting one disjoint `3 x 3` packet before aggregation is not a universal mechanism.

## 1. Setup: the Pluecker probability law

Assume first that the matrix has **exact rank three**:

`A=U Lambda U^T`,

where `U` is `n x 3`, `U^T U=I_3`, and `Lambda` is real symmetric and invertible. Under the target rank-three spectral normalization one has `|det Lambda|>=1`.

Write `u_i^T` for row `i` of `U` and

`ell_i=||u_i||_2^2`.

Then

`sum_i ell_i=3`.

For every three-element subset `I` of `[n]`, define the Pluecker weight

`w_I = det(U_I)^2`.

Cauchy--Binet gives

`sum_{|I|=3} w_I = det(U^T U)=1`.                                      (1.1)

Thus the `w_I` form a probability distribution on triples.

A second exact identity is the one-point marginal

`sum_{I: i in I} w_I = ell_i`.                                        (1.2)

For completeness, scale only row `i` of `U` by `sqrt(z)`. On one hand Cauchy--Binet gives

`det(U(z)^T U(z)) = sum_{I: i notin I} w_I + z sum_{I: i in I}w_I`.

On the other hand

`U(z)^T U(z)=I_3+(z-1)u_i u_i^T`,

so the matrix determinant lemma gives

`det(U(z)^T U(z))=1+(z-1)ell_i`.

Comparison of the coefficient of `z` proves (1.2).

Let `I,J` now be two independent triples sampled from the probability law `w`. Define the **disjoint Pluecker mass**

`R(U)=P(I cap J=empty)=sum_{I cap J=empty} w_I w_J`.                   (1.3)

By the union bound and (1.2),

`1-R(U)=P(I cap J != empty)`
`       <= sum_i P(i in I and i in J)`
`       = sum_i ell_i^2`.

Therefore

`boxed( R(U) >= 1-sum_i ell_i^2. )`                                   (1.4)

This is already a useful collision statistic: localization of the rank-three spectral frame is exactly what can destroy the supply of disjoint volume samples.

## 2. Exact random-cut identity

Choose an auxiliary random subset `S` by placing each original coordinate independently in `S` with probability `1/2`; put `T=S^c`. This auxiliary randomness is only a proof of existence of one deterministic partition and is independent of the input law.

Define

`G_S=U_S^T U_S`, `G_T=U_T^T U_T=I_3-G_S`.

Cauchy--Binet gives

`det G_S = sum_{I subset S, |I|=3} w_I`,
`det G_T = sum_{J subset T, |J|=3} w_J`.

Multiplying and taking expectation, an ordered pair `(I,J)` contributes exactly when the triples are disjoint; then the six distinct membership constraints have probability `2^-6`. Hence

`boxed(
 E_S[det G_S det G_T] = R(U)/64.
)`                                                                    (2.1)

Combining (1.4) and (2.1), if

`kappa(U):=1-sum_i ell_i^2 >0`,

there exists a deterministic original-coordinate partition `(S,T)` satisfying

`boxed(
 det G_S det G_T >= kappa(U)/64.
)`                                                                    (2.2)

In particular both Gramians are positive definite for that partition.

A convenient leverage-only corollary follows from

`sum_i ell_i^2 <= (max_i ell_i) sum_i ell_i =3 max_i ell_i`:

if

`max_i ell_i <= eta <1/3`,

then one can choose `(S,T)` with

`det G_S det G_T >= (1-3eta)/64`.                                    (2.3)

This threshold is substantially larger than the `1/12` leverage threshold in the first random-Frobenius diffuse theorem and also extends beyond the commonly used row-norm `<=1/2` condition, which corresponds to leverage `<=1/4`.

## 3. Cross-block singular product generated by the cut

For the partition from Section 2, the original-coordinate cross block is

`B=A[S,T]=U_S Lambda U_T^T`.

Because `G_S,G_T` are positive definite, factor

`U_S=P G_S^(1/2)`, `U_T=R G_T^(1/2)`,

where `P,R` have orthonormal columns. Thus

`B=P [G_S^(1/2) Lambda G_T^(1/2)] R^T`.

The three nonzero singular values of `B` are exactly the singular values of the middle `3 x 3` matrix. Their product therefore equals

`boxed(
 Delta(B)=|det Lambda| sqrt(det G_S det G_T).
)`                                                                    (3.1)

Using (2.2),

`Delta(B) >= |det Lambda| sqrt(kappa(U))/8`.                          (3.2)

This step is where the Pluecker aggregation pays off: no individual physical `3 x 3` minor has been inverted. The determinant mass is aggregated first into a two-block cross operator.

## 4. Apply the completed cross-block Fourier theorem

The source-pinned `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1` theorem applies directly to the **actual full quadratic form** for this exact-rank-three matrix and the partition `(S,T)`. At rank three,

`||p_Q||_infinity <= 6 Delta(B)^(-1/3)`.

Substituting (3.2) proves the main theorem of this run.

### Theorem 4.1 — `QFORM-PLUCKER-RANDOM-CUT-v1`

Let `A=U Lambda U^T` have exact rank three, `U^TU=I_3`, and let the independent original-coordinate inputs have arbitrary probability densities bounded by one. Put

`kappa(U)=1-sum_i ||u_i||^4`.

If `kappa(U)>0`, then `Q=X^TAX` has a bounded continuous density and

`boxed(
 ||p_Q||_infinity
 <= 12 |det Lambda|^(-1/3) kappa(U)^(-1/6).
)`                                                                    (4.1)

Consequently, under the target normalization `|lambda_j|>=1`,

`boxed(
 ||p_Q||_infinity <= 12 kappa(U)^(-1/6).
)`                                                                    (4.2)

If instead only the leverage cap

`max_i ||u_i||^2 <= eta <1/3`

is recorded, then

`boxed(
 ||p_Q||_infinity <= 12 (1-3eta)^(-1/6).
)`                                                                    (4.3)

No post-rotation independence, pointwise one-dimensional oscillatory decay, moment assumption, support assumption, or finite-search certificate is used.

At the standard diffuse threshold `eta=1/4`, (4.3) gives the explicit elementary bound

`||p_Q||_infinity <= 12*2^(1/3) <15.12`.                              (4.4)

The existing Brascamp--Lieb diffuse theorem has a better constant on part of this region; the point here is different: (4.1) is a direct **aggregate-minor-to-decoupled-time-integral** theorem and remains valid throughout the larger range `eta<1/3`.

## 5. Exact stress test: the overlap-collapse family

The fleet02/B03 adversary has spectral basis `(e,p,q)` and six rows

`a e`, `epsilon e`, `p/sqrt(2)`, `p/sqrt(2)`, `q/sqrt(2)`, `q/sqrt(2)`,

where `a^2+epsilon^2=1`.

Every nonzero Pluecker triple contains one `e` row, one `p` row and one `q` row. There are four triples using the `a e` row, each with weight `a^2/4`, and four using the `epsilon e` row, each with weight `epsilon^2/4`.

An ordered pair of such triples is disjoint exactly when it uses opposite `e` rows, opposite `p` rows and opposite `q` rows. There are eight ordered disjoint pairs, each with product weight `a^2 epsilon^2/16`. Therefore

`boxed( R(U_epsilon)=a^2 epsilon^2/2. )`                              (5.1)

The exact random-cut identity gives

`E[det G_S det G_T]=a^2 epsilon^2/128`.                              (5.2)

The best balanced cut in this family has

`det G_S det G_T=a^2 epsilon^2/16`,

and hence, for `|det Lambda|=1`,

`Delta=a epsilon/4`,                                                  (5.3)

which is precisely the cross-block singular-product collapse recorded by fleet02/B03.

Thus the new theorem does **not** conceal the adversary: its disjoint Pluecker resource genuinely tends to zero as one of the two copies of the shared spectral direction disappears. This is why a universal proof still needs an overlap-aware/heavy-coordinate mechanism in addition to random-cut aggregation.

## 6. Relation to the preceding B03 collision hierarchy

The previous B03 run showed that one fixed copy order cannot by itself yield linear small-ball scaling in complete generality; an all-order exponential collision estimate would be sufficient and equivalent to `L^infinity` after mollification.

The present theorem finds a different route on a substantial structural branch:

1. use the rank-three spectral frame only to manufacture a deterministic **original-coordinate** cut;
2. preserve independence between the two original blocks;
3. aggregate Pluecker mass before paying a determinant;
4. apply the completed cross-block integrated Fourier theorem, which gives an actual `L^1_t` bound and therefore linear small-ball scaling immediately.

So all collision orders are not necessary on this branch. The hard part is now concentrated in the overlap-heavy regime where `R(U)` is small, plus the separate issue of arbitrary additional eigendirections.

## 7. What remains unpaid

This is not the full owner theorem.

**First unpaid exact-rank-three implication.** When `kappa(U)<=0` or merely too small for a useful constant, the spectral frame has enough repeated-coordinate overlap that the random-cut resource can collapse. The finite-heavy/flag and hyperbolic-square results in the current archive strongly suggest a hybrid theorem: either `R(U)` is bounded below and Theorem 4.1 closes the form, or a bounded heavy core supports an overlap-aware principal/hyperbolic smoother. The overlap-collapse family shows that this second branch is logically necessary.

**Full-matrix implication.** For matrices with more than three nonzero eigendirections, one cannot simply discard the remaining spectral component. Its cross block may alter or cancel the rank-three cross block selected from three eigenvectors. A full proof therefore needs either a partition theorem for the actual full `A[S,T]`, or a product-preserving reduction showing that additional eigendirections can be absorbed without destroying the smoothing certificate.

These are the next target-relevant obligations. The full conjecture remains `OPEN`; continuity for the full target also remains separate.

## 8. Correction and status ledger

- `QFORM-FULL`: **OPEN**.
- `QFORM-PLUCKER-RANDOM-CUT-v1`: **PROVED in the exact-rank-three scope above**.
- `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`: **APPLIED mathematically**, not merely cited.
- `QFORM-UV-CONDITIONAL-CAP-FALSE`: **CONSUMED**; the challenged previous B03 conditional-cap step is not used here.
- fleet02/B03 overlap-collapse adversary: **APPLIED as an exact stress test**, equations (5.1)--(5.3).
- designated `fleet04/B03` completed current-program result: **NOT OBSERVED; no substitution or fabricated PASS**.
- native brain receiver/context use: **NOT OBSERVED**; execution remains `WITHOUT_VERIFIED_BRAIN`.

The proof uses only original-coordinate block independence and exact finite-dimensional linear algebra before invoking the already-proved cross-block Fourier theorem.