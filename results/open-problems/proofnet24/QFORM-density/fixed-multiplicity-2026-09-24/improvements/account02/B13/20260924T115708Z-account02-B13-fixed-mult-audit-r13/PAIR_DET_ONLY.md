# Three-eigenvalue physical-pair determinant receiver

Run: `20260924T115708Z-account02-B13-fixed-mult-audit-r13`

Status: **PROVED SUPPORTING THEOREM / FULL THREE-EIGENVALUE QFORM STILL OPEN**.

Source ingredients were independently audited in manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`: Schur spectral count, definite-pair change of variables, hyperbolic-pair envelope, and quarter-power logarithmic concentration.

## Theorem — `QFORM-3EIG-PHYSICAL-PAIR-DET-ONLY-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Let `A=A^T` satisfy `s_3(A)>=1`, and allow arbitrary affine terms `b^T X+c`. Fix distinct original coordinates `i,j`, let

\[
B=A[\{i,j\},\{i,j\}],\qquad D=|\det B|.
\]

If `D>0`, then the quadratic polynomial

\[
Q=X^TAX+b^TX+c
\]

has an essentially bounded density. More precisely, if `B` is definite,

\[
\|p_Q\|_\infty\le\pi D^{-1/2}.
\tag{1}
\]

If `B` is indefinite,

\[
\|p_Q\|_\infty
\le D^{-1/2}\left(6+\log_+(16\sqrt D)+L_0\right),
\qquad L_0=4+4\log16.
\tag{2}
\]

Consequently, in either signature,

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm pair}D^{-1/2}+e^{-1},
\qquad
C_{\rm pair}=10+5\log16=23.8629436111989\ldots .
}
\tag{3}
\]

### Proof

The definite case is the manuscript's two-dimensional elliptic change of variables after conditioning on all other original coordinates. Its bound is uniform in every induced affine term, so averaging preserves (1).

Now suppose `B` is indefinite. Condition on all coordinates outside `{i,j}` and complete the square only in the two physical pair variables. The conditional critical value is a quadratic polynomial `R` in the untouched coordinates whose quadratic matrix is the Schur complement `S=A/B`. Since `s_3(A)>=1` and the pivot has size two, the audited Schur spectral-count lemma gives

\[
N_S(1)\ge N_A(1)-2\ge1,
\]

hence `||S||>=1`. The quarter-power concentration lemma, valid for arbitrary affine terms and arbitrary rough cap-one product laws, therefore yields

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}\le L_0.
\tag{4}
\]

For a fixed outside configuration, the audited hyperbolic-pair lemma gives

\[
p_{Q\mid X_{-\{i,j\}}}(z)
\le
D^{-1/2}\left(
6+\log_+\frac{16\sqrt D}{|z-R|}
\right).
\]

Average and use `log_+(uv)<=log_+u+log_+v` together with (4), proving (2). Finally

\[
\log_+(16\sqrt D)\le\log16+\tfrac12\log_+D
\]

and

\[
\sup_{D>0}D^{-1/2}\log_+D=2/e.
\]

Thus the indefinite right side in (2) is at most

\[
(10+5\log16)D^{-1/2}+1/e.
\]

Since `C_pair>pi`, this also dominates the definite bound (1), proving (3). All conditioning is in original coordinates; the deterministic orthogonal basis used inside the two-dimensional coarea integral is not assigned probabilistic independence. QED.

## Corollary — quantitative collapse of every physical principal two-volume

Let `J` be any interval and put

\[
\rho=\frac{\Pr\{Q\in J\}}{|J|}.
\]

If `rho>1/e`, then every physical pair satisfies

\[
\boxed{
|A_{ii}A_{jj}-A_{ij}^2|
\le
\left(\frac{C_{\rm pair}}{\rho-e^{-1}}\right)^2.
}
\tag{5}
\]

Indeed, if the determinant is nonzero, interval domination by (3) gives

\[
\rho\le C_{\rm pair}D^{-1/2}+e^{-1},
\]

which rearranges to (5); if the determinant vanishes, (5) is automatic. Thus a hypothetical high-density sequence for the exact three-eigenvalue conjecture necessarily has **all original-coordinate principal `2x2` determinants collapsing as `O(rho^{-2})`**.

This is a coefficient obstruction only. It does not justify discarding the resulting small coefficients as a random quadratic perturbation on arbitrary unbounded/fragmented product laws.

## Designated-partner application: account03/B13 r50 is paid before heavy deletion

The latest completed compatible designated-partner report used here is account03/B13 r50, commit

`5ee01246ea47b42ea88c89f54c33e7520883ea21`,

which enters its non-ultracollapse packet with an original-coordinate **indefinite** principal pair satisfying

\[
D_B\ge D_0:=\frac{1001}{12544}.
\]

Theorem (3) therefore gives

\[
\rho
\le
\frac{10+5\log16}{\sqrt{1001/12544}}+\frac1e
=84.8422567126\ldots .
\tag{6}
\]

Partner r50 only invokes the subsequent heavy-Schur-row receiver for `rho>209.078`. Equation (6) excludes that high-ratio packet already at the physical pair. Thus the heavy-row deletion and second-heavy-row alternative are unnecessary in this branch once the audited determinant-only hyperbolic receiver is imported.

This does **not** solve the unrestricted three-eigenvalue conjecture. It removes a substantial physical-pair branch and sharpens the surviving obstruction to the all-pairs collapse (5).

## Sharpness check for the logarithm

Take independent `X,Y ~ Unif[-1/2,1/2]` and `Q=X^2-Y^2`. With `U=X-Y`, `V=X+Y`, the `(U,V)` density is `1/2` on `|U|+|V|<=1`. For `0<|z|<1/4`, direct product coarea gives

\[
p_Q(z)=\log\frac{1+\sqrt{1-4|z|}}{1-\sqrt{1-4|z|}}
=\log\frac1{|z|}+O(1)
\quad(z\to0).
\tag{7}
\]

Thus no determinant-only conditional `L^infty` bound can replace the logarithmic hyperbolic envelope. The surviving Schur direction in the three-eigenvalue theorem is exactly what makes the logarithm integrable after averaging.

## Pinned fifth-volume cross-check

The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves

\[
\|p_Q\|_\infty\le5\sqrt{2e}\,Z_5^{-1/10}
\]

for every physical cross block, without a volume-marginal condition. Combining this with the manuscript's no-pivot `s_17>=1` consequence `Z_5>=4^{-5}\kappa^5`, `\kappa=1/80^2`, gives

\[
\|p_Q\|_\infty\le800\sqrt{2e}=1865.31518528\ldots,
\]

an independent source-pinned check of the no-pivot density branch.

## First unpaid implication

`QFORM-PAIRDET-COLLAPSE-TO-NOPIVOT-RECEIVER-v1`: use (5) together with `s_3(A)>=1` to extract a dimension-free original-coordinate bank/crossing receiver, while preserving arbitrary fragmented/unbounded product supports and without interpreting small coefficients as a small random perturbation. A valid alternative is a genuine product-law counterexample satisfying the all-pairs `O(rho^{-2})` determinant collapse.
