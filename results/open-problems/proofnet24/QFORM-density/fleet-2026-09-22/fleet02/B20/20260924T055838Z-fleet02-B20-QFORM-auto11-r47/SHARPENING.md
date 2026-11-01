# r47 sharpening — current arbitrary-rank small-ball constant 4

The immutable main report used the completed pinned full-matrix pair theorem with its original arbitrary-rank small-ball constant 5, obtaining `||p_Q||_infinity<11329` on fleet03/B20 r48's strong-edge pair.

The latest compatible continuation `interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_pairs/REPORT.md`, Lemma 5, proves the stronger uniform statement for any real quadratic polynomial with quadratic part S:

`P(|zeta-s|<=rho) <= 4 (rho/||S||op)^(1/4)`.

The exact rank-two completion from the main report gives `||S||op>=s3(A)>=1`. Hence for the pair logarithmic envelope

`p_Q(t)<=2 sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa|t-R|))`

the layer-cake bound improves to

`E log_+(a/|t-R|)<=16 a^(1/4)`.

Optimizing `A/r+B sqrt(r)` now gives

`boxed: ||p_Q||_infinity <= 3*256^(1/3) D^(-1/3) kappa^(-1/6).`

For the newest designated partner r48 constants

`D>=9.530157744638501e-7`,
`kappa>=6.075614261408114e-5`,

this becomes

`||p_Q||_infinity <= 9762.690347743192 < 9763.`

For the preceding B20 heavy-pair collar `D>=3/4096`, `kappa>=1/64`, it becomes

`||p_Q||_infinity <= 422.64668785851217 < 423.`

The qualitative conclusion is unchanged but stronger: any target state containing such a quantitative invertible indefinite original-coordinate pair is paid directly by exact Schur completion, without a post-Schur rank-two or third-crossing hypothesis. All other coefficients and the nonzero Schur tail remain present.
