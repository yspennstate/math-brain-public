# account01/B02 r31 early substantive checkpoint

Run `20260923T142315Z-account01-B02-qform-auto11-r31`.

Target remains the full QFORM-DENSITY-3EIG-20260922 conjecture. This checkpoint attacks the newest account02/B02 second-anchor collar, not a subclass claimed as the full theorem.

## Input actually used

Designated partner account02/B02 r12: `yspennstate/math-open-problems@9a5b5b7ee3ec28d8f2fb9eaced2254ac050b5104`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T133727Z-account02-B02-QFORM-r12/REPORT.md`.

On its transport-failure branch it produces an ORIGINAL-coordinate invertible `2 x 2` cross anchor `P` with algebraic cross-Schur residual `S` and

`G := |det P|^2 ||S||_F^2 > Z/24`,

where `Z=E3(B)` is the parent physical cross-block third volume. No independence after the Schur shear is asserted.

I also use the completed exact-rank-three physical-cross-block Fourier theorem from `yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T230126Z-account03-B02-QFORM-r17/REPORT.md`: for an ORIGINAL-coordinate exact-rank-three cross block `C`, with `E3(C)=Gamma^2`,

`int_R |phi_Q(t)| dt <= 12 pi E3(C)^(-1/6)`,
`||p_Q||_infty <= 6 E3(C)^(-1/6)`.

## New calculation: one-sided Schur energy concentration gives an exact-rank-three slice

Write `D=|det P|`, `F=||S||_F^2`, and normalized row/column Schur energies

`a_i=||S_i:||_2^2/F`, `b_j=||S_:j||_2^2/F`,
`h_r=max_i a_i`, `h_c=max_j b_j`.

For a residual physical column `j`, keep **all** source-bank rows but only the two physical pivot columns together with `j`; call this literal physical cross block `C_j`. It has exactly three columns. Every anchored `3 x 3` minor obtained from the two pivot rows and one residual row `i` satisfies the exact block determinant identity

`det C_j[{pivot rows}+i,:] = det(P) S_ij`.

Therefore Cauchy--Binet gives

`E3(C_j)=det(C_j^T C_j) >= D^2 sum_i |S_ij|^2 = b_j G`.

If `b_j>0`, `C_j` has rank exactly three. The exact-rank-three theorem then yields

`int |phi_Q| <= 12 pi (b_j G)^(-1/6)`,
`||p_Q||inf <= 6 (b_j G)^(-1/6)`.

Taking a maximum-energy column, or transposing and taking a maximum-energy row, proves the preliminary receiver

`int |phi_Q| <= 12 pi [max(h_r,h_c) G]^(-1/6)`,
`||p_Q||inf <= 6 [max(h_r,h_c) G]^(-1/6)`.

Applied to the partner inequality `G>Z/24`, any `max(h_r,h_c)>=1/4` is already a uniform-scale L1 branch:

`int |phi_Q| < 12 pi 96^(1/6) Z^(-1/6) < 80.670 Z^(-1/6)`,
`||p_Q||inf < 6 96^(1/6) Z^(-1/6) < 12.839 Z^(-1/6)`.

This uses an exact rank-three physical **three-column or three-row slice**, not a single `3 x 3` minor and not a reciprocal tiny local minor.

## The surviving branch has a strong disjoint-extension resource

If the preceding branch fails at threshold `1/4`, then both `h_r,h_c<1/4`. Normalize Schur-entry energy

`w_ij=|S_ij|^2/F`.

For two iid samples `(I1,J1),(I2,J2)` from `w`, the probability that both residual rows and residual columns are distinct is exactly

`delta_2 = 1 - sum_i a_i^2 - sum_j b_j^2 + sum_ij w_ij^2`.

Since `sum_i a_i^2<=h_r` and `sum_j b_j^2<=h_c`,

`delta_2 >= 1-h_r-h_c > 1/2`.

Thus failure of the one-sided slice compiler forces a genuinely double-diffuse anchored-extension packet with more than one-half two-sample row-and-column disjointness.

Important boundary: this does **not** imply a nontrivial anchored `4 x 4` determinant. If `S=uv^T` is rank one with `|u_i|=|v_j|=m^(-1/2)` on `m>=5` coordinates, then `h_r=h_c=1/m<1/4` and `delta_2=(1-1/m)^2>1/2`, while `E2(S)=0` identically. This is an exact algebraic counterexample to the intermediate shortcut “many disjoint extension pairs force fourth volume.” The partner's exact-rank-one grouped Fourier endpoint already pays that endpoint; the next receiver must be rank-one-compatible and robust to a nonzero transverse tail.

Provisional unpaid implication: `QFORM-SECONDANCHOR-DOUBLEDIFFUSE-NONZERO-TRANSVERSE-v1`.
