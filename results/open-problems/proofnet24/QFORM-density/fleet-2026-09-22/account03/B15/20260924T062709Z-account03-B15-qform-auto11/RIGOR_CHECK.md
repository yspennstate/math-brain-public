# Rigor check — localized physical-triple theorem

Run: `20260924T062709Z-account03-B15-qform-auto11`.

This file checks only the new algebraic synthesis in the companion `REPORT.md`. It does not independently re-prove the two source-pinned supporting analytic theorems.

## Check 1: Frobenius/off-diagonal dichotomy

If a real symmetric `3x3` matrix `B` has eigenvalues `mu_j` with `|mu_j|>=s`, then

`tr(B^2)=sum_j mu_j^2>=3s^2`.

If every diagonal obeys `|B_ii|<s/2`, then

`sum_i B_ii^2<3s^2/4`.

Since

`tr(B^2)=sum_i B_ii^2+2 sum_{i<j} B_ij^2`,

we obtain

`sum_{i<j}B_ij^2>9s^2/8`,

and hence one off-diagonal square is strictly bigger than `3s^2/8`.

## Check 2: the selected pair is quantitatively indefinite

For

`D=[[a,b],[b,d]]`, with `|a|,|d|<s/2` and `b^2>3s^2/8`,

`det D=ad-b^2 <= |ad|-b^2 < s^2/4-3s^2/8=-s^2/8`.

Thus `D` is invertible indefinite and `Delta=|det D|>s^2/8`.

Write `D=J+E` with `J=[[0,b],[b,0]]`, `E=diag(a,d)`. Both singular values of `J` equal `|b|`. The singular-value perturbation inequality gives

`sigma_min(D)>=sigma_min(J)-||E||_op=|b|-max(|a|,|d|)`.

Hence

`kappa>s*(sqrt(3/8)-1/2)=s*(sqrt(6)-2)/4`.

## Check 3: light-diagonal constant

The pair-log source theorem gives

`8 sqrt(5) (Delta*kappa*s)^(-1/4)`.

Using the preceding strict lower bounds,

`Delta*kappa*s > s^4*(sqrt(6)-2)/32`.

Therefore the coefficient is at most the strict limit

`8 sqrt(5) [32/(sqrt(6)-2)]^(1/4) = 51.9616026228...`.

This is smaller than `128*2^(1/4)=152.2185107203...`.

## Check 4: heavy-diagonal constant

If some `|a|>=s/2`, then `|det B|=|mu_1 mu_2 mu_3|>=s^3`. The source rank-three scalar-pivot theorem gives

`128 (|a| |det B|)^(-1/4)`
`<=128 [(s/2)s^3]^(-1/4)`
`=128*2^(1/4)/s`.

Thus both branches are bounded by the common constant `128*2^(1/4)/s<153/s`.

## Check 5: outside conditioning

Conditioning on original coordinates in `I^c` changes only affine and constant terms in the active original-coordinate triple. It does not alter the `3x3` quadratic block, the independence of the active coordinates, or their density caps. Both cited source theorems explicitly allow arbitrary affine terms and outside couplings, so their constants are uniform in the conditioning variable.

## Check 6: continuity is logically separate

The account04/B15 source theorem requires only rank at least three plus a separately paid interval inequality. The physical `3x3` block is invertible, hence the ambient matrix has rank at least three. Applying the source theorem after the height estimate is therefore legitimate; no implication `L^infinity => C_0` for arbitrary one-dimensional densities is used.
