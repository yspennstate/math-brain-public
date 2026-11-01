# Rigor check — fleet01/B15 20260924T110722Z

Status checked: `QFORM-FRESNEL-HALF-HOLDER-v1`, sharpness example, and the fleet02/B15 application in `REPORT.md`.

## 1. Fourier-to-Hölder constant

For `1<alpha<2`,

`(1/(2pi)) int_R |e^{-ith}-1| B|t|^{-alpha}dt
 = (B/pi) int_0^infinity min(2,|h|t)t^{-alpha}dt`.

Splitting at `2/|h|` gives exactly

`(B/pi)2^(2-alpha)|h|^(alpha-1)[(2-alpha)^(-1)+(alpha-1)^(-1)]`.

At `alpha=3/2` this is `(4sqrt(2)/pi)B sqrt(|h|)`. With Theorem F's
`B=(4pi)^(3/2)M^(-1/2)`, the coefficient is `32sqrt(2pi)M^(-1/2)`.

The near-zero existence step uses the separate characteristic-function bound `|phi|<=1`; hence `phi in L1` from `min(1,B|t|^-alpha)`. No law-uniform Fourier decay outside the source theorem is asserted.

## 2. Sharpness convolution

For `Y=(X_1+X_2)/sqrt(2)` with iid `Unif[-1/2,1/2]`,

`p_Y(y)=sqrt(2)(1-sqrt(2)|y|)` on `|y|<1/sqrt(2)`.

Thus for `S=Y^2`,

`h(s)=sqrt(2)s^(-1/2)-2`, `0<s<1/2`.

Let `k(s)=s^-1/2 1_{s>0}`, `u(s)=1_{s>0}`. For `0<t<1/2`,

`k*k=pi`, `k*k*k=2pi sqrt(t)`, `k*u*u=(4/3)t^(3/2)`, `u*u*u=t^2/2`.

Expanding `(sqrt(2)k-2u)^{*3}` gives

`4sqrt(2)pi sqrt(t)-12pi t+16sqrt(2)t^(3/2)-4t^2`.

Therefore `p(t)/sqrt(t)->4sqrt(2)pi`, proving failure of every exponent `beta>1/2` at zero.

## 3. Coupled exact-target matrix

Let

`U=(1/3)[[1,2,2],[2,1,-2],[2,-2,1]]`.

Direct row products give `UU^T=I_3`. Taking rows of `R` to be `+u_j/sqrt(2),-u_j/sqrt(2)` gives `R^TR=I_3` and every row leverage `1/2`. Hence `A_*=R diag(1,2,4) R^T` has nonzero spectrum exactly `{1,2,4}` and `L=8`.

Multiplication gives

`18A_*=[[25,-25,-10,10,2,-2],[-25,25,10,-10,-2,2],[-10,10,22,-22,-8,8],[10,-10,-22,22,8,-8],[2,-2,-8,8,16,-16],[-2,2,8,-8,-16,16]]`.

The partner theorem at `c_i=1/2`, `L=8` gives

`||p_f-p_g||inf <=6*2^(1/6) sum delta_i^(2/3)`.

Concavity gives `sum delta_i^(2/3)<=6^(1/3)Delta^(2/3)`, hence coefficient
`6sqrt(2)3^(1/3)=12.2378934159...`.

Theorem F gives height `12*8^(-1/3)=6`. The new Hölder theorem gives `32sqrt(2pi)/sqrt(8)=16sqrt(pi)=28.3592616145...`.

## 4. Correction audit

No step assumes independence of `R^T X`; all source theorems retain original-coordinate product provenance. No arbitrary-joint bounded coarea estimate is used. The qualitative coarea argument only proves null-set preservation. No projection/X-ray-only closure is used. The pointwise Fourier envelope is consumed only under completed Theorem-F structural hypotheses.

Conclusion: checks pass in the stated scoped chamber. Full unrestricted QFORM remains open.
