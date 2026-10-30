# B03 improvement: split-row decoupling and the order-four endpoint

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T134617Z-fleet01-B03-fixed-multiplicity-audit-r12`  
Baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new rigorous supporting theorems; no unconditional reduction of the fixed-multiplicity threshold below 17 is claimed.**

The previous B03 run showed that changing only the global leverage-free Jensen/copy power cannot improve the manuscript's order-four `|t|^{-1}` endpoint. This run changes mechanism: instead of forcing all physical row factors through one graph determinant, it splits them into two disjoint packets and performs Cauchy--Schwarz while retaining their common difference environment. This can add crossing orders even when the packets use the same column coordinates and are therefore maximally dependent through that environment.

## 1. A graph integral extracted from the baseline proof

Let `D=(D_j)` have independent probability densities `g_j<=1`, let `N` be a real matrix with rows `n_i^T`, and let `f_i` be probability densities bounded by one. For every real `t`,

\[
\boxed{
 \mathbb E_D\prod_i
 |\widehat f_i(2t(ND)_i)|^2
 \le
 \det\left(I+\frac{t^2}{\pi^2e^2}N^TN\right)^{-1/2}.
}
\tag{1}
\]

This is exactly the pre-fourth-root graph integral in the proof of the baseline regularized crossing determinant theorem, but it is useful to isolate it. For completeness: put `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2N^TN`, use the geometric frame with weights

\[
c_j=\alpha e_j^TH^{-1}e_j,
\qquad d_i=a^2n_i^TH^{-1}n_i,
\]

apply the baseline geometric rank-one inequality, use `||g_j||_{1/c_j}<=1`, and use the scalar Fourier-power estimate at exponent `2/d_i`. The `d_i` Jacobian powers cancel, the `c_j` entropy is at most `e^{theta/2}`, and the choice of `alpha` cancels the remaining scalar multiplier. This leaves (1).

## 2. Split-row shared-environment determinant theorem

Consider the full baseline cross form

\[
 Z=F(X_I)+2X_I^TMX_J+G(X_J),
\tag{2}
\]

where `I,J` are disjoint original-coordinate banks, all coordinates are independent with densities bounded by one, and `F,G` are arbitrary measurable real functions finite almost surely.

Let `I_1,I_2` be disjoint subsets of `I`; they need not exhaust `I`. Let `M_1,M_2` be the corresponding row submatrices of `M`. Then for every real `t`,

\[
\boxed{
 |\phi_Z(t)|
 \le
 \prod_{g=1}^2
 \det\left(I+\frac{t^2}{\pi^2e^2}M_g^TM_g\right)^{-1/8}.
}
\tag{3}
\]

### Proof

The baseline two-power decoupling inequality gives, with `D=X_J-X'_J`,

\[
 |\phi_Z(t)|^2
 \le
 \mathbb E_D\prod_{i\in I}
 |\widehat f_i(2t(MD)_i)|.
\tag{4}
\]

Every Fourier factor has modulus at most one. Dropping rows outside `I_1 union I_2` can only increase the right side. Put

\[
 A_g(D)=\prod_{i\in I_g}
 |\widehat f_i(2t(MD)_i)|.
\]

The two packets are not declared independent: both remain functions of the **same** difference vector `D`. Cauchy--Schwarz in this common product law gives

\[
 |\phi_Z(t)|^2
 \le
 (\mathbb E A_1(D)^2)^{1/2}
 (\mathbb E A_2(D)^2)^{1/2}.
\tag{5}
\]

Apply (1) separately to the two expectations, with `N=M_1` and `N=M_2`:

\[
 \mathbb E A_g(D)^2
 \le
 \det\left(I+\frac{t^2}{\pi^2e^2}M_g^TM_g\right)^{-1/2}.
\]

Insert these bounds in (5) and take a square root. This proves (3).

No conditional law of one slope packet given the other is formed. In particular, the proof does not infer a conditional density cap from a marginal density cap, and it does not conditionally recap `X_j-X'_j` after revealing `X_j+X'_j`.

By interchanging the roles of `I` and `J` before the decoupling step, the identical statement holds for two disjoint **column** packets.

## 3. Crossing-volume consequence

For `g=1,2`, suppose `Z_{k_g}(M_g)>0` and put

\[
 K_*=k_1+k_2.
\]

Retaining the order-`k_g` term in each determinant in (3) gives

\[
\boxed{
 |\phi_Z(t)|
 \le
 \min\left\{1,
 \left(\frac{a_*}{|t|}\right)^{K_*/4}
 \right\},
}
\tag{6}
\]

where

\[
\boxed{
 a_*=\pi e
 \left[Z_{k_1}(M_1)Z_{k_2}(M_2)\right]^{-1/(2K_*)}.
}
\tag{7}
\]

If `K_*>4`, absolute Fourier inversion is therefore available and the baseline power-envelope lemma yields

\[
\boxed{
 \|p_Z\|_\infty
 \le
 e\,\frac{K_*}{K_*-4}
 \left[Z_{k_1}(M_1)Z_{k_2}(M_2)\right]^{-1/(2K_*)}.
}
\tag{8}
\]

The density in this branch is continuous and vanishes at infinity.

The critical `1+4` split is

\[
\boxed{
 \|p_Z\|_\infty
 \le
 5e\,[Z_1(M_1)Z_4(M_2)]^{-1/10}.
}
\tag{9}
\]

For a singleton physical row `i`, `Z_1(M_1)=||m_i||_2^2`. Thus any cut for which

\[
 ||m_i||_2^2\,Z_4(M_{I\setminus\{i\},J})>0
\]

has a dependence-safe order-five receiver even if the two packets use exactly the same column bank. A quantitative lower bound `>=tau^10` gives `||p_Z||_infinity<=5e/tau`.

This is genuinely different from merely changing the global Jensen exponent. The preceding B03 power-barrier theorem applies when all rows are paid through one determinant. Here two disjoint original-coordinate row packets contribute separate graph determinants before they are recombined.

## 4. Unconditional order-four endpoint: `L^r` densities

The split theorem above does not by itself force a dimension-free packet product from the aggregate order-four volume. There is nevertheless a useful unconditional endpoint statement that makes the remaining `17 -> 13` analytic gap exact.

Assume only that a cross form (2) has

\[
 Z_4(M)>0.
\]

The baseline order-four volume envelope is

\[
 |\phi_Z(t)|\le\min\{1,U/|t|\},
 \qquad
 U=\pi e\,Z_4(M)^{-1/8}.
\tag{10}
\]

For every `1<p<=2`, direct integration gives

\[
 \|\phi_Z\|_p^p
 \le
 2U+2U^p\int_U^\infty t^{-p}\,dt
 =2U\frac{p}{p-1}.
\tag{11}
\]

Let

\[
 r=\frac{p}{p-1}\in[2,\infty).
\]

With the manuscript Fourier convention, inverse Hausdorff--Young has norm `(2*pi)^(-1/p)` from `L^p(dt)` to `L^r(dx)`. To avoid assuming a density in advance, convolve the law with the manuscript Gaussian `g_epsilon`. Its Fourier transform is `phi_Z(t)e^{-epsilon t^2}`. These transforms converge to `phi_Z` in `L^p`, hence their inverse transforms converge in `L^r` to a function `p`. At the same time the Gaussian convolutions converge weakly to the law of `Z`; therefore that law is `p(x)dx`. Combining (11) with Hausdorff--Young gives

\[
\boxed{
 \|p_Z\|_r
 \le
 \left(\frac{Ur}{\pi}\right)^{1-1/r}
 =
 \left(e r\,Z_4(M)^{-1/8}\right)^{1-1/r}.
}
\tag{12}
\]

Consequently every interval `J` satisfies

\[
\boxed{
 \mathbb P\{Z\in J\}
 \le
 \left(e r\,Z_4(M)^{-1/8}|J|\right)^{1-1/r},
 \qquad r\ge2.
}
\tag{13}
\]

This is an actual absolute-continuity theorem at order four, but it is not an `L^infinity` theorem because the bound grows with `r`.

## 5. Concrete no-pivot `s_13` consequence

Under the normalized manuscript hypotheses `K=s=1`, no `eta`-pivot and

\[
s_{13}(A)\ge1,
\]

the audited spectral-to-volume proposition with `k=4` and the random physical cut produce a cut with

\[
 Z_4(A_{I,J})^{-1/8}\le160.
\tag{14}
\]

Hence (12)--(13) give, for every `r>=2`,

\[
\boxed{
 \|p_Q\|_r\le(160er)^{1-1/r},
}
\tag{15}
\]

and

\[
\boxed{
 \mathbb P\{Q\in J\}
 \le(160er|J|)^{1-1/r}.
}
\tag{16}
\]

For very small intervals this is near-linear. Put `delta=160e|J|`. If `delta<=e^{-2}` and choose

\[
 r=\log(1/\delta)\ge2,
\]

then

\[
 (\delta r)^{1-1/r}
 =\delta r\,(\delta r)^{-1/r}
 =e\,\delta r\,r^{-1/r}
 \le e\,\delta r.
\]

Therefore

\[
\boxed{
 \mathbb P\{Q\in J\}
 \le
 160e^2|J|\log\frac1{160e|J|}
}
\tag{17}
\]

whenever

\[
 |J|\le e^{-3}/160\approx3.11169\times10^{-4}.
\]

This quantifies exactly what the leverage-free order-four endpoint gives without pretending that a logarithmic loss is a bounded density.

## 6. Relation to the current thirteen-direction frontier

A separate completed fleet01/B04 result proves a genuine `L^infinity` order-four theorem whenever the volume-producing physical cut has a fixed maximum-row-leverage gap below one. The present split theorem is complementary: it can produce an integrable exponent by dividing the actual original-coordinate rows into two packets while keeping their common difference environment coupled. In particular it supplies (9) whenever a singleton row and the remaining rows carry a quantitative `1+4` product.

What remains missing for an **unconditional** thirteen-eigenvalue theorem is a dimension-free implication from the structural data guaranteed by `s_13` and no pivot—currently an aggregate lower bound on `Z_4`—to either:

1. a leverage gap on a volume-good cut;
2. a quantitative split product such as `Z_1(M_1)Z_4(M_2)`;
3. a different endpoint receiver that removes the logarithmic loss in (17).

The aggregate `Z_4` lower bound alone does not presently provide any one of these with a universal constant. Therefore the unconditional theorem remains at multiplicity **17** after this run. The result (15)--(17) is not advertised as a threshold reduction.

## 7. Constant checks

For the normalized no-pivot `s_13` application,

\[
U\le160\pi e=1366.3574756277706\ldots.
\]

The `K_*=5` split coefficient in (8) is

\[
5e=13.591409142295225\ldots.
\]

At `delta=e^{-2}`, the optimized endpoint choice is `r=2`; the exact bound `(delta r)^{1-1/r}` is below the simpler majorant `e delta r`, as required. These numerical values are only checks of the displayed exact formulas, not proof substitutes.
