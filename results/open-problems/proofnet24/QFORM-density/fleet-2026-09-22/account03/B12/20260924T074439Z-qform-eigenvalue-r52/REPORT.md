SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T07:44:39Z.
attacking: replace the worst principal-angle obstruction by the full principal-angle spectrum, so several exactly/near-resonant directions may be spent without imposing any magnitude or rank bound on the added signed packet.

# account03/B12 — principal-angle-spectrum shielding and resonance-dimension stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T074439Z-qform-eigenvalue-r52`  
Status: **NEW SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and valid inputs

The owner target remains the unrestricted product-law conjecture: the coordinates are independent real random variables with arbitrary densities bounded by one; `A` is an arbitrary real symmetric matrix having at least three eigenvalues of absolute value at least one. No Gaussianity, log-concavity, moments, compact/connected support, iid law, eigen-coordinate independence, or convolution treatment of a quadratic remainder is used.

Fresh source controls and the live correction inbox were read from `yspennstate/math-research-brain/main`. In particular, this report does not use the refuted uniform pointwise quadratic van-der-Corput claim, arbitrary-joint coarea gate, conditional-density cap/moment gates, naive fiber-supremum argument, or any assertion that a small coefficient remainder is an independent random error.

The completed designated partner actually used is account04/B12 r8:

- repository/commit: `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`;
- theorem: `QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`.

The density receiver used below is the completed account03/B12 five-square-mode compiler:

- repository/commit: `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`;
- theorem: `QFORM-FIVE-SQUARE-MODE-E3-CORE-COMPILER-v1`.

It states that for an ORIGINAL-coordinate carrier `H` of size `m>=5`, if

`lambda_5((A^2)[H,H]) >= h^2 > 0`,

then

`||p_(X^T A X)||_infinity <= sqrt(24*pi*m + K_3^2)/h`,

where `K_3=3*2^(4/3)*exp(1/3)`, and the density has a representative in `C_0(R)`.

## 2. The missing implication attacked first: several resonant directions, not one worst angle

The previous B12 angle shield used only the largest canonical correlation between the old carrier image and the added carrier image. That forces failure as soon as **one** direction is exactly aligned, even when many other directions remain uniformly transverse. For a five-mode receiver this loses too much information: only the fifth surviving singular value matters.

The correct object is therefore the entire canonical-correlation spectrum.

Let `M,N in R^(n x m)`, with `M` of full column rank, and write

`R = Ran(M)`, `S = Ran(N)`.

Let `U in R^(n x m)` have orthonormal columns spanning `R`, and let `Pi_S` be the orthogonal projection onto `S`. Define

`c_1 >= c_2 >= ... >= c_m >= 0`

by

`c_i^2 = lambda_i(U^T Pi_S U)`,

with zero padding when `dim S < m`. Thus the `c_i` are the canonical correlations (cosines of principal angles) between the protected carrier image and the added carrier image.

Put

`g = s_m(M) > 0`.

### Theorem 2.1 — `QFORM-PRINCIPAL-ANGLE-SPECTRUM-SHIELD-v1`

For every `j=1,...,m`,

`boxed: s_j(M+N) >= g sqrt(1-c_(m-j+1)^2).`                 (2.1)

Equivalently, for every `q=0,...,m-1`,

`boxed: s_(m-q)(M+N) >= g sqrt(1-c_(q+1)^2).`              (2.2)

This is completely magnitude-free in `N`: its norm, rank, signs in a symmetric realization, and spectral magnitudes are unrestricted. The theorem says that one may spend `q` highly resonant carrier directions and pay only the `(q+1)`st canonical correlation.

### Proof

Let `Pi_perp = I-Pi_S`. Since `Pi_perp N=0`,

`Pi_perp(M+N)=Pi_perp M`.

For every `x`, orthogonal projection can only decrease norm, hence

`||(M+N)x||^2 >= ||Pi_perp Mx||^2`.

Equivalently in Loewner order,

`(M+N)^T(M+N) >= M^T Pi_perp M`.                              (2.3)

Therefore for every singular index `j`,

`s_j(M+N) >= s_j(Pi_perp M)`.                                (2.4)

Factor `M=UB`, where `B=U^T M` is invertible. Since `U` is an isometry on `R^m`,

`s_m(B)=s_m(M)=g`.

The standard singular-value product inequality gives

`s_j(Pi_perp U B) >= s_j(Pi_perp U) s_m(B)
                   = g s_j(Pi_perp U)`.                      (2.5)

Now

`(Pi_perp U)^T(Pi_perp U)
 = I-U^T Pi_S U`.                                             (2.6)

The eigenvalues of `U^T Pi_S U` are `c_1^2,...,c_m^2` in decreasing order. Hence the singular values of `Pi_perp U`, in decreasing order, are

`s_j(Pi_perp U)=sqrt(1-c_(m-j+1)^2)`.                        (2.7)

Combining (2.4)-(2.7) proves (2.1), and setting `j=m-q` gives (2.2). QED.

### Relation to the previous worst-angle theorem

Taking `q=0` in (2.2) yields

`s_m(M+N) >= g sqrt(1-c_1^2)`,

which is exactly the prior angle shield. The new theorem is strictly stronger whenever a few canonical correlations are close to one but the next correlations are separated from one.

## 3. Sharpness, including symmetric signed additions

The index and sine factor in (2.2) are simultaneously sharp.

Take `n=m+1`, let the ORIGINAL-coordinate embedding be the first `m` basis vectors, and set

`M = g [e_1,...,e_m]`.

Fix `q<=m-1` and `0<c<1`. Construct a symmetric added matrix `G` as follows. For `i<=q`, set

`G_ii=-g`,

so the first `q` carrier columns are cancelled exactly. On coordinates `(q+1,m+1)`, use the symmetric block

`[[-g c^2, -g c sqrt(1-c^2)],
  [-g c sqrt(1-c^2), 0]]`,

and set all other entries relevant to the carrier columns to zero. Let `N=GP`.

Then `Ran(N)` has canonical correlations with `Ran(M)` equal to

`1,...,1 (q times), c, 0,...,0`.

Moreover, `M+N` has `q` zero singular values, `m-q-1` singular values equal to `g`, and one singular value exactly

`g sqrt(1-c^2)`.

Hence

`s_(m-q)(M+N)=g sqrt(1-c_(q+1)^2)`,

so (2.2) is sharp even under the symmetry constraint required by QFORM. At the endpoint `c_(q+1)=1`, one can cancel `q+1` directions exactly, so no positive norm-free lower bound at this index is possible.

## 4. QFORM specialization and dense-tail stability

Let `H` be `m` ORIGINAL coordinates and `P:R^m->R^n` their coordinate embedding. Let `A_*` and `G` be real symmetric matrices. Put

`M=A_*P`, `N=GP`, `g=s_m(M)>0`,

and let `c_1>=...>=c_m` be the canonical correlations between `Ran(A_*P)` and `Ran(GP)`.

Since the final matrix is symmetric,

`((A_*+G)P)^T((A_*+G)P)
 = P^T(A_*+G)^2P
 = ((A_*+G)^2)[H,H]`.

Therefore Theorem 2.1 gives the actual final-matrix square-energy inequality

`boxed:
 sqrt(lambda_(m-q)(((A_*+G)^2)[H,H]))
 >= g sqrt(1-c_(q+1)^2).`                                    (4.1)

No rotation of the random vector occurs.

Now add an arbitrary symmetric dense matrix `T` and set

`epsilon=||TP||_op`.

Singular-value Weyl gives

`boxed:
 sqrt(lambda_(m-q)((A^2)[H,H]))
 >= [g sqrt(1-c_(q+1)^2)-epsilon]_+,
 A=A_*+G+T.`                                                  (4.2)

Again, `X^T T X` is not treated as an independent random error; only its deterministic action on the physical carrier is used.

One may additionally add a completely uncontrolled symmetric packet `R_0` satisfying `rank(R_0P)<=r`. Rank interlacing after (4.1), followed by the same tail estimate, gives whenever `q+r<=m-1`

`boxed:
 sqrt(lambda_(m-q-r)((A^2)[H,H]))
 >= [g sqrt(1-c_(q+1)^2)-epsilon]_+,
 A=A_*+G+R_0+T.`                                              (4.3)

Thus the canonical-angle budget and a literal finite-rank budget can be combined without any size restriction on either `G` or `R_0`.

### Theorem 4.1 — `QFORM-RESONANCE-DIMENSION-FIVE-MODE-STABILITY-v1`

If

`m-q-r >= 5`

and

`h = g sqrt(1-c_(q+1)^2)-epsilon > 0`,                        (4.4)

then every independent cap-one product input satisfies

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24*pi*m+K_3^2)/h`,                                  (4.5)

and the density has a representative in `C_0(R)`.

This is a dependence-safe stability theorem for arbitrary smaller and larger added eigenvalues of either sign. The packet `G` may be full rank and have unbounded spectrum; only the number/strength of its resonant **carrier-image directions** is charged.

## 5. Scalar overlap-energy corollary

Define the subspace-overlap energy

`Omega = tr(Pi_R Pi_S)=sum_(i=1)^m c_i^2`.

Since `c_1>=...>=c_m`,

`(q+1)c_(q+1)^2 <= Omega`,

hence

`c_(q+1)^2 <= Omega/(q+1)`.

Therefore (2.2) implies the coarser but sometimes easier-to-check bound

`boxed:
 s_(m-q)(M+N)
 >= g sqrt((1-Omega/(q+1))_+).`                               (5.1)

This identifies a useful structural obstruction: if the five-mode branch fails because `c_(m-4)` is close to one, then at least `m-4` canonical correlations are close to one. Failure is therefore a **high-dimensional near-alignment certificate**, not merely one bad direction.

## 6. Required account04/B12 application at an actual inequality

Apply the completed account04/B12 r8 theorem to an ORIGINAL-coordinate carrier of size

`m=8`,

with hub dimension `p=2` and transverse dimension `ell=6`. Assume its aligned-packet aggregates satisfy

`s_2(Lambda)>=4`,
`s_6(R)>=2`,
`||Lambda^(-1)W^T||_op<=1`.

The partner's equation (3.8) gives

`s_8(P_H A_*)
 >= gamma(1) min{4,2}
 = ((sqrt(5)-1)/2)*2
 = sqrt(5)-1
 = 1.2360679774997898... .`                                  (6.1)

This is the required equation-level use of the designated partner result.

Now add a **single arbitrary symmetric packet** `G` of unrestricted rank, signs, eigenvalue magnitudes and operator norm. Impose only the fourth canonical-correlation condition

`c_4(Ran(A_*P_H), Ran(GP_H)) <= 1/2`.                         (6.2)

The first three correlations may equal one: three carrier directions may be exactly resonant or exactly cancellable. No decomposition of `G` into a transverse packet plus a separately finite-rank resonant packet is required.

Finally add any symmetric dense `T` satisfying only

`||TP_H||_op <= 1/20`.                                       (6.3)

Take `q=3`, `r=0` in (4.2). Then the actual final matrix satisfies

`boxed:
 sqrt(lambda_5((A^2)[H,H]))
 >= (sqrt(5)-1)*sqrt(3)/2 - 1/20
 = 1.0204662693192699... > 1.`                                (6.4)

Thus this family is genuinely inside the owner target class (`s_5(A)>1`, hence `s_3(A)>1`). Applying the completed five-mode compiler at `m=8` gives

`boxed:
 ||p_Q||_infinity
 <= sqrt(192*pi+K_3^2) /
    ((sqrt(5)-1)*sqrt(3)/2-1/20)
 = 26.193889202899033... < 26.194.`                           (6.5)

The density has a representative in `C_0(R)`.

Compared with the preceding B12 worst-angle theorem, this is a real enlargement. There is no requirement that the whole added packet make a positive angle with the baseline image and no need to peel off the aligned directions as a separate finite-rank matrix. The same full-rank/unbounded packet may contain three perfectly aligned hostile directions while its remaining carrier-image directions are protected by the fourth principal angle.

## 7. Deterministic computation

The committed checker `check_principal_angle_spectrum.py` generated 10,000 seeded symmetric baseline/packet/tail instances. For every instance it checked (2.2) at **all** `q=0,...,m-1`, and then checked the dense-tail version (4.2) at all the same indices.

Results in `CHECK_RESULTS.json`:

- spectrum violations: `0`;
- minimum observed spectrum margin: `0.0003015994840604093`;
- dense-tail violations: `0`;
- minimum observed dense-tail margin: `0.0033561501997330396`.

These are only floating-point sanity checks. The proof is the projection/Loewner inequality (2.3), the singular-value product inequality (2.5), and the exact principal-angle spectrum identity (2.6)-(2.7).

## 8. Exact remaining gap

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

This result removes a further obstruction from the additional-eigenvalue problem: an arbitrary signed packet may have several completely resonant/cancelling physical carrier directions and arbitrary remaining rank/magnitude, while every sufficiently transverse canonical direction is preserved quantitatively.

The next B12 structural implication is now sharper. Starting from only `s_3(A)>=1`, one must prove that either:

1. some bounded ORIGINAL-coordinate carrier has five surviving square-energy modes after spending the high canonical-correlation directions; or
2. systematic failure produces many near-unit canonical correlations, and that high-dimensional overlap can be converted into one of the already-paid physical-pair, projected-crossing, grouped-bank, ridge, hub/common-plane, Schur, or Pluecker-volume exits.

The scalar overlap-energy corollary (5.1) may be a useful bridge: failure of a five-mode angle-spectrum certificate forces large trace overlap, which should be coupled to physical-coordinate leverage/volume rather than interpreted as post-rotation independence.

No counterexample to the full conjecture was found. Continuity is proved for the positive five-mode branch (4.4)-(4.5), not for the unrestricted conjecture.
