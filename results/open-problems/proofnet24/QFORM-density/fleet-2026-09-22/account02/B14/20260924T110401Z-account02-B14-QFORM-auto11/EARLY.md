SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T11:04:01Z.
attacking: decouple before rough localization — prove that arbitrary fragments of one duplicated coordinate copy become mass-homogeneous cap-one difference laws, then apply the fixed-source volume receiver without fragment tax.

# Early substantive checkpoint

Full unrestricted QFORM remains OPEN; continuity is separate.

## First unpaid implication

`QFORM-DIFFERENCE-SIDE-LOCALIZE-OR-KEEP-OSCILLATORY-SIDE-WHOLE-v1`:
after exposing a decoupled D/D'/D5/projected-crossing receiver, place any rough spatial localization on only one duplicated difference-side copy and extract its mass before Brascamp--Lieb/Holder norms. If a structural branch truly requires localizing the oscillatory-side source before its characteristic-function norm, or requires simultaneous normalization of both copies, this compiler does not pay that step and another whole-law receiver is needed.

## One-copy difference cap repair

Let `f` be a probability density with `0<=f<=1`. Let `rho>=0` be any finite subdensity of mass `m=int rho` (for a decomposition one has `rho<=f`). Define

`G_rho(w)=int f(w+y) rho(y) dy = (f * tilde(rho))(w)`.

Then

`int G_rho = m`,  and  `0<=G_rho(w)<=m` for every `w`,

because `f<=1`. Hence for `m>0`

`gamma_rho := G_rho/m`

is again a probability density with cap one. No support, diameter, fragment-count, translation, moment, BV, or connectedness parameter appears.

If `f=sum_a rho_a` is any finite or countable positive decomposition, then exactly

`f*tilde(f)=sum_a m_a gamma_a`,

with `m_a=int rho_a`, `sum_a m_a=1`, and every `gamma_a<=1`.

Coordinatewise, for independent laws `f_j` and arbitrary independent label decompositions `f_j=sum_a rho_{j,a}`, the product difference law is the convex mixture

`tensor_j(f_j*tilde(f_j)) = sum_{alpha} m_alpha tensor_j gamma_{j,alpha_j}`,

where `m_alpha=prod_j m_{j,alpha_j}` and `sum_alpha m_alpha=1`. Thus any decoupled estimate that is uniform for product probability densities capped by one is exactly zero-tax under arbitrary one-copy localization.

## Fixed-source Theorem D stress family

Take six `I` coordinates, three `J` coordinates, and

`M=(1/sqrt(2))*[[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1]]`.

For `A=[[0,M],[M^T,0]]`, the nonzero spectrum is `{1,1,1,-1,-1,-1}`, so this is inside the exact owner target. Also `M^T M=I_3`, hence `Z=e_3(M^T M)=1`. The eight nonzero 3x3 row minors all have squared determinant `1/8`; every row occurs in exactly four, so every volume row marginal is exactly `1/2`.

Therefore the completed fixed-source Theorem D at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives

`||p_Q||_infty <= 6 sqrt(e) = 9.8923276242...`

for `Q=2 X_I^T M X_J`, uniformly over all independent cap-one laws.

Now put each `J` marginal on `N` arbitrary remote teeth of length `1/N`. If one conditions the ORIGINAL `J` variables tooth-by-tooth first, each normalized tooth has cap `N`; after translating and scaling to cap one the cross block is `M/N`, so Theorem D yields only `6 sqrt(e) N` on every conditional cell, and the averaged certificate remains `6 sqrt(e) N`.

If instead one first decouples and fragments only the copied `J'` variables, each conditional difference coordinate has normalized density cap one by the lemma above, while the matrix `M` is unchanged. The same Theorem D bound `6 sqrt(e)` holds on every label cell and averaging the cell masses returns exactly `6 sqrt(e)`, independent of tooth count and locations.

This is a proof-interface obstruction to fragment-first normalization, not a QFORM counterexample. The final report will include the countably fragmented unbounded-support version and the relation to the newest account03/B14 Gaussian-mixture/BV obstruction.
