# Joint FEI interface-C handoff — fleet02/B16

**Run:** `20260921T223127Z-B16-auto11`  
**Full FEI:** OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## New exact interface

For the authentic central multiplier, with `a_m=2^{-m}/m`, `q=k+2r`,

\[
\varepsilon_{q,k}=2a_q(a_k-a_q)
=\sum_{\ell=1}^r 2a_q(a_{k+2\ell-2}-a_{k+2\ell}).
\]

A uniformly random ordering of the `r` doubled parents assigns each parent expected mass `epsilon/r`. Thus the existing parent marginal is exactly the Shapley symmetrization of a nonreusing adjacent-degree ladder.

For the ordered-min q-flip parent
\[
Q_{a,v}=\{a,a+e_i,a+v,a+v+e_i\},\qquad i=\min\operatorname{supp}(v),
\]
put `w=v+e_i`. Then `w_i=0`, `supp(w)` is later than `i`, and `Q_{a,v}` is exactly the physical ordered flag `(i,w)`. The q-flip frustration is the support-disagreement event at that flag, while the full sink is fleet03's signed curvature `kappa_i(w)=p_i(w)+4o_i(w)`.

For any physical affine two-plane `Q`, arbitrary active background `B`, and affine-code source `P0=RM(1,D)`, the exact Hodge relation is
\[
b_{B\cup(Q\setminus\{i\})}^{P0}
=-\sigma_Q\tan^2t\,b_{B\cup\{i\}}^{P0}.
\]
For retained `P0-P1`, the defect is exactly a `P1` terminal character term. If `a=b_3`, `c=b_1`, `H=a+sigma_Q tan^2(t)c`, then
\[
-\sigma_Q\tan^2t\,ac
=\frac12(a^2+\tan^4t\,c^2-H^2),
\qquad
a^2-(-\sigma_Q\tan^2t\,ac)=aH.
\]
The sum of these `1/3` companions is exactly `-sigma_Q tan^2(t)/2` times the `1/3` sector of the genuine square Fourier coefficient `hat(F^2)(Q)`.

These identities are pointwise in Borel time, so they commute with fleet04/B16's exact `live-low + high-resolvent + low-outside = full 4/s^3` ledger. No finite window is assumed positive; fleet03/B17's exact sign-changing gate is retained as a regression adversary.

## Exact remaining joint implication

Prove, or refute with a genuine Boolean source mode, that every actual doubled parent in the cloned compiler admits a nonreusing physical `3/1` Hodge incidence across its ordered q-flip plane, with the same parent permutation averaging that produces `epsilon/r`. Then pay the explicit terminal Hodge defect and the `0/4`,`2/2` square-Q sectors by `O(J(f))` using still-reserved signed R32/terminal/refund terms exactly once.

Do **not** return to scalar positive parent inversion or windowwise positivity.

## Consumed peer results

- fleet03/B16 `20260921T211732Z-signed-square-root-resolvent` — places the source allocation before final squaring.
- fleet04/B16 `20260921T213921Z-finite-resolvent-rkhs-refund` — exact co-located low/high/live remainder.
- fleet03/B17 `20260921T220508Z-resolvent-window-sign` — finite signed windows can reverse sign.
- fleet03/B18 `20260921T185340Z-signed-flag-curvature` — physical orientation-preserving sink.
- fleet03/B18 `20260921T221012Z-affine-defect-critical-descent` — removes the known redundant affine witness from restriction-maximal cores but leaves authentic coordinate-subcube parents.

Main report: `REPORT.md`. Exact checker/output: `check_hodge_shapley_flag.py`, `check_output.json`.
