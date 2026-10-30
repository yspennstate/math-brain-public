# fleet01/B09 — moving-center cross-square absorption and exact light-cone rank-three reduction

Run: `20260922T154635Z-fleet01-B09-QFORM-r11`  
Assignment: `Bilinear block mechanism`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and status

The full conjecture remains OPEN. For every dimension, every independent real coordinates `X_i` with densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, one seeks one universal finite `C` such that

\[
\|p_{X^TAX}\|_\infty\le C,
\qquad
\Pr\{X^TAX\in I\}\le C|I|.
\]

Continuity of the density is tracked separately. No Gaussian, log-concave, compact-support, connected-support, post-rotation independence, or moment assumption is used below.

The live corrections consumed before this derivation include the failures of law-uniform pointwise quadratic-phase decay, conditional caps after sum/difference transforms, a rank-two cross block alone at `L^infinity`, a universal single physical Schur-pivot extraction, and a universal local-principal/rank-three-cross-cut dichotomy. The result below is a new exact payment rule for a previously unpaid *light-cone pivot* branch; it is not a global extraction theorem.

## 2. Named partner result actually used

The assigned partner is fleet02/B09. The newest completed handoff read in this run points to

- repository `yspennstate/math-open-problems`;
- commit `cdf0bb83a38fee4d20cd3fe29b6a4d03e89394bc`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T150741Z-fleet02-B09-QFORM-r3/REPORT.md`;
- result `QFORM-CROSS-SQUARE-COEFFICIENT-SIDE-ABSORPTION-v1`.

The partner result proves, for mutually independent coefficient-side object `Z`, scalar `V,W`, a scalar projection `U=u(Z)` of density cap `M_U`, and arbitrary measurable `H(Z)`,

\[
T_0=H(Z)+2\beta U V+\gamma W^2
\]

satisfies

\[
\boxed{
\|p_{T_0}\|_\infty
\le
4\sqrt2\,M_W\sqrt{M_UM_V}\,|\beta\gamma|^{-1/2}.
}\tag{2.1}
\]

Its proof uses the half-potential inequality

\[
\sup_s\mathbb E|s-Y|^{-1/2}\le2\sqrt{2M}
\quad\text{when }\|p_Y\|_\infty\le M.\tag{2.2}
\]

Equation (2.2) is applied twice below. The new theorem extends the partner's coefficient-side absorption to an arbitrary coefficient-dependent **moving center of the square variable**, with exactly the same constant.

## 3. Moving-center cross-square theorem

### Theorem 3.1 — `QFORM-CROSS-SQUARE-MOVING-CENTER-v1`

Let `Z,V,W` be mutually independent. Let `U=u(Z)` have a probability density bounded by `M_U`; let `V,W` have probability-density caps `M_V,M_W`. Let `H(Z)` and `eta(Z)` be arbitrary measurable real functions, and let `beta,gamma` be nonzero. Then

\[
T=H(Z)+2\beta U V+\gamma W^2+2\eta(Z)W
\tag{3.1}
\]

has a bounded continuous density and

\[
\boxed{
\|p_T\|_\infty
\le
4\sqrt2\,M_W\sqrt{M_UM_V}\,|\beta\gamma|^{-1/2}.
}\tag{3.2}
\]

Thus the partner constant (2.1) survives an arbitrary cross coupling from the whole coefficient-side bank into the square bank, as long as that coupling is linear in `W`.

#### Proof

Complete the square conditionally on `Z`:

\[
\gamma W^2+2\eta(Z)W
=
\gamma\left(W+\frac{\eta(Z)}\gamma\right)^2
-
\frac{\eta(Z)^2}{\gamma}.
\]

Put

\[
\widetilde H(Z)=H(Z)-\eta(Z)^2/\gamma,
\qquad
W_Z=W+\eta(Z)/\gamma.
\]

For every fixed `Z=z`, `W_Z` is a translate of `W`, hence has the same density cap `M_W`, and remains independent of `V` under that conditioning. The square transform therefore obeys

\[
p_{\gamma W_Z^2}(y)
\le M_W|\gamma|^{-1/2}|y|^{-1/2}
\]

on the appropriate half-line. Consequently, for `u=u(z)\ne0`,

\[
\begin{aligned}
p_{T\mid Z=z}(x)
&\le M_W|\gamma|^{-1/2}
\mathbb E_V|x-\widetilde H(z)-2\beta uV|^{-1/2}\\
&\le
2M_W|\gamma|^{-1/2}
\sqrt{\frac{M_V}{|\beta u|}},
\end{aligned}
\tag{3.3}
\]

where the second line is the partner half-potential inequality (2.2) applied to `2 beta u V`, whose density cap is `M_V/(2|beta u|)`. The event `U=0` has probability zero. Averaging (3.3) over `Z` and applying (2.2) again at center zero gives

\[
\mathbb E|U|^{-1/2}\le2\sqrt{2M_U},
\]

which proves (3.2).

For each `z` with `u(z)\ne0`, the conditional law is the convolution of two `L^1` densities and therefore has a continuous representative. The bound in (3.3) is independent of `x` and integrable in `z`; dominated convergence therefore shows that the mixture density is continuous. QED.

### Product-bank corollary

If `U,V,W` are normalized linear projections of three disjoint original-coordinate banks of cap-one product variables, the Livshyts--Paouris--Pivovarov marginal bound gives `M_U,M_V,M_W<=sqrt(2)`, and hence

\[
\boxed{
\|p_T\|_\infty\le 8\sqrt2\,|\beta\gamma|^{-1/2}.
}\tag{3.4}
\]

If `V` is a physical singleton, `M_V<=1`, so

\[
\boxed{
\|p_T\|_\infty\le 8\,2^{1/4}|\beta\gamma|^{-1/2}.
}\tag{3.5}
\]

The same constants give direct `O(|I|)` interval bounds.

## 4. Exact light-cone normal form for rank three

The moving-center theorem is relevant to the branch left open by the previous overlap-one Schur argument: a physical coordinate whose quadratic pivot vanishes by indefinite cancellation.

### Lemma 4.1 — `QFORM-RANK3-LIGHTCONE-CANONICAL-v1`

Let `A` be a real symmetric matrix of exact rank three. Fix a physical coordinate `i` satisfying

\[
A_{ii}=0,
\qquad
b:=A_{\bar i,i}\ne0.
\]

Set `beta=||b||_2` and `u=b/beta`. In an orthonormal decomposition of the residual physical coordinate space as

\[
\mathbb R^{n-1}=\operatorname{span}\{u\}\oplus u^\perp,
\]

write

\[
A_{\bar i,\bar i}
=
\begin{pmatrix}
c&d^T\\d&E\end{pmatrix}.
\tag{4.1}
\]

Then:

1. `rank(E)=1`; hence `E=gamma ww^T` for a unit `w in u^perp` and `gamma!=0`.
2. Decomposing `d=delta w+d_0` with `d_0 perp w`, the quadratic form is exactly

\[
Q
=2\beta U\left(
X_i+\frac{c}{2\beta}U+
\frac{\delta}{\beta}W+
\frac1\beta D_0
\right)
+\gamma W^2,
\tag{4.2}
\]

where `U=<u,X_{\bar i}>`, `W=<w,X_{\bar i}>`, and `D_0=<d_0,X_{\bar i}>` in these orthogonal residual coordinates.
3. If `lambda_1,lambda_2,lambda_3` are the three nonzero eigenvalues of `A`, then

\[
\boxed{
\lambda_1\lambda_2\lambda_3
=-\gamma\left(\beta^2+\|d_0\|_2^2\right).
}\tag{4.3}
\]

#### Proof

In the orthonormal coordinates `(X_i,U,z)` the matrix is

\[
\begin{pmatrix}
0&\beta&0\\
\beta&c&d^T\\
0&d&E
\end{pmatrix}.
\tag{4.4}
\]

The leading `2 x 2` block

\[
H=\begin{pmatrix}0&\beta\\\beta&c\end{pmatrix}
\]

is invertible and

\[
H^{-1}
=
\begin{pmatrix}-c/\beta^2&1/\beta\\1/\beta&0\end{pmatrix}.
\]

The coupling from the `z` coordinates into this block is `[0,d]^T`; because the bottom-right entry of `H^{-1}` is zero, its Schur correction is identically zero. Hence

\[
\operatorname{rank}A=2+\operatorname{rank}E.
\]

Since `rank A=3`, `rank E=1`, proving (1). Expanding the quadratic polynomial gives (4.2).

For (4.3), rotate orthogonally inside `u^perp` so that the first coordinate is `w` and write `d=delta w+d_0`. The third elementary symmetric polynomial of `A` is the sum of its principal `3 x 3` minors and, because `rank A=3`, equals the product of the three nonzero eigenvalues. The only nonzero principal `3 x 3` minors in these coordinates are

\[
-\beta^2\gamma
\]

from the coordinates `(X_i,U,W)`, and

\[
-\gamma d_{0,j}^2
\]

from `(U,W,z_j)` for each coordinate of `d_0`. Their sum is (4.3). QED.

Two useful consequences are

\[
\beta^2=(A^2)_{ii},
\tag{4.5}
\]

and, when `A=R\Lambda R^T` has exact rank three with `R^TR=I_3` and `|lambda_j|>=1`,

\[
\beta^2=r_i^T\Lambda^2r_i\ge\|r_i\|_2^2.
\tag{4.6}
\]

Thus a high-leverage physical coordinate that is exactly lightlike cannot also have a small linear coupling vector `b`.

## 5. A paid exact-rank-three light-cone branch

The canonical form exposes a precise product-structure condition under which the formerly unpaid light-cone branch is now uniformly controlled.

### Theorem 5.1 — `QFORM-LIGHTCONE-DISJOINT-SUPPORT-v1`

Assume the hypotheses of Lemma 4.1 and the target condition

\[
|\lambda_1|,|\lambda_2|,|\lambda_3|\ge1.
\]

Assume in addition that, in the original residual physical coordinates, the three orthogonal coefficient vectors `u`, `d_0` (if nonzero), and `w` are supported on pairwise disjoint coordinate banks. Then for every independent cap-one input law,

\[
\boxed{\|p_Q\|_\infty\le16.}\tag{5.1}
\]

Moreover `Q` has a continuous density, and every interval `I` satisfies

\[
\Pr\{Q\in I\}\le16|I|.
\tag{5.2}
\]

#### Proof

Let `L=||A||_{op}` and `r=||d_0||_2`. Since all three nonzero eigenvalues have modulus at least one,

\[
|\lambda_1\lambda_2\lambda_3|\ge L.
\tag{5.3}
\]

The canonical matrix has a row containing `beta` and `d_0`, so `L>=max(beta,r)`. Combining (4.3) and (5.3),

\[
|\gamma|(\beta^2+r^2)
\ge \max(\beta,r).
\]

If `R=max(beta,r)`, then `beta^2+r^2<=2R^2`, whence

\[
|\gamma|R\ge\frac12.
\tag{5.4}
\]

Therefore either

\[
|\beta\gamma|\ge\frac12
\quad\text{or}\quad
|r\gamma|\ge\frac12.
\tag{5.5}
\]

If the first alternative holds, take the coefficient-side bank to contain `U` and `D_0`, take `V=X_i` (a physical singleton), and take `W` from its disjoint support bank. In (4.2), the terms involving `cU^2+2UD_0` belong to `H(Z)` and the term `2delta UW` is the moving-center coupling. Equation (3.5) gives

\[
\|p_Q\|_\infty
\le8\,2^{1/4}|\beta\gamma|^{-1/2}
\le8\,2^{3/4}<13.455.
\tag{5.6}
\]

If instead `r>0` and the second alternative holds, write `D_0=rV_0` with `V_0` the unit projection of its disjoint bank. Put into the coefficient-side object `Z` both `X_i` and the `U` bank; then `H(Z)` may contain the entire term `2beta UX_i+cU^2`. The cross variable is `V_0`, the cross coefficient is `r`, and the square variable is `W`; again `2delta UW` is absorbed by the moving center. Now all three normalized bank projections have caps at most `sqrt(2)`, so (3.4) yields

\[
\|p_Q\|_\infty
\le8\sqrt2\,|r\gamma|^{-1/2}
\le16.
\tag{5.7}
\]

The two cases prove (5.1). Theorem 3.1 gives continuity in both cases. QED.

This theorem is not an easy definite subclass: it pays an exact-rank-three **indefinite light-cone pivot** where the diagonal scalar pivot is zero and the earlier Schur-complement theorem is unavailable.

## 6. What changed and what remains

New proved claims:

1. `QFORM-CROSS-SQUARE-MOVING-CENTER-v1`: the partner cross-square bound is stable under arbitrary coefficient-dependent translation of the square variable, with unchanged constant and continuity.
2. `QFORM-RANK3-LIGHTCONE-CANONICAL-v1`: every exact-rank-three zero-diagonal physical pivot has the exact hyperbolic-plus-rank-one normal form (4.2) and pseudodeterminant identity (4.3).
3. `QFORM-LIGHTCONE-DISJOINT-SUPPORT-v1`: under pairwise disjoint physical supports of the canonical orthogonal coefficient directions, the target branch has a continuous density bounded by `16`.

The first unpaid implication is now sharply localized:

> **`QFORM-LIGHTCONE-DEPENDENT-PROJECTION-BRIDGE-v1` (OPEN).** Remove the pairwise physical-support separation in Theorem 5.1. In the general light-cone canonical form, `U`, `D_0`, and `W` are orthogonal linear projections of the *same* cap-one product bank and therefore need not be independent. Prove that the moving-center cross-square estimate survives this product-projection dependence with one universal constant, or combine the current ridge/diffuse certificates with a source-valid partition argument that pays the overlap without conditioning on transformed coordinates.

This is exactly where post-rotation independence is forbidden. The new normal form shows that no other algebraic rank-three obstruction remains at an exact light-cone pivot: the outstanding issue is product-projection dependence.

The arbitrary-extra-spectrum target remains separate: Lemma 4.1 uses exact rank three. The full conjecture is therefore still OPEN / NOT PROVED / NOT DISPROVED.
