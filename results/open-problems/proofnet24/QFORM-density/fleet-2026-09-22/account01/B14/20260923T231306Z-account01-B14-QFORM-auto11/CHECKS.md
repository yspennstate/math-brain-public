# Checks for account01/B14 Schur zero-tax localization

Run: `20260923T231306Z-account01-B14-QFORM-auto11`

## C1. Completion of squares, invertible block

For symmetric invertible `B` and `z=(1/2)B^{-1}ell`,

`(x+z)^T B(x+z)=x^T Bx+ell^T x+(1/4)ell^T B^{-1}ell`.

Therefore

`x^T Bx+ell^T x+c=(x+z)^TB(x+z)+c-(1/4)ell^TB^{-1}ell`.

No Jacobian appears because this is a translation of the random input, not a linear rotation/scaling.

## C2. Ambient Schur identity

For `r=Cy` and `z=B^{-1}r`,

`x^TBx+2x^Tr+y^TDy
=(x+z)^TB(x+z)+y^T(D-C^TB^{-1}C)y`.

The identity is exact for every `x,y`; hence the conditional density constant is independent of the magnitude of `y` and of all outside moments/support data.

## C3. Product-law preservation

Conditioning is only on outside **original coordinates**. For fixed `y`, the active vector is shifted coordinatewise by the deterministic vector `B^{-1}Cy`. Translation preserves independence and preserves each marginal density cap `<=1`. No rotation of the input random variables is performed.

## C4. Countable fragments

If the outside law is `sum_j nu_j` with masses `m_j`, then for every interval `I`,

`eta_j(I)=int P(Q in I | Y=y) dnu_j(y) <= m_j K(B)|I|`.

Tonelli/monotone convergence gives

`sum_j eta_j(I)<=K(B)|I| sum_jm_j=K(B)|I|`.

Thus the fragment ledger is exactly mass-linear.

## C5. Singular pseudoinverse identity

For symmetric `B`, let `P0` project to `ker B`, `r0=P0r`, `rR=(I-P0)r`, `z=B^dagger r`. Then `Bz=rR` and `r0^Tz=0`. Hence

`(x+z)^TB(x+z)+2r0^T(x+z)-z^TBz
=x^TBx+2rR^Tx+2r0^Tx
=x^TBx+2r^Tx`.

If `P0C=0`, then `r0=0` for every `y` and the same zero-tax localization applies with `B^dagger`. If `P0C !=0`, the sole residual linear defect after exact completion is `2(P0Cy)^Tx`.

## C6. Dense reflection block

Let `J=11^T` in dimension three. Since `J^2=3J`,

`B_*^2=(I-(2/3)J)^2=I-(4/3)J+(4/9)3J=I`.

On `span{1}`, `J` acts by `3`, so `B_*` acts by `-1`; on `1^perp`, `J=0`, so `B_*` acts by `+1`. Hence `spec(B_*)={1,1,-1}` and `B_*^{-1}=B_*`.

## C7. Exact target verification by interlacing

Let the full ambient matrix be `n x n` and let the principal `3 x 3` block have ordered eigenvalues `mu_1=1, mu_2=1, mu_3=-1`. Cauchy interlacing gives

`lambda_2(A) >= mu_2 = 1`

and

`mu_3=-1 >= lambda_n(A)`.

Thus `lambda_1(A),lambda_2(A)>=1` and `lambda_n(A)<=-1`: at least three eigenvalues have modulus at least one.

## C8. Partner theorem actually used

Completed designated-partner material inspected at source commit

`7a0ffb7d9c4c6074cc6e13375db70828740e1bd4`

under

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T220530Z-account02-B14-QFORM-auto11/REPORT.md`

and its `CHECKS.md` verifies the 3D theorem at threshold one, including affine terms. Applied here to `B_*`, it supplies

`K(B_*) <= 6 sqrt(pi)`.

The new Schur localization then yields the ambient inequality

`||p_Q||_infty <= 6 sqrt(pi)`.

## C9. Scope check

This does **not** derive a suitable invertible original-coordinate principal block from the bare global hypothesis `s_3(A)>=1`. Therefore full QFORM remains open. The report makes no pointwise quadratic Fourier-decay claim and does not treat diagonal/projection-only controls as a proof of the global theorem.