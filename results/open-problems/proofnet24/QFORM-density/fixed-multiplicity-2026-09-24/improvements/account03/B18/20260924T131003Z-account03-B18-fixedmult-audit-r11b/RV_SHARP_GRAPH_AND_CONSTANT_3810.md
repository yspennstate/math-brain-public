# account03/B18 r11b — source-sharp graph determinant and 3810 theorem constant

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T131003Z-account03-B18-fixedmult-audit-r11b`  
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved same-scope improvement; multiplicity remains 17.** The unrestricted three-eigenvalue conjecture remains open.

## 1. Primary-source input

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions* (arXiv:1402.4492), Theorem 1.2, proves the sharp one-dimensional statement: if independent real variables have densities bounded by `K` and `sum a_i^2=1`, then the density of `sum a_i X_i` is bounded by `sqrt(2) K`. No moment, centering, iid, log-concavity, support, or smoothness assumption is present.

For a cap-one density `f`, Fourier convention `fhat(t)=int exp(i t x) f(x) dx`, and every `p>=2`, this implies

\[
\boxed{\int_{\mathbb R}|\widehat f(t)|^p\,dt\le {4\pi\over\sqrt p}.}\tag{1}
\]

Indeed, let `m=floor(p/2)`. Since `|fhat|<=1`,

\[
\int|\widehat f|^p\le\int|\widehat f|^{2m}
 =2\pi\,p_{\sum_{r=1}^m(X_r-X'_r)}(0).
\]

Normalize the `2m` coefficients `(+1,-1,...,+1,-1)` by `sqrt(2m)`. RV Theorem 1.2 gives density at most `sqrt(2)` for the normalized sum, hence at most `1/sqrt(m)` for the unnormalized sum. Since `m>=p/4`, (1) follows.

This is the same source-valid scalar transfer recorded in the preceding B18 review; the new work below propagates it through the graph determinant and the manuscript's quarter-power/pivot chain.

## 2. Sharpened regularized crossing determinant

Let

\[
Z=F(X_I)+2X_I^T M X_J+G(X_J),
\]

where `I,J` are disjoint banks of original independent cap-one coordinates and `F,G` are arbitrary measurable real functions. Then

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+{t^2\over2\pi^2e}M^TM\right)^{-1/8}.
}\tag{2}
\]

Proof. Use the manuscript's fourth-power decoupling. With `a=2t`, `D=X_J-X'_J`, and density `g_j<=1`,

\[
|\phi_Z(t)|^4\le
\int \prod_j g_j(x_j)\prod_i |\widehat f_i(a m_i\cdot x)|^2\,dx.
\]

For `alpha>0` set

\[
H=\alpha I+a^2M^TM,
\quad c_j=\alpha e_j^TH^{-1}e_j,
\quad d_i=a^2m_i^TH^{-1}m_i.
\]

The manuscript proves that the associated graph vectors form a Parseval frame and that
`theta=sum_i d_i=sum_j(1-c_j)`. Apply geometric Brascamp--Lieb after `x=H^{-1/2}z`. The coordinate factors contribute at most

\[
\alpha^{c_j/2}c_j^{-c_j/2},
\]

and (1), with `p=2/d_i>=2`, gives

\[
\left(\int|\widehat f_i|^{2/d_i}\right)^{d_i}
\le (2\sqrt2\pi\sqrt{d_i})^{d_i}.
\]

The BL scaling `d_i^{-d_i/2}` cancels the power of `d_i`. The entropy inequality used in the manuscript gives

\[
\prod_j c_j^{-c_j/2}\le e^{\theta/2}.
\]

After extracting `det(H)^{-1/2}` and the alpha powers, the entire nondeterminant factor is

\[
\left({2\sqrt2\pi\sqrt e\over\sqrt\alpha}\right)^\theta.
\]

Set `alpha=8 pi^2 e`. Then this factor is one and

\[
|\phi_Z(t)|^4\le
\det\!\left(I+{t^2\over2\pi^2e}M^TM\right)^{-1/2},
\]

which proves (2).

This improves the pinned manuscript coefficient `1/(pi^2 e^2)` to `1/(2 pi^2 e)` with the same exponent and hypotheses.

## 3. Fractional graph version and the order-four endpoint

The same calculation also sharpens account01/B06's new fractional graph determinant. Let

\[
\ell_i=m_i^T(M^TM)^+m_i
\]

be row leverage. Fix `q in [1,2]` and suppose `max_i ell_i<=q/2`. Then Jensen applied to the two-power decoupling and (1) at exponent `q/d_i` give

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+{q t^2\over4\pi^2e}M^TM\right)^{-1/(4q)}.
}\tag{3}
\]

The leverage hypothesis is used only to ensure `q/d_i>=2`. If the order-`k` crossing volume `Z_k(M)` is positive, retaining that determinant coefficient gives

\[
|\phi_Z(t)|\le \min\left\{1,\left({u\over|t|}\right)^{k/(2q)}\right\},
\quad
u=2\pi\sqrt{e/q}\,Z_k(M)^{-1/(2k)}.
\]

Therefore, whenever `k>2q`, Fourier inversion yields

\[
\boxed{
\|p_Z\|_\infty
\le
2\sqrt{e/q}\,{k\over k-2q}\,Z_k(M)^{-1/(2k)}.
}\tag{4}
\]

For `k=4` and `max ell_i<=3/4`, take `q=3/2`:

\[
\boxed{
\|p_Z\|_\infty
\le 8\sqrt{2e/3}\,Z_4(M)^{-1/8}.
}\tag{5}
\]

In the manuscript's `s_13(A)>=1` no-pivot algebra, a random-cut witness has
`Z_4(M)>=4^{-4} kappa^4`, `kappa=1/80^2`, hence `Z_4(M)^{-1/8}<=160`. Under the same leverage gate,

\[
\boxed{
\|p_Z\|_\infty
\le1280\sqrt{2e/3}<1724.
}\tag{6}
\]

More generally, if `max ell_i<=1-delta` with `0<delta<=1/2`, choose `q=2(1-delta)` to obtain

\[
\boxed{
\|p_Z\|_\infty
\le {\sqrt{2e/(1-\delta)}\over\delta}\,Z_4(M)^{-1/8}.
}\tag{7}
\]

Thus the analytic order-four obstruction is localized exactly to cuts whose maximum row leverage approaches one. This does **not** prove a universal `s_13` theorem: the existing random-cut argument does not supply a dimension-free leverage gap for the same large-`Z_4` witness. Account01/B08 and account02/B08 also give exact no-pivot examples showing that the manuscript's `rank R<=3r` and `rank R[L,L]<=r` completion bounds are simultaneously sharp, so a purely algebraic rank retuning does not close this branch.

## 4. Sharpened quarter-power small-ball constant

The manuscript's quarter-power lemma starts from a cross cut with `||M||>=L/4`. From (2), retaining one singular factor gives

\[
|\phi_R(t)|
\le
\left({4\sqrt2\pi\sqrt e\over L|t|}\right)^{1/4}.
\tag{8}
\]

For any `rho>0`, Gaussian smoothing with parameter `v>0` gives

\[
\Pr\{|R-a|<\rho\}
\le {e^v\rho\over2\sqrt{\pi v}}
\int e^{-\rho^2t^2/(4v)}|\phi_R(t)|\,dt.
\]

Substitute (8) and use

\[
\int_{\mathbb R}e^{-u t^2}|t|^{-1/4}dt=u^{-3/8}\Gamma(3/8).
\]

The factor `e^v v^{-1/8}` is minimized at `v=1/8`. Hence

\[
\boxed{
\Pr\{|R-a|<\rho\}
\le \min\{1,C_* (\rho/L)^{1/4}\},
\quad
C_*=2^{3/4}e^{1/4}\pi^{-1/4}\Gamma(3/8).
}\tag{9}
\]

A completely elementary coarse bound sufficient for the global theorem is

\[
\boxed{C_*<25/6.}\tag{10}
\]

To verify it, the same alternating-Taylor/incomplete-tail estimate used by account03/B19 gives `Gamma(3/8)<5/2`. Also

\[
\left(2^{3/4}e^{1/4}\pi^{-1/4}\right)^4={8e\over\pi}
<{22\over3}<\left({5\over3}\right)^4,
\]

using `e<11/4` and `pi>3`. Thus the prefactor is `<5/3`, proving (10).

Since `e>8/3` implies `e^{3/2}>25/6`, we have `log C_*<3/2`. For `L>=1`, the manuscript's layer-cake computation therefore sharpens to

\[
\boxed{
\sup_a E\log_+{1\over|R-a|}
\le4+4\log C_*<10.
}\tag{11}
\]

## 5. Unconditional same-scope theorem constant: 3810

Keep the manuscript's `eta=1/100` and every original hypothesis.

For the nine-large-direction half-potential proposition:

- no pivot remains `<200` (and can separately be sharpened using (2));
- scalar pivot: the manuscript's exact kernel proof gives
  `H(Q)<=eta^{-1/2}(8+3 L_0)` with `L_0` the translated logarithmic-potential constant. By (11), `H(Q)<10(8+30)=380`;
- definite pair remains `<40 pi<380`;
- indefinite pair remains `<340<380` by the manuscript/B19 monotonicity calculation.

Adding the outside-distance-one contribution gives

\[
\boxed{
 s_9(A)\ge1\quad\Longrightarrow\quad
 \sup_a E|X^TAX+b^TX+c-a|^{-1/2}<381.
}\tag{12}
\]

Now run the manuscript's main `s_17` case split. In the scalar-pivot branch the Schur complement retains at least nine large directions, and the scalar square profile contributes `eta^{-1/2}=10`, so

\[
\|p_Q\|_\infty<3810.
\]

The no-pivot, definite-pair, and indefinite-pair branches are all below this value. Rescaling exactly as in the manuscript therefore proves

\[
\boxed{
 s_{17}(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3810\,{K^2\over s}.
}\tag{13}
\]

This improves the baseline `10000`, the preceding B18 `5338`, and the concurrent account03/B19 `3910`, without altering dimension, signs, remaining spectrum, affine terms, or the rough/non-iid product-law assumptions. It does not claim continuity in the pivot branches.

## 6. Prior-art scope check

Banks--Garza Vargas--Kulkarni--Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations* (arXiv:2005.08930), Theorem 2.1 and Corollary 2.4, prove strong density bounds for **bilinear-affine** forms

\[
X^T ZY+X^TU+V^TY+W
\]

of two independent random matrices with bounded entry densities. For scalar output (`k=1`), Corollary 2.4 already controls the law when at least two singular directions of `Z` are available. This is genuine prior art for the bilinear-affine subproblem.

It does **not** directly replace the manuscript's crossing theorem, because after a physical coordinate cut the full quadratic form has arbitrary same-bank phases `F(X_I)+G(X_J)`. Those phases disappear only after the manuscript's decoupling step, which introduces absolute Fourier factors; Theorem 2.1 of Banks et al. controls the signed bilinear-affine law and does not justify replacing the resulting absolute Fourier majorant by its characteristic function. I therefore found no source-valid implication from that theorem that closes the leverage-one order-four endpoint or lowers the unconditional multiplicity below 17.

Herry--Malicet--Poly's quadratic-form regularity theory assumes iid inputs with a sufficiently smooth Gaussian-field representation, so it does not match the present arbitrary rough, non-iid cap-one source class.

## 7. Remaining exact obstruction

The best current route to `17 -> 13` is now explicit: the manuscript already converts `s_13` into order-four crossing volume. Equations (3)--(7) close every such witness with a quantitative row-leverage gap. The only analytic survivor is the heavy-leverage endpoint where a required row has leverage arbitrarily close to one. The sharp completion counterexamples rule out resolving that survivor merely by replacing the global `3r` rank loss by `2r` or symmetrizing the interpolation matrix. A new physical-hub/curved-fiber receiver, or a product-preserving repartition theorem that creates a leverage gap while retaining order-four volume, is still required.

Full three-eigenvalue QFORM: **OPEN**.  
Full-target continuity: **OPEN**.  
Fixed-multiplicity `s_17` candidate: **PASS in this audit lineage, with same-scope constant sharpened to 3810**.
