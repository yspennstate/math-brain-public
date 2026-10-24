# Even/odd cross-bank closure of the diffuse trigonometric stress family

This addendum turns the structural obstruction in `REPORT.md` / `SIGNED_EXTENSION.md` into an explicit product-preserving analytic payment. The clean three-scalar core scale decays like `1/n`, but one physical **aggregate cross bank** has three singular values exactly `1/2`, so the completed cross-fiber Plancherel theorem yields a universal continuous density bound `6e`.

## 1. Setup

Let `n=2m` be even with `m>=3`. Use the trigonometric Parseval frame

`r_k=(1/sqrt(n), sqrt(2/n) cos(2pi k/n), sqrt(2/n) sin(2pi k/n))`,

`R=(r_k)_(k=0)^(n-1)`.

Let `Lambda` be any real orthogonal `3 x 3` matrix that is also symmetric; in particular either

`Lambda=I_3`

or

`Lambda=diag(1,1,-1)`.

Set

`A=R Lambda R^T`.                                               (1.1)

The nonzero eigenvalues of `A` are the eigenvalues of `Lambda`, so both displayed choices lie in the owner target.

Partition the ORIGINAL coordinates into

`I={0,2,4,...,2m-2}`, `J={1,3,5,...,2m-1}`.                   (1.2)

## 2. Exact half-frame identities

For `k=2j`, the angle is

`theta_(2j)=2pi j/m`.

Therefore the standard roots-of-unity identities on the `m` equally spaced angles give

`sum_(j=0)^(m-1) cos theta_(2j)=0`,
`sum sin theta_(2j)=0`,
`sum cos theta_(2j) sin theta_(2j)=0`,
`sum cos^2 theta_(2j)=sum sin^2 theta_(2j)=m/2`.               (2.1)

Substituting the column normalizations of `R` yields exactly

`R_I^T R_I=(1/2)I_3`.                                         (2.2)

The odd angles are the same regular `m`-gon rotated by `2pi/n`, hence identically

`R_J^T R_J=(1/2)I_3`.                                         (2.3)

Define

`U=sqrt(2) R_I`, `V=sqrt(2) R_J`.                              (2.4)

Then

`U^T U=V^T V=I_3`.                                            (2.5)

## 3. The physical cross block has exact singular spectrum `(1/2,1/2,1/2)`

The original-coordinate cross block is

`B=A[I,J]=R_I Lambda R_J^T=(1/2) U Lambda V^T`.                (3.1)

Because `U,V` have orthonormal columns and `Lambda` is orthogonal, `B` has rank exactly three and its three nonzero singular values are

`s_1(B)=s_2(B)=s_3(B)=1/2`.                                   (3.2)

Consequently

`D:=product_(nu=1)^3 s_nu(B)=1/8`,                            (3.3)

or equivalently

`pdet_+(BB^T)=D^2=1/64`.                                      (3.4)

This is the aggregate curvature that disappears if one insists on selecting one three-coordinate principal core first.

## 4. Direct application of completed cross-fiber Plancherel

Use account02/B07 `QFORM-CROSS-FIBER-PLANCHEREL-v1`, canonical source

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.

For any physical cross block of rank `r>=3` with nonzero singular values `s_nu`, that theorem retains arbitrary same-side self blocks and gives a **continuous `C_0` density** satisfying

`||p_Q||_infinity <= e r/(r-2) (product s_nu)^(-1/r).`         (4.1)

Apply (4.1) to (3.2)-(3.3), with `r=3`. Then for every independent original-coordinate input law with one-dimensional densities at most one,

`||p_(X^T A X)||_infinity
 <=3e (1/8)^(-1/3)
 =6e
 <16.31.`                                                       (4.2)

Thus

`boxed(||p_(X^T A X)||_infinity <=6e)`                         (4.3)

for every even `n>=6`, both for the positive projection `Lambda=I_3` and for the indefinite signature `(2,1)` form `Lambda=diag(1,1,-1)`. The density is continuous and vanishes at infinity.

No rotated spectral coordinates are declared independent: the theorem is applied to the original even/odd coordinate cut.

## 5. Coarea lesson

On the same family:

- every leakage-free scalar-sufficient bank is a singleton;
- every three-singleton density-normalized core has scale `O(1/n)` (`<=3/n` in the positive case and `<=9/n` in the signed case);
- but the even/odd physical cross block has **three singular values exactly `1/2`**, independent of `n`, and therefore pays the full form with constant `6e`.

So the precise missing factor in a scalar-core-first coarea reduction is not hidden spectral conditioning. It is the **aggregate original-coordinate cross curvature** carried by many individually small entries. A viable global coarea proof must preserve this bank before reciprocal inversion or scalar conditioning.

This addendum does not prove full QFORM; it closes only this explicit diffuse full-spark stress family by a source-valid existing theorem. Full continuity remains open globally, while continuity is proved here by the cross-fiber Fourier argument.
