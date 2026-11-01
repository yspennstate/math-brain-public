# fleet02/B01 early checkpoint — one projected crossing kills the near-null logarithm after square peel

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T170428Z-fleet02-B01-QFORM-auto11`. Full QFORM remains open.

The latest partner fleet03/B01 (`fleet03-B01-20260923T163050Z-auto11`) reduces its punctured near-null leakage branch, after scalar completion of a physical coordinate with coefficient `a != 0`, to

`R = delta Y^2 + 2Y(ell dot Z + beta) + H(Z)`

and proves the leakage currency lower bound

`||ell||_2 >= W2^(1/4)/(sqrt(2)|a|^(1/2))`.

The current projected-crossing theorem `NEW_PROJECTED_CROSSING.md` can be used at the *borderline* `k=1, ell_volume=1`, where it does not by itself give an L-infinity density bound but does give exactly enough averaged frequency decay for the older half-Riesz square peel.

Split the original light coordinates `Z=Z_I union Z_J`, assume `ell_J != 0`, and let `M` be the quadratic matrix of `H`. Put

`C = M_{I,J}(I-Pi_row(ell_J))`,
`Z1 = ||C||_F^2 > 0`,

with row weights `alpha_i=||C_{i,*}||_2^2/Z1 <= 1/2`. Set

`P = ||ell_J||_2 sqrt(Z1) = ||ell_J||_2 ||C||_F`.

Applying grouped projected crossing to `R`, with original hub `Y`, gives

`|phi_R(t)| <= min(1, 2 pi P^(-1/2)|t|^(-1))`.                 (E1)

For the Fourier convention in the source, the Riesz identity at alpha=1/2 is

`H_{1/2}(R) <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)| dt`.

The integral in (E1) is explicit. With `K=2pi P^(-1/2)`,

`int_R |t|^(-1/2) min(1,K/|t|) dt = 8 sqrt(K)`,

hence

`H_{1/2}(R) <= 8 P^(-1/4)`.                                  (E2)

Now restore the completed outer original coordinate:

`Q = a(X+h(Y,Z))^2 + R(Y,Z)`.

The completed square peel from the required 20260922T211500Z Fourier report gives

`||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(R)`.

Therefore

`||p_Q||_infinity <= 8 |a|^(-1/2) (||ell_J||_2 ||C||_F)^(-1/4)`.  (E3)

No reciprocal power of the near-null coefficient `delta`, of the physical-pair determinant, or of `sigma_min(B)` appears. This is the first substantive checkpoint. The remaining work in this run is to verify the precise source hypotheses, combine (E3) with the partner's `W2` leakage inequality, and stress it on a strict-N3 target family where the partner's signed-Fejer estimate still has a logarithmic defect.
