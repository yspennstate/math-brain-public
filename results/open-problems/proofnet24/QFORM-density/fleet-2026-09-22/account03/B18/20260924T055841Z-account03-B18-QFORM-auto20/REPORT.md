SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-24T05:58:41Z.
attacking: a source-valid cross-bank plus Y-dependent moving-square receiver, so same-bank Y--W curvature can be retained instead of conditioned away.

# account03/B18 auto20 — cross bank plus moving diffuse square

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T055841Z-account03-B18-QFORM-auto20`  
Status: **NEW SUPPORTING THEOREM / CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN**.  
Native brain status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact theorem

### `QFORM-CROSS-MOVING-DIFFUSE-SQUARE-v1`

Let

- `X=(X_1,...,X_m)`, `Y=(Y_1,...,Y_n)`, and `Z=(Z_1,...,Z_k)` be three pairwise-disjoint banks of ORIGINAL coordinates;
- every coordinate in the three banks be independent and have a probability density bounded by one;
- `M` be a nonzero real `m x n` matrix, with `sigma=||M||_op>0`;
- `alpha in R^m`, `beta in R^k\{0}`, and `a!=0`;
- `G,H:R^n -> R` be arbitrary measurable functions.

Define

\[
T=X^TMY+\alpha^TX+G(Y)+a\bigl(\beta^TZ+H(Y)\bigr)^2.
\tag{1.1}
\]

Then `T` has a continuous density vanishing at infinity. More precisely, if

\[
K_\beta:=\|p_{\beta^TZ}\|_\infty,
\]

then

\[
\boxed{
\|p_T\|_\infty\le
{8K_\beta\over\sqrt{|a|\,\sigma}}.}
\tag{1.2}
\]

The sharp one-dimensional marginal estimate for cap-one product inputs gives

\[
K_\beta\le {\sqrt2\over\|\beta\|_2},
\]

hence

\[
\boxed{
\|p_T\|_\infty\le
{8\sqrt2\over
\|\beta\|_2\sqrt{|a|\,\sigma}}.}
\tag{1.3}
\]

If `Z` consists of a single original coordinate `W` and `beta=1`, its own density cap gives the sharper

\[
\boxed{
\|p_T\|_\infty\le {8\over\sqrt{|a|\,\sigma}}.}
\tag{1.4}
\]

The new point relative to this slot's earlier independent-square Lorentz endpoint is that the square center `H(Y)` is allowed to depend *arbitrarily* on the entire curved `Y` bank. Thus a genuine `Y--W` coupling can be completed into the square without destroying the proof.

## 2. Primary literature input and exact hypothesis match

The only external anti-concentration theorem needed is the one-dimensional case of the product-marginal theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. If a product probability density has one-dimensional factors bounded by one, every `d`-dimensional orthogonal marginal has density bounded by `2^(d/2)`. For `d=1`, if `c!=0`, this says

\[
\|p_{c^TX}\|_\infty\le {\sqrt2\over\|c\|_2}.
\tag{2.1}
\]

Equivalently one may use Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, arXiv:1402.4492 / IMRN 2015, for the same one-dimensional bounded-density consequence.

These results require independent original coordinates with bounded densities. They do **not** require Gaussianity, log-concavity, moments, compact support, connected support, identical laws, centering, symmetry, or smoothness. The proof below applies them only to genuine linear forms of the original product banks. No spectral rotation is followed by an independence assertion.

No exact published theorem matching the owner's full arbitrary-rough quadratic-form target was found in the primary sources checked; this report makes no novelty claim about the general target.

## 3. Conditional cross-bank density

For fixed `Y=y`, put

\[
c_y=My+\alpha.
\tag{3.1}
\]

Then the first three terms in (1.1) are

\[
R_y=c_y^TX+G(y).
\]

Whenever `c_y!=0`, (2.1) gives a conditional density `h_y` satisfying

\[
\|h_y\|_\infty\le K_X(y):={\sqrt2\over\|c_y\|_2}.
\tag{3.2}
\]

Choose top left/right singular vectors `u,v` of `M` so that

\[
u^TM=\sigma v^T.
\]

The scalar

\[
S=\sigma v^TY+u^T\alpha
\tag{3.3}
\]

has density cap

\[
\|p_S\|_\infty\le L:={\sqrt2\over\sigma}.
\tag{3.4}
\]

Since `u^Tc_Y=S`, we have `||c_Y||>=|S|`, and in particular `P(c_Y=0)=0`. Thus (3.2) is available almost surely.

## 4. A moving square from a disjoint source bank

Let

\[
V=\beta^TZ,
\qquad \|p_V\|_\infty=K_\beta.
\]

For fixed `Y=y`, the square term is

\[
W_y=a(V+H(y))^2.
\]

Translation of `V` does not change its density cap. Up to reflection when `a<0`, for `r>0` the pushforward density `g_y` obeys

\[
g_y(r)
\le {K_\beta\over\sqrt{|a|r}}.
\tag{4.1}
\]

Therefore its decreasing rearrangement satisfies

\[
\boxed{
g_y^*(t)\le {K_\beta\over\sqrt{|a|t}}}
\qquad(t>0),
\tag{4.2}
\]

uniformly in the moving center `H(y)`. Indeed, `{g_y>lambda}` is contained in an interval of length at most `K_beta^2/(|a| lambda^2)`.

Conditional on `Y=y`, the random variables `R_y` and `W_y` are independent because they use the disjoint original banks `X` and `Z`. Hence the conditional density of `T` is the convolution `h_y*g_y`, up to the already included output translation.

## 5. Exact half-Lorentz payment for a capped probability density

For every probability density `h` with `0<=h<=K`, its decreasing rearrangement maximizes

\[
\int_0^\infty t^{-1/2}h^*(t)\,dt
\]

by filling the earliest interval at height `K`. Thus the elementary bathtub principle gives

\[
\boxed{
\int_0^\infty t^{-1/2}h^*(t)\,dt\le 2\sqrt K.}
\tag{5.1}
\]

Hardy--Littlewood rearrangement, (4.2), and (5.1) imply, for almost every `y`,

\[
\begin{aligned}
\|h_y*g_y\|_\infty
&\le \int_0^\infty h_y^*(t)g_y^*(t)\,dt\\
&\le {K_\beta\over\sqrt{|a|}}
\int_0^\infty t^{-1/2}h_y^*(t)\,dt\\
&\le {2K_\beta\over\sqrt{|a|}}\sqrt{K_X(y)}.
\end{aligned}
\tag{5.2}
\]

This avoids first mixing over `Y`; the square and the cross linear form are convolved while their common center parameter is frozen.

## 6. The needed negative half-moment is finite at the exact scale

From (3.2)--(3.4),

\[
\sqrt{K_X(Y)}
=2^{1/4}\|c_Y\|^{-1/2}
\le2^{1/4}|S|^{-1/2}.
\tag{6.1}
\]

For any scalar probability density bounded by `L`, the bathtub principle against the symmetric decreasing kernel `|s|^{-1/2}` gives

\[
\mathbb E|S|^{-1/2}
\le 2\sqrt2\,\sqrt L.
\tag{6.2}
\]

With `L=sqrt(2)/sigma`,

\[
\mathbb E\sqrt{K_X(Y)}
\le 2^{1/4}\,2\sqrt2
\left({\sqrt2\over\sigma}\right)^{1/2}
={4\over\sqrt\sigma}.
\tag{6.3}
\]

Averaging (5.2) over the genuine original `Y` bank therefore yields

\[
\|p_T\|_\infty
\le {2K_\beta\over\sqrt{|a|}}
\,{4\over\sqrt\sigma}
={8K_\beta\over\sqrt{|a|\sigma}},
\]

which proves (1.2). Equation (1.3) follows from the one-dimensional product-marginal theorem applied to `beta^T Z`; (1.4) uses the original coordinate's sharper cap one.

## 7. Continuity

For almost every `y`, both `h_y` and `g_y` are `L^1` densities. Their convolution is therefore continuous and vanishes at infinity. The conditional sup bound in (5.2) is dominated by

\[
B(y)={2K_\beta\over\sqrt{|a|}}\sqrt{K_X(y)},
\]

and (6.3) shows `E B(Y)<infinity`. Consequently

\[
p_T(t)=\mathbb E[p_{T\mid Y}(t)]
\]

is continuous by dominated convergence. Applying the same domination as `|t|->infinity` shows `p_T(t)->0`. Thus this theorem supplies a continuous `C_0` representative in its stated scope.

## 8. Physical quadratic-form corollary: arbitrary Y--W coupling

Let `X`, `Y`, and one scalar original coordinate `W` be disjoint product sources. After conditioning arbitrary outside original coordinates, consider the physical packet

\[
Q=
2X^TCY+Y^TBY+2W h^TY+aW^2
+\alpha^TX+\gamma^TY+dW+c,
\tag{8.1}
\]

where `B,h,alpha,gamma,d,c` are arbitrary, `a!=0`, and there is **no** `X--W` coupling. Completing the square in `W` gives

\[
a\left(W+{h^TY+d/2\over a}\right)^2
+2X^TCY+G(Y)+\alpha^TX+c',
\tag{8.2}
\]

with all induced `Y` curvature absorbed into the arbitrary measurable function `G(Y)`.

Apply (1.4) with `M=2C`, so `sigma=2||C||_op`. Then

\[
\boxed{
\|p_Q\|_\infty
\le {4\sqrt2\over\sqrt{|a|\,\|C\|_{op}}}.}
\tag{8.3}
\]

The density has a continuous `C_0` representative. Arbitrary outside coefficients/couplings are permitted so long as conditioning them produces only the displayed affine coefficients in this retained packet. The restriction is the absent `X--W` cross block; an `X--W` anchor couples the two smoothing sources and requires a different receiver.

More generally, if the private square comes from a disjoint scalar aggregate `beta^T Z` and its physical square eigenvalue is

\[
\lambda=|a|\|\beta\|_2^2,
\]

then (1.3) and `sigma=2||C||_op` give the invariant-looking bank bound

\[
\boxed{
\|p_Q\|_\infty\le {8\over\sqrt{\lambda\,\|C\|_{op}}}.}
\tag{8.4}
\]

Thus a unit private square eigenvalue plus a unit cross singular value already gives a continuous density bounded by `8`, independently of how diffuse the corresponding original-coordinate banks are.

## 9. Required equation-level application of account04/B18

The designated partner result is account04/B18 r6,
`QFORM-TWOSIDED-ANCHOR-PAY-OR-RANK2-COLLAR-v1`, full report

`yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.

Its imported transverse receiver says, in its physical packet, if the top two singular values `c1,c2` of `P_r C` are nonzero, then

\[
\boxed{
\|p_Q\|_\infty\le {2\sqrt{2\pi}\over\sqrt{c_1c_2}}.}
\tag{9.1}
\]

Apply (9.1) and (8.3) to the same literal owner-target family. Let

\[
C_\varepsilon=\operatorname{diag}(1,\varepsilon),
\qquad 0<\varepsilon<1,
\]

and

\[
Q_{\varepsilon,\lambda}
=2X^TC_\varepsilon Y+\lambda W^2,
\qquad \lambda\ge1.
\tag{9.2}
\]

The physical symmetric matrix is

\[
A_{\varepsilon,\lambda}
=\begin{pmatrix}
0&C_\varepsilon&0\\
C_\varepsilon&0&0\\
0&0&\lambda
\end{pmatrix},
\]

with spectrum

\[
\{1,-1,\varepsilon,-\varepsilon,\lambda\}.
\tag{9.3}
\]

Hence for `0<epsilon<1` and `lambda>=1`, it has exactly three eigenvalues of modulus at least one (counting `lambda=1` as the third).

For the partner theorem `r=0`, `c1=1`, `c2=epsilon`, giving

\[
\|p_Q\|_\infty
\le {2\sqrt{2\pi}\over\sqrt\varepsilon}.
\tag{9.4}
\]

The new theorem has `||C_epsilon||_op=1` and gives

\[
\|p_Q\|_\infty
\le {4\sqrt2\over\sqrt\lambda}.
\tag{9.5}
\]

Therefore on the same target-valid matrix

\[
\boxed{
\|p_Q\|_\infty
\le
\min\left\{
{2\sqrt{2\pi}\over\sqrt\varepsilon},
{4\sqrt2\over\sqrt\lambda}
\right\}.}
\tag{9.6}
\]

At `epsilon=1/2` and `lambda=64`, the partner result gives

\[
4\sqrt\pi=7.0898154036220635\ldots,
\]

while the new moving-square receiver gives

\[
{\sqrt2\over2}=0.7071067811865476\ldots .
\]

The new branch is sharper exactly when

\[
\lambda>{4\varepsilon\over\pi}.
\tag{9.7}
\]

This is a direct application of the completed partner theorem to an actual common matrix, not a bibliographic comparison.

## 10. Corrections respected and remaining debt

This proof does not use any of the live refuted interfaces:

- no law-uniform pointwise van-der-Corput decay;
- no independence after spectral rotation;
- no arbitrary-joint quadratic coarea lemma;
- no conditional density cap promoted into independence;
- no naive fiber-sup integration;
- no deletion of a small nonzero coefficient;
- no fixed-good-minor consequence from `s_3(A)>=1`;
- no moments, support geometry, Gaussianity, log-concavity, or Monte Carlo extremality.

The unrestricted conjecture remains **OPEN / NOT PROVED**. This theorem pays a previously awkward one-sided-anchor packet with arbitrary `Y--W` coupling, but the bare spectral hypothesis `s_3(A)>=1` does not force a decomposition with zero `X--W` coupling, a nonzero scalar pivot `a`, and a uniformly large `||C||_op`. The latest account04/B18 reduction identifies the complementary difficult geometry as a near-rank-two two-sided cross carrier (or exact rank-one carrier with complement-active dimension at least three). The next structural step is to retain the `X--W` anchor exactly and combine this moving-square payment with the transverse rank-two/near-rank-two carrier machinery.

Continuity is proved for the theorem and physical branch above. Full-target continuity remains open.

## 11. Source pins

- Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1 (product marginal density bound).
- Rudelson--Vershynin, arXiv:1402.4492 / IMRN 2015(19), 9594--9617 (linear-image anti-concentration; compatible alternative source for the one-dimensional ingredient).
- account04/B18 r6: `yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.
- account03/B18 prior Lorentz endpoint, used only for comparison: path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T030202Z-account03-B18-QFORM-auto17/REPORT.md`.
