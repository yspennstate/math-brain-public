# fleet03/B16 independent review — orientation-free rank-two affine half-Riesz synthesis

**Run:** `20260922T164017Z-fleet03-B16-QFORM-r13`  
**Reviewed source:** `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`  
**Review assignment source:** current QFORM state integrated at `yspennstate/math-research-brain@358a219247c902b0d78467a5c40f493741daeb15`  
**Verdict:** `PASS_SCOPED_INDEPENDENT_REVIEW` for `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` and its stated rank-three Schur consequence. This is not a review or proof of the full QFORM conjecture.

## 1. Diffuse Fourier branch

For row leverage `c_i=|v_i|^2<=1/2`, the Brascamp–Lieb/Hausdorff–Young calculation is consistent with the stated Fourier convention. Writing `w_i=v_i/sqrt(c_i)` gives `sum c_i w_i w_i^T=I_r`. The rescaled BL functions contribute `c_i^(-c_i/2)||hat h_i||_{1/c_i}`. Beckner with `q=1/c_i`, `p=1/(1-c_i)` gives

`||hat h_i||_{1/c_i} <= (2pi)^{c_i}(1-c_i)^{-(1-c_i)/2}c_i^{c_i/2}`,

because `|h_i|=f_i`, `f_i<=1`, and `int f_i=1` imply `||h_i||_p<=1`. The `c_i` factors cancel and `-(1-c)log(1-c)<=c` gives `||hat g_t||_1<=(2pi)^r e^{r/2}`. The Fresnel transform then yields

`|phi_F(t)| <= e^{r/2} pi^{r/2}|det L|^{-1/2}|t|^{-r/2}`.

For `r=2`, integrating against the Fourier kernel of `|x|^{-1/2}` is legitimate after the report's Gaussian regularization. The scalar identity under the stated Fourier convention is

`widehat{|x|^{-1/2}}(t)=sqrt(2pi)|t|^{-1/2}`,

so the factor `(2pi)^(-1/2)` used in the report is correct. Splitting

`int_R |t|^{-1/2} min(1,K/|t|)dt=8 sqrt(K)`

with `K=e pi |det Lambda|^{-1/2}` gives `4sqrt(2e)|det Lambda|^{-1/4}`, safely below `128|det Lambda|^{-1/4}`.

## 2. Rank-one affine small-ball lemma

The heavy-coordinate case is valid with arbitrary linear terms: after conditioning, the coefficient of the surviving scalar quadratic is exactly `lambda u_i^2`; for `u_i^2>=1/2`, the inverse image of an interval of length `2rho` under a quadratic has total length at most `2sqrt(2rho/|a|)`, giving the stated `4sqrt(rho/|lambda|)` cap.

In the diffuse rank-one case, the Fourier estimate is `sqrt(e pi)|lambda t|^{-1/2}`. The Gaussian majorant

`1_{|z|<rho} <= e^v exp(-v z^2/rho^2)`

and exact Gaussian Fourier transform give

`e^v sqrt(e) Gamma(1/4)/(sqrt(2)v^{1/4}) sqrt(rho/|lambda|)`.

At `v=1/4`, this is `e^{3/4}Gamma(1/4)<10`, so the report's constant `10` is valid. No sign of `lambda` is used except through its magnitude.

## 3. Translated-kernel fusion and determinant signs

In the heavy two-frame branch, an orthogonal change only in the two-dimensional spectral coefficient space makes the heavy physical row `(sqrt(h),0)` without rotating the independent inputs. Thus

`Y_1=sqrt(h)X_i+T`, `Y_2=Z`,

where `X_i` is genuinely independent of `(T,Z)`, while `T,Z` may be arbitrarily dependent. This is exactly enough for the conditional translated kernel; no conditional independence of `T,Z` is invoked.

For

`Lambda=[[beta,gamma],[gamma,delta]]`

and `beta!=0`, completing the square gives residual quadratic coefficient

`det(Lambda)/beta`

on `Z^2`. After the kernel scaling, the normalized residual variable has rank-one quadratic coefficient magnitude

`lambda_0=k^2 |det Lambda|/beta^2`, `k=h^{-1/2}`.

Applying the rank-one affine small-ball lemma and the report's layer-cake kernel estimate gives

`32 sqrt(10) sqrt(k)|det Lambda|^{-1/4}`.

Since `h>1/2`, `sqrt(k)=h^{-1/4}<2^{1/4}`, and the constant is below `128`. The factor `|beta|^{-1/2}` cancels exactly against `lambda_0^{-1/4}`. Hence there is no small-nonzero-`beta` loss. Both signs of `det Lambda` and `beta` are covered because only the absolute determinant enters the small-ball coefficient.

For `beta=0`, invertibility forces `gamma!=0` and `|det Lambda|=gamma^2`. Conditional on the remaining coordinates, the polynomial is affine in the independent `X_i`; the cap-one half-kernel integral is `<=2sqrt(2)`. The normalized `Z` has density `<=sqrt(2)`. The resulting bound is `<=8|det Lambda|^{-1/4}`, so the singular endpoint is separately and correctly covered.

## 4. Kernel layer-cake constants

The source kernel scaling for a density cap `K` is correct: scaling `Y=KX` converts the density to cap one and contributes the factor `K Psi(K^2 a)`. For the averaging lemma, if `P(|W|<rho)<=L sqrt(rho)`, then

- for `0<s<1`, `{Psi(W)>s}` is contained in `{|W|<s^{-4}}`, giving `<=L s^{-2}`;
- for `s>=1`, it is contained in `{|W|<e^{1-s}}`, giving `<=L e^{(1-s)/2}<=4L/s^2` because `sup_{s>=1}s^2e^{(1-s)/2}=16e^{-3/2}<4`.

Therefore `int_0^infinity min(1,4L/s^2)ds=4sqrt(L)`, as claimed.

## 5. Rank-three Schur consequence

For the original-coordinate rank-three block `A_{I,I}=VMV^T`, choose physical row vector `v` with `c_i=|v|^2` and `a=v^T Mv!=0`. Completing the physical scalar coordinate leaves

`S=C-bb^T/a`.

Taking `T` to be an orthonormal basis of `v^perp` and `W=V_-T` gives `W^TW=I_2` because `V_-^T V_-=I-vv^T`. In a spectral basis with `v=sqrt(c_i)e_1`, write

`M=[[alpha,q^T],[q,G]]`, `a=c_i alpha`.

The residual coefficient is `N=G-qq^T/alpha`, so

`det N=det M/alpha=c_i det M/a`.

This identity is sign-correct without requiring definiteness. The arbitrary affine term induced by outside conditioning is within the scope of the reviewed rank-two theorem. Thus

`||p_Q||_infinity <=128[c_i |a| |det M|]^(-1/4)`

follows exactly. For a full exact-rank-three target, `|det M|>=||M||` and `|a|<=c_i||M||`, hence the source's `128/sqrt(|a|)` corollary is also correct.

## 6. Review conclusion and remaining scope

I find no mathematical defect in the reviewed statements or constants. In particular, the theorem correctly removes the **residual** small-Rayleigh orientation split and allows arbitrary induced original-coordinate affine terms. It does **not** pay an arbitrarily small or zero **outer scalar pivot**, and it does not apply unchanged to higher-rank Schur remainders. Those limitations are correctly stated in the source.

Accordingly, the next B16 projection-product step is no longer to re-prove arbitrary residual rank-two orientation. The target-relevant debt is to fuse the reviewed rank-two half-Riesz estimate with the zero/near-zero outer-pivot product-bank mechanism, or to make that reduction stable under arbitrary additional spectral components.

**Review verdict: PASS_SCOPED_INDEPENDENT_REVIEW. Full QFORM remains OPEN / NOT PROVED.**
