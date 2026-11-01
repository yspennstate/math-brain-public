# B03 QFORM r18 supplement — exact independent-copy collision potential

Pre-publication reconciliation found a fresh completed same-assignment theorem from `fleet01/B03`:

`yspennstate/math-open-problems@3d6fefe9c92674dff38c97ef8a502787ec3426a2`,  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/fleet01-B03-20260922T144815Z/REPORT.md`.

That theorem proves, for any quadratic form on independent cap-one original coordinates and any physical cross block `B` of rank `r>=1` with positive singular-value product `Delta_r`, the dependence-safe independent-copy estimate

`|phi_R(t)|^2 <= min(1,(2 pi)^r Delta_r^(-1)|t|^(-r)).`                    (S.1)

Its proof uses `|phi|^2=E exp(it(R-R'))` and keeps each `(X_i+X_i',X_i-X_i')` pair coupled; it does not invoke the refuted conditional-cap shortcut.

## S.1 New explicit collision corollary

Let `R'` be an independent copy of `R`. Then

`E |R-R'|^(-1/2) <= [8r/(2r-1)] Delta_r^(-1/(2r)).`                       (S.2)

Proof. The Fourier transform of `|x|^(-1/2)` is `sqrt(2 pi)|t|^(-1/2)`. Gaussian regularization therefore gives

`E |R-R'|^(-1/2)`
` = (1/sqrt(2 pi)) int_R |t|^(-1/2)|phi_R(t)|^2 dt`,                       (S.3)

once the right side is finite; (S.1) supplies that finiteness. Set

`t0=2 pi Delta_r^(-1/r)`.

Splitting at `t0`,

`int_R |t|^(-1/2)|phi_R(t)|^2 dt`
` <= 2[ int_0^t0 t^(-1/2)dt`
`       +(2 pi)^r Delta_r^(-1) int_t0^infinity t^(-r-1/2)dt ]`
` = [8r/(2r-1)] sqrt(2 pi) Delta_r^(-1/(2r)).`

Divide by `sqrt(2 pi)` to obtain (S.2). For `r=1` this is the finite endpoint

`E|R-R'|^(-1/2) <= 8 sigma_1^(-1/2)`,                                      (S.4)

although rank-one hyperbolic output density may have a logarithmic singularity.

This is the exact independent-copy quantity requested by the B03 assignment. It is a collision estimate, not yet a translation-uniform estimate.

## S.2 Why the main r18 theorem is an additional step

A square-pivot density transducer needs

`sup_s E|R-s|^(-1/2)`,                                                      (S.5)

not merely the centered collision quantity in (S.2). The main r18 theorem supplies this stronger translation-uniform estimate when one side of the residual bank is isotropic in original coordinates:

`R=2U^TTV+b(W)^TU+c(V,W)`

implies

`sup_s E|R-s|^(-1/2) <= C_r Delta_r^(-1/(2r))`,

`C_r=[4r/(2r-1)]sqrt(e) v_r^(1/(2r)).`                                     (S.6)

Thus the combined picture is:

1. arbitrary physical cross bank: dependence-safe independent-copy collision potential (S.2);
2. isotropic-side cross bank: translation-uniform half-Riesz potential (S.6);
3. one additional independent physical square pivot: linear small-ball / essential-density bound

`||p_Q||_infinity <= C_r |a|^(-1/2) Delta_r^(-1/(2r)).`                    (S.7)

This avoids the false step of upgrading collision control to a translation supremum without extra structure.

## S.3 Fresh peer reconciliation

A still newer `fleet01/B03` handoff at `20260922T185132Z-r14` proves a square-collision Riesz estimate and explicitly confirms that its earlier whole-bank endpoint survives the current fragmentation correction. This independently supports the conclusion that the previous `k=2` logarithmic threshold was a limitation of the regularized-determinant splice, not a genuine low-rank collision obstruction.

The designated partner `fleet04/B03` still had no completed current-QFORM handoff at the pre-publication scan, so no result from that slot is claimed.

Full QFORM remains OPEN. Continuity is not established by (S.6)-(S.7).
