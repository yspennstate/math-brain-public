# account03/B13 r6 — full fixed-multiplicity audit and independent B13 sharpening check

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T145955Z-account03-B13-fixedmult-audit-r6`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution/memory label: `WITHOUT_VERIFIED_BRAIN`.

## Verdict

**PASS** for the pinned 17-eigenvalue manuscript in this independent end-to-end B13 audit. I read the full 790-line source, `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and the delivery note. I rechecked every proof interface, with detailed attention to definite pairs, the full hyperbolic envelope, rough-law Tonelli steps, nonsymmetric interpolation, the two rank bounds, Schur spectral counts, and full versus truncated half potentials. I found no fatal mathematical defect.

I also independently reconstructed the complete nine-eigenvalue replacement architecture from the current source-backed grouped physical-product Fourier compiler and its order-three density/order-two half-potential receivers. The threshold-nine theorem is mathematically sound in this audit. In addition, I independently verify the newer B10 constant sharpening to

\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty<2422\,K^2/s\qquad(s_9(A)\ge s>0).}
\]

This report is one independent review; it does not mutate any owner release flag. The unrestricted three-eigenvalue conjecture remains open. Global continuity is not proved; the no-pivot Fourier branch is continuous.

## Baseline audit map

- **Fourier inversion / Riesz / power envelopes: PASS.** Constants and Fourier convention are internally consistent. The Riesz weight is used only where the characteristic-function exponent exceeds the required weighted endpoint.
- **Geometric Brascamp–Lieb heat-flow proof: PASS.** Rough inputs are reached by monotone truncation; no rotated independence is asserted.
- **Product-projection lemma: PASS.** When rows with `b_i=0` are dropped, the proof may harmlessly enlarge the entropy sum to all rows; `sum_i(1-b_i)=d` for the full row family. No conditional-density shortcut is used.
- **Regularized determinant theorem: PASS.** The fourth-power decoupling, graph weights, regularizer `(2*pi*e)^2`, scalar Fourier powers, and final `-1/8` determinant exponent agree.
- **Sampling/completion: PASS.** The interpolation is allowed to be nonsymmetric; `rank R<=3r` globally and `rank R[L,L]<=r` are used in their correct locations; `D` vanishes on the seed and `E` has zero diagonal.
- **Spectral-to-volume proposition: PASS.** Singular values, not eigenvalues of the nonsymmetric correction, are used. The diagonal-dominance slack remains positive.
- **Schur spectral count: PASS.** The invertible case follows through the complementary principal compression of `A^{-1}` and the singular case by an `A+epsilon I` limit.
- **Scalar square / definite pair / hyperbolic pair: PASS.** All conditioning is on original physical coordinates. Orthogonal diagonalization occurs only inside deterministic two-dimensional integration.
- **Main 17-direction assembly and scaling: PASS.** The global claim is essential boundedness; continuity is correctly limited to the integrable-Fourier branch.

One harmless wording point persists in the hyperbolic proof: the original coordinate selected for the positive tail and the one selected for the negative tail need not be the same. The proof only needs one suitable coordinate on each tail, so no estimate changes.

## Independent derivation of the sharpened B13 pivot constants

### 1. Singular-convolution kernel

For
\[
J(d)=\int_{-1}^1 |x|^{-1/2}|x-d|^{-1/2}\,dx,
\]
reflection reduces to `d>0`. If `0<d<=1`, putting `r=d^{-1/2}` gives the exact decomposition
\[
J(d)=\pi+2\operatorname{arcosh}r+2\operatorname{arsinh}r.
\]
Now
\[
(r+\sqrt{r^2-1})(r+\sqrt{r^2+1})\le4r^2,
\]
because concavity of `sqrt` gives `sqrt(r^2-1)+sqrt(r^2+1)<=2r` and the product of the two square roots is at most `r^2`. Hence
\[
\boxed{J(d)\le\pi+4\log2+2\log(1/d)}
\]
for `0<d<=1`. For `d>=1`, the integral decreases with `d` on both sides of zero, so the same bound with `log_+` follows. Thus
\[
\boxed{J(d)\le\pi+4\log2+2\log_+(1/|d|).}
\]

### 2. Quarter-power small ball and logarithmic potential

The source-backed Fejer calculation starts from the valid physical sign-cut envelope
\[
|\phi_R(t)|\le(4\pi e/(L|t|))^{1/4}.
\]
With `U=3/(5 rho)` and `K_U(x)=(sin(Ux)/(Ux))^2`, the direct Fourier calculation gives
\[
C_F=\frac{2500}{2209}\frac{16}{21}\left(\frac56\right)^{1/4}(4\pi e)^{1/4}
=1.991708403\ldots<2.
\]
Combining the off-diagonal branch with the elementary diagonal-square branch at the split `rho=L/16` yields
\[
\boxed{\Pr(|R-a|<\rho)\le\min\{1,2(\rho/L)^{1/4}\}.}
\]
For `L>=1`, layer cake therefore gives
\[
\boxed{\sup_a\mathbb E\log_+(1/|R-a|)\le4+4\log2.}
\]
At a scalar physical pivot `|A_ii|>=eta=1/100`, the preceding `J` inequality gives the truncated half potential
\[
H_{\rm scalar}\le10[\pi+8+12\log2]
=194.5935882\ldots,
\]
and the full half potential is `<195.594` after the outside tail.

### 3. Optimized hyperbolic envelope

For an indefinite physical pair with `D=|det B|`, repeat the manuscript hyperbola proof with tail ratio parameter `q=2/9`. On a branch `u e^t+w e^{-t}`, choose a physical coordinate with `|u_i|>=|u|/sqrt2`. The derivative-to-position ratio on the tail is `(1-q)/(1+q)=7/11`, so each tail costs at most `(11/7)log2`. The first tail cutoff is
\[
T_1=\frac12\log(\sqrt2/q)=\log3-\frac14\log2.
\]
The two cutoffs and the two tail costs combine exactly to
\[
C_0=2\log3+\frac{37}{14}\log2
\]
and
\[
p_q(v+\delta)\le D^{-1/2}\left[C_0+
\log_+\frac{72\sqrt2}{49\,|\delta|\Lambda}\right],
\]
where `Lambda=mu_+^{-1}+|mu_-|^{-1}`. Since `Lambda>=2/sqrt D`,
\[
p_q(v+\delta)\le D^{-1/2}\left[C_0+
\log_+\frac{36\sqrt2\sqrt D}{49|\delta|}\right].
\]
Using the manuscript's shifted logarithmic-kernel integral gives
\[
H_{\rm ind}(D)\le D^{-1/2}\left[4C_0+8+4\log_+\left(\frac{36\sqrt2}{49}\sqrt D\right)\right].
\]
For `D>=1/100` this expression is decreasing in `sqrt D`; at `D=1/100` the logarithmic constant term is inactive. Hence
\[
\boxed{H_{\rm ind}<10(4C_0+8)=241.164543,}
\]
and the full half potential is `<242.165<242.2`.

Thus every pivoted Schur remainder with the required surviving spectral direction has full half potential `<242.2`; the indefinite pair is the worst of the three pivot types.

## Complete nine-direction assembly with constant 2422

Normalize `K=s=1`, retaining `eta=1/100`, `kappa=1/80^2`.

1. **No pivot.** The audited order-three spectral-to-volume argument gives `V_3(A)>=kappa^3`. A fair physical cut gives `E_3(M)>=4^{-3}kappa^3`, so `E_3(M)^(-1/6)<=160`. The source-backed marginal-free order-three receiver gives
   \[
   \|p_Q\|_\infty\le160C_3=2370.934027\ldots<2371<2422.
   \]
2. **Scalar pivot.** Its Schur complement retains at least eight unit spectral directions. If the child has a pivot, the preceding full half-potential bound is `<242.2`; if it has no pivot, `s_5>=1` and the order-two half-Riesz receiver gives `<153`. The outer square profile costs `eta^{-1/2}=10`, so
   \[
   \|p_Q\|_\infty<2422.
   \]
3. **Definite pair pivot.** The exact area calculation gives `10*pi<32`.
4. **Indefinite pair pivot.** The pair Schur complement retains at least seven unit directions, hence at least one. The same hyperbolic/log-potential calculation is uniformly far below 2422.

Scaling `Y=KX` and `A/s` gives the stated `2422 K^2/s` bound. No moments, support, smoothness, Gaussianity, sign, exact-rank, leverage, connected-support, or rotated-independence assumption is introduced.

## Current lower-threshold frontier

The newest structural result I checked lowers the **structural** no-pivot boundary to seven directions: under `s_7(A)>=1`, either the ordinary order-three volume already closes by the order-three receiver, or the invertible-seed overlap-one volume satisfies a fixed positive lower bound. This is not yet a seven-direction density theorem because the common physical anchor is shared by the two translated banks; treating it as independent after the shear would be invalid.

The older `s_8` terminal determinant-ratio packet is also not by itself an analytic receiver; the sibling improvement for this run gives an explicit product-law obstruction to any theorem using only that ratio / the Schur-translated pure-triangle curvature.

## Status

- Pinned `s_17` manuscript: **PASS** in this audit.
- Complete `s_9` theorem: **PASS** in this audit.
- Sharpened constant `<2422 K^2/s`: **PASS** in this audit.
- `s_7`/`s_8` full density theorem: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
- Full-target continuity: **OPEN**; no-pivot Fourier branch is continuous.
