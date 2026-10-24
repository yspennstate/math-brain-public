SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T17:13:18Z.
attacking: the partner single-dominant-near-null spike; combine one original hub with the new projected-crossing theorem and eliminate the apparently small hub-coupling loss by an exact rank-three determinant identity.

# Early checkpoint — exact hub/projected-crossing invariant

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN.

Let `A=R M R^T`, `R^T R=I_3`, with `M` invertible symmetric. Fix an ORIGINAL coordinate `h` with spectral row `r=r_h`, and partition the remaining original coordinates into disjoint `I,J`. Put

`G_I=R_I^T R_I`, `G_J=R_J^T R_J`, `m=M r`,
`w=R_J m=A[J,h]`, `S=||w||_2`,
`P_w=ww^T/S^2`,
`C=A[I,J](I-P_w)`.

Here `C` is exactly the projected light-crossing matrix that appears in the completed one-hub + two-crossing-direction theorem `NEW_PROJECTED_CROSSING.md`.

The first essential calculation is

`boxed: S^2 e_2(C^T C)=det(M)^2 det(G_J) r^T adj(G_I) r.`

For positive-definite `G_I,G_J`, write

`H_J=G_J-G_J m m^T G_J/(m^T G_J m)`.

Then `CC^T=R_I M H_J M R_I^T`. The matrix `H_J` has rank two, null vector `m`, and

`pdet(H_J)=det(G_J)||m||^2/(m^T G_J m)`.

For `N=M G_I M`, the product of the two nonzero eigenvalues of `H_J^{1/2} N H_J^{1/2}` is

`pdet(H_J) * [m^T adj(N)m]/||m||^2`.

Since `adj(M G_I M)=det(M)^2 det(G_I) M^{-1}G_I^{-1}M^{-1}` and `m=M r`, this equals

`det(M)^2 det(G_J) det(G_I) r^T G_I^{-1}r /(m^T G_Jm)`.

Multiplying by `S^2=m^T G_Jm` proves the identity. The general semidefinite endpoint follows by continuity and the polynomial form `det(G_I)r^T G_I^{-1}r=r^T adj(G_I)r`.

Moreover, when `G_I` is positive definite and `C` has rank two, its squared two-volume row marginal at `i in I` is exactly

`boxed: alpha_i = r_i^T G_I^{-1}r_i - (r_i^T G_I^{-1}r)^2/(r^T G_I^{-1}r).`

Indeed `col(C)=R_I(r^perp)` because `range(H_J)=m^perp` and `M(m^perp)=r^perp`; the displayed formula is the diagonal of the orthogonal projector onto `R_I(r^perp)`.

Thus the completed one-hub projected-crossing theorem will depend on `S` and `e_2(C^TC)` only through their product, so a small physical hub coupling `S` is not itself a loss in exact rank three. The next step is to turn this identity into a continuous-density theorem and apply the account02/B11 dominant-spike reduction at an actual inequality.
