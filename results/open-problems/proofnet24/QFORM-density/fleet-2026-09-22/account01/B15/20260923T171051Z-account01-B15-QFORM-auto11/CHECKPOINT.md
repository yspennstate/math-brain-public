# QFORM B15 checkpoint — dyadic regularity ladder and soft-bank regularity budget

Run: `20260923T171051Z-account01-B15-QFORM-auto11`

Status: full QFORM OPEN. This checkpoint records two proved B15 interfaces being developed into the final report.

## 1. Original-coordinate absolute continuity

Let `X_1,...,X_n` be independent variables with arbitrary Lebesgue densities and let `A=A^T !=0`. Then `Q=X^TAX` is absolutely continuous.

Proof split, without rotation. If some `A_ii !=0`, condition on `X_{-i}`. Then `Q=a X_i^2+bX_i+c` with `a=A_ii !=0`; the pushforward of an absolutely continuous one-dimensional law by a nonconstant quadratic is absolutely continuous (split R at its single critical point). Averaging the conditional laws preserves absolute continuity.

If all `A_ii=0`, choose `A_ij !=0`. Conditioning on `X_{-i}` gives `Q=B X_i+C`, where `B=2 sum_{k!=i} A_ik X_k`. Since `B=2A_ij X_j+W` with `X_j` independent of `W`, the law of `B` is absolutely continuous, hence `P(B=0)=0`. For almost every outside realization the conditional map in `X_i` is a nonconstant affine map, so the conditional output is absolutely continuous. Again average.

Thus qualitative absolute continuity needs neither the cap-one bound nor three large eigenvalues. This proof is entirely in the original independent coordinates.

## 2. Exact dyadic tent regularity ladder

For a finite positive measure `mu` on R set

`K_r(x)=(r-|x|)_+/r^2`, `H_r=K_r*mu`, and `r_k=2^{-k}`.

Then

`D_infinity(mu) = sup_{k>=0} ||H_{r_k}||_infinity`,

where `D_infinity(mu)=inf{M: mu(E)<=M|E| for every Borel E}` (possibly infinity).

Indeed, if the dyadic supremum is `M`, then `H_{r_k} dx -> mu` weakly as `k->infinity`, while `H_{r_k}<=M`; testing against nonnegative compactly supported continuous functions gives `mu<=M dx`. Conversely, if `mu=p dx`, `||p||_infinity=M`, Young gives `||H_r||_infinity<=M`, and at Lebesgue points `H_{r_k}(x)->p(x)`, giving the reverse inequality.

Moreover

`mu=p dx with p in C_0(R)` iff `(H_{r_k})_k` is Cauchy in `L^infinity`.

The forward direction is uniform approximate-identity convergence. Conversely a sup-norm Cauchy sequence has a uniform limit `p in C_0`; because `H_{r_k} dx -> mu` weakly, necessarily `mu=p dx`. Quantitatively, if `eta_k=||H_{r_{k+1}}-H_{r_k}||_infinity` and `sum eta_k<infinity`, then

`||p-H_{r_m}||_infinity <= sum_{k>=m} eta_k`.

Hence bounded density is merely boundedness of the dyadic desmoothing ladder; continuous density is the strictly stronger Cauchy property.

## 3. Soft-bank regularity budget from completed account02/B15

Use the completed account02/B15 ruled-majority theorem (canonical source `math-open-problems@46c33d97490f78f8c3de0435f63d573958d81180`): for each invertible indefinite original-coordinate physical triple `S`, the majority output submeasure satisfies

`mu_S^+(E)<=C_S |E|`, `C_S<=pi sqrt(2)/kappa_S`, `kappa_S=sigma_min(A_SS)`.

For weights `a_S>=0`, define `R=sum a_S 1_{G_S}` and split the full output law exactly as

`mu=alpha_delta+beta_delta`,

where `alpha_delta` is the pushforward restricted to `{R>=delta}` and `beta_delta` to `{R<delta}`. Then

`alpha_delta(E)<=D_delta |E|`, `D_delta=(1/delta) sum a_S C_S`.

Thus the high-majority component is not only paid in height; it has deterministic regularity budgets at every scale. For normalized box profile `B_r^nu(y)=nu([y-r,y+r])/(2r)`,

`|B_r^alpha(y+h)-B_r^alpha(y)| <= D_delta min(|h|/r,2)`.

For normalized tent profile `H_r^alpha=K_r*alpha`,

`Lip((H_r^alpha)') <= 4 D_delta/r^2`,

so

`|H_r^alpha(y+h)-2H_r^alpha(y)+H_r^alpha(y-h)| <= 4 D_delta h^2/r^2`.

Consequently the low-majority residual obeys the curvature-forcing inequality

`H_r^beta(y) >= [ H_r^mu(y) - (H_r^mu(y-h)+H_r^mu(y+h))/2 - 2D_delta h^2/r^2 ]_+`.

If `a_S=kappa_S/sum_T kappa_T` and `(1/N)sum_S kappa_S >= c s_3(A)`, then

`s_3(A) D_delta <= pi sqrt(2)/(c delta)`.

Therefore any unit-scale tent concavity exceeding the universal high-majority `C^{1,1}` budget must be carried quantitatively by the original-product minority/two-sheet residual.

No uniform pointwise Fourier decay, rotated independence, arbitrary-joint density cap, or projection/X-ray-only shortcut is used.
