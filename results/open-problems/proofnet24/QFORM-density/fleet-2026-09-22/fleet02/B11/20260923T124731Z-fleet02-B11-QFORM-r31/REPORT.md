# A one-sided product-provenance compiler for the indefinite null-sum endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: fleet02/B11, indefinite signatures  
Run: `20260923T124731Z-fleet02-B11-QFORM-r31`

**Status.** A new supporting theorem and a sharp reduction of the completed partner's exact two-bank null-sum endpoint are proved below. The full arbitrary-matrix QFORM conjecture remains OPEN. Essential boundedness is proved in the stated scopes; continuity follows in the new compiler from an integrable characteristic function. No post-rotation independence, moment, support, log-concavity, or continuity assumption on the inputs is used.

## 1. Exact unpaid endpoint and source pins

The completed designated partner fleet03/B11 r29, canonical source

`yspennstate/math-open-problems@2d86ea167ae1b16705983d4cf95198e254de6ca6`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T111415Z-fleet03-B11-QFORM-r29/REPORT.md`,

reduces its exact cross-rank-one, shared-curvature-zero endpoint (up to the sign-dual relabelling) to the following geometry. In a three-dimensional spectral basis,

\[
M=\begin{pmatrix}
\beta&0&\gamma\\
0&0&\alpha\\
\gamma&\alpha&\delta
\end{pmatrix},\qquad \sigma_{\min}(M)\ge s>0,                       \tag{1.1}
\]

while the ORIGINAL physical coordinates split into independent banks `S,T` whose spectral rows are

\[
r_i=(a_i,b_i,0),\ i\in S,\qquad r_j=(0,d_j,c_j),\ j\in T,          \tag{1.2}
\]

and

\[
\sum_{i\in S}r_ir_i^T=\operatorname{diag}(1,\rho,0),\qquad
\sum_{j\in T}r_jr_j^T=\operatorname{diag}(0,1-\rho,1),             \tag{1.3}
\]

with the partner branch satisfying `rho,1-rho >= 1/1024`.

Partner r30, canonical source

`yspennstate/math-open-problems@35b5ef493e41323df07d60d73d77ae84791c5e38`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T115328Z-fleet03-B11-QFORM-r30/REPORT.md`,

proved `QFORM-TWOPLANAR-JOINTCAP-NULLSUM-FALSE-v1`: bounded planar joint densities alone cannot control the corresponding null-sum receiver. Thus (1.2)-(1.3), i.e. genuine product-projection provenance, has to be used.

The required pinned Claude source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. I use two completed pieces at actual inequalities below: its Lemma 1 (`int |hat g|^p <= 4 pi/sqrt(p)` for `p>=2` and `|g|<=f<=1`) in the new proof, and its ruled Theorem C from `COUNTEREXAMPLE_SEARCH.md` to pay the one-sheet sign side.

## 2. Spectral noncollapse is exact at the null endpoint

### Lemma 2.1 — QFORM-NULLSUM-SPECTRAL-NONCOLLAPSE-v1

For (1.1),

\[
\det M=-\beta\alpha^2                                                   \tag{2.1}
\]

and

\[
M^{-1}=\begin{pmatrix}
\beta^{-1}&-\gamma/(\alpha\beta)&0\\
-\gamma/(\alpha\beta)&(\gamma^2-\beta\delta)/(\alpha^2\beta)&\alpha^{-1}\\
0&\alpha^{-1}&0
\end{pmatrix}.                                                          \tag{2.2}
\]

Consequently

\[
|\beta|\ge s,\qquad |\alpha|\ge s.                                     \tag{2.3}
\]

If `beta>0`, the signature is `(+,+,-)`; if `beta<0`, it is `(+,-,-)`.

### Proof

(2.1)-(2.2) are direct determinant/cofactor calculations. Since `M` is symmetric and `sigma_min(M)>=s`, `||M^{-1}||op<=1/s`; every matrix entry of `M^{-1}` therefore has modulus at most `1/s`. The `(1,1)` and `(2,3)` entries give (2.3).

If `beta>0`, (2.1) has negative determinant, so a nonsingular symmetric `3x3` matrix has either one or three negative eigenvalues. The positive Rayleigh value `e_1^TMe_1=beta` excludes negative definiteness, leaving exactly one negative eigenvalue. If `beta<0`, the determinant is positive, so there are zero or two negative eigenvalues; the negative Rayleigh value excludes positive definiteness, leaving exactly two. QED.

This is the first useful obstruction to importing the r30 anisotropic planar-cap example into the target. In the r30 construction the third eigenvalue is `eps^2`. Multiplying the whole form by `eps^{-2}` to restore that eigenvalue to one sends its density at zero to

\[
\varepsilon^2\bigl(2\log(1/\varepsilon)+1+2\log2+\varepsilon^2/12\bigr)\to0,   \tag{2.4}
\]

so the r30 divergence is destroyed by the scalar normalization needed to enter the three-large-eigenvalue target. This does not prove the target, but it rules out that direct counterexample transfer.

## 3. Determinant-one shears expose the correct product structure

Put

\[
U=\sum_{i\in S}a_iX_i,\quad Z=\sum_{i\in S}b_iX_i,\quad
W=\sum_{j\in T}d_jX_j,\quad V=\sum_{j\in T}c_jX_j.                      \tag{3.1}
\]

The exact rank-three form is

\[
Q=\beta U^2+2\alpha V(Z+W)+2\gamma UV+\delta V^2.                      \tag{3.2}
\]

Define

\[
H=Z+(\gamma/\alpha)U,\qquad L=W+(\delta/(2\alpha))V.                  \tag{3.3}
\]

Then, identically,

\[
\boxed{Q=\beta U^2+2\alpha V(H+L).}                                    \tag{3.4}
\]

The shears in (3.3) have determinant one on each source plane. Therefore the left coefficient frame `(a_i, b_i+(gamma/alpha)a_i)` has Gram determinant exactly `rho`; the right `(c_j,d_j+(delta/(2alpha))c_j)` has Gram determinant exactly `1-rho`. More strongly, normalized frame leverage is invariant under the shear: for the left bank it is exactly

\[
\ell_i=a_i^2+b_i^2/\rho.                                                \tag{3.5}
\]

Thus a large `gamma/alpha` cannot by itself create or remove the true product-frame obstruction.

## 4. New theorem: one-sided null-sum Fresnel--Brascamp--Lieb compiler

### Theorem 4.1 — QFORM-ONESIDED-NULLSUM-FRESNEL-BL-v1

Let `S,T` be disjoint original-coordinate sets. The coordinates `X_k` are mutually independent and each density is at most one. Put

\[
U=a\cdot X_S,\qquad H=h\cdot X_S,\qquad V=c\cdot X_T,
\qquad C=\|c\|_2>0.                                                     \tag{4.1}
\]

Let `beta,alpha` be nonzero. Consider

\[
Q=\beta U^2+2\alpha VH+R_T(X_T)+\sum_{i\in S}q_i(X_i),                 \tag{4.2}
\]

where `R_T` is an arbitrary real measurable right-bank function and each `q_i` is an arbitrary real one-coordinate function. (Hence arbitrary right-bank self curvature and arbitrary left diagonal quadratic/affine twists are allowed.)

Let `I subset S`, define `v_i=(a_i,h_i)^T` and

\[
G_I=\sum_{i\in I}v_iv_i^T>0,                                          \tag{4.3}
\]

and suppose

\[
v_i^TG_I^{-1}v_i\le\frac12\qquad(i\in I).                            \tag{4.4}
\]

Then `Q` has a continuous density and

\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{5/3}\,
|\beta|^{-1/3}(|\alpha|C)^{-2/3}\det(G_I)^{-1/3}.}                     \tag{4.5}
\]

No independence between `U` and `H`, or between any rotated spectral coordinates, is assumed.

### Proof

Fix `t != 0`. Insert the standard Gaussian damping in the Fresnel representation of `exp(i t beta U^2)` and remove it at the end exactly as in Lemma 2 / Theorem F of the pinned Claude report. Taking the modulus after the Fresnel step gives

\[
|\phi_Q(t)|
\le (4\pi|\beta t|)^{-1/2}
\int_{\mathbb R}
\left|\mathbb E\exp\left(i\xi U+i2\alpha tVH+i tR_T+i t\sum q_i\right)\right|d\xi.        \tag{4.6}
\]

Condition on the original right bank. For `i in S` put

\[
g_{i,t}(x)=f_i(x)e^{itq_i(x)},\qquad |g_{i,t}|=f_i\le1.                \tag{4.7}
\]

The left expectation factorizes in the ORIGINAL coordinates, so after taking absolute values the right-bank phase disappears:

\[
|\phi_Q(t)|
\le (4\pi|\beta t|)^{-1/2}
\int d\xi\;\mathbb E_T
\prod_{i\in S}\left|\widehat g_{i,t}(a_i\xi+2\alpha t h_iV)\right|.     \tag{4.8}
\]

Because `V=c dot X_T` and `||c||_2=C`, the Rogozin--Ball scalar projection bound gives

\[
\|p_V\|_\infty\le\sqrt2/C.                                            \tag{4.9}
\]

Use (4.9), set `y=2 alpha t V`, and drop factors with `i notin I` (each Fourier transform has modulus at most one):

\[
|\phi_Q(t)|
\le (4\pi|\beta t|)^{-1/2}
\frac{\sqrt2}{2|\alpha t|C}
\int_{\mathbb R^2}\prod_{i\in I}
|\widehat g_{i,t}(a_i\xi+h_i y)|\,d\xi\,dy.                            \tag{4.10}
\]

Set `c_i=v_i^TG_I^{-1}v_i`. After the linear change by `G_I^{1/2}`, the normalized vectors

\[
w_i=G_I^{-1/2}v_i/\sqrt{c_i}
\]

satisf

\[
\sum_i c_iw_iw_i^T=I_2,\qquad \sum_i c_i=2.                            \tag{4.11}
\]

Geometric Brascamp--Lieb therefore yields

\[
\int_{\mathbb R^2}\prod_i|\widehat g_{i,t}(v_i\cdot z)|dz
\le \det(G_I)^{-1/2}
\prod_i\left[c_i^{-1/2}\int|\widehat g_{i,t}(u)|^{1/c_i}du\right]^{c_i}.    \tag{4.12}
\]

Condition (4.4) gives `1/c_i >= 2`. Apply the pinned Claude Lemma 1 to the complex functions (4.7):

\[
\int|\widehat g_{i,t}|^{1/c_i}\le4\pi\sqrt{c_i}.                       \tag{4.13}
\]

The powers of `c_i` cancel exactly in (4.12), and `sum c_i=2`, giving

\[
\int_{\mathbb R^2}\prod_i|\widehat g_{i,t}(v_i\cdot z)|dz
\le(4\pi)^2\det(G_I)^{-1/2}.                                           \tag{4.14}
\]

Combining (4.10) and (4.14),

\[
|\phi_Q(t)|\le\min\{1,K|t|^{-3/2}\},                                  \tag{4.15}
\]

where

\[
K=4\sqrt2\,\pi^{3/2}|\beta|^{-1/2}(|\alpha|C)^{-1}\det(G_I)^{-1/2}.    \tag{4.16}
\]

Finally

\[
\frac1{2\pi}\int_{\mathbb R}\min(1,K|t|^{-3/2})dt
=\frac{3}{\pi}K^{2/3},                                                   \tag{4.17}
\]

which is exactly (4.5). In particular `phi_Q` is integrable, so Fourier inversion gives a continuous density. QED.

### Mechanism: where the third direction enters

The right scalar `V` gives a full `|t|^{-1}` after the change `y=2 alpha t V`; that is the rank-two borderline and corresponds to the logarithmic product singularity. Fresnel linearization of the genuinely third quadratic direction `beta U^2` contributes the missing `|t|^{-1/2}`. The two-dimensional Brascamp--Lieb step keeps the possibly strong dependence of `U,H` generated by their shared ORIGINAL source coordinates. Thus the final `|t|^{-3/2}` is obtained without ever declaring the spectral coordinates independent.

## 5. Application to the exact partner null endpoint

Apply Theorem 4.1 to (3.4), taking

`R_T=2 alpha V L`, `C=||c||_2=1`, and `I=S`.

By determinant-one shear invariance, the normalized left-bank leverages are exactly (3.5), and `det G_S=rho`. Therefore, if

\[
\max_{i\in S}(a_i^2+b_i^2/\rho)\le1/2,                                 \tag{5.1}
\]

then Lemma 2.1 and Theorem 4.1 give

\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{5/3}\rho^{-1/3}s^{-1}.}                                      \tag{5.2}
\]

At the r29/r30 balance scale `rho>=1/1024=2^{-10}`,

\[
\boxed{\|p_Q\|_\infty\le96/s.}                                        \tag{5.3}
\]

This is a genuine extension beyond the ordinary three-mode low-leverage Fresnel gate: the right bank may contain a leverage-one physical coordinate, and `R_T` is arbitrary.

## 6. What failure of the new compiler looks like

### Proposition 6.1 — finite shared-spike reduction

Suppose (5.1) fails. For an offending row set

\[
\ell_i=a_i^2+b_i^2/\rho>1/2.                                            \tag{6.1}
\]

If `a_i^2>=1/4`, then the exact-rank-three scalar-pivot theorem from the orientation-free rank-two fusion source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

pays the entire form by

\[
\|p_Q\|_\infty\le256/s.                                                 \tag{6.2}
\]

Indeed the physical row norm `c_i=a_i^2+b_i^2>=1/4`, the physical diagonal is

\[
A_{ii}=r_i^TMr_i=\beta a_i^2,
\]

so `|A_ii|>=s/4`, while `|det M|>=s^3`; hence

\[
128[c_i|A_{ii}||\det M|]^{-1/4}\le128[(1/4)(s/4)s^3]^{-1/4}=256/s.
\]

Consequently, after excluding this already-paid scalar-pivot exit, every row violating (5.1) obeys

\[
a_i^2<1/4,\qquad b_i^2>\rho/4.                                         \tag{6.3}
\]

Since `sum_{i in S}b_i^2=rho`, there are at most three such rows. Thus the only square-bank obstruction left by the new compiler is a **finite (at most three) shared-direction spike set**; the diffuse part is no longer the unpaid mechanism.

This proposition does not yet prove that conditioning/deleting those spikes is harmless. In fact small quadratic coefficients cannot be discarded perturbatively for unbounded supports. The next bridge has to use the spike variables jointly with the remaining product frame.

## 7. A target-valid family not covered by the ordinary all-row leverage gate

Take six original coordinates and the Parseval frame with rows

\[
\begin{aligned}
r_1&=(1/2,1/(2\sqrt2),0),&r_2&=(1/2,1/(2\sqrt2),0),\\
r_3&=(1/2,-1/(2\sqrt2),0),&r_4&=(1/2,-1/(2\sqrt2),0),\\
r_5&=(0,0,1),&r_6&=(0,1/\sqrt2,0).
\end{aligned}                                                           \tag{7.1}
\]

Then `R^TR=I_3`, `rho=1/2`, the four left normalized planar leverages are exactly `1/2`, but the fifth full spectral row has leverage one. With

\[
M=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},                    \tag{7.2}
\]

the nonzero spectrum of `A=RMR^T` is exactly `{1,1,-1}`. In physical variables,

\[
U=(X_1+X_2+X_3+X_4)/2,
\]

\[
Z=(X_1+X_2-X_3-X_4)/(2\sqrt2),\qquad V=X_5,\qquad W=X_6/\sqrt2,
\]

and

\[
Q=U^2+2V(Z+W).                                                          \tag{7.3}
\]

The ordinary all-three-mode low-leverage hypothesis fails because `||r_5||^2=1`; nevertheless Theorem 4.1 gives, exactly,

\[
\boxed{\|p_Q\|_\infty\le12}                                            \tag{7.4}
\]

for every independent cap-one input law.

This family also retains the mandatory rank-two logarithmic control in the same geometry. Remove the square `U^2`. For centered unit uniforms, `V=X_5` is independent of `Y=Z+X_6/sqrt2`, and the density of `Y` is positive in a neighborhood of zero. Therefore the product `2VY` has a logarithmic divergence at zero. In the canonical two-uniform case one has exactly

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad0<|t|<1/2.                            \tag{7.5}
\]

Restoring `U^2` removes the divergence by the `|t|^{-1/2}` Fresnel gain in Theorem 4.1, even though `U` and `Z` share the same four original coordinates and are generally dependent. This is precisely the non-rotation-independence mechanism sought by B11.

## 8. Sign-specific ruled side from the pinned source

Lemma 2.1 gives the signature directly. Apply the completed ruled Theorem C in the required pinned `COUNTEREXAMPLE_SEARCH.md` after diagonalizing `M` only for geometry, not for probabilistic independence.

If `beta>0`, `M` has signature `(+,+,-)` and all three eigenvalue magnitudes are at least `s`, so on the majority one-sheet side

\[
\boxed{p_Q(t)\le\pi\sqrt2/s\qquad(t\ge0).}                              \tag{8.1}
\]

If `beta<0`, apply the same theorem to `-Q`; then

\[
\boxed{p_Q(t)\le\pi\sqrt2/s\qquad(t\le0).}                              \tag{8.2}
\]

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids extending (8.1)-(8.2) to the opposite side from X-ray control alone. Theorem 4.1 is instead global in its diffuse square-bank chamber and therefore pays that two-sheet side there by a different, product-preserving mechanism.

## 9. Exact remaining implication

The full conjecture is not proved. In the exact r29/r30 null-sum endpoint, the new work reduces the unpaid square-bank geometry to the following finite-spike chamber:

* `|alpha|,|beta|>=s` and the sign is already fixed by `beta`;
* the one-sheet side is paid by the pinned ruled theorem;
* if the square-side planar frame has normalized leverage at most `1/2`, the global density is `<=96/s` at the partner balance scale;
* if a violating row has `a_i^2>=1/4`, the scalar-pivot theorem pays it by `<=256/s`;
* otherwise every violating row carries `b_i^2>rho/4`, hence there are at most three such shared-direction spikes.

The first unpaid implication is therefore:

`QFORM-NULLSUM-FINITE-SHARED-SPIKE-v1` — use the at-most-three square-bank shared spikes jointly with the residual original-product frame to obtain a uniform two-sheet bound, or force an already-paid physical-pair/disjoint-volume/hub certificate. One may not delete their small outer coefficients perturbatively, replace the bank by an arbitrary planar joint density, or use post-rotation independence.

Arbitrary additional nonseparable spectrum beyond this exact-rank-three endpoint remains a separate full-QFORM bridge.
