SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T05:21:44Z.
attacking: extend the self-matched mixed-minor Fourier branch from the 1/2 occupancy threshold to a Jensen-tunable threshold below 5/8, then sharpen the nested-packet router without selecting a physical row/minor.

# B08 r28 handoff

**Canonical mathematics:** `yspennstate/math-open-problems@af8d585f3ac8b3cc243045caf6bbe65d8e956f99`  
**Path:** `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T052144Z-account03-B08-qform-diffuse-r28/REPORT.md`  
**Checks:** `CHECKS.py`, `CHECKS.txt`; output `QFORM_B08_R28_CHECK_PASS`.  
**Status:** complete supporting analytic theorem + sharper diffuse router; full QFORM remains OPEN. `WITHOUT_VERIFIED_BRAIN`.

## New theorem

`QFORM-MIXED-ORDER-JENSEN-COMPILER-v1`: for a probability law `Omega` on nonzero physical square minors of varying orders, let row/column inclusion marginals be `alpha_i,beta_j`, mean order `kbar`, and

`K(Omega)=exp(E log det(M_ST)^2+H(Omega))`.

For `q>=1`, if every row marginal satisfies `alpha_i<=q/2` and `kbar>2q`, then the full ambient quadratic form, with arbitrary same-bank quadratic terms/outside couplings/affine terms, has a continuous `C0` density and

`||p_Q||inf <= [kbar/(kbar-2q)] [B_beta prod_i H_q(alpha_i)]^(1/kbar) K(Omega)^(-1/(2kbar))`

and hence the coarse bound

`||p_Q||inf <= e q^(-1/2)[kbar/(kbar-2q)] K(Omega)^(-1/(2kbar))`.

The proof combines account01/B01's varying-order determinant/BL entropy law with account02/B02's Jensen + sharp Hausdorff--Young calculation. No individual minor is selected.

## B08 anchored packet consequence

For the r27 self-matched law `Omega=(w3+v2*)/2`,

`kbar=5/2`, `K(Omega)>=2Z/R_i`,

anchor-row marginal `1/2`, and each residual-row marginal is the anchored third-volume marginal `alpha_k`. Put `h=max alpha_k`.

Every `h<5/8` is now paid continuously. With `q=max(1,2h)`,

`||p_Q||inf <= [5e/(sqrt(q)(5-4q))](2Z/R_i)^(-1/5)`.

In the current diffuse q=0 branch, `Z>L^6/6912` and `R_i<=L` imply:

- if `h<=1/2`, `||p_Q||inf<70/L` (improves r27's `<85/L`);
- if `h<=3/5`, `||p_Q||inf<317/L`;
- therefore failure of the second bound forces a nested residual-row packet `>3Z/5>L^6/11520`.

The transpose gives the same statement on the column side. Thus after the existing `<77/L` exit, each non-large-star side is either continuously paid by `<317/L` or carries nested third-volume `>L^6/11520`. The `5/8` boundary is the exact integrability threshold of this particular order-3/order-2 half-mixture.

## Correction and partner use

The fresh `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1` correction is respected: r28 never extracts one large physical row/minor from aggregate mass. The failure output is only a nested aggregate event.

No completed current-QFORM artifact was found for designated `account04/B08`; none is fabricated. The compatible completed account04/B18 theorem at `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061` gives `||p_(u^T X)||inf<=sqrt(2)/||u||2`. Applied to the r28 large-star alternative, `R_i>L` gives `||p_(r_i^T X_J)||inf<sqrt(2)/L`; simultaneous opposite-side large stars on disjoint original-coordinate banks give joint cap `<2/L^2`. This remains linear product currency, not a generic quadratic pushforward bound.

## Remaining implication

Consume the `>L^6/11520` three-anchor nested packet at bank level, preferably via the exact co-heavy identity plus the aggregate `e2` Fourier/square-lift theorem when a nonzero physical pivot exists, and a zero-pivot pair/ridge/grouped-bank receiver otherwise. Full bounded-density and global-continuity conclusions remain OPEN.
