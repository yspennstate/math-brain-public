# account01/B11 — rank-one residual compiler for the indefinite null-sum finite-spike chamber

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B11`  
Run: `20260923T131327Z-account01-B11-QFORM-auto11`

**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`.

The result below closes the exact rank-one residual endpoint of the finite-shared-spike chamber isolated by the designated partner account02/B11. It does **not** solve the full conjecture. It proves an essentially bounded density in the stated branch; continuity is not claimed.

## 1. Source-pinned starting point


The designated partner source is

`yspennstate/math-open-problems@34246a856445b2159c10dc138dda513b5e3b1bea`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T124731Z-account02-B11-QFORM-r31/REPORT.md`.

Its exact null-sum endpoint has

\[
M=\begin{pmatrix}\beta&0&\gamma\\0&0&\alpha\\\gamma&\alpha&\delta\end{pmatrix},
\qquad \sigma_{\min}(M)\ge s>0,
\]

and disjoint ORIGINAL-coordinate banks `S,T` with rows

\[
r_i=(a_i,b_i,0),\quad i\in S,
\qquad r_j=(0,d_j,c_j),\quad j\in T,
\]

whose Gram matrices are

\[
\sum_{i\in S}r_ir_i^T=\operatorname{diag}(1,\rho,0),\qquad
\sum_{j\in T}r_jr_j^T=\operatorname{diag}(0,1-\rho,1),
\]

with

\[
\rho,1-\rho\ge 2^{-10}.
\]

The partner proves exactly

\[
|\alpha|,|\beta|\ge s.
\]

After the determinant-one shears

\[
H=Z+(\gamma/\alpha)U,\qquad
L=W+(\delta/(2\alpha))V,
\]

the full form is

\[
\boxed{Q=\beta U^2+2\alpha V(H+L)}. \tag{1.1}
\]

The left normalized leverage is invariant under this shear:

\[
\ell_i=a_i^2+b_i^2/\rho.
\]

Partner Theorem `QFORM-ONESIDED-NULLSUM-FRESNEL-BL-v1` gives a continuous density and

\[
\|p_Q\|_\infty\le 3\,2^{5/3}|\beta|^{-1/3}|\alpha|^{-2/3}\det(G_I)^{-1/3} \tag{1.2}
\]

whenever a left subset `I` has positive two-dimensional Gram `G_I` and all its internal leverages are at most `1/2`. In particular, if all full-left leverages are at most `1/2`, then

\[
\boxed{\|p_Q\|_\infty\le 96/s}. \tag{1.3}
\]

If (1.3) fails and an offending row has `a_i^2>=1/4`, the partner pays the whole form by the existing scalar-pivot theorem with `256/s`. Thus in the only unpaid partner branch the offending set

\[
E=\{i\in S:\ell_i>1/2\}
\]

has at most three elements and every `i in E` satisfies

\[
a_i^2<1/4,\qquad b_i^2>\rho/4. \tag{1.4}
\]

The canonical rank-two fractional-potential input used below is `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`,

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

which states that for an orthonormal two-dimensional projection and any invertible symmetric `Lambda`, with `D=|det Lambda|`, arbitrary affine perturbations satisfy

\[
\sup_w\mathbb E|R-w|^{-1/2}\le128D^{-1/4}. \tag{1.5}
\]

No independence of the two projected coordinates is assumed in (1.5).

## 2. New endpoint theorem

### Theorem 2.1 — `QFORM-NULLSUM-RANKONE-RESIDUAL-COMPILER-v1`

Assume the exact partner geometry above and the unpaid finite-spike branch (1.4). Put `R=S\setminus E`. Suppose the sheared residual left coefficient vectors

\[
v_i=(a_i,h_i),\qquad h_i=b_i+(\gamma/\alpha)a_i,\quad i\in R,
\]

span a one-dimensional subspace. Then, for every independent cap-one product input law,

\[
\boxed{\|p_Q\|_\infty\le 2048/s}. \tag{2.1}
\]

The same theorem applies to signatures `(+,+,-)` and `(+,-,-)`; the sign of `beta` changes but the argument is sign-free after absolute values.

### Proof

Because `|E|<=3` and every exceptional coordinate satisfies `a_i^2<1/4`, while `sum_{i in S}a_i^2=1`, the residual square-direction mass obeys

\[
A^2:=\sum_{i\in R}a_i^2>1-3/4=1/4. \tag{2.2}
\]

The rank-one assumption and `A>0` imply that there is a real `theta` such that

\[
h_i=\theta a_i\qquad(i\in R). \tag{2.3}
\]

Define the normalized ORIGINAL-bank projection

\[
Y=A^{-1}\sum_{i\in R}a_iX_i.
\]

It uses only coordinates in `R`, so it is independent of the right bank `T` and of the finite exceptional coordinates `E`. The coefficient vector has Euclidean norm one, hence the scalar Rogozin--Ball projection bound gives

\[
\|p_Y\|_\infty\le\sqrt2. \tag{2.4}
\]

Condition now on the exceptional ORIGINAL coordinates `X_E`. They contribute deterministic numbers `u,h`. Equations (1.1),(2.3) become

\[
Q=\beta(u+AY)^2+2\alpha V(h+\theta AY+L). \tag{2.5}
\]

Complete the square in the still-independent scalar `Y`. With

\[
d=\beta A^2,\qquad
m={u\over A}+{\alpha\theta\over\beta A}V,
\]

we have the exact identity

\[
Q=d(Y+m)^2+R_T, \tag{2.6}
\]

where

\[
R_T=2\alpha VL+2\alpha(h-\theta u)V-{\alpha^2\theta^2\over\beta}V^2. \tag{2.7}
\]

The crucial point is that **all** dependence on the exceptional values has moved into an affine term of the right-bank receiver; no exceptional coordinate was deleted or bounded in magnitude.

In the right projected coordinates `(V,L)`, the quadratic matrix in (2.7) is

\[
N=\begin{pmatrix}
-\alpha^2\theta^2/\beta&\alpha\\
\alpha&0
\end{pmatrix},
\qquad
\boxed{\det N=-\alpha^2}. \tag{2.8}
\]

Let `C` be the original-coordinate coefficient matrix of `(V,L)` and `G_T=C^TC`. The shear defining `L` has determinant one, while the unsheared right Gram determinant is `1-rho`; therefore

\[
\det G_T=1-\rho. \tag{2.9}
\]

Whiten only for deterministic algebra: `C=O G_T^{1/2}` with `O^TO=I_2`. This does **not** assert independence of the whitened coordinates. The rank-two spectral matrix is

\[
\Lambda=G_T^{1/2}NG_T^{1/2},
\]
so by (2.8)-(2.9)

\[
\boxed{|\det\Lambda|=\alpha^2(1-\rho)}. \tag{2.10}
\]

The affine term in (2.7) is arbitrary and is explicitly allowed by (1.5). Hence, uniformly in the conditioned exceptional values,

\[
\sup_t\mathbb E_T|R_T-t|^{-1/2}
\le128|\alpha|^{-1/2}(1-\rho)^{-1/4}. \tag{2.11}
\]

For fixed right-bank coordinates, `m` in (2.6) is deterministic. If a scalar random variable has density cap `L_0`, then for every shift `m` the pushforward of `d(Y+m)^2` satisfies

\[
p_{d(Y+m)^2}(z)\le L_0|d|^{-1/2}|z|^{-1/2} \tag{2.12}
\]

(on the appropriate half-line, and zero on the other one). Using (2.4), conditioning on `T`, and then averaging,

\[
p_{Q\mid X_E}(t)
\le\sqrt2\,|d|^{-1/2}\mathbb E_T|t-R_T|^{-1/2}. \tag{2.13}
\]

Now (2.2), `|beta|>=s`, `|alpha|>=s`, and `1-rho>=2^{-10}` give

\[
|d|^{-1/2}\le2s^{-1/2},
\qquad
|\alpha|^{-1/2}(1-\rho)^{-1/4}
\le4\sqrt2\,s^{-1/2}. \tag{2.14}
\]

Combining (2.11)-(2.14),

\[
\|p_{Q\mid X_E}\|_\infty
\le \sqrt2\cdot2\cdot128\cdot4\sqrt2\,s^{-1}
=2048/s. \tag{2.15}
\]

The estimate is uniform in `X_E`; averaging over `X_E` proves (2.1). QED.

## 3. Why this is product-safe

The only probabilistic independence used is independence of **disjoint original-coordinate banks**: `Y` uses `R`, the conditioned spikes use `E`, and `(V,L)` uses `T`. The deterministic whitening in (2.10) is used solely to identify the rank-two spectral determinant required by the already-proved affine half-Riesz theorem; no whitened coordinate is declared independent.

The translation `m` in (2.6) depends on `V`. We do not call `Y+m` independent of the receiver. Instead, we use the conditional square-density bound (2.12), which is uniform in every deterministic shift. This explicitly respects the live correction that a conditional density cap is not independence.

## 4. Application of the designated partner theorem to an actual inequality

The same exact null-sum chamber now has the following paid alternatives before the new endpoint is needed.

If

\[
\max_{i\in S}(a_i^2+b_i^2/\rho)\le1/2,
\]
then partner account02/B11 Theorem 4.1 applied with `I=S`, `C=1`, and `det G_S=rho` gives

\[
\|p_Q\|_\infty
\le3\,2^{5/3}\rho^{-1/3}s^{-1}
\le\boxed{96/s}, \tag{4.1}
\]

and this branch has a continuous `C_0` density. If the gate fails but some offending row has `a_i^2>=1/4`, the partner's scalar-pivot calculation gives `256/s`. Otherwise at most three shared-direction spikes remain; Theorem 2.1 now pays the exact rank-one residual endpoint of that branch by `2048/s`.

Thus `QFORM-NULLSUM-FINITE-SHARED-SPIKE-v1` has been strictly reduced: the residual rank-one endpoint is no longer open. The remaining case is a residual left frame of **positive but potentially arbitrarily small two-dimensional Gram determinant** after the at-most-three spikes are isolated.

## 5. Exact wedge bookkeeping for the remaining positive-area branch

There is a useful identity that prevents the remaining obstruction from being described vaguely. Let

\[
G_R=\sum_{r\in R}v_rv_r^T,
\qquad v_i=(a_i,h_i).
\]

Because the shear has determinant one, the full left Gram determinant is `rho`. Cauchy--Binet in dimension two gives the exact decomposition

\[
\boxed{
\rho
=\det G_R
+\sum_{e\in E}\sum_{r\in R}\det(v_e,v_r)^2
+\sum_{\{e,e'\}\subset E}\det(v_e,v_{e'})^2.} \tag{5.1}
\]

Since `|E|<=3`, if `det G_R<=rho/2`, then at least one of the at most six grouped finite-spike wedge contributions in (5.1) is at least `rho/12`. Therefore the near-rank-one transition is not an absence of transverse volume: either the residual bank itself carries at least `rho/2` area, or a dimension-free finite spike-to-bank / spike-to-spike wedge carries at least `rho/12`.

This identity is algebraic only; it is **not** being promoted to a density theorem. It identifies the next product-preserving mechanism that must be paid.

## 6. Rank-two logarithmic control and the role of the third direction

The mandatory obstruction remains genuine. For independent centered unit uniforms,

\[
p_{2XY}(t)=\log{1\over2|t|},\qquad0<|t|<1/2.
\]

In the present endpoint, after the residual bank collapses to one ray, the rank-two right receiver (2.7) can still have precisely this indefinite logarithmic behavior. The third direction does not make that receiver bounded. Instead, the independent residual square `d(Y+m)^2` contributes the half-order kernel `|z|^{-1/2}`, while the completed rank-two theorem says that the receiver has a uniformly finite half-Riesz potential. Their composition in (2.13) is bounded. This is the exact smoothing mechanism in the rank-one residual chamber.

## 7. What remains open

The full conjecture is still OPEN. The first B11 implication left after this run is

`QFORM-NULLSUM-NEAR-RANKONE-FINITE-WEDGE-COMPILER-v1`:

> In the partner finite-spike chamber, with at most three exceptional original coordinates and residual Gram determinant strictly positive but possibly arbitrarily small, use the exact wedge alternative (5.1) jointly with the original-coordinate product structure to obtain a uniform density bound, or force an already-paid physical-pair / one-sided Fresnel-BL / volume / scalar-pivot exit. No perturbative deletion of the small transverse coefficients is allowed.

Continuity is proved in the partner low-leverage branch (4.1), but **not** by Theorem 2.1. Global continuity remains open.

## 8. Verification notes

Symbolic verification used the exact identities

\[
\beta(u+AY)^2+2\alpha V(h+\theta AY+L)-\beta A^2(Y+m)^2
=2\alpha VL+2\alpha(h-\theta u)V-(\alpha^2\theta^2/\beta)V^2
\]

with `m=u/A+alpha theta V/(beta A)`, and

\[
\det\begin{pmatrix}-\alpha^2\theta^2/\beta&\alpha\\\alpha&0\end{pmatrix}=-\alpha^2.
\]

The endpoint constant evaluates exactly to `2048` at `1-rho=2^-10`.
