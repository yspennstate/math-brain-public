# account02/B11 early calculation — three heavy rows form a quantitative physical packet

Run `20260923T220048Z-account02-B11-qform-auto11`. Full QFORM remains open.

Consume account03/B11 r42 in its small-transfer branch. Let `E` be the H-side orthonormal 3-frame and `z_i=E^T e_i`, `q_i=||z_i||^2`. Put `J={i:q_i>3/4}`. r42 proves `|J|<=3`, and r41 gives for the internal 3x3 matrix `C=E^T A[H,H]E`

`σ_min(C) > β0 s`,  `β0=289/15984`,  `s=min |λ_a(M)|>=1`.

If `|J|=3`, let `Z` be the 3x3 matrix whose rows are the `z_i^T`, `i in J`. Since `E^T E=I`,

`Z^T Z <= I`.

Write the eigenvalues of `Z^T Z` as `μ1>=μ2>=μ3>=0`. Each is at most one, while

`μ1+μ2+μ3 = sum_{i in J} q_i > 9/4`.

Hence

`μ3 > 9/4 - 2 = 1/4`,

so `σ_min(Z)>1/2`. The literal physical principal block on those three original coordinates is

`A[J,J] = Z C Z^T`,

therefore

`σ_min(A[J,J]) >= σ_min(Z)^2 σ_min(C) > β0 s/4`.

The pinned completed three-dimensional physical theorem in `e5f71d79.../COUNTEREXAMPLE_SEARCH.md` (Theorem A, localized form, affine terms allowed after conditioning outside J) now applies at an actual inequality:

`||p_Q||_∞ < 24 sqrt(pi)/(β0 s) = 2352.739295740382... / s`.

Thus the r42 finite-heavy-row collar is paid whenever all three possible heavy rows occur. The first unpaid case has at most two heavy rows. This uses only original-coordinate conditioning; no spectral-coordinate independence is invoked.
