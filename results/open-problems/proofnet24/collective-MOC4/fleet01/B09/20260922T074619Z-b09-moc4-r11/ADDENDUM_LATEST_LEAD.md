# Addendum — integration with the latest full-tangent lead

Late in this invocation, fleet03/B07 completed run `20260922T074824Z-fleet03-B07-MOC4-r13`, proving `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` and `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`. This addendum consumes that complete candidate rather than leaving the same-run result tied only to r12.

At a genuine mixed-Schur global maximizer the lead now proves that the pair kernel vector `z` is a kernel vector of the **full** true-unitary Hessian. If the full cubic covector is split into the singular pair tangent and its orthogonal complement, the exact fourth-order gate is

`q + 3 R_pair + 3 R_cross <= 0`,                            (L1)

where `R_cross=<r,S^+r>>=0` is the generalized-Schur-complement cross reserve.

The preceding B09 theorem `MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`, together with the named OTHER-account fleet02/B07 roof identities

`a=2(gamma+r_tau)`, `b=2(gamma+r_{tau^c})`,

implies

`R_pair >= (1/8)[ ||ell_u||^2/(gamma+r_tau)
                 +||ell_v||^2/(gamma+r_{tau^c}) ]`.        (L2)

Substituting (L2) into the new lead gate (L1) gives the exact combined necessary condition

`boxed(
q <= -(3/8)[ ||ell_u||^2/(gamma+r_tau)
             +||ell_v||^2/(gamma+r_{tau^c}) ]
     -3 <r,S^+r>
)`.                                                         (L3)

This is `MOC4-FULL-TANGENT-ROOF-CROSS-RESERVE-v1`.

Independently, the sharp block-row ceiling proved in `ADDENDUM_SHARP_CEILING.md` gives on the same mixed-Schur edge

`boxed(16 h_e (gamma+r_tau)(gamma+r_{tau^c}) <= 1)`,        (L4)

where `h_e=lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)` is built from the exact spectral covariance inverses of fleet01/B07.

Therefore every generic positive-gap MSQR survivor must simultaneously satisfy the full cross-split quartic payment (L3), the full-Hessian cross-block annihilation equations `D^2h[z,Y]=0` for every external root/Cartan tangent, and the spectral-conditioning ceiling (L4). In particular, any nonzero cross residual imposes a strictly additional quartic cost beyond the already roof-weighted same-pair payment, while a large gap forces the covariance metric toward its cross-ratio-degenerate locus.

This still does **not** close `MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1`: the determinant-specific formulas for `r` and `S` must now be evaluated and shown incompatible with (L3)-(L4), or a genuine true-unitary target-level counterexample must be constructed. The `NDI` branch remains separate.
