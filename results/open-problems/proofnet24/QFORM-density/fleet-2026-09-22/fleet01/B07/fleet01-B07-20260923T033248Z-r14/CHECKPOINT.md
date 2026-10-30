# fleet01/B07 r14 early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: supporting structural reduction proved below; full QFORM remains open. No continuity claim outside the explicitly Fourier-paid branch.

## Obligation attacked

Produce an actual physical-core or diffuse alternative from a determinant-weighted third-minor bank, without selecting or reciprocating one tiny physical minor.

Let `B=A[I,J]` be an original-coordinate cross block and

`P=E3(B)=sum_{|R|=|C|=3} det(B[R,C])^2>0`.

Normalize the squared-minor weights to a probability law and let `alpha_i` and `beta_j` be the row/column inclusion marginals, so `sum alpha=sum beta=3`.

## Step 1: apply the current fractional-volume theorem

Source actually used at an equation: `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, Theorem (10): if all row marginals are at most `q/2`, `1<=q<3/2`, then

`||p_Q||inf <= 3e/[(3-2q)sqrt(q)] P^(-1/6)`

with a continuous density, preserving arbitrary within-bank terms/outside couplings.

Take `q=4/3`. If `max_i alpha_i<=2/3`, or after transposing `max_j beta_j<=2/3`, then

`||p_Q||inf <= (9 sqrt(3)e/2) P^(-1/6)`.

Otherwise choose physical anchors `i,j` with `alpha_i>2/3`, `beta_j>2/3`. By the union bound under the joint determinant law, the packet mass containing both anchors satisfies

`M_ij >= (alpha_i+beta_j-1)P > P/3`.

## Step 2: a four-by-four physical-core versus residual-diffusion dichotomy

Condition the determinant law on the event that the row triple contains `i` and the column triple contains `j`. Its residual row and column inclusion marginals `rho_k,sigma_l` each sum to `2`.

Define

`R0={i} union {k:rho_k>1/2}`,
`C0={j} union {l:sigma_l>1/2}`.

Because each residual marginal family sums to two, `|R0|,|C0|<=4`. Put

`delta_R=sum_{k notin R0}rho_k`, `delta_C=sum_{l notin C0}sigma_l`.

If `delta_R+delta_C<1/2`, apply the designated partner fleet02/B07 theorem `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`, source `math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T023322Z-r11/REPORT.md`. Its exact union-bound identity gives

`E3(B[R0,C0]) >= (1-delta_R-delta_C) M_ij > P/6`.

Thus the concentrated survivor has a genuine physical `<=4 x <=4` cross core carrying a constant fraction of the entire third-compound mass.

If instead `delta_R+delta_C>=1/2`, then the only survivor is a genuine support-diffuse bi-anchor packet: it carries mass `>P/3`, every residual coordinate outside the at-most-three heavy residual coordinates on each side has conditional inclusion marginal at most `1/2`, and their two tail marginal sums total at least `1/2`.

This is the first substantive checkpoint; the N3 quantitative receiver and exact constants will be completed in REPORT.md.
