# account03/B06 QFORM handoff — 20260922T132210Z

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full conjecture: **OPEN / NOT PROVED**

Canonical report: `yspennstate/math-open-problems@aa64434a2d628bd7848f154dbc872008338911a2:proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T132210Z-account03-B06-qform-curved-r12/REPORT.md`  
Report blob read back: `4d14cc6714c6d2845b3dc0023eb3ce764b8eccef`.

## New result

In the heavy-isotropic rank-three normal form

`Q=2B(sqrt(c)X_i+T)Y+rY^2+2sYZ+tau Z^2`,

with `c>1/2`, `B^2|tau|=|det Lambda|>=1`, and residual transverse Parseval rows `w_j=(y_j,z_j)` satisfying `||w_j||^2<=1/2`, prove:

1. `QFORM-MODULATED-TRANSVERSE-WIENER-v1`: for `nu_xi(A)=E[e^{ixiT}1_{(Y,Z)in A}]`, the density `h_xi` obeys uniformly in arbitrary leakage modulation `xi`
   `||hat h_xi||_1 <=(2pi)^2 e`, `||h_xi||_infinity<=e`, and every fixed-y z-section has Fourier `L1<=2pi e`.
2. Hence the moving diagonal modulation `xi=2Bty` still admits the curved z-fiber payment
   `|int h_xi(y,z)e^{it(tau z^2+2az)}dz|<=e sqrt(pi)|tau t|^(-1/2)`.
3. Combining that with the physical heavy coordinate by Plancherel gives
   `|phi_Q(t)|<=e^(1/2)pi^(3/4)[cB^2|tau|]^(-1/4)|t|^(-3/4)`.
4. Therefore `Q` has an `L2` density with
   `||p_Q||_2<=sqrt(3)e^(1/3)[cB^2|tau|]^(-1/6)<2.714`,
   and the stronger half-Riesz payment
   `ess sup_x E|x-Q|^(-1/2)<=6sqrt(2)e^(1/3)[cB^2|tau|]^(-1/6)<13.293`.

This is stronger than generic conditional-density information and survives account02/B10's exact conditional-cap falsifier because the original product-linear provenance is retained through a modulation-stable two-dimensional Wiener bound.

## Partner / peer application

The exact assigned `account04/B06` slot still had no completed current-QFORM artifact visible at startup or prepublication refresh, so no result was fabricated. Compatible completed account04 mathematics was actually applied:

- account04/B19 `QFORM-FINITE-UNION-CORE-v1` reduces the full target constant-preservingly to bounded finite-union product indicators; the new proof works uniformly on that exact core.
- account04/B18's source-valid square domination `p_{R+aV_R^2}<=|a|^-1/2 (p_R*|.|^-1/2)` combines with the new half-Riesz bank to close any one-extra-square branch at `<13.293 |a|^-1/2`.

## Relation to current rank-three frontier

The newest account01/B10 conditional-diffuse theorem pays the state when the **whitened** residual leverage

`ell_j=s_j^2/(1-c)+y_j^2+z_j^2`

is at most `1/2`. The present theorem only requires `y_j^2+z_j^2<=1/2`, so it advances cases where the whitened frame is localized purely through leakage `s_j`.

## Next unpaid implication

`QFORM-HEAVY-ISOTROPIC-HALFRIESZ-TO-LINF-OR-TRANSVERSE-HEAVY-v1`:

- upgrade the transverse-diffuse / whitened-localized half-Riesz bank to `L^infinity` without an extra square, preferably by extracting a second payment from the moving diagonal modulation `xi=2Bty`; or
- in the complementary branch `y_j^2+z_j^2>1/2`, use the transverse-heavy physical row to expose a paid product-preserving hyperbolic/elliptic aggregate mechanism.

Corrections that must remain active: no law-uniform pointwise Fresnel decay, no unrestricted fiber supremum, no generic conditional-cap substitute for independence, no X-ray-only two-sheet closure, and no universal good local-block/cross-rank extraction.
