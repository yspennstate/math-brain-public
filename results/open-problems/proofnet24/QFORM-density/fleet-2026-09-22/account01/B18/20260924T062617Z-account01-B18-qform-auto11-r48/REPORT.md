# account01/B18 r48 — Hilbert–Schmidt moving-square receiver with arbitrary same-bank remainder

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T062617Z-account01-B18-qform-auto11-r48`  
**Role:** literature-to-proof transfer  
**Status:** **PROVED SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
**Continuity:** proved in the theorem below; unrestricted QFORM continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T06:26:17Z.  
attacking: close account02/B18's named Hilbert–Schmidt moving-square-with-remainder gap by replacing the fixed-output-center half-Riesz step with a source-valid Gaussian-randomized negative-moment estimate.

## 1. Exact theorem

### `QFORM-CROSS-MOVING-DIFFUSE-SQUARE-HS-REMAINDER-v1`

Let `X in R^m`, `Y in R^n`, and `Z in R^k` be three pairwise-disjoint ORIGINAL-coordinate banks. Assume all their coordinates are mutually independent and each one-dimensional probability density is bounded by one. Let

- `M` be a nonzero real `m x n` matrix,
- `alpha in R^m`,
- `beta in R^k \ {0}`,
- `a != 0`,
- `G,H : R^n -> R` be arbitrary measurable functions.

Set

\[
T=X^TMY+\alpha^TX+G(Y)+a\bigl(\beta^TZ+H(Y)\bigr)^2.
\tag{1.1}
\]

Write

\[
K_\beta:=\|p_{\beta^TZ}\|_\infty,
\qquad H_M:=\|M\|_{HS}.
\]

Then `T` has a continuous density in `C_0(R)` and

\[
\boxed{
\|p_T\|_\infty\le {8K_\beta\over\sqrt{|a|H_M}}.
}
\tag{1.2}
\]

Rudelson–Vershynin Theorem 1.2 gives

\[
K_\beta\le {\sqrt2\over\|\beta\|_2},
\]

hence

\[
\boxed{
\|p_T\|_\infty\le
{8\sqrt2\over\|\beta\|_2\sqrt{|a|H_M}}.
}
\tag{1.3}
\]

If `Z` is one literal original coordinate `W` and `beta=1`, its original density cap one gives the sharper

\[
\boxed{
\|p_T\|_\infty\le {8\over\sqrt{|a|H_M}}.
}
\tag{1.4}
\]

The point is that `G(Y)` is completely arbitrary. Thus the Hilbert–Schmidt cross-energy gain survives a moving output center and arbitrary same-bank `Y` curvature/remainder; no projected coordinates sharing a source bank are declared independent.

## 2. Primary source and exact hypothesis match

The only external anti-concentration theorem used in the new step is Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, arXiv:1402.4492 / IMRN (2015), Theorem 1.2:

> if independent real variables have densities bounded by `K` and `sum a_j^2=1`, the density of `sum a_j X_j` is bounded by `sqrt(2) K`.

Therefore for every nonzero coefficient vector `b` and every cap-one ORIGINAL-coordinate product bank `U`,

\[
\boxed{
\|p_{b^TU}\|_\infty\le {\sqrt2\over\|b\|_2}.
}
\tag{2.1}
\]

No moments, iid assumption, support restriction, centering, symmetry, log-concavity, or smoothness is imported. The theorem is applied only before any source-mixing rotation, to genuine linear forms of original product banks.

As a scope check, Herry–Malicet–Poly's quadratic-form regularity theory assumes iid inputs whose common law is a sufficiently smooth function of a Gaussian field. That does not match the owner's arbitrary non-iid cap-one input class, so it is not used as a full-target theorem here.

## 3. Scalar negative half-moment from a density cap

If a scalar random variable `S` has a density bounded by `L`, then for every `c in R`, the bathtub principle against the symmetric decreasing kernel `|s-c|^{-1/2}` gives

\[
\boxed{
\mathbb E|S-c|^{-1/2}\le 2\sqrt{2L}.
}
\tag{3.1}
\]

Indeed, among all probability densities `0<=f<=L`, the integral is maximized by filling the interval of length `1/L` centered at `c` at height `L`, and

\[
L\int_{-1/(2L)}^{1/(2L)}|u|^{-1/2}\,du=2\sqrt{2L}.
\]

Combining (2.1) and (3.1), for every nonzero `b`, every `c`, and every cap-one product bank `U`,

\[
\boxed{
\mathbb E|b^TU-c|^{-1/2}
\le 2^{7/4}\|b\|_2^{-1/2}.
}
\tag{3.2}
\]

## 4. Gaussian randomization converts operator directions into Hilbert–Schmidt energy

### Lemma `QFORM-HS-NEGATIVE-HALF-MOMENT-v1`

For every nonzero real `m x n` matrix `M`, every `alpha in R^m`, and every cap-one original-coordinate product bank `Y in R^n`,

\[
\boxed{
\mathbb E\|MY+\alpha\|_2^{-1/2}
\le 2^{7/4}\|M\|_{HS}^{-1/2}.
}
\tag{4.1}
\]

### Proof

Let `g~N(0,I_m)` be an auxiliary Gaussian independent of everything, and put

\[
c_0:=\mathbb E|G|^{-1/2},\qquad G\sim N(0,1).
\]

For fixed `z in R^m`,

\[
\mathbb E_g|g^Tz|^{-1/2}=c_0\|z\|_2^{-1/2}.
\]

By Tonelli and (3.2), for Gaussian-a.e. `g` (those with `M^Tg!=0`),

\[
\begin{aligned}
c_0\,\mathbb E_Y\|MY+\alpha\|^{-1/2}
&=\mathbb E_g\mathbb E_Y
  |(M^Tg)^TY+g^T\alpha|^{-1/2}\\
&\le 2^{7/4}\mathbb E_g\|M^Tg\|^{-1/2}.
\end{aligned}
\tag{4.2}
\]

Let the nonzero singular values of `M` be `sigma_j`, let

\[
H_M=(\sum_j\sigma_j^2)^{1/2},
\qquad p_j={\sigma_j^2\over H_M^2},
\qquad \sum_jp_j=1.
\]

Then

\[
\mathbb E_g\|M^Tg\|^{-1/2}
=H_M^{-1/2}
\mathbb E\Bigl(\sum_jp_jG_j^2\Bigr)^{-1/4}.
\tag{4.3}
\]

For `t>=0`,

\[
\mathbb E e^{-t\sum_jp_jG_j^2}
=\prod_j(1+2tp_j)^{-1/2}
\le(1+2t)^{-1/2},
\tag{4.4}
\]

because

\[
\prod_j(1+2tp_j)\ge1+2t\sum_jp_j=1+2t.
\]

Using

\[
x^{-1/4}=\Gamma(1/4)^{-1}
\int_0^\infty t^{-3/4}e^{-tx}\,dt,
\]

(4.4) yields

\[
\mathbb E\Bigl(\sum_jp_jG_j^2\Bigr)^{-1/4}
\le \mathbb E|G|^{-1/2}=c_0.
\tag{4.5}
\]

Substitute (4.5) into (4.2) and cancel `c_0`; this is (4.1). QED.

The auxiliary Gaussian is only an integration device. It does not rotate the original random vector and it introduces no probabilistic independence assertion about spectral coordinates.

## 5. Conditional moving-square convolution

Fix `Y=y` and put

\[
c_y=My+\alpha.
\]

The cross/remainder part

\[
R_y=c_y^TX+G(y)
\]

has a density `h_y` with

\[
\|h_y\|_\infty\le
K_X(y):={\sqrt2\over\|c_y\|_2}
\tag{5.1}
\]

for a.e. `y`. The exceptional event `c_Y=0` has probability zero because `M!=0` and at least one nonzero linear functional of `Y` has an absolutely continuous law.

Let

\[
V=\beta^TZ,
\qquad \|p_V\|_\infty=K_\beta.
\]

For fixed `y`, the square

\[
W_y=a(V+H(y))^2
\]

has decreasing rearrangement satisfying

\[
\boxed{
g_y^*(t)\le {K_\beta\over\sqrt{|a|t}}}
\qquad(t>0),
\tag{5.2}
\]

uniformly in `H(y)`. Given `Y=y`, `R_y` and `W_y` use the disjoint original banks `X` and `Z`, hence are genuinely independent.

For any probability density `h` with `h<=K`,

\[
\int_0^\infty t^{-1/2}h^*(t)\,dt\le2\sqrt K.
\tag{5.3}
\]

Hardy–Littlewood rearrangement, (5.2), and (5.3) therefore give

\[
\|p_{T\mid Y=y}\|_\infty
\le {2K_\beta\over\sqrt{|a|}}\sqrt{K_X(y)}.
\tag{5.4}
\]

By (4.1),

\[
\begin{aligned}
\mathbb E\sqrt{K_X(Y)}
&=2^{1/4}\mathbb E\|MY+\alpha\|^{-1/2}\\
&\le 2^{1/4}2^{7/4}H_M^{-1/2}
=4H_M^{-1/2}.
\end{aligned}
\tag{5.5}
\]

Averaging (5.4) proves (1.2).

For a.e. `y`, `p_{T|Y=y}=h_y*g_y` is in `C_0(R)`. The right side of (5.4) is integrable in `y` by (5.5). Dominated convergence therefore shows that

\[
p_T(t)=\mathbb E[p_{T|Y}(t)]
\]

is continuous and vanishes at infinity. Thus the theorem supplies continuity in this exact source-preserving packet.

## 6. This closes the latest account02/B18 analytic remainder gap

The latest completed designated partner handoff, account02/B18 `account02-B18-20260924T060756Z-db964583`, proved `QFORM-HS-MOVING-DIFFUSE-SQUARE-v1` for the same packet **without** `G(Y)` and explicitly named

`QFORM-HS-MOVING-SQUARE-WITH-REMAINDER-OR-STRUCTURAL-EXIT-v1`

as its first remaining implication. Its Hilbert–Schmidt branch came from a fixed-output-center half-Riesz theorem, so an arbitrary `G(Y)` was not covered. The theorem above closes exactly the **analytic receiver** side of that implication: arbitrary measurable `G(Y)` is allowed, with the explicit universal constant `8` in (1.2). This does not supply the missing structural extraction of such a packet from an arbitrary three-large-eigenvalue matrix.

I make no publication-novelty claim. A targeted fleet/source search found no earlier artifact containing this exact HS-with-arbitrary-`G(Y)` estimate, but search absence is not novelty evidence.

## 7. Actual inequality from the completed account02/B18 result and new extension

The partner's target-valid family is

\[
Q_{N,\varepsilon,0}
=4\sqrt3 X_0Y_0
 +2\varepsilon\sum_{j=1}^N X_jY_j
 +3\bigl(\beta^TZ+\sqrt{2/3}Y_0\bigr)^2,
\tag{7.1}
\]

where `0<epsilon<1` and `||beta||_2=1`. Its explicit completed operator-norm branch gives

\[
\boxed{
\|p_{Q_{N,\varepsilon,0}}\|_\infty
\le {8\sqrt2\over\sqrt{12\sqrt3}}
=2.481612957605599\ldots .
}
\tag{7.2}
\]

This is the required direct equation-level use of the designated partner result.

Now add the previously unpaid same-bank remainder

\[
G(Y)=gY_0^2,
\qquad |g|\le1,
\]

and define

\[
Q_{N,\varepsilon,g}
=4\sqrt3 X_0Y_0
 +2\varepsilon\sum_{j=1}^N X_jY_j
 +gY_0^2
 +3\bigl(\beta^TZ+\sqrt{2/3}Y_0\bigr)^2.
\tag{7.3}
\]

Here

\[
M=\operatorname{diag}(4\sqrt3,2\varepsilon,\ldots,2\varepsilon),
\qquad
\|M\|_{HS}=2\sqrt{12+N\varepsilon^2},
\qquad a=3.
\]

Equation (1.3) yields

\[
\boxed{
\|p_{Q_{N,\varepsilon,g}}\|_\infty
\le
{8\over\sqrt3\,(12+N\varepsilon^2)^{1/4}}.
}
\tag{7.4}
\]

At `N=0`, (7.4) equals the partner's explicit bound (7.2). For every `N>0` it is strictly smaller than that explicit operator-norm certificate and decays like `(N epsilon^2)^(-1/4)` as diffuse cross energy grows. This comparison is only against the partner's explicit operator branch; its no-`G` Hilbert–Schmidt branch contains the unoptimized source constant `K_HP` and is not numerically compared.

### Target validity with the new remainder

On the core coordinates `(X_0,Y_0,beta^T Z)`, the physical matrix is

\[
A_g=
\begin{pmatrix}
0&2\sqrt3&0\\
2\sqrt3&2+g&\sqrt6\\
0&\sqrt6&3
\end{pmatrix}.
\tag{7.5}
\]

At `g=0`, its spectrum is exactly

\[
\{-3,2,6\}.
\]

The perturbation from `g=0` is `g e_2e_2^T`, with operator norm at most one. Weyl's inequality therefore places the three ordered core eigenvalues in

\[
[-4,-2],\qquad [1,3],\qquad [5,7].
\tag{7.6}
\]

Every remaining `(X_j,Y_j)` block has spectrum `{+epsilon,-epsilon}`. Hence for `0<epsilon<1` and `|g|<=1`, the full physical matrix has **exactly three eigenvalues of modulus at least one**. Thus (7.4) is a genuine owner-target family closure, now with the previously unpaid same-bank quadratic remainder retained exactly.

## 8. Scope and remaining implication

What is now paid:

- arbitrary rough/non-iid cap-one original-coordinate inputs;
- a full cross bank measured at Hilbert–Schmidt scale;
- arbitrary affine `alpha^T X`;
- arbitrary measurable same-bank remainder `G(Y)`;
- a moving square center `H(Y)` from a disjoint smoothing bank;
- continuous `C_0` density in this packet;
- no deletion of small nonzero crossing directions.

What remains for FULL QFORM is structural: starting from only `s_3(A)>=1`, force a product-preserving decomposition of this type with `|a| ||M||_HS` bounded below at a universal scale, or route failures into one of the already-paid physical-pair/ridge/grouped-hub/exterior-volume branches. The full universal density theorem and its unrestricted continuity statement remain **OPEN**.

## 9. Source pins actually used

- Rudelson–Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, arXiv:1402.4492 / IMRN 2015, Theorem 1.2.
- Account03/B18 moving-square conditional receiver/check: `QFORM-CROSS-MOVING-DIFFUSE-SQUARE-v1`, scientific commit `866968bafb00203a9892c46bf761dbb150d705cc`.
- Herry–Malicet–Poly, *Regularity of laws via Dirichlet forms — Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, used only for hypothesis-scope comparison.

No refuted arbitrary-joint coarea theorem, post-rotation independence, conditional-cap-as-independence, pointwise law-uniform Fresnel decay, fixed-good-minor inference, or deletion of a small nonzero quadratic tail is used.
