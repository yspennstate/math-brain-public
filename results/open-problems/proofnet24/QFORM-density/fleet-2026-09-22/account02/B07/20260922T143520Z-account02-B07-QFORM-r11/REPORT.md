# account02/B07 — Pluecker stratum collar and full-spectrum cancellation stress

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Run: `20260922T143520Z-account02-B07-QFORM-r11`  
Assignment: coordinate minor selection / complementary constructions  
Classification: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. First unpaid implication and source state

The full target remains the arbitrary-product-law statement: independent real coordinates with densities at most one, and arbitrary real symmetric `A` having at least three eigenvalues of absolute value at least one, should give a universal density bound for `X^T A X`.

The first B07 debt inherited from the preceding run was the localized branch of determinant-weighted minor selection. The designated partner account03/B07 has now completed `QFORM-PLUCKER-COLLAR-TRICHOTOMY-v1`, canonical report `yspennstate/math-open-problems@3f7a03a9e3799798af3ed81e4f55ea6aed46efe9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/account03-B07-20260922T124045Z-qform-minors-v11/REPORT.md`. I apply its exceptional branch below rather than merely citing it.

Partner input: for a rank-three spectral frame `U^T U=I_3`, after the paid diffuse and minority-pivot branches fail there is an actual original-coordinate set `J`, `1<=|J|<=3`, such that

`det(U_{J^c}^T U_{J^c}) < 1/8`.                                      (1.1)

The partner also retains an ordered conditional-majority certificate and pivot restrictions, but the new argument below needs only (1.1).

Current corrections are respected: no pointwise law-uniform Fresnel decay, no independence after rotation, no fiber-supremum argument, and no claim that one small principal minor is enough. The live local-cross and single-Schur counterexamples are also kept in force.

## 2. New theorem: a localized set carries a constant Pluecker stratum

Let `U in R^{n x 3}` have orthonormal columns. For every coordinate triple `S`, put

`w_S = det(U_S)^2`.

Cauchy--Binet gives `sum_S w_S=1`. For a fixed coordinate set `J` and every `T subset J`, define the intersection-stratum mass

`m_T(J) = sum_{|S|=3, S cap J=T} w_S`.                              (2.1)

Then

`m_empty(J)=sum_{S subset J^c}w_S=det(U_{J^c}^T U_{J^c})`.          (2.2)

### Theorem `QFORM-PLUCKER-STRATUM-COLLAR-v1`

If `1<=|J|<=3` and `m_empty(J)<1/8`, then some nonempty `T subset J` satisfies

`m_T(J) > [7/8]/[2^{|J|}-1] >= 1/8`.                               (2.3)

Moreover this mass has one of the following exact factorizations.

**One fixed coordinate.** If `T={i}`, put `c_i=||u_i||^2`, let `P_i` be orthogonal projection in spectral `R^3` onto `u_i^perp`, and define on that two-dimensional plane

`R_i = sum_{k in J^c} (P_i u_k)(P_i u_k)^T`.

Then

`m_{i}(J)=c_i det(R_i)`.                                            (2.4)

Thus `m_i>=1/8` forces both `c_i>=1/8` and `det R_i>=1/8`.

**Two fixed coordinates.** If `T={i,j}`, put

`D_ij=det Gram(u_i,u_j)=||u_i wedge u_j||^2`,

and let `n_ij` be a unit normal to their span. Then

`m_{ij}(J)=D_ij sum_{k in J^c}<n_ij,u_k>^2`.                        (2.5)

Hence `m_ij>=1/8` forces both the physical spectral-pair area `D_ij>=1/8` and the remaining normal spectral energy at least `1/8`.

**Three fixed coordinates.** Necessarily `|J|=3`, `T=J`, and

`m_J(J)=w_J=det(U_J)^2`.                                            (2.6)

So this branch contains one coordinate triple of Pluecker weight at least `1/8`.

### Proof

The masses in (2.1) partition all triples. Equation (2.2) is Cauchy--Binet. Therefore the sum over nonempty `T` is greater than `7/8`; there are at most seven nonempty strata, proving (2.3).

For (2.4), choose an orthonormal spectral basis with first vector `u_i/||u_i||`. For `j,k in J^c`,

`det(u_i,u_j,u_k)^2=c_i det_2(P_i u_j,P_i u_k)^2`.

Sum over `j<k` and apply two-dimensional Cauchy--Binet. For (2.5),

`det(u_i,u_j,u_k)^2=D_ij <n_ij,u_k>^2`,

and summation gives the claim. Equation (2.6) is immediate. All covariance factors in (2.4)--(2.5) are contractions of `sum_k u_k u_k^T=I`, so each factor is at most one; the separate lower bounds follow from their product. QED.

### Application of the designated partner

Insert the `J` supplied by account03/B07 into the theorem. Its entire localized exceptional branch therefore contains a **constant-size determinant resource in one of only three packet shapes**:

`1+2`: one genuine physical coordinate and an outside transverse two-volume;

`2+1`: one genuine physical coordinate pair and an outside normal-energy bank;

`3`: one genuine physical triple.

This is stronger than saying merely that one spectral direction has more than half its energy on three coordinates. It carries the determinant weight through the localization and avoids a reciprocal cost for an arbitrarily tiny single minor in the first two packet types.

The exact-rank-three next step is to pay these three packets using the completed hyperbolic-square / Schur / mixed-bank theorems. In particular the `2+1` packet is the quantitative form of the two-heavy-plus-diffuse-tail bank appearing in account02/B19 `QFORM sequential-heavy determinant bank` (`yspennstate/math-research-brain` handoff from run `20260922T140533Z-account02-B19-qform-r12`).

## 3. New source-valid obstruction: selected-core minors need not survive the extra spectrum

A tempting bridge from the theorem to the full owner target is false: a constant Pluecker minor of the selected three-large-eigenvalue subspace does **not** imply a nondegenerate principal minor, nor a rank-two cross block, for the full matrix once the orthogonal spectral complement is restored.

Take `n=4`, let

`v=(1,1,1,1)^T/2`,

and let `U` be any orthonormal basis of `v^perp`; concretely use the first three columns of the normalized `4 x 4` Hadamard matrix, with `v` its fourth column. Give the three `U` directions eigenvalue `1`, and give `v` eigenvalue `-1/3`. Then

`A = U U^T -(1/3) vv^T = I-(4/3)vv^T = I-(1/3)J_4`.               (3.1)

Its spectrum is exactly

`{1,1,1,-1/3}`,                                                     (3.2)

so it is inside the full target class. Every three-row Pluecker weight of the selected large eigenspace is

`w_I=1/4`.                                                          (3.3)

Nevertheless every physical principal triple is singular:

`A[I,I]=I_3-(1/3)J_3`, hence `det A[I,I]=0` for every `|I|=3`.      (3.4)

Even more strongly, every `2+2` original-coordinate cross block has all entries `-1/3`, hence rank one. Thus this same matrix defeats the shortcut “large selected-core triple or packet => good full physical triple/cross-rank packet.”

This is **not** a counterexample to QFORM. It is a counterexample only to that transfer implication. It also lands exactly in the current hard geometric regime: for `H=A-diag(A)=(I-J_4)/3`, `||H||op=1` and `sr(H)=4/3`, so account03/B19's high-off-diagonal-stable-rank branch does not cover it.

The construction explains why the arbitrary-extra-spectrum debt is substantive rather than bookkeeping: a small orthogonal eigenvalue can cancel every good selected-core principal triple simultaneously while leaving the three required large eigenvalues untouched.

## 4. Exact check

A standard-library `Fraction` checker in this run verifies (3.1)--(3.4), all four core Pluecker weights, and all six `2+2` cross determinants exactly. Its terminal line is

`QFORM_PLUCKER_STRATUM_CANCELLATION_CHECK_PASS`.

The checker is only an exact regression of the explicit construction; the theorem in Section 2 is analytic.

## 5. Conditional end-to-end route and first remaining implication

The B07 route is now:

1. use determinant-weighted diffuse smoothing when the disjoint/balanced Pluecker mass is large;
2. use account03/B07's completed collar to obtain `J`, `|J|<=3`, when it is not;
3. apply `QFORM-PLUCKER-STRATUM-COLLAR-v1` to retain at least `1/8` of determinant mass in a single `1+2`, `2+1`, or `3` original-coordinate packet;
4. pay that packet **before** taking a reciprocal of one local minor;
5. in the full matrix, retain the orthogonal spectral complement throughout rather than replacing the selected-core packet by a principal minor of `A`.

The first unpaid implication is therefore

`QFORM-STRATUM-PACKET-NONSEPARABLE-TRANSFER-v1`:

> Given a selected three-large-eigenvalue frame and a stratum packet of mass at least `1/8` as in Section 2, convert that determinant bank directly into a dimension-free small-ball/density estimate while retaining an arbitrary orthogonal spectral complement. The mechanism must cover the exact stress matrix `A=I_4-J_4/3`; it may not assume that the selected-core principal minors survive in the full physical matrix.

For exact rank three, the same implication without the orthogonal remainder is a smaller predecessor and should be attacked through the existing dependent-square, mixed-Hessian and two-heavy/diffuse-tail bank results.

Full QFORM remains `OPEN / NOT PROVED`.

## 6. Source ledger

Fresh control: owner revision `2026-09-22.5`; no later stop observed before publication.

Applied designated partner result:
- account03/B07, `QFORM-PLUCKER-COLLAR-TRICHOTOMY-v1`, canonical package `yspennstate/math-open-problems@3f7a03a9e3799798af3ed81e4f55ea6aed46efe9`.

Compatible completed results used to locate the remaining packet debt:
- account02/B19 sequential-heavy determinant bank, handoff `20260922T140533Z-account02-B19-qform-r12`;
- account03/B19 off-diagonal stable-rank branch, handoff `20260922T140323Z-account03-B19-QFORM-r11`;
- interactive regularized-determinant theorem, canonical package `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`.

No moments, support regularity, Gaussianity, post-rotation independence, public data, paid calls, or benchmark material are used.