SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T10:53:21Z.
attacking: nonzero near-coloop interpolation; identify the exact Schur/Fresnel currency of a high-leverage physical row and splice it with the account02/B10 true-collar reduction.

# account01/B10 — exact coloop-defect Schur/Fresnel identity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: arbitrary exact-rank-three coupled case  
Status: `ESSENTIAL_STEP_APPLIED / NEW_EXACT_STRUCTURAL_IDENTITY / NEW_QUANTITATIVE_SUBBRANCH / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full QFORM target remains OPEN / NOT PROVED / NOT DISPROVED. This report treats the nonzero-pivot near-coloop interpolation only. No Gaussianity, moments, support restriction, log-concavity, connected support, spectral-coordinate independence, or law-uniform one-dimensional oscillatory decay is used. Continuity is stated only on the Fourier-integrable branch actually proved below.

## 1. Pinned sources actually used

Fresh owner control was resolved from `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The required newest-Claude source actually used is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

especially its twisted Hausdorff--Young/Brascamp--Lieb mixed-Fresnel mechanism. I also use the aligned-square implementation derived in account01/B16,

`yspennstate/math-open-problems@dd628c373863e2a0296617e74810343a93379813`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/B16-20260923T013905Z-qform-projection-product/CHECKPOINT.md`.

The designated partner actually applied is account02/B10,

`yspennstate/math-open-problems@16ecbcc3f6d34d4195ff6e29066216df155d9530`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T064541Z-account02-B10-QFORM-auto11/REPORT.md`.

That report imports the completed near-coloop mixed-row excision theorem and sharpens every still-unpaid true-collar state to

`1-eta < 2(1-rho_M)|alpha| <= 2|alpha|`,

with the majority one-sheet side already bounded by `pi sqrt(2)`. It also proves the product-safe collinear-bank compression inequality

`||p_Q||_infinity <= 2 C_3 (D w)^(-1/3)`,

`C_3=16 sqrt(30) 2^(1/4)`.

## 2. Near-coloop coordinates

Let

`A=R Lambda R^T`, `R^T R=I_3`,

with `Lambda` real symmetric invertible. Put

`D=|det Lambda|`.

Choose a physical row

`r_0=sqrt(c) e`, `||e||=1`, `0<c<1`,

and write

`rho=1-c`.

For every complementary row write

`r_j=s_j e+w_j`, `w_j perpendicular e`.

Parseval gives

`sum_j s_j^2=rho`,
`sum_j s_j w_j=0`,
`sum_j w_j w_j^T=I_2`.

Set

`alpha=e^T Lambda e`.

This report assumes `alpha!=0`; the exact physical null-pivot endpoint is already separately paid in the fleet. The physical hub pivot is

`a=A_00=c alpha`.

Let `R_L` be the matrix of complementary rows. Then

`G_L:=R_L^T R_L=I-c ee^T=rho ee^T+P_(e^perp)`.

## 3. New exact theorem — the Schur transverse fraction is exactly the coloop defect

Partition

`A=[[a,h^T],[h,B]]`,

so

`h=A_{L0}=sqrt(c) R_L Lambda e`.

Let

`S=B-hh^T/a`

be the scalar Schur complement.

### Theorem 3.1 — `QFORM-COLOOP-DEFECT-SCHUR-FRESNEL-IDENTITY-v1`

For the exact-rank-three representation above:

1. `S` has rank two and

   `range(S)=R_L(e^perp)`.

2. If `q=dist(h,range(S))`, then

   `boxed: q^2=c rho alpha^2.`

3. Consequently the aligned-square transverse fraction

   `eta_perp:=q^2/(a^2+q^2)`

   satisfies the exact orientation-free identity

   `boxed: eta_perp=rho=1-c.`

4. If `U` is any orthonormal basis matrix for `range(S)`, `W=[h,U]`, and `Gamma=W^T W`, then the normalized row leverage of complementary physical coordinate `j` is exactly

   `boxed: ell_j=s_j^2/rho+||w_j||^2.`

In particular, the apparent Schur singularity at `alpha->0` is not the geometric loss of the mixed-Fresnel route. Its only invariant loss is the physical coloop defect `rho`.

### Proof

Because

`B=R_L Lambda R_L^T`,

and

`hh^T/a
 =R_L [Lambda e e^T Lambda/alpha] R_L^T`,

we have

`S=R_L K R_L^T`,

where

`K=Lambda-Lambda e e^T Lambda/alpha`.

Now

`K e=Lambda e-Lambda e (e^T Lambda e)/alpha=0`.

Since `Lambda` is invertible and `alpha!=0`, the scalar Schur complement of `alpha` inside `Lambda` is invertible on `e^perp`, hence `K` has rank two. Because `K` is symmetric, its range is exactly `e^perp`. Thus

`range(S)=R_L(e^perp)`.

Write

`Lambda e=alpha e+b`, `b perpendicular e`.

Then

`h=sqrt(c) alpha R_L e+sqrt(c) R_L b`.

The second term lies in `range(S)`. Moreover for every `z perpendicular e`,

`<R_L e,R_L z>=e^T G_L z=0`,

while

`||R_L e||^2=e^T G_L e=rho`.

Therefore the perpendicular component of `h` relative to `range(S)` is exactly

`sqrt(c) alpha R_L e`,

and hence

`q^2=c alpha^2 rho`.

Since `a=c alpha`,

`eta_perp
 =c rho alpha^2/(c^2 alpha^2+c rho alpha^2)
 =rho/(c+rho)
 =rho`.

Finally, because `rho>0` and `alpha!=0`, the perpendicular component above is nonzero, so

`span(h,range(S))=range(R_L)`.

The normalized row leverage of `W=[h,U]` is therefore the diagonal of the orthogonal projector onto `range(R_L)`. For row `r_j=s_j e+w_j`,

`ell_j=r_j^T G_L^(-1) r_j
      =s_j^2/rho+||w_j||^2`,

which proves the final identity. QED.

## 4. Analytic payment under the exact normalized-complement diffuse gate

Choose `U` orthonormal with `range(U)=range(S)` and write

`S=U M U^T`

with `M` invertible symmetric `2 x 2`. Completing only the physical scalar pivot gives the exact identity

`Q=a (X_0+a^(-1)h^T X_L)^2+X_L^T U M U^T X_L`

(up to arbitrary affine/constant terms if outside original coordinates have first been conditioned).

The aligned-square mixed-Fresnel calculation applies to this expression before taking absolute values. Its core step is to Fresnel-linearize the two `U` squares and the aligned square, shift the aligned auxiliary variable by `2tX_0`, and then use the original product amplitudes in the leaf coordinates. Under

`max_j ell_j<=1/2`,

it gives an integrable characteristic-function majorant and

`||p_Q||_infinity
 <=12 [ |a|/(|det M| det Gamma) ]^(1/3).`                       (4.1)

For completeness, the exact-rank-three factorization also identifies the invariant in (4.1). Since `U` is orthonormal,

`det Gamma=q^2`.

Writing the completed-square factorization as

`A=a v v^T+Ubar M Ubar^T`,

with `v=(1,h/a)` and `Ubar=(0;U)`, the product of the three nonzero eigenvalues satisfies

`D=|det M| (a^2+q^2)/|a|`.

Therefore

`|det M| det Gamma/|a|
 =D q^2/(a^2+q^2)
 =D rho`.

Substituting into (4.1) proves the target-level branch

`boxed:
 max_j (s_j^2/rho+||w_j||^2)<=1/2
 ==> ||p_Q||_infinity<=12(D rho)^(-1/3)<=12 rho^(-1/3).
`                                                                    (4.2)

The characteristic function is `L^1` in this branch, so the density has a continuous version vanishing at infinity. This is stronger regularity than merely essential boundedness.

The important feature is that (4.2) is uniform as the nonzero physical pivot `alpha` crosses arbitrarily close to zero. No negative power of `|alpha|` remains.

## 5. A quantitative new true-collar reduction

In the live B10 predecessor collar one already has, for every complementary row,

`||w_j||^2<1/4`.

Hence failure of the diffuse gate in (4.2) has a concrete original-coordinate meaning:

`ell_j>1/2`

forces

`s_j^2/rho>1/4`,

or

`boxed: s_j^2>rho/4.`                                            (5.1)

Thus a near-coloop state no longer has an unstructured failure of the Schur/Fresnel route: either the whole normalized complement is diffuse and (4.2) pays it, or one ORIGINAL physical coordinate carries more than one quarter of all longitudinal leakage.

More generally, for every fixed `tau>0`,

`rho>=tau` and `max ell_j<=1/2`

imply

`||p_Q||_infinity<=12 tau^(-1/3)`.

Taking

`tau=1/512`

gives the convenient universal payment

`boxed: rho>=1/512, max ell_j<=1/2 ==> ||p_Q||_infinity<=96.`      (5.2)

Combining this with the designated-partner true-collar sharpening, any state still unpaid after the known exits and after (5.2) must satisfy simultaneously:

- `1-eta<2(1-rho_M)|alpha|<=2|alpha|` from account02/B10's current true-collar handoff;
- the minority/two-sheet side only, because the majority one-sheet side is already `<=pi sqrt(2)`;
- and either `rho<1/512`, or there is an original complementary row with `s_j^2>rho/4`.

This is the new frontier localization. It separates an **ultra-coloop defect** from a **single-original-row longitudinal concentration**. Neither alternative may be replaced by post-rotation independence.

## 6. Actual designated-partner application: the corrected true-collar stress family

Apply the account02/B10 target-valid stress family from its completed report. It has

`D=1`,
`c=127/128`,
`rho=1/128`,
`eta=1-1/(4m)`,

with even `m>=64`. For a mixed row,

`s_j^2/rho=(1/(256m))/(1/128)=1/(2m)`,

and

`||w_j||^2=eta/m<1/m`.

Thus

`ell_j<3/(2m)<=3/128<1/2`.

The pure-longitudinal rows have `ell=1/(2m)`, the pure-`v` rows have `ell=1/(4m^2)`, and the pure-`u` rows have `ell=1/m`. Hence the diffuse gate holds throughout the family. Equation (4.2) gives the new full-output estimate

`boxed:
 ||p_Q||_infinity<=12(1/128)^(-1/3)
                  =12*128^(1/3)
                  <60.477.
`                                                                    (6.1)

For comparison, applying the designated partner's own completed collinear-bank theorem to the same family gives, with

`w=c eta/2>=(127/128)(255/256)/2`,

`||p_Q||_infinity
 <=2 C_3 w^(-1/3)
 <263.642.`                                                         (6.2)

So the partner theorem is applied at an actual inequality, and the new Schur/coloop identity improves that particular payment by more than a factor four while removing any need to use the special collinearity of its positive-slope half-bank.

The partner family therefore cannot witness the genuinely unpaid interpolation even after collinearity is removed: what future stress tests must force is either the ultra-defect `rho->0` or the normalized-complement heavy-row alternative (5.1).

## 7. What is not proved and the next implication

Equation (4.2) still loses `rho^(-1/3)` as the physical row becomes an exact coloop. This loss is not caused by the scalar pivot `alpha`: Theorem 3.1 proves exactly that it is the coloop defect `rho=1-c`. The exact endpoint `rho=0` is separately paid by the fleet, so the remaining difficulty is a genuine interpolation discontinuity of this particular Fresnel parametrization.

The first unpaid implication is now

`QFORM-ULTRACOLOOP-OR-LONGITUDINAL-HEAVY-INTERPOLATION-v1`.

A successful next receiver should use the exact product provenance in the two alternatives above:

1. `rho<1/512` with the partner's extreme transverse-overlap condition `1-eta<2|alpha|`; or
2. an original row with `s_j^2>rho/4`, which can be conditioned/deleted without inventing a rotated independent coordinate.

One cannot simply treat the `sqrt(rho)` longitudinal projection as a small random perturbation: there are no support or moment bounds. Likewise, a bounded projected joint density cannot replace the original product source. The full arbitrary exact-rank-three theorem remains open, and hence the full three-large-eigenvalue conjecture remains open.
