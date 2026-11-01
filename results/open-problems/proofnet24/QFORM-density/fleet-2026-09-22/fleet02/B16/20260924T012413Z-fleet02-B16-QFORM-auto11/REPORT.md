SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-24T01:24:13Z.
attacking: the punctured majority-sign near-coloop by deriving the exact physical-hub discriminant sign dichotomy, then testing precisely what a bounded two-dimensional product marginal can and cannot control.

# fleet02/B16 — discriminant sign dichotomy and fixed-determinant hyperbolic trace barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** projection-product interaction / complementary source-valid constructions  
**Status:** `NEW SUPPORTING DICHOTOMY + FIXED-DETERMINANT INTERFACE OBSTRUCTION + LATEST PARTNER APPLIED / FULL QFORM OPEN`  
**Regularity:** the unrestricted continuity problem remains separate and open.

## 1. Source boundary and first unpaid implication


Required pinned source consumed at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed two-dimensional product-projection density bound and the ruled one-sheet theorem are applied below at actual equations. No arbitrary-joint rank-three coarea, conditional projection-height cap, or independence after rotation is used.

Latest compatible designated partner consumed: fleet03/B16 r38, report commit

`453ee59466af7ec139622f7e7bc335b2feff1e71`,

with the strengthened deterministic checker through

`2a89ffaf38323c264edcd994d61684fb90cf312f`.

The first unpaid implication is now:

**`QFORM-PUNCTURED-MAJORITY-HUB-TTSTAR-v1`.** In the exact-rank-three near-coloop chamber, when the nonzero physical hub pivot has the majority spectral sign, the literal-hub discriminant is necessarily indefinite. A successful punctured-to-zero bridge must therefore retain original-product source information or Fourier/TT* cancellation through the hyperbolic trace; replacing the remaining pair merely by a bounded joint density cannot work, even at fixed nonzero determinant.

## 2. Literal physical hub and exact discriminant identity

Let `H` be one untouched original coordinate with density `f_H<=1`. Let `Z=(U,V)` be any random pair, independent of `H`, with joint density `rho`; no independence between `U` and `V` is assumed. Consider the affine quadratic

`Q = a H^2 + 2 H u^T Z + Z^T C Z + r H + s^T Z + c`,

where `a!=0`, `u in R^2`, and `C=C^T`. Put

`B = [[a,u^T],[u,C]]`.

For fixed `z`, write

`D_q(z)=(u^T z+r/2)^2-a(z^T C z+s^Tz+c-q)`.

Every real root of `Q(H,z)=q` has derivative magnitude `2 sqrt(D_q(z))`. Since `f_H<=1`, the total contribution of the at-most-two roots is at most `D_q(z)^(-1/2)`. Therefore

`p_Q(q) <= integral rho(z) [D_q(z)]_+^(-1/2) dz`.                 (2.1)

The quadratic matrix of `D_q` is

`K = u u^T-aC`.                                                   (2.2)

The determinant is exact:

`det K = a det B`.                                                (2.3)

Indeed, for `a!=0`, Schur complementation gives

`det B = a det(C-u u^T/a)`,

while in dimension two

`det(u u^T-aC)=a^2 det(C-u u^T/a)=a det B`.

Thus the sign of `a det B` is exactly the elliptic/hyperbolic sign of the two-dimensional physical-hub discriminant.

## 3. The safe branch: definite discriminant uses only the joint pair density

Assume

`a det B>0`,                                                      (3.1)

so `K` is definite. Complete the square in `D_q`. For every `tau>0`, regardless of the affine translation and target `q`,

`Leb{z:0<D_q(z)<tau^(-2)} <= pi tau^(-2)/sqrt(a det B)`.           (3.2)

This is just the area difference of two nested ellipses; it is valid for either positive- or negative-definite `K`.

If `||rho||_infinity<=M`, layer cake in (2.1) gives

`p_Q(q)`
`<= integral_0^infinity min(1, pi M tau^(-2)/sqrt(a det B)) d tau`
`= 2 sqrt(pi M) (a det B)^(-1/4)`.                                (3.3)

Hence

**`QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1`**

`||p_Q||_infinity <= 2 sqrt(pi M) (a det B)^(-1/4)`                (3.4)

whenever `a det B>0`.

Now apply the completed pinned two-dimensional product-projection theorem. If `Z` is an orthonormal two-dimensional projection of a disjoint original-coordinate product source, then legitimately

`||rho||_infinity<=2`,                                            (3.5)

with no claim that `U,V` are independent. Therefore

`boxed: ||p_Q||_infinity <= 2 sqrt(2 pi) (a det B)^(-1/4).`        (3.6)

This is a real curved use of the joint projected density. For a carrier of signature `(+,+,-)`, `det B<0`, so (3.1) means the physical hub diagonal `a` has the minority negative sign. For `(+,-,-)`, it means the hub has the minority positive sign. Thus the minority-sign nonzero physical pivot is the elliptic discriminant branch.

## 4. New fixed-determinant obstruction on the majority-sign branch

When

`a det B<0`,                                                      (4.1)

`K` is indefinite. The failure of a cap-only argument is not merely a degenerating-determinant effect.

Take the fixed matrix

`K=diag(1,-1)`, so `|det K|=1`. For `R>1`, introduce

`r=u-v`, `t=u+v`,

so

`u^2-v^2=rt`, `du dv=(1/2)dr dt`.

Let

`Omega_R={1<=r<=R, 0<t<=2/(r log R)}`

and let `rho_R` be the indicator of its image in `(u,v)`-space. Its total mass is exactly

`(1/2) integral_1^R [2/(r log R)] dr=1`,                           (4.2)

so `rho_R` is a probability density with

`||rho_R||_infinity=1`.                                          (4.3)

Nevertheless,

`integral (u^2-v^2)_+^(-1/2) rho_R(u,v) du dv`
`= (1/2) integral_1^R r^(-1/2)`
`    integral_0^{2/(r log R)} t^(-1/2) dt dr`
`= sqrt(2/log R) integral_1^R dr/r`
`= sqrt(2 log R) -> infinity`.                                   (4.4)

Therefore:

**`QFORM-INDEFINITE-DISCRIMINANT-CAP-BARRIER-v1`.** There is no finite bound for

`integral [z^T K z+s]_+^(-1/2) rho(z) dz`

depending only on a planar probability-density cap `||rho||_infinity` and `|det K|` when `K` is indefinite. This failure already occurs with cap one and determinant magnitude one.

This is an **interface obstruction, not a QFORM counterexample**: `rho_R` is not asserted to be an orthogonal projection of a product measure. Its role is exact: it proves that the majority-sign hub branch cannot close after product provenance is discarded down to a generic two-dimensional density cap.

## 5. Latest fleet03/B16 r38 inserted at the exact discriminant

The latest designated partner makes the preceding interface failure source-authentic in the actual punctured near-coloop family. It takes

`c=127/128`, `N=128`,

with one literal cap-one hub and three disjoint original-coordinate uniform banks, and defines

`Y=sqrt(c)X_0+S`,

`Q_a=aY^2+4YU+V^2`,                                                (5.1)

for `0<a<2^-14`. Its carrier is

`Lambda_a=[[a,2,0],[2,0,0],[0,0,1]]`,

with

`det Lambda_a=-4`                                                 (5.2)

and three eigenvalues of modulus at least one. The pair `(U,V)` is an authentic orthonormal product projection, so the pinned theorem gives

`||p_(U,V)||_infinity<=2`.                                        (5.3)

Treating the literal physical hub exactly as in Section 2, all dependence on the shared longitudinal variable `S` cancels from the discriminant. At target zero the quadratic part is

`K_a=diag(4,-a)`,                                                  (5.4)

and indeed

`det K_a=-4a=a det Lambda_a<0`.                                   (5.5)

So the latest partner lives **exactly** in the majority-sign/hyperbolic side of the sign dichotomy, not in the elliptic branch (3.6).

Its source-valid lower bound for the hub-first positive trace is

`T_a(0)=c^(-1/2) E[(4U^2-aV^2)_+^(-1/2)]`

`>= c^(-1/2)(m^2 eta/4) log(1/(2 sqrt(a))) -> infinity`,           (5.6)

for fixed `m,eta>0` independent of `a`. Thus even an authentic product projection with the genuine cap (5.3) does not permit a uniform punctured-to-zero passage after replacing the hub root densities by their supremum.

This is precisely the partner application required by the B16 role: (2.3) identifies why r38 is the hyperbolic sign branch, and (4.4) shows the obstacle is intrinsic to arbitrary-joint cap reduction rather than merely to the particular normalized-sum law.

## 6. Pinned ruled theorem shows the trace divergence is proof loss, not density blow-up

The same r38 family has exact rank three and signature `(+,+,-)`, with all three nonzero eigenvalue magnitudes at least one. The completed ruled one-sheet theorem in the required pinned `COUNTEREXAMPLE_SEARCH.md` therefore applies directly and gives

`boxed: p_(Q_a)(s) <= pi sqrt(2) = 4.442882938158...`              (6.1)

on the one-sheet side `s>=0` (in the theorem's a.e./density-representative sense), uniformly in `a`.

Compare (6.1) with (5.6): the true one-sheet density stays uniformly bounded while the positive scalar-root half-trace used by the hub-first cap argument diverges logarithmically. Hence the r38 divergence is rigorously a **loss of cancellation/source information in the proof interface**, not evidence for a QFORM counterexample.

This also supplies the requested direct use of a completed result from the pinned `e5f71d79...` package at a real inequality.

## 7. Consequence for the live punctured endpoint

The exact-rank-three physical-hub chamber now separates cleanly:

- **minority-sign nonzero hub:** `a det Lambda>0`; the discriminant is definite and a legitimate two-dimensional projected density cap pays the branch by (3.6);
- **majority-sign nonzero hub:** `a det Lambda<0`; the discriminant is hyperbolic. A generic joint pair cap cannot control its half-trace even at fixed determinant by (4.4), and fleet03/B16 r38 shows the actual near-coloop hub-first trace already diverges logarithmically on a strict source-valid target family as the pivot tends to zero.

The surviving implication is therefore not “improve the two-dimensional projection constant.” It is:

**`QFORM-PUNCTURED-MAJORITY-HUB-TTSTAR-v1`:** retain the same original leaf sources through the nonzero hub chirp and the hyperbolic discriminant, or use a frequency-side Hilbert/TT* pairing before taking absolute values, in a way uniform as the majority-sign pivot tends to zero.

The preceding fleet02/B16 phase-weighted punctured theorem already shows that arbitrary same-bank quadratic phases can be retained on the Fourier side; its remaining coefficient loss is nonperturbative. The present sign dichotomy says exactly why a fallback to a positive two-dimensional curved trace cannot supply the missing zero-coupling bridge.

Arbitrary additional spectrum is still a separate full-target interface. Nothing here proves or disproves the unrestricted conjecture.
