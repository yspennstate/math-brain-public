SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-22T20:39:15Z.
attacking: the density-normalized three-bank extraction interface; quantify the forced within-bank leakage instead of assuming that a diffuse spectral core can be collapsed to three clean scalar banks.

# account03/B05 — diffuse full-spark obstruction to leakage-free scalar-bank coarea

**Run:** `20260922T203915Z-account03-B05-QFORM-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `RIGOROUS INTERMEDIATE-REDUCTION COUNTEREXAMPLE + SOURCE-VALID TARGET CONTROL / FULL QFORM OPEN`.

## 1. Exact target and correction discipline

The full target is unchanged. For independent real coordinates with probability densities bounded by one and an arbitrary real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or produce a target-valid counterexample. No Gaussian, moment, support, log-concavity, post-rotation independence, or diagonal-basis hypothesis is added. Continuity is tracked separately.

This run attacks the first unpaid interface created by the new account02/B05 three-scalar core theorem: can the three spectral directions always be compressed into three disjoint scalar product banks with a uniformly nonsingular density-normalized `3 x 3` core, while all variables internal to those banks disappear except through the three scalars? The answer is **no**. A completely explicit rank-three projection family shows that every exact scalar-sufficient bank contains only one original coordinate, so the normalized three-scalar core has smallest singular value at most `3/n -> 0`. The same family is nevertheless uniformly paid by the completed diffuse ridge-window theorem. Thus this is a counterexample to a stronger extraction mechanism, not to QFORM.

No arbitrary-joint coarea estimate, normalized conditional-density supremum, positive conditional projection-density moment, fiber-supremum argument, one-minor reciprocal averaging, or law-uniform pointwise quadratic phase decay is used.

## 2. Completed mathematics consumed

### 2.1 General three-scalar core theorem

Fresh source: account02/B05 run `20260922T202100Z-b05-qform-47d9c1a2`, canonical commit

`yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`.

It proves `QFORM-THREE-BANK-GENERAL-CORE-v1`: if `Y_1,Y_2,Y_3` are independent scalar variables with densities at most one and a symmetric `3 x 3` matrix `M` satisfies `sigma_min(M)>=s>0`, then, uniformly over arbitrary affine terms,

`||p_(Y^T M Y + ell^T Y+c)||_infinity < 36/s`.                (2.1)

It also records the density-normalized version for disjoint scalar banks. This run applies (2.1) below to an actual physical-coordinate conditional inequality and then proves that a stronger leakage-free grouped-scalar extraction cannot be universal.

### 2.2 Diffuse spectral-window theorem

Canonical source:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

If `P_H` is the spectral projection of `A` onto `|lambda|>=1/64`, the target spectral hypothesis holds, and

`max_i (P_H)_ii <= 1/32`,                                      (2.2)

then the full form, with arbitrary additional spectrum and all original-coordinate product laws retained, has a continuous `C_0` density with

`||p_Q||_infinity <= 288 sqrt(3e)/13 <64`.                    (2.3)

### 2.3 Exact assigned partner status

The designated partner is `account04/B05`. Fresh searches of both authorized repositories found no completed current-QFORM artifact from that exact slot; its visible commits remain the superseded BT4 line. I therefore do not fabricate a partner theorem or PASS. The current account02/B05 theorem (2.1), which explicitly consumes and applies the preceding account03/B05 r16 result, is used as the compatible B05 peer result in this run. The exact-partner requirement remains operationally blocked by source absence, not by mathematics.

## 3. The diffuse full-spark target family

Fix `n>=5`. Put

`theta_k=2 pi k/n`, `k=0,...,n-1`,

and let `R_n` be the `n x 3` real matrix whose `k`th row is

`r_k=(1/sqrt(n), sqrt(2/n) cos(theta_k), sqrt(2/n) sin(theta_k)).` (3.1)

The usual roots-of-unity sums give

`R_n^T R_n=I_3`.                                                (3.2)

Define

`P_n=R_n R_n^T`.                                                (3.3)

Then `P_n` is an orthogonal projection of rank three. Its spectrum is exactly

`{1,1,1,0,...,0}`.                                             (3.4)

Thus every `P_n` lies in the exact owner target with `s_3(P_n)=1`.

Every row has the same leverage

`||r_k||^2=1/n+2/n=3/n`,                                      (3.5)

hence

`(P_n)_{kk}=3/n`.                                              (3.6)

### Full-spark property

Any two distinct rows of `R_n` are linearly independent. Indeed their first coordinates agree and are nonzero; proportionality would therefore force equality of their cosine-sine pairs and hence equality of the underlying points on the unit circle.

Any three distinct rows are linearly independent. After removing the nonzero column scalings, their determinant is the determinant of three rows

`(1,cos theta_i,sin theta_i)`.

A vanishing determinant would put the three distinct points `(cos theta_i,sin theta_i)` on one affine line. A line meets the unit circle in at most two points. Therefore the determinant is nonzero. Consequently

`rank (R_n)_S = min(|S|,3)` for every nonempty `S` with `|S|<=3`, (3.7)

and in particular every subset of at least two rows has rank at least two.

An equivalent useful statement is that every nonzero vector in `range(R_n)` has at most two zero coordinates: its entries are samples of a nonzero first-degree trigonometric polynomial `a+b cos theta+c sin theta`, which has at most two zeros on the circle.

## 4. Exact notion of a scalar-sufficient physical bank

Let `A` be any symmetric matrix and `S` a set of original coordinates. Call `S` **scalar-sufficient** if there is a nonzero vector `u` supported on `S` such that, after fixing all original coordinates outside `S`, the conditional quadratic polynomial depends on `X_S` only through the one scalar

`U=u^T X_S`.                                                    (4.1)

This is precisely the leakage-free interface needed to replace a multi-coordinate physical bank by one scalar without conditioning on additional linear combinations of the same original coordinates. Such extra conditioning would generally destroy the cap-one product law, which is one of the live corrections.

### Lemma 4.1 — algebraic characterization

If `S` is scalar-sufficient, then

`rank A[S,:] <=1`.                                             (4.2)

#### Proof

For every fixed outside vector `z`, the conditional polynomial in `x=X_S` is

`x^T A[S,S] x + 2 x^T A[S,S^c] z + constant`.                 (4.3)

If this depends on `x` only through `u^T x`, then its Hessian has image contained in `span(u)`, so

`range A[S,S] subset span(u)`.                                 (4.4)

Moreover, for every `z`, the linear coefficient `A[S,S^c]z` must also lie in `span(u)`. Hence every column of the entire row block `A[S,:]` lies in `span(u)`, proving (4.2). QED.

For the projection `P_n=R_nR_n^T`,

`P_n[S,:] R_n = R_n[S,:] R_n^T R_n = R_n[S,:]`.               (4.5)

Therefore

`rank P_n[S,:]=rank R_n[S,:]`.                                (4.6)

Combining (3.7), (4.2), and (4.6) gives the first main conclusion.

### Theorem 4.2 — `QFORM-DIFFUSE-SCALAR-BANK-SUFFICIENCY-v1`

For the target-valid projection `P_n`, every scalar-sufficient original-coordinate bank has cardinality exactly one.

In particular, **no bank containing two or more physical coordinates can be collapsed exactly to one scalar while preserving the original product law and relegating all remaining dependence to outside-conditioned affine terms.**

This is the forced leakage statement: in this diffuse full-spark geometry, any nontrivial grouped scalar aggregate leaves at least one additional active within-bank direction.

## 5. Consequence for density-normalized three-bank extraction

Consider any three pairwise disjoint scalar-sufficient banks `S_1,S_2,S_3`. By Theorem 4.2 each is a singleton. Write the corresponding physical triple as

`I={i_1,i_2,i_3}`.                                              (5.1)

The conditional quadratic core after fixing all other original coordinates is exactly

`B_I=P_n[I,I]=R_n[I,:]R_n[I,:]^T`.                             (5.2)

It is positive definite by full spark. Its trace is

`tr B_I=sum_(j=1)^3 ||r_(i_j)||^2=9/n`.                        (5.3)

Hence

`boxed(sigma_min(B_I) <= 3/n.)`                                (5.4)

This already shows that no leakage-free three-scalar extraction of this type can provide a uniform core scale.

The conclusion is invariant under arbitrary nonzero rescalings of the three singleton aggregates. Indeed, let

`U_j=a_j X_(i_j)`,                                             (5.5)

and take inputs whose original density caps are attained, for example independent `Uniform[0,1]` variables. Then `U_j` has exact density cap

`L_j=1/|a_j|`.                                                 (5.6)

If `A_a=diag(a_1,a_2,a_3)`, the matrix of the physical core in the `U` coordinates is

`M=A_a^(-1) B_I A_a^(-1)`.                                    (5.7)

With `D=diag(L_1,L_2,L_3)`,

`D^(-1) M D^(-1)=S B_I S`,                                    (5.8)

where `S=diag(sign a_1,sign a_2,sign a_3)`. Therefore

`boxed(sigma_min(D^(-1) M D^(-1))=sigma_min(B_I)<=3/n.)`       (5.9)

Thus rescaling cannot rescue the density-normalized core.

### Corollary 5.1 — `QFORM-LEAKAGE-FREE-TRIBANK-EXTRACTION-FALSE-v1`

There is no universal `c>0` such that every target matrix admits three disjoint **scalar-sufficient** original-coordinate linear banks whose density-normalized compressed core has smallest singular value at least `c`.

The explicit counterexample family is `A=P_n` above, and its best possible scale within this exact leakage-free scalar-bank interface is at most `3/n`.

This refutes only that stronger intermediate extraction requirement. It does **not** refute the owner QFORM conjecture.

## 6. Actual application of the new account02/B05 theorem

The same family gives a concrete application of the completed three-scalar theorem rather than merely citing it. Fix any physical triple `I` and condition on every coordinate in `I^c`. Since these are original coordinates, the three surviving variables remain independent and retain density cap one. All cross terms with the conditioned coordinates become an arbitrary affine vector. Therefore (2.1) gives

`||p_(Q | X_(I^c)=z)||_infinity < 36/sigma_min(B_I)`           (6.1)

for almost every outside realization `z`. Averaging the conditional densities gives the identical unconditional bound

`||p_Q||_infinity < 36/sigma_min(B_I)`.                        (6.2)

Equation (5.4) explains why this **single physical triple** route is not uniform on the diffuse family: its available core scale can be only order `1/n`. The failure is not in the analytic three-scalar theorem; it is in trying to extract a uniformly conditioned clean scalar core before aggregation.

This is an actual target-level inequality obtained from the fresh account02/B05 result, with arbitrary outside couplings retained through conditioning.

## 7. The stress family is nevertheless uniformly paid

For `n>=96`, (3.6) gives

`max_k (P_n)_(kk)=3/n <=1/32`.                                 (7.1)

Since `P_n` itself is the spectral projection onto `|lambda|>=1/64`, the completed spectral-window theorem (2.3) applies directly to the **same** family, for every allowed independent input law:

`boxed(||p_(X^T P_n X)||_infinity <=288 sqrt(3e)/13<64.)`      (7.2)

Moreover that theorem gives a continuous density vanishing at infinity.

This comparison is the key point of the run:

- every exact leakage-free scalar-sufficient bank is a singleton;
- every three-singleton density-normalized core has scale at most `3/n`;
- nevertheless an aggregate diffuse argument proves a dimension-free density bound below `64` on the full family.

Therefore **within-bank residual leakage / aggregate curvature is not a perturbative nuisance that can be discarded before coarea. It is the resource that must be retained.**

## 8. A general projection compression identity locating the missing factor

The preceding obstruction has an exact coordinate-free algebraic form that is useful beyond the example.

Let `P=P^2=P^T` be any orthogonal projection. Let `U` be an `n x k` matrix with orthonormal columns, and complete it to an orthogonal matrix `[U W]`. Put

`M=U^T P U`, `E=U^T P W`.                                    (8.1)

The top-left block of `P^2=P` gives

`boxed(E E^T=M-M^2.)`                                         (8.2)

Hence, if the eigenvalues of `M` are `mu_j in [0,1]`, the nonzero squared singular values of the aggregate-to-residual leakage are exactly

`mu_j(1-mu_j)`.                                                (8.3)

So a compressed scalar core that is neither nearly absent (`mu_j≈0`) nor nearly reducing (`mu_j≈1`) necessarily carries macroscopic residual leakage. This is the precise factor missing from a naive “good compressed core implies clean three-scalar coarea” argument.

For example, if some compressed direction has

`s <= mu <=1/2`,                                               (8.4)

then the corresponding leakage singular value is at least

`sqrt(mu(1-mu)) >= sqrt(s/2).`                                 (8.5)

Thus a uniformly conditioned but genuinely nonreducing compression forces a uniformly nonzero leakage bank. A viable next coarea theorem should **spend (8.2)** rather than condition it away.

## 9. First unpaid implication after this run

The natural next B05 statement is

`QFORM-COMPRESSED-CORE-PLUS-LEAKAGE-COAREA-v1`:

> For three disjoint original-coordinate banks, prove a dimension-free interval/coarea estimate that jointly consumes a density-normalized `3 x 3` compressed core and the within-bank leakage currency `E E^T` (or an original-coordinate analogue of it), without conditioning on the orthogonal residual coordinates of the same bank. In the projection endpoint, use the exact conservation law `E E^T=M-M^2`; in the general symmetric case use `U^T A^2 U-M^2` as the corresponding total leakage matrix and route its original-coordinate pieces through an already-proved ridge/cross-bank payment.

This is narrower than the preceding “extract three scalar banks” goal. The new no-go shows that demanding zero internal leakage is structurally impossible even for a rank-three target projection whose density is already known to be uniformly bounded by the diffuse ridge theorem.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The full continuity conclusion remains open separately, although the stress family (7.2) has a continuous `C_0` density by the cited ridge theorem.

## 10. Computation / integrity note

A numerical regression check was run only as a sanity check, not as proof. For `n=5,8,16,96`, it verified `R^T R=I` to floating-point precision, `max diag(P)=3/n`, the rank-three projection spectrum, and `max_I sigma_min(P[I,I])<=3/n`. At `n=96`, the observed maximum smallest singular value was exactly `0.03125=3/96` to machine precision and the maximum principal-triple determinant was `3.0517578125e-05=27/96^3`. The analytic proof above does not depend on the finite check.

Only authorized private mathematical repositories were used. No scheduler mutation, notification change, email/Drive action, public release, paid model/API/Codex call, workflow launch, credential access, or cross-account authentication was performed. Repository transport is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
