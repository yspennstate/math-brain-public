# Addendum — newest partner r49 consumed

After the main report was written, the fresh partner-directory read exposed a newer compatible fleet03/B06 handoff than r48:

`yspennstate/math-open-problems@ac4d8963e32785d2191e535b0268fe451262a903`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T012256Z-fleet03-B06-qform-r49/REPORT.md`,
with theorem `QFORM-RANK1T-TWOPIVOT-AGGREGATE-v1`.

This addendum applies the present run's theorem to r49's actual newest debt.

## 1. r49 endpoint

r49 starts from the same exact shear-flat singular coefficient

`S=C-E^T H^(-1)E=D+lambda(E^T v)(E^T v)^T`,

and obtains a density bound when the determinant-squared pair law is disjoint enough and

`Xi_H(v)=sum_(s:H_ss!=0)|H_ss| |(Hv)_s|^2 >0`.

It leaves two literal endpoint types:

1. low environment pair-law disjointness, forcing a leverage hub `>3/5`;
2. `Xi_H(v)=0`, which r49 proves is exactly a zero-diagonal/tangency face. If exactly one diagonal of `H` is nonzero, the other is zero and `det H=-c^2<0`; if both diagonals vanish, `H=[[0,c],[c,0]]` and again `det H=-c^2<0`. Hence every `Xi_H(v)=0` endpoint has an invertible indefinite physical pair `H`.

## 2. Present theorem bypasses Xi and Omega analytically

Theorem `QFORM-DIAG-RANK1-SQRT-SMALLBALL-v1` from the main report applies to the entire r49 Schur residual before any environment pair-law split. Put

`L=||S||op`.

Then

`sup_t P(|Y^T S Y+ell^T Y+c-t|<rho)
 <= H_* L^(-1/2) sqrt(rho),`

`H_*=10.443428396672811... .`

Because the ambient QFORM target has at least three eigenvalues of modulus at least one and `H` is an invertible physical `2 x 2` block, the pinned Schur-complement spectral lemma gives `L>=1`.

Therefore on every r49 zero-diagonal/tangency face, the completed physical-indefinite-pair logarithmic theorem gives

`boxed:
 ||p_Q||infinity
 <=18.280856344644523
   (|det H| sigma_min(H) L)^(-1/4)
 <=18.281 (|det H| sigma_min(H))^(-1/4).`

This statement has no `Xi_H(v)`, no `Omega`, no environment leverage gate, and no `D_hh` pivot. It retains all shared-coordinate diagonal curvature `D` and the complete rank-one Schur term. Thus the r49 analytic zero-diagonal/tangency obstruction is paid whenever the physical-pair currency is quantitative.

In the pure zero-diagonal case

`H=[[0,c],[c,0]]`,

one has `|det H| sigma_min(H)=|c|^3`, so explicitly

`boxed: ||p_Q||infinity <=18.281 |c|^(-3/4).`

For the one-zero-diagonal tangent case `H=[[a,c],[c,0]]`, the same bound holds with the exact pair currency `c^2 sigma_min(H)`.

## 3. Sharpened live debt

The newest r49 debt can therefore be narrowed. `Xi_H(v)=0` and low pair-law disjointness are not independent analytic singularities once the exact residual is recognized as diagonal plus rank one. The remaining target-level problem is structural and can be stated as

`QFORM-R49-SMALL-PAIR-CURRENCY-TO-SHEAR-EXIT-v1`:

In the complete r49 singular-`T` packet, if `|det H| sigma_min(H)` is too small for the preceding pair bound to be universal, use the intact two-row shear block `E`, r49's pair-area/leverage information, and the target's third large spectral resource to force a product-preserving paid exit, without dropping `D`, the rank-one term, or any nonzero tail.

This is strictly narrower than r49's `ZERODIAG-TANGENCY-OR-HEAVYHUB` debt: the tangency itself has disappeared from the analytic side. The obstruction is now only the possible degeneration of the physical pair currency relative to the direct shear/crossing currencies.

A simple model explains why no lower bound on the pair currency alone can finish the theorem: matrices with a vanishing physical `2 x 2` hub block but a fixed rank-two hub-to-environment crossing can keep order-one spectrum. Hence the next step must be a compiler from small pair currency to the intact shear block rather than another attempt to improve the pair kernel.

Full QFORM remains OPEN; continuity remains separate.
